---
title: "Common pitfalls"
description: "The five highest-leverage failure modes at FAANG-tier loops: jumping to code, silent solving, missed clarifications, unstructured complexity answers, and the signal failures that look like skill failures."
slug: 05-common-pitfalls
part: 14
chapter: 5
difficulty: intermediate
prerequisites:
  - part-14-interview-framework/02-communicating
  - part-14-interview-framework/04-mock-interview-process
date_updated: 2026-05-25
languages: []
ladder:
  core: []
  stretch: []
---

# Common pitfalls

A 2025 analysis of roughly 100,000 technical interviews on interviewing.io found that for a third of all loops, dropping a single point on the Code or Solve scores raised the rejection rate by up to 6x. Communication, scored separately, looked statistically thinner. The naive reading is that you should grind LeetCode and let the talking sort itself out. Reality runs the other way: nearly every behavior people label "communication failure" actually corrupts the Code or Solve scores it sits underneath, because the interviewer cannot grade reasoning they did not hear.

That is the frame for this chapter. Most rejections at FAANG-tier loops are not skill failures. They are signal failures.[^1] The interviewer is producing a one-page rubric the calibration committee, hiring committee, or bar raiser will read in your absence; what you did not externalize during the hour is invisible on that page. Every pitfall below reduces to one rule: if you do not say it, it does not count.

## Why do prepared candidates still fail?

The candidate believes the interview is a test of skill. Solve the problem, get the offer. The interviewer is in fact running a one-hour proxy for "would this person be a safe collaborator on a 30-engineer team shipping a real feature next quarter," and your solution is one of seven inputs to that proxy. The other six: did you ask the questions a senior would ask, did you propose a plan before coding, did you react to the hint constructively, did you explain your decisions out loud, did you handle being wrong, did you ask the kind of questions at the end that signal you care about the team. None of those six are "did the code compile."

The calibration step amplifies this. A candidate who fixed an off-by-one bug after a hint gets one of two written notes: "iterated cleanly on hint, demonstrated good debugging instinct" (Hire), or "had to be hint-fed, did not initially see the boundary case" (Lean No Hire). The bug fix is identical in both cases. The behavior around it is the entire signal.

## What's the most common silent failure?

Going quiet. Formation.dev's interview-prep team calls it "test mode": the candidate hears the prompt, works internally for eight to twelve minutes, surfaces a fully-formed solution at the end. The code is correct. The decision is no-advance, because the interviewer has no read on reasoning, no opening to redirect, no signal on how the candidate handles uncertainty.

Two cousins of test-mode show up everywhere. First, jumping straight to code without a plan. Ian Douglas, who has run 600+ technical interviews on interviewing.io, calls this the number-one problem area he sees: candidate hears the prompt, talks for thirty seconds, starts typing, and by minute eight is refactoring a confused fifty-line draft.[^4] The fix is cheap. State the problem in your own words for thirty seconds. Walk one example by hand for sixty. Write down the approach name and its data structures for sixty. Then code. Two minutes of plan saves twenty of recovery.

Second, half-thoughts. "I wonder if I could... no, never mind, I'll just do this instead." The candidate finishes the thought silently and changes the code. The interviewer hears the start, the trail-off, and a different keystroke. Reasoning that good produced a 2 on Communicate because it never reached the room. Convert the trail-off into a sentence: *"I considered binary search, but the array isn't sorted and sorting is O(n log n) which already dominates, so I'll stay linear."* That is five extra seconds of speech and a full point on the rubric.

The unifying corrective move is narration of decisions, not internal doubt. Three lines per decision: what you are choosing, why over the alternative, what it costs. Then code.

## When does over-engineering kill you?

At senior loops, more often than under-engineering does. Stefan Mai, HelloInterview co-founder who has run 1,000+ interviews, describes the canonical down-level pattern in 2025: a senior candidate brings Elasticsearch to a problem a Postgres index would solve, then cannot answer follow-ups about Elasticsearch internals. The interviewer's note: "name-dropping technologies they cannot defend." Offer arrives one level lower than the candidate targeted.[^2]

Mai's rule is short. More moving parts means more mistakes, and senior engineers have seen every way that cleverness becomes a maintenance nightmare over time. Start with the simplest design that satisfies the functional requirements. Add complexity only when the interviewer asks "what if it's 10x bigger" or you yourself can name the bottleneck.

The algorithmic version of the same pitfall is premature optimization without measurement. Candidate jumps from "I could brute-force this in O(n²)" to "but let me build the O(n log n) with a segment tree" without writing the brute force. At minute thirty-five the segment tree is half-done and broken. The senior expectation is brute-force first, optimize second, with the conversation in between. Skipping the floor case to chase the ceiling costs you both.

The diagnostic question, asked aloud, is enough: *"do you want me to code the brute force first or jump to the optimized version?"* The interviewer almost always says "jump to the optimized," but asking is worth a Communicate point and a sanity check on the framing.

## How do I recover from a wrong direction?

The graceful pivot is the most undervalued skill in the loop, and the failure mode it prevents is the most lethal. Quitting. One Workplace Stack Exchange writeup from November 2024 describes a candidate who stopped an interview at the forty-minute mark because the problems involved tech they had not used in years. There is no hour in interviewing where stop is the right move.

