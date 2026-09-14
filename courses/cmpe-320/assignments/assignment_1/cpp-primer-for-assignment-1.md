---
course: cmpe-320
type: problem-set
date: 2026-09-14
tags: [assignment-1, cpp-basics, python-to-cpp, std-set, random, exceptions, file-io, const-correctness, headers, rejection-sampling]
---

# C++ Primer for Assignment 1 — written from a Python background

> Companion to [`instructions.md`](instructions.md), which holds the handout and the API contract.
> This file covers the *language*: every C++ concept Assignment 1 needs, explained from a starting
> point of "I know Python, I have never written C or C++."
>
> Every code snippet and every number in this file was compiled and run against the real
> `InsultsSource.txt` with `g++ -std=c++14 -Wall` on macOS (Darwin 25.5) on 2026-09-14.

## TLDR

Assignment 1 needs about seven C++ concepts. Python has a direct analogue for five of them; the two
genuinely new ideas are **the header/implementation split** and **`const`**.

The two load-bearing answers:

1. **`std::set`** is a *sorted, duplicate-rejecting* container — a balanced binary search tree, not a
   hash table. Python's `set` is unordered; C++'s `std::set` iterates in sorted order. Insert your
   insults into one and "unique + alphabetical" solves itself, with no sort step and no dedup step.
2. **`rand() % n` is biased**; `<random>` (`std::mt19937` + `std::uniform_int_distribution`) is the
   correct C++11/14 tool and is in scope for this course.

**Measured**: generating 10,000 unique insults with a `std::set` takes **11 ms** with `-O2`,
**36 ms** without. The marked timing test is a non-issue if you use a set.

---

## Part 0 — The three things that make C++ feel alien coming from Python

### 1. There is a compile step, and it is where your errors appear

Python finds a `NameError` when the line runs. C++ finds it before the program exists at all.
`g++` reads your source, checks every type, and emits a machine-code executable.

- **Upside:** a whole class of bugs cannot reach runtime.
- **Downside:** error messages are long. Read only the **first** one — the rest are usually
  cascading noise from it.

### 2. Everything has a declared type, and types are checked

```python
# Python
words = []
words.append("artless")
```

```cpp
// C++
std::vector<std::string> words;
words.push_back("artless");
```

`std::vector<std::string>` is one type meaning "a growable list whose elements are strings". The
`<...>` is a **template parameter** — `vector` is a recipe, `vector<string>` is the concrete type
baked from it. You cannot put an `int` in it.

### 3. Variables hold values, not references to objects

This is the deepest difference and the one that will bite you.

In Python, `b = a` makes `b` point at the same object as `a`. In C++, `b = a` **copies** `a`.
Assigning a 10,000-element vector copies all 10,000 strings. So C++ gives you `&` to say
"don't copy, refer to the original":

```cpp
void f(std::vector<std::string> v);          // copies the whole vector — slow
void f(const std::vector<std::string>& v);   // refers to the caller's vector — free, and read-only
```

`const ...&` ("const reference") is the default way to pass anything bigger than a number.
`const` means "I promise not to modify this", enforced at compile time. **This assignment is
explicitly graded on `const` usage.**

---

## Part 1 — The two concepts the assignment leaves you to discover

### 1.1 `std::set` — the container that does two jobs at once

The assignment needs insults that are **unique** and **alphabetically ordered**. The Python instinct:

```python
insults = set()
while len(insults) < 10000:
    insults.add(make_insult())
result = sorted(insults)     # <- separate sorting step
```

Python's `set` is a **hash set**: `add` is $O(1)$ average, but iteration order is arbitrary, so the
final `sorted()` costs another $O(n \log n)$.

C++ gives two different containers where Python gives one:

| C++ | Implementation | Insert cost | Iteration order | Python equivalent |
|---|---|---|---|---|
| `std::unordered_set<T>` | hash table | $O(1)$ average | arbitrary | `set` |
| `std::set<T>` | balanced BST (red-black tree) | $O(\log n)$ | **sorted, ascending** | *none* |

