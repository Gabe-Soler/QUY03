---
course: mthe-351
type: lecture
date: 2026-09-11
tags: [axioms-of-probability, relative-frequency, sigma-field, event-space, probability-space, countable-additivity, finite-additivity, equally-likely-outcomes, kolmogorov]
source: "Lect03-Axioms-of-Probability .pdf"
---

# MTHE 351 Lecture 3 — Axioms of Probability

> ⚠️ **Conversion fidelity — read this before trusting a symbol.**
> The source is **handwritten tablet notes** (12 pp.) whose only text layer is **Apple's handwriting
> recognition** — all spaces dropped, symbols frequently mangled. This note is a **reconstruction**.
> **`2026-09-11-lecture03-axioms-of-probability.pdf` beside this file is the authority.** Genuinely
> ambiguous passages are left as `<!-- unclear: … -->` comments rather than guessed.
>
> 🖼 **No figures extracted** — handwriting and diagrams are vector paths.

## TLDR

The lecture motivates the axioms by showing the obvious definition **fails**: defining $P(E)$ as
the limiting relative frequency $\lim_{n\to\infty} n(E)/n$ is conceptually broken three ways (you
can't repeat an experiment indefinitely; the limit may not exist; and even if it does, nothing
guarantees you get the same limit next time). So instead the theory **assumes** $P(E)$ exists on a
suitable collection of events and satisfies intuitively desirable axioms.

That collection is the **event space** (a $\sigma$-field) $\mathcal{F}$: closed under complement
and countable union, containing $S$. The **three axioms** are non-negativity, $P(S) = 1$, and
**countable additivity**. Everything else in the lecture is derived from them: $P(\emptyset) = 0$,
finite additivity, $P(E^c) = 1 - P(E)$, and $0 \le P(E) \le 1$. The **equally likely** case then
falls out as a special case giving $P(E) = |E|/N$ — the counting formula — which is proved, not
assumed.

---

## Motivation — why not just use relative frequency?

Consider repeating **indefinitely** a random experiment with sample space $S$.

Let $E \subseteq S$ be an event and let $n(E)$ denote the number of times event $E$ occurs in the
first $n$ repetitions.

One "may" define the probability $P(E)$ of event $E$ as the **limit of the relative frequency** of
$E$ as $n \to \infty$ — i.e. the limit of the fraction of times $E$ occurs out of $n$ experimental
trials:

$$P(E) = \lim_{n \to \infty} \frac{n(E)}{n}$$

However, there are **conceptual problems** with the above definition:

1. In practice, one **cannot repeat an experiment indefinitely**.
2. The **limit above might not exist** in general.
3. Even if the limit exists, **there is no guarantee that it will be the same** when the process is
   run at a later time.

> ⟹ A mathematically consistent theory is possible if we **assume** that $P(E)$ exists for all
> "**measurable**" subsets of $S$, and that it satisfies intuitively desirable **axioms**.

---

## Definition — event space ($\sigma$-field)

Given a random experiment with sample space $S$, an **event space** (or **$\sigma$-field**, or
**$\sigma$-algebra**) $\mathcal{F}$ for $S$ is a collection of events (subsets of $S$) such that:

1. $S \in \mathcal{F}$
2. If $E \in \mathcal{F}$, then $E^c \in \mathcal{F}$  — *(closure under complement)*
3. If $E_1, E_2, \dots \in \mathcal{F}$, then $\displaystyle\bigcup_{i=1}^{\infty} E_i \in \mathcal{F}$  — *(closure under **countable** union)*

The elements of $\mathcal{F}$ are called **measurable sets** or "**$\mathcal{F}$-measurable sets**".
We will only consider such sets in this course — **we simply call them events.**

### Immediate consequences

- $\emptyset \in \mathcal{F}$, since $\emptyset = S^c$ (by 1 and 2).
- The union of a **finite** collection of events in $\mathcal{F}$ also belongs to $\mathcal{F}$ —
  set $E_i = \emptyset$ for all $i$ beyond the finite collection, and apply (3).
- The **intersection** of finitely or countably many events in $\mathcal{F}$ also belongs to
  $\mathcal{F}$.
  **Ex.** If $E, F \in \mathcal{F}$, then
  $$E \cap F = (E^c \cup F^c)^c \in \mathcal{F}$$
  by (2) and (3) — i.e. via De Morgan from Lecture 1.

### Examples of event spaces

- The **simplest** example is $\mathcal{F} = \{\emptyset, S\}$.
- The collection of **all** subsets of $S$ (the **power set** of $S$) is an event space.

---

## Definition — the axioms of probability

Given a sample space $S$ and an event space $\mathcal{F}$ for $S$, a real-valued function $P$ on
$\mathcal{F}$ is called a **probability function** if it satisfies the following:

> **Axiom 1.** $P(E) \ge 0$ for all $E \in \mathcal{F}$.
> $P(E)$ is called the **probability of event $E$**.
>
> **Axiom 2.** $P(S) = 1$.
>
> **Axiom 3.** If $E_1, E_2, \dots$ are **mutually exclusive** events in $\mathcal{F}$
> (i.e. $E_i \cap E_j = \emptyset$ for all $i \ne j$), then
> $$P\!\left(\bigcup_{i=1}^{\infty} E_i\right) = \sum_{i=1}^{\infty} P(E_i)$$
> — the **countable additivity property**.

