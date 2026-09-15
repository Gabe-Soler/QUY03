---
course: cmpe-365
type: summary
date: 2026-09-15
tags: [test1-prep, insertion-sort, loop-invariants, ram-model, order-of-growth, theta-notation, big-o-notation, omega-notation, merge-sort, divide-and-conquer, asymptotic-notation, practice-questions]
---

# Test 1 Study Guide — CLRS Ch. 2–3 (Algorithm Complexity)

**Test 1: Thursday 24 September 2026, in class.** Syllabus scope: *"Algorithm complexity
(Ch. 2–3)"*. This is a consolidation of lectures 1–3 plus the filed CLRS reference chapters —
not new material. Sources:
[`../lectures/2026-09-08-lecture01-introduction-slides.md`](../lectures/2026-09-08-lecture01-introduction-slides.md),
[`../lectures/2026-09-10-lecture02-algorithm-complexity-slides.md`](../lectures/2026-09-10-lecture02-algorithm-complexity-slides.md),
[`../lectures/2026-09-14-lecture03-asymptotic-notations-slides.md`](../lectures/2026-09-14-lecture03-asymptotic-notations-slides.md),
[`../lectures/2026-09-14-lecture03-asymptotic-notation.md`](../lectures/2026-09-14-lecture03-asymptotic-notation.md) (Gabe's own, corrected),
[`../references/clrs-4e/05-2-getting-started.md`](../references/clrs-4e/05-2-getting-started.md),
[`../references/clrs-4e/06-3-characterizing-running-times.md`](../references/clrs-4e/06-3-characterizing-running-times.md).

> **Out of scope, confirmed:** Ch. 4 (recurrences, substitution/recursion-tree/master theorem) is
> **Test 2** territory (8 Oct) — lecture 4 started it on 15 Sep but Test 1 doesn't reach it. Ch. 1
> (role of algorithms) is included below only as brief vocabulary background, since it's what
> lecture 1 actually covered and the syllabus's own week-1 entry is already labelled "Ch. 2" —
> treat it as low-yield if you're short on time, not zero-yield.

## TLDR

Two design methods (**incremental**, **divide-and-conquer**), one correctness technique
(**loop invariants**: initialization/maintenance/termination), one cost model (**RAM model**: every
instruction and access costs constant time), and three pieces of **asymptotic notation** ($\Theta$,
$O$, $\Omega$) — each a *set* of functions, each defined by a $c \cdot g(n)$ bound holding for all
$n \ge n_0$. $\Theta$ needs two constants (clamps both sides); $O$ and $\Omega$ need one each.
Insertion sort is $\Theta(n)$ best case, $\Theta(n^2)$ worst case — and "the running time" with no
qualifier can only be truthfully bounded by $O(n^2)$ or $\Omega(n)$, never a single $\Theta$.
Merge sort is $\Theta(n \lg n)$ **in every case**.

**The single most-tested-feeling skill**: pick $c$ (or $c_1, c_2$) and $n_0$ to prove a $\Theta/O/\Omega$
claim from the formal set-builder definition, and know when a substituted value pins down a
constant versus when it doesn't (see Trouble Spots below — this is Gabe's own documented mistake).

---

## 1. Background vocabulary (Ch. 1)

| Term | Meaning |
|---|---|
| **Problem** | The general input/output relationship, for inputs of any size |
| **Instance** | One concrete input |
| **Algorithm** | The procedure achieving the relationship for **every** instance |

**Correctness** = halts **and** gives the right output, on **every** instance — not just the ones
you tried.

**Why asymptotic growth beats hardware.** A computer **1000× slower** running merge sort
($\Theta(n\lg n)$) beats a computer running insertion sort ($\Theta(n^2)$) by **~17×** at
$n = 10^7$, and the gap only widens as $n$ grows. This is the standing argument for why the rest of
the course cares about order of growth and not constant factors.

---

## 2. Insertion sort

```
INSERTION-SORT(A)                                  cost   times
1  for j = 2 to A.length                            c1     n
2      key = A[j]                                   c2     n-1
3      // Insert A[j] into the sorted                0     n-1
          sequence A[1 .. j-1].
4      i = j - 1                                     c4     n-1
5      while i > 0 and A[i] > key                    c5     Σ_{j=2}^{n} t_j
6          A[i+1] = A[i]                              c6     Σ_{j=2}^{n} (t_j - 1)
7          i = i - 1                                  c7     Σ_{j=2}^{n} (t_j - 1)
8      A[i+1] = key                                  c8     n-1
```

