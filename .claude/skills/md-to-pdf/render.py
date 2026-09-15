#!/usr/bin/env python3
"""
render.py - convert a Markdown note (with LaTeX math) into a submission-ready PDF.

Pure Python: renders through matplotlib (Agg/PDF backends), which ships its own font
and layout code and needs no system libraries (no Pango/Cairo, no headless Chromium,
no LaTeX install). Built because none of those were available in this environment.

    python3 render.py IN.md --out OUT.pdf [options]

Options
  --out PATH           output PDF (required). With --split, this is the *combined*
                        PDF; per-problem PDFs are written alongside it.
  --split              also write one PDF per top-level numbered problem heading
                        (headings whose text matches --split-regex), into
                        <out-dir>/<out-stem>-problems/NN-slug.pdf. This is what
                        Crowdmark wants: "upload all pages corresponding to each
                        problem separately, in its designated location."
  --split-regex REGEX  what counts as a problem-starting heading (default: a
                        heading whose text begins with "<int>.", e.g. "1." or
                        "1. Urn with four balls" - matches this repo's ps/lecture
                        note convention and Crowdmark-style numbered questions)
  --header TEXT         a line printed small in the top-right of every page
                        (e.g. a name and student number) - optional but useful
                        since Crowdmark pages can get shuffled
  --page-size letter|a4 (default: letter - Crowdmark's / Queen's usual size)
  --font-size PT        body text size in points (default: 10.5)

Exit status is 0 on success. Unsupported Markdown constructs are rendered as
literal text with a note in stderr rather than silently dropped.
"""

import argparse
import re
import sys
import os
import unicodedata

import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
from matplotlib.backends.backend_pdf import PdfPages
from matplotlib.font_manager import FontProperties

# ---------------------------------------------------------------------------
# Page geometry (all in points, 72pt = 1 inch)

PAGE_SIZES = {
    "letter": (612.0, 792.0),
    "a4": (595.28, 841.89),
}
MARGIN = 60.0  # 5/6 inch all round - readable but not wasteful

# ---------------------------------------------------------------------------
# LaTeX preprocessing
#
# matplotlib's mathtext supports a real but limited subset of LaTeX. These
# substitutions cover the gap between "what these notes write" and "what
# mathtext accepts" - found by empirically probing every \command used across
# the filed notes in this repo (see the render.py development notes in the
# skill's SKILL.md for the probe results).

_SIMPLE_SUBS = [
    (re.compile(r"\\displaystyle\s*"), ""),
    (re.compile(r"\\textstyle\s*"), ""),
    (re.compile(r"\\tfrac\b"), r"\\frac"),
    (re.compile(r"\\dfrac\b"), r"\\frac"),
    (re.compile(r"\\ge(?![a-zA-Z])"), r"\\geq"),
    (re.compile(r"\\le(?![a-zA-Z])"), r"\\leq"),
    (re.compile(r"\\ne(?![a-zA-Z])"), r"\\neq"),
    (re.compile(r"\\iff\b"), r"\\Longleftrightarrow"),
    (re.compile(r"\\implies\b"), r"\\Longrightarrow"),
    (re.compile(r"\\impliedby\b"), r"\\Longleftarrow"),
    (re.compile(r"\\textbf\b"), r"\\mathbf"),
    (re.compile(r"\\textit\b"), r"\\mathit"),
    (re.compile(r"\\bm\b"), r"\\mathbf"),
]


def _find_matching_brace(s, open_pos):
    """s[open_pos] == '{'. Return index of the matching '}'."""
    assert s[open_pos] == "{"
    depth = 0
    for i in range(open_pos, len(s)):
        if s[i] == "{":
            depth += 1
        elif s[i] == "}":
            depth -= 1
            if depth == 0:
                return i
    raise ValueError(f"unbalanced braces in math: {s!r}")


