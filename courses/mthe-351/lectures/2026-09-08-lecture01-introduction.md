---
course: mthe-351
type: lecture
date: 2026-09-08
tags: [probability, randomness, axiomatic-approach, set-theory, subsets, complement, union, intersection, set-difference, cartesian-product, de-morgan]
source: Lect01-Introduction.pdf
---

# MTHE 351 Lecture 1 — Introduction & Review of Basic Set Theory

> ⚠️ **Conversion fidelity — read this before trusting a symbol.**
> The source is **handwritten notes written on a tablet** (11 pp.). Its only text layer is
> **Apple's handwriting recognition**, which drops every space and mangles mathematical symbols —
> e.g. `AUB= [xeS:AonB(orboth)}` for $A\cup B=\{x\in S: x\in A \text{ or } x\in B\}$. This note is
> a **reconstruction** of that text, not a mechanical extraction: the mathematics below is standard
> elementary set theory and was rebuilt with high confidence, but **`courses/mthe-351/lectures/2026-09-08-lecture01-introduction.pdf`
> beside this file is the authority** wherever something looks wrong.
> Anything genuinely ambiguous is left in an `<!-- unclear: … -->` comment rather than guessed.
>
> 🖼 **No figures were extracted.** The handwriting and the Venn diagrams are **vector paths**, not
> embedded images, so nothing could be pulled out. Every place the original draws a Venn diagram is
> marked **[Venn diagram in original]** below — open the PDF at that point to see it.

## TLDR

Two halves. First, **why probability needs an axiomatic treatment**: everyday intuition about
chance is subjective and varies between people, so the course builds the theory from axioms
instead (intuition still guides *which* axioms and how to interpret results). Second, a **complete
review of elementary set theory** — membership, set-builder notation, subsets, equality,
complement, union, intersection, disjointness, difference, Cartesian products — ending with the
algebraic identities (commutativity, associativity, distributivity, De Morgan) that the rest of the
course manipulates constantly. Nothing here is probability yet; it is the language probability is
written in.

---

## Introduction

Probability theory is a branch of mathematics that focuses on **analyzing and quantitatively
assessing chance and randomness**.

Many phenomena in real life produce outcomes that are **observable** (after occurring) but **not
predictable with certainty** (before occurring).

**Examples:**
- tomorrow's weather
- the outcome of tossing a die
- gambling (games of chance)

Hence the need to calculate "likelihood", "risks" and "chances" in many fields: finance (stock
market), engineering, physics, biology, chemistry, medicine, genetics, pharmacology, epidemiology,
and so on.

### Why an axiomatic approach

One typically has an **intuitive** understanding of probability.

> **Example:** "If an unbiased coin is flipped, then there is a 50% chance (or likelihood) of tails
> coming up."

However, a **subjective interpretation of probability can vary from person to person**. Therefore
we need an **axiomatic approach** to develop a consistent, rigorous theory — although intuition
does play a role in *setting* the axioms and in solving and interpreting problems.

This course provides a basic introduction to probability theory.

---

## Review of basic set theory

**Definition.** A **set** $A$ is a collection of objects. The key idea is **membership** of a set.

**Examples:**
- the set $\mathbb{Z}$ of all integers
- the set of all letters in the alphabet
- the set $\mathbb{R}$ of all real numbers
- the set of all atoms in the universe

The objects in a set $A$ are called **elements** of $A$.

### Notation

- $a \in A$ means "$a$ is an element of the set $A$", or "$a$ is a member of the set $A$", or "$a$
  belongs to the set $A$".
- $a \notin A$ means "$a$ is **not** an element of $A$".

One often defines a set by **listing its elements within braces**, each element listed once:

$$A = \{a, b, c, \dots, z\}$$
$$B = \{2\} \quad \text{— a \textbf{singleton} set}$$
$$\mathbb{Z} = \{\dots, -2, -1, 0, 1, 2, \dots\}$$
$$D = \{0, 1, 4, 9, 16, 25, 36, \dots\}$$

> **Note.** $\{a, b, b, a\} = \{a, a, b, b, b\}$ — **the order of elements does not matter, and
> listing elements repeatedly does not matter either.**

### Set-builder notation

More generally, if $p(x)$ is a statement describing a property of the elements of a set, we can
write $A$ as

$$A = \{x : p(x)\}$$

where the colon reads "**such that**" — i.e. $A$ is the set of all objects $x$ for which $p(x)$
holds.

**Examples:**

$$\{x \in \mathbb{Z} : x \ge 3\} = \{3, 4, 5, \dots\} \quad \text{the set of all integers} \ge 3$$

$$B = \{x \in \mathbb{R} : 0 \le x \le 1\} = [0, 1] \quad \text{the \textbf{unit interval}: all reals between 0 and 1}$$

$$C = \{0, 1, 4, 9, 16, 25, 36, \dots\} = \{m : m = n^2,\ n \in \mathbb{Z}\} \quad \text{the set of all square integers}$$

<!-- unclear: the handwriting-recognition layer renders the last set-builder as "Emim=5,se2]".
     The left side (0,1,4,9,16,25,36,…) makes the squares reading certain; the exact dummy
     variables used by the professor are a reconstruction. Check the PDF. -->

**Definition — empty set.** The **empty set** is a set with no elements, denoted $\emptyset$ (or
$\{\,\}$).

### Subsets

Given sets $A$ and $B$, we say $A$ is a **subset** of $B$ and write $A \subseteq B$ (or
$A \subset B$) if **every** element of $A$ is also an element of $B$:

$$A \subseteq B \iff (x \in A \implies x \in B)$$

**[Venn diagram in original]** — $A$ drawn nested inside $B$.