**This is the professor's index convention** (outer loop `j`, inner `i`) — **CLRS 4th ed. swaps
them** (`INSERTION-SORT(A,n)`, outer `i`, inner `j`). Use the professor's letters on the test;
expect them flipped when reading the filed textbook chapter. $t_j$ = number of times the `while`
test on line 5 runs for that value of $j$.

### Loop invariant (correctness proof)

> **Invariant:** at the start of each iteration of the `for` loop, the subarray `A[1..j-1]` holds
> the elements originally in `A[1..j-1]`, in sorted order.

Three things to show, always in this order:

| Property | What you argue |
|---|---|
| **Initialization** | True before the first iteration (`j=2`: a 1-element subarray is trivially sorted) |
| **Maintenance** | If true before an iteration, still true before the next |
| **Termination** | The loop ends (here, when `j` exceeds `A.length`), and the invariant at that point gives you what you wanted to prove |

A loop-invariant proof **is** mathematical induction: initialization = base case, maintenance =
inductive step, termination = where the induction stops (unlike ordinary induction, which runs
forever).

### Best case vs. worst case

| Case | Input | $t_j$ | Cost | Order of growth |
|---|---|---|---|---|
| **Best** | already sorted | $t_j = 1$ | $T(n) = an + b$ | $\Theta(n)$ |
| **Worst** | reverse sorted | $t_j = j$ | $T(n) = an^2 + bn + c$ | $\Theta(n^2)$ |

**Why default to worst case** (three reasons, know all three):
1. It's a **guarantee** — an upper bound valid for *any* input, no need to guess how bad it gets.
2. The worst case **occurs fairly often** in practice (e.g. searching for absent data).
3. The **average case is usually just as bad** — for insertion sort, $t_j \approx j/2$ on average,
   still $\Theta(n^2)$.

### The direct $\Theta(n^2)$ argument (no summations) — CLRS §3.1

You don't have to re-derive the cost formula every time. Two halves:

- **Upper bound, $O(n^2)$, holds for *every* input:** the outer loop runs $n-1$ times, the inner
  loop at most $i-1 < n$ times each, so total inner-loop iterations $< (n-1)(n-1) < n^2$, each
  costing constant time.
- **Lower bound, $\Omega(n^2)$, for the worst case:** split the array into three blocks of $n/3$.
  If the $n/3$ largest values start in the *first* block, each must move through the *entire*
  middle block (at least $n/3$ swaps each) to reach the last block. That's at least
  $(n/3)(n/3) = n^2/9$ swaps — $\Omega(n^2)$.

$O(n^2)$ in all cases **and** $\Omega(n^2)$ for the worst case $\implies$ worst-case running time is
$\Theta(n^2)$ (Theorem 3.1, below).

---

## 3. The RAM model

- **One processor, no concurrency.** Instructions execute one after another.
- **Every instruction and every data access costs constant time** — even indexing into an array.
- Contains the instruction set of a real computer (arithmetic, data movement, control) — **not** an
  instruction that would trivialize the problem (no "sort" instruction).
- **Does not model the memory hierarchy** (no caches, no virtual memory) — but is still an excellent
  predictor of real performance.

**Why not just time it?** A stopwatch only tells you about *that* machine, *that* input, *that*
run. Analysis predicts the running time for inputs you haven't tried.

---

## 4. Order of growth — the professor's rules

Once you have a per-line cost formula, **discard lower-order terms and the leading coefficient** —
only the dominant term's shape survives. $n^2/100 + 100n + 17$ is dominated by the $n^2/100$ term
once $n$ exceeds 10,000 (smaller than an average town).

| | Exact | Drop lower-order | Drop coefficient | Order of growth |
|---|---|---|---|---|
| $T_1(n)$ | $20n+5$ | $20n$ | $n$ | $\Theta(n)$ |
| $T_2(n)$ | $4n+50$ | $4n$ | $n$ | $\Theta(n)$ |
| $T_3(n)$ | $n^2+n$ | $n^2$ | $n^2$ | $\Theta(n^2)$ |
| $T_4(n)$ | $2n^2+50$ | $2n^2$ | $n^2$ | $\Theta(n^2)$ |

