# ELEC 371 — Microprocessor Interfacing and Embedded Systems

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** ELEC 371 — Microprocessor Interfacing and Embedded Systems
- **Official description:** Microprocessor-based system organization and address decoding; memory
  technology and memory interfaces; parallel input/output interface design; assembly-language and
  high-level-language programming; interrupts and exceptions; timers; embedded systems
  organization and design considerations; integration in microcontrollers and programmable logic
  chips; interfacing with sensors and actuators; embedded system case studies.
- **Format:** **F 3-0.5-0.5 4** - Fall, 3 h lecture, 0.5 lab, 0.5 tutorial, **4.0 units**.
  In person. **The syllabus gives no rooms or times** - it says to consult your individual **SOLUS**
  timetable, and to note the lab-session dates at the top of the SOLUS tables. There are **two
  lecture sections** (001 and 002).
- **Prerequisites:** **ELEC 274** Computer Architecture and **ELEC 271** Digital Systems, or
  equivalents. The syllabus adds that beyond the official prerequisites, conceptual and practical
  competence in software/programming is relevant.
- **Actual topics** (from the Fall 2026 syllabus, by week):
  - **1-2:** microprocessor-based system organization; memory technology and memory interfaces;
    **address decoding**; system bus interconnection, operation and timing; parallel I/O interfaces;
    interface logic design; software programming.
  - **3-4:** **interrupts** - concepts, programming considerations, hardware registers in the
    processor and in I/O interfaces, details of interrupt programming, timer interfaces with
    interrupts.
  - **5-6:** software issues; **code-generation tools** (compiler/assembler/linker); using **C** for
    I/O and interrupts.
  - **7-9:** **embedded systems** concepts, design issues, microcontrollers, sensors/actuators.
  - **10-11:** **system-on-chip** integration with **FPGA** technology; embedded processors.
  - **12:** additional concepts and examples; summary and review.

  **The syllabus never names the target platform.** It refers only to "the specific environment for
  the target platform for practical work in the course" - so the Nios II guess previously recorded
  here is still **unconfirmed**; wait for the lab handouts.
- **Professor:** **Naraig Manjikian, PhD, PEng** - Dept. of Electrical and Computer Engineering,
  Walter Light Hall. Consulting times are posted in onQ (no fixed hours in the syllabus).
  **He is a co-author of the course's reference textbook**, so the book's notation and treatment
  are the course's.
- **Term:** Fall 2026
- **Assessment:** labs **10%**, in-class midterm quiz **25%**, final exam **65%**.
  **Quiz: Wed 7 Oct 2026** - **10:30 for Section 002, 14:30 for Section 001**, both official lecture
  slots. Closed book, **no aids of any kind**, **40 minutes**. Students are assigned to **specific
  rooms** communicated by email; **sitting in the wrong room is an automatic 20% penalty on the
  quiz**. Final is closed book, no aids, **3 hours**.
  **Only weeks 1-3 material is on the quiz** - everything from week 5 on (C, tool flow, embedded
  systems, SoC/FPGA) is examined **only on the final**.
- **Textbook (reference):** C. Hamacher, Z. Vranesic, S. Zaky, and **N. Manjikian**, *Computer
  Organization and Embedded Systems*, **6th ed.**, McGraw-Hill, 2012. Campus Bookstore e-version $70.
- **Suggested workload:** 7-9 hours per week over the 12-week term.

## Reference materials

- `references/syllabus-f2026.md` (+ `.pdf`) - the Fall 2026 syllabus, converted and restructured.
  **Check it before answering anything about dates or weighting.** Its only images are the Queen's
  and Smith Engineering marks, extracted to `references/assets/syllabus-f2026/`.
  It also records a document quirk: the running head on page 2 still reads "APSC 123 - Insert Course
  Title Semester Year", an unfilled template placeholder rather than a different course.

## Course policies worth remembering

- **Labs are attendance-gated.** Four in-person sessions, **your registered section only**. No
  accommodation and **no credit for attending the wrong day/time**; attendance sheets list only the
  students eligible for that session; **no switching** without a formal change of lab registration.
- **Absences: do NOT email the instructor.** File the Smith Engineering online form (ideally before
  the missed activity). On approval the course policy applies automatically - **other labs are
  reweighted**, or **the quiz's 25% transfers to the final**. Invalid reasons include travel plans,
  extra-curriculars, family events and poor time management.
- **Email is instructor-to-student only, for administrative matters.** Questions about course
  material go to class or the posted consulting times, never email.
- **GenAI: the strictest policy of the six courses in this repo.** No aids of any kind on the quiz
  or final, and the syllabus goes further - "the individual learning pursued by students leading up
  to these assessments **should not rely on AI tools**", naming tutorial questions and lab
  preparation specifically. **Do tutorial questions and lab prep unaided first**; use this repo for
  `quiz-me` and for checking your own completed work, not for worked solutions.

## Notation / conventions specific to this professor

(e.g. the specific instruction-set architecture / assembly syntax used, timing-diagram notation
conventions, address-space layout used in labs)

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).

- Week 1: *(no lecture material filed yet - only the syllabus)*

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions — timing diagrams for bus read/write cycles
and interrupt-vector/priority handling are commonly reported as tricky in this course.

-
