# Handoff: Foundations to the Continuing Capstone

## End-of-Week-4 Baseline
Students have tried AI coding, practiced validation, navigated an unfamiliar existing codebase, and supervised an agent through a bounded full-stack build.

The Week 4 repository is the capstone they retain through Week 12. It contains:
- One approved project domain and a working local slice: simple UI → FastAPI → SQLAlchemy → SQLite.
- An architecture ADR, API contract, schema diagram, and initial plus follow-up Alembic migrations with data-preservation evidence.
- Varied seed data, tests for core and failure behavior, and configured validation commands.
- Agent instructions, logs explaining automated corrections and human interventions, and a reflection on remaining limitations.

Four related tables, 100 users, and ten meaningful tests are scope targets. Mentors assess demonstrated integrity and judgment rather than counts alone. Record unfinished criteria explicitly; do not assume every student reaches the baseline on schedule.

## Week 5 Intake
Review the local slice, contract, migrations, and test evidence. Agree a recovery plan for missing core behavior before expanding UI scope. The instructor supplies a tested React/TypeScript scaffold; students integrate it with their existing API.

## Continuation
| Week | Work on the same capstone |
|---|---|
| 5 | Strengthen API contracts and external integrations; integrate the provided frontend |
| 6 | Add failure-path tests, coverage, security scanning, and quality gates |
| 7 | Validate migrations and behavior on PostgreSQL; containerize and extend CI |
| 8 | Review deployment architecture, IAM, secrets, and budgets; deploy |
| 9 | Diagnose an injected incident and protect the fix with a regression test |
| 10 | Audit workflow evidence and test one improvement; write the AI Workflow SOP |
| 11 | Practice interviews using the workflow and architecture decisions |
| 12 | Present the deployed capstone and a verified before/after engineering case study |

## Topics Still to Teach
Cloud deployment, managed database operations, production secrets and IAM, containerization, CI/CD, operational debugging, and interview practice. W4 introduces local contracts, data integrity, migrations, and agent checks; it does not certify production readiness.

## Assessment Handoff
Week 1 is assessed through its exploratory field report. Weeks 2–4 use their published weights with the shared rubric as evidence guidance. Weeks 5–12 use the shared rubric. Reward effective checks, justified decisions, and proportionate intervention. Neither autonomous recovery nor multiple iterations is a failure by itself.
