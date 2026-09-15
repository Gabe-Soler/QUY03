---
name: md-to-pdf
description: Use when the user wants a Markdown note (a homework attempt, a filed note, a summary) turned into a PDF for submission or printing — e.g. "make this into a PDF for Crowdmark", "render my homework", "I need to submit this as a PDF". Splits multi-problem homework into one PDF per problem when asked, matching Crowdmark's "upload each problem separately" requirement.
---

# md-to-pdf

Converts a Markdown file (with LaTeX math) into a PDF, entirely in Python via matplotlib -
no LaTeX install, no Pango/Cairo, no headless Chromium. Built because none of those were
available in this environment (no Homebrew, no `pandoc`, no `pdflatex`, no `weasyprint`
system libs). See `render.py`'s module docstring for the full CLI.

## Quick use

```bash
python3 .claude/skills/md-to-pdf/render.py INPUT.md --out OUTPUT.pdf \
  --header "Name - Student Number" --split
```

- `--split` also writes one PDF per top-level numbered problem
  (`OUTPUT-problems/01-....pdf`, `02-....pdf`, ...) — this is what Crowdmark wants:
  "do not answer more than one problem on the same page... upload all pages corresponding to
  each problem separately." Content before the first detected problem (a name/date preamble)
  stays in the combined PDF only, not in any per-problem file — Crowdmark identifies the
  student from the upload link, so it isn't needed there.
- A "problem" boundary is **any heading or top-level numbered list item whose text starts with
  `<int>.`** — e.g. `#### 1.` and a bare `2. ` both count, so a file that mixes heading-style
  and plain-numbered problem markers (common when someone starts formatting partway through)
  still splits correctly. Override with `--split-regex` if a document numbers differently.
- `--header "..."` prints a small line top-right of every page (name/student number) - cheap
  insurance against shuffled pages once uploaded.

## What it supports

Headings, paragraphs with word-wrap, **bold**, *italic*, `inline code`, bullet and numbered
lists (including soft-wrapped continuation lines with no marker of their own), blockquotes,
horizontal rules, pipe tables, inline `$...$` and display `$$...$$` math anywhere in a line
(not just at the start), multi-row `\begin{gathered}`/`\begin{aligned}` blocks (row-split on
`\\`, column-aligned on `&`), and `\boxed{...}` at any position within an expression, including
mid-expression (`= \boxed{1/6} \approx 0.1667` boxes only the `1/6`).

matplotlib's mathtext supports a real but limited LaTeX subset. `render.py` patches the gap
found by probing every command actually used in this repo's filed notes:
`\ge/\le/\ne` → `\geq/\leq/\neq`, `\iff` → `\Longleftrightarrow`, `\implies` →
`\Longrightarrow`, `\tfrac/\dfrac` → `\frac`, `\displaystyle`/`\textstyle` stripped,
`\textbf/\textit/\bm` → `\mathbf/\mathit/\mathbf`, and `\underbrace{X}_{Y}` (unsupported by
mathtext) falls back to `(X)_Y`. Unrenderable math degrades to a visible `[math error]` in red
rather than crashing the whole document — check stderr for a warning list either way.

**Not supported**: nested/multi-column tables, footnotes, images, code fences (multi-line),
task-list checkboxes. These would render as literal text rather than crash; extend
`parse_blocks`/`render_blocks` in `render.py` if a note actually needs one of them.

## How it works, if it needs extending

`Page` wraps a single-page matplotlib `Figure`/`Axes` set up as a point-unit canvas
(`y` inverted so it increases downward from the top margin, like a document). `Layout` tracks
the write cursor across an unbounded sequence of `Page`s, paginating via `PdfPages`. Text is
laid out by **measuring before drawing**: `Page.measure(s, fontprops, ismath, size)` asks
matplotlib's own renderer for the exact width/height a string will occupy *at the size it will
actually be drawn at* — every call site must pass that real size, since a bare `FontProperties()`
carries a default size that has nothing to do with what `ax.text(..., fontsize=...)` will use;
mismatching the two is what caused headings to render as overlapping garbage during
development (see the "why every `.measure()` call takes an explicit size" comment on `Page.measure`).

`draw_wrapped_runs` buffers one visual line at a time (word by word, using real measured
widths) before drawing any of it, so a line's height adapts to its tallest element (e.g. an
inline $\sum_{i=1}^n$) instead of being computed from font size alone and overflowing into
whatever follows.

Any function that calls `layout.ensure_space(...)` mid-way through — which may silently start a
new `Page` — must re-fetch `page = layout.page` **after** that call, not reuse a `page` variable
captured earlier, or subsequent drawing lands on the old (already-archived) page at
coordinates meant for the new one. This bit us three times during development
(`draw_display_math_block`, `draw_list_item`, and the original single-shot `draw_wrapped_runs`)
before being fixed everywhere - worth remembering before adding a new block renderer.

## Debugging without a PDF viewer

This environment has no `pdftoppm`/poppler, so the `Read` tool can't render PDF pages as
images. To inspect output visually, render `Page.fig` straight to PNG instead of going through
`PdfPages`:

```python
import sys; sys.path.insert(0, ".claude/skills/md-to-pdf")
import render as R
blocks = R.parse_blocks(R.strip_frontmatter(open("FILE.md").read()))
layout = R.Layout(*R.PAGE_SIZES["letter"], header_text="...")
R.render_blocks(layout, blocks, fontsize=10.5)
layout.finish()
for i, p in enumerate(layout.pages):
    p.fig.savefig(f"page{i+1}.png", dpi=150)
```
