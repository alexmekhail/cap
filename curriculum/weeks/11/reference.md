# Week 11 Student Reference

## Working Principle
Demonstrate engineering understanding with and without AI, communicate tradeoffs, and use tools only within the stated interview rules.

## Concepts to Apply
### Clarify the task and tool rules
Ask about requirements and constraints before implementation. Separate a short unaided explanation from an AI-assisted repair. Do not assume employers allow AI because the course teaches it.

### Audit behavior and authorization
Inspect a bounded endpoint or function. Distinguish input validation, authentication, authorization, and SQL parameterization. A safe query does not automatically prevent cross-user access.

### Defend the result
Explain the affected data flow, tests, tradeoffs, and remaining risks. Present an architecture decision with an alternative and connect portfolio claims to actual evidence.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
A parameterized SQL query can still return another user’s record if ownership is not checked. Require an explicit actor/resource relationship and test both allowed and denied access.

## Primary References
[OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). Use your own project or the instructor’s chosen classroom example.
