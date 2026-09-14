---
course: elec-371
type: reference
date: 2026-09-14
tags: [syllabus, embedded-systems, microprocessor, interrupts, address-decoding, fpga, system-on-chip, labs, marking-scheme, deadlines, genai-policy]
source: ELEC 371 Microprocessor Interfacing and Embedded Systems Fall 2026 Syllabus.pdf
---

# ELEC 371 — Microprocessor Interfacing & Embedded Systems (Fall 2026 Syllabus)

> Source: `syllabus-f2026.pdf` (15 pp.), kept beside this note. Its only images are the Queen's and
> Smith Engineering marks, extracted to `assets/syllabus-f2026/`. **This note is the authority for
> dates and weighting.**

## TLDR

**90% of the grade is two closed-book written sittings** — a 40-minute in-class quiz (25%) and a
3-hour final (65%). Labs are only 10%, but they are attendance-gated in a way nothing else here is:
**four in-person sessions, your assigned section only, no switching, no credit for the wrong
day/time.** The quiz is **Wednesday 7 October 2026**, and you must sit in the specific room emailed
to you — wrong room is an **automatic 20% penalty on the quiz**. For absences, **do not email the
instructor**; file the Smith Engineering form and the reweighting happens automatically.

## Course identity

| Item | Detail |
|---|---|
| Code | ELEC 371 — Microprocessor Interfacing & Embedded Systems |
| Load | **F 3-0.5-0.5 4** — Fall, 3 h lecture, 0.5 lab, 0.5 tutorial, **4.0 units** |
| Mode | In person |
| Location / time | **Consult your SOLUS timetable** — the syllabus gives no rooms. Note the lab-session dates at the top of the SOLUS tables |
| AU breakdown | 0 / 0 / 0 / **36 Engineering Science** / **12 Engineering Design** |

**Prerequisites:** ELEC 274 *Computer Architecture* and ELEC 271 *Digital Systems* (or equivalents).
The syllabus adds that beyond the official prerequisites, **conceptual and practical competence in
software/programming is relevant** — the course is written in assembly and C.

> 📝 **Document quirk.** The running head on page 2 still reads "APSC 123 – Insert Course Title
> Semester Year" — an unfilled template placeholder, not a different course. Everything else in the
> document is ELEC 371.

## Teaching team

**Instructor: Naraig Manjikian, PhD, PEng** — Dept. of Electrical and Computer Engineering,
Walter Light Hall. Department site: <https://smithengineering.queensu.ca/ece/>.
Consulting times are posted in onQ (the syllabus gives no fixed hours here).

> 🔑 **The instructor co-wrote the textbook.** The reference text is Hamacher, Vranesic, Zaky **and
> Manjikian** — so the book's treatment, notation and terminology *are* the course's, and lecture
> material can be expected to track it closely.

**Graduate TAs:** Liam Burns, Patrick Burns, Ethan Shama, Zachary Silva, Ryan Silverberg,
Sebastian Zylberberg.
**Undergraduate TAs:** Abby Ratkowski, Kinnel Tsang, Jordan Vick, Ethen Wyett.

## Assessment

| Component | Weight |
|---|---|
| Laboratory exercises (4) | **10%** |
| In-class midterm quiz | **25%** |
| Final examination | **65%** |

### Laboratory exercises (10%)

Four **in-person** lab exercises during the term. Consult your **individual SOLUS timetable** for
your lab section and its four official session days/times.

The attendance rules are unusually strict and are worth reading literally:

- **No accommodation and no credit for attending the wrong day/time.**
- Each session has an attendance sheet listing **only** the students who can receive credit for it.
  Others are directed to leave and attend their correct session.
- **No arbitrary switching between sessions for any reason** — only a formal change in lab section
  registration is acceptable.

### In-class midterm quiz (25%)

**Wednesday, 7 October 2026** — **10:30** for Section 002, **14:30** for Section 001. Both are
official lecture slots for the course in the university timetable. The syllabus says, in capitals,
**"PLAN ACCORDINGLY."**

- **Closed book, no aids of any kind — only writing tools.**
- **40 minutes**, deliberately shorter than the lecture slot to allow for paper distribution across
  double-seated rooms and collection at the end.
- Additional rooms are reserved for double seating and **students are assigned to specific rooms**,
  communicated **by email** in advance, with an onQ announcement confirming the email went out. You
  are responsible for confirming you received your assignment and recording it in your calendar.
