# Week 6 Homework: Quality, Access, and Evidence

## Goal and Starting Point
Strengthen the Week 5 project and make the release access decision. Configure the provided checks for your project, add meaningful failure cases, and demonstrate at least one intentionally incorrect implementation failing a relevant test.

Bring the Week 5 slice, contract, migrations, and a working local check command. If setup is incomplete, use the reference starter to learn the checks while recording the gap in your own project.

## Required Acceptance Evidence
- Success and failure tests for the core contract, including persistence and input handling; test an upstream error with a fake response if your app uses an external service.
- At least 80% backend coverage as a course floor, plus a written explanation of a significant behavior coverage does not prove.
- An access policy: a public read-only synthetic demonstration with writes disabled, or authenticated writes with object-level authorization and two-actor tests.
- A CI run that installs dependencies, executes tests/lint/security checks, builds the frontend, and checks an actual evidence log.
- Findings triaged with fixes or a justified, narrow exception; no blanket suppression to obtain a green result.
- A red-before/green-after demonstration of a meaningful check, with unchanged acceptance intent.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit the PR, CI run URL, access-policy note, test results, one deliberate failure demonstration, and `docs/prompt-logs/week-06.md`. Do not claim a scan proves complete security.

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
Week 7 transports the tested app into containers and verifies its database behavior on PostgreSQL.
