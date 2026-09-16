---
course: mthe-351
type: lecture
date: 2026-09-15
tags: [monotonicity, inclusion-exclusion, union-bound, boole-inequality, continuity-of-probability, increasing-decreasing-sequences, random-point-selection, uniform-distribution, sigma-field]
source: Lect04-Corollaries-Axioms-Probability.pdf
---

# MTHE 351 Lecture 4 — Corollaries of the Axioms of Probability

> ⚠️ **Conversion fidelity — read this before trusting a symbol.**
> The source is **handwritten tablet notes** (12 pp.) whose only text layer is **Apple's
> handwriting recognition** — it drops every space and mangles symbols. This note is a
> **reconstruction**, not a mechanical extraction: the mathematics below is standard and was
> rebuilt with high confidence by working the derivations forward from the axioms (Lecture 3) and
> cross-checking every number that survived the OCR layer, but
> **`2026-09-15-lecture04-corollaries-of-axioms.pdf` beside this file is the authority** wherever
> something looks wrong. Genuinely unrecoverable passages are left as `<!-- unclear: ... -->`
> rather than guessed.
>
> 🖼 **No figures extracted** — the handwriting and diagrams (a Venn diagram on pp. 1–2 illustrating
> the partition arguments) are vector paths, not embedded images, so nothing could be pulled out.
> Marked **[Venn diagram in original]** below.
>
> ✅ **Both worked examples' numbers were recovered exactly** from the raw OCR text (not
> reconstructed from a similar textbook problem elsewhere) — see the inline notes at each one.

## TLDR

Four results built directly on the three axioms from
[Lecture 3](2026-09-11-lecture03-axioms-of-probability.md): **monotonicity**
($E\subseteq F \Rightarrow P(E)\le P(F)$), the **two-event and $n$-event inclusion–exclusion
formulas**, the **union bound** ($P(E\cup F)\le P(E)+P(F)$), and **continuity of probability**
along monotone sequences of events ($\lim P(E_n) = P(\lim E_n)$). The lecture then applies
continuity to build **continuous probability from scratch** on an interval $(a,b)$: probability
proportional to length, every single point has probability exactly $0$, and — the payoff —
**a probability-1 event need not be the whole sample space**.

---

## Monotonicity

**Theorem.** Given events $E$ and $F$ (in $\mathcal{F}$), if $E \subseteq F$ then
$P(E) \le P(F)$.

**Proof.** Since $E \subseteq F$, we can partition $F$ into two disjoint sets:

$$F = E \cup (F - E), \qquad E \cap (F-E) = \emptyset$$

**[Venn diagram in original]** — $E$ nested inside $F$, the crescent $F-E$ shaded.

Hence by finite additivity (Corollary of Axiom 3, Lecture 3),

$$P(F) = P(E) + P(F-E)$$

and by Axiom 1, $P(F-E) \ge 0$, so

$$P(F) \ge P(E) \qquad \blacksquare$$

**Corollary.** If $E \subseteq F$, then $P(F-E) = P(F) - P(E)$.

---

## Inclusion–exclusion for two events

**Theorem.** For any events $E$ and $F$ (in $\mathcal{F}$),

$$P(E \cup F) = P(E) + P(F) - P(EF)$$

**Proof.** Partition $E \cup F$ as

$$E \cup F = E \cup (F - EF), \qquad E \cap (F-EF) = \emptyset$$

**[Venn diagram in original]** — $E$ and $F$ overlapping, the lens $EF$ and the two crescents shown.

By finite additivity,

$$P(E\cup F) = P(E) + P(F-EF)$$

and since $EF \subseteq F$, the monotonicity corollary above gives $P(F-EF) = P(F)-P(EF)$. So

$$P(E\cup F) = P(E) + \big[P(F)-P(EF)\big] = P(E)+P(F)-P(EF) \qquad \blacksquare$$

**Corollary — the union bound ("Boole's inequality").**

$$P(E\cup F) \le P(E) + P(F)$$

*(Immediate from the theorem, since $P(EF)\ge 0$ by Axiom 1.)*

---

## Generalization — the inclusion–exclusion principle

**For 3 events** $E_1, E_2, E_3$:

$$P(E_1\cup E_2\cup E_3) = P(E_1)+P(E_2)+P(E_3) - P(E_1E_2)-P(E_1E_3)-P(E_2E_3) + P(E_1E_2E_3)$$

**For $n \ge 2$ events** $E_1, E_2, \dots, E_n$ (by induction on the two-event case):

$$P\!\left(\bigcup_{i=1}^n E_i\right) = \sum_{i=1}^n P(E_i) \;-\; \sum_{i<j} P(E_iE_j) \;+\; \sum_{i<j<k} P(E_iE_jE_k) \;-\; \cdots \;+\; (-1)^{n+1} P(E_1E_2\cdots E_n)$$

> In words: *the probability of a union of $n$ events is the sum of the probabilities of these
> events taken one at a time, minus the sum of the probabilities of these events taken two at a
> time, plus the probabilities of these events taken three at a time, and so on* — alternating
> sign, increasing group size.

### Example 1 — divisible by 5 or 7

An integer between 1 and 100 is chosen at random. What is the probability that it is divisible by
either 5 or 7 (or both)?

**Answer.** Let $E$ = "chosen integer divisible by 5", $F$ = "... by 7". Then
$P(E\cup F) = P(E)+P(F)-P(EF)$.

- $P(E) = 20/100 = 1/5$ (twenty multiples of 5 in $[1,100]$)
- $P(F) = 14/100 = 7/50$ (fourteen multiples of 7)
- Since $5$ and $7$ are relatively prime, $EF$ = "divisible by 35" — two multiples of 35 in
  $[1,100]$ (35, 70), so $P(EF) = 2/100 = 1/50$

$$P(E\cup F) = \frac{1}{5}+\frac{7}{50}-\frac{1}{50} = \frac{10+7-1}{50} = \frac{16}{50} = \boxed{0.32 = 32\%}$$

*(Matches the "32%" figure legible at the end of the source page.)*

### Example 2 — the hotel smokers (numbers recovered exactly from the OCR text)

In a hotel with 300 guests: 27 smoke cigarettes, 11 smoke cigars, 8 smoke pipes, 4 smoke both
cigarettes and cigars, 3 smoke both cigarettes and pipes, 3 smoke both cigars and pipes, and 1
guest smokes all three. How many smoking guests are staying in the hotel?

**Answer.** Let $S$ be the set of all guests (sample space), $|S| = N = 300$. Define
$E$ = "smokes cigarettes", $F$ = "smokes cigars", $G$ = "smokes pipes". Then $E\cup F\cup G$ is the
event that a (randomly chosen) guest smokes at least one of the three, and we want $|E\cup F\cup G|$.

Since every guest is equally likely to be the one selected, $P(A) = |A|/N$ for any event $A$
(the counting formula, Theorem 3 from
[Lecture 3](2026-09-11-lecture03-axioms-of-probability.md)) — so applying inclusion–exclusion to
the *probabilities* and multiplying back through by $N=300$ converts it directly into
inclusion–exclusion on the *counts*:

$$
\frac{|E\cup F\cup G|}{300} = P(E\cup F\cup G) = P(E)+P(F)+P(G)-P(EF)-P(EG)-P(FG)+P(EFG)
$$

$$
\Longrightarrow\quad |E\cup F\cup G| = |E|+|F|+|G|-|EF|-|EG|-|FG|+|EFG|
$$

With $|E|=27,\ |F|=11,\ |G|=8,\ |EF|=4,\ |EG|=3,\ |FG|=3,\ |EFG|=1$:

$$|E\cup F\cup G| = 27+11+8-4-3-3+1 = \boxed{37 \text{ guests}}$$

---

## Continuity of the probability function

**Real-analysis motivation.** A function $f:\mathbb{R}\to\mathbb{R}$ is continuous if for all $x$
and every convergent sequence $\{x_n\}$ with $\lim_{n\to\infty} x_n = x$, we have
$\lim_{n\to\infty} f(x_n) = f(x)$. Probability functions have an analogous continuity property.

**Definition — monotone sequences of events.** A sequence of events $E_1, E_2, E_3, \dots$ is

