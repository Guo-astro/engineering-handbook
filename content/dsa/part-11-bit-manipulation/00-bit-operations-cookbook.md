---
title: "Bit operations cookbook"
description: "The two identities the rest of Part 11 stands on: x & -x for the lowest set bit, x & (x-1) to clear it. Plus popcount, set/clear/flip/test, and subset iteration."
slug: 00-bit-operations-cookbook
part: 11
chapter: 0
difficulty: intermediate
prerequisites:
  - part-0-foundations/03-bit-manipulation-primer
date_updated: 2026-05-25
languages: [python, java, cpp, go]
canonical_test: LC-338
widgets: []
ladder:
  core: [LC-338, LC-1009, LC-201]
  stretch: [LC-89, LC-1521]
  star: LC-338
---

# Bit operations cookbook

Two expressions carry this chapter:

```text
x & -x         # the value of the lowest set bit
x & (x - 1)    # x with the lowest set bit cleared
```

Everything else in Part 11 is built on those two lines. Fenwick trees walk the index space with `i += i & -i`. Brian Kernighan's popcount loops on `n &= n - 1`. Bitmask DP iterates subsets with `sub = (sub - 1) & mask`. The single-number-XOR family separates two unique numbers by isolating any one bit they differ in — and that bit is `(a ^ b) & -(a ^ b)`. Memorize both identities and the rest of Part 11 stops looking like sorcery.

The other primitives (set, clear, flip, test, popcount, iterate set bits) are one line apiece. This chapter is a reference, not a narrative. Skim it once. Come back when a problem asks for one of the operations and you forgot the exact form.

The [bit manipulation primer](../part-0-foundations/03-bit-manipulation-primer.md) introduced AND, OR, XOR, NOT, shifts, and Brian Kernighan's loop. This chapter is the operational vocabulary on top of those primitives, the one Hacker's Delight §2-1 catalogs and that JDK source comments tag with `// HD, Section 2-1`.[^1]

## Set bit i

```text
x | (1 << i)
```

`1 << i` is a mask with one bit set at position `i`. OR with that mask forces bit `i` to 1 and leaves every other bit alone. Idempotent: setting a bit that's already set is a no-op.

```python
def set_bit(x, i):
    return x | (1 << i)
```

## Clear bit i

```text
x & ~(1 << i)
```

Negate the single-bit mask to get all-ones-except-position-`i`. AND clears bit `i` and leaves the rest. Also idempotent.

Go has a single operator for this combination: `x &^ (1 << i)` reads as "x AND NOT (1 << i)" and saves one token.

```python
def clear_bit(x, i):
    return x & ~(1 << i)
```

## Flip bit i

```text
x ^ (1 << i)
```

XOR with the mask flips the target bit, leaves the others. Two flips return to the original — XOR is its own inverse, the foundational identity for everything in chapter 11.1.

```python
def flip_bit(x, i):
    return x ^ (1 << i)
```

## Test bit i

```text
(x >> i) & 1     # returns 0 or 1
```

Shift bit `i` down to position 0, then mask off everything else. The parentheses are not optional. `x >> i & 1` happens to parse correctly in C, C++, Java, and Python (`>>` binds tighter than `&`), but reviewers will flag it every time, and one day you'll write the same expression with `==` in it and get bitten by `==` binding tighter than `&`. Parenthesize.

```python
def test_bit(x, i):
    return (x >> i) & 1
```

> [!WARNING]
> **Use the unsigned right-shift in Java when the input might be negative.** `(x >> i) & 1` with Java's arithmetic `>>` sign-extends, so testing high bits of a negative `int` always returns 1. Use `(x >>> i) & 1` to get the bit value without sign extension. C++ and Go solve this by using unsigned types (`uint32_t`, `uint32`) for bit work; Python has no fixed width and is unaffected.

## Isolate the lowest set bit: `x & -x`

The first of the two load-bearing identities. Returns a power of two: the value of the lowest set bit of `x`, or zero if `x` is zero.

The proof is two's complement.[^2] By definition `-x = ~x + 1`. Flipping every bit of `x` produces `~x`, where the trailing ones cover the positions that were trailing zeros in `x`. Adding one to `~x` propagates a carry through that run of trailing ones, rolling them back to zero and stopping at the first zero in `~x`. That stopping position is exactly the lowest 1-bit of `x`, and it now holds a 1 in both `x` and `-x`. Every other bit position holds a 1 in exactly one of the two operands. AND keeps only the shared bit.

Walk it on `x = 0b01100` (= 12):

```text
 x = 01100
~x = 10011
-x = 10100   (~x + 1, the carry hits position 2)
x & -x       = 00100   (only position 2 is set in both)
```

