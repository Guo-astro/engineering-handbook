---
title: "Per-company tracks: index and how to use"
description: "When to open a per-company track, how to layer it on Parts 0-13, and the three signals that tell you it's time to move from pattern practice to company-specific calibration."
slug: 11-per-company-tracks-index
part: 14
chapter: 11
difficulty: intermediate
prerequisites:
  - part-14-interview-framework/00-pattern-recognition
  - part-14-interview-framework/04-mock-interview-process
  - part-14-interview-framework/05-common-pitfalls
date_updated: 2026-05-25
---

# Per-company tracks: index and how to use

The per-company tracks are layered on top of the core handbook, not a substitute for it. Without the pattern-recognition skill from Parts 0 through 13 and [Pattern recognition](./00-pattern-recognition.md), a per-company track is a list of LeetCode problems with company tags glued onto them, and that is exactly the prep substrate the 2024 to 2026 evidence shows produces brittle outcomes.

Three signals tell you it's time to open a track. A recruiter call is on the calendar. Your loop is within twelve weeks. Or you have competing offers and need to calibrate. Without one of those, every hour spent on a track is an hour not spent on a pattern you haven't yet seen, and the marginal hour is better spent in the core book.

When the signal fires, the question becomes which track. The six below pin a one-line framing to each company, the bottleneck axis the track is built around, and the deeper sub-chapters where the actual drilling lives.

## Amazon

Behavioral overlay is the highest in the FAANG ladder. Coding rounds at the onsite always include one to two Leadership Principle questions, and Bar Raisers say strong behavioral can save weak coding while strong coding cannot save weak behavioral.[^1] The track front-loads LP narration before any LeetCode work. AI tools are prohibited in 2025 and 2026 loops.[^1]

Drill into the [Amazon Leadership Principles brief](./06-amazon-lps-brief.md) and [Narrating LPs during a DSA round](./07-amazon-lps-narration.md).

## Meta

The single biggest format change in big-tech DSA interviews since remote: one coding round (rolling toward all of them through 2026) is AI-assisted, with CoderPad's built-in assistant offering GPT-5, Claude Sonnet 4.5, Gemini 2.5 Pro, and Llama 4 Maverick.[^2] Pace is the other bottleneck. Phone screen is two questions in 35 minutes. DP is banned per Meta's internal interviewer guidance.

The [Meta AI-assisted round](./08-meta-ai-round-format.md) covers prompt patterns, the model menu, and the two-questions-in-35-minutes phone-screen rhythm.

## Google

Coding is weighted higher than system design, the only FAANG where that holds.[^3] DP is fully in scope, the FAANG most likely to ask it (Yangshun: "if joining Google is your dream, DP is unavoidable"). Expect red-herring framing and follow-ups that retract earlier assumptions. The Googleyness round assesses cultural fit on attributes that are commonly reported, not officially published.[^4]

Per-company track planned: `content/dsa/per-company/google.md`.

## Apple

The highest team-by-team variance in the FAANG ladder.[^5] One team asks classic LC mediums; another runs a take-home plus live-debug onsite; a third does a daylong deep-dive on Java concurrency or Swift internals. "Why Apple?" is do-or-die in the behavioral round, and multiple interviewers reject solely on a weak answer to it. Don't open the Apple track without a specific team in mind.

Per-company track planned: `content/dsa/per-company/apple.md`.

## Microsoft

The most "classic CS fundamentals" loop of the six. Top tagged questions skew Easy-to-Medium and feature parsing, IP validation, integer-to-words, and linked-list manipulation.[^6] DP rare but creeping in (coin change, edit distance level). One round is domain-specific and tests depth on the team's stack: cloud networking, big data, distributed storage. The "As Appropriate" interviewer makes the final hire/no-hire call.

Per-company track planned: `content/dsa/per-company/microsoft.md`.

## Netflix

Netflix is to system design as Google is to coding.[^7] Coding carries the least weight of any FAANG; design and behavioral carry the most. Loops run roughly eight interviews, often split across two days, with one or two directors on the panel. The director-led "Dream Team" behavioral round can independently fail a candidate. Netflix only hires senior, the bar is design plus behavioral, and the volume is small.

Per-company track planned: `content/dsa/per-company/netflix.md`.

> [!WARNING]
> **Two cells in the comparison drift fast.** Meta's AI-round format is the freshest signal in the book (October 2025 rollout, expanding through 2026); date-check it against [interviewing.io's blog](https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples) before your loop. The krishnadey30 LeetCode-CompanyWise tags many readers reach for were last meaningfully refreshed in 2022 to 2023; treat them as relative weighting, never absolute frequency.[^8]

## What to do this week

If you have one of the three signals, open the matching track and use it as the spine of the next four to twelve weeks of prep. Otherwise, close this page and finish the part of the core book you skipped to get here. The tracks earn their keep on the calibration phase. They do not replace the core.

[Common pitfalls](./05-common-pitfalls.md) is the cross-cutting failures sheet. [Mock interview process](./04-mock-interview-process.md) is how you simulate any of the six bottleneck axes above. The next 6 to 12 weeks of prep are the part that decides the loop.

## References

[^1]: interviewing.io, "Amazon interview process and questions," refreshed Q4 2025, [interviewing.io/guides/hiring-process/amazon](https://interviewing.io/guides/hiring-process/amazon).

[^2]: interviewing.io blog, "How to Use AI in Meta's AI-Assisted Coding Interview, with Real Prompts and Examples," published 2025, [interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples](https://interviewing.io/blog/how-to-use-ai-in-meta-s-ai-assisted-coding-interview-with-real-prompts-and-examples).

[^3]: interviewing.io, "Google interview process and questions," refreshed 2026, [interviewing.io/guides/hiring-process/google](https://interviewing.io/guides/hiring-process/google).

[^4]: Hello Interview, "Google L5 (Senior) Software Engineer Interview Guide," 2025, [hellointerview.com/guides/google/l5](https://www.hellointerview.com/guides/google/l5).

[^5]: interviewing.io, "Apple interview process and questions," [interviewing.io/guides/hiring-process/apple](https://interviewing.io/guides/hiring-process/apple).

[^6]: interviewing.io, "Microsoft interview process and questions," [interviewing.io/guides/hiring-process/microsoft](https://interviewing.io/guides/hiring-process/microsoft).

[^7]: interviewing.io, "A Senior Engineer's Guide to Netflix's Interview Process and Questions," by Kevin Landucci, fetched 20 May 2026, [interviewing.io/netflix-interview-questions](https://interviewing.io/netflix-interview-questions).

[^8]: krishnadey30, "LeetCode-Questions-CompanyWise" GitHub repository, [github.com/krishnadey30/LeetCode-Questions-CompanyWise](https://github.com/krishnadey30/LeetCode-Questions-CompanyWise).
