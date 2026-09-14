#!/usr/bin/env python3
"""
pdf_to_md.py - convert a PDF capture into Markdown for the course-notes repo.

Used by the `file-notes` skill so that nothing stays in a binary format: every
capture that lands in inbox/ ends up as Markdown that can be grepped, quizzed
from, and diffed in git.

    python3 pdf_to_md.py IN.pdf --out NOTE.md [options]

Options
  --out PATH          output markdown file (required)
  --assets DIR        extract embedded images here and reference them inline
                      (default: <out dir>/assets/<out stem>/)
  --no-assets         skip image extraction
  --split-outline     write one file per top-level PDF bookmark, plus an index
  --course SLUG       frontmatter: course
  --type TYPE         frontmatter: lecture | problem-set | summary | reference
  --date YYYY-MM-DD   frontmatter: date
  --tags a,b,c        frontmatter: tags
  --title TEXT        H1 title (default: derived from the filename)

Exit status is 0 on success. If the PDF has no extractable text layer the
script still writes a stub note, extracts the page images, and prints
NEEDS_OCR on stderr so the caller knows a vision/OCR pass is required.
"""

import argparse
import json
import os
import re
import sys

import pypdf

# ---------------------------------------------------------------------------
# TeX math-font repair
#
# Many TeX-produced PDFs (CLRS 4e is the example in this repo) embed subsetted
# math fonts whose ToUnicode CMap is wrong, so text extraction silently yields
# the wrong characters: "(n/3)(n/3) = n^2/9" comes out as ".n=3/.n=3/ D n 2 =9".
# Runs set in those fonts are detectable (the font dict has no /BaseFont), so we
# repair them in isolation and leave body text alone.
#
# Only mappings confirmed against surrounding prose are applied. Glyphs whose
# meaning depends on which subset font is active are left alone and reported, so
# the output is never confidently wrong.
# ---------------------------------------------------------------------------

MATH_GLYPH_MAP = {
    ".": "(",
    "/": ")",
    "=": "/",
    "D": "=",
    "C": "+",
    ";": ",",
    ":": ".",
    "\u0152": "[",          # OE ligature slot -> opening bracket
    "\u201a": "\\Theta ",
    "\u00b4": "z",
    "\u02db": "\\alpha ",
    "\u00a4": "\\neq ",
    "\u2740": "\\leadsto ",
    "\u0dc4": "\\le ",
}

# Glyphs that mean different things in different subset fonts. Passed through
# untouched and counted, rather than guessed at.
UNRESOLVED = re.compile(r"[\ue000-\uf8ff]")

# Per-font symbol table, keyed "<font object number>|<character>".
#
# The symbol fonts here are Type3: the glyphs are drawing programs with no names
# and no usable ToUnicode, and each chapter gets its own subset, so the same
# codepoint is a minus sign in one chapter and a multiplication sign in another.
# The only reliable identity is the rendered shape, so the map is built offline
# by rendering one instance of every (font, character) pair, clustering the
# images, and naming each cluster once. See SKILL.md, "Identifying symbol fonts".
GLYPH_MAP = {}

MATH_AMBIGUOUS = {
    "1": "1 or infinity",
    "(": "{ or (",
    "\u02da": "{ or phi",
    '"': "[ or similar",
    "#": "] or similar",
}

LIGATURES = {
    "\u00fb": "fi",        # broken fi ligature: "deûnitions" -> "definitions"
    "ﬁ": "fi", "ﬂ": "fl", "ﬀ": "ff", "ﬃ": "ffi", "ﬄ": "ffl",
    "’": "'", "‘": "'", "“": '"', "”": '"',
}


