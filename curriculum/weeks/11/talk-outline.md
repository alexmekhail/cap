# Week 11: Interviews: Explain, Repair, and Defend

## Teaching Purpose
Demonstrate engineering understanding with and without AI, communicate tradeoffs, and use tools only within the stated interview rules.

## Entry Check
Bring the capstone architecture, Week 10 SOP, and one evidence-backed case study. The mock interviewer explicitly states whether AI is allowed for each section.

## Exit Evidence
A completed mock interview, peer feedback, a verified repair, and a concrete improvement plan.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). The assignment is in [homework.md](homework.md).

## Core Instruction
### 1. Clarify the task and tool rules (25m)
Ask about requirements and constraints before implementation. Separate a short unaided explanation from an AI-assisted repair. Do not assume employers allow AI because the course teaches it.

### 2. Audit behavior and authorization (25m)
Inspect a bounded endpoint or function. Distinguish input validation, authentication, authorization, and SQL parameterization. A safe query does not automatically prevent cross-user access.

### 3. Defend the result (25m)
Explain the affected data flow, tests, tradeoffs, and remaining risks. Present an architecture decision with an alternative and connect portfolio claims to actual evidence.

## Instructor Demonstration Plan (45m)
Prepare a small function that returns a record by ID without checking whether the authenticated actor owns it. First explain the authorization defect without AI. Then allow the agent to propose a repair and tests, inspect the change, and prove that user A cannot read user B’s record while the owner still can. Use prepared tests as disclosed calibration, not a secret answer.

## Student Practice and Review (60m)
Run one 20m round, switch for a second 20m round, then spend 20m on feedback and a repeated explanation of the weakest point.

## Misconception to Address
A parameterized SQL query can still return another user’s record if ownership is not checked. Require an explicit actor/resource relationship and test both allowed and denied access.

## Connection to the Next Stage
Week 12 packages the verified work for a final demonstration and job applications.

## Further Reading
[OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)
