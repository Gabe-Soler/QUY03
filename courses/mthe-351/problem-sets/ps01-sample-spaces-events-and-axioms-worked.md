---
course: mthe-351
type: problem-set
date: 2026-09-21
tags: [homework-1, worked-solutions, sample-space, events, set-operations, probability-axioms, counterexamples, bonferroni, inclusion-exclusion]
---

# MTHE 351 Homework 1 — Worked Solutions

> ⚠️ **These are my own worked solutions, not an official answer key.** The course has not issued
> one. Everything here is derived from the axioms in
> [Lecture 3](../lectures/2026-09-11-lecture03-axioms-of-probability.md) and checked, but it is not
> the professor's work and carries no authority. The questions are in
> [`ps01-sample-spaces-events-and-axioms.md`](ps01-sample-spaces-events-and-axioms.md).
>
> ✅ **Permitted use.** The [MTHE 351 syllabus](../references/syllabus-f2026.md) allows GenAI **for
> homework assignments only**, as an educational tool — clarifying concepts and getting feedback on
> work — with the expectation that you critically evaluate the output and that submitted work
> reflects your own understanding. Use this to check against after you have worked each question,
> not to copy from. **Due Mon 21 Sep 2026 via Crowdmark.**

> 🔴 **Before you start Q1: your current attempt has one wrong assumption that changes every answer.**
> `Hw1_MTHE351_Gabe_Soler.md` lists outcomes like `[1,1,1,1,1]` and `[1,1,2,2]` with repeated
> labels. The problem says balls are drawn **without replacement**, so no label can appear twice and
> no outcome can be longer than four draws. Redo Q1 on that basis before reading Section 1 below —
> the correction is more valuable than the answer.

---

## 1. Urn with four balls

Balls labelled 1–4, drawn one at a time **without replacement**, stopping as soon as the running
sum **exceeds 4** (strictly greater). The **sequence** drawn is recorded.

### (a) The sample space

Build it as a stopping tree. Two facts prune it fast:

- **No outcome has length 1.** The largest single ball is 4, and $4 \not> 4$.
- **No outcome has length 4.** Any two distinct balls other than $\{1,2\}$ and $\{1,3\}$ already sum
  past 4, and even those two pairs are forced to stop on the third draw (the smallest ball left is
  at least 2, giving $3+2 = 5 > 4$ or $4+2 = 6 > 4$).

So **every outcome has length 2 or 3.**

**Length 2** — first draw $a_1$, second draw $a_2 \ne a_1$, stopping iff $a_1 + a_2 > 4$:

| $a_1$ | continues with | **stops** with |
|---|---|---|
| 1 | 2 (sum 3), 3 (sum 4) | **4** (sum 5) |
| 2 | 1 (sum 3) | **3** (5), **4** (6) |
| 3 | 1 (sum 4) | **2** (5), **4** (7) |
| 4 | — | **1** (5), **2** (6), **3** (7) |

$$\{(1,4),\ (2,3),\ (2,4),\ (3,2),\ (3,4),\ (4,1),\ (4,2),\ (4,3)\} \qquad \text{— 8 outcomes}$$

**Length 3** — the four surviving prefixes are $(1,2), (1,3), (2,1), (3,1)$, each with two balls
left, and both choices stop:

$$\{(1,2,3),\ (1,2,4),\ (1,3,2),\ (1,3,4),\ (2,1,3),\ (2,1,4),\ (3,1,2),\ (3,1,4)\} \qquad \text{— 8 outcomes}$$

$$\boxed{|S| = 16}$$

> ✅ **Brute-force verified.** The full sample space, $|E| = 10$, $|F| = 8$ and all three event sets
> in part (b) were independently re-enumerated by exhaustive search over draw sequences, and match
> the hand derivation exactly. The search also confirms no outcome has length 4 or more.

> 🔑 **Why $a_1 = 4$ does not stop immediately.** The question defines "exceeds 4" as "strictly
> larger than 4" in a bracketed note — that note exists precisely to settle this case. A first draw
> of 4 gives a sum of exactly 4, which does *not* exceed 4, so you draw again. That is why
> $(4,1), (4,2), (4,3)$ are all in $S$ and $(4)$ alone is not.

