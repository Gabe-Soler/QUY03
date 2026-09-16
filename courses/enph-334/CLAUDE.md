# ENPH 334 — Electronics for Applied Scientists

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** ENPH 334 — Electronics for Applied Scientists
- **Official description:** The design of electronic circuits and systems using commonly available
  devices and integrated circuits. Properties of linear circuits, with particular reference to the
  applications of feedback and operational amplifiers.
- **Format:** **F 3-1.5-0.5; 5.0 units** (0/0/0/27/27). Lectures **KINGST 101**, 3 h/week on
  **Tue, Wed and Fri in the 14:30-17:30 band** (the exact hour per day is reconstructed from the
  timetable grid - confirm against SOLUS). Tutorial/quizzes **Tue 11:30-12:30, MACDON 1**. Labs
  3 h/week in **Stirling 404/405**: L005 Mon 08:30, L004 Wed 08:30, L003 Thu 11:30, L002 Wed 18:30.
  Expected load **10 h/week** including 3 h preparation.
- **Prerequisites:** **ELEC 221** (ENPH 334) / PHYS 239 (PHYS 334).
  *(This file previously said "ENPH 316 (PHYS 316)" from the calendar - the syllabus says ELEC 221.
  Corrected 2026-09-14.)*
- **Exclusions:** **ENPH 333 (PHYS 333)**.
  *(Previously listed ENPH 312 and MTHE 338/334/335 - those came from the wrong calendar entry
  entirely. Corrected 2026-09-14.)*
- **Actual topics** (from the Fall 2026 syllabus). Two halves:
  1. **Analog** - review of basics (KCL/KVL, Thevenin, capacitors, phasors, complex AC); R-C
     circuits, diodes, **dB and Bode plots**, generalized amplifiers; **op-amps** and op-amp
     circuits; op-amp parameters (slew rate, rise time, bandwidth), noise and EMC; comparators,
     the **555 timer**, feedback basics, differential amplifiers, input/output impedance; effects
     of **negative feedback**; **active filters**.
  2. **Digital** - number systems and binary arithmetic; digital gates, switch debouncing,
     multivibrators; **Boolean algebra**, TTL and CMOS characteristics, adders, latches,
     **flip-flops**; **D/A conversion**, counters, counter decoding; ripple counters, modulo-N,
     up/down, synchronous, **shift registers**; **A/D conversion**; **memory**.
- **Professor:** **Prof. Bhavin J. Shastri** - Stirling 308F, `bhavin.shastri@queensu.ca`.
  Slides are the primary course material, posted weekly.
- **Term:** Fall 2026
- **Assessment:** final exam **40%**, quizzes **21%** (4, **best 3 of 4**, in the Tuesday tutorial,
  **open-book and open-notes**, no electronic devices), design projects **24%** (analog 10% due
  week 8, digital 14% due week 11), **lab test 8%** (20 min hands-on, week 12, includes simulation
  questions), **lab notebook 7%** (feedback-only in week 4, marked week 11).
  **Quiz dates: Tue 29 Sep, Tue 20 Oct, Tue 10 Nov, Tue 1 Dec.**
  **Calculator policy: the non-communicating Casio 991 series is the ONLY permitted calculator.**
- **Cross-listed as:** PHYS 334 (lab manuals are issued under "ENPH 334/PHYS 334")
- **Main textbook:** Storey (Week 1 readings are chapters 3-6). Alternatives named in the lab
  overview: *The Art of Electronics* (Horowitz & Hill) and *Principles and Applications of
  Electrical Engineering* (Rizzoni & Kearns).
- **Teaching team:** Arpan Sur (quizzes, exam); lab TAs Fraser McCauley (lab admin, Mon/Wed AM),
  Sam Lamontagne (Wed PM/Thurs), Ammar Ibrahim (Mon/Wed AM, notebook grading), Cameron Ingo
  (Wed PM/Thurs, notebook grading).
- **Labs:** Stirling **404/405**, in **fixed pairs for the whole term** (register the team with the
  TA in the first lab). Attendance is **mandatory and recorded**; missed labs must be made up in
  another session. Completion needs a TA sign-off **and** a check-off in the attendance register.
  **The lab section is 39%** (design projects 24 + lab test 8 + notebook 7) and is
  **all-or-nothing**: if all labs are not completed satisfactorily, the whole 39% is zeroed.

  > ⚠️ **Contradiction between course documents.** This file previously recorded **36%**, from the
  > lab-overview deck. The syllabus states **39%** explicitly and its components sum to 39. Going
  > with 39%, but the two documents genuinely disagree - worth confirming with the Head TA.

## Folder layout for this course

**This course splits lab material into its own `labs/` folder**, because the labs are a major
graded component rather than incidental to the lectures:

```
courses/enph-334/
|-- labs/           # lab manuals, lab handouts, marking schemes, lab-book guidance
|-- problem-sets/   # problem sets and tutorial/class problems, with their solutions beside them
|-- lectures/
|-- references/     # syllabus and other source material
`-- summaries/
```

- **Labs go in `labs/`, problem sets in `problem-sets/`** - do not mix them. Anything issued as a
  lab manual, lab handout or lab-assessment document is lab material even when it contains
  problems to work through.
- **Frontmatter `type:` stays `problem-set`** for lab material - the repo's schema in the root
  `CLAUDE.md` is unchanged, only this course's folder layout differs. This follows the precedent
  `cmpe-320` set with its `assignments/` folder.
- **Solutions sit beside the thing they solve**, under the same basename plus `-solutions`, rather
  than in `references/`. The root `CLAUDE.md` sends *book-length* solution manuals to `references/`;
  a three-page solution set to one week's problems is far more useful adjacent to the problems.

- Lab filenames are `lab-{id}-short-topic.md`, using the course's own lab identifiers
  (`lab-a0-...`, `lab-a1-...`) rather than a repo-invented number, since the manuals are issued and
  referred to by those ids.
- Problem-set filenames follow the repo's `psNN-short-topic.md`. Note this course runs **two
  parallel problem streams** - "Week N Problems" and "Class Problems, Week N" - which are different
  documents covering different material in the same week; keep both, and say which is which in the
  topic slug.

## Notation / conventions specific to this professor

- **Simulation tool: LTspice** - the syllabus calls it "strongly preferred" over OrCAD, and OrCAD
  is **Windows-only** (the syllabus tells Mac users to dual-boot; ignore that, use LTspice).
  **Note the syllabus's own CLO 05 still says "OrCAD" - a stale learning outcome**, contradicted by
  its own simulation note and by Lab A0 being an LTspice lab. Simulation is examined: **the lab
  test includes circuit simulation questions**. Lab instructions are written for
  Windows/Linux; the macOS build has the same capability but different menus - Gabe is on macOS,
  so translate menu paths or use the lab machines.
- Lab work is organized into numbered **Tasks** that are the deliverables and are checked off
  individually by a TA during the session.
- Lab manuals use $V_{Th}$ / $R_{Th}$ for Thevenin quantities and quote low-pass gain as
  $A_v = 1/\sqrt{1+(\omega RC)^2}$ with phase $\phi = -\arctan(\omega RC)$.

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).

- **Week 0 / lab orientation (2026-09-08):** lab structure and logistics; goal of the labs is
  instrument fluency (breadboard, function generator, multimeter, oscilloscope); practical
  electronics framing - circuit diagrams are models, real components have parasitics (every
  capacitor is an inductor at high enough frequency and vice versa), always check datasheets and
  measure components. Bench specifics: red breadboard rails are +/-15 V (op-amp supplies) and
  +5 V (digital logic), BNC for signals, never connect the rails to the function generator.
- **Lab A0 (LTspice), assigned Week 1:** the three SPICE analyses - `.op` (DC operating point),
  `.tran` (time-domain transient), `.ac` (frequency-domain sweep) - applied to a Thevenin
  resistor network and an RC low-pass ($R = 5$ k$\Omega$, $C = 100$ nF, $f_c \approx 318$ Hz).
  **Prelab calculations filed** (2026-09-15): `labs/lab-a0-prelab-calculations.md` - all three
  tasks derived in full ($V_{Th}=5$ V, $R_{Th}=750\,\Omega$ for the Thevenin network; $A_v=0.303$,
  $\phi=-72.3°$ at 1 kHz for the RC low-pass; $f_c=318.3$ Hz with phase always $-45°$ at cutoff for
  any single-pole RC low-pass). The theory half only - still needs the actual LTspice runs to
  compare against.
- **Week 1 readings:** Storey chapters 3-6. Thevenin's theorem and AC/phasor analysis are flagged
  as the prerequisites for the first two labs.
- **Week 1 problem sets filed (both streams).** `problem-sets/ps01-week1-problems-dc-fundamentals`
  (Ohm's law, voltage divider, KCL and a 2 W power-rating check, Thevenin by superposition, a
  series R-C phasor problem, an RC charge/discharge, and a complex-number evaluation) and
  `problem-sets/ps02-week1-class-problems-thevenin-superposition` (Thevenin, superposition, and
  Storey Ex. 6.24 - a 5 k / 100 nF series R-C at 500 Hz solved by phasor diagram). **Solutions are
  filed beside each.** The ps02 solutions carry a bonus **week 2 successive-Thevenin-reduction**
  worked example on their last page.
- **Lab A1 filed** (`labs/lab-a1-resistors-capacitors-diodes`), the **week 3** lab: measure a
  Thevenin equivalent with both a multimeter and an oscilloscope, find the **-3 dB point and phase
  shift** of a Thevenin RC circuit (using $R_T$, not the raw resistor, in the $f_{3dB}$
  calculation), and take forward/reverse **I-V characteristics for a silicon diode and an LED**.
  Manual revised **September 2024** - a carry-over from a previous offering.
- **Lab-book rubric filed** (`labs/00-lab-book-marking-and-debugging`): six sections each marked
  out of 5, plus a debugging checklist. **Version 2 is dated 2017** and predates the current
  instructor, but it is still the operative rubric.
- **Not yet filed:** Prof. Shastri's weekly lecture slides - the *primary* course material, and the
  Week 1/2 course notes that Lab A0 and the ps01 Q6 switch diagram both refer to.

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — feedback stability analysis and
non-ideal op-amp behavior are common sticking points in courses like this.

-