def repair_math(text, obj=None, state=None):
    """Apply the confirmed glyph map to a run of math-font text.

    U+FFFD is emitted for two different glyphs depending on the subset font:
    capital Omega and a closing square bracket. They are separable by context -
    Omega is essentially always applied to an argument ("Omega(n^2)"), while the
    bracket always closes an index opened earlier in the same run ("A[j]").
    """
    if state is None:
        state = {"depth": 0}
    out = []
    for i, ch in enumerate(text):
        mapped = GLYPH_MAP.get(f"{obj}|{ch}") if obj is not None else None
        if mapped is not None:
            out.append(mapped)
            continue
        if ch == "\ufffd":
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if state["depth"] > 0 and nxt not in (".", "-"):
                out.append("]")
                state["depth"] -= 1
            elif nxt in (".", "(", "-"):
                out.append("\\Omega ")
            else:
                out.append(ch)
            continue
        if ch == "!":
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if nxt == "-":                  # "!-notation" -> omega-notation
                out.append("\\omega ")
                continue
            if nxt == "1":                  # "n!1" -> n \to \infty
                out.append("\\to \\infty ")
                skip = True
                out.append("\x00")         # marker consumed below
                continue
        if out and out[-1] == "\x00":
            out.pop()                       # drop the "1" that meant infinity
            continue
        if UNRESOLVED.match(ch):
            out.append("{?}")               # symbol we cannot identify - see note
            continue
        if ch in ("\u0152", "["):          # bracket glyph, or a literal one
            state["depth"] += 1
        out.append(MATH_GLYPH_MAP.get(ch, ch))
    return "".join(out).replace("\x00", "")


def is_math_font(font_dict):
    """Subsetted TeX math fonts carry no /BaseFont; body fonts do."""
    return bool(font_dict) and not font_dict.get("/BaseFont")


def clean_body(text):
    for a, b in LIGATURES.items():
        text = text.replace(a, b)
    return text


# ---------------------------------------------------------------------------
# Extraction
# ---------------------------------------------------------------------------

def page_tokens(page):
    """Collect positioned text runs for one page: (is_math, text, size, baseline)."""
    toks = []

    def visitor(text, cm, tm, font_dict, font_size):
        if not text:
            return
        ref = getattr(font_dict, "indirect_reference", None) if font_dict else None
        toks.append({"math": is_math_font(font_dict), "text": text,
                     "space": not text.strip(), "obj": ref.idnum if ref else None,
                     "size": float(font_size or 0), "y": round(tm[5], 1)})

    try:
        page.extract_text(visitor_text=visitor)
    except Exception as exc:
        return [{"math": False, "text": f"extraction failed: {exc}",
                 "space": False, "obj": None, "size": 0, "y": 0}]
    return toks


QUOTE_PAIR = re.compile(r"<([^<>=\n]{1,120}?)=")


def escape_body(text):
    """Make body prose safe for a Markdown renderer.

    The PDF uses '<' and '=' as its opening/closing curly-quote glyphs, so raw
    output contains things like '<big-oh of g of n='. A Markdown renderer reads
    that as an unclosed HTML tag and swallows the rest of the document, which is
    the single worst rendering failure in a converted chapter.
    """
    for a, b in LIGATURES.items():
        text = text.replace(a, b)
    text = QUOTE_PAIR.sub(r'"\1"', text)        # paired quote glyphs
    text = text.replace("/ /", "//")            # split comment marker
    text = text.replace("<", "&lt;").replace(">", "&gt;")
    return text


def render_math(group, base_size):
    """Join consecutive math runs into one LaTeX expression.

    Superscripts and subscripts are recoverable: they are set smaller than body
    text AND shifted off the baseline, which distinguishes them from small caps
    (smaller, but on the same baseline). Consecutive runs at the same level are
    merged so that "r", "n", "-", "1" becomes r_{n-1} rather than r_{n}_{-}_{1}.
    """
    full = [t["y"] for t in group
            if not t["space"] and (not base_size or t["size"] >= 0.8 * base_size)]
    base_y = max(set(full), key=full.count) if full else \
        min((t["y"] for t in group), default=0)

    levelled = []
    state = {"depth": 0}
    for t in group:
        body = repair_math(t["text"], t.get("obj"), state)
        if t["space"]:
            levelled.append((None, " "))
            continue
        small = base_size and t["size"] and t["size"] < 0.8 * base_size
        if small and t["y"] > base_y + 1:
            levelled.append(("^", body.strip()))
        elif small and t["y"] < base_y - 1:
            levelled.append(("_", body.strip()))
        else:
            levelled.append((None, body))

    out, i = [], 0
    while i < len(levelled):
        lvl, txt = levelled[i]
        if lvl is None:
            out.append(txt)
            i += 1
            continue
        j, parts = i, []
        while j < len(levelled) and levelled[j][0] == lvl:
            parts.append(levelled[j][1])
            j += 1
        out.append(lvl + "{" + "".join(parts) + "}")
        i = j

    expr = re.sub(r"\s{2,}", " ", "".join(out)).strip()
    expr = re.sub(r"\s+([\^_]\{)", r"\1", expr)
    expr = re.sub(r"(\})\s+(?=[)\],./])", r"\1", expr)
    expr = re.sub(r"(\\[A-Za-z]+)\s+(?=[(\[])", r"\1", expr)
    expr = re.sub(r"([(\[])\s+", r"\1", expr)
    expr = re.sub(r"\s+([)\]])", r"\1", expr)
    expr = expr.replace("<", r"\lt ").replace(">", r"\gt ")
    expr = expr.replace("/ /", "//")
    return re.sub(r"\s{2,}", " ", expr).strip()


