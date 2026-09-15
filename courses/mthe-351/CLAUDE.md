# MTHE 351 — Probability I

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** MTHE 351 — Probability I
- **Calendar description:** Introduction to probability theory and its applications in engineering
  science: basic concepts of probability, counting, conditional probability, Bayes' rule,
  independence; probability models; random variables, distribution functions, probability mass
  functions, probability density functions; expectation, variance, moments; jointly distributed
  random variables; transformations of random variables. Distributions: Bernoulli, binomial,
  geometric, negative binomial, Poisson, uniform, exponential, normal. Applications: elementary
  stochastic processes, noisy communication channels. (Lec: 3, Lab: 0, Tut: 0.5).
- **Format:** Lectures **Tue 8:30 (Dupuis 215), Wed 12:30 (Jeff 126), Fri 9:30 (Dupuis 215)**;
  tutorial **Wed 13:30 (Jeff 126)**. 3.5 units.
- **Exclusions:** ELEC 326 (Probability and Random Processes covers overlapping material)
- **Actual topics** (from the Fall 2026 syllabus, with text chapters and weeks):
  1. **Basic concepts of probability theory** - axioms of probability; counting; conditional
     probability; law of total probability and Bayes' rule; independence of events.
     (Ch. 1, SS2.1-2.4, Ch. 3 - weeks 1-4)
  2. **Discrete random variables** - random variables; distribution functions; expectation and
     variance; uniform, Bernoulli, binomial, negative binomial, Poisson, geometric.
     (Ch. 4 and 6 - weeks 4-8)
  3. **Continuous random variables** - probability density functions; functions of random
     variables; expectation and variance; uniform, normal, exponential.
     (Ch. 5, SS7.1, 7.2, 7.4 - weeks 8-10)
  4. **Pairs of random variables** - joint distributions; independent random variables;
     conditional distribution and expectation; functions of two random variables.
     (SS8.1, 8.4, 8.5 - weeks 10-12)
- **Professor:** **Fady Alajaji** - `fa@queensu.ca`, office hours **Wed 10:30-11:30**.
  TA and marker: Ananya Omanwar (`22aso1@queensu.ca`); second marker: Jonas Schuppert
  (`26qtd1@queensu.ca`).
- **Term:** Fall 2026
- **Assessment:** Homeworks **10%** (10 of them, via **Crowdmark**), Quiz 1 **20%**, Quiz 2 **20%**,
  final exam **50%**. **Quiz 1: Fri 9 Oct 2026, 9:30-10:20. Quiz 2: Wed 4 Nov 2026, 13:30-14:20**
  (in the tutorial slot, not a lecture slot). No makeups - a missed quiz with a valid reason has its
  weight moved to the final. Final is run by the Exams Office.
- **Textbook:** F. Ghahramani, *Fundamentals of Probability with Stochastic Processes*, **5th ed.**,
  Chapman and Hall/CRC, 2024. All chapter references in the syllabus are to this edition.
- **GenAI policy:** permitted **for homework assignments only**, as an educational tool; students
  must critically evaluate output and ensure submitted work reflects their own understanding.
  Nothing permissive is said about the quizzes or final, which are 90% of the grade.

## Reference materials

- `references/syllabus-f2026.md` (+ `.pdf`) - the Fall 2026 syllabus, converted and restructured.
  **Check it before answering anything about dates or weighting.**
