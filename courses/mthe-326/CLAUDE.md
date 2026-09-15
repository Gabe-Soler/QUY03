# MTHE 326 — Functions of a Complex Variable

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** MTHE 326 (MATH 326) — Functions of a Complex Variable
- **Official description:** Complex numbers, analytic functions, harmonic functions. Cauchy's
  theorem. Taylor and Laurent series. Calculus of residues. Rouché's theorem.
- **Format:** Lectures **Mon 12:30-13:30, Thu 13:30-14:30, Fri 10:30-11:30**, tutorial
  **Tue 9:30-10:30** - all in **Kingston Hall 201**. The outline says the tutorial is a **full
  hour**, where the calendar says "Tut 0.5"; trust the outline. **3.0 units** as MATH 326,
  **3.5 units** as MTHE 326.
- **Prerequisites:** **MATH 281 / MTHE 281** only. *(This file previously said "MTHE 280 (MATH 280),
  MTHE 281 (MATH 281)" from the calendar - the actual course outline lists 281 alone. Corrected
  2026-09-14.)*
- **Actual topics** (from the Fall 2026 outline, in the order they are treated):
  1. **Complex numbers** - algebra, geometry, polar form, roots, topology of the complex plane.
  2. **Analytic functions** - limits, differentiability, Cauchy-Riemann equations, harmonic functions.
  3. **Elementary functions** - complex exponential, trigonometric and hyperbolic functions,
     logarithms, powers, and **branches**.
  4. **Complex integration** - contours and contour integrals, Cauchy's theorem, Cauchy's integral
     formula.
  5. **Power and Laurent series** - zeros and singularities.
  6. **Residue theory** - evaluating real and complex integrals by residues.

  Note that **Rouche's theorem and the argument principle appear in the calendar description but
  not in the outline's topic list** - do not assume they are covered until they show up in lecture.
- **Professor:** **Ivan Dimitrov** - `dimitrov@queensu.ca`, Jeffery Hall Rm 508, office hours
  **Mon 11:00-12:00** and by appointment. Replies to email within **two business days**, and not in
  evenings, on weekends, or on university holidays; maths questions are to go to office hours, the
  tutorial, or the end of a lecture rather than email.
- **Term:** Fall 2026 (8 September - 8 December 2026)
- **Assessment:** 12 unannounced in-class quizzes, **best 8 count, 10%**; **Midterm 1 - Tue 6 Oct,
  18:00-19:30, 20%**; **Midterm 2 - Wed 18 Nov, 18:00-19:30, 20%**; final exam **50%** (TBA within
  10-23 Dec 2026). **Both midterms are evening sittings unrelated to the lecture slots.**
  **There is no submitted homework at all** - problem sets are posted but never collected, so 100%
  of the grade is written in person with no aids. Missing a midterm with an approved consideration
  redistributes its weight proportionally; without one it is a zero. Regrade requests in writing
  within one week.
- **GenAI policy:** permitted **while studying** (exercises, problem sets, reading - no disclosure
  required since none of it is submitted), and **prohibited on every assessment**, where no aids of
  any kind are allowed. The instructor adds an unusually direct caution that these tools "routinely
  produce confident, fluent, wrong complex analysis - mishandled branch cuts, invented residues,
  contours that do not close, theorems applied where their hypotheses fail." **Lean on `quiz-me`
  here and verify every worked contour integral by hand.** See `references/course-outline-f2026.md`
  for the full quote.

## Reference materials

- `references/course-outline-f2026.md` (+ `.pdf`) - the Fall 2026 course outline, converted and
  restructured. **Check it before answering anything about dates or weighting.**
- **Recommended textbook:** E.B. Saff and A.D. Snider, *Fundamentals of Complex Analysis*, 3rd ed.,
  Pearson, 2003 - on reserve at Stauffer Library; $199.99 print / $71.99 for a 180-day e-book
  rental. Not required, and no lecture notes will be posted. **The outline misspells the second
  author as "Snyder"** - it is Snider, and it is the same book the solutions manual below covers.
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
- `references/saff-snider-fundamentals-of-complex-analysis.pdf` - the main textbook itself
  (3rd ed., 585 pp.), now in the repo alongside its solutions manual above.

  **Also deliberately kept as a PDF, for a different reason: it's a scan with an OCR text layer of
  unreliable quality**, not a proper conversion candidate. Its fonts are a single `/Type0 Invisible`
  font over the whole document - the signature of a scanned book with a hidden OCR layer laid over
  page images (Google Books / Archive.org style), rather than real typeset text. Spot-checking the
  extracted text found OCR misreads throughout (e.g. "With an appendix" read as "Willi an
  appendix"), including inside mathematical expressions where a misread digit or symbol is far more
  costly than in prose. Converting it would just capture this same imperfect OCR text, not improve
  it, so - per the same "a wrong symbol is worse than a gap" principle as the CLRS conversion - it
  stays a PDF. Read it directly; a $199.99 print / $71.99 e-book rental copy is also on reserve at
  Stauffer Library per the course outline above, which would be a more reliable source to transcribe
  from than this scan if particular sections turn out to be worth filing properly.

## Notation / conventions specific to this professor

(e.g. whether $z = x+iy$ or $z = re^{i\theta}$ is the default working form in this course,
specific contour-orientation conventions)

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).
All math in this course should be filed in LaTeX per the root `CLAUDE.md` rule.

- Week 1: *(no lecture material filed yet - only the course outline)*

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — distinguishing removable/pole/essential
singularities and setting up the correct contour for residue-based real-integral evaluation are
common sticking points.

-