def _replace_one_arg_with_subscript(s, cmdname):
    """Replace every \\cmdname{X}_{Y} with (X)_{Y} - the \\underbrace fallback.

    mathtext has no \\underbrace/\\overbrace; visually annotating with a
    subscript loses the brace glyph but keeps the (label, target) relationship
    readable, which is what matters for a homework submission.
    """
    marker = "\\" + cmdname + "{"
    out = []
    i = 0
    while True:
        j = s.find(marker, i)
        if j == -1:
            out.append(s[i:])
            break
        out.append(s[i:j])
        open_pos = j + len(marker) - 1
        close_pos = _find_matching_brace(s, open_pos)
        inner = s[open_pos + 1 : close_pos]
        rest = s[close_pos + 1 :]
        if rest.startswith("_{"):
            y_open = close_pos + 2
            y_close = _find_matching_brace(s, y_open)
            label = s[y_open + 1 : y_close]
            out.append(f"({inner})_{{{label}}}")
            i = y_close + 1
        elif rest.startswith("_") and len(rest) > 1:
            out.append(f"({inner})_{{{rest[1]}}}")
            i = close_pos + 1 + 2
        else:
            out.append(f"({inner})")
            i = close_pos + 1
    return "".join(out)


def split_boxed(latex):
    """Split a math string on top-level \\boxed{...} occurrences.

    Returns a list of (text, is_boxed) pairs, in order, with empty pieces
    dropped. mathtext has no \\boxed; a boxed segment is instead rendered as
    its own Text artist with a bbox rectangle around it (see draw_math_row).
    """
    marker = "\\boxed{"
    pieces = []
    i = 0
    while True:
        j = latex.find(marker, i)
        if j == -1:
            tail = latex[i:]
            if tail:
                pieces.append((tail, False))
            break
        head = latex[i:j]
        if head:
            pieces.append((head, False))
        open_pos = j + len(marker) - 1
        close_pos = _find_matching_brace(latex, open_pos)
        inner = latex[open_pos + 1 : close_pos]
        pieces.append((inner, True))
        i = close_pos + 1
    return pieces


def prep_math(latex):
    """Apply the simple substitutions and the \\underbrace fallback.

    \\boxed is handled separately by split_boxed, since it changes *drawing*
    (a box is added), not just the token stream.
    """
    s = latex
    for pat, repl in _SIMPLE_SUBS:
        s = pat.sub(repl, s)
    if "\\underbrace" in s:
        s = _replace_one_arg_with_subscript(s, "underbrace")
    if "\\overbrace" in s:
        s = _replace_one_arg_with_subscript(s, "overbrace")
    return s


# ---------------------------------------------------------------------------
# Low-level canvas: a matplotlib Figure/Axes used as a point-unit page, with
# y increasing downward from the top margin, like a document.


class Page:
    def __init__(self, width, height):
        self.fig = plt.figure(figsize=(width / 72.0, height / 72.0))
        self.ax = self.fig.add_axes([0, 0, 1, 1])
        self.ax.set_xlim(0, width)
        self.ax.set_ylim(0, height)
        self.ax.invert_yaxis()
        self.ax.axis("off")
        self.width = width
        self.height = height
        self._renderer = None

    def renderer(self):
        if self._renderer is None:
            self.fig.canvas.draw()
            self._renderer = self.fig.canvas.get_renderer()
        return self._renderer

    def measure(self, s, fontprops, ismath, size):
        """Measure s as it would actually be drawn at `size` points. fontprops'
        own .get_size() is ignored - the actual draw always passes fontsize=
        explicitly to ax.text, so measurement must match that, not whatever
        default size a bare FontProperties() carries (mismatch there is what
        caused headings to render as overlapping garbage during development)."""
        fp = fontprops.copy()
        fp.set_size(size)
        w, h, d = self.renderer().get_text_width_height_descent(s, fp, ismath)
        dpi_scale = 72.0 / self.fig.dpi
        return w * dpi_scale, h * dpi_scale, d * dpi_scale

    def invalidate(self):
        self._renderer = None


BODY_FONT = FontProperties(family="DejaVu Serif")
BOLD_FONT = FontProperties(family="DejaVu Serif", weight="bold")
ITALIC_FONT = FontProperties(family="DejaVu Serif", style="italic")
MONO_FONT = FontProperties(family="DejaVu Sans Mono")
HEADING_FONT = FontProperties(family="DejaVu Sans", weight="bold")


def font_for(style):
    return {
        "bold": BOLD_FONT,
        "italic": ITALIC_FONT,
        "code": MONO_FONT,
    }.get(style, BODY_FONT)


# ---------------------------------------------------------------------------
# Math row drawing: a full "$$...$$" line, or one row of an aligned/gathered
# block. Handles mid-expression \boxed by drawing boxed and unboxed segments
# as separate Text artists placed edge-to-edge.


