---
course: cmpe-365
type: lecture
date: 2026-09-15
tags: [recursion, merge-sort, recurrence-relations, substitution-method, base-case, divide-and-conquer, ch4]
source: L04 RecursionComplexityI.pdf
---

# CISC/CMPE 365 — Lecture 4: Complexity of Recursive Algorithms I (slides)

> Source: `L04 RecursionComplexityI.pdf` (Yuanzhu Chen, 2026-09-15), kept beside this note.
> **Companion:** Gabe's own live-typed notes from this lecture are
> [`2026-09-15-lecture04-recursion-complexity.md`](2026-09-15-lecture04-recursion-complexity.md) —
> the practice-question review of lecture 3's material that opened the lecture, kept separate since
> it's Gabe's own working, not slide content.
>
> 🖼 Nine images were extracted but not linked here — spot-checked and they're decorative (a
> playing-card clip-art icon, plain slide-title text rendered as an image), not diagrams. They're
> still in `assets/2026-09-15-lecture04-recursion-complexity-slides/` if that changes.
>
> ⚠️ **Not Test 1 material.** Test 1 (24 Sep) covers CLRS Ch. 2–3 only, per the
> [syllabus](../references/syllabus-f2026.md). This lecture starts **Ch. 4 (Divide-and-Conquer)**
> territory — recursion, recurrence relations, the substitution method — which is **Test 2**
> scope (8 Oct). Filed here for completeness; excluded from
> [`../summaries/test1-chapters-2-3-study-guide.md`](../summaries/test1-chapters-2-3-study-guide.md).

## TLDR

What recursion is and when it stops (base case). Merge sort as the running example of a recursive
algorithm. Then the real content: turning a recursive algorithm's step-count into a **recurrence
relation**, and solving it by **repeated substitution** — expand the self-reference a few steps,
spot the pattern, generalize. Two worked examples: a straight-line recursion giving $\Theta(n)$,
and one with an inner loop giving $\Theta(n^2)$.

## Recursion

**When a function calls itself.** Example: `my_function(n)` prints `n` then calls
`my_function(n-1)`, so `my_function(2)` prints `2`, `1`, `0` via nested calls.

**Why recursion:**
- Many computational problems have well-understood recursive solutions.
- Recursive solutions are often easier to understand and code than the equivalent loop.
- A recursive solution can usually be converted to an iterative one, but the iterative version is
  typically *harder* to read.

**A recursive call with no base case never terminates** — the slide's `main()` example calls
`main()` before its own `print` statement ever runs, so `"Important message!"` is never printed;
the calls just nest forever (an infinite loop, not merely a long one).

**When to stop:** the **base case** is a condition, usually in an `if`, that does **not** lead to a
further recursive call. Once execution reaches it, the recursion stops. E.g.
```
my_function(n):
    if n <= 0: print(n)              # base case
    else: print(n); my_function(n-1)  # recursive case
```

## Merge sort, as the recursion running example

Same algorithm as [CLRS Ch. 2.3.1](../references/clrs-4e/05-2-getting-started.md) — see that file
for the full `MERGE`/`MERGE-SORT` pseudocode and the $\Theta(n)$ merge-cost argument. The slide
deck's version:

1. **Divide** the $n$-element sequence into two subsequences of $n/2$ elements each.
2. **Sort** the two subsequences recursively using merge sort.
3. **Merge** the two sorted subsequences to produce the sorted answer.

Worked on `[38, 27, 43, 3, 9, 82, 10]`: split down to single elements, then merge back up —
`[3,27,38,43]` merged with `[9,10,82]` gives `[3,9,10,27,38,43,82]`.

## Complexity of recursive algorithms — the real question

> Will `A(7)` run longer than `A(5)`? Can the running time be determined as a function of $n$? What
> is the relation between input size and number of steps executed?

```
A(n):
    if n >= 1:
        print n
        A(n-1)
```

## Recurrence relations

Express the running time $T(n)$ as a function of the running time on a **smaller input**, plus the
work done at this level:

$$T(n) = \begin{cases} c_1 & n = 0 \\ c_2 + T(n-1) & n \ge 1 \end{cases}$$

$c_1$ is the base-case cost; $c_2$ is the constant work (`print n`) done before recursing.

**The problem:** $T(n)$ is defined in terms of itself. To know how it grows with $n$, that
self-reference has to go — turn the recurrence into a **closed-form formula**. Two named methods;
this lecture does **substitution**.

### Solving by substitution — worked example

Expand $T(n-1)$ using the recurrence itself, repeatedly:

$$
\begin{aligned}
T(n) &= c_2 + T(n-1) \\
&= c_2 + \big[c_2 + T(n-2)\big] = 2c_2 + T(n-2) \\
&= 2c_2 + \big[c_2 + T(n-3)\big] = 3c_2 + T(n-3) \\
&= 4c_2 + T(n-4) \\
&\ \ \vdots \\
&= \underbrace{c_2 + c_2 + \cdots + c_2}_{n \text{ times}} + T(0) \\
&= n c_2 + c_1
\end{aligned}
$$

$$\boxed{T(n) = c_2 n + c_1 = \Theta(n)}$$

> 🔑 **The pattern to watch for.** Each substitution step peels off one $c_2$ and reduces the
> argument of $T$ by 1. After $k$ substitutions you have $k \cdot c_2 + T(n-k)$. The recursion
> bottoms out when $n - k = 0$, i.e. $k = n$ — that's where the "$n$ times" comes from. This is the
> general shape of substitution: **expand until you can see the count in terms of $n$, then stop.**

### A second example — recursion with an inner loop

```
B(n):
    if n >= 1:
        for i in range(n):
            print n
        B(n-1)
```

Now each recursive level does $\Theta(n)$ work (the loop), not $\Theta(1)$:

$$T(n) = \begin{cases} c_1 & n = 0 \\ c_2 + c_3 n + T(n-1) & n \ge 1 \end{cases}$$

Substituting the same way accumulates a **sum of decreasing loop costs** rather than a constant
count:

$$T(n) = c_2 n + c_3 \sum_{k=1}^{n} k + c_1 = c_2 n + c_3 \frac{n(n+1)}{2} + c_1$$

$$\boxed{T(n) = \Theta(n^2)}$$

> 🔑 **Why this jumps from $\Theta(n)$ to $\Theta(n^2)$.** In the first example, each of the $n$
> recursive levels contributes a *constant* ($c_2$), summing to $\Theta(n)$. Here each level
> contributes work *proportional to its own $n$* (the loop runs $n$ times at the top level, $n-1$
> at the next, etc.), so the total is $\sum_{k=1}^n k \cdot c_3 = \Theta(n^2)$ — the same
> arithmetic-series pattern as insertion sort's worst-case inner-loop count in Ch. 2.

### Summary table (from the slides)

| Recurrence | Complexity |
|---|---|
| $T(0) = c_1,\quad T(n) = c_2 + T(n-1)$ | $\Theta(n)$ |
| $T(0) = c_1,\quad T(n) = c_2 + c_3 n + T(n-1)$ | $\Theta(n^2)$ |

## Connections

- Builds directly on **Ch. 2.3's divide-and-conquer / merge sort** and previews the general
  recurrence form $T(n) = aT(n/b) + f(n)$ that **Ch. 4** (Test 2 territory) solves with the
  substitution, recursion-tree, and master-theorem methods properly.
- The loop-cost-summed-over-recursive-levels trick in the second example is the same
  $\sum_{i=2}^n i = \Theta(n^2)$ shape as insertion sort's worst case — see
  [`../summaries/unit02-getting-started-summary.md`](../summaries/unit02-getting-started-summary.md).
