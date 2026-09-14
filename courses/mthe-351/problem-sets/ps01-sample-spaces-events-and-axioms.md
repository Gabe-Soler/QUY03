---
course: mthe-351
type: problem-set
date: 2026-09-21
tags: [homework-1, sample-space, events, set-operations, probability-axioms, counterexamples, crowdmark, dice, urn-problems]
source: hw1_mthe_251.pdf
---

# MTHE 351 — Homework 1: Sample Spaces, Events and the Axioms

> **Due Monday, 21 September 2026.** This is graded homework — **submitted via Crowdmark**, per the
> [syllabus](../references/syllabus-f2026.md). It is 1 of 10 homework assignments making up 10% of
> the course grade.
>
> ⚠️ **The source file was misnamed.** It arrived as **`hw1_mthe_251.pdf`**, but the document itself
> is headed "**MTHE 351 – Fall 2026, Homework 1**" and its content is exactly the material from
> Lectures 2–3 of this course. There is no MTHE 251 in this repo, and the "251" is a typo for
> **351**. Filed here under the repo's `psNN` convention; the original keeps its content but the
> filed basename is `ps01-sample-spaces-events-and-axioms.pdf`.
>
> The PDF has a clean text layer. The extractor silently drops **$\cap$**, so every intersection
> below was restored from context; check the PDF if a statement looks odd.

## 1. Urn with four balls

An urn contains four balls, labeled 1 to 4. Balls are drawn at random one by one, **without
replacement**, until the sum of the numbers on the balls drawn **exceeds 4**. The sequence of balls
drawn is noted. *[Note: "exceeds 4" means "strictly larger than 4".]*

**(a)** Write down the sample space for this experiment.

**(b)** Let $E$ be the event "one of the balls drawn is 1", and $F$ the event "the final sum of
numbers on the balls drawn is even". Give the set of outcomes corresponding to each of the
following events:

  **(i)** "both $E$ and $F$ occur"
  **(ii)** "neither $E$ nor $F$ occurs"
  **(iii)** "exactly one of the events $E$, $F$ occurs"

> Part (b)(iii) is **Example (a) of [Lecture 2](../lectures/2026-09-09-lecture02-sample-space-and-events.md)**
> applied to a concrete sample space: $(E - F) \cup (F - E) = (E \cup F) - (E \cap F)$.
> Part (a) is the same "variable-length sequences" structure as the stopping examples in that
> lecture — the outcomes are sequences of different lengths, not a fixed-length tuple.

## 2. Three events in set-theoretic operations

Let $E$, $F$, and $G$ be three events. Express the following events using set-theoretic operations:

**(a)** at least two of the three events occur;
**(b)** at most two of the three events occur;
**(c)** exactly two of the three events occur.

> This is the three-event generalisation of **Example (b) of Lecture 2**, which does "at least one"
> and "at most one". Same construction, one level up.

## 3. Which statements are always true?

Which of the following is always true for arbitrary events $A$, $B$ and $C$ defined on some sample
space?

**(a)** $\ P(A) + P(B) \ge P(A)P(B)$

**(b)** $\ P(A \cap B) \ge P(A) - P(B^c)$

**(c)** If $P(A) + P(B) = P(C^c)$, then the events $A$, $B$ and $C$ are mutually exclusive.

> ⚠️ **You must justify each of your answers with a proof or counterexample, as the case may be.
> Venn diagrams are unacceptable as proofs, but can be used for counterexamples.**

> Theorem 2 ($P(E^c) = 1 - P(E)$) and its corollary ($0 \le P(E) \le 1$) from
> [Lecture 3](../lectures/2026-09-11-lecture03-axioms-of-probability.md) are the tools for (a) and
> (b). For (c), note that the *equation* constrains only three numbers — think about whether
> numbers can constrain set relationships at all.

## 4. Two painted dice

Two fair dice both have **two of their sides painted red, two painted black, one painted yellow,
and one painted white**. If we roll this pair of dice, what is the probability that

**(b)** they both land on the same number?
**(c)** they both land on the same color?

<!-- unclear: the handout numbers the parts of Q4 as (b) and (c) with no part (a). The text layer
     shows no (a) and no gap where one would sit, so this looks like a numbering error in the
     original rather than a conversion loss. Check the PDF, and confirm with the TA before
     assuming there are only two parts. -->

> Two different sample spaces on the same physical experiment — the **Example (4)** point from
> Lecture 2. "Same number" needs the 36-outcome equally likely space; "same color" does not, since
> the colors are not equally likely (2, 2, 1, 1 out of 6).

## 5. Are $Q$ and $R$ probability functions?

Let $P$ be a probability defined on a sample space $S$. For events $A$ of $S$ define

$$Q(A) = [P(A)]^3 \qquad \text{and} \qquad R(A) = \frac{P(A)}{3}$$

Is $Q$ a probability on $S$ (i.e., satisfying all probability axioms)? Is $R$ a probability on $S$?
Justify your answers.

> A direct check against **Axioms 1–3** from Lecture 3. Work through them in order for each
> function: non-negativity, $P(S) = 1$, and countable additivity — one of the two fails on the
> second axiom and the other on the third.

## 6. Rings and necklaces

Fifty percent of the students at a high school wear **neither** a ring nor a necklace, 40 percent
wear a ring, and 30 percent wear a necklace. If one of the students is chosen at random, what is
the probability that the student is wearing

**(a)** a ring **but not** a necklace?
**(b)** a necklace **but not** a ring?

> The "neither" figure is $P((R \cup N)^c)$, so Theorem 2 gives $P(R \cup N)$ immediately, and the
> inclusion–exclusion step from there recovers $P(R \cap N)$. "Ring but not necklace" is the set
> difference $R - N = R \cap N^c$ from Lecture 1.
