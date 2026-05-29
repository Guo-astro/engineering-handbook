---
title: "The first five minutes: clarifying questions"
description: "What to ask in the first five minutes. The questions interviewers grade you on, the prompts that signal seniority, and the failure mode that costs the most candidates the round."
slug: 01-clarifying-questions
part: 14
chapter: 1
difficulty: intermediate
prerequisites:
  - part-14-interview-framework/00-pattern-recognition
date_updated: 2026-05-25
---

# The first five minutes: clarifying questions

The interviewer reads the prompt. *"Reverse a string."* Three words. The screen-share goes quiet. You have two seconds before the silence starts to feel like the wrong answer, and the most common thing candidates do at that moment is the one move that costs them the round: they start coding.

Across 600 logged technical interviews on interviewing.io's platform (2023), Ian Douglas listed "not asking clarifying questions" as one of the five most common candidate failure modes.[^1] Codeintuition's 45-minute Google-round decomposition (2026) puts a number on the same observation from the other direction: 3 to 5 of the 45 minutes go to clarification, and what registers as positive signal is **constraint questions**, not "what does this mean?" questions.[^2] The first kind tightens the spec. The second tells the interviewer you didn't read carefully.

This chapter is what to ask, in what order, and when to stop.

## What do I ask first?

Restate the prompt in your own words before you ask anything. Thirty seconds, no more. Pick one concrete piece from what the interviewer just said and put it back at them: *"So we have an array of integers, and we want the indices of two elements that sum to the target. The output is a pair of indices, not the values themselves. Right?"* This single move catches misreads early, gives the interviewer permission to redirect, and converts "I'm thinking" silence into a contract negotiation.

Then ask in this order. Input shape, output contract, constraints, edge cases. Most prompts have gaps in the first two and the rest fall out from there.

**Input shape.** Type, range, signedness, mutability, sortedness. *"Is it an array, a stream, or a generator?"* A stream input forces a single-pass algorithm. *"Can the values be negative?"* Negative numbers break the sliding-window monotonicity that the textbook two-pointer solution depends on. *"Can I modify the input in place?"* That's O(1) extra space versus O(n).

**Output contract.** Return type, ordering, missing-value behavior. *"If no answer exists, what do I return: `null`, `-1`, throw?"* LeetCode 1's contract is `-1`; production code reaches for `Optional`. Same problem, different signature, and the wrong assumption fails the hidden test case.

**Constraints.** The size of `n`, the time and space target. *"`n` up to 10^5 or 10^9?"* The answer picks the algorithm class. 10^9 rules out anything quadratic before you've written a line.

**Edge cases.** Empty input, single element, all-identical, boundary values. The candidate Codeintuition flagged as strong (2026) caught the empty-grid case proactively on a Number-of-Islands prompt.[^2] The candidate next to them did not, which is why one of them moved to the next round.

Each of these is a question whose **answer changes the code**. That's the test. If the answer doesn't change the code, the question doesn't earn its place.

## Which questions actually matter?

Take a real example. *"Given an array of integers, find two numbers that sum to a target."* That's [LC 1 — Two Sum](https://leetcode.com/problems/two-sum/), phrased ambiguously. Ian Douglas uses a near-identical warm-up specifically because most candidates hear "array" without checking; the prompt he uses says "grouping," and he's watching whether they ask.[^1]

Five questions are worth asking. *"Is the array sorted?"* Sorted unlocks a two-pointer solution in O(1) extra space; unsorted forces a hash map. *"Can the same index be used twice?"* That affects the loop's inner check. *"Are there duplicates?"* Duplicates change the return contract when two valid pairs exist. *"What do I return on no match?"* The answer picks the function signature. *"Negatives allowed?"* That eliminates the can't-go-below-zero argument before it bites.

Five questions, ninety seconds, and you've pinned the problem down to one algorithm. That's what the interviewer is grading.

The contrast: a candidate who asks *"is the array zero-indexed?"* or *"should I name the loop variable `i`?"* is checking boxes, not narrowing the spec. The substack walkthrough of a 45-minute FAANG round (Rafay Abbasi, 2026) names this directly: *"Asking questions whose answers don't change your code"* is a documented failure pattern.[^3]

## What's the budget?

Three to five minutes. Not five exactly. The upper bound, not the target.

| Sub-phase | Time | What happens |
|---|---|---|
| Restate the prompt | ~30 sec | Paraphrase in your own words; surface misreads |
| Input shape | ~60 to 90 sec | Type, range, mutability |
| Output contract | ~30 to 60 sec | Return type, ordering, missing-value |
| Constraints | ~30 to 60 sec | `n`, time/space target |
| Edge cases | ~30 to 60 sec | Empty, single, ties |
| Validate the approach | ~30 sec | Restate the chosen direction; let the interviewer redirect |

That tops out at about four minutes for a fresh medium prompt.[^2][^3] Cracking the Coding Interview's "Listen / Debug example / Special cases" sequence (McDowell, 6th ed., 2015) front-loads the same three steps into the same window.[^4] AlgoCademy's published guidance also lands in the 2-to-5-minute range.[^5]

What does *not* fit in the budget: designing the algorithm, walking through trade-offs between two solutions, or asking process meta-questions like "how detailed should I be?" Those come later. A 15-second exchange to set communication expectations ("I'll think for about a minute, then share my approach, then code") is fine; a multi-minute conversation about how you work is not.

