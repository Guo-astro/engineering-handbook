---
title: "Language idioms across Python, Java, C++, Go"
description: "Idiomatic patterns for Python, Java, C++, and Go: collections, iteration, sorting, comparators. The dialect each language wants you to write."
slug: 05-language-idioms
part: 0
chapter: 5
difficulty: beginner
prerequisites: [00-how-to-use]
date_updated: 2026-05-24
languages: [python, java, cpp, go]
ladder:
  core: []
  stretch: []
---

# Language idioms across Python, Java, C++, Go

A candidate writes the obvious frequency counter in Python: `Counter(s)`, one line, ships. They open Java to port it for an Amazon loop and write `freq[c]++`. The compiler refuses. Same shape in C++ just works; same shape in Go just works too. One algorithm, four surface forms, two of which lean on a language rule the other two don't have. The whole chapter is in that detail.

This page is the reference you come back to. Every later chapter on the site renders code tabs that follow these conventions; if a Java tab uses `ArrayDeque` for a queue or a Go tab clones a slice before passing it down, that's the page you're reading right now. The eight idiom rules below (DSH-01 through DSH-08) are enforced by CI; this chapter is the rationale and the table.

## The same problem, four ways

Count the frequency of each character in `"abracadabra"`. The answer is `{a: 5, b: 2, r: 2, c: 1, d: 1}`. Here is the canonical Python, short because `collections.Counter` exists for exactly this.

```python
from collections import Counter


def count_freqs(s: str) -> dict[str, int]:
    return dict(Counter(s))
```

**Solution** — Python ([Java](./05-language-idioms/sol.java) · [C++](./05-language-idioms/sol.cpp) · [Go](./05-language-idioms/sol.go))

```python
from collections import Counter


def count_freqs(s: str) -> dict[str, int]:
    """Return a frequency map of characters in s using Counter."""
    return dict(Counter(s))
```

Look at all four side by side. The shapes diverge in two important places. Python and Java make the missing-key check explicit: `Counter` hides it, `getOrDefault(c, 0) + 1` exposes it. C++ and Go let the zero-value rule eliminate the check entirely. `++freq[c]` and `freq[s[i]]++` work because indexing a missing key value-initialises a fresh entry to zero in `std::unordered_map`[^1] and returns the zero value of the value type in `map[byte]int`.[^2]

That single observation generalises to most of what follows. Naming flips by convention in the same way: `count_freqs` for Python (`snake_case` per PEP 8)[^3] and the C++ STL, `countFreqs` for Java (`camelCase`) and Go (`MixedCaps`, where the leading lowercase makes the function package-private).

## The reference table

Twelve idioms across four languages.

| Idiom | Python | Java | C++ | Go |
|---|---|---|---|---|
| **Counter / frequency map** | `Counter(s)` | `m.getOrDefault(c, 0) + 1` then `put` | `++freq[c]` (zero-init) | `freq[c]++` (zero value) |
| **Stack / LIFO** | `list` with `append`/`pop` | `ArrayDeque` (`push`/`pop`) — never `Stack`[^4] | `std::stack` or `vector::push_back`/`pop_back` | `[]T` slice with `append` and `s = s[:len(s)-1]` |
| **Queue / FIFO** | `collections.deque` (`popleft`) | `ArrayDeque` (`offer`/`poll`) | `std::queue` (adapter over `std::deque`) | `[]T` slice or ring buffer |
| **Min-heap** | `heapq` (min by default) | `PriorityQueue` (min by default) | `std::priority_queue` is **MAX**; pass `std::greater<>` for min | `container/heap` with explicit `Less` |
| **Max-heap** | negate values into `heapq` | `PriorityQueue<>(Comparator.reverseOrder())` | `std::priority_queue` (default) | `container/heap` with reversed `Less` |
| **Sorted map / floor / ceiling** | `sortedcontainers.SortedDict` (third-party) | `TreeMap` (red-black tree) | `std::map` (red-black tree) | none in stdlib; use a sorted slice + `sort.Search` |
| **Iterate map (key, value)** | `for k, v in m.items()` | `for (Map.Entry<K,V> e : m.entrySet())` | `for (auto& [k, v] : m)` (C++17) | `for k, v := range m` |
| **Iterate with index** | `for i, v in enumerate(nums)` | `for (int i = 0; i < n; i++)` | `for (size_t i = 0; i < n; ++i)` | `for i, v := range s` |
| **Slice (half-open `[lo, hi)`)** | `s[lo:hi]` (always copies) | `s.subList(lo, hi)` (view) | `std::span<T>{begin+lo, hi-lo}` (C++20) | `s[lo:hi]` (aliases backing array) |
| **Reverse a sequence** | `s[::-1]` (copy) or `list.reverse()` (in-place) | `Collections.reverse(list)` | `std::reverse(begin, end)` | `slices.Reverse(s)` (1.21+) |
| **Sort with comparator** | `key=lambda x: (x[0], x[1])` | `Comparator.comparingInt(...).thenComparingInt(...)`[^5] | lambda returning `bool` | `slices.SortFunc` returning `cmp.Compare` |
| **Custom sort, stable** | `list.sort` (always stable) | `Arrays.sort(Object[])` (stable) | `std::stable_sort` | `slices.SortStableFunc` |