`std::set` keeps elements sorted *as an invariant of the data structure*. Every insertion walks down
the tree comparing the new element against existing ones and lands it in its correct sorted
position. Walking the set from beginning to end therefore yields sorted output with no sort step:

```cpp
std::set<std::string> unique;
while (unique.size() < 10000)
    unique.insert(makeInsult());          // duplicates silently ignored
std::vector<std::string> result(unique.begin(), unique.end());  // sorted + unique + exactly 10000
```

That last line is a **range constructor**: "build a vector by copying everything from `begin()` up to
`end()`" — roughly Python's `list(some_iterable)`. Because the set iterates in sorted order, the
vector comes out sorted.

Two details that matter:

- **`insert` on a duplicate is a no-op**, not an error. The `while` loop is therefore natural
  rejection sampling: keep drawing until 10,000 *distinct* ones have landed. This is exactly what
  the handout's hint — "a container that maintains sorted order and rejects duplicates does both at
  once" — is pointing at.
- **"Sorted" for `std::string` means lexicographic byte comparison.** Every insult starts with
  `"Thou "`, so ordering is decided by the first word, then the second, then the third. Every word in
  the data file is lowercase ASCII with hyphens, and `'-'` (0x2D) sorts before every letter — so
  lexicographic *is* alphabetical here.
  **Verified:** first insult out is `Thou artless base-court foot-licker!`, last is
  `Thou yeasty weather-bitten giglet!`. Correct on both ends.

### 1.2 Random integers — and why `rand() % n` is wrong

The C way, which appears in older code and in Deitel:

```cpp
srand(time(NULL));
int index = rand() % 50;     // "random number 0..49"
```

**Where the bias comes from.** `rand()` returns an integer uniformly in $[0, \text{RAND\_MAX}]$.
Take `% 50`: outputs $0, \dots, 49$ are hit whenever `rand()` returns something congruent to them
mod 50. If $\text{RAND\_MAX}+1$ is not an exact multiple of 50, low residues get one extra chance.

Concretely, if $\text{RAND\_MAX}+1 = 2^{31} = 2147483648$:

$$2147483648 = 50 \times 42949672 + 48$$

So residues $0$ through $47$ each occur $42\,949\,673$ times, while $48$ and $49$ occur only
$42\,949\,672$ times. The bias is about 1 part in $4.3 \times 10^7$ — invisible here, genuinely fatal
in a Monte Carlo simulation. It is also *not* the main reason to avoid `rand()`: the bigger problems
are that `rand()`'s output quality is implementation-defined and historically poor (some
implementations had visibly periodic low bits), and that `rand() % 50` only works when the range
starts at 0.

**The C++11/14 way** — in scope, since this course teaches C++14:

```cpp
#include <random>

std::mt19937 engine(std::random_device{}());        // the source of randomness
std::uniform_int_distribution<int> dist(0, 49);     // the shape you want
int index = dist(engine);                           // a draw
```

Three pieces, deliberately separated:

- **`std::mt19937`** — the *engine*, a Mersenne Twister generating uniform 32-bit integers. The name
  is its parameters: period $2^{19937}-1$. The standard general-purpose choice.
- **`std::random_device{}()`** — produces a seed from the OS entropy source. The `{}` constructs a
  temporary `random_device`, the `()` calls it. Better than `srand(time(NULL))`, which has
  one-second resolution, so two runs in the same second produce identical output.
  *For debugging, seed with a fixed number (`std::mt19937 engine(12345);`) so runs are reproducible.*
- **`std::uniform_int_distribution<int> dist(0, 49)`** — the *distribution*, mapping the engine's raw
  output onto $[0, 49]$ **inclusive on both ends**, with the modulo bias correctly removed
  (internally by rejecting and redrawing the skewing values). Note it is inclusive of 49, unlike
  Python's `range(50)` / `random.randrange(50)`; it matches `random.randint(0, 49)`.

The separation exists because engines are expensive to construct and distributions are cheap — build
the engine once, draw from it thousands of times.

> **Make the engine a member of your class, not a local inside the generating function.** A fresh
> engine per call would be slow, and if seeded from `time()` would return the same insult repeatedly.

