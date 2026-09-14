---
name: build-cheat-sheet
description: Use when the user asks for a cheat sheet, exam reference sheet, summary sheet, or a compressed review document for a unit/chapter/course before a test — e.g. "build me a cheat sheet for unit 3", "summarize everything before the midterm".
---

# Build Cheat Sheet

Compresses filed notes for a scoped unit into a single dense reference document — a compression
task, not a re-teaching task. Assumes the reader (Gabe) has already learned the material once and
needs a fast recall aid.

## Step-by-step

1. **Determine scope** — a specific unit/lecture range if named, otherwise the whole course.
2. **Read every filed note in scope**: lectures, problem-sets, and any prior summaries, in
   chronological order — the sheet should reflect the actual sequence and phrasing used in class,
   not a reorganized textbook structure.
3. **Extract, per concept:**
   - The formal statement / formula (in LaTeX)
   - The one-line "when to use this" trigger condition
   - Any gotchas or edge cases explicitly mentioned in the notes (these are usually the exam
     traps)
4. **Compress aggressively.** This is not a full explanation document — no step-by-step derivation
   walkthroughs here (that belongs in the original notes / `quiz-me` sessions). Each concept
   should be a few lines: statement, trigger condition, gotcha.
5. **Organize by topic, not by lecture date** — group related concepts together even if they were
   taught weeks apart, since this is a pre-exam reference, not a chronological record.
6. **Add a short TLDR block at the very top** listing just the concept names covered, so it
   doubles as a table of contents for a document that's likely more than a 2-minute read.
7. **Save the result** to `courses/{slug}/summaries/unitNN-{topic}-cheat-sheet.md` with the
   standard frontmatter (`type: summary`), and report the path.

## Notes

- If a concept in scope has known weak spots from a prior `quiz-me` session, mark it with a short
  flag (e.g. "⚠ review derivation") rather than expanding it — the cheat sheet stays compressed;
  the flag is the signal to go do a focused `quiz-me` pass on that specific concept instead.