### (b) Events

$E$ = "one of the balls drawn is 1" · $F$ = "the final sum is even"

Tabulating all 16 outcomes with their sums:

| Outcome | Sum | $\in E$? | $\in F$? |
|---|---|---|---|
| $(1,4)$ | 5 | ✔ | |
| $(2,3)$ | 5 | | |
| $(2,4)$ | 6 | | ✔ |
| $(3,2)$ | 5 | | |
| $(3,4)$ | 7 | | |
| $(4,1)$ | 5 | ✔ | |
| $(4,2)$ | 6 | | ✔ |
| $(4,3)$ | 7 | | |
| $(1,2,3)$ | 6 | ✔ | ✔ |
| $(1,2,4)$ | 7 | ✔ | |
| $(1,3,2)$ | 6 | ✔ | ✔ |
| $(1,3,4)$ | 8 | ✔ | ✔ |
| $(2,1,3)$ | 6 | ✔ | ✔ |
| $(2,1,4)$ | 7 | ✔ | |
| $(3,1,2)$ | 6 | ✔ | ✔ |
| $(3,1,4)$ | 8 | ✔ | ✔ |

so $|E| = 10$ and $|F| = 8$.

> **Note every length-3 outcome contains a 1.** That is forced: the only prefixes that survive to a
> third draw are $(1,2), (1,3), (2,1), (3,1)$, and all four contain a 1.

**(i) Both $E$ and $F$ occur — $E \cap F$**

$$\boxed{E \cap F = \{(1,2,3),\ (1,3,2),\ (1,3,4),\ (2,1,3),\ (3,1,2),\ (3,1,4)\}} \qquad |E \cap F| = 6$$

**(ii) Neither occurs — $E^c \cap F^c = (E \cup F)^c$** *(De Morgan, Lecture 1)*

Take the rows with no ticks at all:

$$\boxed{(E \cup F)^c = \{(2,3),\ (3,2),\ (3,4),\ (4,3)\}} \qquad |(E \cup F)^c| = 4$$

**(iii) Exactly one occurs — $(E - F) \cup (F - E)$**

This is the construction from
[Lecture 2, Example (a)](../lectures/2026-09-09-lecture02-sample-space-and-events.md):
$(E-F) \cup (F-E) = (E \cup F) - (E \cap F)$.

- $E - F$ (has a 1, odd sum): $\{(1,4),\ (4,1),\ (1,2,4),\ (2,1,4)\}$
- $F - E$ (even sum, no 1): $\{(2,4),\ (4,2)\}$

$$\boxed{(E-F) \cup (F-E) = \{(1,4),\ (4,1),\ (2,4),\ (4,2),\ (1,2,4),\ (2,1,4)\}} \qquad = 6$$

> **Consistency check.** $|E \cup F| = |E| + |F| - |E \cap F| = 10 + 8 - 6 = 12$, so
> $|(E\cup F)^c| = 16 - 12 = 4$ ✓ matches (ii), and exactly-one $= 12 - 6 = 6$ ✓ matches (iii).
> The four disjoint pieces $6 + 6 + 4 = 16$ ✓ account for all of $S$.

---

## 2. Three events in set-theoretic operations

**(a) At least two of the three occur.** "At least two" means some *pair* both occur:

$$\boxed{(E \cap F) \cup (E \cap G) \cup (F \cap G)}$$

Note this automatically includes the case where all three occur — $E \cap F \cap G$ is a subset of
each pairwise intersection, so no extra term is needed.

**(b) At most two of the three occur.** "At most two" is the complement of "all three":

$$\boxed{(E \cap F \cap G)^c} \quad = \quad E^c \cup F^c \cup G^c \ \text{ by De Morgan}$$

**(c) Exactly two occur.** Take "at least two" and remove "all three":

