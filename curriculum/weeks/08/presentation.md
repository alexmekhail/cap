---
marp: true
theme: default
paginate: true
---

# Deployment and Operating Boundaries

Deploy a bounded demonstration that can be verified, observed, recovered, and shut down without confusing a public URL with production readiness.

---

# Choose one deployment path

Default to a single app container on Cloud Run with managed PostgreSQL; an equivalent provider is allowed when the student maps the same responsibilities. A same-origin UI avoids an unnecessary second-host integration problem. Review durable storage and connection limits.

---

# Identity and configuration

Separate the deployer, runtime service identity, and application users. Attach an appropriate runtime identity and grant the needed resource access. Use the provider secret mechanism for database configuration; a service-account key JSON is not an IAM policy.

---

# Release and operational checks

Review the access mode before public exposure. Establish a budget alert, low scaling limits appropriate to the demo, startup/liveness behavior, release smoke checks, and rollback/forward-repair steps. Budget alerts notify; they do not cap spending. Record cleanup steps and retain needed evidence.

---

# Demonstrate and Defend

A deployed synthetic-data demonstration, release evidence, least-privilege identity decisions, and a runbook for verification, recovery, and cleanup.

---

# Homework

Deploy the production project as a bounded demonstration. Use either authenticated/authorized writes with the Week 6 tests or a read-only public mode. Do not expose the unauthenticated starter write endpoint.
5–10 hours. Required criteria and evidence: homework.md.

---

# What Comes Next

Week 9 rehearses incident response in a disposable environment using the same release and observability habits.
