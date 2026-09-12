# Week 8 Student Reference

## Working Principle
Deploy a bounded demonstration that can be verified, observed, recovered, and shut down without confusing a public URL with production readiness.

## Concepts to Apply
### Choose one deployment path
Default to a single app container on Cloud Run with managed PostgreSQL; an equivalent provider is allowed when the student maps the same responsibilities. A same-origin UI avoids an unnecessary second-host integration problem. Review durable storage and connection limits.

### Identity and configuration
Separate the deployer, runtime service identity, and application users. Attach an appropriate runtime identity and grant the needed resource access. Use the provider secret mechanism for database configuration; a service-account key JSON is not an IAM policy.

### Release and operational checks
Review the access mode before public exposure. Establish a budget alert, low scaling limits appropriate to the demo, startup/liveness behavior, release smoke checks, and rollback/forward-repair steps. Budget alerts notify; they do not cap spending. Record cleanup steps and retain needed evidence.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
Demonstrate a missing runtime permission in the instructor sandbox. Identify which identity needs which resource grant rather than adding broad administrator access. Keep this separate from app-user authorization.

## Primary References
[Cloud Run service identity](https://docs.cloud.google.com/run/docs/securing/service-identity) · [Cloud Run secrets](https://docs.cloud.google.com/run/docs/configuring/services/secrets) · [Budget alerts](https://docs.cloud.google.com/billing/docs/how-to/budgets)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). Use your own project or the instructor’s chosen classroom example.
