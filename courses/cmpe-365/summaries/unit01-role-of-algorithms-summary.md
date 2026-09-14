---
course: cmpe-365
type: summary
date: 2026-09-10
tags: [algorithms, problem-vs-instance, correctness, order-of-growth, np-completeness, approximation-algorithms, parallel-algorithms, online-algorithms, insertion-sort, merge-sort]
---

# CLRS Ch. 1 — The Role of Algorithms in Computing

*~2 min read · Introduction to Algorithms, 4th ed., pp. 5–16*

Source chapter: [`../references/clrs-4e/04-1-the-role-of-algorithms-in-computing.md`](../references/clrs-4e/04-1-the-role-of-algorithms-in-computing.md)

---

## The one-sentence version

An algorithm is a well-defined procedure that turns input into correct output in **finite time**, and choosing a better algorithm beats buying better hardware.

---

## 1.1 Algorithms

**Three things to keep separate:**

| Term | Meaning |
|---|---|
| **Problem** | The general input/output relationship, for inputs of any size |
| **Instance** | One concrete input satisfying the problem's constraints |
| **Algorithm** | The procedure achieving that relationship for *all* instances |

**Sorting, stated formally** (the book's running example):
- **Input:** a sequence ⟨a₁, …, aₙ⟩
- **Output:** a permutation ⟨a′₁, …, a′ₙ⟩ where a′₁ ≤ a′₂ ≤ ⋯ ≤ a′ₙ

**Correctness:** for *every* instance, the algorithm halts **and** outputs the right answer. Incorrect algorithms can still be useful if you can control the error rate (e.g. primality testing, Ch. 31).

**Two traits of interesting algorithmic problems:**
1. Huge numbers of candidate solutions, nearly all wrong — the challenge is finding a good one *without enumerating them all*.
2. Real practical stakes (fuel costs, routing latency, lab time).

**Four sub-themes:**
- **Data structures** — ways to organize data for fast access/modification. No single one wins everywhere.
- **Technique** — the book teaches design methods (divide-and-conquer, dynamic programming, amortized analysis), not just recipes.
- **Hard problems** — NP-complete problems have no known efficient algorithm, but none is proven impossible. If *one* has an efficient algorithm, *all* do. Practical move: prove NP-completeness, then build an **approximation algorithm** (Ch. 35).
- **New models** — clock speeds stalled (power density), so multicore → **parallel algorithms** (Ch. 26). Input that arrives over time → **online algorithms** (Ch. 27).

---

## 1.2 Algorithms as a technology

Insertion sort ≈ c₁n², merge sort ≈ c₂n lg n, with c₁ < c₂. Read them as c₁·n·**n** vs. c₂·n·**lg n** — the asymptotic factor dominates the constant. lg n is ~10 at n = 1,000 and only ~20 at n = 1,000,000.

**No matter how much smaller c₁ is, a crossover point always exists where merge sort wins.**

The chapter's punchline:

| | Computer A | Computer B |
|---|---|---|
| Speed | 10¹⁰ instr/sec | 10⁷ instr/sec (**1000× slower**) |
| Code | insertion sort, expert-tuned, 2n² | merge sort, mediocre compiler, 50n lg n |
| Sort 10⁷ numbers | 20,000 s (**>5.5 hrs**) | ~1,163 s (**<20 min**) |

The 1000×-slower machine wins by **17×**. At 10⁸ numbers: 23 days vs. under 4 hours. **The gap grows with problem size.**

**On machine learning:** it's a way to do algorithmic tasks without explicitly designing the algorithm. It doesn't make this material obsolete — ML *is* a collection of algorithms, and its wins concentrate on problems where humans don't know the right algorithm (vision, translation). Where we do, purpose-built algorithms usually beat ML.

---

## Takeaways

1. **Asymptotic growth rate is what matters.** Constants and hardware are second-order.
2. **Correctness must be argued, not assumed.** Halt *and* be right, on every instance.

**Worth doing:** Ex. 1.2-2 (solve 8n² < 64n lg n), Ex. 1.2-3 (smallest n where 100n² beats 2ⁿ), Problem 1-1 (growth-rate table: lg n → n! against one second → one century).