---

## Part 2 — The C++ machinery this assignment needs

| Python | C++14 | Note |
|---|---|---|
| `import x` | `#include <x>` | literal text-paste, not a module object |
| `list[str]` | `std::vector<std::string>` | |
| `set` (unordered) | `std::unordered_set` | |
| *(nothing)* | `std::set` | sorted + unique |
| `str` | `std::string` | mutable, `+` concatenates |
| `class C:` / `def m(self)` | `class C { ... };` / `void C::m()` | note the `;` after `}` |
| `self.x` | `x` (implicit `this`) | no `self` parameter |
| `raise ValueError("msg")` | `throw NumInsultsOutOfBounds("msg")` | |
| `except ValueError as e:` | `catch (NumInsultsOutOfBounds& e) {` | catch **by reference** |
| `with open(f) as fh:` | `std::ifstream in(f);` | closes itself when it goes out of scope |
| *(nothing)* | `const` | compile-time immutability promise |

### 2.1 The two-file split — the one with no Python analogue

You must write **two** files: `insultgenerator_23rtk.h` and `insultgenerator_23rtk.cpp`.

- The **header (`.h`)** holds *declarations*: the shape of your classes — what members exist, their
  names, parameter types, return types. It is the public contract. Think of a `.pyi` type stub,
  except mandatory and actually load-bearing.
- The **implementation (`.cpp`)** holds *definitions*: the actual function bodies.

Why the split exists: `TestInsultGenerator.cpp` needs to know that `InsultGenerator` has a method
`generate` taking an `int` and returning a `vector<string>`, so it can type-check the call on line
49. It does **not** need to know how you implemented it. So it does
`#include "insultgenerator_23rtk.h"` (line 12) and gets exactly the declarations.

`#include` is not `import`. The preprocessor **literally pastes the header's text** into the file at
that point, before compilation. Which leads directly to:

### 2.2 Include guards

If a header were pasted twice you would have two definitions of the same class — a compile error.
Every header is therefore wrapped:

```cpp
#ifndef INSULTGENERATOR_23RTK_H
#define INSULTGENERATOR_23RTK_H
// ... everything ...
#endif
```

"If `INSULTGENERATOR_23RTK_H` isn't defined, define it and include this content; otherwise skip to
`#endif`." A second paste sees the symbol already defined and produces nothing.

`#pragma once` does the same in one line and every real compiler supports it, but it is not in the
standard — **use the traditional guards for a graded assignment.**

### 2.3 Declaring a class, defining its methods

In the header:

```cpp
class InsultGenerator {
public:
    void initialize();
    std::string talkToMe() const;
private:
    std::vector<std::string> column1;
};    // <-- this semicolon is mandatory and everyone forgets it
```

In the `.cpp`:

```cpp
#include "insultgenerator_23rtk.h"

void InsultGenerator::initialize() {
    // body here
}
```

`InsultGenerator::initialize` — the `::` is the **scope resolution operator**, meaning "this is the
`initialize` belonging to `InsultGenerator`", not a free function of the same name. There is no
`self` parameter; inside the body you write `column1` and it implicitly means this object's
`column1`.

**`public:` and `private:` are real access control**, not Python's leading-underscore convention. A
`private` member cannot be touched from outside the class — the compiler refuses. The handout
requires that *only* the five tested methods be public and everything else private, so this maps
directly onto the marking scheme.

### 2.4 `const` on a method

```cpp
std::string talkToMe() const;
```

The trailing `const` means "calling this does not modify the object", enforced by the compiler:
inside a `const` method you cannot assign to any member.

Mark every method `const` that does not change the stored word lists — `talkToMe`, `generate` and
`generateAndSave` all qualify; `initialize` does not, since it fills the columns.

**The one snag, and it is worth understanding.** Drawing from a random engine *mutates* the engine
(it advances its internal state), so `dist(engine)` inside a `const` method will not compile. The
fix is the `mutable` keyword:

```cpp
mutable std::mt19937 engine;
```

