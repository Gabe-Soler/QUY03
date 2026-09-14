# ENPH 334 — Electronics for Applied Scientists

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** ENPH 334 — Electronics for Applied Scientists
- **Official description:** The design of electronic circuits and systems using commonly available
  devices and integrated circuits. Properties of linear circuits, with particular reference to the
  applications of feedback and operational amplifiers.
- **Prerequisites:** ENPH 316 (PHYS 316)
- **Exclusions:** ENPH 312 (PHYS 312), MTHE 338 (MATH 338), MTHE 334 (MATH 334), MTHE 335 (MATH
  335)
- **Typical topics** (fill in / correct against your actual syllabus): op-amp fundamentals
  (ideal vs. real op-amps, golden rules), negative feedback theory and stability, filter design
  (active filters), amplifier configurations, oscillators, basic semiconductor devices (diodes,
  BJTs/MOSFETs) as used in these circuits, signal conditioning circuits.
- **Professor:** Dr. Bhavin Shastri (lectures, course admin)
- **Term:** Fall 2026
- **Cross-listed as:** PHYS 334 (lab manuals are issued under "ENPH 334/PHYS 334")
- **Main textbook:** Storey (Week 1 readings are chapters 3-6). Alternatives named in the lab
  overview: *The Art of Electronics* (Horowitz & Hill) and *Principles and Applications of
  Electrical Engineering* (Rizzoni & Kearns).
- **Teaching team:** Arpan Sur (quizzes, exam); lab TAs Fraser McCauley (lab admin, Mon/Wed AM),
  Sam Lamontagne (Wed PM/Thurs), Ammar Ibrahim (Mon/Wed AM, notebook grading), Cameron Ingo
  (Wed PM/Thurs, notebook grading).
- **Labs:** Stirling 405, in pairs. Four assessed components - weekly completion (binary), lab
  notebook (Week 4 feedback / Week 11 graded), two design projects (analog Week 8, digital
  Week 11), end-of-term lab test. Labs are 36% and are all-or-nothing on completion.

## Notation / conventions specific to this professor

- **Simulation tool: LTspice** (switched from OrCAD in 2023). Lab instructions are written for
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
- **Week 1 readings:** Storey chapters 3-6. Thevenin's theorem and AC/phasor analysis are flagged
  as the prerequisites for the first two labs.
- **Not yet filed:** Week 2A course notes (the Lab A0 manual says the gain/phase formulae are
  derived there).

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — feedback stability analysis and
non-ideal op-amp behavior are common sticking points in courses like this.

-
