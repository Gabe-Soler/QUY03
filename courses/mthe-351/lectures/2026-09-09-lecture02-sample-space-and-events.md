---
course: mthe-351
type: lecture
date: 2026-09-09
tags: [sample-space, events, random-experiment, certain-event, impossible-event, mutually-exclusive, set-operations, de-morgan, infinite-sample-space]
source: "Lect02-Sample-Space-and-Events .pdf"
---

# MTHE 351 Lecture 2 — Sample Space and Events

> ⚠️ **Conversion fidelity — read this before trusting a symbol.**
> The source is **handwritten tablet notes** (10 pp.) whose only text layer is **Apple's
> handwriting recognition** — it drops all spaces and mangles symbols. This note is a
> **reconstruction**, not a mechanical extraction. **`2026-09-09-lecture02-sample-space-and-events.pdf`
> beside this file is the authority.** Ambiguous passages are left as `<!-- unclear: … -->`
> comments rather than guessed — the worked algebra in Example (a) is the least certain part and is
> flagged inline.
>
> 🖼 **No figures extracted** — the handwriting and diagrams are vector paths. Diagram positions are
> marked **[diagram in original]**.

## TLDR

This lecture starts **Unit I: Axioms of Probability**. It does one thing: it maps the set theory
from Lecture 1 onto probability vocabulary. A **random experiment** has an uncertain outcome; the
set of all its possible outcomes is the **sample space** $S$; subsets of $S$ are **events**. The
dictionary is exact — universal set $\to$ sample space, subset $\to$ event, $\emptyset \to$
impossible event, $S \to$ certain event — so every set identity from Lecture 1 is immediately a
statement about events. Two ideas do real work: **a single experiment can have more than one valid
sample space**, depending on what you choose to record; and **sample spaces need not be finite** —
they can be continuous intervals or sets of infinite-length sequences.

---

## Random experiments

**Definition.** A **random experiment** is a procedure whose outcome is **uncertain** (or
unpredictable).

**Examples:**
- tossing a die or a coin
- drawing a card from a deck
- tomorrow's temperature / weather

## Sample space and events

**Definition.** The set of all possible outcomes of a random experiment is called the **sample
space**, usually denoted $S$. The outcomes are sometimes called **sample points** (or **points**)
in $S$.

**Subsets of the sample space $S$ are called events**, usually denoted $A, B, C, D$, etc. — e.g.
$A \subseteq S$.

### Examples

**(1) Flipping a coin.**
$$S = \{H, T\}$$
where $H$ is the outcome "the outcome is heads" and $T$ is "the outcome is tails".

**(2) Rolling a die.**
$$S = \{1, 2, 3, 4, 5, 6\}$$
The event $A$ = "the outcome is even" is $A = \{2, 4, 6\}$.

**(3) Flip a coin repeatedly until obtaining a total of two heads or a total of two tails.**

Here the sample space is
$$S = \{HH,\ TT,\ THT,\ THH,\ HTH,\ HTT\}$$
— **the outcomes are variable-length sequences.**

- The event $A$ = "two flips are needed to stop" is $\ A = \{HH, TT\}$.
- The event $B$ = "three flips are needed to stop" is $\ B = A^c = \{THT,\ THH,\ HTH,\ HTT\}$.

**(4) A coin is flipped 3 times.**

If **the sequence of outcomes** is recorded, the sample space is
$$S_1 = \{HHH,\ HHT,\ HTH,\ HTT,\ THH,\ THT,\ TTH,\ TTT\}$$

But if instead **the number of heads** is recorded, the sample space is
$$S_2 = \{0, 1, 2, 3\}$$

> 🔑 **Note.** Given a random experiment, a sample space **depends on what outcomes are being
> observed and recorded** — so **more than one sample space can be formed from a single
> experiment.** Choosing it is a modelling decision, not something the experiment hands you.

