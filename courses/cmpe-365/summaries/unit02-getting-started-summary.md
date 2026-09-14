---
course: cmpe-365
type: summary
date: 2026-09-13
tags: [insertion-sort, loop-invariants, ram-model, worst-case-analysis, average-case-analysis, order-of-growth, theta-notation, merge-sort, divide-and-conquer, recurrences, recursion-tree]
---

# CLRS Ch. 2 — Getting Started

*~2 min read · Introduction to Algorithms, 4th ed., pp. 17–48*

Source chapter: [`../references/clrs-4e/05-2-getting-started.md`](../references/clrs-4e/05-2-getting-started.md)

---

## The one-sentence version

Two sorting algorithms, two design methods, and the machinery to prove one correct and measure how fast it is: **loop invariants** for correctness, the **RAM model** + **Θ-notation** for cost.

---

## 2.1 Insertion sort — the incremental method

Works like sorting a hand of cards: hold a sorted hand on the left, pick up one card at a time, slide it left past bigger cards until it fits.

```
INSERTION-SORT(A, n)
1  for i = 2 to n
2      key = A[i]
3      // Insert A[i] into the sorted subarray A[1:i-1].
4      j = i - 1
5      while j > 0 and A[j] > key
6          A[j+1] = A[j]
7          j = j - 1
8      A[j+1] = key
```

**Vocabulary:** the values sorted are **keys**; the data dragged along with them is **satellite data**; together they form a **record**.

### Loop invariants — how you prove correctness

> **Invariant:** At the start of each iteration of the `for` loop, the subarray `A[1:i-1]` holds the elements originally in `A[1:i-1]`, in sorted order.

Prove **three** things — it's induction with a stopping point:

| Property | What you show |
|---|---|
| **Initialization** | True before the first iteration (here i = 2: a 1-element subarray is trivially sorted) |
| **Maintenance** | If true before an iteration, still true before the next |
| **Termination** | The loop ends, and the invariant + the reason it ended proves the algorithm correct |

Termination is the payoff: the loop exits when i = n + 1, so `A[1:n]` is sorted. Done.

---

## 2.2 Analyzing algorithms

**The RAM model:** one processor, no concurrency, every instruction and data access costs constant time. Realistic instruction set only — no "sort" instruction. Ignores caches and virtual memory, but predicts real performance well.

**Why not just time it?** A stopwatch tells you about *that* machine, *that* compiler, *that* input, on *that* day. Analysis predicts the running time for inputs you haven't run.

**Line-by-line counting** gives an exact but ugly formula. Assign cost cₖ to line k, count executions, sum:

- **Best case** (already sorted): while loop exits immediately, tᵢ = 1 → `T(n) = an + b` — **linear**
- **Worst case** (reverse sorted): tᵢ = i, scan the whole prefix → `T(n) = an² + bn + c` — **quadratic**

### Why worst case?

1. It's an **upper-bound guarantee** — critical for real-time deadlines.
2. The worst case **happens often** (e.g. searching for an absent record).
3. The **average case is usually just as bad** — for insertion sort, tᵢ ≈ i/2, still quadratic.

### Order of growth

Throw away constants *and* lower-order terms; only the leading factor survives. n²/100 + 100n + 17 is dominated by the n² term once n > 10,000 — smaller than an average town.

Write it with **Θ-notation**: insertion sort is **Θ(n²)** worst case, **Θ(n)** best case. Read Θ as "roughly proportional to, for large n." Formalized in Ch. 3.

---

## 2.3 Merge sort — divide-and-conquer

Three steps, applied recursively, bottoming out at a 1-element subarray:

| Step | Merge sort |
|---|---|
| **Divide** | Split `A[p:r]` at midpoint q — Θ(1) |
| **Conquer** | Recursively sort `A[p:q]` and `A[q+1:r]` — 2T(n/2) |
| **Combine** | `MERGE` the two sorted halves — **Θ(n)** |

`MERGE` copies both halves into temp arrays L and R, then repeatedly takes the smaller of the two front elements — two face-up sorted piles, always pick the smaller top card. Every element is copied back exactly once → n iterations total → **Θ(n)**.

### The recurrence

General divide-and-conquer form — a subproblems of size n/b, plus divide cost D(n) and combine cost C(n):

> T(n) = Θ(1) if n < n₀, else **D(n) + aT(n/b) + C(n)**

For merge sort, a = b = 2, D(n) + C(n) = Θ(n):

> **T(n) = 2T(n/2) + Θ(n)  →  T(n) = Θ(n lg n)**

**The recursion-tree intuition** (no master theorem needed): the tree has **lg n + 1** levels. Each level down doubles the nodes but halves the cost per node — they cancel, so **every level costs c₂n**. Total: c₂n·lg n + c₁n = **Θ(n lg n)**.

Merge sort trades a factor of **n** for a factor of **lg n**. That's a good trade.

---

## Takeaways

1. **Loop invariant = correctness proof.** Initialization, maintenance, termination — always all three.
2. **Count lines → drop constants → keep the leading term.** That's how a messy T(n) becomes Θ(n²).
3. **Incremental vs. divide-and-conquer** are the two design methods so far; D&C recurrences get solved in Ch. 4.

**Worth doing:** Ex. 2.2-2 (selection sort: invariant + why n−1 passes suffice), Ex. 2.3-6 (binary search is Θ(lg n)), Ex. 2.3-7 (does binary search inside insertion sort make it Θ(n lg n)? — think about the *moves*, not the comparisons), Prob. 2-4 (inversions — the hint "modify merge sort" is the whole exercise).
