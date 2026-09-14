# CMPE 365 — Algorithms

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** CMPE 365 (cross-listed as CISC 365 in some calendars) — Algorithms
- **Official description:** Mathematics for order-of-growth analysis and recurrences to
  characterize algorithm running times. Different algorithmic design techniques and their
  optimality guarantees. Complexity theory and NP-completeness (decision algorithms, verification
  algorithms, complexity classes, reductions). Graph algorithms and their running times.
- **Format:** Lec 3, Lab 1
- **Prerequisites:** ELEC 278 or MREN 178; ELEC 270 or a discrete mathematics course
- **Exclusions:** ELEC 226
- **Typical topics** (fill in / correct against your actual syllabus): asymptotic notation
  (Big-O/Θ/Ω), recurrence relations (substitution, recursion tree, master theorem), divide and
  conquer, greedy algorithms, dynamic programming, graph algorithms (traversal, shortest path,
  spanning trees), NP-completeness and reductions, convex hull, activity selection, longest common
  subsequence.
- **Professor:**
- **Term:**

## Reference materials

- `references/clrs-4e/` - Cormen, Leiserson, Rivest & Stein, *Introduction to Algorithms*, 4th ed.
  (MIT Press, 2022), converted to Markdown and split one file per chapter, with `00-index.md` as
  the contents page. **Grep this** for anything in the course: asymptotics and recurrences
  (ch. 3-4), divide and conquer, greedy, DP, graph algorithms, NP-completeness.
- `references/clrs-4e.pdf` - the original, kept as the reference copy. Needed for two things the
  conversion can't give you: **figures** (CLRS draws them as vector graphics, so none were
  extracted) and **checking ambiguous math**. The PDF's math fonts have a broken ToUnicode map;
  the converter repairs the confirmed glyphs (`\Theta`, `\Omega`, `\le`, `\ge`, `(`/`)`, `/`, `=`)
  but a few stay ambiguous and are listed in a warning block at the top of each chapter file - the
  common one is `1`, which is sometimes the digit and sometimes $\infty$.

## Notation / conventions specific to this professor

(e.g. specific pseudocode style used in lecture, specific proof-writing conventions for
correctness/complexity proofs)

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).
This is especially important here since algorithms build cumulatively (e.g. DP relies on
recursion/recurrence understanding from earlier weeks).

- Week 1:

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — NP-completeness proofs and recurrence
solving are common sticking points in this course, worth watching for.

-