**(5) A patient arrives to a 9:00 AM dentist appointment no later than 9:30 AM.** The amount of
time (in minutes) the patient is late is observed and recorded. Here

$$S = \{t \in \mathbb{R} : 0 \le t \le 30\} = [0, 30]$$

The event $A$ = "the patient arrives more than 10 minutes late" is

$$A = \{t \in S : 10 < t \le 30\} = (10, 30] \ \subseteq S$$

**(6) Observe and measure the lifetime of a bulb in hours.** Here

$$S = \{t : t \ge 0\} = [0, \infty) = \mathbb{R}^+$$

- The subset $B = [1000, \infty)$ is the event "the bulb lasts at least 1000 hours".
- The subset $C = \{25.7\}$ is the event "the bulb lives exactly 25.7 hours".

> **Note.** **A sample space need not be finite in general** — examples (5) and (6) are continuous,
> and the die example at the end of this lecture has infinite-length sequences in it.

---

## Nomenclature of probability theory

In probability theory a slightly different terminology is used than in set theory:

| Set theory | Probability theory |
|---|---|
| universal set $S$ | **sample space** $S$ |
| subset $E$ | **event** $E$ |

- The sample space $S$ is called the **certain event**, since its occurrence is inevitable (it
  contains all the outcomes).
- The empty set $\emptyset = S^c$ is called the **impossible** or **null event**.

### Events as statements

Given $E \subseteq S$ and $F \subseteq S$, if the outcome of the random experiment belongs to $E$,
we say **event $E$ occurs**. Thus:

| Set expression | Reads as |
|---|---|
| $E^c$ | "$E$ does **not** occur" |
| $E \cup F$ | "**at least one** of $E$ or $F$ occurs" |
| $E \cap F$ | "**both** $E$ and $F$ occur simultaneously" |
| $E - F$ | "$E$ occurs **but** $F$ does not occur" |

If $E \subseteq F$, then $F$ occurs whenever $E$ occurs: we say **"$E$ implies $F$"**.

### Countable families of events

Given events $E_1, E_2, \dots, E_n$, then

$$\bigcup_{i=1}^{n} E_i = \{x \in S : x \in E_i \ \text{ for some } i = 1, \dots, n\}$$

is the event that "**at least one** of the $E_i$'s occurs", and

$$\bigcap_{i=1}^{n} E_i = \{x \in S : x \in E_i \ \text{ for all } i = 1, \dots, n\}$$

is the event that "**all** the $E_i$'s occur simultaneously".

**E.g.** if the events $E_1, E_2, \dots, E_n$ are **mutually exclusive**, i.e.

$$E_i \cap E_j = \emptyset \quad \text{for all } i \ne j$$

then

$$\bigcap_{i=1}^{n} E_i = \emptyset \quad \text{(the impossible event)}$$

---

## Worked examples — translating English into set operations

### Example (a) — "exactly one of $E$ or $F$ occurs"

Given events $E$ and $F$ in a sample space $S$, the event "**exactly one of $E$ or $F$ occurs**" is
given by

$$(E - F) \cup (F - E)$$

**[diagram in original]** — the two crescent regions of the Venn diagram shaded, the lens left
white.

Let us show, via the set-operation properties from Lecture 1, that

$$(E - F) \cup (F - E) = (E \cup F) - (E \cap F)$$

**Proof.** We have

