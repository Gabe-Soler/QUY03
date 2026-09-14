---
course: cmpe-365
type: reference
date: 2026-09-09
tags: [syllabus, algorithms, test-dates, clrs, np-completeness, divide-and-conquer, greedy, dynamic-programming, branch-and-bound, marking-scheme]
source: CISC365_Syllabus_Fall2026_v02.pdf
---

# CISC 365 — Algorithms I (Fall 2026 Syllabus)

> Source: `syllabus-f2026.pdf` (4 pp., School of Computing, **revised 9 September 2026**, version
> v02), kept beside this note. No figures in the PDF. **This note is the authority for dates and
> weighting.**

## TLDR

**Five in-class term tests at 20% each. That is the entire grade — no assignments, no midterm, no
final exam.** Dates: **24 Sep, 8 Oct, 29 Oct, 12 Nov, 1 Dec**. Four of the five are Thursdays; the
last is a Tuesday. Missing one costs a full fifth of the course and the syllabus offers no make-up
mechanism.

This **confirms** the assessment and test dates already recorded in `../CLAUDE.md` from the
lecture 1 slides — they were right. What is new here is the contact protocol, office hours, the
remark deadline, and the official learning outcomes.

## Logistics

| Item | Detail |
|---|---|
| Offering | Fall 2026, **face to face** |
| Lecture dates | **8 September – 8 December 2026** |
| Lecture times | **Mon 11:30–12:20, Tue 13:30–14:20, Thu 12:30–13:20** |
| Location | **Stirling B** |
| Instructors | **Prof. Yuanzhu Chen**, **Prof. Xu Wang** |
| TAs | Felix Xing, James Song, Mohamed Harmanani |

**Office hours**
- **Instructor — Tuesdays 14:30–15:20**, Goodwin 536 *and* MS Teams (channel "Office hour with Instructor")
- **TA — Thursdays 17:00–18:00**, Goodwin 536 *and* MS Teams (channel "Office hour with TA")

## Communication protocol — follow this exactly

> - **Online:** MS Teams
> - **Email:** `cisc365@cs.queensu.ca`, `yuanzhu.chen@queensu.ca`
>   — **use the Queen's addresses above, not OnQ**
>   — include **"CISC365" in the subject**, and your **name and student number in the body**
> - **In person:** by appointment

## Prerequisites

**Registration in a School of Computing plan and a C– or higher in CISC 203, 204 and 235.**

> ⚠️ **This is the CISC-side prerequisite and it is not the one that applies to Gabe.** He is
> registered under **CMPE 365** (Mathematics and Engineering), whose calendar prerequisites are
> **ELEC 278 or MREN 178; ELEC 270 or a discrete mathematics course**. Both are recorded in
> `../CLAUDE.md`. Same situation as CMPE/CISC 320 — the syllabus is written from the School of
> Computing side. Not an error, just a different entry route.

## Assessment

| Component | Weight |
|---|---|
| **Term tests ×5, in class** | **20% each = 100%** |

That is the whole scheme. **No assignments, no midterm, no final exam.**

| Test | Date | Weekday | Topic it follows |
|---|---|---|---|
| **Test 1** | **24 September 2026** | Thursday | Algorithm complexity (Ch. 2–3) |
| **Test 2** | **8 October 2026** | Thursday | Divide-and-conquer (Ch. 4) |
| **Test 3** | **29 October 2026** | Thursday | Greedy strategy (Ch. 15) |
| **Test 4** | **12 November 2026** | Thursday | Dynamic programming (Ch. 14) |
| **Test 5** | **1 December 2026** | **Tuesday** | Branch-and-bound + review |

> 🔑 **Test 5 is a Tuesday, the other four are Thursdays.** Easy to mis-diarise.

**Remarks.** Requests go to the instruction team's email (`cisc365@cs.queensu.ca`) **within 5
calendar days after grades are posted. Late requests will not be considered.**

## Textbook

Cormen, Leiserson, Rivest and Stein, ***Introduction to Algorithms***, **4th edition**, MIT Press,
2022 — already filed at `clrs-4e/` (converted, one file per chapter) and `clrs-4e.pdf`.

## Topics

1. Algorithm efficiency and problem complexity
2. Divide-and-conquer
3. Greedy strategies
4. Dynamic programming
5. Branch-and-bound

## Tentative schedule

| Week | Topic (chapters) | Evaluation |
|---|---|---|
| 1 | 1a: Algorithm complexity (Ch. 2) | |
| 2 | 1a: Algorithm complexity (Ch. 3) | |
| 3 | 2: Divide-and-conquer (Ch. 4) | **24 Sep — Test 1** |
| 4 | 2: Divide-and-conquer (Ch. 4) | |
| 5 | 3: Greedy strategy (Ch. 15) | **8 Oct — Test 2** |
| **6** | **Fall reading break** | |
| 7 | 3: Greedy strategy (Ch. 15) | |
| 8 | 4: Dynamic programming (Ch. 14) | **29 Oct — Test 3** |
| 9 | 4: Dynamic programming (Ch. 14) | |
| 10 | 5: Branch-and-bound | **12 Nov — Test 4** |
| 11 | 5: Branch-and-bound | |
| 12 | 1b: NP-completeness (Ch. 34) | |
| 13 | 1b: NP-completeness (Ch. 34) + review | **1 Dec — Test 5** |

> 🔑 **NP-completeness is numbered "1b" but taught last**, in weeks 12–13, after branch-and-bound.
> The learning outcomes below list it first, which makes the course look front-loaded with
> complexity theory when it is the opposite. Note also that **Test 5 (1 Dec) sits in week 13**
> alongside the NP-completeness material and review.

> 📝 The syllabus writes "Brand-and-bound" in the topic list — a typo for **branch-and-bound**,
> spelled correctly in the schedule table.

## Learning outcomes

- Possess a strong understanding of **computational complexity**, up to and including polynomial
  time reducibility; class **P** and **NP**; **NP-completeness**; proofs of NP-completeness.
- Be able to **recognize classical NP-complete problems**.
- Be able to **prove that new problems are NP-complete** using polynomial-time reductions from
  known NP-complete problems.
- **Apply key algorithm paradigms**, both in the abstract and through concrete examples:
  divide-and-conquer; greedy algorithms; dynamic programming; branch-and-bound.

## Administrative

- **Academic integrity** — six core values (honesty, trust, fairness, respect, responsibility,
  courage). Departures include plagiarism, use of unauthorized materials, facilitation, forgery and
  falsification. **The instructor reserves the right to give a failing course grade** for breaches
  deemed serious, including plagiarism of assignments.
- **Copyright** — course website material is for registered students' personal use only and must
  not be distributed to anyone outside the course during the current term.
- **Support** — SASS academic-integrity tutorial; QSAS for accommodations; Arts & Science academic
  consideration for extenuating circumstances.
- School's Common Syllabus Information: <https://www.cs.queensu.ca/undergraduate/syllabus/>

> The syllabus numbers its policy sections 1, 2, 3, 4, 5, **7** — there is no section 6.
