---
title: "Complexity discussions"
description: "How to answer 'what's the time complexity?' in one sentence: derive vs memorize, time alongside space, the right qualifier (worst/average/amortized), all four signals at once."
slug: 03-complexity-discussions
part: 14
chapter: 3
difficulty: intermediate
prerequisites:
  - part-0-foundations/01-complexity-big-o
  - part-14-interview-framework/02-communicating
date_updated: 2026-05-25
languages: [python]
ladder:
  core: []
  stretch: []
---

# Complexity discussions

Minute 34 of a 45-minute coding round. Your code compiles, the test cases pass, the interviewer leans back and asks: "what's the time complexity?" Thirty seconds of silence start now. Those thirty seconds are the unit this page is built around.

You already know the bound by the time the question lands. The tape stuck in your head is "O(n)" or "O(n log n)" or whatever it is; the problem is that "O(n)" said alone is not the answer. Interviewers are listening for four things at once and rate the response on whether the candidate hit all four in one sentence: did you derive it or memorize it, did you state it tightly, did you name space alongside time, and did you give the right qualifier (worst case, expected, amortized, or average).[^1] [Computational complexity and Big-O](../part-0-foundations/01-complexity-big-o.md) is the machinery; what follows is the phrasebook that sits on top of it.

## When do I state complexity?

Twice. State it once when you've described the approach but before you start typing ("I'll use a hash map, so it's O(n) expected time and O(n) space"), and once when the code compiles, in the form the interviewer will ask for. The pre-coding statement protects you against the worst outcome: writing a solution whose bound the interviewer would have rejected if you'd said it out loud first. After the code runs, the second statement is the one your loop debrief actually quotes.[^2]

Volunteering the bound twice has another effect. It marks you as someone who reads complexity off their own code rather than off a memory of similar problems. Interviewers consistently rank "it's O(n²) because of the nested loops over the same array" higher than a confident-sounding "I think it's O(n log n)" with no justification, because the first one is reasoning the interviewer can correct and the second one is a guess.[^1]

## What does the answer sound like?

Three sentences. Time bound, space bound, where each comes from. Fill this template:

> [Time bound] time, [Space bound] space. The time comes from [the dominant loop or recursion]. The space comes from [the auxiliary structure or recursion depth].

A worked fill on Two Sum, the brute-force-then-hash-map refactor most readers have seen:

```python
def two_sum_quadratic(nums, target):
    n = len(nums)
    for i in range(n):
        for j in range(i + 1, n):
            if nums[i] + nums[j] == target:
                return [i, j]
    return []

def two_sum_linear(nums, target):
    seen = {}  # value -> first index
    for i, x in enumerate(nums):
        if target - x in seen:
            return [seen[target - x], i]
        seen[x] = i
    return []
```

The discussion you say out loud, in order:

> "The brute force is O(n²) time, O(1) extra space. The two nested loops give the n²; the indices are constant. I can do better by carrying a hash map of value to index: O(n) expected time, O(n) space. We trade space to drop a factor of n in time, which is the right trade at any realistic n. Problems with n ≤ 10⁵ time out on O(n²), and an n-entry hash table is rarely a problem at that scale."

That is the unit. Roughly twenty-five seconds spoken, names time, names space, names the trade, and ends. The interviewer either accepts it or asks one of two predictable follow-ups, both covered below.

## What if there are two parameters?

Then the bound has two letters. A BFS on a graph with V vertices and E edges is O(V + E), not O(n); merging k sorted lists of total length n is O(n log k), not O(n log n). The mistake to avoid is the sloppy O(n) that hides the second parameter under "n is the input size." When the interviewer asks "what's n?" you've now spent ten seconds re-deriving a bound you already had.

State which letter is which the first time. "V is the vertex count, E is the edge count, the BFS visits each vertex once and each edge twice, so it's O(V + E) time and O(V) space for the visited set and queue." If the problem text gave you two array lengths, name them: O(n + m), where n is the length of nums1 and m the length of nums2. Reusing n for both is a bug the interviewer cannot tell from a misunderstanding.

## Expected, amortized, average — which word?

Three words, three arguments, no overlap. Many candidates use them interchangeably and lose calibration ticks each time.[^1]

**Expected** is for hashing. Hash-map insert and lookup are O(1) *expected* under simple uniform hashing, with worst case O(n) per operation when an adversary or pathological input forces all keys into one bucket.[^3] Java since version 8 mitigates the worst case to O(log n) per lookup by converting a bucket to a red-black tree once it hits eight entries, but only when the keys implement Comparable; otherwise the worst case stays O(n).[^4] Saying "O(1)" without "expected" invites the follow-up "and the worst case?" which you'd rather have already answered.

**Amortized** is for capacity-doubling structures. Python `list.append`, Java `ArrayList.add`, C++ `vector::push_back`, Go `append`. Most calls are O(1); on resize, the call is O(n) because every element gets copied to a fresh, double-sized array. Across n calls, the total resize work is `1 + 2 + 4 + ... + n = 2n − 1`, which divides out to O(1) per call on average over the operation sequence.[^5] This is *amortized*, not average; the argument is over an arbitrary worst-case sequence on the same structure, not over random inputs.[^6] In a latency-sensitive system the amortized bound stops helping, because individual calls can still spike to O(n) and the spike is what the user feels.[^5]

