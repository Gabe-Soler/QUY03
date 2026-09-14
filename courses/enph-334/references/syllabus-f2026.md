---
course: enph-334
type: reference
date: 2026-09-14
tags: [syllabus, electronics, op-amps, digital-logic, labs, design-projects, quizzes, lab-notebook, marking-scheme, ltspice, calculator-policy]
source: Course_Information_2026_enph334.pdf
---

# ENPH 334 / PHYS 334 — Electronics for Applied Scientists and Physicists (Fall 2026 Syllabus)

> Source: `syllabus-f2026.pdf` (10 pp.), kept beside this note. No figures in the PDF.
> **This note is the authority for dates and weighting** — and it **corrects several things**
> previously recorded in `../CLAUDE.md` from the lab-overview deck. See "Corrections" at the end.

## TLDR

**The lab section is 39% of the grade and is all-or-nothing on completion** — if all labs are not
completed satisfactorily, the entire 39% is zeroed regardless of how well the individual pieces
went. The rest is a **40% final exam** and **21% of quizzes** (four, best three count, open-book,
in the Tuesday tutorial).

Two design projects carry most of the lab weight (analog 10% in week 8, digital 14% in week 11),
with a 20-minute hands-on lab test (8%) in the last week and the lab notebook (7%) marked in week
11 — submitted for **feedback only** in week 4. Labs are in **fixed pairs for the whole term** and
attendance is mandatory and recorded.

## Course overview

The objective is an introduction to basic **analog and digital electronics**. The course is in two
parts:

- **Analog** — applied electronics with an emphasis on **operational amplifier circuits**.
  Following a brief review of basic components: op-amp circuits, the effects of **feedback** to
  produce different mathematical operations, and applications as **amplifiers and filters**.
- **Digital** — **binary arithmetic and Boolean algebra**, then gates, latches, flip-flops,
  counters, shift registers, **DACs and ADCs**, and finally memory in electronic circuits and
  computers.

## Teaching team

**Instructor: Prof. Bhavin J. Shastri** — Stirling 308F, `bhavin.shastri@queensu.ca`

Five TAs, who are the **primary contact for the labs and quizzes**:

| TA | Role | Email |
|---|---|---|
| **Fraser McCauley** | **Head TA** — labs | `fraser.mccauley@queensu.ca` |
| Sam Lamontagne | labs | `gqb5@queensu.ca` |
| Ammar Ibrahim | labs | `bv56@queensu.ca` |
| Cameron Ingo | labs | `23vqp@queensu.ca` |
| Arpan Sur | **quizzes** / labs | `bv56@queensu.ca` |

> 📝 **Ammar Ibrahim and Arpan Sur are both listed with `bv56@queensu.ca`.** One of the two is
> wrong — this is the same kind of copy-paste slip as the rotated TA emails in the CMPE 320
> syllabus. Confirm before emailing either.

## Course identity

**ENPH 334 Electronics for Applied Scientists — F 3-1.5-0.5; 5.0 units**
(0/0/0/27/27 — 27 Engineering Science, 27 Engineering Design)
**Prerequisite: ELEC 221. Exclusion: ENPH 333 (PHYS 333).**

**PHYS 334/3.0 Electronics for Physicists** — Learning hours 132 (36L; 36Lb; 12T; 48P).
Prerequisite: PHYS 239/3.0.

## Schedule

| | Day | Time | Room |
|---|---|---|---|
| **Lecture** | Tuesday | 14:30 – 15:30 | KINGST 101 |
| **Lecture** | Wednesday | 16:30 – 17:30 | KINGST 101 |
| **Lecture** | Friday | 15:30 – 16:30 | KINGST 101 |
| **Tutorial / Quizzes** | **Tuesday** | **11:30 – 12:30** | **MACDON 1** |
| Lab 005 | Monday | 08:30 – 11:30 | Stirling 404/405 — Fraser/Ammar |
| Lab 004 | Wednesday | 08:30 – 11:30 | Stirling 404/405 — Fraser/Ammar |
| Lab 003 | Thursday | 11:30 – 14:30 | Stirling 404/405 — Sam/Cameron |
| Lab 002 | Wednesday | 18:30 – 21:30 | Stirling 404/405 — Sam/Cameron |