`mutable` means "this member is exempt from `const`" — it may be modified even inside a `const`
method. It exists precisely for state that is not part of the object's logical value: caches,
counters, and RNG state. Using it here is correct and demonstrates that you understand what `const`
actually promises.

### 2.5 Exception classes

Python lets you raise anything. C++ requires you to define the class, and the test file constrains it
precisely — line 26–27 is `catch (FileException& e) { cerr << e.what() << endl; }`, so
`FileException` must exist and must have a `what()`.

```cpp
#include <exception>
#include <string>

class FileException : public std::exception {
public:
    explicit FileException(const std::string& msg) : message(msg) {}
    const char* what() const noexcept override { return message.c_str(); }
private:
    std::string message;
};
```

Five new things in six lines:

- **`: public std::exception`** — inheritance. Roughly `class FileException(Exception):`.
- **`explicit`** — prevents the compiler from silently converting a `string` into a `FileException`
  behind your back. Good hygiene on any one-argument constructor.
- **`: message(msg)`** — a **member initializer list**. It runs *before* the constructor body and
  initializes `message` directly from `msg`. Prefer it to assigning inside the body; for `const`
  members and references it is the only option.
- **`const char* what() const noexcept override`** — you are overriding the base class's `what()`, so
  the signature must match **exactly**. `const char*` is a C-style string (a pointer to characters),
  `const` says the method does not modify the object, `noexcept` promises it will not itself throw,
  and `override` tells the compiler to verify you really are overriding something.
  **Always write `override`** — without it, a mistyped signature creates a new unrelated method and
  your real one silently never gets called.
- **`message.c_str()`** — converts `std::string` to `const char*`. The pointer is valid only as long
  as `message` lives, which is why `message` is a **member** of the exception. The classic bug is
  building the message in a local variable and returning its `.c_str()` — the local dies at `return`
  and you hand back a dangling pointer.

Throwing:

```cpp
if (n < 1 || n > 10000)
    throw NumInsultsOutOfBounds("Number of insults must be between 1 and 10000.");
```

`NumInsultsOutOfBounds` is a second, identically-structured class. Note the test catches **by
reference** (`&`); catching by value would slice off the derived part of the object.
**Catch by reference always.**

### 2.6 File I/O and splitting on tabs

```cpp
#include <fstream>
#include <sstream>

std::ifstream inFile("InsultsSource.txt");
if (!inFile)
    throw FileException("Could not open InsultsSource.txt");

std::string line;
while (std::getline(inFile, line)) {
    std::istringstream ss(line);
    std::string w1, w2, w3;
    std::getline(ss, w1, '\t');
    std::getline(ss, w2, '\t');
    std::getline(ss, w3, '\t');
    column1.push_back(w1);
    column2.push_back(w2);
    column3.push_back(w3);
}
```

- **`std::ifstream`** = input file stream. Constructing it opens the file. **It closes itself when it
  goes out of scope** — this is RAII, C++'s answer to `with open(...)`, and it works even if an
  exception unwinds through. An explicit `inFile.close()` is fine for clarity but not required.
- **`if (!inFile)`** — a stream converts to `false` when in a failed state. This is the open-failed
  check, and it is what triggers `FileException`.
- **`std::getline(inFile, line)`** reads one line into `line`, stripping the `\n`, and returns the
  stream — which is `false` at EOF. So the `while` is the idiomatic read-every-line loop,
  ≈ `for line in fh:`.
- **`std::istringstream ss(line)`** wraps a string so you can read *from* it as if it were a file.
  `std::getline(ss, w1, '\t')` then reads up to the next tab. **This is how you split on a delimiter
  in C++** — there is no `line.split('\t')`. The third call has no tab after it, so it takes the rest
  of the line.

**Verified properties of `InsultsSource.txt`** (so you do not need to code defensively): 50 rows,
exactly 3 tab-separated fields each, 50 *distinct* words per column, plain ASCII, Unix `LF` line
endings with **no stray `\r`**. A Windows CRLF file would require stripping a trailing `\r` off `w3`;
this one does not.

