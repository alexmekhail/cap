# Week 5: Capstone API & Frontend Integration

## Entry Point
Continue the Week 4 FastAPI/SQLAlchemy capstone with its ADR, API contract, migrations, seed data, tests, and simple local UI. Resolve an incomplete core API-to-database slice before adding new UI scope. The instructor supplies and rehearses a minimal React/TypeScript scaffold before class; students place it in `/src/frontend`.

## Technical Deep Dive (75m)
- **Contract review (25m):** Strengthen Pydantic request/response validation, documented errors, and separation between routes and business logic. Update the Week 4 OpenAPI contract rather than inventing a competing API.
- **External integrations (20m):** Handle timeout and upstream failure paths with an HTTP client; bound retries and avoid automatically repeating non-idempotent writes.
- **Frontend integration (30m):** Connect the provided React/TypeScript UI to the contract, including loading, empty, success, and error states. Keep credentials on the backend.

## Lab: Extend the Existing Slice
1. Review the W4 contract against the working API and document one correction.
2. Add or strengthen an external data integration appropriate to the domain, using a deterministic fixture for tests.
3. Integrate the provided frontend with one complete workflow. Reuse existing functionality; replacing the simple W4 UI is expected.
4. Run backend and frontend checks; demonstrate a successful request, invalid input, and an upstream timeout/failure.
5. Record the architectural decision, checks, and interventions in `docs/prompt-logs/week-05.md`.

## Deliverable
A PR in the continuing capstone repository with the integrated UI, updated contract, tests, and evidence of success and failure behavior. Keep SQLite for this milestone. Week 6 strengthens quality gates; Week 7 adds PostgreSQL and containers; Week 8 deploys.