<!-- unclear: the lecture DAYS are certain (the three "Lecture" cells sit unambiguously in the
     Tuesday, Wednesday and Friday columns), but the row alignment of single-line cells in the
     timetable grid is offset by a constant 22 units from the row labels, so the day-to-hour
     mapping above is reconstructed from that geometry rather than read directly. The lectures are
     certainly within the 14:30-17:30 band in KINGST 101. Confirm the exact hour per day against
     SOLUS. The tutorial slot is independently confirmed: all four quiz dates fall on Tuesdays. -->

Expected weekly load, per the syllabus: **lectures 3 h + tutorials 1 h + labs 3 h + preparation
3 h = 10 hours/week**. "For every lecture hour, students should plan to spend an additional hour
reinforcing key concepts."

## Marking scheme

| Component | Weight |
|---|---|
| **Final exam** | **40%** |
| Quizzes (×4, **best 3 of 4**) | **21%** |
| Design projects (×2) | **24%** |
| Laboratory test | **8%** |
| Laboratory notebook | **7%** |
| **Total** | **100%** |

> ⚠️ **The lab section is 39%** — design projects 24% + lab test 8% + notebook 7%. The syllabus
> states it explicitly: *"If all labs are not completed satisfactorily, then a zero mark will apply
> to the entire lab section of the course (39%)."*
>
> **This corrects the 36% previously recorded in `../CLAUDE.md`**, which came from the lab-overview
> deck. 24 + 8 + 7 = 39, and the syllabus names the figure, so 39% is the one to trust — but the
> two course documents genuinely disagree, so it is worth confirming with the Head TA.

### Quizzes — 21%

Four quizzes during the term, **administered during the scheduled tutorial sessions**. Equally
weighted; **your best three of four count**.

> **Open-book and open-notes. Laptops, phones, tablets and other electronic devices are not
> permitted.**

| Quiz | Date | Weekday |
|---|---|---|
| Quiz 1 | **29 September 2026** | Tuesday (week 4) |
| Quiz 2 | **20 October 2026** | Tuesday (week 6) |
| Quiz 3 | **10 November 2026** | Tuesday (week 9) |
| Quiz 4 | **1 December 2026** | Tuesday (week 12) |

> 📝 The timetable prints "Quiz 4 (Dec. 1)" in the **week 11** row, but 1 December falls in week 12
> (the week of 30 November). The date is what matters; the row placement is a slip.

### Laboratory work

- **Labs start in week 2.** *(The syllabus says "Labs will start on Sep. 14, **2024**" — a stale
  year carried over from a previous offering. 14 September **2026** is a Monday and is the start of
  week 2, which matches the timetable, where week 1 has no labs.)*
- **Teams of two**, your own choice of partner, but **you must keep the same partner all term**.
  Register your team with the TA in the first lab. PHYS and Applied Maths students are encouraged
  to partner with ENPH students.
- **Attendance is mandatory and is taken.** Missed or incomplete labs **must be made up in another
  lab session** — arrange it with the TAs.
- **Completion evidence:** (a) a sign-off or initial in the lab by a TA, and (b) a corresponding
  check-off in the attendance register.
- ⚠️ **All labs must be completed. If they are not, a zero applies to the entire 39% lab section.**

### Design projects — 24%

| Project | Weight | Assigned | Due |
|---|---|---|---|
| **Analog** | **10%** | week 6 | week 8 |
| **Digital** | **14%** | week 9 | week 11 |

On the due date students get **20 minutes of lab time to test and troubleshoot**, after which the
TAs evaluate the project. A **written report with the course cover sheet** must also be submitted,
containing: a brief description of the circuit, circuit diagram, **transfer function** (an equation
relating output to input), calculations for circuit components, a summary of the purpose and
functionality of the design, and references.