$$
\begin{aligned}
(E - F) \cup (F - E)
&= (E \cap F^c) \cup (F \cap E^c) && \text{by definition of set difference} \\
&= \big[(E \cap F^c) \cup F\big] \cap \big[(E \cap F^c) \cup E^c\big] && \text{by distributivity of } \cup \text{ over } \cap \\
&= \big[(E \cup F) \cap (F^c \cup F)\big] \cap \big[(E \cup E^c) \cap (F^c \cup E^c)\big] && \text{distributivity again} \\
&= (E \cup F) \cap S \cap S \cap (F^c \cup E^c) \\
&= (E \cup F) \cap (E^c \cup F^c) \\
&= (E \cup F) \cap (E \cap F)^c && \text{by De Morgan's law} \\
&= (E \cup F) - (E \cap F) && \text{by definition of set difference}
\end{aligned}
$$

<!-- unclear: this is the most heavily mangled passage in the deck. The recognition layer gives
     "=(FSUF)(PUE)bydistributivityofUvisa,& Uf)(E)(I =(EUF)SS(F'v2Y =(UF)(FUEP)deMorgan'slow".
     The first line, the last two lines and the result are legible; the two intermediate
     distributivity steps above are a standard reconstruction of that route and may differ in
     arrangement from the professor's. The IDENTITY and the sequence of justifications
     (set difference → distributivity → De Morgan → set difference) are what the note states, and
     those are certain. Check the PDF before reproducing this proof on an assessment. -->

### Example (b) — three events

Given events $E$, $F$, $G$ in a sample space $S$:

The event "**at least one of $E$, $F$ or $G$ occurs**" is

$$E \cup F \cup G$$

The event "**at most one of $E$, $F$, $G$ occurs**" is

$$(E \cup F \cup G)^c \ \cup\ \Big[(E \cup F \cup G) - \big((E \cap F) \cup (E \cap G) \cup (F \cap G)\big)\Big]$$

reading as: *(none of them occurs)* $\cup$ *(exactly one of them occurs)*, the second bracket being
the construction from part (a) generalised — take everything in the union and remove every point
lying in two or more of the events.

---

## Example — rolling a die until a 6 occurs

A die is repeatedly rolled until a 6 occurs.

### (a) Describe the sample space of the experiment

$S$ consists of **all finite-length sequences** of integers between 1 and 6 such that 6 appears
**only in the last position**, **plus all infinite-length sequences** in which 6 does **not** appear:

$$S = \left(\bigcup_{n=1}^{\infty} A_n\right) \cup B$$

where

$$A_n = \text{"}n \text{ rolls are needed to complete the experiment"}$$

i.e. $A_n$ is the set of length-$n$ sequences $(a_1, \dots, a_n)$ with $a_i \in \{1, \dots, 6\}$
and 6 appearing only in the last position, and

$$B = \{(a_1, a_2, a_3, \dots) : a_j \in \{1, 2, 3, 4, 5\},\ j = 1, 2, \dots\}$$

is the set of infinite-length sequences where 6 never appears.

### (b) What is the event $\left(\bigcup_{n=1}^{\infty} A_n\right)^c$?

This is indeed the event "**6 never appears**":

$$\left(\bigcup_{n=1}^{\infty} A_n\right)^{\!c} = \{(a_1, a_2, a_3, \dots) : a_j \in \{1,\dots,5\}\} = B$$

> 🔑 **Why this example is here.** It is the first sample space in the course that is neither finite
> nor a simple interval: it mixes countably many finite blocks with an uncountable set of infinite
> sequences. The event $B$ — "the experiment never terminates" — is non-empty, which is exactly the
> kind of event the countable-additivity axiom in Lecture 3 has to be able to handle.

---

## Connections

- Every set operation used here is defined in
  [`2026-09-08-lecture01-introduction.md`](2026-09-08-lecture01-introduction.md); this lecture adds
  only the vocabulary layer on top.
- Recall the professor's convention from Lecture 1: **$EF$ written as juxtaposition means
  $E \cap F$**.
- Lecture 3 puts a measure on these events — it defines the **event space ($\sigma$-field)** of
  admissible events and the **axioms of probability** that assign each one a number.
- Homework 1 Q1–Q2 are direct drills on this lecture: writing down a sample space for an
  urn-without-replacement experiment, and expressing "at least two / at most two / exactly two of
  three events occur" in set-theoretic operations — the three-event generalisation of Example (b).
