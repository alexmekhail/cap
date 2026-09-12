# Week 6 Homework: Quality, Access, and Evidence

## Goal and Starting Point
Strengthen the Week 5 project and make the release access decision. Configure checks appropriate to your project, add meaningful failure cases, and demonstrate at least one intentionally incorrect implementation failing a relevant test.

Bring the Week 5 slice, contract, migrations, and a working local check command. If setup is incomplete, pair on an instructor-selected example to learn the checks while recording the gap in your own project.

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

Report each required criterion as met, partial, or unmet with evidence. Prioritize broken core behavior before optional extensions.

## Submission
Submit the PR, CI run URL, access-policy note, test results, one deliberate failure demonstration, and `docs/prompt-logs/week-06.md`. Do not claim a scan proves complete security.

Use the [shared evidence-log template](../../../infrastructure/template/docs/prompt-logs/TEMPLATE.md). Share the PR/repository link to your own repository before the next session. Disclose reused material and explain your contribution.

## Assessment
The [shared engineering rubric](../../../tools/agentic-mentor/evaluation-rubric.md) applies: context management, validation and correction, structural oversight, and system integrity, each worth 25%. Assess these against the required evidence above; missing evidence keeps the affected score provisional.

## Next
Week 7 transports the tested app into containers and verifies its database behavior on PostgreSQL.
