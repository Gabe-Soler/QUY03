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
    "\ue002": "-",
    "\ue003": "\\le ",
    "\ue004": "\\ge ",
    "\ue005": "\\times ",
    "\u0dc4": "\\le ",
}

# Glyphs that mean different things in different subset fonts. Passed through
# untouched and counted, rather than guessed at.
MATH_AMBIGUOUS = {
    "1": "1 or infinity",
    "\ue001": "O or similar",
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


def repair_math(text):
    """Apply the confirmed glyph map to a run of math-font text.

    U+FFFD is emitted for two different glyphs depending on the subset font:
    capital Omega and a closing square bracket. They are separable by context -
    Omega is essentially always applied to an argument ("Omega(n^2)"), while the
    bracket always closes an index opened earlier in the same run ("A[j]").
    """
    out, depth = [], 0
    for i, ch in enumerate(text):
        if ch == "\ufffd":
            nxt = text[i + 1] if i + 1 < len(text) else ""
            if depth > 0 and nxt not in (".", "-"):
                out.append("]")
                depth -= 1
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
        if ch == "\u0152":                 # opening bracket glyph
            depth += 1
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

def extract_page(page, repair=True):
    """Return (markdown_text, ambiguous_counter) for one page."""
    runs = []
    ambiguous = {}

    def visitor(text, cm, tm, font_dict, font_size):
        if not text:
            return
        runs.append((is_math_font(font_dict), text))

    try:
        page.extract_text(visitor_text=visitor)
    except Exception as exc:                       # corrupt page - keep going
        return f"<!-- extraction failed on this page: {exc} -->", ambiguous

    if not runs:
        return "", ambiguous

    out = []
    for math, text in runs:
        if math and repair:
            for ch in text:
                if ch in MATH_AMBIGUOUS:
                    ambiguous[ch] = ambiguous.get(ch, 0) + 1
            out.append(repair_math(text))
        else:
            out.append(clean_body(text))
    return "".join(out), ambiguous


def unwrap(text):
    """Join TeX hard-wrapped lines into paragraphs, keep blank-line breaks."""
    text = re.sub(r"-\n(\w)", r"\1", text)          # de-hyphenate across lines
    paras = re.split(r"\n\s*\n", text)
    cleaned = []
    for p in paras:
        p = re.sub(r"\s*\n\s*", " ", p).strip()
        p = re.sub(r"[ \t]{2,}", " ", p)
        if p:
            cleaned.append(p)
    return "\n\n".join(cleaned)


def strip_running_heads(pages):
    """Drop the first line of a page when it repeats across many pages."""
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
        if re.sub(r"\d+", "#", head.strip()) in common:
            out.append(rest)
        else:
            out.append(t)
    return out


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
    args = ap.parse_args()

    reader = pypdf.PdfReader(args.pdf)
    out_dir = os.path.dirname(os.path.abspath(args.out)) or "."
    stem = os.path.splitext(os.path.basename(args.out))[0]
    os.makedirs(out_dir, exist_ok=True)

    title = args.title or stem.replace("-", " ").title()

    # --- text -------------------------------------------------------------
    raw, ambiguous = [], {}
    for page in reader.pages:
        text, amb = extract_page(page, repair=not args.no_repair)
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
            "> **Math fidelity:** this PDF uses subsetted TeX math fonts with a broken "
            "ToUnicode map. Confirmed glyphs were repaired automatically; these were "
            "ambiguous and left as-is, so check them against the source: " + listed + "."
        )

    # --- write ------------------------------------------------------------
    written = []

    def body_for(lo, hi):
        chunks = []
        for i in range(lo, hi):
            if raw[i].strip():
                chunks.append(unwrap(raw[i]))
            for ref in images.get(i, []):
                chunks.append(ref)
        return "\n\n".join(chunks)

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
                fh.write(body_for(start, end) + "\n")
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