$$\boxed{\Big[(E \cap F) \cup (E \cap G) \cup (F \cap G)\Big] - (E \cap F \cap G)}$$

Equivalently, written as an explicit disjoint union of the three ways it can happen:

$$\boxed{(E \cap F \cap G^c) \ \cup\ (E \cap F^c \cap G) \ \cup\ (E^c \cap F \cap G)}$$

> 🔑 **Give the second form if you want the safer mark.** The three pieces are visibly disjoint and
> visibly exhaust "exactly two", so it is self-evidently correct; the subtraction form needs the
> reader to accept that $E\cap F\cap G$ lies inside the union. Both are right.

---

## 3. Which statements are always true?

> The question requires a **proof or counterexample** for each, and says explicitly that **Venn
> diagrams are not acceptable as proofs** (though they may be used for counterexamples).

First, a lemma used twice below.

> **Lemma (monotonicity).** If $X \subseteq Y$ then $P(X) \le P(Y)$.
> *Proof.* $Y = X \cup (Y - X)$ and these are disjoint, so by finite additivity
> $P(Y) = P(X) + P(Y-X)$. By Axiom 1, $P(Y-X) \ge 0$, hence $P(Y) \ge P(X)$. $\blacksquare$

### (a) $P(A) + P(B) \ge P(A)P(B)$ — **always true**

**Proof.** By the corollary to Theorem 2, $0 \le P(B) \le 1$. Since $P(A) \ge 0$ (Axiom 1),
multiplying the inequality $P(B) \le 1$ by the non-negative number $P(A)$ preserves it:

$$P(A)P(B) \le P(A)$$

And since $P(B) \ge 0$,

$$P(A) \le P(A) + P(B)$$

Chaining the two gives $P(A)P(B) \le P(A) + P(B)$. $\blacksquare$

> Note this needs nothing about how $A$ and $B$ relate — no independence, no disjointness. It is
> pure arithmetic on two numbers in $[0,1]$.

### (b) $P(A \cap B) \ge P(A) - P(B^c)$ — **always true**

**Proof.** The sets $A \cap B$ and $A \cap B^c$ are disjoint and their union is $A$, so by finite
additivity

$$P(A) = P(A \cap B) + P(A \cap B^c) \implies P(A \cap B) = P(A) - P(A \cap B^c)$$

Now $A \cap B^c \subseteq B^c$, so by the lemma $P(A \cap B^c) \le P(B^c)$. Subtracting a smaller
quantity leaves a larger result:

$$P(A \cap B) = P(A) - P(A \cap B^c) \ \ge\ P(A) - P(B^c) \qquad \blacksquare$$

> **Equivalent form.** Using Theorem 2, $P(B^c) = 1 - P(B)$, so the claim is
> $$P(A \cap B) \ge P(A) + P(B) - 1$$
> This is the **Bonferroni inequality**, and it is the useful shape to remember: two events each of
> probability $0.9$ must overlap in probability at least $0.8$.

### (c) If $P(A) + P(B) = P(C^c)$ then $A$, $B$, $C$ are mutually exclusive — **false**

**Counterexample.** Roll a fair die, $S = \{1,2,3,4,5,6\}$ with equally likely outcomes. Take

$$A = \{1,2,3\}, \qquad B = \{3,4,5\}, \qquad C = \emptyset$$

Then by Theorem 3, $P(A) = P(B) = \tfrac{3}{6} = \tfrac12$, and $P(C^c) = P(S) = 1$ by Axiom 2, so
the hypothesis holds:

$$P(A) + P(B) = \tfrac12 + \tfrac12 = 1 = P(C^c) \ \checkmark$$

But $A \cap B = \{3\} \ne \emptyset$, so $A$ and $B$ are **not** mutually exclusive, and the
conclusion fails. $\blacksquare$

> 🔑 **Why it has to be false.** The hypothesis is a single equation between three *numbers*.
> Mutual exclusivity is a statement about *sets*. Numbers cannot constrain set structure: you can
> always redistribute which outcomes sit in $A$ and $B$ while holding $P(A)$ and $P(B)$ fixed. Any
> claim of the shape "this probability equation forces this set relationship" should be treated as
> false until proven otherwise.

