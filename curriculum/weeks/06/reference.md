# Week 6 Student Reference

## Working Principle
Establish checks that expose important failures and define who may perform each operation before the application is made public.

## Concepts to Apply
### Contract-focused testing
Choose checks from the user contract: valid input, invalid input, missing records, duplicate writes, persistence, and state changes. Separate upstream timeout/rate-limit failures from client validation. Decide the mapping in your contract and assert it.

### Access and security
Identify trusted/untrusted inputs and write endpoints. Choose a read-only synthetic public demo or implement tested authentication and object-level authorization. A user ID provided by the caller is not proof of identity. Use two actors to test ownership rules.

### Quality gates and interpretation
Run tests, coverage, lint, static security, dependency audits, and log-structure checks. Teach that a green scan means no findings from that tool/configuration, not zero vulnerabilities. Treat assessment as human-reviewed evidence, not a count of prompts.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
The old curriculum conflated upstream 429 responses with malformed user input. Use a concrete contract: invalid request → 422; duplicate → 409; a bounded unavailable dependency may produce 503 or another explicitly justified server-side response. Do not rewrite upstream failures as client mistakes by default.

## Primary References
[FastAPI errors](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [GitHub secure workflow use](https://docs.github.com/en/actions/reference/security/secure-use) · [OWASP authorization guidance](https://cheatsheetseries.owasp.org/cheatsheets/Authorization_Cheat_Sheet.html)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). Use your own project or the instructor’s chosen classroom example.
