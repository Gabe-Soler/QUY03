Run the `file-notes` workflow on everything currently in `inbox/`: file each item into the correct
course folder per the conventions in the root `CLAUDE.md`, fully automatically, and then report a
one-line summary per file (`old path → new path`). Do not ask for approval before filing.

**Convert everything convertible to Markdown, and keep every original.** Run PDFs, slide decks,
and lab manuals through `.claude/skills/file-notes/pdf_to_md.py`, extract their figures to
`assets/`, and link them from the note. Move the source file out of `inbox/` to sit beside its
note under the same basename — never delete it. If an item genuinely cannot be converted (a scan
with no text layer), file it as the original PDF, record it in the course's `CLAUDE.md`, and say
so explicitly in the report.