---

## 4. Two painted dice

Each die: **2 faces red, 2 black, 1 yellow, 1 white**, and (as ordinary dice) faces numbered 1–6.
Both fair, so all $6 \times 6 = 36$ ordered outcomes are equally likely and Theorem 3 applies.

> 📝 The handout numbers these parts **(b)** and **(c)** with no part (a) — flagged in the filed
> question sheet. Answering the two that are printed.

### (b) Both land on the same number

Same number means the 6 outcomes $(1,1), (2,2), \dots, (6,6)$:

$$P(\text{same number}) = \frac{6}{36} = \boxed{\frac{1}{6}} \approx 0.1667$$

### (c) Both land on the same colour

The colour events on a single die have probabilities $\tfrac26, \tfrac26, \tfrac16, \tfrac16$. The
four "same colour" cases are mutually exclusive, so by **finite additivity**:

$$
\begin{aligned}
P(\text{same colour})
&= P(\text{both red}) + P(\text{both black}) + P(\text{both yellow}) + P(\text{both white}) \\[2pt]
&= \tfrac{2}{6}\cdot\tfrac{2}{6} + \tfrac{2}{6}\cdot\tfrac{2}{6} + \tfrac{1}{6}\cdot\tfrac{1}{6} + \tfrac{1}{6}\cdot\tfrac{1}{6} \\[2pt]
&= \tfrac{4}{36} + \tfrac{4}{36} + \tfrac{1}{36} + \tfrac{1}{36} = \frac{10}{36} = \boxed{\frac{5}{18}} \approx 0.2778
\end{aligned}
$$

Equivalently, count directly on the 36-outcome sample space: red–red accounts for
$2\times 2 = 4$ face pairs, black–black another 4, yellow–yellow 1, white–white 1, totalling 10.

> 🔑 **This is the "two sample spaces from one experiment" point** from
> [Lecture 2, Example (4)](../lectures/2026-09-09-lecture02-sample-space-and-events.md). The
> 36 face-pairs are equally likely, so Theorem 3 applies there. The 16 *colour* pairs are **not**
> equally likely — red is twice as likely as yellow — so you must not count colour pairs and divide
> by 16. Work on the face-pair space, where equal likelihood actually holds.

---

## 5. Are $Q$ and $R$ probability functions?

$$Q(A) = [P(A)]^3, \qquad R(A) = \frac{P(A)}{3}$$

Check each against the three axioms in turn.

### $Q(A) = [P(A)]^3$ — **not a probability**

| Axiom | Verdict |
|---|---|
| 1. $Q(A) \ge 0$ | ✅ $P(A) \ge 0 \implies [P(A)]^3 \ge 0$ |
| 2. $Q(S) = 1$ | ✅ $Q(S) = [P(S)]^3 = 1^3 = 1$ |
| 3. Countable additivity | ❌ **fails** |

**Counterexample to Axiom 3.** Let $A$ and $B$ be disjoint events with
$P(A) = P(B) = \tfrac12$ and $A \cup B = S$ (a fair coin: $A = \{H\}$, $B = \{T\}$). Then

$$Q(A \cup B) = Q(S) = 1 \qquad\text{but}\qquad Q(A) + Q(B) = \left(\tfrac12\right)^3 + \left(\tfrac12\right)^3 = \tfrac18 + \tfrac18 = \tfrac14$$

and $1 \ne \tfrac14$. $\blacksquare$

The underlying reason: additivity demands $Q(A \cup B) = Q(A) + Q(B)$, i.e.
$(a+b)^3 = a^3 + b^3$, which is false for any $a, b > 0$.

### $R(A) = P(A)/3$ — **not a probability**

| Axiom | Verdict |
|---|---|
| 1. $R(A) \ge 0$ | ✅ $P(A)/3 \ge 0$ |
| 2. $R(S) = 1$ | ❌ **fails** — $R(S) = P(S)/3 = \tfrac13 \ne 1$ |
| 3. Countable additivity | ✅ holds |