Position 2 is the lowest set bit of 12. The result is `4 = 2^2`, a power of two: the *value* of that bit, not its index.

```python
def lowest_set_bit(x):
    return x & -x
```

This is the operation Fenwick trees use for index walks: `update(i, v)` advances by `i += i & -i`, `query(i)` retreats by `i -= i & -i`. The walk costs `O(log n)` per operation because every step strips the lowest set bit, and there are at most `log2(n)` of them.

## Strip the lowest set bit: `x & (x - 1)`

The second load-bearing identity. Returns `x` with the lowest set bit removed, leaving every bit above untouched.

Subtracting one from `x` borrows through the trailing zeros of `x`, flipping them to ones. The borrow stops at the lowest set bit of `x`, which becomes a zero. So `x - 1` and `x` agree above the lowest set bit, disagree at the lowest set bit (1 in `x`, 0 in `x - 1`), and disagree below (0 in `x`, 1 in `x - 1`). AND keeps the agreeing high bits and zeros the rest.

Same `x = 0b01100`:

```text
x     = 01100
x - 1 = 01011    (borrow rolls through positions 0 and 1)
x & (x - 1) = 01000   (positions 3 above; lowest 1 at position 2 is gone)
```

Twelve loses its lowest set bit and becomes eight.

```python
def strip_lowest_set_bit(x):
    return x & (x - 1)
```

The mnemonic that keeps the two identities straight: **minus-x isolates, x-minus-one strips**. They look symmetric. They are not. `x & -x` returns the bit's value; `x & (x - 1)` returns the integer with that bit removed. Submissions on LC 191 and LC 338 routinely swap the two and infinite-loop or return the wrong count. Build the muscle memory before you trust it.

The corollary: `x & (x - 1) == 0` is true iff `x` is a power of two (assuming `x > 0`). A power of two has exactly one set bit; stripping it leaves zero. Anything else has at least two set bits, and stripping the lowest leaves something nonzero.

## Count set bits: Brian Kernighan's loop

The signature application of `x & (x - 1)`. Strip the lowest set bit until `x` is zero; count the iterations.

```python
def popcount(x):
    count = 0
    while x:
        x &= x - 1     # one set bit gone per iteration
        count += 1
    return count
```

Every iteration clears exactly one set bit and never sets one. The loop runs once per set bit, then terminates. On `x = 0xFFFFFFFF` (all 32 bits set) it runs 32 times. On `x = 1` it runs once. The naive `for k in range(32): count += (x >> k) & 1` always runs 32 times regardless of input.

Hand-trace on `x = 0b1011` (= 11):

| iteration | x before | x - 1 | x & (x - 1) | bit cleared | count |
|---|---|---|---|---|---|
| 1 | `1011` | `1010` | `1010` | bit 0 | 1 |
| 2 | `1010` | `1001` | `1000` | bit 1 | 2 |
| 3 | `1000` | `0111` | `0000` | bit 3 | 3 |

Loop exits, returns 3.

The algorithm was first published by Peter Wegner in *CACM* Vol 3 (1960), independently rediscovered by Derrick Lehmer in 1964, and included as exercise 2-9 in *The C Programming Language* 2nd edition (1988), which is why the algorithm carries Kernighan's name.[^1][^3]

The signature problem is LC 338 Counting Bits. Asked to compute popcount for every integer in `[0, n]`, the natural recurrence falls out of `x & (x - 1)`:

```python
def count_bits(n):
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```

**Solution** — Python ([Java](./00-bit-operations-cookbook/lc-338/sol.java) · [C++](./00-bit-operations-cookbook/lc-338/sol.cpp) · [Go](./00-bit-operations-cookbook/lc-338/sol.go))

```python
# LC 338. Counting Bits


def count_bits(n: int) -> list[int]:
    """Return ans[i] = popcount(i) for i in 0..n.

    Recurrence: dp[i] = dp[i & (i - 1)] + 1.
    Cleared-lowest-bit subproblem already solved; add one for the bit just removed.
    O(n) time, O(n) space (output dominates).
    """
    dp = [0] * (n + 1)
    for i in range(1, n + 1):
        dp[i] = dp[i & (i - 1)] + 1
    return dp
```

The subproblem `dp[i & (i - 1)]` is `popcount` of `i` with the lowest bit stripped, already computed because `i & (i - 1) < i`. Add one for the bit just removed. Two lines, `O(n)` time.

## Stdlib popcount: when the loop is the wrong answer

Don't write Brian Kernighan's loop in production. Every modern language ships a popcount intrinsic that compiles to a hardware `POPCNT` instruction on x86 SSE4.2 and ARMv8.[^4]

