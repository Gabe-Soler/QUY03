---
course: cmpe-320
type: lecture
date: 2026-09-11
tags: [cpp-toolchain, gcc, g++, mingw, ide, eclipse, vscode, clion, xcode, hello-world, compilation, noteq]
---

# CISC/CMPE 320 — Setting up a C++ Environment (slides)

> Source: `02-CISC-320-F26-Slides-GettingSetup.pdf` (Dr. Samir Mohammad), kept beside this note.

## TLDR

You need a **text editor** and a **C++ compiler**. On macOS the compiler comes from
`xcode-select --install`; compile and run with:

```bash
g++ HelloWorld.cpp -o HelloWorld.out
./HelloWorld.out
```

The deck's "recommended safe configuration" is **Eclipse + MinGW** — but that is Windows-only, so
it does not apply to you. See the macOS note at the bottom.

## What you need

**A text editor**

- Basic: Sublime, VS Code — fine for simple programs.
- IDEs (extra features): Eclipse, Code::Blocks, Xcode, CLion.

**A C++ compiler** — converts high-level code into machine-understandable low-level (assembly)
code. **Platform dependent.**

## What is GCC?

- **GNU Compiler Collection.** GNU is a recursive acronym for *"GNU's Not Unix!"* and is a large
  collection of free software.
- GCC is an integrated distribution of compilers for several major languages, one being C++.
- **`g++`** is the invocation command that does preprocessing, compilation, assembly and linking to
  produce an executable.

```bash
g++ fileName.cpp -o fileName.out
./fileName.out
```

## Per-platform compiler

| Platform | Compiler |
|---|---|
| **Windows** | **MinGW** — a compiler system based on GNU GCC that compiles and links code to run on Win32 |
| **macOS** | GCC via Command Line Tools for Xcode: **`xcode-select --install`** |

## IDE recommendations

- **Cross-platform (recommended):** VS Code, JetBrains **CLion** (free for students), Eclipse for
  C++.
- **Windows:** Code::Blocks is ok.
- **macOS:** Xcode is a good choice.

## Hello World

```cpp
#include <iostream>

int main(int argc, const char * argv[]) {
    // insert code here...
    std::cout << "Hello, World!\n";
    return 0;
}
```

Steps: open the editor → write the code → save with a **`.cpp`** extension → open a terminal →
navigate to the directory → `g++ HelloWorld.cpp -o HelloWorld.out` → `./HelloWorld.out`.

## For more complex code

A proper IDE is needed. The deck recommends **Eclipse + MinGW** as "a safe configuration that
causes less trouble during the marking process", then walks through installing MinGW (extract to
`C:\MinGW`, set a `MINGW_HOME` environment variable, add `%MINGW_HOME%\bin\` to `Path`) and linking
Eclipse CDT to it (copy `gcc.exe` to `mingw32-gcc.exe`, then point
Window → Preferences → C/C++ → Build → Environment at it).

> **This section is Windows-only and does not apply on macOS.** MinGW is a Windows toolchain. The
> macOS equivalent is `xcode-select --install` plus any of VS Code / CLion / Xcode. The grading
> concern behind "safe configuration" is that your code compiles on a standard toolchain — so
> build with plain `g++` against **ISO C++14** (the standard this course teaches) and avoid
> IDE-specific project files, and platform shouldn't matter.

The deck asks you to **get your environment ready very soon** and to use the OnQ forum to discuss
installation issues — starting the post with "Windows" or "Apple" on its own first line.

## Note taking — noteQ

- **noteQ** is a note-taking tool from Queen's Student Accessibility Services with IT Services.
- It integrates with **Ventus** and **OnQ** so students registered with QSAS who are approved for
  note-taking can access notes shared by classmates.
- An announcement has been posted to CISC 320 001; if no notes are uploaded after two weeks, a
  second one follows.
- Questions: `notetake@queensu.ca`.

## Course project reminder

The deck's flow: have you been assigned to a group? If **yes** — start thinking about a project and
discuss it with the team in week 2. If **no** — get assigned, then do the above.
