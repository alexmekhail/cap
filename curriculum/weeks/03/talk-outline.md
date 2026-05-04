# Week 3: Architecture & Starter Cloud Patterns

## Talk Outline: Designing for the Cloud
### Technical Deep Dive (75m)
- **Architectural Decision Records (ADRs):** Forcing AI to justify its choices and avoiding "Hype-Driven Development".
- **Starter Cloud Patterns on GCP:** Do not let AI invent architectures. Steer it toward established "Golden Paths":
    1.  **Scheduled Batch Pattern:** Cloud Scheduler -> Cloud Run Job -> BigQuery. Best for content metadata (Netflix clone).
    2.  **Event-Driven Serverless Pattern:** API Gateway -> Cloud Functions -> Pub/Sub -> Firestore. Best for high-throughput (Twitter clone, Ads Auction).
    3.  **Stateful Container Pattern:** Cloud Load Balancing -> Cloud Run -> Cloud SQL (PostgreSQL). Best for complex relational data (Marketplace, Legal Storage).
- **Security by Design:** Asking AI to identify specific IAM roles (e.g., `roles/run.invoker`) *before* coding.

## Lab Instructions: The ADR Defense
### Objective
Select a concrete Starter Cloud Pattern for your Production-Grade Cloud Application and defend it.

### Steps
1. **Pattern Matching:** Based on your chosen project (e.g., Airbnb Clone), select one of the three Starter Cloud Patterns.
2. **Steering the AI:** Prompt the AI to map your specific ingestion and transformation needs to the selected pattern. *Constraint: Forbid the AI from adding Kafka or Kubernetes.*
3. **The ADR:** Write `docs/adrs/001-cloud-architecture.md`. You must include the chosen Starter Pattern, the rejected patterns, and *why* they were rejected based on data throughput and latency needs.
4. **The Log:** Update `docs/prompt-logs/week-03.md` highlighting how you steered the AI back to a simple Starter Pattern when it tried to over-engineer.

### Deliverable
A completed ADR defining a concrete Starter Cloud Pattern and a Prompt Log showing structural oversight.