Three moves, in order, when you realize the approach is wrong.

**Acknowledge out loud.** *"I've been trying X for the last few minutes and it's running into Y. Let me back up."* That sentence, spoken at minute twenty-five, scores higher on Solve than another five minutes of head-down debugging. The interviewer does not score "never wrong." They score "noticed when wrong, reacted constructively."

**Propose the floor.** *"Let me describe the brute force, code that as a working baseline, and we can discuss what would make it faster."* Even a brute force coded in the last fifteen minutes plus a clean complexity discussion is often a Hire. A half-finished clever solution with no working baseline is almost never one.

**Treat the interviewer's hint as a soft signal that something is wrong.** Do not argue. A November 2024 Meta full-loop reject, posted on LeetCode Discuss, captured the inverse beautifully: the candidate solved Top K Frequent Elements in O(N log K), the interviewer (unfamiliar with Python's `heapq`) asserted that heap ops were O(1), and the candidate clarified the bound and accepted the alternative without arguing. That is the right move even when you are correct, because the calibration step will read the interviewer's note, not your conviction. The Forbes 2026 piece quoting a Google exec names the inverse explicitly: "always needing to be right, being closed-minded, that's a red flag." Try the hint for a minute. If it does not work, say *"I tried X but it ran into Y, can we revisit?"* That is collaborative. *"I don't think that's right"* is not.

## What changed with AI in 2026?

A 2026 audit of 19,368 technical interviews flagged 38.5% of candidates for AI-assisted cheating. Technical roles hit 48%. Sixty-one percent of detected cheaters scored above the passing threshold without the detection layer.[^3] The defensive response from companies has been to weight signal more heavily relative to artifact. Karat's 2026 detection guide catalogs six tells, of which the deadliest is "explanations that don't match the code": the candidate, asked to walk through their own solution, describes a different algorithm or contradicts themselves on follow-up questions.[^5]

Even setting aside the policy question, every detection signal is also a competence signal. A candidate who cannot defend code they typed is unhirable for the same reason an AI-using candidate is. The interviewer's job has shifted from grading whether the code is correct to grading how you reason about code, including AI-generated code.

The corrective move splits by company. For shops that prohibit AI in screens, do not use it. For 2026-era loops that explicitly permit it (Canva, Anthropic, Meta's AI-assisted coding round), use it visibly: prompt, validate, iterate. The thing being graded is judgment around the code, not typing speed.

## What three habits should I drill before the next loop?

Pick the three that map to your weakest pitfall above and rehearse them in mock interviews until they are involuntary.

First, the twenty-second opener that flips the round from quiz to collaboration. Douglas's exact script works: *"my typical process is to spend a minute or two thinking quietly and writing down notes, then share them with you for input. While I code I tend to work quietly, but I'll pause to share my thought process. Sound good?"*[^4] That single sentence repositions you as a collaborator, locks in permission for thinking time, and prepays the trust budget for any silence later.

Second, the ninety-second dry-run. After the code compiles in your head, narrate one concrete input through it line by line, state outputs at each step, then explicitly try the empty input and one boundary case. Most candidates treat this as overtime; the senior interviewer treats its absence as evidence you ship untested code.

Third, the closing question. *"Do you have any questions for me?"* answered with "no, I think you covered it" reads as low curiosity on a senior loop. Prepare three: one team-specific (the on-call rotation, the largest piece of open tech debt), one role-specific (what would a strong six-month ramp look like), one interviewer-specific (what brought them to this team). The point is not to interview the interviewer. The point is to leave them with one more data point that you would care about the work.

The single sentence to make sticky, from the signal-failure frame at the top: the interviewer cannot read your mind. If you do not say it, it does not count. Every pitfall in this chapter reduces to a violation of that rule, and every fix reduces to externalizing one more piece of reasoning the interviewer would otherwise have had to guess.

## References

[^1]: Korolev, D., "Does communication matter in technical interviewing? We looked at 100K interviews to find out," interviewing.io blog, November 2025. <https://interviewing.io/blog/does-communication-matter-in-technical-interviewing-we-looked-at-100k-interviews-to-find-out>.

[^2]: Mai, S., "Over-engineering is getting you down-levelled," HelloInterview blog, January 2025. <https://www.hellointerview.com/blog/over-engineering-is-getting-you-down-levelled>.

[^3]: Pan, T., "The AI Interview Collapse: Engineering Hiring Has Lost Its Signal," tianpan.co, April 2026. <https://tianpan.co/blog/2026-04-23-ai-interview-collapse-engineering-hiring-signal>.

[^4]: Douglas, I., "I've conducted over 600 technical interviews on interviewing.io. Here are 5 common problem areas I've seen," interviewing.io blog, May 2023. <https://www.interviewing.io/blog/ive-conducted-over-600-technical-interviews-on-interviewing-io-here-are-5-common-problem-areas-ive-seen>.

[^5]: Hanrahan, G., "How to Detect AI Use in Technical Interviews: A Practical Guide for Training Interviewers," karat.com blog, March 2026. <https://karat.com/detect-ai-use-technical-interviews/>.