- `references/ghahramani-5e-fundamentals-of-probability.pdf` - the course textbook (F. Ghahramani,
  *Fundamentals of Probability with Stochastic Processes*, 5th ed.), matching the syllabus's chapter
  references (Ch. 1/3 weeks 1-4, Ch. 4/6 weeks 4-8, Ch. 5/§7 weeks 8-10, §8 weeks 10-12). 699 pages,
  confirmed against the syllabus's own outline (bookmarks: Ch. 1 Axioms of Probability, Ch. 2
  Combinatorial Methods, Ch. 3 Conditional Probability... matches "Ch 1, §2.1-2.4, Ch 3" for weeks
  1-4 given the book's own ch. 2 = counting).

  **Deliberately kept as a PDF - conversion was attempted and discarded.** This is an old
  TeX/dvips-produced PDF: its math fonts (CMMI10, CMSY10, CMEX10, MSAM10 - classic Computer Modern
  math italic/symbol/extension fonts) are embedded with **no ToUnicode CMap at all**, so text
  extraction has nothing correct to fall back on and silently substitutes wrong-but-plausible
  Unicode letters for math variables and symbols throughout - e.g. the sample space "S" extracts as
  "τ", subset "⊆" extracts as "⊃" (the **opposite** direction), "∈" extracts as arbitrary Greek
  letters. This is pervasive (every math variable and symbol in the book), not isolated, and differs
  from CLRS's issue (which had a *repairable* broken ToUnicode map): here there is nothing to repair
  from, only glyph-shape identification per font, per the `build_glyph_map.py` workflow - across
  six different fonts with no existing per-book map, which is a substantial undertaking not
  attempted here. **A silently wrong symbol is worse than an unconverted PDF**, so the conversion
  was discarded rather than filed. Read this one from the PDF directly; ask before starting a
  glyph-map pass on it if reliable searchable notes from it become worth the investment.
- **The lecture notes are handwritten tablet notes, and this matters for every filed lecture.**
  Each `lectures/*.pdf` is a stylus-written PDF whose only text layer is **Apple's handwriting
  recognition** - it drops every space and mangles symbols (`AUB= [xeS:AonB(orboth)}` for
  $A \cup B$). The filed `.md` beside each one is therefore a **reconstruction**, not a mechanical
  extraction, and each carries a fidelity warning at the top. **The PDF is always the authority.**
  Passages that could not be recovered confidently are left as `<!-- unclear: ... -->` comments -
  never silently guessed.
- **No figures can be extracted from the lecture PDFs.** The handwriting and the Venn diagrams are
  **vector paths**, not embedded images, so `pdf_to_md.py` finds nothing to pull out, and this
  environment has no PDF page renderer (`pdftoppm`/poppler, PyMuPDF and `pypdfium2` are all absent).
  Every place the original draws a diagram is marked `**[Venn diagram in original]**` in the note.
  Recovering the figures would need `pypdfium2` installed to rasterise pages - **ask Gabe first.**

## Notation / conventions specific to this professor

- **Juxtaposition means intersection:** the professor writes $AB$ for $A \cap B$ throughout, and
  uses it heavily from Lecture 2 onward.
- Set difference is written $A - B$ (with $A \setminus B$ given as an alternative).
- The sample space is $S$ (not $\Omega$), the event space is $\mathcal{F}$, and a probability
  space is the triplet $(S, \mathcal{F}, P)$.

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).
This course feeds directly into your existing quant/trading work (QUANTT, options strategy
research) — the `concept-map` skill is worth using here to trace how topics connect to material
you already use in that context.

- **Lecture 1 (2026-09-08):** *Introduction & review of basic set theory.* Why probability needs an
  **axiomatic** treatment - intuitive/subjective probability varies between people, so the theory is
  built from axioms (intuition still guides which axioms and how to interpret results). Then a full
  set-theory review: membership and set-builder notation, the empty set, subsets, the **principle of
  set equality** ($A = B \iff A \subseteq B$ and $B \subseteq A$), universe and complement, union,
  intersection, disjoint/mutually exclusive sets, set difference ($A - B = A \cap B^c$), Cartesian
  products, and the properties list - commutativity, associativity, distributivity, **De Morgan's
  laws**.
