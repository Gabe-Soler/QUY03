---
course: cmpe-320
type: reference
date: 2026-09-13
tags: [syllabus, cpp, cpp14, cpp-cli, software-engineering, agile, scrum, uml, testing, stl, smart-pointers, marking-scheme, deadlines]
---

# CISC/CMPE 320 — Fundamentals of Software Development (Fall 2026 Syllabus)

> Source: `CISC-CMPE-320-Syllabus-F26.pdf` (7 pp., authored by Dr. Samir Mohammad, 2026-09-13),
> kept beside this note. The only image in the PDF is the Queen's crest, so no figures were
> extracted.

## TLDR

- **Instructor:** Dr. Samir Mohammad, Robert Sutherland Hall Rm 532, `sm373@queensu.ca`.
  **Email subject must be `320_<last 4 of student ID>_<topic>`** — e.g. `320_3670_Assignment 2`.
- **Lectures:** Mon 4:30–5:30, Wed 3:30–4:30, Fri 2:30–3:30, **Dupuis Auditorium**.
  **Tutorials:** Kingston Rm 209 — Mon 9:30–11:30, Thu 9:30–11:30, Thu 12:30–2:30.
- **Marks: 4 assignments × 7.5% = 30%, project 35%, final exam 35%.** No midterm.
- **Assignments due Wednesdays 23:59; project deliverables due Fridays.** There is an automatic
  **second week of grace** for emergencies — but the real deadline is one week.
- **Textbook (recommended):** Deitel & Deitel, *C++ How to Program*, 10th ed. — the same book the
  vendored [`../Cpp-Learing-Archive/`](../Cpp-Learing-Archive/) draws its worked source from.
- **Standard taught: C++14.** The course also covers **C++/CLI**, which is Windows/.NET only.

## Deadlines at a glance

| Due | Item |
|---|---|
| Wed 23 Sep, 23:59 | Assignment 1 |
| Fri 2 Oct, 23:59 | Project Outlines |
| Wed 7 Oct, 23:59 | Assignment 2 |
| **12–18 Oct** | **Reading Week — no classes** |
| Fri 30 Oct, 23:59 | RAD submission (Requirements Analysis Document) |
| Wed 11 Nov, 23:59 | Assignment 3 |
| Fri 13 Nov, 23:59 | SDD submission (Software Design Document) |
| Wed 25 Nov, 23:59 | Assignment 4 |
| Week of 30 Nov | Project presentation |
| Week of 7 Dec | Monday only — last class |

## Weekly schedule

| Week | Week of | Subject |
|---|---|---|
| 1 | Sep 8 (Tue) | Introduction, setup, history, basics |
| 2 | Sep 14 | Data types, pointers, arrays |
| 3 | Sep 21 | Agile, passing, operators, loops, string |
| 4 | Sep 28 | I/O, classkey, exceptions, RAD_SCRUM |
| 5 | Oct 5 | Functions, overloading 1 |
| — | Oct 12–18 | Reading week |
| 6 | Oct 19 | Overloading 2 & 3, repositories, SDD |
| 7 | Oct 26 | SW analysis 1 & 2, SW design |
| 8 | Nov 2 | Namespaces, memory, memory errors, help tools |
| 9 | Nov 9 | Inheritance 1 |
| 10 | Nov 16 | Inheritance 2–4, testing |
| 11 | Nov 23 | Testing 1 & 2, templates, STL |
| 12 | Nov 30 | Smart pointers |
| 13 | Dec 7 | Monday of this week only |

## Course topics

The syllabus explicitly calls this a **"wish list"** — order and depth are not guaranteed.

### ISO Standard C++ (implemented standard: **C++14**)

Given a Python/Java background, conditionals and loops get only a short review, with emphasis on
where C++ differs. The syllabus stresses that **C++ is not a "safe" language like Java** and that
"gotchas" will be highlighted throughout.

Fundamental types and declaration · expressions and type casting · console I/O · libraries and
namespaces · pre-processor directives · conditionals and loops · functions · scope rules ·
**pointers and references** · arrays and vectors · structures · classes · constructors ·
destructors · **operator overloading** · strings · streams and file I/O · **inheritance** ·
**virtual functions and polymorphism** · templates · exceptions · **the STL**

### C++/CLI

CLI is the **Common Language Infrastructure** — a Microsoft extension to ISO C++, implemented in
Visual Studio .NET. It compiles to **MSIL** (Microsoft Intermediate Language), letting Visual
Basic, C++ and C# combine into one program, and allows *managed* code that is safer than plain
ISO C++.