### Analyzing composite code — the rules straight off the slides

| Construct | Complexity is |
|---|---|
| **Sequence of statements** | the complexity of the **most complex single statement** in it |
| **Loop** | (complexity of the loop body) × (number of times the loop executes) |
| **Conditional (`if`/`else`)** | the complexity of **whichever branch is higher** |

**Method, in order:**
1. Identify the fundamental step executed most often.
2. Write a function relating how often that step executes to the input size.
3. Discard lower-order terms and the constant coefficient.
4. What's left is the complexity.

---

## 5. Merge sort & divide-and-conquer

Three steps, applied recursively, bottoming out at a 1-element subarray (always sorted):

| Step | Merge sort | Cost |
|---|---|---|
| **Divide** | split `A[p..r]` at the midpoint | $\Theta(1)$ |
| **Conquer** | recursively sort each half | $2T(n/2)$ |
| **Combine** | `MERGE` the two sorted halves | $\Theta(n)$ |

**`MERGE` is $\Theta(n)$**: copy both halves into temp arrays `L`, `R`; repeatedly take the smaller
of the two front elements (two face-up sorted card piles, always flip the smaller top card). Every
element is copied back into `A` exactly once $\Rightarrow$ $n$ iterations, each $\Theta(1)$.

**The recurrence:** $T(n) = 2T(n/2) + \Theta(n) \implies T(n) = \Theta(n \lg n)$.

**Recursion-tree intuition** (no master theorem needed — that's Ch. 4/Test 2): $\lg n + 1$ levels;
each level down doubles the number of nodes but halves the cost per node, so **every level costs
the same, $c_2 n$**. Total: $c_2 n \cdot \lg n + c_1 n = \Theta(n \lg n)$.

**Merge sort trades a factor of $n$ for a factor of $\lg n$** — and unlike insertion sort, it runs
in $\Theta(n \lg n)$ in **every** case, best and worst alike. No case-splitting needed when you
state its complexity.

---

## 6. Asymptotic notation — the formal definitions

All three are **sets of functions**. Write $f(n) = \Theta(g(n))$ to mean $f(n) \in \Theta(g(n))$ —
an accepted "abuse" of `=`, not literal equality (more on this below).

| Notation | Set-builder definition | Bounds $f$ | Constants needed |
|---|---|---|---|
| $\Theta(g(n))$ | $\{f(n): \exists\, c_1,c_2,n_0 > 0 \text{ s.t. } 0 \le c_1 g(n) \le f(n) \le c_2 g(n)\ \forall n \ge n_0\}$ | **both sides** | $c_1, c_2, n_0$ |
| $O(g(n))$ | $\{f(n): \exists\, c,n_0 > 0 \text{ s.t. } 0 \le f(n) \le c\,g(n)\ \forall n \ge n_0\}$ | above only | $c, n_0$ |
| $\Omega(g(n))$ | $\{f(n): \exists\, c,n_0 > 0 \text{ s.t. } 0 \le c\,g(n) \le f(n)\ \forall n \ge n_0\}$ | below only | $c, n_0$ |

> ⚠️ **The constants are positive *reals*, not positive integers.** $c_1 = 1/5$ is a completely
> normal answer. Writing "$c \in \mathbb{Z}^+$" is wrong and was Gabe's own documented mistake —
> see Trouble Spots.

**Plain-English reading:** $O$ = grows no faster than; $\Omega$ = grows at least as fast as;
$\Theta$ = grows at exactly the same rate (to within constant factors, from both directions).

### Theorem 3.1 (the bridge between them)

$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))$$

This is how you build a $\Theta$ proof in practice: prove the upper and lower bounds separately,
then invoke this theorem. (It's exactly what §2's insertion-sort argument did.)

### Worked example — pin down $c_1, c_2, n_0$

Claim: $\tfrac12 n^2 - 3n = \Theta(n^2)$.

$$c_1 n^2 \le \tfrac12 n^2 - 3n \le c_2 n^2$$

Divide through by $n^2$ (valid, $n>0$):

$$c_1 \le \tfrac12 - \tfrac3n \le c_2$$