- **Lecture 2 (2026-09-09):** *Sample space and events* - begins **Unit I: Axioms of Probability**.
  Random experiment; **sample space** $S$; **events** as subsets of $S$. The set-theory/probability
  dictionary (universal set $\to$ sample space, subset $\to$ event, $S$ = **certain event**,
  $\emptyset$ = **impossible/null event**), and events as statements ($E^c$ = does not occur,
  $E \cup F$ = at least one, $E \cap F$ = both, $E - F$ = $E$ but not $F$, $E \subseteq F$ = "$E$
  implies $F$"). Two ideas do the real work: **one experiment can have several valid sample spaces**
  depending on what you record (3 coin flips: sequence vs. number of heads), and **sample spaces
  need not be finite** (a continuous interval; the roll-until-6 space, which mixes countably many
  finite blocks with infinite non-terminating sequences). Worked: "exactly one of $E$, $F$ occurs"
  $= (E-F) \cup (F-E) = (E \cup F) - (E \cap F)$, proved algebraically.
- **Lecture 3 (2026-09-11):** *Axioms of probability.* Why **relative frequency**
  $P(E) = \lim_{n\to\infty} n(E)/n$ fails as a definition (can't repeat indefinitely; limit may not
  exist; no guarantee of the same limit later). **Event space / $\sigma$-field** $\mathcal{F}$:
  contains $S$, closed under complement and **countable** union; consequences ($\emptyset \in
  \mathcal{F}$, closure under finite union and under finite/countable intersection via De Morgan);
  examples $\{\emptyset, S\}$ and the power set. **The three axioms** - non-negativity, $P(S)=1$,
  **countable additivity** - and the **probability space** $(S, \mathcal{F}, P)$. Derived:
  **Theorem 1** $P(\emptyset)=0$; **finite additivity** (a *theorem*, derived from countable
  additivity plus Theorem 1 - not an axiom); **Theorem 2** $P(E^c) = 1 - P(E)$; corollary
  $0 \le P(E) \le 1$. **Equally likely outcomes** give $P(\{s_i\}) = 1/N$ and **Theorem 3**
  $P(E) = |E|/N$ - the counting formula is a *theorem valid only under the equally-likely assumption
  on a finite sample space*, not a definition. Examples: fair coin, sum of two dice $=7$, exactly 2
  tails in 3 flips, and a **non**-equally-likely race worked straight from the axioms.
- **Problem Set 0 issued** - *Practice* only, not submitted, not graded; the drill set for Lecture 1
  (elementary set theory). `problem-sets/ps00-elementary-set-theory.md`.
- **Homework 1 issued** - **due Mon 21 Sep 2026**, submitted via **Crowdmark**, 1 of 10 homeworks.
  Covers lectures 2-3. `problem-sets/ps01-sample-spaces-events-and-axioms.md`. **Its source file was
  misnamed `hw1_mthe_251.pdf`** - the document is headed "MTHE 351" and there is no MTHE 251; the
  "251" is a typo for 351.
- **Homework 1 in progress.** Gabe's own attempt is
  `problem-sets/Hw1_MTHE351_Gabe_Soler.md` (submission-style filename, deliberately kept outside the
  `psNN-` convention). Worked solutions to all six questions are in
  `problem-sets/ps01-sample-spaces-events-and-axioms-worked.md` - **mine, not an official key**;
  the course issues none. The syllabus permits GenAI **for homework only**, so this is within policy,
  but submitted work must be his own.

  > ⚠️ **Misconception caught on Q1 (2026-09-14):** the first attempt enumerated the urn draws
  > **with** replacement (outcomes like `[1,1,1,1,1]`), where the question says **without**
  > replacement. Worth re-checking on the next sampling question - see "Known trouble spots".
- **Next up:** counting, conditional probability, law of total probability and Bayes' rule,
  independence (weeks 1-4 material, Ch. 1 / SS2.1-2.4 / Ch. 3 of Ghahramani).

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — setting up the correct sample space for
combinatorics problems and correctly identifying independence vs. mutual exclusivity are common
sticking points.

- **Sampling with vs. without replacement** (HW 1 Q1, 2026-09-14). Enumerated the sample space with
  repeated labels when the question specified drawing **without** replacement. **Worth a quiz
  question:** give two near-identical urn problems differing only in replacement and check the
  sample-space sizes come out different.
- **Boundary wording in stopping rules** (same question). "Exceeds 4" means **strictly** $> 4$, so a
  first draw of 4 does *not* stop the experiment - the question spells this out in a bracketed note
  precisely because it decides three outcomes. Read stopping conditions literally.