Writing is symmetric:

```cpp
std::ofstream outFile(fileName);
if (!outFile)
    throw FileException("Could not write to " + fileName);
for (const std::string& insult : insults)
    outFile << insult << std::endl;
```

`for (const std::string& insult : insults)` is a **range-based for loop** — C++'s
`for insult in insults:`. The `const&` means each element is referred to, not copied.

---

## Part 3 — The design

**Members (all private):**

- three `std::vector<std::string>` for the three columns
- a `mutable std::mt19937` engine
- a `mutable std::uniform_int_distribution<int>` over $[0, 49]$
- a private helper `std::string makeInsult() const;` that draws three indices and assembles
  `"Thou " + w1 + " " + w2 + " " + w3 + "!"`

Making `makeInsult` a private helper is what keeps `talkToMe` and `generate` from duplicating the
assembly logic — and the handout requires everything beyond the five tested methods to be private
anyway.

| Method | What it does | `const`? |
|---|---|---|
| `initialize()` | open, read, fill the three vectors; throw `FileException` on failure | no |
| `talkToMe()` | `return makeInsult();` — one line | yes |
| `generate(int n)` | bounds-check → throw `NumInsultsOutOfBounds`; then the `std::set` loop; then range-construct the vector | yes |
| `generateAndSave(const std::string&, int n)` | call your own `generate(n)` **first**, then open the file | yes |

> **Why `generateAndSave` must bounds-check before touching the file.** Test line 61,
> `generateAndSave("Nothing.txt", 40000)`, is wrapped in a `try` that catches **only**
> `NumInsultsOutOfBounds`. If your file open came first and threw `FileException` there, nothing
> would catch it and the program would `terminate()`. Calling `generate(n)` first gets the ordering
> right *and* avoids duplicating logic — and it means you never leave a stray `Nothing.txt` on the
> grader's disk.

---

## Part 4 — Efficiency, with the actual numbers

The marked timing call is `generate(10000)`. You are rejection-sampling from $N = 50^3 = 125{,}000$
possible insults, wanting $n = 10{,}000$ distinct ones. The expected number of draws is the partial
coupon-collector sum:

$$E[\text{draws}] = \sum_{k=0}^{n-1} \frac{N}{N-k} = N\left(H_N - H_{N-n}\right) \approx N \ln\!\frac{N}{N-n}$$

$$= 125000 \cdot \ln\!\frac{125000}{115000} = 125000 \times 0.08338 \approx 10{,}423$$

So ~10,423 draws for 10,000 uniques — **about 4% wasted work**.
**Measured: 10,414 draws.** The theory holds.

This is the whole reason rejection sampling is fine here. It degrades badly only as $n \to N$
(collecting all 125,000 would take $125000 \times H_{125000} \approx 1.47$ million draws), but at an
8% load factor you never approach that regime.

Total cost: ~10,423 insertions into a `std::set` at $O(\log n)$, so roughly
$\log_2 10000 \approx 13$ string comparisons each. Timed end to end:

```
10000 insults in 11.4 msec     (g++ -std=c++14 -O2)
10000 insults in 35.7 msec     (g++ -std=c++14, no optimization)
```

Both comfortably fast. **The failure mode the handout warns about** is the naive alternative:
generate into a `vector`, then `std::sort` + `std::unique`, then re-generate to top up, repeatedly.
That re-sorts $O(n \log n)$ on every round trip and is where the efficiency marks are lost.

---

## Part 5 — Build and verify

**First, fix the two blockers** in the starter files:

1. Delete the `int main()` from `insultgenerator_23rtk.cpp` — it collides with the `main()` in
   `TestInsultGenerator.cpp` (`duplicate symbol _main` at link time). The implementation file
   contains **only** member-function definitions.
2. Write the class declarations into the currently-empty `insultgenerator_23rtk.h`.

Then, from this folder:

```bash
g++ -std=c++14 -Wall TestInsultGenerator.cpp insultgenerator_23rtk.cpp -o test.out && ./test.out
```