- ⚠️ **Sitting in a room other than the one you were assigned = automatic 20% penalty on the quiz**,
  for failure to follow clearly communicated directives.
- Students with university-approved accommodations are handled through the **Exams Office** and are
  not assigned a room by the instructor. Accommodations must go through **Ventus**, as early as
  possible — particularly if other courses have assessments earlier than this one.

### Final examination (65%)

Closed book, **no aids of any kind**, standard **3-hour** duration, on the day and time scheduled by
the University unless the Exams Office has arranged accommodations. **Do not schedule vacation or
travel during the exam period** — check Term and Session Dates for the period.

### Grading

Assessments are scored as numerical percentages, combined per the weights above, then converted to
a letter grade via the established Grade Point Index. Note that **IN (incomplete) counts as a grade**
and is released on the transcript.

## Absences — the course-specific policy

This is the part most worth internalising, because it inverts the usual instinct:

> **DO NOT contact the instructor** when illness or a family emergency arises. Complete the Smith
> Engineering **online form** submitted to Student Services, ideally *before* the missed
> lab/quiz/exam, otherwise as soon as feasible afterwards.

Once Smith Engineering approves a request, it notifies the instructor (with a copy to you), and the
course policies apply **automatically**:

| Missed | Automatic consequence of an approved absence |
|---|---|
| A lab | the **other labs are reweighted** |
| The quiz | the **quiz's 25% transfers to the final exam** |

There is explicitly "nothing to discuss" — the syllabus states the design is to avoid unnecessary
stress and let an affected student concentrate on the illness or emergency itself.

**Invalid reasons** for academic consideration: extra-curricular activities, travel plans, family
events, poor time management, problems with classmates.

Whether excused or not: a student who misses a lab "should pursue the work later for learning", and
one who misses the quiz "should write it later as practice for learning."

## Email policy

Email in this course runs **instructor → students only**, and **only for important or urgent
administrative matters**. It is **not** used to answer questions about course material — those go to
in-class opportunities or the posted consulting times.

## Course outline

| Weeks | Topics |
|---|---|
| **1–2** | Microprocessor-based system organization; memory technology and memory interfaces; address decoding; system bus interconnection, operation and timing; parallel I/O interfaces; interface logic design; software programming |
| **3–4** | Interrupt concepts; programming considerations for interrupts; hardware registers in the processor and in I/O interfaces to support interrupts; details of programming for interrupts; timer interfaces with interrupts |
| **5–6** | Software issues; code-generation tools; use of C for I/O and interrupts |
| **7–9** | Embedded systems concepts, design issues, microcontrollers, sensors/actuators |
| **10–11** | System-on-chip integration with FPGA technology; embedded processors |
| **12** | Additional concepts and examples; course summary and review |

### Weekly learning outcomes, and where each is assessed

| Weeks | Outcomes | Assessed by |
|---|---|---|
| **1, 2** — system org. with memory and I/O; assembly-language software considerations | describe microprocessor-based system organization and bus interconnection and **draw diagrams** of it; describe memory technology and memory interfaces; **design address decoding logic** to a given specification; understand system bus/memory timing, **draw functional timing waveforms** cycle by cycle, and describe how real timing with delays differs from the functional diagram; understand parallel I/O interfaces and describe their logic design; write assembly for **program-controlled (polling-based)** I/O | Quiz; Final **[CLO 3]** |
| **2, 3** — interrupts for I/O, hardware and software | concepts of interrupts and the contrast with program-controlled I/O; hardware registers in processor and I/O interfaces supporting interrupts; interrupt programming; timer interfaces with interrupts | Quiz; Final **[CLO 1]** |
| **5, 6** — software issues/tools; high-level I/O programming in C | the full code-generation tool flow (**compiler → assembler → linker**); the correspondence between assembly and high-level code for both polling- and interrupt-based I/O; **write proper C** for program-controlled and interrupt-based I/O, including within the specific environment of the course's target platform | Final **[CLO 4]** |
| **7, 8, 9** — embedded systems | embedded systems concepts and terminology; design issues; purpose and features of **microcontroller chips**; types of **sensors/actuators** | Final **[CLO 2]** |
| **10, 11** — system-on-chip design | SoC integration concepts and design issues for custom-chip design and for **FPGA** technology; the variations and configurability of **embedded processors** for SoC, particularly on FPGA | Final **[CLO 2]** |
| **12** — wrap-up | additional concepts and examples as time permits; use the summary to review all course material | — |

