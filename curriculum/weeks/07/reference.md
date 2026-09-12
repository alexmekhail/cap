# Week 7 Student Reference

## Working Principle
Reproduce the application outside the development machine and make database changes without losing the evidence or data the system depends on.

## Concepts to Apply
### Build and runtime boundaries
Inspect the multi-stage reference Dockerfile: Node builds static React assets; Python serves the API and assets on the same origin. Dependencies used at build time differ from runtime dependencies. Keep secrets out of layers and inspect the runtime user.

### Database transition and migrations
Run migrations on PostgreSQL, seed records, and verify constraints and query behavior. SQLite results alone do not establish PostgreSQL behavior. Add a nullable field, upgrade against existing data, and compare IDs and relationships afterward.

### Delivery and recovery
Separate image build, migration, and app startup. Define health checks, rollout verification, and what happens if migration or startup fails. Do not have every replica race to run migrations. A rollback may require forward repair rather than a destructive downgrade.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
Change the database hostname to an invalid service name in a disposable environment. Read the failure and fix the configuration. Contrast this with schema mismatch: identical symptoms at the UI may require different repairs.

## Primary References
[Docker multi-stage builds](https://docs.docker.com/build/building/multi-stage/) · [Compose startup order](https://docs.docker.com/compose/how-tos/startup-order/) · [Alembic tutorial](https://alembic.sqlalchemy.org/en/latest/tutorial.html)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). The production reference is [here](../../../infrastructure/template/README.md).