Evaluated on: report handed in; presentation in the lab and discussions; circuit construction;
correct circuit operation. The marking scheme is posted on OnQ. **A standard ENPH334/PHYS334 title
page must be used and signed.**

### Laboratory test — 8%

A **20-minute, hands-on, individual** exercise in the **last week of term**, demonstrating
familiarity with the lab equipment and the ability to make basic electronic measurements. **It
includes circuit simulation questions** (see the simulation note below).

### Laboratory notebook — 7%

An **electronic** notebook is required (Google Docs, OneNote with Jupyter Notebooks, or a physical
notebook **scanned to PDF**), so it can be shared easily. Front cover: name, lab section, group.

- **Week 4 — submit for feedback only** (no mark).
- **Week 11 — marked**, though it may be requested earlier at the instructor's or TAs' discretion.

The standard: a TA must be able to **reproduce what you did using nothing but your book**. Checked
for **completeness** — table of contents, numbered pages, circuit diagrams, labeled and titled
graphs, and a summary of each lab.

The syllabus asks for four kinds of content: **objective** information (apparatus sketches, circuit
diagrams, instrument settings, data filenames, plots, experimental conditions); **subjective**
information (your interpretation or evaluation of what happened); **analysis** (preliminary
analysis performed on raw data throughout); and **planning** (plans or directions for the
experiment).

Specifics called out:
- Numbered pages and a table of contents.
- **Circuit diagrams with component values prepared *before* the lab**, drawn before wiring, and
  including **device pin numbers**.
- Labeled waveform sketches, including scales.
- Tables of data with descriptive titles; formats can be prepared beforehand.
- Graphs with titles and properly labeled axes, **drawn as you take measurements** — early results
  guide which measurements to take next and save lab time.
- Summaries and comments on each circuit's operation, with enough circuit analysis to compare data
  against expected behaviour and discuss discrepancies. A detailed error discussion is **not**
  required; **agreement within 5–10% is expected**.

No need to copy instructions from the lab sheets if the sheets are **permanently fastened** into
the book — but **explicitly note any variation from them**. Record a reference for anything taken
from the lab data books, the web, or elsewhere.

## Course timetable

| Week | Lectures / theory | Lab | Comments |
|---|---|---|---|
| **1** — Sep 7 | Review of basics; resistors; **KCL and KVL**; **Thévenin's theorem**; capacitors; **phasors**; complex AC circuits; lab equipment | *no labs* | Tutorial covers the lab overview (Fraser McCauley) |
| **2** — Sep 14 | Review phasors; **R-C circuits**; diodes; **decibel (dB)**; **Bode plots**; generalized amplifiers | **A0 — Simulation Intro** | Tutorial covers lecture material |
| **3** — Sep 21 | **Op-amps**; op-amp circuits | **A1 — Resistors, Capacitors, Diodes** | Tutorial covers lecture material |
| **4** — Sep 28 | Op-amp parameters (**slew rate, rise time, bandwidth**); noise and EMC | **A2 — Inverting Amplifier and Voltage Follower** | **Quiz 1 (Sep 29)**; **submit lab notebooks for feedback** |
| **5** — Oct 5 | **Comparators**; **555 timer**; feedback basics; differential amplifiers; input and output impedance | **A3 — Summing Amplifiers (hardware) and the 555 Timer (simulation)** | |
| | **Thanksgiving and Fall Term Break — Oct 12–16** | | |
| **6** — Oct 19 | **Effects of negative feedback**; **active filters** and their response | **A4 — Simple Comparator and Window Comparator** | **Quiz 2 (Oct 20)**; **analog lab projects assigned** |
| **7** — Oct 26 | **Number systems**; binary arithmetic; **digital gates**; switch debouncing; multivibrators | Analog project work | Tutorial to troubleshoot design projects |
| **8** — Nov 2 | **Boolean algebra**; **TTL and CMOS** characteristics; adders; **latches**; **flip-flops** | **Analog project presentation** | Tutorial goes over practice problems |
| **9** — Nov 9 | Flip-flops; **D/A conversion**; counters; counter decoding | **D1 — Gates & Latches, NAND, AND, Full Adder (simulation), Clocked RS and JK Flip-Flops** | **Quiz 3 (Nov 10)**; **digital lab projects assigned** |
| **10** — Nov 16 | **Ripple counters**; modulo-N; up/down; synchronous; **shift registers**; serial-parallel; parallel-load shift register | **D2 — Ripple Counter and D/A Conversion (hardware)** | Tutorial to troubleshoot design projects |
| **11** — Nov 23 | **A/D conversion** — terminology, circuits, methods | **Digital project presentation** | **Lab notebooks marked** |
| **12** — Nov 30 | **Memory** — terms and acronyms, digital memory, PC memory | **Lab test** | **Quiz 4 (Dec 1)**; tutorial goes over practice problems |

