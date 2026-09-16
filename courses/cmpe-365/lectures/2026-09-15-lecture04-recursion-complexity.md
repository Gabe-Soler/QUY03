---
course: cmpe-365
type: lecture
date: 2026-09-15
tags: [asymptotic-notation, theta-notation, big-o-notation, omega-notation, insertion-sort, practice-questions, recursion, base-case]
---

# September 15, 2026 — Lecture 4, CMPE 365

> Gabe's own live-typed notes. **This is the lecture 3 review that opened lecture 4** — both
> practice-question sets are the ones posed (unanswered) at the end of
> [`2026-09-14-lecture03-asymptotic-notations-slides.md`](2026-09-14-lecture03-asymptotic-notations-slides.md).
> A full worked answer key for both sets is in
> [`../summaries/test1-chapters-2-3-study-guide.md`](../summaries/test1-chapters-2-3-study-guide.md) —
> left unanswered here since this file is your own working, not filled in for you.
>
> The rest of lecture 4 (recursion, merge sort, recurrence relations) is filed separately as
> [`2026-09-15-lecture04-recursion-complexity-slides.md`](2026-09-15-lecture04-recursion-complexity-slides.md) —
> **Ch. 4 material, not in scope for Test 1.**

#### Are these statements correct? (the $n+1$ set)
1. $n + 1 = \Theta(n)$
- yes because there exist upper and lower bounds 

2. $n+1 = O(n)$ 
- for O(n) we only care about the upper bound, thus this is correct

3. $n+1 = O(n^2)$
- yes this is correct because $n^2$ can be an upper bound. 


4. $n+1 = \Omega(n)$

> **[added]** Yes — this follows straight from #1: if $n+1=\Theta(n)$, then by definition
> $n+1=O(n)$ *and* $n+1=\Omega(n)$ together (Theorem 3.1). No separate proof needed once #1 is
> established.

5. $n+1 = \Omega(n^2)$

> **[added]** **No.** $\Omega(n^2)$ would need $c\,n^2 \le n+1$ for *every* $n \ge n_0$, for some
> fixed $c>0$. But $(n+1)/n^2 \to 0$ as $n\to\infty$, so no positive $c$ can stay below that ratio
> forever — past some point $n^2$ always overtakes $n+1$, whatever $c$ you pick.

6. $n+1 = \Omega(1)$

> **[added]** Yes, trivially: $n+1 \ge 1$ for every $n\ge 0$, so $c=1,\,n_0=1$ satisfies the
> $\Omega(1)$ definition directly.


#### Are these statements correct? (insertion sort's running time)

*Omega -> lower only 
Big O -> only upper 
Theta -> both*

1. Running time of insertion sort is $\Omega(n)$
- in best case -> at least n-1 comparisons -> lower bound
- worst case -> backwards array -> more comparisons than the best case, never fewer

> **[added, completing the thought]** Since **even the best case never runs faster than
> $cn$** (the outer loop alone forces $n-1$ iterations, each with at least one comparison), *every*
> input — best case included — takes $\Omega(n)$ time. That's what makes the unqualified claim
> true: an $\Omega$ bound only needs to hold for *some* positive constant across all large $n$, and
> the best case already clears that bar, so every slower case clears it too.

2. Running time of insertion sort is $O(n^2)$

> **[added]** **Yes.** The worst case is $\Theta(n^2)$, and nothing runs slower than the worst
> case — so $O(n^2)$ is a valid blanket upper bound covering every input, not just the worst one.

3. Running time of insertion sort is $\Omega(n^2)$

> **[added]** **No.** The *best* case is $\Theta(n)$, which is **not** $\Omega(n^2)$ ($n$ doesn't
> grow as fast as $n^2$) — so this fails for at least one input, and an unqualified claim about
> "the running time" has to hold for all of them.

4. Running time of insertion sort is $\Theta(n)$

> **[added]** **No.** A $\Theta(n)$ claim needs an $O(n)$ upper bound on *every* case, but the
> worst case is $\Theta(n^2)$, which is not $O(n)$.

5. Running time of insertion sort is $\Theta(n^2)$

> **[added]** **No**, for the mirror-image reason to #4: $\Theta(n^2)$ needs an $\Omega(n^2)$
> lower bound on *every* case, but the best case is only $\Theta(n)$.

6. The **best-case** running time is $\Theta(n)$

> **[added]** **Yes** — already-sorted input, the `while` test fails immediately every time,
> giving $T(n) = an+b$.

7. The **worst-case** running time is $\Theta(n^2)$

> **[added]** **Yes** — reverse-sorted input, the `while` loop walks the full sorted prefix every
> time, giving $T(n) = an^2+bn+c$.

> **[added]** **The pattern across 1–7, worth keeping as a rule of thumb:** an unqualified
> statement about "the running time" can only be truthfully bounded by the *weakest* claim that
> holds across every case — $O$ of the worst case, $\Omega$ of the best case. A $\Theta$ claim with
> no case qualifier is almost always false for an algorithm whose best and worst cases differ, since
> it would have to pin down every case to the *same* tight bound. Full worked reasoning for both
> question sets, including explicit $c,n_0$ where relevant, is in
> [`../summaries/test1-chapters-2-3-study-guide.md`](../summaries/test1-chapters-2-3-study-guide.md#9-practice-questions--full-answer-key).

### Recursion

- when a function calls itself, stopping once it reaches a **base case** — a condition that does
  not lead to a further recursive call

> **[added — the note stops here, but the lecture continued substantially past this point]**
> From here the lecture moved into: merge sort as the running example of a recursive algorithm;
> turning a recursive algorithm's step count into a **recurrence relation**
> ($T(n) = c_1$ for $n=0$, $T(n) = c_2 + T(n-1)$ for $n\ge1$); and solving it by **repeated
> substitution** — expanding the self-reference a few steps until the pattern in terms of $n$ is
> visible. Two worked examples: a straight-line recursion giving $T(n) = \Theta(n)$, and one with
> an inner loop giving $T(n) = \Theta(n^2)$ (the same arithmetic-series shape as insertion sort's
> worst case). Full derivations of both are in
> [`2026-09-15-lecture04-recursion-complexity-slides.md`](2026-09-15-lecture04-recursion-complexity-slides.md) —
> worth reading in full, since this note doesn't capture any of it. **This is Ch. 4 material, Test 2
> scope (8 Oct), not Test 1.**

---

**Source note.** Cleaned against
[`2026-09-14-lecture03-asymptotic-notations-slides.md`](2026-09-14-lecture03-asymptotic-notations-slides.md)
(both practice-question sets originate there, unanswered) and
[`2026-09-15-lecture04-recursion-complexity-slides.md`](2026-09-15-lecture04-recursion-complexity-slides.md)
(the recursion section). One Tier 1 fix: `\theta` → `\Theta` in the first question (lowercase
theta is an angle; capital $\Theta$ is the asymptotic tight bound — the professor's slides and
CLRS both use capital throughout). No Tier 3 disagreements found — everything Gabe wrote out in
full was correct; every gap was an incomplete or missing answer, not a wrong one. 