def measure_math_row(page, latex, fontsize):
    """Return (total_width, max_height, max_descent, segments) without drawing,
    where segments is [(text_math, is_boxed, width, height, descent), ...]."""
    latex = prep_math(latex)
    segs = []
    total_w = 0.0
    max_h = 0.0
    max_d = 0.0
    for text, boxed in split_boxed(latex):
        s = f"${text}$"
        try:
            w, h, d = page.measure(s, BODY_FONT, True, fontsize)
        except Exception:
            s = f"$\\mathrm{{[unrenderable\\ math]}}$"
            w, h, d = page.measure(s, BODY_FONT, True, fontsize)
        pad = 6.0 if boxed else 0.0
        segs.append((text, boxed, w + 2 * pad, h, d))
        total_w += w + 2 * pad
        max_h = max(max_h, h)
        max_d = max(max_d, d)
    return total_w, max_h, max_d, segs


def draw_math_row(page, latex, x_start, y_top, fontsize, warnings):
    """Draw a math row with its left edge at x_start, top at y_top.
    Returns (width, height) actually used."""
    total_w, max_h, max_d, segs = measure_math_row(page, latex, fontsize)
    x = x_start
    for text, boxed, w, h, d in segs:
        s = f"${text}$"
        pad = 6.0 if boxed else 0.0
        try:
            if boxed:
                page.ax.text(
                    x + pad, y_top, s, fontsize=fontsize, va="top", ha="left",
                    bbox=dict(boxstyle="square,pad=0.35", edgecolor="black",
                              facecolor="none", linewidth=0.9),
                )
            else:
                page.ax.text(x + pad, y_top, s, fontsize=fontsize, va="top", ha="left")
        except Exception as e:
            warnings.append(f"unrenderable math segment {text!r}: {e}")
            page.ax.text(x + pad, y_top, "[math error]", fontsize=fontsize,
                          va="top", ha="left", color="red")
        x += w
    return total_w, max_h


# ---------------------------------------------------------------------------
# Inline run parsing: split one logical line of prose into styled runs.
# Runs: ("text", style) where style in {"plain","bold","italic","code","math"}


_INLINE_TOKEN = re.compile(
    r"(?P<math>\$[^$]+\$)"
    r"|(?P<code>`[^`]+`)"
    r"|(?P<bold>\*\*[^*]+\*\*)"
    r"|(?P<italic>\*[^*]+\*)"
)


def parse_inline(text):
    runs = []
    pos = 0
    for m in _INLINE_TOKEN.finditer(text):
        if m.start() > pos:
            runs.append((text[pos : m.start()], "plain"))
        kind = m.lastgroup
        val = m.group()
        if kind == "math":
            runs.append((val[1:-1], "math"))
        elif kind == "code":
            runs.append((val[1:-1], "code"))
        elif kind == "bold":
            runs.append((val[2:-2], "bold"))
        elif kind == "italic":
            runs.append((val[1:-1], "italic"))
        pos = m.end()
    if pos < len(text):
        runs.append((text[pos:], "plain"))
    # split plain/bold/italic runs into words (math/code stay atomic)
    words = []
    for val, style in runs:
        if style in ("math", "code"):
            words.append((val, style))
        else:
            parts = val.split(" ")
            for i, w in enumerate(parts):
                if w == "" and 0 < i < len(parts) - 1:
                    continue
                if w:
                    words.append((w, style))
                if i < len(parts) - 1:
                    words.append((" ", style))
    return words


# ---------------------------------------------------------------------------
# The document layout / pagination engine


class Layout:
    def __init__(self, width, height, header_text=None):
        self.width = width
        self.height = height
        self.header_text = header_text
        self.pages = []  # list of Page
        self.page = None
        self.y = MARGIN
        self.warnings = []
        self._new_page()

    def _new_page(self):
        if self.page is not None:
            self.pages.append(self.page)
        self.page = Page(self.width, self.height)
        if self.header_text:
            self.page.ax.text(
                self.width - MARGIN, MARGIN * 0.55, self.header_text,
                fontsize=8, ha="right", va="center", color="0.35",
            )
        self.y = MARGIN

    def finish(self):
        if self.page is not None:
            self.pages.append(self.page)
            self.page = None

    def ensure_space(self, needed):
        if self.y + needed > self.height - MARGIN:
            self._new_page()

    def force_page_break(self):
        if self.y > MARGIN:
            self._new_page()

    def advance(self, dy):
        self.y += dy

    @property
    def left(self):
        return MARGIN

    @property
    def right(self):
        return self.width - MARGIN

    @property
    def content_width(self):
        return self.width - 2 * MARGIN


