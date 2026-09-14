# CMPE 320 — Fundamentals of Software Development

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** CMPE 320 — Fundamentals of Software Development
- **Official description:** Introduction to management of small- and medium-scale software
  projects. Advanced programming methodology using C++. Includes a significant programming
  project.
- **Format:** Lectures Mon 4:30-5:30, Wed 3:30-4:30, Fri 2:30-3:30 in **Dupuis Auditorium**.
  Tutorials are **two hours** in Kingston Rm 209 (Mon 9:30-11:30, Thu 9:30-11:30, Thu 12:30-2:30) -
  the calendar's "Tut 1" understates this.
- **Prerequisites:** **ELEC 278 or MREN 178** for the CMPE/Math & Eng stream (this is the one that
  applies to Gabe). The Fall 2026 syllabus is written from the CISC side and instead states
  registration in a School of Computing plan plus a minimum C- in **CISC 235** - recorded here so
  the difference isn't mistaken for an error.
- **Actual topics** (from the Fall 2026 syllabus, which calls the list a "wish list" - order and
  depth are not guaranteed). Three areas:
  1. **ISO Standard C++**, implemented standard **C++14**: types, casting, console I/O, namespaces,
     preprocessor, functions, scope, **pointers and references**, arrays/vectors, structs, classes,
     ctors/dtors, **operator overloading**, strings, file I/O, **inheritance**, **virtual functions
     and polymorphism**, templates, exceptions, **the STL**, smart pointers.
  2. **C++/CLI** - Microsoft's .NET extension: `gcnew` vs `new`, handles vs pointers, managed vs
     unsafe code, DLLs, generics, properties/delegates/events, Windows Forms. **Windows-only**; see
     the note in the syllabus file about running this on macOS.
  3. **Software engineering**: complexity, **UML**, version control and repositories,
     **testing and TDD**, bug tracking, *The Mythical Man-Month*, team documentation, **agile**.

  The calendar description gives no hint that a full third of the course is C++/CLI and .NET.
- **Professor:** Dr. Samir Mohammad - Robert Sutherland Hall Rm 532, `sm373@queensu.ca`,
  office hours by appointment (Tue 2-3, Wed 12-1).
- **Term:** Fall 2026
- **Assessment:** 4 assignments @ 7.5% = **30%**, project **35%**, final exam **35%**. No midterm.
  Assignments due **Wednesdays 23:59**, project deliverables **Fridays**. Each assignment has a
  real one-week deadline plus an automatic second week reserved for emergencies.
- **Textbook (recommended):** Deitel & Deitel, *C++ How to Program*, 10th ed. - the same book the
  vendored `Cpp-Learing-Archive/` takes its worked source from, so that folder is directly useful
  for this course.

## Reference materials

- `references/syllabus-f2026.md` (+ `.pdf`) - the Fall 2026 syllabus, converted. Holds the full
  week-by-week schedule, every deadline, the marking scheme and the late policy. **Check it before
  answering anything about dates or weighting.** It also flags an apparent error in the source
  document: three TA emails appear rotated by one row relative to their names.
- `Cpp-Learing-Archive/` - worked C++ source from *Deitel, C++ How to Program* (10th ed.) and
  *Malik, Data Structures Using C++* (2nd ed.). 733 `.cpp`/`.hpp` files organised by book and
  chapter - useful for seeing idiomatic implementations of the things this course covers.

  **Vendored, not a clone.** Originally cloned from
  <https://github.com/saitcakir/Cpp-Learing-Archive> at commit `66acd515` (2020-07-08, branch
  `master`); MIT licensed, Copyright (c) 2019 Erdem Ozgen - `LICENSE` is kept in the folder and
  must stay. The nested `.git` was removed so the files live in this repo directly (an embedded
  git repo pushes as an empty folder). That means `git pull` cannot update it: to refresh, re-clone
  from the URL above and copy the files back over.

  Compiled output (`bin/`, `obj/`, `*.o`, `*.exe`) is gitignored - it was 12 MB of Windows binaries
  that cannot run on macOS and rebuild from source anyway.

## Notation / conventions specific to this professor

- **Email subject format is mandatory:** `320_<last four digits of student ID>_<topic>`,
  e.g. `320_3670_Assignment 2`. Mail without it may not be handled.
- **C++14** is the standard actually taught - not C++17/20/23. Watch for answers that rely on
  later features (structured bindings, `std::optional`, concepts, ranges); they are out of scope
  and may be marked wrong.
- Project deliverables use the **RAD** (Requirements Analysis Document) and **SDD** (Software
  Design Document) format, and the agile framework named in the schedule is **SCRUM**
  (week 4, "RAD_SCRUM").
- Course announcements and the live schedule live on **OnQ**, not in the syllabus PDF.

## Covered so far

Update every time new lecture material is filed (the `file-notes` skill does this automatically).

*Nothing has been filed from lectures yet - the entries below come from the syllabus schedule, so
they say what is planned, not what was actually delivered. Replace them as real notes land.*

- **Week 1 (Sep 8, Tue start):** introduction, setup, history, basics.
- **Week 2 (Sep 14):** data types, pointers, arrays. *(current week as of filing)*
- **Week 3 (Sep 21):** agile, parameter passing, operators, loops, string. Assignment 1 due Sep 23.

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions.

-
