# Week 5: Production Project Entry — Architecture, API & Frontend

## Entry Point
Choose an approved domain from the master curriculum. Start a new repository or adapt Week 4 work if it fits the production objectives. Do not assume the previous app has a Python backend, database, or migration history. Review prior evidence to identify gaps in verification and supervision.

The instructor supplies a rehearsed minimal FastAPI/SQLAlchemy/Alembic and React/TypeScript starter before class, with setup/run/check commands. Use it to reach one coherent slice within the 5–10 hour homework budget; adapting a starter is allowed when students explain it.

## Technical Deep Dive (75m)
- **Architecture and data (25m):** Define UI → API → business logic → database boundaries. Write an ADR comparing a simple stateful app with batch/event-driven alternatives. Design keys, relationships, uniqueness, deletion behavior, and an index tied to a real query. Establish initial migrations and demonstrate a schema change preserving seeded records.
- **API contract (25m):** Define request/response validation and failure behavior. Separate routes from business logic. Bound retries and use deterministic fixtures for external integrations.
- **Frontend integration (25m):** Connect the provided React/TypeScript UI to one complete API workflow, including loading, empty, success, and error states. Keep credentials on the backend.

## Lab and Independent Work
1. Decide whether to start anew or continue, and record the reason.
2. Establish the ADR, API contract, schema, and reproducible run/check commands.
3. Build one narrow UI-to-API-to-database workflow with SQLite, SQLAlchemy, and Alembic.
4. Demonstrate the initial migration and a data-preserving schema change. Check constraints and one failure case.
5. Integrate an external data source where appropriate to the domain; isolate it behind a test fixture.
6. Record checks, architectural decisions, and interventions in `docs/prompt-logs/week-05.md`.

## Deliverable
A PR with a working slice, integrated UI, ADR, contract, schema/migrations, tests, and evidence for success and failure behavior. This is the production project retained through Week 12. Week 6 strengthens quality gates; Week 7 validates PostgreSQL and adds containers; Week 8 deploys.