## Circuit simulation

> **Electronic circuit simulation is part of the lab course**, using **LTspice (strongly
> preferred)** or OrCAD with PSpice. Apart from the introductory labs in **week 2, which are all
> simulation**, the other simulation labs have only **part** of the lab done in LTspice.
> **Therefore the lab test will include circuit simulation questions.**

- LTspice is free: <https://www.analog.com/en/design-center/design-tools-and-calculators/ltspice-simulator.html>
- OrCAD is installed on all lab workstations and is **Windows only**. The syllabus tells Mac users
  to dual-boot or use the lab machines.

> 🔑 **Gabe is on macOS — use LTspice**, which the syllabus already calls "strongly preferred", and
> ignore the OrCAD dual-boot advice entirely. See `../CLAUDE.md` on translating the manuals' menu
> paths to the macOS LTspice build.

> 📝 **CLO 05 is stale.** It reads "Have a working knowledge of the **OrCAD** circuit simulation
> software package", which contradicts note 1 above and the fact that **Lab A0 is an LTspice lab**.
> The course moved to LTspice; the learning outcome was not updated.

**Prior equipment familiarity.** The syllabus expects 334 students to already know the lab
equipment in Stirling 404/405; if not, it says to download and work through the **ENPH 333 Lab A0
(Lab Equipment)**.

## Course material

- **Slides** — Prof. Shastri's slides are the primary material, posted weekly.
- **Recommended textbook** — Neil Storey, *Electronics: A Systems Approach*, **6th edition**.
  **Buying new is not necessary**; an older edition suffices, as would any circuit textbook
  covering the listed topics.
- **Companion website** (free) — Storey 6e video library and multiple-choice practice:
  <https://wps.pearsoned.co.uk/ema_uk_he_storey_electronics_6/253/64880/16609466.cw/index.html>
  and <https://wps.pearsoned.co.uk/ema_uk_he_storey_electronics_6/253/64879/16609133.cw/index.html>
- **Legacy notes** — the previous instructor, **Prof. Jordan Morelli**, wrote two-part course notes
  on analog and digital electronics, posted on OnQ. Usable, but the course mainly follows Shastri's
  slides.

## Laboratory equipment

Each station in Stirling Hall has:

- A **breadboard unit** with three supplies: **+15 V at 0.5 A, −15 V at 0.5 A (or 1 A), and
  +5 V at 1 A** (Proto-board 203A / Project-board PP272 in Stirling; Global Specialities PB503 in
  the ILC).
- A **function generator** (HP 3311A, Global 2001, or BK Precision 3011 in Stirling; Global
  Specialities 105-2102 in the ILC).
- A **digital multimeter** (HP 3476A or Data Precision 1351 in Stirling; AW Sperry DM-8700 in the ILC).
- A **dual-trace oscilloscope** (Hitachi V-222 or V-252, both 20 MHz, in Stirling; Tektronix
  TDS 210, 60 MHz, in the ILC).