**Examples:**

$$\mathbb{N} \subset \mathbb{Z} \subset \mathbb{Q} \subset \mathbb{R} \subset \mathbb{C}$$

where $\mathbb{N} = \{0, 1, 2, 3, \dots\}$ is the set of natural numbers, $\mathbb{Z}$ the
integers, $\mathbb{R}$ the reals, and

$$\mathbb{C} = \{z : z = x + iy\}, \quad i = \sqrt{-1} \ \text{(the imaginary unit)}$$

is the set of complex numbers.

<!-- unclear: the recognition layer gives "A22cRLK11" and "· &notasubset" for two items in this
     example list. The chain of number-system inclusions is legible from the surrounding words
     ("set of natural number", "set of integer", "set of real", "set of complex"); the ordering
     above is the standard one. There is also one example of something that is NOT a subset whose
     content could not be recovered. Check the PDF. -->

For any set $A$: $\quad \emptyset \subseteq A$.

### Set equality

Two sets $A$ and $B$ are **equal** if they have exactly the same elements. We write $A = B$.

> **Principle of set equality:**
> $$A = B \iff A \subseteq B \ \text{ and } \ B \subseteq A$$
> where $\iff$ reads "is equivalent to" or "if and only if".

This is the standard route for **proving** two sets equal — show each contains the other. It is
used directly in the De Morgan proof on Problem Set 0, Q4.

### Universe and complementation

Throughout we consider subsets of a fixed **universe** $S$.

Given a universe $S$ and $A \subseteq S$, the **complement** of $A$ (in $S$), denoted $A^c$, is
the set of all elements of $S$ that are **not** in $A$:

$$A^c = \{x \in S : x \notin A\}$$

**[Venn diagram in original]** — the shaded area outside $A$ within the box $S$ is $A^c$.

### Set union

Given two subsets $A$ and $B$ in a universe $S$, the **union** of $A$ and $B$, denoted
$A \cup B$, is the set of all elements which are in $A$, in $B$, or both:

$$A \cup B = \{x \in S : x \in A \ \text{ or } \ x \in B \ \text{(or both)}\}$$

**[Venn diagram in original]** — both circles shaded.

### Set intersection

Given subsets $A$ and $B$ in $S$, the **intersection** of $A$ and $B$, denoted $A \cap B$ (or
$AB$), is the set of all elements that belong to **both** sets:

$$A \cap B = \{x \in S : x \in A \ \text{ and } \ x \in B\}$$

**[Venn diagram in original]** — the lens-shaped overlap shaded.

> 📝 **Notation to carry forward: the professor writes $AB$ for $A \cap B$.** Juxtaposition means
> intersection throughout these notes, and it is used heavily from Lecture 2 onward.

### Disjoint sets

**Definition.** Sets $A$ and $B$ are said to be **(mutually) disjoint** or **mutually exclusive**
if they have no elements in common:

$$A \cap B = \emptyset$$

### Set difference

Given subsets $A$ and $B$ in $S$, the **difference** of $A$ and $B$, denoted $A - B$ (or
$A \setminus B$), is the set of elements of $A$ that are not in $B$:

$$A - B = \{x \in A : x \notin B\} = A \cap B^c$$

**[Venn diagram in original]** — the part of $A$ outside $B$ shaded.

> **Notes.**
> - $S - A = A^c$
> - In general, $A - B \ne B - A$ — **set difference is not commutative.**

### Cartesian products

The **Cartesian product** of sets $A$ and $B$ is the set $A \times B$ defined by

$$A \times B = \{(a, b) : a \in A \ \text{ and } \ b \in B\}$$

**Example.** $A = \{1\}$ and $B = \{1, 2\}$. Then

$$A \times B = \{(1,1), (1,2)\} \quad \text{but} \quad B \times A = \{(1,1), (2,1)\}$$

so **the Cartesian product is not commutative** either.

**Notation.** $A \times A = A^2$, and

$$\underbrace{A \times A \times \cdots \times A}_{n \text{ times}} = A^n, \qquad n > 1$$

---

## Properties of set operations

These are the identities the rest of the course uses without comment.

**Complement and the extremes**

$$S^c = \emptyset \qquad \emptyset^c = S \qquad (A^c)^c = A$$

**Identity and domination**

$$A \cup \emptyset = A \qquad A \cap \emptyset = \emptyset$$
$$A \cup S = S \qquad A \cap S = A$$

**Complement laws**

$$A \cup A^c = S \qquad A \cap A^c = \emptyset$$

**Commutativity**

$$A \cup B = B \cup A \qquad A \cap B = B \cap A$$

**Associativity**

$$A \cup (B \cup C) = (A \cup B) \cup C \qquad A \cap (B \cap C) = (A \cap B) \cap C$$

**Distributivity**

$$A \cup (B \cap C) = (A \cup B) \cap (A \cup C)$$
$$A \cap (B \cup C) = (A \cap B) \cup (A \cap C)$$

**De Morgan's laws**

$$(A \cup B)^c = A^c \cap B^c \qquad (A \cap B)^c = A^c \cup B^c$$

> 🔑 **These are the workhorses.** Lecture 2 uses distributivity and De Morgan to prove that
> "exactly one of $E$, $F$ occurs" can be written two different ways, and Problem Set 0 Q4–Q5 are
> direct drills on them.

---

## Connections

- Everything here is exercised directly by
  [`../problem-sets/ps00-elementary-set-theory.md`](../problem-sets/ps00-elementary-set-theory.md),
  which is the practice set for this lecture.
- Lecture 2 renames this vocabulary for probability: universe $S$ becomes the **sample space**, and
  subsets become **events** — the mathematics is unchanged, only the terminology.