Let $h(n) = \tfrac12 - \tfrac3n$ — this is **increasing** in $n$ ($h(10) = 0.2$, $h(100) = 0.47$,
$h(n) \to \tfrac12$). That monotonicity decides how each constant gets picked:

- **$c_1$** needs $c_1 \le h(n)$ for *every* $n \ge n_0$. Since $h$ is increasing, its smallest value
  on $[n_0,\infty)$ is at $n = n_0$ itself — so **substituting $n_0$ directly gives you $c_1$**.
  At $n_0 = 10$: $c_1 = 1/5$.
- **$c_2$** needs $h(n) \le c_2$ for *every* $n \ge n_0$, including $n \to \infty$ — so **$c_2$ must
  clear the supremum**, not the value at $n_0$. Since $h(n) < \tfrac12$ always, $c_2 = \tfrac12$
  works; $c_2 = 1/5$ would fail (e.g. at $n=100$, $h(100)=0.47 > 0.2$).

$$\boxed{c_1 = \tfrac15,\ c_2 = \tfrac12,\ n_0 = 10}$$

**General theorem** (of which this is the case $a=\tfrac12, b=-3, c=0$):
$$an^2+bn+c = \Theta(n^2) = O(n^2) = \Omega(n^2) \quad (a>0)$$

### Counterexample — when $\Theta$ fails

$6n^3 \ne \Theta(n^2)$: the upper-bound half alone already breaks, since $6n^3 \le c_2 n^2$ would
force $6n \le c_2$ for *all* $n \ge n_0$ — impossible, since the left side grows without bound and
no constant can stay ahead of it.

---

## 7. Asymptotic notation in equations, and the properties

**Reading equations with notation embedded.** $2n^2 + 3n + 1 = 2n^2 + \Theta(n)$ means: there's
*some* $f(n) \in \Theta(n)$ such that $2n^2+3n+1 = 2n^2+f(n)$ (here, $f(n)=3n+1$). When the
notation is on the *right* of a chained equation, e.g. $2n^2+\Theta(n)=\Theta(n^2)$, it means: for
*any* choice of the left anonymous function, *some* choice on the right makes it hold — **read
strictly left to right**, the `=` is not symmetric here.

**Transitivity** (holds for $\Theta$, $O$, $\Omega$):
$$f=\Theta(g),\ g=\Theta(h) \implies f=\Theta(h) \qquad \text{(likewise for } O,\ \Omega\text{)}$$

**Reflexivity:** $f(n) = \Theta(f(n)) = O(f(n)) = \Omega(f(n))$.

**Symmetry:** $f(n)=\Theta(g(n)) \iff g(n)=\Theta(f(n))$ — **only $\Theta$ is genuinely symmetric.**

**Transpose symmetry (the useful, easy-to-forget one):**
$$f(n) = O(g(n)) \iff g(n) = \Omega(f(n))$$
$O$ and $\Omega$ are **duals** — swap the two arguments and the notation flips. This is the fastest
way to convert between an upper-bound and a lower-bound statement without redoing the proof.

---

## 8. Known trouble spots (from prior sessions — watch for these on the test)

- **Choosing $c_2$ from a single substitution.** Plugging in one value of $n$ pins down the
  constant on the side the function is moving *away from*, not both. If $f(n)/g(n)$ is
  **increasing**, a substitution at $n_0$ gives $c_1$ but says nothing about $c_2$ (which needs the
  *supremum*, often as $n\to\infty$). If $f(n)/g(n)$ is **decreasing**, it's the other way round —
  check which direction before reusing one substitution for both constants. **This was Gabe's own
  documented error** on the $\tfrac12n^2-3n$ example (concluded $c_2 \ge 1/5$ when $c_2 \ge 1/2$ was
  required).
- **Stating the $O$ definition in full.** Missing pieces to watch for: the bound
  $f(n) \le c\,g(n)$ itself, and **"for all $n \ge n_0$"**. A definition missing either isn't a
  definition.
- **"Constants" means positive reals, not positive integers.** $c_1 = 1/5$ is a normal, correct
  answer — don't second-guess a non-integer constant.

---

## 9. Practice questions — full answer key

**No official key exists for either set** (posed on the slides/in lecture with no answers shown) —
these are worked from the formal definitions above; check the reasoning, not just the verdict.

### Set A — is $n+1$ in each set?