def render_page(page, repair=True):
    """Return (markdown, ambiguous_counter) for one page."""
    toks = page_tokens(page)
    if not toks:
        return "", {}

    sizes = [t["size"] for t in toks if not t["math"] and t["size"]]
    base_size = max(set(sizes), key=sizes.count) if sizes else 0

    ambiguous, out, i = {}, [], 0
    while i < len(toks):
        if toks[i]["math"] and not toks[i]["space"] and repair:
            j = i
            while j < len(toks):
                if toks[j]["math"] and not toks[j]["space"]:
                    for ch in toks[j]["text"]:
                        if GLYPH_MAP.get(f"{toks[j].get('obj')}|{ch}"):
                            continue
                        if ch in MATH_AMBIGUOUS or UNRESOLVED.match(ch):
                            key = "{?}" if UNRESOLVED.match(ch) else ch
                            ambiguous[key] = ambiguous.get(key, 0) + 1
                    j += 1
                elif toks[j]["space"]:
                    nxt = next((k for k in range(j + 1, len(toks))
                                if not toks[k]["space"]), None)
                    if nxt is None or not toks[nxt]["math"]:
                        break
                    j += 1
                else:
                    break
            trailing = " " if toks[j - 1]["space"] else ""
            expr = render_math(toks[i:j], base_size).strip()
            if expr:
                # bare punctuation is not worth a math span
                out.append((expr if not re.search(r"[A-Za-z0-9\\]", expr)
                            else f"${expr}$") + trailing)
            i = j
        else:
            chunk = escape_body(toks[i]["text"])
            smallcap = (not toks[i]["space"] and base_size and toks[i]["size"]
                        and toks[i]["size"] < 0.95 * base_size
                        and toks[i]["text"][:1].isupper())
            if smallcap and out and out[-1].endswith(" ") \
                    and out[-1].rstrip()[-1:].isupper():
                out[-1] = out[-1].rstrip()
            out.append(chunk)
            i += 1

    text = "".join(out)
    text = re.sub(r"\$\s*\$", "", text)
    text = re.sub(r"(?<=\S)\$(\w)", r" $\1", text)
    return text, ambiguous


HEAD_RUNNING = re.compile(
    r"^\s*(?:\d{1,4}\s+)?(?:Chapter\s+\d+|Part\s+[IVX]+|Appendix\s+[A-D])\b.*$|"
    r"^\s*\d{1,4}\s*$|^\s*\d+\.\d+\s+.{0,70}?\s+\d{1,4}\s*$",
    re.IGNORECASE)


def strip_running_heads(pages):
    """Drop page numbers and running heads from the top of each page."""
    firsts = {}
    for t in pages:
        line = t.strip().split("\n", 1)[0].strip() if t.strip() else ""
        key = re.sub(r"\d+", "#", line)
        if key:
            firsts[key] = firsts.get(key, 0) + 1
    common = {k for k, n in firsts.items() if n > max(3, len(pages) * 0.15)}
    out = []
    for t in pages:
        if not t.strip():
            out.append(t)
            continue
        head, _, rest = t.strip().partition("\n")
        if HEAD_RUNNING.match(head.strip()) or \
                re.sub(r"\d+", "#", head.strip()) in common:
            out.append(rest)
        else:
            out.append(t)
    return out


SECTION_BREAKS = [
    (re.compile(r"(?<![\w.-])Exercises\s+(\d+\.\d+)(?![\w-])"),
     r"\n\n#### Exercises \1\n"),
    (re.compile(r"(?<![\w.$-])(\d+\.\d+-\d+)\s"), r"\n\n**\1** "),
    (re.compile(r"(?<![\w.$-])\?\s*(\d+\.\d+-\d+)\s"), r"\n\n**\1 (starred)** "),
]