LINE_GAP = 1.28  # line-height multiplier


def draw_wrapped_runs(layout, words, fontsize, x0, indent_hang=0.0):
    """Flow a list of (text, style) words within [x0, layout.right], wrapping
    on measured widths, buffering one visual line at a time so a tall inline
    element (e.g. $\\sum_{i=1}^n$) grows that line's height instead of
    overflowing into whatever comes after it."""
    page = layout.page
    base_h = fontsize * LINE_GAP
    max_x = layout.right
    start_x = x0 + indent_hang

    def measure_word(val, style):
        if style == "math":
            w, h, d, _ = measure_math_row(page, val, fontsize)
            return w, h, d
        if val == " ":
            sw, _, _ = page.measure(" ", BODY_FONT, False, fontsize)
            return sw, fontsize, 0.0
        fp = font_for(style)
        msize = fontsize * 0.95 if style == "code" else fontsize
        w, h, d = page.measure(val, fp, False, msize)
        return w, h, d

    def draw_word(px, py, val, style, w):
        if val == " ":
            return
        if style == "math":
            draw_math_row(page, val, px, py, fontsize, layout.warnings)
        elif style == "code":
            page.ax.text(px, py, val, fontsize=fontsize * 0.95, va="top",
                         ha="left", fontproperties=MONO_FONT,
                         bbox=dict(boxstyle="round,pad=0.15", edgecolor="0.6",
                                   facecolor="0.93", linewidth=0.5))
        else:
            page.ax.text(px, py, val, fontsize=fontsize, va="top",
                         ha="left", fontproperties=font_for(style))

    if not words:
        # nothing to lay out (e.g. a bare "2. " list marker with no text after
        # it) - still advance one line, or the next block silently overlaps
        # this one at the same y-coordinate.
        layout.ensure_space(base_h)
        layout.advance(base_h)
        return

    i = 0
    n = len(words)
    while i < n:
        # buffer one visual line: (val, style, x_offset, w)
        line = []
        x = start_x
        line_h = base_h
        while i < n:
            val, style = words[i]
            w, h, d = measure_word(val, style)
            if val != " " and x + w > max_x and x > start_x:
                break  # this word starts the next line
            line.append((val, style, x, w))
            if val != " ":
                line_h = max(line_h, h * LINE_GAP)
            x += w
            i += 1
        layout.ensure_space(line_h)
        page = layout.page  # ensure_space may have started a new page
        y = layout.y
        for val, style, xoff, w in line:
            draw_word(xoff, y, val, style, w)
        layout.advance(line_h)


def draw_paragraph(layout, text, fontsize=10.5, indent=0.0):
    words = parse_inline(text)
    draw_wrapped_runs(layout, words, fontsize, layout.left + indent)
    layout.advance(fontsize * 0.35)


def draw_heading(layout, level, text):
    sizes = {1: 17, 2: 14.5, 3: 12.5, 4: 11.5, 5: 10.5, 6: 10.5}
    fs = sizes.get(level, 11)
    layout.advance(fs * 0.5)
    layout.ensure_space(fs * LINE_GAP + fs * 0.3)
    words = parse_inline(text)
    # headings render in the heading font for plain runs, bold for bold, etc.
    styled = [(v, ("bold" if s == "plain" else s)) for v, s in words]
    page = layout.page
    x = layout.left
    space_w, _, _ = page.measure(" ", HEADING_FONT, False, fs)
    for val, style in styled:
        if val == " ":
            x += space_w
            continue
        if style == "math":
            w, h, d, _ = measure_math_row(page, val, fs)
            draw_math_row(page, val, x, layout.y, fs, layout.warnings)
        else:
            fp = HEADING_FONT if style == "bold" else font_for(style)
            w, h, d = page.measure(val, fp, False, fs)
            page.ax.text(x, layout.y, val, fontsize=fs, va="top", ha="left",
                         fontproperties=fp)
        x += w
    layout.advance(fs * LINE_GAP)
    if level <= 2:
        page.ax.plot([layout.left, layout.right],
                     [layout.y + 2, layout.y + 2], color="0.75", linewidth=0.7)
        layout.advance(6)
    layout.advance(fs * 0.25)


