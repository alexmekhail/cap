# Week 5 Homework: Production Entry: One Working Slice

## Goal and Starting Point
Build one complete domain-specific operation in a new project or your compatible Week 4 app. Avoid a clone-sized feature list: for a library, add a book to a collection; for a marketplace, register a listing; for a content service, save metadata.

## Required Acceptance Evidence
- A working browser interaction that writes and reads persisted data, with empty/loading/error feedback.
- An ADR with the chosen architecture, one rejected alternative, and a scope boundary.
- A relational schema with an enforced relationship and uniqueness/integrity rules relevant to the domain.
- An initial migration reproducible on an empty database; test data can be seeded repeatedly.
- An API contract with successful and invalid requests, including evidence that UI and API agree.
- Run instructions and meaningful checks; record missing authentication as a release blocker rather than silently implying production readiness.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

Report each required criterion as met, partial, or unmet with evidence. Prioritize broken core behavior before optional extensions.

## Submission
Submit a PR, a 3–5 minute demo, `docs/adrs/001-architecture.md`, exported OpenAPI or a reviewed contract, schema/migration evidence, and the weekly log. Explain one route, one relationship, and one acceptance test.

Use the [shared evidence-log template](../../../infrastructure/template/docs/prompt-logs/TEMPLATE.md). Share the PR/repository link to your own repository before the next session. Disclose reused material and explain your contribution.

## Assessment
The [shared engineering rubric](../../../tools/agentic-mentor/evaluation-rubric.md) applies: context management, validation and correction, structural oversight, and system integrity, each worth 25%. Assess these against the required evidence above; missing evidence keeps the affected score provisional.

## Next
Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.
