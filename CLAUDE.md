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
│   └── commands/               # slash commands triggered explicitly (/organize, /review,
│                               #   /clean_lecture)
├── inbox/                     # raw, unfiled captures land here — lecture transcripts,
│                               # phone photos of whiteboards, scratch notes, voice-memo transcripts
├── courses/
│   └── {course-slug}/
│       ├── CLAUDE.md          # course-specific context — only loads when Claude touches this folder
│       ├── lectures/
│       ├── problem-sets/
│       ├── summaries/
│       ├── references/        # textbooks, solution manuals — source material, not course notes
│       ├── code/              # source files handed out in lecture, kept compilable + an index
│       └── */assets/{note}/   # figures extracted from a note's source, linked from that note
├── assessment-calendar.md     # cross-course calendar of everything that carries marks
└── glossary.md                # optional cross-course term index
```

- **`assessment-calendar.md`** is the single place every graded deadline lives — assignments,
  tests, quizzes, midterms, project deliverables and exams for all six courses, in date order,
  with the weight of each. **Update it whenever a syllabus is filed or a date is confirmed**, and
  keep the per-course syllabus in `courses/{slug}/references/` as the authority it is derived
  from. It also carries a "still unknown" section — dates that are genuinely not published yet
  (final exams, ELEC 371 lab sessions) belong there rather than being guessed.

- **Course slugs** are lowercase-kebab-case (e.g. `linear-algebra`, `stochastic-processes`).
- **Cross-listed courses keep one folder, under the CMPE code** (`cmpe-320`, `cmpe-365`), since
  that is the code Gabe is registered under. Their CISC names are aliases, not separate courses:
  a file, search or question mentioning **CISC 320** or **CISC 365** refers to `cmpe-320` and
  `cmpe-365`. Course material arrives labelled with the CISC code more often than the CMPE one,
  so expect filenames and slide headers to say CISC.
- **Filed note filenames** follow: `YYYY-MM-DD-lectureNN-short-topic.md` (e.g.
  `2026-09-15-lecture03-eigenvalues.md`). Problem sets: `psNN-short-topic.md`. Summaries:
  `unitNN-short-topic-summary.md`.
- **Reference material** (textbooks, solution manuals) goes in `courses/{slug}/references/`.
  Book-length sources are split one file per chapter into a subfolder with an `00-index.md`.
- **A course may override this layout** in its own `CLAUDE.md`, and that override wins for files
  in that course. `cmpe-320` does: it uses `assignments/assignment_N/` (one folder per assignment,
  holding the handout plus every supplied and written source file) instead of `problem-sets/`.
  Check the course's `CLAUDE.md` before filing into it.
- **Source code handed out in lecture** goes in `courses/{slug}/code/`, **left in its original
  language, not converted to Markdown** — it is already plain text and greppable, and it has to
  stay compilable. Write one `00-index.md` there instead, describing what each file demonstrates
  and how to build it. This is the one exception to the everything-becomes-Markdown rule, and it
  exists because converting code would destroy the thing that makes it useful.
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

- `courses/cmpe-320/` — Fundamentals of Software Development (C++, OOP, software project mgmt).
  **Also called CISC 320** — the course is cross-listed and its own material is labelled
  "CISC/CMPE 320".
- `courses/cmpe-365/` — Algorithms (order of growth, recurrences, NP-completeness, graph algos).
  **Also called CISC 365** — cross-listed; the lecture slides are titled "CISC 365 - Algorithms I".
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

## Lecture notes taken live

Notes typed during a lecture are expected to be rough — gaps where the lecture outran the typing,
LaTeX written at speaking speed, and the occasional thing written down wrong. That is fine; the
capture is the point.

`/clean_lecture` (see `.claude/skills/clean-lecture/SKILL.md`) reconciles such a note against that
lecture's slides and the course's filed reference material. It fixes malformed LaTeX silently,
**marks** anything it adds from a source, and **flags rather than rewrites** anything where the
note and the source disagree — because the professor may have corrected the slides out loud, and
because a note quietly edited into agreement with the textbook hides the misunderstanding that
most needs finding before the exam.

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
