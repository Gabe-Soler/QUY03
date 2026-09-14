---
course: cmpe-320
type: reference
date: 2026-09-14
tags: [demo-code, cpp14, atomic-types, integer-overflow, pointers, references, pointer-arithmetic, arrays, array-decay, c-strings, undefined-behaviour]
---

# CMPE 320 — Lecture demo programs

Source files handed out by Dr. Samir Mohammad. They are kept as **`.cpp`, not converted to
Markdown** — they are already plain text and greppable, and they have to stay compilable. This
note is the Markdown index for them.

These accompany the **"Basics"** topic (types, pointers, arrays), which is the lecture after
[`../lectures/2026-09-14-lecture03-history-slides.md`](../lectures/2026-09-14-lecture03-history-slides.md)
and matches the syllabus's week 2, "Data Types, Pointers, Arrays".

**To build and run** (macOS, the standard this course teaches):

```bash
g++ -std=c++14 -Wall TestTypes.cpp -o TestTypes.out && ./TestTypes.out
```

> Every one of these programs is a **deliberate gotcha demo**. Several read or write memory they
> don't own, and one dereferences a null pointer on purpose. Expect crashes, garbage values, and
> output that differs between machines — **that is the lesson**, not a bug in the file. This is the
> syllabus's "C++ is not a safe language like Java" made concrete.

---

## [`TestTypes.cpp`](TestTypes.cpp) — atomic types and their memory use

> *"This program declares examples of atomic types and determines their memory usage. Also, the
> behaviour of integers is explored to see if they wrap around as in Java."*

- **C++14 binary literals with digit separators**: `int aVal(0b1100'0010'0001'1111);` — the `'`
  separators are a C++14 feature, which is exactly the standard this course uses.
- An `enum MonthLengths` with explicit values.
- Character types: `char`, `wchar_t`, and the C++11 `char16_t` / `char32_t`.
- Integer types: `short`, `int`, `long`, `long long`, `long long int` — note `short int` and
  `long int` are the same types spelled differently.
- Floating point: `float` (`2.5F`), `double`, `long double`.
- **Integer wrap-around** — the headline question: does C++ wrap like Java? Signed overflow in C++
  is *undefined behaviour*, not guaranteed wrap-around, which is a sharper answer than Java's.

Note the file's own header comment says to compile to **C++14 or C++17**.

## [`TestSimplePointers.cpp`](TestSimplePointers.cpp) — pointers and references

> *"…demonstrates the ability C++ provides to manipulate pointers and to poke around in memory, in
> places where you really don't belong!"*

- **References**: `int& refAVal(aVal);` — assigning through the reference changes the original.
- **`sizeof` on a reference** is the demo's trick question: it reports the size of the *referent*
  (4 for `int`, 16 for `long double`), not of the reference itself. The comment in the file asks
  exactly this.
- **Three equivalent pointer declarations**, with the author preferring `int* ptrAVal(&aVal);`.
- **Dereferencing / indirection**: `*ptrAVal = 200;` changes `aVal`.
- **Pointer arithmetic into memory you don't own**: `ptrAVal + 1`, `ptrAVal - 1`, then *writing*
  through it with `*above = 1000;`. This is undefined behaviour and the whole point of the demo.
- `int* wayOut(ptrAVal + 1000);` — the dereference and assignment are commented out because they
  crash. The comment asks "why?"
- **Pointer sizes**: `sizeof(int*)`, `sizeof(long double*)`, `sizeof(void*)` are all the same (8 on
  a 64-bit machine) — the pointer's size doesn't depend on what it points to.
- **Uninitialized pointer** `int* notInitPtr;` printed but not dereferenced.
- **`NULL` vs `nullptr`** — the file says to prefer `nullptr` from C++11 onward.

> ⚠️ **The last statement, `cout << *nullPointer11 << endl;`, dereferences a null pointer and will
> crash the program.** It is left uncommented in the file, unlike the other dangerous lines. Expect
> a segfault at the end of the run; that is the demonstration.

## [`ArrayExample.cpp`](ArrayExample.cpp) — arrays, decay, and C strings

- **Uninitialized array contents** — prints whatever was in that memory.
- **`sizeof` idiom for element count**: `sizeof(anArray) / sizeof(int)`. The file's comment
  immediately adds: *"Use a vector instead!!! Much easier to get the size."*
- **The array name is a pointer**: printing `anArray` gives an address; `&anArray` and
  `&anArray[0]` are the same address.
- **Pointer arithmetic out of bounds** — the loop runs `i = -1` to `5` on a 5-element array, then
  prints `*(anArray + 10)`, asking "how far can I go?" All undefined behaviour.
- **Array decay in function parameters** — `passArray1(int param[])` and `passArray2(int* param)`
  both print `sizeof(param)` as the size of a *pointer*, not the array. The size is lost at the
  call. This is the reason the file keeps recommending `vector`.
- **Writing past the end**: `int bArray[] = {1, 2};` then `bArray[2] = 300;` — a two-element array
  written at index 2. Undefined behaviour that usually appears to "work".
- **C strings**: `char aString[] = "Hello"` is mutable and `sizeof` is 6 (five characters plus the
  terminating `\0`).
- `char* bString = "Goodbye";` — marked in the file as *"Depreciated - don't do this anymore!"*.
  Assigning a string literal to a non-const `char*` was removed in C++11; with
  `-std=c++14 -Wall` expect a warning, and with `-Werror` it fails to build.
- `const char* cString` is the correct form; writing through it is commented out because it is
  not permitted.
- The file's closing advice: *"Better to use the string class instead of C-strings… Better to use
  vectors instead of arrays!"*

---

## Why these matter for the course

The syllabus lists **pointers and references**, **arrays and vectors**, and **strings** as topics,
and warns that C++ "gotchas" will be emphasised. Each of these programs is built around a question
the professor poses in a comment rather than an answer — worth running them and predicting the
output *before* you do, since that is how the material is likely to be tested.
