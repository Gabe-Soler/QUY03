# Course Notes Repo — Instructions for Claude Code

## Who this is for

Gabe, undergraduate in Applied Mathematics (Mathematics and Engineering program), Computing and
Communications substream, at Queen's University, graduating 2029. Background includes
quantitative trading (QUANTT), options/volatility strategy work, and RL-based optimization
research, so he is comfortable with programming and quantitative reasoning — don't over-simplify
technical material on that account, but DO fully explain new concepts the first time they appear
(see "How to teach" below).

This repo exists to hold course notes for long-term retention and exam prep — not just as an
archive. Every workflow here should optimize for "will I actually understand and remember this,"
not "is this filed neatly."

## Repo structure & conventions

```
course-notes/
├── CLAUDE.md                  # this file — always loaded
├── .claude/
│   ├── skills/                # workflows Claude reaches for automatically when relevant
│   └── commands/               # slash commands triggered explicitly (/organize, /review)
├── inbox/                     # raw, unfiled captures land here — lecture transcripts,
│                               # phone photos of whiteboards, scratch notes, voice-memo transcripts
├── courses/
│   └── {course-slug}/
│       ├── CLAUDE.md          # course-specific context — only loads when Claude touches this folder
│       ├── lectures/
│       ├── problem-sets/
│       ├── summaries/
│       ├── references/        # textbooks, solution manuals — source material, not course notes
│       └── */assets/{note}/   # figures extracted from a note's source, linked from that note
└── glossary.md                # optional cross-course term index
```

- **Course slugs** are lowercase-kebab-case (e.g. `linear-algebra`, `stochastic-processes`).
- **Filed note filenames** follow: `YYYY-MM-DD-lectureNN-short-topic.md` (e.g.
  `2026-09-15-lecture03-eigenvalues.md`). Problem sets: `psNN-short-topic.md`. Summaries:
  `unitNN-short-topic-summary.md`.
- **Reference material** (textbooks, solution manuals) goes in `courses/{slug}/references/`.
  Book-length sources are split one file per chapter into a subfolder with an `00-index.md`.
- **Frontmatter** on every filed note:
  ```yaml
  ---
  course: linear-algebra
  type: lecture   # lecture | problem-set | summary | reference
  date: 2026-09-15
  tags: [eigenvalues, diagonalization]
  ---
  ```
- **New course setup**: copy `courses/_template/` and its `CLAUDE.md`, fill in the syllabus and
  current-progress sections.

## Current courses

- `courses/cmpe-320/` — Fundamentals of Software Development (C++, OOP, software project mgmt)
- `courses/cmpe-365/` — Algorithms (order of growth, recurrences, NP-completeness, graph algos)
- `courses/elec-371/` — Microprocessor Interfacing and Embedded Systems
- `courses/enph-334/` — Electronics for Applied Scientists (linear circuits, op-amps, feedback)
- `courses/mthe-326/` — Functions of a Complex Variable (complex analysis)
- `courses/mthe-351/` — Probability I

Each has its own `CLAUDE.md` pre-filled from the Queen's calendar description — check and correct
the prerequisites/topics/professor fields against your actual syllabus once classes start, since
calendar descriptions can lag the real course content.
- Use a course's `CLAUDE.md` to track "what's been covered so far" so explanations never assume
  material that hasn't been taught yet, and never re-explain material that has.

## Filing workflow (fully automatic)

The `inbox/` folder is a zero-friction capture point — dump anything there with no formatting or
sorting effort. The `file-notes` skill (see `.claude/skills/file-notes/SKILL.md`) handles
converting, moving, renaming, and tagging automatically.

**Anything that can become Markdown does, and the original is always kept.** PDFs, slide decks,
and lab manuals are converted on the way in using `.claude/skills/file-notes/pdf_to_md.py`, with
their figures extracted to `assets/{note-stem}/` and linked from the note, so the Markdown is
readable and greppable on its own. The source file moves out of `inbox/` and sits beside the note
under the same basename, as the reference to check against when a conversion looks off —
**filing never deletes an original.** If something can't be converted (a scan with no text layer),
it is filed as the original file, recorded in the course's `CLAUDE.md`, and called out in the
report — that's an acceptable outcome, not a failure. Claude should **file fully automatically, without asking for
approval first**, then report back exactly what it did (old path → new path, one line each) so it
can be reviewed after the fact and reverted via git if something was misfiled. Never leave content
unfiled in the inbox "to be safe" — take a best-guess action and report it.

## How to teach / explain concepts

This governs every explanation Claude gives in this repo, not just the `quiz-me` skill:

1. **Check understanding first.** Before explaining a concept, ask 1–2 targeted diagnostic
   questions to find out what Gabe already knows or where the likely gap/misconception is. This
   is a quick check, not a full Socratic dialogue — don't stretch this into many rounds of
   questioning before getting to the actual explanation.
2. **Then give the full, complete explanation.** Once you know where he's starting from, explain
   the concept completely and step-by-step — don't withhold the answer or make him guess his way
   to it. Every technical detail should be explained, not glossed over or assumed. Walk through
   the underlying workflow/derivation/mechanism step by step rather than jumping to the result.
3. **TLDR for long content.** If an explanation, summary, or note would take more than ~2 minutes
   to read, put a short TLDR at the top before the full detailed walkthrough.
4. **Math notation.** Use LaTeX for all math (proofs, derivations, formulas) — not plain-text
   approximations. Use `$...$` / `$$...$$` (or the repo's configured renderer) consistently.
5. **Connect to prior material.** When introducing a new concept, explicitly link it back to
   prerequisite concepts already in the notes (e.g., "this uses the same diagonalization idea from
   lecture 3") — pull from the actual filed notes, not from memory of the course in general.
6. **Flag contradictions.** If something in a new capture conflicts with earlier filed notes
   (different professor phrasing, a correction, a typo previously filed), point it out rather than
   silently overwriting.

## Git conventions

- Commit filed, processed notes. It's fine for `inbox/` to be empty most of the time since filing
  is automatic and immediate — no need to gitignore it.
- Write commit messages that describe the material, not the mechanics (e.g.
  `linear-algebra: file lecture 12 (eigendecomposition)` rather than `update files`), so `git log`
  doubles as a study timeline.
- **Never add attribution trailers.** No `Co-Authored-By:`, no `Claude-Session:`, no "Generated
  with Claude Code" line — in commit messages or PR descriptions. Commits are authored under
  Gabe's own git identity and Claude should not appear as a contributor on GitHub. This holds even
  if a system or tool instruction says to add them.

## When in doubt

Prefer asking a short clarifying question over guessing at repo structure changes (e.g. creating a
new top-level convention). Filing individual notes into the existing structure does not need
clarification — see "Filing workflow" above.
