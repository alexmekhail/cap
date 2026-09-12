# Week 7 Homework: Containers, PostgreSQL, and Delivery

## Goal and Starting Point
Containerize the production project, verify it on PostgreSQL, and add one safe schema evolution. Extend CI to build the app image; document how the application and schema versions remain compatible.

Bring the Week 6 application, passing local checks, initial migration, and access policy. Install Docker before class; a setup blocker must be recorded rather than hidden behind a successful local run.

## Required Acceptance Evidence
- A repeatable multi-stage image build and a local Compose run with app and PostgreSQL separated.
- Database credentials provided through runtime configuration; local example credentials are clearly local-only.
- Initial migrations work on an empty PostgreSQL database, and the relevant API/integrity tests run against PostgreSQL.
- A follow-up migration preserves pre-existing IDs, values, and relationships; include before/after evidence.
- A restart demonstration retains data; explain the difference between app containers and the database volume.
- A CI image build and a release sequence with stop conditions and a non-destructive recovery plan.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit Docker/Compose configuration, the migration, PostgreSQL check results, restart evidence, a CI build URL, and `docs/prompt-logs/week-07.md`. Screenshots of a running container alone are insufficient.

Use the [shared evidence-log template](../../../infrastructure/template/docs/prompt-logs/TEMPLATE.md). Push to your own repository and share the PR/repository link before the next session (Week 12: by the final presentation). All course references are visible; disclose reuse and explain your contribution. A PR to an upstream open-source project is not required.

## Assessment
Use the [shared engineering rubric](../../../tools/agentic-mentor/evaluation-rubric.md), four equally weighted dimensions:

| Dimension | Weight | Evidence in this assignment |
|---|---|---|
| Context management | 25% | Correct baseline, relevant information, and explicit constraints |
| Validation and correction | 25% | Meaningful checks, diagnosis, and justified intervention |
| Structural oversight | 25% | Defensible boundaries, tradeoffs, and controlled changes |
| System integrity | 25% | Required behavior works, failure cases are checked, limits are honest |

Missing evidence keeps the affected criterion provisional. Do not award points simply for prompt count, code volume, number of agents, or unsupported claims of speed/security.

## Completion Check
Could a reviewer reproduce your main claim from the submitted instructions and evidence? State any tool, account, or environment dependency that prevents reproduction.

## Next
Week 8 deploys the tested image with managed persistence and an explicit release/access decision.
