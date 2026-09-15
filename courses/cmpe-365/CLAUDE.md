# CMPE 365 — Algorithms

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** CMPE 365 — Algorithms. **Also called CISC 365**, where it is titled
  *Algorithms I*; the lecture slides are headed "CISC 365 - Algorithms I". Treat the two codes as
  the same course — material, OnQ pages and emails may use either, and the slides use CISC.
- **Official description:** Mathematics for order-of-growth analysis and recurrences to
  characterize algorithm running times. Different algorithmic design techniques and their
  optimality guarantees. Complexity theory and NP-completeness (decision algorithms, verification
  algorithms, complexity classes, reductions). Graph algorithms and their running times.
- **Format:** Lec 3, Lab 1
- **Prerequisites:** **ELEC 278 or MREN 178; ELEC 270 or a discrete mathematics course** - this is
  the CMPE/Math & Eng route, the one that applies to Gabe. The Fall 2026 syllabus is written from
  the CISC side and instead requires **registration in a School of Computing plan plus a C- or
  higher in CISC 203, 204 and 235**. Recorded here so the difference isn't mistaken for an error -
  same situation as CMPE/CISC 320.
- **Exclusions:** ELEC 226
- **Typical topics** (fill in / correct against your actual syllabus): asymptotic notation
  (Big-O/Θ/Ω), recurrence relations (substitution, recursion tree, master theorem), divide and
  conquer, greedy algorithms, dynamic programming, graph algorithms (traversal, shortest path,
  spanning trees), NP-completeness and reductions, convex hull, activity selection, longest common
  subsequence.
- **Professor:** Yuanzhu Chen (`yuanzhu.chen@queensu.ca`), with Xu Wang (`xw41@queensu.ca`).
- **Term:** Fall 2026
- **Lectures:** Stirling Room B - **Mon 11:30-12:20, Tue 13:30-14:20, Thu 12:30-13:20**. Slides
  are posted *before* each lecture, and go on OnQ; MS Teams for discussion.
- **Assessment: five in-class tests, 20% each. No assignments, no midterm, no final exam.**
  Dates: **Thu 24 Sep, Thu 8 Oct, Thu 29 Oct, Thu 12 Nov, and Tue 1 Dec** - one per topic, and note
  **the last one is a Tuesday while the other four are Thursdays**. Every test is worth a fifth of
  the grade and the syllabus offers no make-up mechanism.
  **Remark requests** go to `cisc365@cs.queensu.ca` **within 5 calendar days** of grades being
  posted; late requests are not considered.
- **Office hours:** instructor **Tue 14:30-15:20**, TA **Thu 17:00-18:00** - both in **Goodwin 536**
  and on MS Teams (channels "Office hour with Instructor" / "Office hour with TA").
- **Contact protocol (mandatory):** email `cisc365@cs.queensu.ca` or `yuanzhu.chen@queensu.ca` -
  **not OnQ** - with **"CISC365" in the subject** and **name and student number in the body**.
  TAs: Felix Xing, James Song, Mohamed Harmanani.
- **Textbook:** CLRS 4th ed. (3rd ed. accepted) - the filed copy is 4th ed.
- **Topic order:** 1a algorithm complexity (ch. 2-3) → 2 divide-and-conquer (ch. 4) → 3 greedy
  (ch. 15) → 4 dynamic programming (ch. 14) → 5 branch-and-bound → 1b NP-completeness (ch. 34).
  Chapter numbers are 4th-edition; in the 3rd edition DP and greedy are 15 and 16.
  **NP-completeness is numbered "1b" but taught last**, in weeks 12-13 after branch-and-bound, even
  though the learning outcomes list it first. **Week 6 is the fall reading break.**

## Reference materials

- `references/syllabus-f2026.md` (+ `.pdf`) - the Fall 2026 syllabus (v02, revised 9 Sep 2026),
  converted and restructured. **Check it before answering anything about dates or weighting.** It
  **confirms** the assessment scheme and all five test dates that were previously recorded here from
  the lecture 1 slides.
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

- **Pseudocode follows CLRS 3rd edition, not the 4th edition that is filed here.** Lecture 2 writes
  `INSERTION-SORT(A)` with the **outer** loop index $j$ and the **inner** index $i$; CLRS 4e writes
  `INSERTION-SORT(A, n)` with outer $i$ and inner $j$ - **the two indices are swapped**. Use the
  professor's form in tests, and expect the letters to flip when reading the filed textbook.
- Array indices run **1 to `A.length`**, not from 0.
- Set membership and equality are both used for asymptotic classes: $f(n) \in \Theta(g(n))$ and
  $f(n) = \Theta(g(n))$ are treated as interchangeable.
- Definitions are stated with **"positive constants"** (reals), never "positive integers".

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
- **Lecture 1 (2026-09-08):** course admin, what an algorithm is (informal and formal definitions,
  emphasis on *halts in finite time*), the five topics, class schedule and test dates.
- **Lecture 2 (2026-09-10):** algorithm correctness ("for every input instance, halts with the
  correct output"); choosing between correct algorithms on understanding / elegance / efficiency;
  the insertion-sort cost-and-times table; $t_j$ and the best case $\Theta(n)$ vs worst case
  $\Theta(n^2)$; why worst case is the default; order of growth; the rules for analysing
  sequences, loops and conditionals.
- **Lecture 3 (2026-09-14):** asymptotic notation proper - order of growth (lower-order terms
  don't matter); formal set-builder definitions of $\Theta$, $O$ and $\Omega$; worked
  $\tfrac{1}{2}n^2 - 3n = \Theta(n^2)$ example with explicit constants; Theorem 3.1
  ($f = \Theta(g) \iff f = O(g)$ and $f = \Omega(g)$). The slides go further than Gabe's own note:
  the counterexample $6n^3 \ne \Theta(n^2)$, the general quadratic theorem, **asymptotic notation
  inside equations**, and **transitivity / reflexivity / symmetry** (notably
  $f = O(g) \iff g = \Omega(f)$). The slide deck's two sets of practice questions are the most
  test-like material available so far - **use them for `quiz-me` before the Sep 24 test.**
- **Lecture 4 (2026-09-15):** opened with the **lecture 3 practice questions** (unanswered on the
  slides) - see `lectures/2026-09-15-lecture04-recursion-complexity.md` for Gabe's own attempt and
  `summaries/test1-chapters-2-3-study-guide.md` for the full key. Then starts **Ch. 4** proper:
  recursion and base cases; merge sort as the running recursive example; turning a recursive
  algorithm into a **recurrence relation**; solving by **substitution** (expand the self-reference,
  spot the pattern) - worked for a straight-line recursion ($T(n)=c_2+T(n-1) \to \Theta(n)$) and one
  with an inner loop ($T(n)=c_2+c_3n+T(n-1) \to \Theta(n^2)$, the same arithmetic-series shape as
  insertion sort's worst case). **This is Test 2 scope (8 Oct), not Test 1.**
- **Test 1 study guide filed** (2026-09-15):
  `summaries/test1-chapters-2-3-study-guide.md` - consolidated notes and a worked answer key for
  Ch. 2-3, covering lectures 1-3 plus the CLRS reference chapters.
- **Not yet covered:** the recursion-tree method and the master theorem for solving recurrences
  properly (rest of ch. 4).

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
