# CMPE 320 — Fundamentals of Software Development

Only loaded automatically when Claude reads/edits files inside this folder. General repo
conventions live in the root `CLAUDE.md`.

## Course info

- **Course code / name:** CMPE 320 — Fundamentals of Software Development.
  **Also called CISC 320**: the course is cross-listed and the Fall 2026 syllabus is titled
  "CISC/CMPE 320". Treat the two codes as the same course — material, OnQ pages and emails may use
  either, and most use CISC.
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

## Programming background Gabe brings to this course

**Gabe has never written C or C++.** His programming experience is essentially all **Python**
(plus the quantitative/RL work described in the root `CLAUDE.md`). The root file's "comfortable with
programming, don't over-simplify" note still holds for *concepts* — algorithms, complexity, the
maths — but **does not** extend to C++ language mechanics, which are genuinely new as of
2026-09-14.

Practical consequences for explanations in this course:

- **Teach C++ syntax and semantics from scratch the first time each appears**, and anchor them to
  Python where an analogue exists (`vector` = `list`, `unordered_set` = `set`, range-based `for` =
  `for x in xs`). Do not assume the C-family background that the course itself assumes via its
  ELEC 278 / CISC 235 prerequisite.
- **Concepts with no Python analogue need the most care** — the header/implementation split,
  `#include` as literal text-paste, include guards, compile-vs-run-time errors, value semantics and
  copying, references (`&`), `const` and `const` correctness, `mutable`, pointers, manual memory,
  RAII, templates.
- **Do not over-simplify the reasoning.** Complexity analysis, the coupon-collector maths behind
  rejection sampling, modulo bias in `rand()` — all land fine and are worth including. The gap is
  language mechanics, not rigour.
- A long-form worked example of this pitch exists at
  `assignments/assignment_1/cpp-primer-for-assignment-1.md` — reuse its Python→C++ framing.

## Folder layout for this course

**This course uses `assignments/` instead of the repo-standard `problem-sets/`**, because each
assignment is a small project with several files rather than a single write-up:

```
courses/cmpe-320/
├── assignments/
│   └── assignment_1/          # one folder per assignment, numbered with an underscore
│       ├── instructions.md    # the handout, converted and annotated
│       └── ...                # supplied files (TestInsultGenerator.cpp, InsultsSource.txt)
│                              #   and Gabe's own source (insultgenerator_netid.h / .cpp)
├── code/                      # demo programs from lecture, not assignment work
├── lectures/
├── references/
└── summaries/
```

- **File assignment material into `assignments/assignment_N/`**, not `problem-sets/` — that folder
  has been removed here so nothing lands in it by mistake. There are four assignments this term.
- Keep everything for one assignment in its own folder: the handout, the files the course supplies,
  and the files Gabe writes. That way the submission is self-contained and the whole folder can be
  read at once when revising.
- Frontmatter `type:` stays **`problem-set`** — the repo's schema is unchanged, only this course's
  folder layout differs.
- `code/` is for lecture demos and is *not* assignment work; don't mix the two.

## Reference materials

- `code/` - demo programs handed out in lecture, kept as `.cpp` with `code/00-index.md` describing
  each. **They are deliberate gotcha demos**: several read or write memory they don't own and one
  dereferences a null pointer on purpose, so crashes and garbage output are the intended lesson.
  Build with `g++ -std=c++14 -Wall`.
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

- **Lecture 1 (2026-09-09):** course admin - grading scheme (30% assignments / 35% project /
  35% final), assignment rules and the one-week emergency period, the "discuss but don't copy"
  integrity line, agile team project assigned by the Head TA, TA groups G1-G5.
- **Lecture 2 (2026-09-11):** setting up a C++ environment - editors vs IDEs, GCC and `g++`,
  `g++ file.cpp -o file.out`, MinGW on Windows / `xcode-select --install` on macOS, the
  Eclipse + MinGW "safe configuration" (Windows-only), Hello World, and noteQ.
- **Lecture 3 (2026-09-14):** a bit of history - BCPL (1966, O-code and portability) → B (1969,
  Thompson) → C (1972, Ritchie, ANSI C) → "C with classes" (Stroustrup, 1979) → C++ (1983);
  the standards timeline through C++20; and the design philosophy, notably that C++ "gives the
  programmer a choice, even if this makes it possible to choose incorrectly".
- **Assignment 1 issued** - Shakespearean insult generator, due **Wed 23 Sep 23:59**, out of 20.
  See `assignments/assignment_1/instructions.md`. Both supplied files are filed beside it; the
  note carries the full API contract read off `TestInsultGenerator.cpp`.
  `assignments/assignment_1/cpp-primer-for-assignment-1.md` holds the language-level walkthrough
  written for a Python background — `std::set` for unique+sorted in one pass, `<random>` vs
  `rand() % n`, headers, exception classes, file I/O, `const`/`mutable`, plus the measured timing
  (11 ms with `-O2`, 36 ms without) and the coupon-collector maths for the 10,000-insult run. **The data file must be
  opened as `InsultsSource.txt`** - it downloaded under a different name, and `initialize()` takes
  no arguments so the filename is hardcoded in Gabe's implementation.
- **Next up:** "Basics" - data types, pointers, arrays. The demo programs in `code/` belong to it
  and are already filed, so they can be read before the lecture.

## Known trouble spots

Concepts flagged as weak from prior `quiz-me` sessions.

- **All of C++ as a language, as of 2026-09-14** — first exposure; see "Programming background"
  above. Not yet attempted: writing a class, the `.h`/`.cpp` split, `const` correctness, references,
  pointers. Trim this entry as specific topics stop being weak rather than leaving it blanket.
