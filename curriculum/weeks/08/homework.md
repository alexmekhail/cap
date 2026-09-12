# Week 8 Homework: Deployment and Operating Boundaries

## Goal and Starting Point
Deploy the production project as a bounded demonstration. Use either authenticated/authorized writes with the Week 6 tests or a read-only public mode. Do not expose unauthenticated write endpoints.

Bring a working container image, PostgreSQL migration evidence, and the Week 6 access policy. Instructor rehearses one cloud path; students arrange cloud access and a personal budget before class. A cloud account is additional to the day-one LLM requirement.

## Required Acceptance Evidence
- A reachable demonstration URL, or documented cloud-access blockage plus a local release rehearsal; the latter is partial, not a completed deployment.
- Managed persistent storage and migration results, with restart/persistence evidence.
- An access policy enforced in the deployed environment, including a forbidden-operation check.
- Documented deployer/runtime/user identity distinctions, narrow grants, and secrets supplied outside source/image layers.
- Budget alert and scaling-limit evidence plus cleanup steps; acknowledge that alerts do not stop charges.
- A release record with image/version, smoke checks, relevant logs, rollback/forward-repair plan, and known limitations.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit the URL, release/runbook document, sanitized configuration evidence, deployment checks, and `docs/prompt-logs/week-08.md`. Never include credentials or raw customer data.

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
Week 9 rehearses incident response in a disposable environment using the same release and observability habits.