PSEUDO_HEAD = re.compile(
    r"([A-Z][A-Z0-9]*(?:-[A-Z0-9]+)*)\s*(\$\([^$]*\)\$)\s+1\s")


def find_pseudocode(text, start):
    """Return (end_index, [lines]) for a numbered algorithm listing, or None.

    CLRS prints algorithms as numbered lines, which flatten into the paragraph
    stream as "... 1 for i = 2 to n 2 key = A[i] 3 // ...". The line numbers run
    1, 2, 3, ... in order, so walking that sequence recovers the listing.
    """
    lines, pos, n = [], start, 2
    while True:
        nxt = text.find(f" {n} ", pos, pos + 420)
        if nxt == -1:
            break
        lines.append(text[pos:nxt].strip())
        pos = nxt + len(f" {n} ")
        n += 1
    if len(lines) < 2:
        return None
    span = min(110, int(max(len(x) for x in lines) * 1.4) + 10)
    tail = text[pos:pos + span]
    cut = tail.find(". ")
    if cut != -1:
        last = tail[:cut + 1]
    else:                                   # don't cut in the middle of a word
        last = tail[:tail.rfind(" ")] if " " in tail else tail
    lines.append(last.strip())
    return pos + len(last), lines


def extract_pseudocode(text):
    """Turn flattened algorithm listings back into numbered lists."""
    out, pos = [], 0
    while True:
        m = PSEUDO_HEAD.search(text, pos)
        if not m:
            out.append(text[pos:])
            break
        found = find_pseudocode(text, m.end())
        if not found:
            out.append(text[pos:m.end()])
            pos = m.end()
            continue
        end, lines = found
        out.append(text[pos:m.start()])
        out.append(f"\n\n**{m.group(1)}{m.group(2)}**\n\n")
        for i, ln in enumerate(lines, 1):
            out.append(f"{i}. {ln}\n")
        out.append("\n")
        pos = end
    return "".join(out)


def add_structure(text):
    """Break the flat text stream into navigable Markdown sections."""
    for pattern, repl in SECTION_BREAKS:
        text = pattern.sub(repl, text)
    return extract_pseudocode(text)


def unwrap(text):
    """Join hard-wrapped lines into paragraphs, keeping blank-line breaks."""
    text = re.sub(r"-\n(\w)", r"\1", text)
    paras = re.split(r"\n\s*\n", text)
    cleaned = []
    for para in paras:
        para = re.sub(r"\s*\n\s*", " ", para).strip()
        para = re.sub(r"[ \t]{2,}", " ", para)
        if para:
            cleaned.append(para)
    return "\n\n".join(cleaned)


def extract_images(reader, assets_dir, rel_prefix):
    """Write embedded rasters to assets_dir. Returns {page_index: [md_refs]}."""
    os.makedirs(assets_dir, exist_ok=True)
    by_page, seen, n = {}, set(), 0
    for i, page in enumerate(reader.pages):
        refs = []
        try:
            images = list(page.images)
        except Exception:
            images = []
        for img in images:
            try:
                data = img.data
            except Exception:
                continue
            if len(data) < 3000:                    # skip icons/bullets/rules
                continue
            digest = hash(data)
            if digest in seen:
                continue
            seen.add(digest)
            n += 1
            ext = os.path.splitext(img.name)[1].lower() or ".png"
            fname = f"p{i + 1:03d}-{n:02d}{ext}"
            target = os.path.join(assets_dir, fname)
            if ext in (".tif", ".tiff", ".jp2", ".bmp"):
                # not web-displayable; re-encode so the Markdown actually renders
                try:
                    fname = f"p{i + 1:03d}-{n:02d}.png"
                    target = os.path.join(assets_dir, fname)
                    img.image.save(target, "PNG", optimize=True)
                except Exception:
                    fname = f"p{i + 1:03d}-{n:02d}{ext}"
                    target = os.path.join(assets_dir, fname)
                    with open(target, "wb") as fh:
                        fh.write(data)
            else:
                with open(target, "wb") as fh:
                    fh.write(data)
            refs.append(f"![figure from page {i + 1}]({rel_prefix}/{fname})")
        if refs:
            by_page[i] = refs
    return by_page, n


