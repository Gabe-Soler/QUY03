---
course: cmpe-320
type: problem-set
date: 2026-09-14
tags: [assignment-1, cpp-classes, references, member-functions, vectors, strings, file-io, exceptions, random-numbers, const-correctness]
---

# CMPE 320 — Assignment 1: Shakespearean Insult Generator

> **Due Wednesday 23 September 2026, 23:59** (per
> [`../references/syllabus-f2026.md`](../references/syllabus-f2026.md)), with the automatic
> one-week emergency period after that. **Out of 20.** Submit only
> `insultgenerator_netid.h` and `insultgenerator_netid.cpp` to OnQ.

## What it exercises

References · member functions · vectors · strings · text file I/O · building a C++ class ·
exception classes · `const` correctness · generating random integers.

## Files you write vs. files you are given

| | File | Note |
|---|---|---|
| **Write** | `insultgenerator_netid.h` | document this one |
| **Write** | `insultgenerator_netid.cpp` | basic comments are enough |
| Given | `TestInsultGenerator.cpp` | only change the `#include` to your netid |
| Given | `InsultsSource.txt` | tab-delimited, 50 words per column |

> **Neither given file is in this repo yet** — `TestInsultGenerator.cpp` and `InsultsSource.txt`
> are linked from OnQ. Drop them in `inbox/` and run `/organize` to file them alongside this note.
> (The instructions spell the test file `TestInsutGenerator.cpp`, missing the `l` — check the
> actual name on OnQ before writing the `#include`.)

## Requirements at a glance

- Three classes: the exception classes **`FileException`** and **`NumInsultsOutOfBounds`**, and the
  generator class **`InsultGenerator`**.
- Generate between **1 and 10,000** insults, inclusive — that range is the bound
  `NumInsultsOutOfBounds` enforces.
- Insults must be **unique** (no duplicates) and in **alphabetical order** whenever displayed or
  saved.
- Only the public member functions tested by the supplied test file may be public; **everything
  else must be private**.
- Use **`const` wherever possible**.
- The test program **times** the generation of 10,000 insults — efficiency is marked.

## Insult format

`Thou ` + one word from each of the three columns + `!`

```
artless         base-court      apple-john
bawdy           bat-fowling     baggage
beslubbering    beef-witted     barnacle
```

→ `Thou artless bat-fowling barnacle!`

With 50 words per column there are $50^3 = 125{,}000$ possible insults, so 10,000 unique ones is
comfortably feasible — but see the note on efficiency below.

## Where the marks go

Graded out of 20. **You lose marks for poor style and inefficient code even if it works.** Document
the header file; the implementation needs only basic comments.

## Things worth thinking about before coding

- **Uniqueness + sorted order together.** Generating then de-duplicating then sorting is the
  obvious route, but re-sorting repeatedly is where the time goes. A container that maintains
  sorted order and rejects duplicates does both at once.
- **Efficiency at 10,000.** Rejection sampling gets slower as the set fills, though at
  10,000 / 125,000 the load factor stays low. The assignment explicitly says to "give some thought
  to creating an efficient algorithm".
- **Random integers in C++** — the assignment leaves this for you to find. Note the course teaches
  **C++14**, so `<random>` (`std::mt19937`, `std::uniform_int_distribution`) is available and is
  the modern answer; `rand() % n` is the C-style one and is biased.
- **`const` correctness** is explicitly marked, so plan it from the start rather than retrofitting.

---

# Original instructions (as given)

The purpose of this assignment is to give you some practice with references, member functions, vectors, strings, text file I/O and the construction of a C++ class. You may have written this assignment in another course but this should be different enough - having to do it in C++ in a more object oriented way - to still prove interesting!

You will need to complete a program that will generate and save between 1 and 10,000 "Shakespearian" insults. You complete the program by writing two source code files:

1- a header file "insultgenerator_netid.h" and
2- the implementation file "insultgenerator_netid.cpp". 

Replace the "netid" part of the filename with your netid. In these files you define and implement three classes, the exception classes: "FileException" and "NumInsultsOutOfBounds" and the generator class "InsultGenerator". The public member functions of the InsultGenerator class are tested in this supplied source code file: TestInsutGenerator.cpp. Examine the code and comments in this program carefully so you can see how your object must behave. The only part of the program that you will need to change is the #include statement, replacing "netid" with your netid. Note that all insults in a list must be unique (no duplicates) and in alphabetical order. The test program tests all public member functions - everything else in the class must be private.

You will also note that the length of time to generate 10,000 insults is measured and reported. You should give some thought to creating an efficient algorithm to generate such a large number of insults.

An insult is generated by putting in three words or hyphenated phrases inbetween "Thou " and "!". The three words are picked at random, one from each column of words that are supplied in the tab-delimited file InsultsSource.txt. Here are the first few lines from the file:

artless		base-court	apple-john
bawdy		bat-fowling	baggage
beslubbering	beef-witted	barnacle
For example, using the first, second and third words from each column in turn, you would generate the insult:

Thou artless bat-fowling barnacle!
(This sounds nasty, even if I don't know exactly what it means!)

With 50 words in each column, you could generate a maximum of 50 \*50* 50 or 125,000 unique insults - more than enough for anyone! Your program should be able to generate up to 10,000 unique insults with ease. So, the legal range for the number of insults to generate is between 1 and 10,000 inclusive.

Whenever you display or save insults to a file they must be in alphabetical order.

Use the const keyword wherever possible.

Note that you are going to have to figure out how to generate random integers in C++...

Submission and Grading:

Submit your two source files, insultgenerator_netid.h and insultgenerator_netid.cpp to onQ. Do not submit any other files. Your grader will test your code with the testing file linked above.

The assignment will be graded out of 20. You will lose marks for poor style and inefficient code, even if it works. Document your header file, but don't worry about putting too many comments in your implementation file, but basic comments are required.