> **Note.** We call the triplet $(S, \mathcal{F}, P)$ a **probability space**.

---

## Theorem 1 — $P(\emptyset) = 0$

**Proof.** Consider a sequence of events $E_1, E_2, \dots$ in $\mathcal{F}$ such that

$$E_1 = S \quad \text{and} \quad E_i = \emptyset \ \text{ for all } i = 2, 3, \dots$$

Then $\displaystyle\bigcup_{i=1}^{\infty} E_i = S$ and $E_i \cap E_j = \emptyset$ for all
$i \ne j$. Hence

$$
\begin{aligned}
P(S) = P\!\left(\bigcup_{i=1}^{\infty} E_i\right)
&= \sum_{i=1}^{\infty} P(E_i) && \text{by Axiom 3} \\
&= P(S) + \sum_{i=2}^{\infty} P(\emptyset) \\
&= 1 + \sum_{i=2}^{\infty} P(\emptyset) && \text{by Axiom 2}
\end{aligned}
$$

which forces $\ P(\emptyset) = 0$. $\blacksquare$

---

## Consequence of Axiom 3 — finite additivity

For any **finite** number $n$ of mutually exclusive events $E_1, E_2, \dots, E_n$ in $\mathcal{F}$,
we have

$$P\!\left(\bigcup_{i=1}^{n} E_i\right) = \sum_{i=1}^{n} P(E_i) \qquad \textbf{(finite additivity)}$$

**Proof.** Use Axiom 3 by setting $E_{n+1} = E_{n+2} = \cdots = \emptyset$. Then

$$
\begin{aligned}
P\!\left(\bigcup_{i=1}^{n} E_i\right) = P\!\left(\bigcup_{i=1}^{\infty} E_i\right)
&= \sum_{i=1}^{\infty} P(E_i) && \text{by Axiom 3} \\
&= \sum_{i=1}^{n} P(E_i) + \underbrace{\sum_{i=n+1}^{\infty} P(\emptyset)}_{= \ 0 \ \text{ by Theorem 1}} \\
&= \sum_{i=1}^{n} P(E_i) \qquad\blacksquare
\end{aligned}
$$

> 🔑 **Note the logical order.** Countable additivity is the axiom; **finite additivity is a
> theorem derived from it**, and the derivation needs Theorem 1. It does not work the other way
> round — finite additivity alone is strictly weaker.

**Special case ($n = 2$).** For any mutually exclusive events $E$ and $F$,

$$P(E \cup F) = P(E) + P(F)$$

---

## Theorem 2 — $P(E^c) = 1 - P(E)$

**Proof.** $E \cup E^c = S$ and $E \cap E^c = \emptyset$, so

$$1 \overset{\text{Axiom 2}}{=} P(S) = P(E \cup E^c) \overset{\text{finite additivity}}{=} P(E) + P(E^c)$$

hence $P(E^c) = 1 - P(E)$. $\blacksquare$

### Corollary — $0 \le P(E) \le 1$

**Proof.** For any event $E \in \mathcal{F}$,

$$0 \overset{\text{Axiom 1}}{\le} P(E^c) \overset{\text{Thm 2}}{=} 1 - P(E)$$

so $P(E) \le 1$; and $P(E) \ge 0$ by Axiom 1. $\blacksquare$

<!-- unclear: the recognition layer renders this corollary's proof as
     "o=P(s)=1-P(E))< B & ↑asiom! Thm2 Fabiom". The statement 0 ≤ P(E) ≤ 1 and the two
     justifications named in the margin (Axiom 1 and Theorem 2) are legible; the exact chain above
     is the standard reconstruction from those two ingredients. Check the PDF. -->

---

## Example — the fair coin

A coin is called **fair** if $H$ or $T$ are **equally likely** in a single toss of the coin. Let us
apply the probability axioms to determine $P(\{H\})$ and $P(\{T\})$.

Here $S = \{H, T\}$ and $\{H\} \cap \{T\} = \emptyset$, so

$$1 \overset{\text{Axiom 2}}{=} P(S) = P(\{H\}) + P(\{T\}) \overset{\text{equally likely}}{=} 2P(\{H\})$$

$$\therefore \quad P(\{H\}) = P(\{T\}) = \tfrac{1}{2}$$

> 🔑 **This result is a direct consequence of the axioms — not a result of an actual experiment.**
> That is the whole point of the axiomatic route: the $\tfrac12$ is *derived* from "fair" plus the
> axioms, rather than measured by flipping a coin many times.

---

## Equally likely outcomes

Consider a sample space $S = \{s_1, s_2, \dots, s_N\}$ with $N$ **equally likely** outcomes:

$$P(\{s_1\}) = P(\{s_2\}) = \cdots = P(\{s_N\})$$

Then by the axioms we directly have

