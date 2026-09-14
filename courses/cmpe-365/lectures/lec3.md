# September 14, 2026, lecture 3 CMPE 365


- input size increase without bound = asymptotic

### Order of running time growth 
    - lower order terms dont mater
    order of growth =  0(n) plug in

for example 
$$t_1(n) = 3n^3 - n^2 + 2 =  \theta(n^3)$$

An asymptoptic efficient algorithm will usually be a better choice unless the input is really small.

### Asymptotic notiation (theta)

$$\theta(g(n)) = (f(n : there \ exist \ constants \ in  \  Z^+,\ c_1, c_2, and \ N_0 \ s.t. \ 0≤c_1g(n)≤f(n)≤c_2g(n) \ for  \ all \ n≥n_0)$$

- $f(n)$ will be tightly bounded by $c_1f(n)  \ and  \ c_2f(n)$

#### Example 1

$$1/2n^2 -3n = \theta(n^2)$$
now to bound $f(n)$, we consider the constants  $c_1, c_2$,
$$c_1n^2≤1/2n^2-3n≤c_2n^2$$ $$c_1≤1/2-3/10≤c_2$$ $$c_1≤1/5≤c_2$$

$$upper bound ≥ 1/5$$
$$lower bound ≤ 1/5$$

### Asymptotic notation O
$O(g(n)) = (f(n) : \ there \ exists \ a \ positive \ integer \ c_1 s,t, 0≤c_1g(n))$


$$ f(n) = \theta(g(n)) , \  implies \ f(n) = O(g(n))$$

theta has both uper and lower bounds
big O has just upper bound

### Symptotic notation (omega) $\Omega$

only a lower bound 

### theorem 
for any two functions f(n) and g(n), we have $$f(n) = \theta(g(n)) \ iff \ f(n) = O(g(n)) \ and  \ f(n) = \Omega(g(n))$$


