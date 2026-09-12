# Week 5 Homework: Production Entry: One Working Slice

## Goal and Starting Point
Build one complete domain-specific operation on the production starter or your compatible Week 4 app. Avoid a clone-sized feature list: for a library, add a book to a collection; for a marketplace, register a listing; for a content service, save metadata.

Start anew or continue Week 4 work. Use the supplied inventory starter as an executable reference, then choose one approved domain and one narrow user journey. A new stack is not an extra-credit exercise.

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

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit a PR, a 3–5 minute demo, `docs/adrs/001-architecture.md`, exported OpenAPI or a reviewed contract, schema/migration evidence, and the weekly log. Explain one route, one relationship, and one acceptance test.

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
Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.