# ---------------------------------------------------------------------------
# Output
# ---------------------------------------------------------------------------

def frontmatter(args, extra=None):
    lines = ["---"]
    if args.course:
        lines.append(f"course: {args.course}")
    if args.type:
        lines.append(f"type: {args.type}")
    if args.date:
        lines.append(f"date: {args.date}")
    if args.tags:
        tags = ", ".join(t.strip() for t in args.tags.split(",") if t.strip())
        lines.append(f"tags: [{tags}]")
    for k, v in (extra or {}).items():
        lines.append(f"{k}: {v}")
    lines.append("---")
    return "\n".join(lines)


def outline_chapters(reader):
    """[(title, first_page_index)] for top-level bookmarks, in page order."""
    items = []

    def walk(node, depth):
        for entry in node:
            if isinstance(entry, list):
                walk(entry, depth + 1)
            elif depth <= 1:
                try:
                    items.append((entry.title.strip(),
                                  reader.get_destination_page_number(entry)))
                except Exception:
                    pass

    try:
        walk(reader.outline, 0)
    except Exception:
        return []
    items.sort(key=lambda x: x[1])
    return items


def all_outline_entries(reader):
    """{page_index: [section titles starting on that page]} for every depth."""
    found = {}

    def walk(node, depth):
        for entry in node:
            if isinstance(entry, list):
                walk(entry, depth + 1)
            elif depth >= 1:                    # depth 0 == the chapter itself
                try:
                    pg = reader.get_destination_page_number(entry)
                except Exception:
                    continue
                found.setdefault(pg, []).append(entry.title.strip())

    try:
        walk(reader.outline, 0)
    except Exception:
        return {}
    return found


def insert_heading(page_md, title):
    """Promote a section title to a Markdown heading inside a page's text.

    The outline title and the extracted text rarely match character for character
    (the outline says "3.1 O-notation, Omega-notation" while the text carries
    repaired LaTeX), so anchor on the section number, which is stable.
    """
    level = "###" if re.match(r"^\d+\.\d+", title) else "##"
    heading = f"\n\n{level} {title}\n\n"
    num = re.match(r"^(\d+\.\d+|[A-D]\.\d+)\s", title)
    if num:
        anchor = re.search(r"(?<![\w.-])" + re.escape(num.group(1)) + r"\s+\S",
                           page_md)
        if anchor:
            return page_md[:anchor.start()] + heading + page_md[anchor.start():]
    idx = page_md.find(title[:40])
    if idx != -1:
        return page_md[:idx] + heading + page_md[idx:]
    return heading.lstrip() + page_md