- Components, tools, wires; a bench DMM for resistance and a digital capacitance meter.
- A set of reference data books, **not to be removed from the lab** — cite them in your lab book if
  you use them.

## Learning outcomes

| CLO | Description | Indicator |
|---|---|---|
| 01 | Thorough understanding of current, voltage, resistance and **Ohm's law** | KB-NS (Electricity and Magnetism) |
| 02 | Analyze **DC circuits** using **Kirchhoff's laws** | KB-NS, IN-Analysis |
| 03 | Analyse **AC circuits** using complex representations — impedance, **RC filters**, decibels, tuned filters | KB-NS, IN-Analysis |
| 04 | Use an **Arduino** microcontroller to replicate a multimeter and an oscilloscope, and implement functional circuit designs | ET-Apply |
| 05 | Working knowledge of the ~~OrCAD~~ **LTspice** circuit simulation package *(see the stale-CLO note above)* | ET-Apply |
| 06 | Knowledge of voltage and current sources, **Thévenin's and Norton's theorems** | KB-NS |
| 07 | Analyse circuits containing **operational amplifiers**, and design complex circuits using op-amps as building blocks | PA-Solve, IN-Analysis |
| 08 | Analyse **digital electronics** — logic gates, flip-flops, counters, memory — with truth tables, **De Morgan's theorems** and **Boolean algebra** | PA-Solve, IN-Analysis |
| 09 | Create figures and diagrams for the design project reports | CO-Graphics |
| 10 | Use multiple strategies to solve an engineering problem as part of design projects | DE-Strategies, DE-Solutions |
| 11 | Deliver short presentations on the design projects | CO-Spoken |
| 12 | Work in **teams of two** to complete labs and design projects | TW-Contribution |

> 🔑 **CLO 04 mentions an Arduino**, which appears nowhere in the 12-week timetable. Either it is
> folded into a design project or it is another stale outcome — worth asking about before the
> analog project is assigned in week 6.

## Calculator policy

> **The only calculator permitted is the non-communicating Casio 991 series.**

This is the Arts & Science and Engineering standard. Calculators fall into three classes:
communicating (never permitted); non-communicating with text storage, graphing or long-term memory
(permitted only where significant written material is also allowed, and must carry a red sticker);
and non-communicating without those features (gold or blue sticker — except the Casio 991, which
needs no sticker).

## Administrative

- **Accommodations** — a note or form from Queen's Health Services or Queen's Counselling Services
  is required for quiz accommodations and extra time on the lab project or lab test. The instructor
  may also grant accommodations in exceptional circumstances (illness, court proceedings, other
  emergencies). Register with **Student Wellness Services** as early as possible.
- **Academic integrity** — five core values (honesty, trust, fairness, respect, responsibility).
  Sanctions range from a warning through loss of grades, course failure, to withdrawal.
- **Copyright** — course material is for registered ENPH 334 / PHYS 334 students' personal use and
  must not be distributed.

---

## Corrections to this repo's earlier notes

Everything below was recorded in `../CLAUDE.md` before this syllabus was filed, from the
lab-overview deck. The syllabus overrides it:

| Was recorded | Syllabus says |
|---|---|
| Labs are **36%** | **39%** (24 + 8 + 7), stated explicitly |
| Prerequisite **ENPH 316 (PHYS 316)** | **ELEC 221** |
| Exclusions **ENPH 312, MTHE 338/334/335** | **ENPH 333 (PHYS 333)** — the MTHE exclusions were from the wrong calendar entry |
| No units recorded | **5.0 units**, F 3-1.5-0.5 |
| Lab notebook "Week 4 feedback / Week 11 graded" | ✅ confirmed |
| Two design projects, analog week 8 / digital week 11 | ✅ confirmed as **due** weeks; **assigned** weeks 6 and 9 |
| End-of-term lab test | ✅ confirmed — 20 min, individual, week 12, **includes simulation questions** |