- **increasing** if $E_1 \subseteq E_2 \subseteq E_3 \subseteq \cdots \subseteq E_n \subseteq E_{n+1} \subseteq \cdots$
- **decreasing** if $E_1 \supseteq E_2 \supseteq E_3 \supseteq \cdots \supseteq E_n \supseteq E_{n+1} \supseteq \cdots$

**Definition — the limit of a monotone sequence.**

- If $\{E_n\}$ is **increasing**, define $\displaystyle\lim_{n\to\infty} E_n = \bigcup_{n=1}^{\infty} E_n$
  — the event that **at least one** $E_n$ occurs.
- If $\{E_n\}$ is **decreasing**, define $\displaystyle\lim_{n\to\infty} E_n = \bigcap_{n=1}^{\infty} E_n$
  — the event that **every** $E_n$ occurs.

### Theorem — continuity of $P$

If $\{E_n\}$ is an increasing or decreasing sequence of events, then

$$\lim_{n\to\infty} P(E_n) = P\!\left(\lim_{n\to\infty} E_n\right)$$

**Proof (increasing case — the decreasing case follows by a similar argument on complements).**
Set

$$A_1 = E_1, \qquad A_n = E_n - E_{n-1} \ \text{ for } n \ge 2$$

By construction the $A_i$ are pairwise disjoint ($A_i \cap A_j = \emptyset$ for $i \ne j$), and

$$\bigcup_{i=1}^{n} A_i = E_n \quad \text{for every } n, \qquad\qquad \bigcup_{i=1}^{\infty} A_i = \bigcup_{i=1}^{\infty} E_i = \lim_{n\to\infty} E_n$$

Then

$$
\begin{aligned}
P\!\left(\lim_{n\to\infty} E_n\right) &= P\!\left(\bigcup_{i=1}^{\infty} A_i\right) \\
&= \sum_{i=1}^{\infty} P(A_i) && \text{by Axiom 3 (countable additivity) — the } A_i \text{ are disjoint} \\
&= \lim_{n\to\infty} \sum_{i=1}^{n} P(A_i) && \text{definition of an infinite sum} \\
&= \lim_{n\to\infty} P\!\left(\bigcup_{i=1}^{n} A_i\right) && \text{finite additivity} \\
&= \lim_{n\to\infty} P(E_n) \qquad\blacksquare
\end{aligned}
$$