| # | Claim | Verdict | Why |
|---|---|---|---|
| 1 | $n+1=\Theta(n)$ | ✅ **True** | $c_1=1, c_2=2, n_0=1$: $n \le n+1 \le 2n$ for all $n\ge1$ |
| 2 | $n+1=O(n)$ | ✅ **True** | Implied by 1 (or directly: $c=2, n_0=1$) |
| 3 | $n+1=O(n^2)$ | ✅ **True** | $n$ grows slower than $n^2$, so eventually $n+1 \le c\,n^2$ (e.g. $c=1, n_0=2$) |
| 4 | $n+1=\Omega(n)$ | ✅ **True** | Implied by 1 |
| 5 | $n+1=\Omega(n^2)$ | ❌ **False** | $(n+1)/n^2 \to 0$ — no constant $c$ can keep $cn^2 \le n+1$ as $n\to\infty$ |
| 6 | $n+1=\Omega(1)$ | ✅ **True** | Trivial: $n+1 \ge 1$ for all $n \ge 0$ |

### Set B — is insertion sort's running time in each set?

*(Unqualified "the running time" must hold across **every** case — best, worst, everything in
between. Best case is $\Theta(n)$, worst case is $\Theta(n^2)$.)*

| # | Claim | Verdict | Why |
|---|---|---|---|
| 1 | running time $\in \Omega(n)$ | ✅ **True** | Even the *best* case is $\Theta(n) \subseteq \Omega(n)$, and every other case is at least as slow |
| 2 | running time $\in O(n^2)$ | ✅ **True** | The *worst* case is $\Theta(n^2)$; nothing runs slower, so $O(n^2)$ is a valid blanket bound |
| 3 | running time $\in \Omega(n^2)$ | ❌ **False** | The *best* case is $\Theta(n)$, which is **not** $\Omega(n^2)$ — fails to hold for every input |
| 4 | running time $\in \Theta(n)$ | ❌ **False** | Would need an $O(n)$ upper bound for *every* case, but the worst case is $\Theta(n^2)$ |
| 5 | running time $\in \Theta(n^2)$ | ❌ **False** | Would need an $\Omega(n^2)$ lower bound for *every* case, but the best case is only $\Theta(n)$ |
| 6 | **best-case** running time $\in \Theta(n)$ | ✅ **True** | Directly from §2 |
| 7 | **worst-case** running time $\in \Theta(n^2)$ | ✅ **True** | Directly from §2 |

> 🔑 **The lesson these are drilling** (CLRS says this almost verbatim): you can correctly say
> "insertion sort's running time is $O(n^2)$" — that's a true blanket statement. You **cannot**
> correctly say "insertion sort's running time is $\Theta(n^2)$" with no case qualifier — that's an
> overstatement, since the best case violates it. Always qualify $\Theta$ claims by case unless the
> algorithm (like merge sort) has the *same* order of growth in every case.

---

## 10. Self-check before the test

Work through these without looking back — if any are shaky, that's your remaining study time.

1. State the loop invariant for `INSERTION-SORT` and prove all three properties.
2. Why does the RAM model assume constant-time array indexing, and what would go wrong if a "sort"
   instruction were allowed?
3. Given a cost/times table like §2's, derive $T(n)$ for the best case and the worst case.
4. Write the full set-builder definitions of $O$, $\Omega$, $\Theta$ from memory — bound, direction,
   number of constants, and the "$\forall n \ge n_0$" clause.
5. Prove $3n^2+2n+5 = \Theta(n^2)$ from the definition (find explicit $c_1, c_2, n_0$) — then check:
   is $f(n)/g(n)$ increasing or decreasing here, and does that change which constant a single
   substitution pins down?
6. State transpose symmetry and use it to convert an $O$ claim into an $\Omega$ claim without
   redoing the proof.
7. Why is it correct to say merge sort's running time is $\Theta(n\lg n)$ with no case qualifier,
   but incorrect to say the same for insertion sort?
8. Redo Set A and Set B above with the answers hidden — check your reasoning matches, not just the
   True/False.

**Good `quiz-me` fodder beyond this file:** CLRS exercises 2.2-1, 2.2-2 (selection sort), 3.1-1
(the $n/3$ argument for input sizes not a multiple of 3), 3.2-2, 3.2-3, and 3.2-5 — all answerable
from what's in this guide.
