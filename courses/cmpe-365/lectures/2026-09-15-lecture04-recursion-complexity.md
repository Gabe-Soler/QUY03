---
course: cmpe-365
type: lecture
date: 2026-09-15
tags: [asymptotic-notation, theta-notation, big-o-notation, omega-notation, insertion-sort, practice-questions]
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

#### Are these statements correct?
1. $n + 1 = \theta (n)$
- yes because there exist upper and lower bounds 

2. $n+1 = O(n)$ 
- for O(n) we only care about the upper bound, thus this is correct

3. $n+1 = O(n^2)$
- yes this is correct because $n^2$ can be an upper bound. 


4. $n+1 = \Omega(n)$
5. $n+1 = \Omega(n^2)$
6. $n+1 = \Omega(1)$


#### Are these statements correct?

*Omega -> lower only 
Big O -> only upper 
Theta -> both*

1. Running time of insertion sort is $\Omega(n)$
- in best case -> at least n-1 comparisons -> lower bound
- worst case -> backwards array -> 
2. 
3. 
4. 
5. 
6. 
7. 