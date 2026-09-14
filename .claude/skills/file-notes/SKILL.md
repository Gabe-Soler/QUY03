---
name: file-notes
description: Use when the user asks to organize, file, sort, or process their inbox — e.g. "file my inbox", "organize what I dumped in", "sort these notes", or when new content has been added to inbox/ and needs to be placed into the right course folder.
---

# File Notes

Takes raw, unsorted captures out of `inbox/` and files them into the correct course folder
following the conventions in the root `CLAUDE.md`, fully automatically — no approval step.

## The core rule: convert everything convertible, keep every original

**Anything that can be converted to Markdown is converted, with its figures.** PDFs, slide decks,
lab manuals, and exported documents all become Markdown as part of filing, because a note that is
only a PDF can't be grepped, quoted in a cheat sheet, diffed in git, or used by `quiz-me`.
Anything the Markdown can't hold — schematics, plots, photos — is extracted to an image file and
**linked from the note**, so the note stands on its own.

**The original file is always kept, in both cases.** Conversion is lossy in ways that aren't
always obvious at filing time (vector figures don't extract, math fonts can be mis-encoded, page
layout is flattened), so the source stays alongside the note as the authority to check against.
Never delete a source file as part of filing.

If a capture **can't** be converted — a scan with no text layer, an unsupported format — that is
fine: it stays as the original file, gets recorded in the course's `CLAUDE.md` so it's still
discoverable, and the report says plainly that it wasn't converted and why.

## Step-by-step

1. **Read root `CLAUDE.md`** for the current filename convention, frontmatter schema, and folder
   structure (do this fresh each run — conventions may have been updated).
2. **List everything in `inbox/`.** Each item could be: a lecture transcript, a photo/scan of
   handwritten notes, a scratch braindump, a voice-memo transcript, a lab manual or slide deck as
   a PDF, a textbook, or a partially-formatted note.
3. **Convert it to Markdown** (see "Converting" below). Do this before deciding filename and tags —
   you need the actual content to pick a topic slug and specific tags.
4. **For each item, determine:**
   - **Course** — match against existing `courses/{slug}/` folders first. If genuinely no match,
     create a new course folder using `courses/_template/` as the pattern (copy its `CLAUDE.md`
     too) rather than leaving the item unfiled.
   - **Type** — `lecture`, `problem-set`, `summary`, or `reference` (textbooks, solution manuals,
     and anything else that is source material rather than course notes).
   - **Date** — from the content itself if present, otherwise the file's creation date. If a
     document's own date is from a previous year (a deck reused from an earlier offering), use
     that date but **say so at the top of the note**, so it doesn't look like current-term material.
   - **Topic** — a short 2–4 word slug for the filename, drawn from the actual content (don't
     invent a generic label).
   - **Tags** — pull specific concept names mentioned (e.g. `eigenvalues`, `martingales`), not
     generic tags like `math` or `notes`.
5. **Clean and reformat the content** as you file it:
   - Convert math to proper LaTeX (`$...$` / `$$...$$`) even if the raw capture used plain text or
     ASCII approximations.
   - Fix obvious transcription/OCR errors where confident; leave a `<!-- unclear: ... -->` comment
     where not confident rather than guessing silently.
   - Preserve the original structure/order of the material — don't reorganize the professor's
     sequence of ideas.
6. **Write the frontmatter block** per the schema in root `CLAUDE.md`.
7. **Place the note** in `courses/{slug}/{lectures|problem-sets|summaries|references}/` with the
   correct filename, its figures in `assets/{note-stem}/` beside it, and **the original file
   beside the note under the same basename** (e.g. `ps00-lab-a0-ltspice-simulation.md` next to
   `ps00-lab-a0-ltspice-simulation.pdf`). Move the original out of `inbox/` — don't copy it.
8. **Update the course's `CLAUDE.md`** "covered so far" section if this is new lecture material
   that extends what's been taught (see that file's own structure).
9. **Report back** a short list, one line per file:
   `inbox/raw-name.pdf → courses/linear-algebra/lectures/2026-09-15-lecture03-eigenvalues.md`.
   No approval question — this is a statement of what was done, so it can be checked and reverted
   via `git diff` / `git checkout` if something's wrong.

## Converting

### PDFs, slide decks, lab manuals

Use the bundled converter:

```bash
python3 .claude/skills/file-notes/pdf_to_md.py INPUT.pdf \
  --out courses/{slug}/{folder}/{filename}.md \
  --course {slug} --type {type} --date YYYY-MM-DD --tags "a,b,c" \
  --title "Human readable title"
```

It handles the things that silently corrupt naive PDF text extraction:

- **Broken TeX math fonts.** Many TeX-produced PDFs carry subsetted math fonts with a wrong
  ToUnicode map, so `(n/3)(n/3) = n²/9` extracts as `.n=3/.n=3/ D n 2 =9`. The converter detects
  math-font runs and repairs them. Glyphs that are genuinely ambiguous between subset fonts are
  **left alone and listed in a warning block at the top of the note** — never silently guessed.
