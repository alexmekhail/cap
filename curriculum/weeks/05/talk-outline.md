# Week 5: Production Entry: One Working Slice

## Teaching Purpose
Turn the AI workflow skills from Weeks 1–4 into a small application whose interfaces, data, and behavior you can explain.

## Entry Check
Start anew or continue Week 4 work. Choose one approved domain and one narrow user journey; build anew or adapt an existing repository using AI. A new stack is not an extra-credit exercise.

## Exit Evidence
A reproducible UI → API → database slice, a short ADR, an API contract, and an initial migration. This repository continues through Week 12.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). The assignment is in [homework.md](homework.md).

## Core Instruction
### 1. Scope and architecture (25m)
Choose one user, one operation, and one source of data. Draw the boundaries and identify one failure at each boundary. Compare a stateful application with batch/event alternatives; record why the simplest suitable pattern wins.

### 2. Data and API contract (25m)
Explain keys, foreign keys, uniqueness, and input validation using a small example from the instructor’s chosen project. Inspect the initial migration and generated OpenAPI. A schema diagram and contract should match the actual implementation.

### 3. Integration and feedback (25m)
Trace a browser request through FastAPI to SQLAlchemy and back. Demonstrate loading, empty, success, and error states. Keep frontend scope to the selected user journey.

## Instructor Demonstration Plan (45m)
For an inventory example, demonstrate a category and item, reload the UI, then submit a duplicate and an unknown category. Prepare this behavior in the chosen classroom project before the session. Trace the 409 and 422 responses through the client and backend. Open the migration and explain the foreign key. Have the agent propose a domain adaptation, inspect the proposed boundary changes, and implement one small part.

## Student Practice and Review (60m)
Pairs map the request path in their chosen project (15m), adapt one domain operation (30m), and review the ADR and contract against the running result (15m).

## Misconception to Address
Use a duplicate item or nonexistent category. The instructor should explain why those are different failures rather than mapping every error to a generic response.

## Connection to the Next Stage
Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.

## Further Reading
[FastAPI error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)