The trap layer. The shape that bites between languages and is the leading source of "my code worked locally" anecdotes:

| Trap | Python | Java | C++ | Go |
|---|---|---|---|---|
| **Integer overflow** | none (`int` is unbounded per PEP 237)[^6] | silent wrap; JLS §4.2.2: "the integer operators do not indicate overflow or underflow in any way"[^7] | undefined behaviour for signed overflow[^8]; widen to `long long` | silent wrap (two's complement); widen to `int64` |
| **Default recursion depth** | 1,000 (raise to `10**6` at module top) | ~5,000–20,000 (`-Xss` controlled) | ~50,000–200,000 on an 8 MB stack | unbounded; goroutine stacks auto-grow |
| **Hash-map iteration order** | insertion order (3.7+) | undefined in `HashMap`; use `LinkedHashMap` for insertion order | undefined in `unordered_map` | randomised by design across map iterations |
| **`>>` on negative input** | floor (`-5 >> 1 == -3`) | arithmetic (sign-extending); use `>>>` for logical | implementation-defined pre-C++20; arithmetic from C++20 | arithmetic for signed; logical for unsigned |
| **Sort stability default** | stable | stable for `Object[]`, not for primitive `int[]` | not stable; use `std::stable_sort` | not stable; use `slices.SortStableFunc` |
| **Comparator overflow** | none (arbitrary precision) | `(a, b) -> a - b` overflows; the resulting comparator is non-transitive and TimSort throws[^5] | subtraction is UB on overflow | wrong order with no panic; use `cmp.Compare` |
| **Map default for missing key** | `KeyError` for `d[k]`, `None` for `d.get(k)` | `null` from `get`; default from `getOrDefault` | value-initialises to zero[^1] | zero value of `V`[^2] |
| **String mutability** | immutable (need `list(s)` to mutate) | immutable (use `StringBuilder`) | mutable (`std::string`) | immutable (`string`); use `[]byte` to mutate |
| **Slice / view aliasing** | always copies | `subList` is a live view of the parent list | iterators and spans alias the underlying container | slices alias by default; `slices.Clone` for independence |

The DSH rules in the companion are this table compressed into a binding contract. DSH-01 forbids subtraction-based comparators (the comparator-overflow row). DSH-04 pins Python's recursion-limit policy. DSH-07 governs sort stability across the four languages. DSH-08 governs `unordered_map` behaviour on adversarial input.

## What you actually need to remember

Three reflexes are worth burning in. They cover the failure modes that account for most of the cross-language porting bugs.

**Python and Java need explicit lookup-or-default; C++ and Go don't.** When the algorithm is "increment a count for this key," `Counter` or `getOrDefault` in the explicit pair, `++freq[k]` or `freq[k]++` in the implicit pair. Pasting `freq[c]++` into Java is a `NullPointerException`. Pasting `getOrDefault` into C++ compiles but reads as a translation, not a native idiom; use the bracket-and-increment form.

**Half-open intervals `[lo, hi)` are universal.** All four languages index from zero and treat ranges as half-open. Python slicing, Java `subList`, C++ iterator pairs, Go slicing: same convention. `len = hi - lo` works without `+1`, which kills off-by-one bugs that closed intervals invite. Skiena's *Algorithm Design Manual* makes the discipline explicit.[^9] The handbook always writes ranges as `[lo, hi)` and never as `[lo, hi]`.

**Boxing is a Java tax; UB is a C++ tax; aliasing is a Go tax.** Each language carries one structural cost the other three avoid. Java's `PriorityQueue<Integer>` autoboxes on every `offer` and `poll`; on a Dijkstra hot path the GC pressure is measurable, and the canonical workaround is `int[]` paired with `Comparator.comparingInt`. C++ signed overflow is undefined under `-O2` and the compiler is free to assume it does not happen; you defend by widening to `int64_t` before the multiply. Go slices share a backing array unless you `slices.Clone`, and the most common Go chapter-code bug is mutating one slice and accidentally mutating another that was passed in by value. Python pays none of these taxes and pays a different one, which is that arbitrary-precision arithmetic and reference semantics together cost a constant factor of three to ten on hot paths.

## Where this leads

[Choosing your interview language](./06-choosing-your-language.md) is the next chapter and answers "given a target company, which one should I write in." The recommendation is mostly Python; the exceptions are Google (Java, C++, JavaScript, or Python only) and a candidate whose day-job language is already fluent.

Every chapter from Part 1 onward consumes this page's idiom rules. When [Arrays: static, dynamic, multi-dimensional](../part-1-linear-data-structures/00-arrays.md) shows a Java tab using `ArrayDeque` for a stack, that's DSH-DSA from this page. When [Hash maps](../part-1-linear-data-structures/03-hash-maps.md) shows a Go tab cloning a slice before passing it down, that's the aliasing rule. The four-language posture only works if the chapters and the reader share this conventions table; this page is where the table lives.

## References

[^1]: cppreference contributors, "std::unordered_map::operator[]", [en.cppreference.com/w/cpp/container/unordered_map/operator_at](https://en.cppreference.com/w/cpp/container/unordered_map/operator_at).

[^2]: The Go Authors, *The Go Programming Language Specification*, "Map types," [go.dev/ref/spec](https://go.dev/ref/spec#Map_types)

[^3]: van Rossum, G., Warsaw, B., and Coghlan, A., "PEP 8 — Style Guide for Python Code," [peps.python.org/pep-0008](https://peps.python.org/pep-0008/). Naming conventions, comprehensions, docstring style.

[^4]: Oracle, *ArrayDeque (Java SE 21)*, [docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayDeque.html](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/ArrayDeque.html)

[^5]: Oracle, *Comparator (Java SE 21)*, [docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html](https://docs.oracle.com/en/java/javase/21/docs/api/java.base/java/util/Comparator.html)

[^6]: Zadka, M. and van Rossum, G., "PEP 237 — Unifying Long Integers and Integers," [peps.python.org/pep-0237](https://peps.python.org/pep-0237/).

[^7]: Java Language Specification, JLS 21, §4.2.2 "Integer Operations," [docs.oracle.com/javase/specs/jls/se21/html/jls-4.html](https://docs.oracle.com/javase/specs/jls/se21/html/jls-4.html#jls-4.2.2).

[^8]: ISO/IEC 14882:2017 (C++17), §6.9.1; cppreference, "Arithmetic operators" §"Overflows," [en.cppreference.com/w/cpp/language/operator_arithmetic](https://en.cppreference.com/w/cpp/language/operator_arithmetic)

[^9]: Skiena, S.S., *The Algorithm Design Manual*, 3rd ed., Springer, 2020, ISBN 978-3-030-54256-6. Half-open interval discipline as a primary tool against off-by-one errors.