On a true warm-up easy ([LC 344 — Reverse String](https://leetcode.com/problems/reverse-string/)), the budget compresses to 60 to 90 seconds total. Spending four minutes clarifying *"reverse a string"* is the same failure mode as not clarifying at all.

## When does over-clarifying become the failure?

Six to eight minutes in, asking question number twelve. The interviewer reads it as stalling.

Mid-level candidates absorb "ask clarifying questions" as a quantity goal. They run down a checklist (input, output, constraints, edges, distribution, environment) without asking whether any given answer would change a line of code. The substack writeup quotes interviewer notes verbatim: *"Treating clarification as a checkbox. The point isn't to ask questions, it's to narrow the problem. Every question should eliminate a possible interpretation."*[^3]

Three other moves cost candidates the round in this same phase.

**Asking and then ignoring the answer.** You ask if `k` is always valid. The interviewer says yes. Then you write `if (k <= 0) return [];` defensively, and now the interviewer thinks you weren't listening or don't trust the contract you just negotiated. Drop the guard.[^3]

**Asking for the solution disguised as a question.** *"Should I use a hash map or sort first?"* reads as fishing. State the choice with a reason and ask for confirmation: *"I'm going hash map for O(n) lookup, trading O(n) space. Sound reasonable?"* Same answer, different signal.[^5]

**Vague restate that masks misreading.** *"So we want the most common things"* tells the interviewer nothing about whether you understood, and you're about to code a slightly wrong problem. Restate with concrete pieces from the prompt: input type, output type, the constraint that disambiguates.

The fix for all three is the same. Treat clarification as **contract negotiation between two engineers**, not a quiz the interviewer is giving you.

## When should I ask less?

Three cases compress the budget.

**The prompt arrives with a written spec.** Two examples, explicit constraints (`1 <= n <= 10^5`), value range. The questions left are tiebreaks and one or two edge cases. Don't invent gaps that were already filled.

**The mid-interview follow-up.** *"Now what if the grid wraps around?"* The universe is established. One or two delta-clarifications, then code.

**The warm-up easy.** Reverse a string. Valid parentheses. The interviewer is measuring whether you can move quickly. Sixty to ninety seconds total: type, in-place vs return new, ASCII vs Unicode, done.

Outside these three, the full clarification phase runs every time. The chapter's title says *five minutes* because that's the upper bound the eight surveyed sources converge on; the floor is closer to two.

## What to do this week

Pull two prompts from your queue, one easy and one medium, and run the clarification phase out loud, on a timer, before solving. Three minutes for the medium, ninety seconds for the easy. Record yourself. Listen back for the questions whose answers wouldn't have changed the code, and cross them off next time.

Two illustrative problems to think about, not solve as part of this chapter:

- [LC 1 — Two Sum](https://leetcode.com/problems/two-sum/) [Easy]. The surface ambiguity (sortedness, return-format, missing-answer behavior) is the cleanest substrate for practicing the input-shape arc.
- [LC 146 — LRU Cache](https://leetcode.com/problems/lru-cache/) [Medium]. The prompt is *"design and implement"*, which forces the API contract into the open. `get` returns what on a miss? Is the cache thread-safe? What's the complexity target, O(1) worst case or amortized? The answers pick the data structure.

Both are CORE in their algorithmic chapters; this chapter only references them. The clarification skill itself is built by drilling it on whatever you're already practicing.

[Pattern recognition: the fastest skill to develop](./00-pattern-recognition.md) is upstream of this chapter. Once the input shape is pinned, pattern recognition fires on the input-output signature and tells you which algorithm to reach for. Communication during the rest of the round is the chapter that follows.

## References

[^1]: Douglas, I., "I've conducted over 600 technical interviews on interviewing.io. Here are 5 common problem areas I've seen," interviewing.io blog, 1 May 2023, [interviewing.io/blog/ive-conducted-over-600-technical-interviews-on-interviewing-io-here-are-5-common-problem-areas-ive-seen](https://www.interviewing.io/blog/ive-conducted-over-600-technical-interviews-on-interviewing-io-here-are-5-common-problem-areas-ive-seen).

[^2]: Codeintuition, "Google Coding Interview Experience: 45 Minutes Decoded," accessed 21 March 2026, [codeintuition.io/blogs/google-coding-interview-experience](https://www.codeintuition.io/blogs/google-coding-interview-experience).

[^3]: Abbasi, R., "The Anatomy of a Perfect FAANG Coding Interview (A 45-Minute Breakdown)," DG Learning Substack, 13 April 2026, [dglearning.substack.com/p/the-anatomy-of-a-perfect-faang-coding](https://dglearning.substack.com/p/the-anatomy-of-a-perfect-faang-coding).

[^4]: McDowell, G.L., *Cracking the Coding Interview: 189 Programming Questions and Solutions*, 6th ed., CareerCup, 2015, ISBN 978-0-9847828-5-7.

[^5]: AlgoCademy, "Should You Ask Clarifying Questions Before Coding in Interviews?" AlgoCademy Blog, accessed 20 May 2026, [algocademy.com/blog/should-you-ask-clarifying-questions-before-coding-in-interviews](https://algocademy.com/blog/should-you-ask-clarifying-questions-before-coding-in-interviews/).