def draw_display_math_block(layout, rows, fontsize=11.5):
    """rows: list of raw LaTeX rows (already split on \\\\), each possibly
    containing an alignment '&'. Renders centered; if any row has '&', aligns
    all rows on that column like a LaTeX `aligned` environment."""
    page = layout.page
    has_align = any("&" in r for r in rows)

    if has_align:
        lefts, rights = [], []
        for r in rows:
            if "&" in r:
                l, _, rgt = r.partition("&")
            else:
                l, rgt = "", r
            lefts.append(l.strip())
            rights.append(rgt.strip())
        left_widths = []
        for l in lefts:
            if l:
                w, h, d, _ = measure_math_row(page, l, fontsize)
            else:
                w = 0.0
            left_widths.append(w)
        col_w = max(left_widths) if left_widths else 0.0
        row_heights = []
        for l, r in zip(lefts, rights):
            _, hl, dl, _ = measure_math_row(page, l, fontsize) if l else (0, fontsize, 0, [])
            wr, hr, dr, _ = measure_math_row(page, r, fontsize)
            row_heights.append(max(hl, hr, fontsize) * LINE_GAP)
        total_h = sum(row_heights)
        layout.ensure_space(total_h + 6)
        page = layout.page  # ensure_space may have started a new page
        y = layout.y
        amp_x = layout.left + layout.content_width / 2 - col_w / 2
        for (l, r, rh) in zip(lefts, rights, row_heights):
            if l:
                lw, lh, ld, _ = measure_math_row(page, l, fontsize)
                draw_math_row(page, l, amp_x - lw, y, fontsize, layout.warnings)
            if r:
                draw_math_row(page, r, amp_x + col_w + 8, y, fontsize, layout.warnings)
            y += rh
        layout.advance(total_h + 6)
    else:
        row_data = []
        for r in rows:
            w, h, d, _ = measure_math_row(page, r, fontsize)
            row_data.append((r, w, h))
        total_h = sum(h for _, _, h in row_data) * LINE_GAP + 6
        layout.ensure_space(total_h)
        page = layout.page  # ensure_space may have started a new page
        y = layout.y
        for r, w, h in row_data:
            cx = layout.left + layout.content_width / 2 - w / 2
            draw_math_row(page, r, cx, y, fontsize, layout.warnings)
            y += h * LINE_GAP
        layout.advance(total_h)
    layout.advance(fontsize * 0.3)


def draw_hr(layout):
    layout.advance(6)
    layout.ensure_space(6)
    page = layout.page
    page.ax.plot([layout.left, layout.right], [layout.y, layout.y],
                 color="0.7", linewidth=0.8)
    layout.advance(10)


def draw_blockquote(layout, lines, fontsize=10.5):
    text = " ".join(l.strip() for l in lines)
    words = parse_inline(text)
    styled = [(v, ("italic" if s == "plain" else s)) for v, s in words]
    page_before = layout.page
    y_before = layout.y
    draw_wrapped_runs(layout, styled, fontsize, layout.left + 14, indent_hang=14)
    y_after = layout.y
    if layout.page is page_before:
        # skip the decorative bar if the quote spanned a page break - a single
        # straight line can't meaningfully connect coordinates on two pages
        page_before.ax.plot([layout.left + 3, layout.left + 3],
                             [y_before - 2, y_after - fontsize * 0.35],
                             color="0.65", linewidth=2.2, solid_capstyle="butt")
    layout.advance(fontsize * 0.2)


def draw_list_item(layout, marker, text, fontsize=10.5, indent=0.0):
    layout.ensure_space(fontsize * LINE_GAP)
    page = layout.page  # after ensure_space, which may have started a new page
    mw, _, _ = page.measure(marker + " ", BODY_FONT, False, fontsize)
    page.ax.text(layout.left + indent, layout.y, marker, fontsize=fontsize,
                 va="top", ha="left", fontproperties=BODY_FONT)
    words = parse_inline(text)
    draw_wrapped_runs(layout, words, fontsize, layout.left + indent + mw,
                       indent_hang=0.0)


