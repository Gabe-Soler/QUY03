# MTHE 326 — Functions of a Complex Variable

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** MTHE 326 (MATH 326) — Functions of a Complex Variable
- **Official description:** Complex numbers, analytic functions, harmonic functions. Cauchy's
  theorem. Taylor and Laurent series. Calculus of residues. Rouché's theorem.
- **Format:** Lec 3, Tut 0.5
- **Prerequisites:** MTHE 280 (MATH 280), MTHE 281 (MATH 281)
- **Typical topics** (fill in / correct against your actual syllabus): complex number arithmetic
  and geometry, analytic/holomorphic functions and Cauchy-Riemann equations, harmonic functions,
  contour integration, Cauchy's integral theorem and formula, Taylor and Laurent series
  expansions, classification of singularities, calculus of residues, the residue theorem,
  Rouché's theorem and argument principle, applications to evaluating real integrals.
- **Professor:**
- **Term:**

## Reference materials

- `references/saff-snider-fundamentals-of-complex-analysis-solutions.pdf` - solutions manual for
  Saff & Snider, *Fundamentals of Complex Analysis with Applications to Engineering and Science*
  (Pearson, 2003). 243 pp. Solutions only; the main textbook is not in the repo.

  **Deliberately kept as a PDF - it cannot be converted here.** It is a pure scan: no text layer,
  so nothing to extract. Image extraction also fails (the pages are CCITT G4 fax-encoded and PIL's
  decoder returns blank images), and visual page rendering needs poppler/`pdftoppm`, which is not
  installed. Converting it would require installing `pypdfium2` to render pages, then transcribing
  243 pages of math by hand - worth doing per-chapter before the midterm, not in bulk. Ask Gabe
  before installing anything. Until then, read it by opening the PDF directly, and it will not show
  up in greps.

## Notation / conventions specific to this professor

(e.g. whether $z = x+iy$ or $z = re^{i\theta}$ is the default working form in this course,
specific contour-orientation conventions)

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).
All math in this course should be filed in LaTeX per the root `CLAUDE.md` rule.

- Week 1:

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — distinguishing removable/pole/essential
singularities and setting up the correct contour for residue-based real-integral evaluation are
common sticking points.

-
