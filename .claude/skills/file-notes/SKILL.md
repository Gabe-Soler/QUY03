---
name: file-notes
description: Use when the user asks to organize, file, sort, or process their inbox — e.g. "file my inbox", "organize what I dumped in", "sort these notes", or when new content has been added to inbox/ and needs to be placed into the right course folder.
---

# File Notes

Takes raw, unsorted captures out of `inbox/` and files them into the correct course folder
following the conventions in the root `CLAUDE.md`, fully automatically — no approval step.

## Step-by-step

1. **Read root `CLAUDE.md`** for the current filename convention, frontmatter schema, and folder
   structure (do this fresh each run — conventions may have been updated).
2. **List everything in `inbox/`.** Each item could be: a lecture transcript, a photo/scan of
   handwritten notes, a scratch braindump, a voice-memo transcript, or a partially-formatted note.
3. **For each item, determine:**
   - **Course** — match against existing `courses/{slug}/` folders first. If genuinely no match,
     create a new course folder using `courses/_template/` as the pattern (copy its `CLAUDE.md`
     too) rather than leaving the item unfiled.
   - **Type** — lecture, problem-set, or summary, based on content.
   - **Date** — from the content itself if present, otherwise the file's creation date.
   - **Topic** — a short 2–4 word slug for the filename, drawn from the actual content (don't
     invent a generic label).
   - **Tags** — pull specific concept names mentioned (e.g. `eigenvalues`, `martingales`), not
     generic tags like `math` or `notes`.
4. **Clean and reformat the content** as you file it:
   - Convert math to proper LaTeX (`$...$` / `$$...$$`) even if the raw capture used plain text or
     ASCII approximations.
   - Fix obvious transcription/OCR errors where confident; leave a `<!-- unclear: ... -->` comment
     where not confident rather than guessing silently.
   - Preserve the original structure/order of the material — don't reorganize the professor's
     sequence of ideas.
5. **Write the frontmatter block** per the schema in root `CLAUDE.md`.
6. **Move the file** from `inbox/` to `courses/{slug}/{lectures|problem-sets|summaries}/` with the
   correct filename.
7. **Update the course's `CLAUDE.md`** "covered so far" section if this is new lecture material
   that extends what's been taught (see that file's own structure).
8. **Report back** a short list, one line per file: `inbox/raw-name.txt → courses/linear-algebra/lectures/2026-09-15-lecture03-eigenvalues.md`.
   No approval question — this is a statement of what was done, so it can be checked and reverted
   via `git diff` / `git checkout` if something's wrong.

## Notes

- If an inbox item clearly contains material for *multiple* courses or topics, split it into
  multiple filed notes rather than forcing it into one file.
- If an item is too ambiguous to file confidently (e.g., no identifiable course or topic at all),
  leave it in `inbox/` and say so explicitly in the report, with the reason — don't silently skip
  it.