You pass **both** `.cpp` files. The header is pulled in by `#include` and is never compiled directly.
`-Wall` turns on warnings — treat them as errors, since style and correctness are both graded.

**The test prints its insults but never asserts that they are sorted and unique.** Prove it yourself
on the saved file:

```bash
sort -c SavedInsults.txt && echo "sorted OK"
[ "$(sort -u SavedInsults.txt | wc -l)" -eq 1000 ] && echo "1000 unique OK"
```

---

## Part 6 — What `TestInsultGenerator.cpp` actually does

Supplied by Alan McLeod; contains `main()`; you never modify it beyond the `#include` on line 12
(already pointed at `insultgenerator_23rtk.h`). **It is the real specification** — the full API
contract table is in [`instructions.md`](instructions.md). The call sequence:

| Lines | Phase | What it pins down |
|---|---|---|
| 16–20 | setup | `InsultGenerator ig;` — a **default constructor with no args** is required, and the object must be usable before `initialize()` |
| 24–29 | load | `initialize()` takes **no arguments** ⇒ the filename is hardcoded in *your* code. On `FileException` the test does `return 1`, so a wrong filename kills the entire run |
| 32–33 | single insult | `talkToMe()` returns one `string` by value |
| 36–45 | bounds probing | `generate(-100)` and `generate(40000)` must throw `NumInsultsOutOfBounds`. No `return` in these catches — failing to throw silently corrupts the next phase |
| 48–54 | indexed loop | guard checks only `size() > 0`, then indexes `0..99` with unchecked `operator[]`. **Returning 99 elements is undefined behaviour, not a short print** — `generate(n)` must return exactly `n` |
| 60–72 | save | `generateAndSave("Nothing.txt", 40000)` is caught as `NumInsultsOutOfBounds` **only** ⇒ bounds-check before opening the file |
| 75–83 | timed run | `generate(10000)` between `clock()` calls, printed in msec. This is the efficiency mark made visible; `insults.size()` must print `10000` |

**What it does not check** — you must verify these yourself, and the grader will:

- ordering is never asserted, only printed for a human to eyeball
- uniqueness within a batch is never asserted programmatically
- `const` correctness, style, and header documentation are all marked and entirely invisible here

---

## Appendix — verification scratch program

This is **not** the assignment structure — it is a single `main()` with no classes, no exception
hierarchy and no `const` correctness, written only to confirm that the mechanics above compile and
produce the stated numbers. The graded content is exactly the parts this leaves out.

```cpp
#include <iostream>
#include <fstream>
#include <sstream>
#include <string>
#include <vector>
#include <set>
#include <random>
#include <time.h>

int main() {
    std::vector<std::string> c1, c2, c3;
    std::string line;
    std::ifstream in("InsultsSource.txt");
    while (std::getline(in, line)) {
        std::istringstream ss(line);
        std::string a, b, c;
        std::getline(ss, a, '\t');
        std::getline(ss, b, '\t');
        std::getline(ss, c, '\t');
        c1.push_back(a); c2.push_back(b); c3.push_back(c);
    }
    std::mt19937 eng(7);
    std::uniform_int_distribution<int> d(0, 49);
    clock_t s = clock();
    std::set<std::string> u;
    while (u.size() < 10000)
        u.insert("Thou " + c1[d(eng)] + " " + c2[d(eng)] + " " + c3[d(eng)] + "!");
    std::vector<std::string> v(u.begin(), u.end());
    clock_t f = clock();
    std::cout << v.size() << " insults in " << (1e3*(f-s)/CLOCKS_PER_SEC) << " msec" << std::endl;
}
```

---

## Where to look next

- `../../Cpp-Learing-Archive/` — 733 worked source files from Deitel, *C++ How to Program* (10th ed.),
  the course's recommended textbook. The chapters on **classes**, **file I/O** and **exceptions** are
  idiomatic examples of exactly these patterns.
- `../../code/` — the lecture demo programs. Note these are **deliberate gotcha demos**: several read
  or write memory they do not own and one dereferences a null pointer on purpose, so crashes and
  garbage output are the intended lesson, not a bug in your setup.
