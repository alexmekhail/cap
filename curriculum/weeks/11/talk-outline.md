# Week 11: Interviews: Explain, Repair, and Defend

## Teaching Purpose
Demonstrate engineering understanding with and without AI, communicate tradeoffs, and use tools only within the stated interview rules.

## Entry Check
Bring the capstone architecture, Week 10 SOP, and one evidence-backed case study. The mock interviewer explicitly states whether AI is allowed for each section.

## Exit Evidence
A completed mock interview, peer feedback, a verified repair, and a concrete improvement plan.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). Inspect student entry evidence before expanding scope. The required assignment is in [homework.md](homework.md); avoid maintaining a second specification in slides.

## Core Instruction
### 1. Clarify the task and tool rules (25m)
Ask about requirements and constraints before implementation. Separate a short unaided explanation from an AI-assisted repair. Do not assume employers allow AI because the course teaches it.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 2. Audit behavior and authorization (25m)
Inspect a bounded endpoint or function. Distinguish input validation, authentication, authorization, and SQL parameterization. A safe query does not automatically prevent cross-user access.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 3. Defend the result (25m)
Explain the affected data flow, tests, tradeoffs, and remaining risks. Present an architecture decision with an alternative and connect portfolio claims to actual evidence.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

## Instructor Demonstration (45m)
Use the public interview exercise in the reference. First explain the authorization defect without AI. Then allow the agent to propose a repair and tests, inspect the change, and prove that user A cannot read user B’s record while the owner still can. Use prepared tests as disclosed calibration, not a secret answer.

Use [instructor-demo.md](instructor-demo.md) for preparation, checkpoints, and fallback. Ask students to predict the outcome before running the check, then reconcile their prediction with the evidence.

## Student Practice and Review (60m)
Run one 20m round, switch for a second 20m round, then spend 20m on feedback and a repeated explanation of the weakest point.

## Misconception to Address
A parameterized SQL query can still return another user’s record if ownership is not checked. Require an explicit actor/resource relationship and test both allowed and denied access.

## Close the Session
Have students name one decision, the evidence supporting it, and the next missing check. Confirm they can find the homework and know what to submit. Do not equate partially demonstrated behavior with a completed milestone.

## Connection to the Next Stage
Week 12 packages the verified work for a final demonstration and job applications.

## Materials
[Presenter notes](lecture-script.md) · [Slides](presentation.md) · [Student reference](reference.md) · [Homework](homework.md)