def slugify(text):
    s = re.sub(r"[^a-z0-9]+", "-", text.lower()).strip("-")
    return re.sub(r"-{2,}", "-", s)[:60] or "section"


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--out", required=True)
    ap.add_argument("--assets")
    ap.add_argument("--no-assets", action="store_true")
    ap.add_argument("--split-outline", action="store_true")
    ap.add_argument("--course")
    ap.add_argument("--type")
    ap.add_argument("--date")
    ap.add_argument("--tags")
    ap.add_argument("--title")
    ap.add_argument("--no-repair", action="store_true")
    ap.add_argument("--glyph-map",
                    help="JSON symbol table for this PDF's Type3 fonts; defaults "
                         "to <pdf>.glyphs.json beside the source if present")
    args = ap.parse_args()

    gm = args.glyph_map or os.path.splitext(args.pdf)[0] + ".glyphs.json"
    if os.path.exists(gm):
        GLYPH_MAP.update(json.load(open(gm, encoding="utf-8")))
        print(f"glyph map: {len(GLYPH_MAP)} entries from {os.path.basename(gm)}")

    reader = pypdf.PdfReader(args.pdf)
    out_dir = os.path.dirname(os.path.abspath(args.out)) or "."
    stem = os.path.splitext(os.path.basename(args.out))[0]
    os.makedirs(out_dir, exist_ok=True)

    title = args.title or stem.replace("-", " ").title()

    # --- text -------------------------------------------------------------
    raw, ambiguous = [], {}
    for page in reader.pages:
        text, amb = render_page(page, repair=not args.no_repair)
        raw.append(text)
        for k, v in amb.items():
            ambiguous[k] = ambiguous.get(k, 0) + v

    have_text = sum(len(t.strip()) for t in raw)
    pages_with_text = sum(1 for t in raw if t.strip())
    raw = strip_running_heads(raw)

    # --- images -----------------------------------------------------------
    images, n_images = {}, 0
    if not args.no_assets:
        assets_dir = args.assets or os.path.join(out_dir, "assets", stem)
        rel_prefix = os.path.relpath(assets_dir, out_dir)
        images, n_images = extract_images(reader, assets_dir, rel_prefix)
        if n_images == 0 and os.path.isdir(assets_dir):
            try:
                os.rmdir(assets_dir)
            except OSError:
                pass

    note = []
    if have_text == 0:
        note.append(
            "> **No text layer.** This PDF is a scan - every page is an image, so no text "
            "could be extracted mechanically. The page images are linked below; they need an "
            "OCR pass or a vision transcription before this note is searchable."
        )
        print("NEEDS_OCR", file=sys.stderr)
    if ambiguous:
        listed = ", ".join(f"`{k}` x{v}" for k, v in
                           sorted(ambiguous.items(), key=lambda x: -x[1]))
        note.append(
            "> **Math fidelity.** This PDF sets its symbols in Type3 subset fonts whose "
            "private-use codepoints are assigned per subset, so the same code means "
            "different things in different chapters and cannot be decoded from the font "
            "alone. Letters, digits, brackets, fractions, superscripts and the named "
            "operators were repaired and are reliable. Every symbol that could not be "
            "identified is shown as `{?}` rather than guessed at - look it up in "
            "`clrs-4e.pdf` at the page given above. Unresolved here: " + listed + "."
        )

    # --- write ------------------------------------------------------------
    written = []

    sections = all_outline_entries(reader) if args.split_outline else {}

    def body_for(lo, hi, own_title=None):
        chunks = []
        for i in range(lo, hi):
            page_md = unwrap(raw[i]) if raw[i].strip() else ""
            for title in sections.get(i, []):
                if not title.strip() or title == own_title:
                    continue
                page_md = insert_heading(page_md, title)
            if page_md.strip():
                chunks.append(page_md)
            for ref in images.get(i, []):
                chunks.append(ref)
        return add_structure("\n\n".join(chunks))

    chapters = outline_chapters(reader) if args.split_outline else []
    if chapters:
        index = [frontmatter(args, {"source": os.path.basename(args.pdf)}), "",
                 f"# {title}", "",
                 f"Converted from `{os.path.basename(args.pdf)}` "
                 f"({len(reader.pages)} pages).", ""]
        index += note + [""] if note else []
        index.append("## Contents")
        index.append("")
        for n, (ct, start) in enumerate(chapters):
            end = chapters[n + 1][1] if n + 1 < len(chapters) else len(reader.pages)
            fname = f"{n:02d}-{slugify(ct)}.md"
            path = os.path.join(out_dir, fname)
            with open(path, "w") as fh:
                fh.write(frontmatter(args, {"source": os.path.basename(args.pdf),
                                            "part": f'"{ct}"'}))
                fh.write(f"\n\n# {ct}\n\n")
                if note:
                    fh.write("\n\n".join(note) + "\n\n")
                fh.write(f"*Source pages {start + 1}-{end} of "
                         f"`{os.path.basename(args.pdf)}`.*\n\n")
                fh.write(body_for(start, end, ct) + "\n")
            written.append(path)
            index.append(f"- [{ct}]({fname}) - pages {start + 1}-{end}")
        with open(args.out, "w") as fh:
            fh.write("\n".join(index) + "\n")
        written.append(args.out)
    else:
        with open(args.out, "w") as fh:
            fh.write(frontmatter(args, {"source": os.path.basename(args.pdf)}))
            fh.write(f"\n\n# {title}\n\n")
            if note:
                fh.write("\n\n".join(note) + "\n\n")
            fh.write(body_for(0, len(reader.pages)) + "\n")
        written.append(args.out)

    print(f"pages={len(reader.pages)} with_text={pages_with_text} "
          f"chars={have_text} images={n_images} files={len(written)}")
    for p in written:
        print("  wrote", os.path.relpath(p))


if __name__ == "__main__":
    main()