def draw_table(layout, rows, fontsize=9.5):
    """rows: list of list-of-cell-strings; rows[0] is the header."""
    page = layout.page
    ncols = max(len(r) for r in rows)
    rows = [r + [""] * (ncols - len(r)) for r in rows]
    col_w = [0.0] * ncols
    for r in rows:
        for c, cell in enumerate(r):
            words = parse_inline(cell)
            w = 0.0
            for val, style in words:
                if val == " ":
                    sw, _, _ = page.measure(" ", BODY_FONT, False, fontsize)
                    w += sw
                elif style == "math":
                    mw, _, _, _ = measure_math_row(page, val, fontsize)
                    w += mw
                else:
                    fp = font_for(style if style != "plain" else "bold" if r is rows[0] else "plain")
                    cw, _, _ = page.measure(val, fp, False, fontsize)
                    w += cw
            col_w[c] = max(col_w[c], w + 14)
    total_w = sum(col_w)
    scale = min(1.0, layout.content_width / total_w) if total_w > 0 else 1.0
    col_w = [w * scale for w in col_w]

    row_h = fontsize * LINE_GAP + 6
    for ridx, r in enumerate(rows):
        layout.ensure_space(row_h)
        page = layout.page
        x = layout.left
        y0 = layout.y
        is_header = ridx == 0
        for c, cell in enumerate(r):
            words = parse_inline(cell)
            styled = [(v, ("bold" if (is_header and s == "plain") else s)) for v, s in words]
            xr = x
            space_w, _, _ = page.measure(" ", BODY_FONT, False, fontsize)
            for val, style in styled:
                if val == " ":
                    xr += space_w
                    continue
                if style == "math":
                    w, h, d, _ = measure_math_row(page, val, fontsize)
                    draw_math_row(page, val, xr, y0, fontsize, layout.warnings)
                else:
                    fp = font_for(style)
                    w, h, d = page.measure(val, fp, False, fontsize)
                    page.ax.text(xr, y0, val, fontsize=fontsize, va="top",
                                 ha="left", fontproperties=fp)
                xr += w
            x += col_w[c]
        layout.y = y0
        layout.advance(row_h)
        page.ax.plot([layout.left, layout.left + sum(col_w)],
                     [layout.y - 3, layout.y - 3], color="0.8", linewidth=0.6)
        if is_header:
            page.ax.plot([layout.left, layout.left + sum(col_w)],
                         [layout.y - 3, layout.y - 3], color="0.3", linewidth=1.0)
    layout.advance(6)


# ---------------------------------------------------------------------------
# Block-level Markdown parsing


def strip_frontmatter(text):
    if text.startswith("---\n") or text.startswith("---\r\n"):
        end = text.find("\n---", 4)
        if end != -1:
            nl = text.find("\n", end + 1)
            return text[nl + 1 :] if nl != -1 else ""
    return text


def _looks_like_new_block(line):
    """True if `line` starts something other than a plain continuation of the
    current list item / paragraph: a heading, hr, blockquote, display-math
    opener, a fresh list marker, or a table row."""
    s = line.lstrip()
    if s == "":
        return True
    if re.match(r"^#{1,6}\s", s):
        return True
    if re.match(r"^(-{3,}|\*{3,})\s*$", s):
        return True
    if s.startswith(">"):
        return True
    if s.startswith("$$"):
        return True
    if re.match(r"^([-*+]|\d+\.)\s+", s):
        return True
    if s.startswith("|"):
        return True
    return False


def _consume_list_continuation(lines, i, n, text_parts):
    """Starting at line i, append any indented lines that continue the list
    item just opened (soft-wrapped source text with no marker of its own) to
    text_parts, in place. Returns the new value of i."""
    while i < n and lines[i].strip() != "" and not _looks_like_new_block(lines[i]) \
            and re.match(r"^\s", lines[i]):
        text_parts.append(lines[i].strip())
        i += 1
    return i