| Language | Production call | Notes |
|---|---|---|
| Python | `x.bit_count()` (3.10+); `bin(x).count('1')` (older) | `int.bit_count` added in PEP 632. |
| Java | `Integer.bitCount(x)` / `Long.bitCount(x)` | OpenJDK implements the SWAR algorithm from Hacker's Delight Figure 5-2; commented `// HD, Section 5-1`.[^1] |
| C++ | `std::popcount(x)` (C++20, `<bit>`); `__builtin_popcount(x)` (GCC/Clang) | Companion intrinsics in `<bit>`: `std::countl_zero`, `std::countr_zero`, `std::bit_width`, `std::has_single_bit`. Operate on unsigned types only. |
| Go | `bits.OnesCount(x)` (`math/bits`); typed variants `OnesCount32`, `OnesCount64` | Compiler emits `POPCNT` under `GOAMD64=v3` or with the `runtime/internal/cpu` feature check. |

Three things are happening in the background that the loop hides. The SWAR algorithm (*SIMD Within A Register*) uses magic constants `0x55555555`, `0x33333333`, `0x0F0F0F0F` to count bits in parallel across nibbles, bytes, and halves of the word in `O(log w)` operations on a `w`-bit word. JDK's `Integer.bitCount` is exactly this construction; the source is short enough to read in one minute and is the cleanest production reference for the technique.[^1] The hardware `POPCNT` instruction goes one step further and runs in fixed three-cycle latency regardless of input. And the lookup-table approach pre-computes popcount for every 8-bit byte, then sums four lookups for a 32-bit word: the right tool when you want predictable cache behavior more than peak throughput.

The Brian Kernighan loop wins exactly one teaching round: it makes the proof obvious that the answer is `popcount(x)`. Use it to learn. Use the intrinsic to ship.

## Iterate over set bits

When a problem asks for "every set bit of `x`," the natural loop combines both identities:

```python
def set_bit_positions(x):
    while x:
        bit = x & -x        # value of the lowest set bit
        x &= x - 1          # strip it; the rest of the loop sees the next-lowest
        yield bit.bit_length() - 1   # convert value to position
```

For each iteration: isolate the lowest set bit (its value is a power of two), do whatever the problem wants with that position, then strip it. The loop runs `popcount(x)` times. This is the underlying machinery for bitmask iteration over a set's elements: enumerating subsets of a mask uses the same shape with one twist (`sub = (sub - 1) & mask`) to walk subsets in a fixed order rather than just the set bits of one mask. [Subset enumeration with bitmasks](../part-7-recursion-backtracking/02-subsets-combinations-permutations.md) makes that twist load-bearing.

Stdlib position-of-lowest-set-bit calls exist when you don't want to hand-convert value to position: Java `Integer.numberOfTrailingZeros(x)`, C++20 `std::countr_zero(x)`, Go `bits.TrailingZeros(x)`, Python `(x & -x).bit_length() - 1` (no direct intrinsic; bigint friendly). All four return a defined value when `x = 0`: 32 (Java), `w` (C++/Go for width-`w` types), undefined for the Python expression (returns `-1` because `(0).bit_length() == 0`). Range-check first.

## Operator precedence and language-shift gotchas

Bit operators have lower precedence than comparisons in C, C++, Java, and Python. `x & 1 == 0` parses as `x & (1 == 0)` = `x & 0` = `0`, which is falsy in every language. The condition is never true. Parenthesize: `(x & 1) == 0`. GCC's `-Wparentheses` was added specifically for this antipattern, and the warning fires on the same expression every interview season.

Three more cross-language traps for the cookbook reader.

> [!WARNING]
> **C++ signed left-shift into the sign bit is implementation-defined (C++14+) or undefined (C++11).** `1 << 31` on a signed 32-bit `int` is not portable.[^5] Reach for unsigned literals (`1u << 31`) and unsigned types (`uint32_t`, `uint64_t`) whenever the work is genuinely bit-level. The cookbook's C++ code uses `uint32_t` throughout for this reason.

> [!WARNING]
> **Shift amounts equal to or exceeding the operand's width diverge by language.** `1 << 32` is undefined behavior in C and C++. Java takes the shift amount modulo the operand width (so `1 << 32 == 1` for `int`, `1 << 64 == 1` for `long`). Go specifies the result is zero. Python has arbitrary precision and just produces `4294967296`. Code copied across languages silently changes meaning. Range-check the shift amount before issuing it whenever the value can come from input.

