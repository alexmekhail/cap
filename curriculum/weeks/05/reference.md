# Week 5 Student Reference

## Working Principle
Turn the AI workflow skills from Weeks 1–4 into a small application whose interfaces, data, and behavior you can explain.

## Concepts to Apply
### Scope and architecture
Choose one user, one operation, and one source of data. Draw the boundaries and identify one failure at each boundary. Compare a stateful application with batch/event alternatives; record why the simplest suitable pattern wins.

### Data and API contract
Explain keys, foreign keys, uniqueness, and input validation using the starter. Inspect the initial migration and generated OpenAPI. A schema diagram and contract should match the actual implementation.

### Integration and feedback
Trace a browser request through FastAPI to SQLAlchemy and back. Demonstrate loading, empty, success, and error states. Keep frontend work bounded by adapting the supplied reference.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
Use a duplicate item or nonexistent category. The instructor should explain why those are different failures rather than mapping every error to a generic response.

## Primary References
[FastAPI error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/) · [SQLAlchemy tutorial](https://docs.sqlalchemy.org/en/20/tutorial/) · [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). The production reference is [here](../../../infrastructure/template/README.md).
