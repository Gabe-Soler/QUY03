#!/usr/bin/env python3
"""
build_glyph_map.py - identify the symbol glyphs in a TeX-produced PDF.

Some PDFs (CLRS 4e is the example in this repo) set their mathematical symbols
in Type3 subset fonts. Type3 glyphs are drawing programs: they have no glyph
names, no font descriptor, and a ToUnicode map that is wrong or absent, and each
chapter gets its own subset, so the same codepoint is a minus sign in one
chapter and a multiplication sign in the next. Nothing static identifies them.

What *is* stable is the shape on the page. This script renders one instance of
every (font, character) pair, groups the images by appearance, and writes a
contact sheet. You look at the sheet once, name each group, and it writes the
map that `pdf_to_md.py --glyph-map` consumes.

    # 1. render and cluster
    python3 build_glyph_map.py BOOK.pdf --chars "fgWj" --sheet /tmp/sheet.png

    # 2. look at /tmp/sheet.png, then name the clusters you recognise
    python3 build_glyph_map.py BOOK.pdf --chars "fgWj" \
        --assign '{"1": "\\\\{", "2": "\\\\}", "3": ":"}' \
        --out BOOK.glyphs.json

`--chars` selects which extracted characters to investigate; omit it for the
private-use characters, which is where the unidentified symbols land. Letters
are worth a pass too, since the symbol fonts reuse letter slots: in CLRS, `f`
and `g` are braces, `W` is a colon, `b`/`c`/`d`/`e` are floor and ceiling
brackets, and `h`/`i` are angle brackets.

Clusters are ordered by size, so the low-numbered ones matter most. Anything you
do not name stays unmapped and is rendered as `{?}` rather than guessed at.
"""

import argparse
import json
import sys

import pypdf
import pypdfium2 as pdfium
from PIL import Image, ImageChops, ImageDraw

THUMB = 26


def is_target(ch, wanted):
    return ch in wanted if wanted else 0xE000 <= ord(ch) <= 0xF8FF


def locate(reader, wanted):
    """One clean single-character occurrence per (font object, character)."""
    found = {}
    for index in range(len(reader.pages)):
        def visitor(text, cm, tm, font_dict, font_size):
            if not text or not font_dict:
                return
            ref = getattr(font_dict, "indirect_reference", None)
            if ref is None:
                return
            stripped = text.strip()
            if len(stripped) == 1 and is_target(stripped, wanted):
                found.setdefault((ref.idnum, stripped),
                                 (index, tm[4], tm[5], font_size or 10))
        try:
            reader.pages[index].extract_text(visitor_text=visitor)
        except Exception:
            continue
    return found


def thumbnails(path, found, scale=6):
    """Render each glyph, trim to its ink, pad to a square so shape is kept."""
    doc = pdfium.PdfDocument(path)
    out, cache = {}, {}
    for (obj, ch), (index, x, y, size) in found.items():
        if index not in cache:
            if len(cache) > 30:
                cache.clear()
            page = doc[index]
            cache[index] = (page.render(scale=scale).to_pil().convert("L"),
                            page.get_height())
        bitmap, height = cache[index]
        px, py, pad = x * scale, (height - y) * scale, size * scale
        crop = bitmap.crop((int(px - pad * 0.04), int(py - pad * 0.9),
                            int(px + pad * 0.52), int(py + pad * 0.33)))
        box = ImageChops.invert(crop).getbbox()
        if not box:
            continue
        crop = crop.crop(box)
        if crop.width < 2 or crop.height < 2:
            continue
        side = max(crop.width, crop.height)
        square = Image.new("L", (side, side), 255)
        square.paste(crop, ((side - crop.width) // 2, (side - crop.height) // 2))
        out[(obj, ch)] = square.resize((THUMB, THUMB), Image.LANCZOS)
    return out


def cluster(thumbs, threshold=1100):
    vectors = {k: list(v.get_flattened_data()) for k, v in thumbs.items()}

    def distance(a, b):
        return sum((p - q) ** 2 for p, q in zip(a, b)) / len(a)

    groups = []
    for key, vec in sorted(vectors.items()):
        best, best_d = None, float("inf")
        for i, (rep, _) in enumerate(groups):
            d = distance(vec, rep)
            if d < best_d:
                best_d, best = d, i
        if best is not None and best_d < threshold:
            groups[best][1].append(key)
        else:
            groups.append((vec, [key]))
    groups.sort(key=lambda g: -len(g[1]))
    return groups


def write_sheet(groups, path, cell=104):
    cols = 8
    rows = (len(groups) + cols - 1) // cols
    sheet = Image.new("L", (cols * cell, rows * (cell + 18)), 255)
    draw = ImageDraw.Draw(sheet)
    for i, (rep, keys) in enumerate(groups):
        img = Image.new("L", (THUMB, THUMB))
        img.putdata(rep)
        x, y = (i % cols) * cell, (i // cols) * (cell + 18)
        sheet.paste(img.resize((cell - 10, cell - 10), Image.LANCZOS), (x + 5, y + 5))
        draw.rectangle([x, y, x + cell - 1, y + cell - 1], outline=0)
        chars = "".join(sorted({k[1] for k in keys}))
        draw.text((x + 3, y + cell + 3), f"#{i} n={len(keys)} {chars!r}", fill=0)
    sheet.save(path)


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("pdf")
    ap.add_argument("--chars", default="",
                    help="characters to investigate; default: private-use only")
    ap.add_argument("--sheet", help="write the contact sheet here")
    ap.add_argument("--assign", help='JSON {"cluster index": "LaTeX"}')
    ap.add_argument("--out", help="glyph map to write or extend")
    ap.add_argument("--threshold", type=float, default=1100)
    args = ap.parse_args()

    reader = pypdf.PdfReader(args.pdf)
    found = locate(reader, set(args.chars))
    print(f"(font, character) pairs: {len(found)}")
    thumbs = thumbnails(args.pdf, found)
    groups = cluster(thumbs, args.threshold)
    print(f"clusters: {len(groups)}")

    if args.sheet:
        write_sheet(groups, args.sheet)
        print(f"contact sheet: {args.sheet}")

    if args.assign:
        assign = json.loads(args.assign)
        mapping = {}
        if args.out:
            try:
                mapping = json.load(open(args.out, encoding="utf-8"))
            except FileNotFoundError:
                pass
        before = len(mapping)
        for index, symbol in assign.items():
            for obj, ch in groups[int(index)][1]:
                mapping[f"{obj}|{ch}"] = symbol
        if not args.out:
            print("--assign given without --out; nothing written", file=sys.stderr)
            return
        with open(args.out, "w", encoding="utf-8") as fh:
            json.dump(mapping, fh, indent=0, ensure_ascii=False)
        print(f"glyph map {before} -> {len(mapping)} entries in {args.out}")


if __name__ == "__main__":
    main()