Syntax differences · **`gcnew` vs `new`** · **handles vs pointers** · managed vs unsafe code ·
building and using `*.dll` libraries · generics · properties, delegates and events · .NET framework
libraries · integrated XML documentation · Windows Form applications

### Software Engineering

Framed as "applied common sense" plus the jargon and standard techniques needed to communicate
with a team.

Dealing with complexity · **UML diagrams** · version control · code repositories ·
**testing and test-driven development** · bug tracking · *The Mythical Man-Month* ·
team communications and documentation · **agile programming techniques**

## Course objectives

By the end of the course, students will:

1. Design and construct medium-sized console and GUI programs in both procedural and
   object-oriented paradigms.
2. Design and construct **500–1000 line** console and GUI C++ programs using both OO and
   procedural C++.
3. Contribute to a larger software project as a member of an **agile programming team**.
4. Use software engineering techniques and tools for larger-scale projects.

## Marking scheme

| Component | Weight |
|---|---|
| 4 assignments @ 7.5% | 30% |
| Project | 35% |
| Final exam | 35% |

Percentages round to the nearest whole number, then convert per Section 10 of the Arts & Science
calendar: A+ 90–100, A 85–89, A− 80–84, B+ 77–79, B 73–76, B− 70–72, C+ 67–69, C 63–66, C− 60–62,
D+ 57–59, D 53–56, D− 50–52, F 0–49.

**70% of the grade is the project plus the final** — the assignments are, in the syllabus's own
words, mainly there to prepare you for the exam.

## Late policy

- Every assignment gets **one week** as the real deadline, plus an automatic **second week** as an
  emergency grace period. The syllabus is emphatic that this is *not* a two-week deadline and is
  "to be used responsibly only for emergencies."
- Past both weeks, submissions are investigated and handled under one of three routes: letters of
  accommodation, faculty-office academic consideration for short-term extenuating circumstances,
  or an urgent request direct to the instructor (**max 7 further days**).
- Beyond that, not accepted without the instructor's permission.

## Other logistics

- **Pre/co-requisite (as stated):** registration in a School of Computing plan and a minimum
  **C−** in **CISC 235** — see the discrepancy note below.
- **Required reading:** the CISC "Common Syllabus Information" page —
  <http://www.cs.queensu.ca/students/undergraduate/syllabus/>
- **Extra references:** <https://www.learncpp.com/> and <http://www.cppreference.com/>
- **OnQ** carries the course schedule and all announcements; check it regularly.
- **Final exams** are scheduled by the Faculty of Arts and Science; Fall schedules post on SOLUS
  just before Thanksgiving. Exams must be written on the Kingston campus and **will not be moved
  for travel plans** — don't book flights until the schedule is out.
- Queen's is situated on traditional Anishinaabe and Haudenosaunee territory.

## Teaching assistants

Office hours are during the tutorial.

| Name | Email as printed in the syllabus |
|---|---|
| Mohammad Faiyaz Khan | `mohammadfaiyaz.khan@queensu.ca` |
| Adekunle Akinjobi Ajibode | `23xtx1@queensu.ca` |
| Ali Sedigh Moghadam | `17jp53@queensu.ca` |
| Jihyeon Park | `m.makarem@queensu.ca` |
| Mohammed Makarem | `ali.sedighmoghadam@queensu.ca` |

> ⚠️ **The last three emails look rotated by one row in the source document.** `17jp53` reads like
> Jihyeon Park's NetID, `m.makarem` like Mohammed Makarem's, and `ali.sedighmoghadam` like Ali
> Sedigh Moghadam's — each is listed one row above the name it appears to belong to. Transcribed
> here exactly as printed rather than silently corrected. **Confirm before emailing a TA.**

## Discrepancies with the course-context file

- **Prerequisite.** This syllabus is written from the CISC side and states **CISC 235**. The
  Queen's calendar entry for the CMPE stream gives **ELEC 278 or MREN 178**, which is the one that
  applies to you in Mathematics and Engineering. Both are recorded; neither was overwritten.
- **Topic coverage.** The calendar description mentions only "advanced programming methodology
  using C++." The real syllabus devotes an entire third of the course to **C++/CLI and .NET**,
  which the calendar does not hint at.
- **Tutorials.** The calendar format says "Tut 1"; the syllabus schedules **two-hour** tutorial
  blocks.

## Practical note — C++/CLI on macOS

C++/CLI is a Microsoft extension that requires **Visual Studio on Windows**; it is not supported by
clang/gcc on macOS, and Visual Studio for Mac does not implement it. The `gcnew`/handles/Windows
Forms material therefore cannot be run natively on your machine. Options are a Windows VM, Remote
Desktop to a lab machine, or the School of Computing's lab systems — worth sorting out before the
C++/CLI weeks rather than during them.