def parse_blocks(text):
    lines = text.split("\n")
    blocks = []
    i = 0
    n = len(lines)

    def is_blank(l):
        return l.strip() == ""

    while i < n:
        line = lines[i]
        if is_blank(line):
            i += 1
            continue

        m = re.match(r"^(#{1,6})\s+(.*)$", line)
        if m:
            blocks.append(("heading", len(m.group(1)), m.group(2).strip()))
            i += 1
            continue

        if re.match(r"^(-{3,}|\*{3,})\s*$", line):
            blocks.append(("hr",))
            i += 1
            continue

        if line.lstrip().startswith(">"):
            buf = []
            while i < n and lines[i].lstrip().startswith(">"):
                buf.append(re.sub(r"^\s*>\s?", "", lines[i]))
                i += 1
            blocks.append(("quote", buf))
            continue

        if line.strip().startswith("$$"):
            buf = []
            first = line.strip()[2:]
            if first.strip().endswith("$$") and len(first.strip()) > 2:
                buf.append(first.strip()[:-2])
                i += 1
            else:
                if first.strip():
                    buf.append(first)
                i += 1
                while i < n and "$$" not in lines[i]:
                    buf.append(lines[i])
                    i += 1
                if i < n:
                    tail = lines[i].split("$$")[0]
                    if tail.strip():
                        buf.append(tail)
                    i += 1
            blocks.append(("displaymath", buf))
            continue

        if line.lstrip().startswith("|") and "|" in line[1:]:
            buf = []
            while i < n and lines[i].lstrip().startswith("|"):
                buf.append(lines[i].strip())
                i += 1
            rows = []
            for r in buf:
                if re.match(r"^\|?[\s:|-]+\|?$", r):
                    continue
                cells = [c.strip() for c in r.strip("|").split("|")]
                rows.append(cells)
            if rows:
                blocks.append(("table", rows))
            continue

        m = re.match(r"^(\s*)([-*+])\s+(.*)$", line)
        if m:
            indent = len(m.group(1))
            text_parts = [m.group(3)]
            i += 1
            i = _consume_list_continuation(lines, i, n, text_parts)
            blocks.append(("listitem", "\u2022", " ".join(text_parts), indent))
            continue

        m = re.match(r"^(\s*)(\d+)\.\s+(.*)$", line)
        if m:
            indent = len(m.group(1))
            text_parts = [m.group(3)]
            i += 1
            i = _consume_list_continuation(lines, i, n, text_parts)
            blocks.append(("listitem", m.group(2) + ".", " ".join(text_parts), indent))
            continue

        m = re.match(r"^(\s{2,})(.*)$", line)
        base_indent = len(m.group(1)) if m else 0

        buf = [line.strip()]
        i += 1
        while i < n and not is_blank(lines[i]) and not re.match(r"^(#{1,6})\s", lines[i]) \
                and not lines[i].lstrip().startswith(">") and not lines[i].strip().startswith("$$") \
                and not re.match(r"^\s*([-*+]|\d+\.)\s+", lines[i]) \
                and not lines[i].lstrip().startswith("|"):
            buf.append(lines[i].strip())
            i += 1
        blocks.append(("para", " ".join(buf), base_indent))

    return _split_inline_display_math(blocks)


_DOLLAR_DOLLAR = re.compile(r"\$\$(.+?)\$\$")


def _split_inline_display_math(blocks):
    """A `$$...$$` span doesn't have to start its own line - "thus, $$...$$"
    is common in hand-written notes. The line-level detector above only
    catches $$ at the start of a line, so any block whose *text* payload
    still contains $$ (para/listitem/quote) gets split here into a sequence
    of para + displaymath blocks, reusing the same row-splitting/\\begin
    stripping that a real block-level $$ gets in render_blocks."""
    out = []
    for b in blocks:
        kind = b[0]
        if kind not in ("para", "listitem", "quote"):
            out.append(b)
            continue
        text = b[2] if kind == "listitem" else b[1]
        if "$$" not in text:
            out.append(b)
            continue
        pos = 0
        first = True
        for m in _DOLLAR_DOLLAR.finditer(text):
            pre = text[pos : m.start()].strip()
            if pre:
                if kind == "listitem" and first:
                    out.append(("listitem", b[1], pre, b[3]))
                elif kind == "quote":
                    out.append(("quote", [pre]))
                else:
                    out.append(("para", pre, b[2] if kind == "para" else 0))
            elif kind == "listitem" and first:
                # keep the marker even if there's no lead-in text before the math
                out.append(("listitem", b[1], "", b[3]))
            out.append(("displaymath", [m.group(1)]))
            pos = m.end()
            first = False
        tail = text[pos:].strip()
        if tail:
            if kind == "quote":
                out.append(("quote", [tail]))
            else:
                out.append(("para", tail, b[2] if kind == "para" else 0))
    return out


# ---------------------------------------------------------------------------
# Rendering a list of blocks into a Layout, with optional forced breaks at
# problem-numbering headings.


