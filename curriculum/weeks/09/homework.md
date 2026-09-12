# Week 9 Homework: Incident Response and Regression Repair

## Goal and Starting Point
Inject one controlled defect into a disposable branch or test environment: a serialization mismatch, duplicate-write failure, or query-count regression. Diagnose it with AI assistance, protect the fix with a regression check, and explain recovery.

Bring a reproducible release and sanitized logs. Run the exercise in a disposable local/staging copy; do not inject faults into a service people depend on.

## Required Acceptance Evidence
- An isolated exercise environment and known baseline, with no real-user or production-data impact.
- A reproducible symptom and sanitized evidence linked to the affected version.
- At least two plausible hypotheses and a discriminating check.
- A regression check observed failing before the fix and passing afterward.
- A reviewed fix plus relevant broader checks showing recovery without a new regression.
- An incident note with impact, timeline, cause, recovery, prevention, and remaining uncertainty.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit a PR in your own repository, red/green check output, a short incident report, and `docs/prompt-logs/week-09.md`. A merge is not required for grading; review evidence is.

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
Week 10 uses incident and earlier workflow evidence to test a specific improvement.