- **Figures.** Embedded images are extracted to `assets/{note-stem}/` and linked inline at the
  page where they appeared. Non-web formats (TIFF etc.) are re-encoded to PNG so they render.
- **Running heads and hard wrapping** are stripped, and paragraphs are rejoined.
- **Structure.** Section headings come from the PDF outline, numbered algorithm listings are
  rebuilt as ordered lists, running heads and page numbers are dropped, and `<` / `>` are escaped
  so a Markdown renderer doesn't read the text as HTML and swallow the page.
- **Long documents.** `--split-outline` writes one file per top-level PDF bookmark plus an index —
  use it for anything book-length instead of producing one enormous file.

### Identifying symbol fonts

Some TeX PDFs set their symbols in **Type3** fonts. These are the hard case: a Type3 glyph is a
drawing program with no name, no font descriptor and a wrong-or-absent ToUnicode map, and each
chapter gets its own subset — so the same codepoint is a minus sign in one chapter and a
multiplication sign in the next. **No global character table can be correct**, and pdfium's text
extraction drops these glyphs entirely rather than guessing.

The only stable identity is the rendered shape, so `build_glyph_map.py` renders one instance of
every (font, character) pair, clusters the images by appearance, and writes a contact sheet. You
read the sheet once and name the clusters:

```bash
# 1. cluster and render the sheet
python3 .claude/skills/file-notes/build_glyph_map.py BOOK.pdf --sheet /tmp/sheet.png

# 2. look at the sheet, then name what you recognise
python3 .claude/skills/file-notes/build_glyph_map.py BOOK.pdf \
    --assign '{"0": "-", "1": "\\ge ", "3": "\\times "}' --out BOOK.glyphs.json

# 3. convert; the map beside the PDF is picked up automatically
python3 .claude/skills/file-notes/pdf_to_md.py BOOK.pdf --out note.md
```

Run it again with `--chars` for letters, because the symbol fonts reuse letter slots. In CLRS,
`f`/`g` are braces, `W` is a colon, `b`/`c`/`d`/`e` are floor and ceiling brackets, and `h`/`i`
are angle brackets — all invisible until you look at the sheet.

Anything left unnamed renders as `{?}`, never as a guess. **A wrong symbol in a reference is worse
than a visible gap**, because it reads as correct: the first pass of the CLRS conversion silently
turned `n - 1` into `n \le 1` throughout, which is exactly the failure this workflow exists to
prevent. Check the fidelity note at the top of a converted file to see what is still unresolved.

**Always read the converted output before reporting.** For lecture and lab material the raw dump
is a starting point, not the final note: rewrite it into the structure described in root
`CLAUDE.md` (TLDR at top for anything over ~2 minutes of reading, LaTeX for all math, links back
to prerequisite material already in the notes). For `reference` material — textbooks, solution
manuals — the mechanical conversion is enough; don't hand-rewrite a thousand pages.

### Scans and photos (no text layer)

If the converter prints `NEEDS_OCR`, the PDF is a scan — every page is an image and no text can be
extracted mechanically. **File it as the PDF**, record it in the course's `CLAUDE.md` under
reference materials with a note that it has no text layer, and say so in the report. Don't leave
it in `inbox/`, and don't fake a conversion.

This environment has no OCR and no PDF page renderer — `tesseract`, `pdftoppm`/poppler, and
`pdftotext` are all absent, and PIL's CCITT G4 decoder fails on fax-encoded scans (pages come out
blank). Reading such a PDF visually therefore does not work either. Unblocking one needs an
install (`pypdfium2` renders pages with no system dependencies; `rapidocr-onnxruntime` does OCR
but mangles math notation) — **ask before installing anything**, and only when the user actually
wants that document transcribed.

### Everything else

Plain text, Markdown, and transcripts are already text — just clean, add frontmatter, and file.
For a format with no converter here, extract what text you can and note explicitly in the report
what could not be converted.

## Notes

- If an inbox item clearly contains material for *multiple* courses or topics, split it into
  multiple filed notes rather than forcing it into one file.
- If an item is too ambiguous to file confidently (e.g., no identifiable course or topic at all),
  leave it in `inbox/` and say so explicitly in the report, with the reason — don't silently skip
  it.
- **Flag contradictions.** If a new capture conflicts with something already filed (a reused deck
  from a previous year, a correction, a professor rephrasing something), point it out in the note
  and in the report rather than silently overwriting.
- **Originals are always kept** alongside the Markdown, converted or not. The Markdown is what you
  read and search; the original is what you check against when something looks wrong. Filing never
  deletes a source file.
- When a conversion is known to be imperfect — the converter reported ambiguous math glyphs, or
  figures are vector and didn't extract — say so at the top of the note and point at the original
  file by name.