def render_blocks(layout, blocks, split_regex=None, on_split=None, fontsize=10.5):
    for b in blocks:
        kind = b[0]
        if kind == "heading":
            _, level, text = b
            if split_regex and level <= 4 and split_regex.match(text.strip()):
                if on_split:
                    on_split(text.strip())
            draw_heading(layout, level, text)
        elif kind == "para":
            _, text, indent = b
            draw_paragraph(layout, text, fontsize=fontsize, indent=indent * 0.6)
        elif kind == "listitem":
            _, marker, text, indent = b
            # a top-level numbered item ("2.", no heading markup at all) is a
            # common way to mark a new problem, same as a "## 2." heading -
            # watch for it too, or a document that mixes styles (one problem
            # under a heading, the next as a bare list item) loses the split.
            if split_regex and indent == 0 and split_regex.match(marker.strip()):
                if on_split:
                    on_split((marker + " " + text).strip())
            draw_list_item(layout, marker, text, fontsize=fontsize,
                            indent=14 + indent * 0.6)
        elif kind == "quote":
            _, buf = b
            draw_blockquote(layout, buf, fontsize=fontsize)
        elif kind == "hr":
            draw_hr(layout)
        elif kind == "displaymath":
            _, buf = b
            raw = "\n".join(buf)
            raw = re.sub(r"\\begin\{[a-zA-Z*]+\}", "", raw)
            raw = re.sub(r"\\end\{[a-zA-Z*]+\}", "", raw)
            rows = [r.strip() for r in raw.split("\\\\")]
            rows = [r for r in rows if r.strip()]
            if not rows:
                continue
            draw_display_math_block(layout, rows, fontsize=fontsize + 1)
        elif kind == "table":
            _, rows = b
            draw_table(layout, rows, fontsize=fontsize - 1)


# ---------------------------------------------------------------------------
# CLI


def slugify(text, maxlen=48):
    text = re.sub(r"\$[^$]*\$", "", text)
    text = unicodedata.normalize("NFKD", text).encode("ascii", "ignore").decode()
    text = re.sub(r"[^a-zA-Z0-9]+", "-", text).strip("-").lower()
    return text[:maxlen] or "section"


def main():
    ap = argparse.ArgumentParser(description=__doc__,
                                  formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("input")
    ap.add_argument("--out", required=True)
    ap.add_argument("--split", action="store_true")
    ap.add_argument("--split-regex", default=r"^\d+\.")
    ap.add_argument("--header", default=None)
    ap.add_argument("--page-size", choices=list(PAGE_SIZES), default="letter")
    ap.add_argument("--font-size", type=float, default=10.5)
    args = ap.parse_args()

    with open(args.input, encoding="utf-8") as f:
        raw = f.read()
    body = strip_frontmatter(raw)
    blocks = parse_blocks(body)

    width, height = PAGE_SIZES[args.page_size]
    layout = Layout(width, height, header_text=args.header)

    split_regex = re.compile(args.split_regex) if args.split else None
    problems = []  # (title, first_page_index)
    current = {"title": None, "start": 0}

    def on_split(title):
        current["title"] = title
        current["start"] = len(layout.pages)  # page count so far (0-indexed next page)
        layout.force_page_break()
        problems.append({"title": title, "start_page": len(layout.pages)})

    render_blocks(layout, blocks, split_regex=split_regex, on_split=on_split,
                  fontsize=args.font_size)
    layout.finish()

    os.makedirs(os.path.dirname(os.path.abspath(args.out)) or ".", exist_ok=True)
    with PdfPages(args.out) as pdf:
        for p in layout.pages:
            pdf.savefig(p.fig)
    n_pages = len(layout.pages)
    print(f"wrote {args.out}  ({n_pages} page{'s' if n_pages != 1 else ''})")

    if args.split and problems:
        out_dir = os.path.splitext(args.out)[0] + "-problems"
        os.makedirs(out_dir, exist_ok=True)
        for idx, prob in enumerate(problems):
            start = prob["start_page"]
            end = problems[idx + 1]["start_page"] if idx + 1 < len(problems) else n_pages
            fname = f"{idx+1:02d}-{slugify(prob['title'])}.pdf"
            fpath = os.path.join(out_dir, fname)
            with PdfPages(fpath) as pdf:
                for p in layout.pages[start:end]:
                    pdf.savefig(p.fig)
            print(f"  -> {fpath}  (pages {start+1}-{end})")

    if layout.warnings:
        print(f"\n{len(layout.warnings)} rendering warning(s):", file=sys.stderr)
        for w in layout.warnings[:20]:
            print(f"  - {w}", file=sys.stderr)

    for p in layout.pages:
        plt.close(p.fig)


if __name__ == "__main__":
    main()
