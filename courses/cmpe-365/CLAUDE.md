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
- `references/clrs-4e.pdf` - the original, kept as the reference copy. Still needed for **figures**:
  CLRS draws them as vector graphics, so none could be extracted. A "Figure N.M" reference in the
  Markdown means opening the PDF at the page named at the top of that chapter file.
- `references/clrs-4e.glyphs.json` - the symbol table for the PDF's Type3 fonts, built by
  `.claude/skills/file-notes/build_glyph_map.py`. **Don't delete it**: without it the conversion
  cannot tell a minus sign from a multiplication sign, because Type3 subsets assign codepoints
  per chapter. Regenerating it means re-identifying the glyphs from a rendered contact sheet.
- Math that could not be identified renders as `{?}` rather than a guess (about 730 spots, mostly
  large summation and integral delimiters). Each chapter file opens with a note saying what is
  unresolved in it.

## Notation / conventions specific to this professor

(e.g. specific pseudocode style used in lecture, specific proof-writing conventions for
correctness/complexity proofs)

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).
This is especially important here since algorithms build cumulatively (e.g. DP relies on
recursion/recurrence understanding from earlier weeks).

- **Ch. 1 - The Role of Algorithms in Computing** (summarised 2026-09-10): problem vs. instance vs.
  algorithm; correctness means halting *and* being right on every instance; asymptotic growth beats
  hardware (the 10 billion vs 10 million instr/sec comparison, where the 1000x slower machine running
  merge sort beats the fast one running insertion sort by 17x at $n = 10^7$); NP-completeness and
  approximation; parallel and online algorithms as newer models.
- **Ch. 2 - Getting Started** (summarised 2026-09-13): insertion sort as the incremental method;
  **loop invariants** (initialization / maintenance / termination) as the correctness proof
  technique; the **RAM model**; line-by-line counting giving $T(n) = an + b$ best case and
  $T(n) = an^2 + bn + c$ worst case; why worst case is the default; order of growth and
  $\Theta$-notation; merge sort and divide-and-conquer, with
  $T(n) = 2T(n/2) + \Theta(n) \to \Theta(n \lg n)$ argued from the recursion tree.
- **Lecture 3 (2026-09-14):** asymptotic notation proper - order of growth (lower-order terms
  don't matter); formal set-builder definitions of $\Theta$, $O$ and $\Omega$; worked
  $\tfrac{1}{2}n^2 - 3n = \Theta(n^2)$ example with explicit constants; Theorem 3.1
  ($f = \Theta(g) \iff f = O(g)$ and $f = \Omega(g)$). Filed note has been through
  `/clean_lecture` against CLRS ch. 3.
- **Not yet covered:** solving recurrences (ch. 4), referenced forward by the ch. 2 summary but not
  yet taught.

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — NP-completeness proofs and recurrence
solving are common sticking points in this course, worth watching for.

- **Choosing $c_2$ in a $\Theta$ proof** (from lecture 3, 2026-09-14). Substituting a single value
  of $n$ pins down the *lower* constant $c_1$ but not the *upper* constant $c_2$: when the ratio
  $f(n)/g(n)$ is increasing, $c_2$ has to beat its supremum as $n \to \infty$, not its value at
  $n_0$. Gabe concluded "$c_2 \ge 1/5$" from $n = 10$ when $c_2 \ge 1/2$ was required. **Worth a
  quiz question**: give a $\Theta$ bound where $f/g$ is *decreasing* and check he flips which
  constant the substitution determines.
- **Stating the $O$ definition in full** (same lecture). Wrote it without the $f(n) \le c\,g(n)$
  bound and without "for all $n \ge n_0$". Drill the full set-builder form, not the intuition.
- **"Constants" vs "positive integers"** in asymptotic definitions - the constants are positive
  *reals*; $c_1 = 1/5$ is a normal answer.

-
