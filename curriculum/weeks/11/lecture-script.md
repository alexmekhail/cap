# Week 11 Presenter Notes: Interviews: Explain, Repair, and Defend

## Opening
“Demonstrate engineering understanding with and without AI, communicate tradeoffs, and use tools only within the stated interview rules.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Clarify the task and tool rules
Ask about requirements and constraints before implementation. Separate a short unaided explanation from an AI-assisted repair. Do not assume employers allow AI because the course teaches it.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Audit behavior and authorization
Inspect a bounded endpoint or function. Distinguish input validation, authentication, authorization, and SQL parameterization. A safe query does not automatically prevent cross-user access.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Defend the result
Explain the affected data flow, tests, tradeoffs, and remaining risks. Present an architecture decision with an alternative and connect portfolio claims to actual evidence.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
A parameterized SQL query can still return another user’s record if ownership is not checked. Require an explicit actor/resource relationship and test both allowed and denied access.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 12 packages the verified work for a final demonstration and job applications.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
