---
course: mthe-351
type: problem-set
date: 2026-09-08
tags: [set-theory, set-operations, de-morgan, cartesian-product, intervals, nested-intervals, practice]
source: Problem_set_0_mthe351.pdf
---

# MTHE 351 — Practice Problem Set 0: Elementary Set Theory

> **Practice only — not submitted and not graded.** The syllabus lists 10 *Homework* assignments
> via Crowdmark worth 10% collectively; this "Problem Set 0" is not one of them. It is the drill
> set for [Lecture 1](../lectures/2026-09-08-lecture01-introduction.md).
>
> Source: `ps00-elementary-set-theory.pdf` (2 pp.), kept beside this note. The PDF has a clean text
> layer and converted cleanly; the only repair needed was restoring **$\cap$**, which the extractor
> drops silently (it renders `A∩B` as `AB`). Every restored intersection is forced by the
> surrounding mathematics — e.g. De Morgan in Q4 — but check the PDF if a statement looks odd.

## 1. Insurance policyholders

An insurance company classifies its set $S$ of policyholders using the following sets:

$$
\begin{aligned}
A &= \{x \in S : x \text{ drives a subcompact car}\} \\
B &= \{x \in S : x \text{ drives a car that is more than 5 years old}\} \\
C &= \{x \in S : x \text{ is married}\} \\
D &= \{x \in S : x \text{ is over 20 years of age}\} \\
E &= \{x \in S : x \text{ is male}\}
\end{aligned}
$$

Express each of the following subsets of $S$ in terms of $A, B, C, D$ and $E$.

**(a)** Female policyholders over 20 years of age.
**(b)** Policyholders who are male or drive cars more than 5 years old.
**(c)** Female policyholders over 20 years of age who drive subcompact cars.
**(d)** Male policyholders who are either married or over 20 years of age and do not drive
subcompact cars.

## 2. Sets of integers and reals

Let $\mathbb{N}$ and $\mathbb{R}$ denote the set of positive integers and the set of real numbers,
respectively. Define the following sets:

$$
\begin{aligned}
E &= \{x : x = 2n \ \text{ for } n \in \mathbb{N}\} \\
F &= \{x : x = 2n - 1 \ \text{ for } n \in \mathbb{N}\} \\
A &= \{x \in \mathbb{R} : -4 < x < 3\} \\
B &= \{x \in \mathbb{R} : -1 < x < 7\} \\
C &= \{x \in \mathbb{R} : x^2 = -2\}
\end{aligned}
$$

**(a)** Describe the sets $E$, $F$ and $C$ in words.
**(b)** Find $A \cup B$, $A \cap B$, $A - B$, and $A^c$.
**(c)** Find $F \cup E$, $F \cap C$, and $C^c$.

## 3. Cartesian products with a disk

Let $A = \{(x, y) \in \mathbb{R}^2 : x^2 + y^2 \le 1\}$ and
$B = \{z \in \mathbb{R} : 0 \le z \le 1\} = [0, 1]$.

Describe the following sets in words: $\ A \times B$, $\ A \times \{0\}$, and
$\ A \times \{1/2\}$.

## 4. De Morgan's law

Prove De Morgan's law

$$(A \cup B)^c = A^c \cap B^c$$

by showing that $\ (A \cup B)^c \subseteq A^c \cap B^c\ $ **and** $\ A^c \cap B^c \subseteq (A \cup B)^c$.

> This is the **principle of set equality** from Lecture 1 used as a proof technique: prove
> $X = Y$ by proving $X \subseteq Y$ and $Y \subseteq X$ separately.

## 5. A set identity

Show that for any sets $A$ and $B$ in a universal set $S$,

$$A - (A - B) = A \cap B$$

by using elementary properties of set operations (such as De Morgan's law, distributivity, etc.).

> Note the contrast with Q4: **Q4 wants an element-chasing proof, Q5 wants an algebraic one.** The
> properties list at the end of Lecture 1 is the toolkit for this one, and the
> $X - Y = X \cap Y^c$ rewrite is the way in.

## 6. Cartesian products

Let $A = \{x, y\}$, $B = \{0, 1\}$, and $C = \{-1, 0, 1\}$. Find the following sets:

**(a)** $A \times B$
**(b)** $A \times B \times C$

## 7. Nested intervals and limits

For $n = 1, 2, \dots$ consider the following intervals of the real line:

$$A_n = \left[0,\ 1 + \tfrac{1}{n}\right), \qquad B_n = \left[1,\ 1 + \tfrac{1}{n}\right), \qquad C_n = \left(1,\ 1 + \tfrac{1}{n}\right), \qquad D_n = \left[0,\ 1 - \tfrac{1}{n}\right]$$

**(a)** Determine $\ \displaystyle\bigcap_{n=1}^{\infty} A_n$, $\ \displaystyle\bigcap_{n=1}^{\infty} B_n$, and $\ \displaystyle\bigcap_{n=1}^{\infty} C_n$.

**(b)** Determine $\ \displaystyle\bigcup_{n=1}^{\infty} D_n$.

> 🔑 **Why this question is on a probability problem set.** Countable unions and intersections of
> nested sets are exactly what **Axiom 3 (countable additivity)** in
> [Lecture 3](../lectures/2026-09-11-lecture03-axioms-of-probability.md) operates on, and the
> open-vs-closed endpoint distinction between $B_n$ and $C_n$ is the point — the two differ in a
> single endpoint and their infinite intersections differ accordingly. Getting comfortable with
> this now pays off when continuity of probability measures arrives.
