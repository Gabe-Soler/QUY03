---
course: cmpe-365
type: lecture
date: 2026-09-14
tags: [asymptotic-notation, order-of-growth, theta-notation, big-o-notation, omega-notation, tight-bounds, upper-bounds, lower-bounds]
---

# September 14, 2026 — Lecture 3, CMPE 365

- Input size increasing without bound = **asymptotic**.

## Order of running time growth

- Lower order terms don't matter.
- Order of growth = $O(n)$, plug in.

For example:

$$t_1(n) = 3n^3 - n^2 + 2 = \Theta(n^3)$$

An asymptotically efficient algorithm will usually be a better choice unless the input is really
small.

## Asymptotic notation (theta)

$$\Theta(g(n)) = \{\, f(n) : \text{there exist constants } c_1, c_2, n_0 \text{ s.t. }
0 \le c_1 g(n) \le f(n) \le c_2 g(n) \text{ for all } n \ge n_0 \,\}$$

> ⚠️ **Check this — "constants in $\mathbb{Z}^+$".** Your note says the constants are in
> $\mathbb{Z}^+$ (positive *integers*). CLRS §3.2 says **positive constants**, i.e. positive reals.
> This matters, and your own Example 1 below is the proof: it lands on $c_1 = 1/5$ and
> $c_2 = 1/2$, neither of which is an integer. If the constants had to be integers, no $c_1$ would
> exist for that example at all.
>
> **Confirmed against the slides (filed 2026-09-14).** Slide 4 of `L03 AsymptoticNotations.pdf`
> reads "there exist **positive constants** $c_1$, $c_2$, and $n_0$" — so "$\in \mathbb{Z}^+$" was
> yours, not the professor's. Definition corrected here.

- $f(n)$ will be tightly bounded by $c_1 g(n)$ and $c_2 g(n)$.

> ⚠️ **Corrected — you wrote $c_1 f(n)$ and $c_2 f(n)$.** Bounding $f(n)$ between two multiples of
> *itself* is trivially true and says nothing. The whole point is that $f$ is sandwiched between
> two multiples of the *comparison* function $g$. Almost certainly a slip while typing, so I fixed
> it here rather than flagging it inline — but it's worth knowing you made it, because it's the
> single most common way to misstate this definition.

### Example 1

$$\tfrac{1}{2}n^2 - 3n = \Theta(n^2)$$

Now to bound $f(n)$, we consider the constants $c_1, c_2$:

$$c_1 n^2 \le \tfrac{1}{2}n^2 - 3n \le c_2 n^2$$

Dividing through by $n^2$ (valid since $n > 0$):

$$c_1 \le \tfrac{1}{2} - \tfrac{3}{n} \le c_2$$

Taking $n = 10$:

$$c_1 \le \tfrac{1}{2} - \tfrac{3}{10} \le c_2 \quad\Longrightarrow\quad c_1 \le \tfrac{1}{5} \le c_2$$

> ⚠️ **The upper constant doesn't follow from this.** Your note concludes
> "upper bound $\ge 1/5$, lower bound $\le 1/5$". The lower one is right; the upper one isn't, and
> the reason is worth understanding because it's the heart of what "for all $n \ge n_0$" means.
>
> Write $h(n) = \tfrac{1}{2} - \tfrac{3}{n}$. This is **increasing** in $n$: $h(10) = 1/5$, but
> $h(100) = 0.47$, and $h(n) \to \tfrac{1}{2}$ as $n \to \infty$.
>
> - **$c_1$** must satisfy $c_1 \le h(n)$ for *every* $n \ge n_0$. Since $h$ is increasing, the
>   tightest case is the smallest one, $n = n_0$. So $n_0 = 10$ gives $c_1 \le 1/5$ — **your
>   conclusion is correct.**
> - **$c_2$** must satisfy $h(n) \le c_2$ for *every* $n \ge n_0$ — including $n = 10^6$. So $c_2$
>   has to beat the *supremum*, not the value at $n_0$. Since $h(n) < \tfrac{1}{2}$ always,
>   $c_2 = \tfrac{1}{2}$ works. **$c_2 = 1/5$ would fail** — at $n = 100$ the expression needs
>   $0.47 \le c_2$.
>
> So the example closes with $c_1 = \tfrac{1}{5}$, $c_2 = \tfrac{1}{2}$, $n_0 = 10$.
>
> The trap: plugging in a single $n$ pins down $c_1$ (because $h$ increases away from $n_0$) but
> tells you nothing about $c_2$ (because $h$ keeps growing). Check which direction your function
> moves before reusing one substitution for both constants.
>
> **Confirmed against the slides.** The deck stops at $c_1 \le \tfrac12 - \tfrac3n \le c_2$ and
> never substitutes a value — **the $n = 10$ step and the "$\ge 1/5$" conclusion are both yours.**
> So this is your own inference to correct, not something mis-copied from the board.

