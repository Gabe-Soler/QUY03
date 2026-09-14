---
course: cmpe-365
type: reference
date: 2026-09-13
tags: [algorithms, asymptotics, recurrences, dynamic-programming, graph-algorithms, np-completeness]
source: clrs-4e.pdf
part: "Introduction"
---

# Introduction

> **Math fidelity.** This PDF sets its symbols in Type3 subset fonts whose private-use codepoints are assigned per subset, so the same code means different things in different chapters and cannot be decoded from the font alone. Letters, digits, brackets, fractions, superscripts and the named operators were repaired and are reliable. Every symbol that could not be identified is shown as `{?}` rather than guessed at - look it up in `clrs-4e.pdf` at the page given above. Unresolved here: `1` x11412, `{?}` x612, `˚` x124, `"` x73, `(` x47, `#` x22.

*Source pages 383-383 of `clrs-4e.pdf`.*

Introduction This part covers three important techniques used in designing and analyzing effi- cient algorithms: dynamic programming (Chapter 14), greedy algorithms (Chap- ter 15), and amortized analysis (Chapter 16). Earlier parts have presented other widely applicable techniques, such as divide-and-conquer , randomization, and how to solve recurrences. The techniques in this part are somewhat more sophisticated, but you will be able to use them solve many computational problems. The themes introduced in this part will recur later in this book. Dynamic programming typically applies to optimization problems in which you make a set of choices in order to arrive at an optimal solution, each choice generates subproblems of the same form as the original problem, and the same subproblems arise repeatedly. The key strategy is to store the solution to each such subproblem rather than recompute it. Chapter 14 shows how this simple idea can sometimes transform exponential-time algorithms into polynomial-time algorithms. Like dynamic-programming algorithms, greedy algorithms typically apply to optimization problems in which you make a set of ch oices in order to arrive at an optimal solution. The idea of a greedy algorithm is to make each choice in a locally optimal manner, resulting in a faster algorithm than you get with dynamic program- ming. Chapter 15 will help you determine when the greedy approach works. The technique of amortized analysis applies to cert ain algorithms that perform a sequence of similar operations. Instead of boundi ng the cost of the sequence of operations by bounding the actual cost of each oper ation separately, an amortized analysis provides a worst-case bound on the actual cost of the entire sequence. One advantage of this approach is that although some op erations might be expensive, many others might be cheap. You can use amortized a nalysis when designing algorithms, since the design of an algorithm and th e analysis of its running time are often closely intertwined. Chapter 16 introduces three ways to perform an amortized analysis of an algorithm.
