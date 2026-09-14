---
course: cmpe-320
type: lecture
date: 2026-09-14
tags: [cpp-history, bcpl, b-language, c-language, stroustrup, cpp-standards, cpp14, cpp17, cpp20, design-philosophy, ansi-c]
---

# CISC/CMPE 320 — A Bit of History (slides)

> Source: `03-CISC-320-F26-Slides-History.pdf` (Dr. Samir Mohammad), kept beside this note.
> **Announcement on the deck:** groups will be finalised **Sep 15**.

## TLDR

BCPL (1966) → B (1969) → C (1972) → "C with classes" (1979) → **C++ (1983)**. Standardised by ISO
in 1998, then C++11 / **C++14** / C++17 / C++20. **This course teaches C++14.** The design
philosophy: as efficient and portable as C, supports multiple paradigms, and *gives the programmer
a choice even if the choice can be wrong.*

## The lineage

### BCPL — 1966

- **Basic Computer Programming Language**, designed by **Martin Richards** at Cambridge.
- Used to write compilers.
- First language to generate **"O-code"** — an intermediate step before executable code.
- **Why that mattered:** before BCPL, porting to a new platform meant rewriting the *entire*
  compiler (about **5 man-months**). With BCPL only the part that turned O-code into machine code
  — roughly **1/5 of the code**, the "virtual machine" — had to change. The O-code generator stayed
  put.
- Also the first language to use **`{ }`** and **`//`** for comments.

### B — 1969

- Written at **Bell Labs** by **Ken Thompson**, with contributions from **Dennis Ritchie**.
- A stripped-down BCPL for "minicomputers" like the **DEC PDP-11**.
- Had a **single data type**, the *word* — usually an integer, but could also be a memory
  reference.
- Evolved into C through the early '70s.

### C — 1972

- Credited to **Dennis Ritchie** at Bell Labs.
- A **procedural** language for systems programming (compilers) and embedded systems.
- Gives **low-level memory access** and efficient translation to machine code — no more coding in
  assembly.
- Everywhere in the late '70s / early '80s, including the IBM-PC.
- Standardised by **ANSI in 1983** → **"ANSI C"**, also called **C89**.

> <!-- unclear: the slide says ANSI standardised C in 1983 and calls the result "C89". The
>      ANSI C standard (X3.159-1989) was ratified in 1989, which is where the name C89 comes
>      from; the committee began work in 1983. Worth not repeating "1983 = C89" in a test. -->

### C with classes → C++ — 1979/1983

- Developed by **Bjarne Stroustrup** at Bell Labs from **1979** as an enhancement to C.
- Added: **classes, virtual functions, operator overloading, multiple inheritance, templates,
  exception handling**, etc.
- Renamed **C++** in **1983** — after the increment operator.

## C++ standards

| Standard | Date | Note |
|---|---|---|
| First ISO standard | **1998** | took a long time |
| Updated | 2003 | amended 2005 — 310 pages without the library |
| **C++11** | Aug 12, 2011 | 1338 pages |
| **C++14** | Aug 18, 2014 | a smaller set of changes from C++11 — **the standard this course uses** |
| **C++17** | Dec 2017 | 1605 pages |
| **C++20** | Dec 2020 | |

Two caveats the deck stresses:

- It takes a while, and considerable work, for **compilers to catch up** to a new standard.
- **Compilation is *not* standardised — only the syntax is.** (The slide asks how Java compares:
  Java standardises the bytecode and the VM, so a compiled Java artifact is portable in a way a
  compiled C++ binary is not.)

## The "philosophy" of C++

- Statically typed, general-purpose, **as efficient and portable as C**.
- Directly and comprehensively supports **multiple programming styles**: procedural, data
  abstraction, object-oriented, and generic programming.
- **Gives the programmer a choice, even if that makes it possible to choose incorrectly.**
- As **compatible with C as possible**, for a smooth transition.
- Avoids features that are **platform-specific** or not general purpose.
- Designed to **function without a sophisticated programming environment**.

> That third point is the one the syllabus echoes when it warns that C++ is "not a safe language
> like Java" and that "gotchas" will be emphasised. The freedom is deliberate, and so is the risk.

**Next topic: Basics** — the demo programs in [`../code/`](../code/) belong to that lecture.
