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
[Homework and submission requirements](homework.md). The production reference is [here](../../../infrastructure/template/README.md).

## Public Interview Exercise
Use [authorization.py](demo/authorization.py) and [its checks](demo/test_authorization.py). From `demo/`, run `python3 -m unittest -v`. The vulnerable function intentionally ignores ownership; the corrected reference assumes actor identity was authenticated upstream. It demonstrates authorization only, not a complete authentication system. For the mock interview, vary the policy or data model and ask the candidate to explain it before using AI.
