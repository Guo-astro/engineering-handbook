---
title: "Amazon Leadership Principles narration"
description: "STAR-format micro-narrations for the technical rounds, plus the eight to twelve full stories the behavioral and Bar Raiser rounds expect candidates to walk in carrying."
slug: 07-amazon-lps-narration
part: 14
chapter: 7
difficulty: intermediate
prerequisites:
  - part-14-interview-framework/06-amazon-lps-brief
date_updated: 2026-05-25
---

# Amazon Leadership Principles narration

Amazon is the only top-tier company where you cannot pass the loop on algorithm fluency alone. Every round, including the two coding rounds, scores the Leadership Principles in the same notes the technical signal goes into. Coding-strong, behaviorally-silent candidates report the same outcome from debriefs: both problems solved, every clarification answered with a one-liner, no-hire on insufficient signal. The fix is small in surface area. About a dozen rehearsed micro-narrations for the coding rounds, and eight to twelve full stories for the behavioral and Bar Raiser rounds.

For the principles themselves (the canonical 16, the 14-to-16 transition, which five surface most heavily in coding), read [Amazon Leadership Principles primer](./06-amazon-lps-brief.md) first. The page below assumes you already know what they say.

## How long should each story be?

Roughly four minutes spoken. Amazon's own published interview guide tells candidates to use STAR and to be specific about their personal contribution; the industry-standard pacing inside one STAR answer is one minute on Situation, one on Task, ninety seconds on Action, and thirty to sixty seconds on Result.[^1][^2] Bar Raisers will interrupt a story that runs past five minutes. They will probe a story that comes in under two.

Time the four sections deliberately. A story that opens "the project was a six-month migration of our payments stack from Postgres to Spanner..." has burned ninety seconds on Situation and now you have two minutes left for everything that mattered. Lead the Situation with one sentence and one number. *"Q3 2024, our checkout service was dropping 0.3% of carts under load. I owned the fix."* Now the interviewer can focus.

## What does STAR mean and is it required?

STAR is **Situation, Task, Action, Result.** The acronym was popularized by Development Dimensions International (DDI) in the 1970s as part of their *Targeted Selection* methodology, and it shares a common root with Tom Janz's academic Behavior Description Interviewing (1986)[^3] in John Flanagan's Critical Incident Technique (1954).[^4] You don't need the history. You need the structure, because Amazon's interview guide names STAR explicitly and says responses without it tend to omit the actor and the outcome.[^2]

It is not a script you recite. The interviewer is not grading "did the candidate name each letter." They are grading: did you tell me the *specific* situation (not a category of situations), what *you personally* were responsible for, what *you personally* did, and what changed because of it. STAR is the checklist that catches the four omissions Bar Raisers flag in debrief: vague situation, unclear ownership, no concrete actions, no measurable result.[^2]

The biggest single rewrite an Amazon-prepping candidate needs is the pronoun. Stories that drift into "we" tank. Amazon's guide says it directly: rewrite "we" to "I" wherever you personally drove the action.[^2] *"We rolled out a feature flag system"* becomes *"I designed the feature flag system. Two engineers helped me build it. I owned the rollout."* Same project. Different story.

## How do I show "Customer Obsession" in a backend story?

Most candidates assume Customer Obsession requires a customer-facing surface. It doesn't. The principle's official text is "leaders start with the customer and work backwards" and "work vigorously to earn and keep customer trust."[^5] The customer can be internal. Your customer can be the on-call engineer who pages at 3 a.m. Or the data scientist whose query hit your service.

A backend Customer Obsession story has three load-bearing pieces. Who the customer was, named specifically. What they needed, framed as their goal not your work. What you changed in the system to give it to them, with the metric.

*"Our internal ML team was the customer. Their bottleneck was a feature-store query that ran in 800ms p99, which forced them to precompute features overnight and ship stale predictions. I drove the schema change to a covering index. p99 dropped to 40ms. They moved to real-time inference the next quarter."*

That story passes Customer Obsession because it leads with the customer's goal, not your code. It also passes Deliver Results (the metric) and lightly touches Dive Deep (the schema-level fix). One story, three principles. That's the shape you're aiming for.

## How many stories do I need and how should they map?

Eight to twelve. A LeetCode Discuss writeup from a 2.75-YOE Amazon SDE-II candidate who took an offer in 2025 describes the same calibration: a bank of about ten to fifteen stories, each tagged to two or three principles.[^6] Below that count and the same project starts repeating across rounds, which Bar Raisers compare in debrief and downscore. Above that count and you can't keep them rehearsed.

The eight-to-twelve target works because most strong stories already hit two or three principles cleanly. A migration project that you owned solo for six weeks before the company hired more help is Ownership and Bias for Action and Deliver Results. The bug you caught after the launch passed code review is Dive Deep and Earn Trust and Insist on the Highest Standards. Tag each story with the principles it actually demonstrates, not the ones you wish it demonstrated. Forced mappings read as rehearsed and the Bar Raiser is trained to penalize them.[^1]