$$1 \overset{\text{Axiom 2}}{=} P(S) = P\!\left(\bigcup_{i=1}^{N}\{s_i\}\right) \overset{\text{finite additivity}}{=} \sum_{i=1}^{N} P(\{s_i\}) \overset{\text{equally likely}}{=} N \cdot P(\{s_i\})$$

$$\therefore \quad P(\{s_i\}) = \frac{1}{N}, \qquad i = 1, 2, \dots, N$$

> The **equally likely assumption imposes the above probability function** on the sample space $S$ —
> it is an assumption you make about the model, and it then determines $P$ completely.

### Theorem 3 — the counting formula

Let $S$ be a sample space with $N$ equally likely outcomes. Then for all $E \subseteq S$,

$$P(E) = \frac{|E|}{N} = \frac{\text{size of the set } E}{\text{size of the sample space}}$$

**Proof.**

$$P(E) = P\!\left(\bigcup_{s_i \in E}\{s_i\}\right) = \sum_{s_i \in E} P(\{s_i\}) \quad \text{by finite additivity} \quad = \frac{|E|}{N} \qquad\blacksquare$$

> 🔑 **This is why counting matters.** The familiar "favourable outcomes over total outcomes" rule
> is not a definition of probability — it is a **theorem**, valid **only** under the equally likely
> assumption on a **finite** sample space. Applying it when outcomes are not equally likely (see
> the race example below) gives wrong answers.

---

## Worked examples

### Two dice, sum equal to 7

**Q.** If two dice are rolled, what is the probability that the sum of the two resulting numbers is 7?

**A.** Here the sample space is

$$S = \{(i, j) : 1 \le i, j \le 6\}, \qquad |S| = 36$$

Assuming the dice are fair, all 36 outcomes in $S$ are equally likely. The event $E$ = "sum is 7" is

$$E = \{(1,6), (2,5), (3,4), (4,3), (5,2), (6,1)\}$$

$$\therefore \quad P(E) = \frac{6}{36} = \frac{1}{6}$$

### Exactly 2 tails in 3 flips

**Q.** What is the probability of getting exactly 2 tails in 3 flips of a fair coin?

**A.**
$$S = \{HHH, HHT, HTH, HTT, THH, THT, TTH, TTT\}, \qquad N = |S| = 8$$
$$E = \{HTT,\ THT,\ TTH\}$$
$$\therefore \quad P(E) = \frac{|E|}{|S|} = \frac{3}{8}$$

### A race — outcomes **not** equally likely

**Q.** Consider a race with three competitors $A$, $B$ and $C$, where it is assumed that $A$ is
**twice as likely as $B$** to win, and $C$ is **$\tfrac14$ as likely as $A$** to win. Assuming no
ties are allowed, find the probabilities of winning for $A$, $B$ and $C$.

**A.** Let the events be $A$ = "$A$ wins", $B$ = "$B$ wins", $C$ = "$C$ wins", so
$S = \{A, B, C\}$ (the possible winners). We know

$$P(A) = 2P(B) \qquad \text{and} \qquad P(C) = \tfrac{1}{4}P(A)$$

Thus

$$
\begin{aligned}
1 = P(S) &= P(A) + P(B) + P(C) \\
&= 2P(B) + P(B) + \tfrac14\big(2P(B)\big) \\
&= \left(2 + 1 + \tfrac12\right)P(B) = \tfrac{7}{2}P(B)
\end{aligned}
$$

$$\implies P(B) = \frac{2}{7}, \qquad P(A) = \frac{4}{7}, \qquad P(C) = \frac{1}{7}$$

<!-- unclear: the recognition layer gives "Cis4aslikelyasAtowin" for the second condition, with no
     visible fraction, and renders the algebra as "=2P(B)+P(B)+&(2P(D)) =-P(B)3 =>P(BI= 3".
     The coefficient 7/2 and the denominators of 7 in the final answers are only consistent with
     P(C) = (1/4)P(A), which is the reading used above; "C is 4× as likely as A" would give
     denominators of 11. Confirm the fraction against the PDF. -->

> 🔑 **Why this example closes the lecture.** Theorem 3 does not apply — the three outcomes are not
> equally likely, so $P(A) \ne \tfrac13$. You go back to the axioms: the probabilities must be
> non-negative and sum to 1 over the sample space, and the stated ratios pin down the rest.

---

## Connections

- The $\sigma$-field definition leans on **De Morgan's laws** and closure arguments from
  [`2026-09-08-lecture01-introduction.md`](2026-09-08-lecture01-introduction.md).
- The die-until-6 experiment at the end of
  [`2026-09-09-lecture02-sample-space-and-events.md`](2026-09-09-lecture02-sample-space-and-events.md)
  is exactly the kind of sample space that motivates **countable** rather than finite additivity.
- Homework 1 Q3 asks which of several inequalities involving $P(A)$, $P(B)$, $P(A \cap B)$ and
  $P(B^c)$ are always true, with proofs or counterexamples — that is Theorem 2 and the corollary
  applied directly. Q5 asks whether $Q(A) = [P(A)]^3$ and $R(A) = P(A)/3$ are probability
  functions, which is a direct check against Axioms 1–3 above.
- Per the syllabus, this material is **Chapter 1 / §2.1–2.4** of Ghahramani.