**Average** (or **expected** again, depending on whose textbook you read) is for randomized algorithms. Quicksort's expected runtime is O(n log n) with a random pivot or median-of-three; the worst case is O(n²) on a sorted input with last-element pivot. The expectation is over the algorithm's coin flips, not over random inputs. Randomization keeps the bound robust to adversarial data.[^3] Hash-map *expected* O(1) and quicksort *expected* O(n log n) are the same kind of expectation, taken over the algorithm's randomness.

The verbal rule: *expected* for hashing, *amortized* for capacity-doubling, *average* or *expected* for randomized algorithms. Three words, three pairings, picked automatically once you have them mapped.

## How do I respond to "can you do better?"

This question is rarely about a tighter bound; it's a check on whether you know there is one. Three honest responses cover most cases.

If the comparison-sort lower bound is in play and your bound matches it, say so: "Not for general comparison input; n log n is the comparison-sort lower bound. We could drop it with counting or radix sort if the keys are bounded integers, but the constants make the trade worth it only at large n."[^3] Naming the lower bound moves the conversation from "find a faster algorithm" to "relax the input model," which is the productive next step.

If you traded time for space and the interviewer is hunting for the symmetric trade, give the cost: "I can drop space to O(1) by [in-place modification / two pointers / the three-reverse trick on rotation], but that mutates the input — is that acceptable?" Asking before mutating saves you from a wrong assumption that's hard to walk back.

If you genuinely don't know whether you can do better, say so plainly: "I don't see a tighter bound; do you have one in mind?" An honest "I don't know, what am I missing?" reads better than five seconds of stalling.

## Pitfalls

> [!WARNING]
> **Stating time without space.** The number-one calibration tick lost in complexity discussions is the candidate who says "O(n)" and waits for the follow-up "and space?" before naming auxiliary memory.[^1] Internalize "time AND space" as one phrase. Auxiliary space includes hash maps, result arrays, the recursion stack, and any temporary structures the algorithm allocates; it does not include the input itself.

> [!WARNING]
> **Confusing best, average, and worst case.** If the algorithm has different bounds for different cases (quicksort, hash map, BST, Bloom filter), say both proactively: "quicksort is O(n log n) expected, O(n²) worst case." Letting the interviewer ask "and the worst case?" is a forfeited signal that you knew the asymmetry was there.

> [!WARNING]
> **Hidden library calls inside loops.** A tight loop with `if substring in s:` is not O(n); the substring scan is itself O(n), so the total is O(n·m). Same trap with `list.remove(x)` (O(n)), `x in list` (O(n)), and slicing (copies, O(k)). For every method call, ask what the library does before you put a Big-O label on the loop that contains it.

> [!WARNING]
> **Counting recursion as free.** A recursive in-place quicksort is O(log n) auxiliary space on average, not O(1). The recursion stack is real memory: each frame holds parameters and a return address. Iterative rewrites are the same Big-O space (the explicit stack replaces the call stack); the win from going iterative is dodging Python's 1,000-frame default or Java's ~10⁴-frame ceiling, not asymptotic space.

## Where this leads

That is the whole script. Drilling the answer-shape is what [The mock interview process](./04-mock-interview-process.md) covers. The neighboring chapter [Communicating during the interview](./02-communicating.md) frames complexity discussion as one slice of the broader "what to say out loud" problem, and [Common interview pitfalls](./05-common-pitfalls.md) collects the high-frequency mistakes across all four interview surfaces.

## References

[^1]: codeintuition.io, "How to Analyze Your Code's Complexity in an Interview" (retrieved 2026-05-19), <https://www.codeintuition.io/blogs/time-and-space-complexity-interview>.

[^2]: Lerner, A. and Holtz, D., "We analyzed thousands of technical interviews on everything from language to code style. Here's what we found," interviewing.io blog (post date circa 2016-2019, retrieved 2026-05-20), <https://interviewing.io/blog/we-analyzed-thousands-of-technical-interviews-on-everything-from-language-to-code-style-here-s-what-we-found>.

[^3]: Cormen, T.H., Leiserson, C.E., Rivest, R.L., Stein, C., *Introduction to Algorithms*, 4th ed., MIT Press, 2022, ISBN 978-0-262-04630-5.

[^4]: Stack Overflow, "The worst case time complexity for HashMap after Java 8 is still O(n) not O(log n)?" (April 2024), <https://stackoverflow.com/questions/78295005/>.

[^5]: Tarjan, R.E., "Amortized Computational Complexity," *SIAM Journal on Algebraic and Discrete Methods*, Vol. 6, No. 2, April 1985, pp.

[^6]: *Amortized analysis*, Wikipedia (retrieved 2026-05-19), <https://en.wikipedia.org/wiki/Amortized_analysis>.