**Axiom 3 does hold**, which is worth showing: for mutually exclusive $E_1, E_2, \dots$,

$$R\!\left(\bigcup_{i=1}^{\infty}E_i\right) = \frac{1}{3}P\!\left(\bigcup_{i=1}^{\infty}E_i\right) = \frac{1}{3}\sum_{i=1}^{\infty}P(E_i) = \sum_{i=1}^{\infty}\frac{P(E_i)}{3} = \sum_{i=1}^{\infty}R(E_i)$$

using Axiom 3 for $P$ and the fact that a constant factors out of a convergent series. So $R$ fails
**only** the normalization axiom. $\blacksquare$

> 🔑 **The contrast is the point of the question.** $Q$ is correctly normalized but destroys
> additivity; $R$ is perfectly additive but has total mass $\tfrac13$. Neither is a probability, and
> they fail for opposite reasons. $R$ is "almost" one — $3R$ *is* a probability (it is just $P$), so
> a merely mis-scaled set function is repairable in a way that a nonlinear one is not.

---

## 6. Rings and necklaces

Let $R$ = "wears a ring" and $N$ = "wears a necklace". Given:

$$P(R) = 0.40, \qquad P(N) = 0.30, \qquad P\big((R \cup N)^c\big) = 0.50$$

**Step 1 — get $P(R \cup N)$.** By Theorem 2,

$$P(R \cup N) = 1 - P\big((R\cup N)^c\big) = 1 - 0.50 = 0.50$$

**Step 2 — get $P(R \cap N)$ by inclusion–exclusion.** Deriving the rule rather than quoting it,
since only finite additivity has been proved so far:

$R \cup N = R \cup (N \cap R^c)$ with those two pieces disjoint, so $P(R\cup N) = P(R) + P(N \cap R^c)$.
Also $N = (N \cap R) \cup (N \cap R^c)$, disjoint, so $P(N \cap R^c) = P(N) - P(N \cap R)$.
Substituting:

$$P(R \cup N) = P(R) + P(N) - P(R \cap N)$$

$$\implies P(R \cap N) = 0.40 + 0.30 - 0.50 = 0.20$$

**(a) Ring but not necklace.** $R = (R\cap N) \cup (R \cap N^c)$, disjoint, so

$$P(R \cap N^c) = P(R) - P(R \cap N) = 0.40 - 0.20 = \boxed{0.20 = 20\%}$$

**(b) Necklace but not ring.** Symmetrically,

$$P(N \cap R^c) = P(N) - P(R \cap N) = 0.30 - 0.20 = \boxed{0.10 = 10\%}$$

> **Consistency check.** The four disjoint categories must sum to 1:
> $$\underbrace{0.20}_{\text{both}} + \underbrace{0.20}_{\text{ring only}} + \underbrace{0.10}_{\text{necklace only}} + \underbrace{0.50}_{\text{neither}} = 1.00 \ \checkmark$$

---

## What this homework is really testing

| Q | Skill | Where it came from |
|---|---|---|
| 1 | Building a sample space from a **stopping rule**, and reading a boundary condition exactly ("strictly larger") | Lecture 2 — variable-length-sequence sample spaces |
| 2 | Translating quantified English ("at least two") into set operations | Lecture 2, Example (b) |
| 3 | Proving from the **axioms**, and knowing when to reach for a counterexample instead | Lecture 3 — Theorem 2 and its corollary |
| 4 | Choosing the sample space on which outcomes are **actually** equally likely | Lecture 3, Theorem 3 |
| 5 | Checking a candidate set function against **all three axioms in order** | Lecture 3 — the axioms themselves |
| 6 | Finite additivity on a partition, and deriving inclusion–exclusion rather than quoting it | Lecture 3 — finite additivity |

**The recurring trap is Q3(c) and Q4(c):** both punish assuming a structure that is not there —
that a numerical equation implies disjointness, and that named categories are equally likely. Watch
for that on Quiz 1 (Fri 9 Oct).