Your bank should cover the five DSA-round-adjacent principles that surface most often (Customer Obsession, Earn Trust, Dive Deep, Insist on the Highest Standards, Bias for Action) plus the four that show up in nearly every behavioral round (Ownership, Deliver Results, Are Right A Lot, Have Backbone). If a principle has zero stories in your bank after that pass, write one. Two or three of the company-scope principles (Strive to be Earth's Best Employer, Success and Scale Bring Broad Responsibility) almost never come up in SDE loops; one story each is enough insurance.

## What are the four mistakes that tank a strong-on-paper candidate?

**Stories that are all "we" and never "I."** The single most common failure mode. The candidate describes a real, impressive project but uses the team's voice the whole time. The interviewer's debrief reads "could not identify the candidate's specific contribution" and the round scores down. Fix: rewrite every "we" that describes an action you personally took. Keep "we" only when the action was genuinely collective.[^2]

**Results without metrics.** *"It worked well and the team was happy"* is a non-result. Bar Raiser Dawn Brun's published guidance is direct on this: every story needs a measurable outcome.[^7] The Substack 2026 loop breakdown lists "stories with no measurable outcome" as a top-three reason for behavioral-round downscores.[^1] Fix: in every story, finish with a number. Latency, dollar amount, error rate, time saved, retention, headcount, anything quantitative.

**Stories from too long ago.** A senior candidate telling a college internship story raises a different alarm: nothing has happened in eight years that beats this. Aim for stories from the last two to three years; a single story from longer ago is fine if it's genuinely your strongest, but it should not be the bank's center of gravity.[^1]

**Not adapting to the question that was asked.** The Bar Raiser asks *"tell me about a time you disagreed with your manager."* The candidate launches into a rehearsed Customer Obsession story because it's their best one. The interviewer notes "candidate did not answer the question." Bar Raisers Josh Hirschland and Jess Turner both flag this pattern as a downscore.[^7] Fix: keep your bank tagged by principle and by question shape, and pick the story that answers what was asked, even if it's not your strongest one.

## What should I do this week?

Write down ten projects from the last three years, one paragraph each. For each, list the principles it actually demonstrates, the metric in the Result, and the *specific* action you owned. You will find that two or three of your draft stories collapse under that test (no metric, or no clear ownership). Replace them.

Then practice them aloud with a timer. Four minutes per story, no notes. Time the Situation: anything past one minute is too long. The first time you do this you will hate the recording. The second time it will be tolerable. The third time it will be the version you tell on Friday.

For the Amazon-coding-round narration layer (the five interleaved moments inside a 45-minute solve, not the full stories), [Communicating during a coding interview](./02-communicating.md) is the broader baseline. For Meta's parallel, where the format diverges sharply, [Meta AI-assisted coding round](./08-meta-ai-round-format.md) is the contrast piece. The two companies score very different things; do not blur the prep.

## References

[^1]: Rafay Abbasi, "Inside the Amazon 2026 Loop: Rounds, Rubric, and What Each Interviewer Scores You On," *Cracking the Tech Interview* (Substack), May 7, 2026, [dglearning.substack.com/p/inside-the-amazon-2026-loop-rounds](https://dglearning.substack.com/p/inside-the-amazon-2026-loop-rounds).

[^2]: Brittany Bunch, "Your complete guide to the Amazon interview process," *About Amazon* (Workplace), April 8, 2025, [aboutamazon.com/news/workplace/amazon-interview-guide](https://www.aboutamazon.com/news/workplace/amazon-interview-guide).

[^3]: Janz, T., Hellervik, L., and Gilmore, D.C., *Behavior Description Interviewing: New, Accurate, Cost Effective*, Boston: Allyn & Bacon, 1986, ISBN 0-205-08597-0.

[^4]: Flanagan, J.C., "The Critical Incident Technique," *Psychological Bulletin*, 51(4), 327-358, 1954.

[^5]: Amazon Jobs, "Leadership Principles" (canonical page), [amazon.jobs/content/en/our-workplace/leadership-principles](https://www.amazon.jobs/content/en/our-workplace/leadership-principles)

[^6]: "Amazon SDE II Final Loop Experience by a 2.75 YOE candidate," *LeetCode Discuss*, 2025, [leetcode.com/discuss/post/6706138/amazon-sde-ii-final-loop-experience-by-a-svnh/](https://leetcode.com/discuss/post/6706138/amazon-sde-ii-final-loop-experience-by-a-svnh/).

[^7]: Alexis L. Loinaz, "8 interview tips from Amazon Bar Raisers to help you clinch the job," *About Amazon* (Workplace), [aboutamazon.com/news/workplace/amazon-job-interview-questions-tips-bar-raisers](https://www.aboutamazon.com/news/workplace/amazon-job-interview-questions-tips-bar-raisers).