> [!WARNING]
> **Java has two right-shift operators; pick the right one.** `>>` is arithmetic (sign-extending) and `>>>` is logical (zero-fill). For bit-level work where the high bits matter, use `>>>`. The same expression with `>>` on a negative `int` returns garbage when extracting the sign bit. C++ and Go have only one `>>` per type, but the behavior is determined by signed-vs-unsigned: signed `>>` sign-extends, unsigned `>>` zero-fills. The portable reflex across all four languages is the same: do bit work in unsigned types when you have a choice.[^6]

The fifth trap is the off-by-one in same-width mask construction. For LC 1009 Complement of Base 10 Integer with `n = 5` (`0b101`), the same-width all-ones mask is `0b111 = 7`, not `0b1111 = 15`. The iterative builder is harder to get wrong than the closed form: `mask = 1; while mask < n: mask = (mask << 1) | 1`. After the loop `mask >= n` and `mask` is `0b1...1` with the same bit count as `n`. Then `complement = mask ^ n`.

## Practice

This chapter teaches reference primitives; the ladder pulls problems where the cookbook *is* the solution. The earlier popcount and Hamming-distance problems (LC 191, LC 461) live in the [bit manipulation primer](../part-0-foundations/03-bit-manipulation-primer.md) and don't repeat here.

### CORE

- [LC 338 — Counting Bits](https://leetcode.com/problems/counting-bits/) [Easy] • bit-dp-on-low-bit ★
- [LC 1009 — Complement of Base 10 Integer](https://leetcode.com/problems/complement-of-base-10-integer/) [Easy] • mask-construction *(reference: Python only)*
- [LC 201 — Bitwise AND of Numbers Range](https://leetcode.com/problems/bitwise-and-of-numbers-range/) [Medium] • common-prefix-via-shift *(reference: Python only)*

### STRETCH

- [LC 89 — Gray Code](https://leetcode.com/problems/gray-code/) [Medium] • gray-code-formula *(reference: Python only)*
- [LC 1521 — Find a Value of a Mysterious Function Closest to Target](https://leetcode.com/problems/find-a-value-of-a-mysterious-function-closest-to-target/) [Hard] • sliding-and-deduplication *(reference: Python only)*

LC 1521 is the rare canonical Hard for the per-bit-monotonicity argument: each AND-of-subarray-ending-here can only clear bits, never set them, so the set of distinct AND-values you carry forward has size at most `log2(max(arr)) + 1`. Pure cookbook reasoning at scale.

## Where this leads

[XOR patterns](./01-xor-patterns.md) takes the cancellation identity (`a ^ a = 0`) and builds the single-number family on top of it, using `x & -x` as the bit-isolator that splits two unique numbers into two groups. [Subset enumeration with bitmasks](../part-7-recursion-backtracking/02-subsets-combinations-permutations.md) iterates the set bits of a mask using the loop in this chapter's "Iterate over set bits" section. And [bitmask DP](../part-9-dynamic-programming/14-bitmask-dp.md) uses the same iteration shape for state transitions over `O(2^n)` subset states.

Outside Part 11, the cookbook's identities show up everywhere. Fenwick trees walk indices with `i += i & -i`. The JDK `HashMap` rounds capacity up to a power of two with `Integer.numberOfLeadingZeros` and the strip-lowest-bit identity. Binary search uses unsigned right shift to compute a midpoint without overflow: `lo + ((hi - lo) >>> 1)` in Java, the same logic everywhere else.

[XOR patterns](./01-xor-patterns.md) is next.

## References

[^1]: Stack Overflow, "cryptic comment in jdk source: // HD, Section 2-1", 2009, [stackoverflow.com/questions/1006626](https://stackoverflow.com/questions/1006626/cryptic-comment-in-jdk-source-hd-section-2-1).

[^2]: Anderson, S.E., "Bit Twiddling Hacks", Stanford Computer Graphics Laboratory, 1997-2005, [graphics.stanford.edu/~seander/bithacks.html](https://graphics.stanford.edu/~seander/bithacks.html).

[^3]: Knuth, D.E., *The Art of Computer Programming, Volume 4A: Combinatorial Algorithms, Part 1*, Addison-Wesley, 2011.

[^4]: Liu, N., "Algorithms behind Popcount," Nimrod's Coding Lab, 2022, [nimrod.blog/posts/algorithms-behind-popcount](https://nimrod.blog/posts/algorithms-behind-popcount/).

[^5]: Stack Overflow, "Why was 1 << 31 changed to be implementation-defined in C++14?", [stackoverflow.com/questions/26331035](https://stackoverflow.com/questions/26331035).

[^6]: The Go Authors, "The Go Programming Language Specification — Operators," [go.dev/ref/spec#Operators](https://go.dev/ref/spec#Operators).