<!-- unclear: the OCR for this proof is heavily fragmented ("Plimb) P(E)EPIEA)... u=1 Ai's
     disjoint =linpaiPM"). The structure above is the standard, essentially unique proof of
     continuity of a countably-additive measure along a monotone sequence, and the fragments that
     *are* legible ("disjoint", "by axiom 3", the union/lim pattern) are consistent with it — but
     none of the individual equality steps were independently confirmed character-by-character
     against the source the way the two worked examples were. Check the PDF. -->

---

## Random selection of points from an interval

**Motivation.** Want to define the probability of "randomly selecting" a point from a continuous,
bounded interval $(a,b) = \{x : a < x < b\}$ — the sample space here.

For any sub-interval $[\alpha,\beta) \subseteq [a,b)$, denote by $[\alpha,\beta)$ the event "the
point falls in $[\alpha,\beta)$". Intuitively, for $\beta > \alpha$,

$$P([\alpha,\beta)) = k(\beta-\alpha) \quad \text{for some } k > 0$$

— i.e. probability **proportional to length**. Since $S = [a,b)$ and $P(S) = 1$:

$$1 = P(S) = P([a,b)) = k(b-a) \quad\Longrightarrow\quad k = \frac{1}{b-a}$$

So for $a \le \alpha < \beta \le b$:

$$\boxed{P([\alpha,\beta)) = \frac{\beta-\alpha}{b-a}}$$

Any two sub-intervals of $[a,b)$ of the **same length** are equally likely to contain the selected
point.

### What is the probability of selecting one given point?

Consider $a < x_0 < b$ and choose $\varepsilon>0$ small enough that $(x_0-\varepsilon,x_0+\varepsilon) \subseteq (a,b)$.
Define

$$E_n = \left[x_0 - \tfrac1n,\ x_0+\tfrac1n\right), \qquad n \ge 1 \text{ (large enough that } E_n \subseteq [a,b))$$

Then $\{E_n\}$ is a **decreasing** sequence of events, and $\lim_{n\to\infty} E_n = \{x_0\}$ (the
sets shrink down onto the single point). By continuity of $P$:

$$P(\{x_0\}) = P\!\left(\lim_{n\to\infty}E_n\right) = \lim_{n\to\infty} P(E_n) = \lim_{n\to\infty} \frac{2/n}{b-a} = \boxed{0}$$

**Selecting any one specific point from a continuous interval has probability exactly 0.**

### Open vs. half-open vs. closed intervals — it doesn't matter

$$P(\{\alpha,\beta)) = P(\{\alpha\}) + P((\alpha,\beta)), \qquad \{\alpha\} \text{ and } (\alpha,\beta) \text{ disjoint}$$

Since $P(\{\alpha\})=0$, this gives $P((\alpha,\beta)) = P([\alpha,\beta)) = \dfrac{\beta-\alpha}{b-a}$,
and the same argument shows $P([\alpha,\beta]) = P((\alpha,\beta])$ equal the same value too —
**whether or not the endpoints are included never changes the probability**, because each endpoint
alone contributes $0$.

> 🔑 **Two consequences worth remembering, stated explicitly in the lecture:**
> - $P(\{x\}) = 0$ shows there exist **non-empty events with zero probability**.
> - Since $S = [a,b)$ and $P(S) = 1$, but also $P((a,b)) = 1$ (same length, endpoint doesn't
>   matter), **there exist events that are *not equal to* $S$ but still have probability 1**.
>   Probability 1 does **not** mean "certain" in the naive sense of "is the whole sample space" —
>   it only means the axioms assign it the value 1.

### Example — the almost-punctual bus

A bus arrives at a bus station at random between 8:00 and 8:15 am. Its scheduled arrival time is
8:05 am. Say the bus is "**almost punctual**" if it is less than 2 minutes early and less than 5
minutes late. What is the probability that the bus is **not** almost punctual?

**Answer.** $S = [8{:}00, 8{:}15]$, length 15 minutes, uniform. "Less than 2 minutes early" means
arriving after 8:03; "less than 5 minutes late" means arriving before 8:10. So the almost-punctual
window is $(8{:}03, 8{:}10)$, length $10-3=7$ minutes. Let $E$ = "almost punctual", so
$P(E) = 7/15$. Then

$$P(E^c) = 1-P(E) = 1-\frac{7}{15} = \boxed{\frac{8}{15} \approx 0.533}$$

<!-- unclear: the final numeric confirmation on the source page is too fragmented to read back
     ("Wantfind P(&): P((y=1-P(E) =1- E= 9"). The derivation above follows deterministically from
     the problem statement itself (a 7-minute punctual window out of 15), independent of the OCR,
     so the boxed answer is trustworthy even though the source's own written final digit could not
     be independently confirmed character-by-character. Check the PDF if you want the professor's
     own written form of the answer. -->

---

## Connections

- Every corollary here is built directly on **Axioms 1–3** and **Theorems 1–3** from
  [Lecture 3](2026-09-11-lecture03-axioms-of-probability.md) — this lecture is "what falls out of
  the axioms," not new axioms.
- The hotel-smokers example is the clearest link yet between the **abstract inclusion–exclusion
  principle** (a statement about probabilities) and the **counting formula** $P(A)=|A|/N$
  (Theorem 3, equally-likely outcomes) — dividing a counting inclusion–exclusion through by $N$ and
  an ordinary probabilistic inclusion–exclusion are the *same identity*.
- The random-point-selection material is the course's **first genuinely continuous sample space**
  (previous examples — coins, dice, the roll-until-6 experiment — were all discrete or countable).
  It's also the first time an *axiom* (countable additivity via continuity) is doing real work
  rather than finite additivity alone: the single-point-has-probability-zero result is
  **impossible to get from finite additivity**, since summing zero infinitely many times needs the
  countable version.
- Per the syllabus, this is still **Chapter 1 territory** (axioms of probability) — weeks 1–4.
