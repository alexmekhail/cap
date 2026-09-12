---
marp: true
theme: default
paginate: true
---

# Containers, PostgreSQL, and Delivery

Reproduce the application outside the development machine and make database changes without losing the evidence or data the system depends on.

---

# Build and runtime boundaries

Inspect the multi-stage reference Dockerfile: Node builds static React assets; Python serves the API and assets on the same origin. Dependencies used at build time differ from runtime dependencies. Keep secrets out of layers and inspect the runtime user.

---

# Database transition and migrations

Run migrations on PostgreSQL, seed records, and verify constraints and query behavior. SQLite results alone do not establish PostgreSQL behavior. Add a nullable field, upgrade against existing data, and compare IDs and relationships afterward.

---

# Delivery and recovery

Separate image build, migration, and app startup. Define health checks, rollout verification, and what happens if migration or startup fails. Do not have every replica race to run migrations. A rollback may require forward repair rather than a destructive downgrade.

---

# Demonstrate and Defend

A containerized app connected to PostgreSQL, with explicit migration steps, data-preservation evidence, and CI image build checks.

---

# Homework

Containerize the production project, verify it on PostgreSQL, and add one safe schema evolution. Extend CI to build the app image; document how the application and schema versions remain compatible.
5–10 hours. Required criteria and evidence: homework.md.

---

# What Comes Next

Week 8 deploys the tested image with managed persistence and an explicit release/access decision.