> 🔑 **Only weeks 1–3 material is on the quiz.** Everything from week 5 onward — C programming, the
> tool flow, embedded systems, SoC/FPGA — is examined **only on the final**, which is 65% of the
> grade.

### Course learning outcomes

| CLO | Description | Indicator |
|---|---|---|
| **1** | Describe the organization and behaviour of hardware supporting interrupts, and write appropriate assembly-language code sequences to initialize hardware for and respond to interrupt requests | KB-Engineering Science |
| **2** | Describe concepts and design issues for embedded systems and system-on-chip implementation with microcontrollers and field-programmable logic chips, highlighting similarities and differences | KB-Engineering Science |
| **3** | Design the address space and address decoding logic for specified memory and I/O components, and analyze memory-interface timing for load/store execution | DE-Solutions, PA-Solve |
| **4** | Write a C program for a specified embedded application using parallel I/O ports and a hardware timer with interrupt capability | ET-Apply |

## Materials and workload

**Reference textbook:** C. Hamacher, Z. Vranesic, S. Zaky, and **N. Manjikian**, *Computer
Organization and Embedded Systems*, **6th edition**, McGraw-Hill, 2012. The Campus Bookstore
provides an electronic version for **$70**.

Course material and instructor-prepared documents are posted on the **onQ** site. Announcements go
in the onQ Announcements section — the syllabus includes instructions to turn on email notification
for them (Communications → Announcements → More Actions → Notifications → check the Email box for
"new announcement available" → Save).

**Suggested time commitment: 7–9 hours per week** across the 12-week term.

## GenAI policy

The stated position, in full:

> "For this course, the formal supervised written assessments — quiz and final examination —
> constitute a substantial portion of the overall grade. **No aids of any kind are permitted** for
> the quiz and final examination. Therefore, AI tools are clearly not available and not applicable
> for these assessments.
>
> Furthermore, **the individual learning pursued by students leading up to these assessments should
> not rely on AI tools.** Students should strive to individually complete tutorial questions, lab
> preparation, and other independent learning activities […] For in-lab activity, students should
> work within their lab groups, relying on their individual preparation, active discussion among
> group members, relevant course material, and practical experience […] Seeking shortcuts through
> AI tools and other Internet-based resources does NOT contribute to true individual learning that
> must ultimately be demonstrated without any aids during the formal supervised written assessments."

> 🔑 **This is the strictest GenAI stance of the six courses in this repo** — it discourages AI use
> in the *preparation* for assessments, not only during them, and names tutorial questions and lab
> prep specifically. Treat ELEC 371 material here as something to read, quiz yourself against and
> check your own work with — `quiz-me` rather than worked solutions — and do lab preparation and
> tutorial questions unaided first.

## Administrative

- **Invalid exams** — an exam may be declared invalid if there is an interruption during
  administration or the integrity of the exam cannot be verified; a re-write may be granted.
- **Academic consideration** — Smith Engineering's Academic Consideration (Absences) website; apply
  through the online form, not the instructor.
- **Religious accommodation** — submit the Religious Observance and Academic Activities form on
  Smith Engineering's Academic Accommodation webpage **within a week of receiving the syllabus each
  term**; dates verified against the Queen's Multi-faith Calendar. Contact `chaplain@queensu.ca` or
  `engineering.aac@queensu.ca`.
- **Accommodations** — via **Ventus**;
  <https://www.queensu.ca/ventus-support/students/visual-guide-ventus-students>. Questions to the
  Smith Engineering Academic Accommodation and Consideration Advisor, `engineering.aac@queensu.ca`.
- **Academic integrity** — departures include plagiarism, unauthorized materials or services,
  facilitation, forgery, falsification, unauthorized use of intellectual property, and
  collaboration. Sanctions range from a warning through loss of grades, course failure, to
  withdrawal from the University.
- **Copyright** — instructor-created materials (slides, recordings, handouts, tests, exams) are the
  instructor's intellectual property; redistributing or posting them is an integrity departure.
- **Student Code of Conduct** — <https://www.queensu.ca/nonacademicmisconduct/policies>
- **Wellbeing** — **EngWell** provides confidential support through a Wellness Advisor, embedded
  counsellors, mental health programming, and referrals.