**Conclusion:** $c_1 = \tfrac{1}{5}$, $c_2 = \tfrac{1}{2}$, $n_0 = 10$ satisfy the definition, so
$\tfrac{1}{2}n^2 - 3n = \Theta(n^2)$.

## Asymptotic notation $O$

$$O(g(n)) = \{\, f(n) : \text{there exist positive constants } c, n_0 \text{ s.t. }
0 \le f(n) \le c\,g(n) \text{ for all } n \ge n_0 \,\}$$

> ⚠️ **Your version was missing $f(n)$.** You wrote
> "$O(g(n)) = (f(n) : \text{there exists a positive integer } c_1 \text{ s.t. } 0 \le c_1 g(n))$" —
> which only says $c_1 g(n)$ is non-negative, and never mentions $f(n)$ at all, so it doesn't
> define anything. Two pieces were lost: the **$f(n) \le c\,g(n)$** bound (the actual content) and
> the **for all $n \ge n_0$** condition. Restored from CLRS §3.2. Same "integer" vs "constant"
> issue as above.

$$f(n) = \Theta(g(n)) \implies f(n) = O(g(n))$$

Theta has both upper and lower bounds. Big O has just an upper bound.

## Asymptotic notation (omega) $\Omega$

Only a lower bound.

> **[added from CLRS §3.2 — your note had one line here]**

$\Omega$ gives an **asymptotic lower bound**: $f(n)$ grows at least as fast as $g(n)$, to within a
constant factor.

$$\Omega(g(n)) = \{\, f(n) : \text{there exist positive constants } c, n_0 \text{ s.t. }
0 \le c\,g(n) \le f(n) \text{ for all } n \ge n_0 \,\}$$

It is the mirror image of $O$: where $O$ caps $f(n)$ *above* by $c\,g(n)$, $\Omega$ floors it
*below*. Written side by side, with the differing part in the same position:

| | condition for all $n \ge n_0$ | meaning |
|---|---|---|
| $O(g(n))$ | $0 \le f(n) \le c\,g(n)$ | $f$ grows **no faster** than $g$ |
| $\Omega(g(n))$ | $0 \le c\,g(n) \le f(n)$ | $f$ grows **at least as fast** as $g$ |
| $\Theta(g(n))$ | $0 \le c_1 g(n) \le f(n) \le c_2 g(n)$ | $f$ grows **exactly** like $g$ |

Note $\Theta$ needs **two** constants ($c_1, c_2$) because it clamps from both sides, while $O$ and
$\Omega$ need only one.

**Worked example**, matching Example 1 above: $\tfrac{1}{2}n^2 - 3n = \Omega(n^2)$. Using the same
division by $n^2$, we need $c \le \tfrac{1}{2} - \tfrac{3}{n}$ for all $n \ge n_0$; taking
$n_0 = 10$ and $c = \tfrac{1}{5}$ works — which is exactly the $c_1$ from the $\Theta$ argument.
That is Theorem 3.1 in action: the $\Theta$ proof already contains the $\Omega$ proof.

## Theorem

For any two functions $f(n)$ and $g(n)$, we have

$$f(n) = \Theta(g(n)) \iff f(n) = O(g(n)) \text{ and } f(n) = \Omega(g(n))$$

> **[CLRS Theorem 3.1]** — matches your note exactly. This is the formal version of the line above,
> "theta has both upper and lower bounds, big O has just upper bound": proving a tight bound
> usually means proving the upper and lower bounds separately and invoking this.

---

**Source note.** Originally cleaned against CLRS §3.1–3.2 only, because no slides were filed at the
time. The slides arrived later the same day and are now filed as
[`2026-09-14-lecture03-asymptotic-notations-slides.md`](2026-09-14-lecture03-asymptotic-notations-slides.md)
— **all three flags above were re-checked against them and all three hold.** The
$\tfrac{1}{2}n^2 - 3n$ example is not in CLRS 4th ed. (it is in the 3rd), but it *is* on the
professor's slides, worked to the same point.

**What the lecture covered that this note doesn't.** The slide deck goes further than these notes
do — worth reading the rest of it before the Sep 24 test:

- the counterexample $6n^3 \ne \Theta(n^2)$;
- the general theorem $an^2 + bn + c = \Theta(n^2) = O(n^2) = \Omega(n^2)$, of which your
  Example 1 is the case $a = \tfrac12, b = -3, c = 0$;
- **using asymptotic notation inside equations** ($2n^2 + 3n + 1 = 2n^2 + \Theta(n) = \Theta(n^2)$);
- **properties**: transitivity, reflexivity, and symmetry — including
  $f = O(g) \iff g = \Omega(f)$, i.e. $O$ and $\Omega$ are duals;
- two sets of practice questions, which are the most test-like material available so far.
