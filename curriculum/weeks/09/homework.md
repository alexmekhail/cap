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

Report each required criterion as met, partial, or unmet with evidence. Prioritize broken core behavior before optional extensions.

## Submission
Submit a PR in your own repository, red/green check output, a short incident report, and `docs/prompt-logs/week-09.md`. A merge is not required for grading; review evidence is.

Use the [shared evidence-log template](../../../infrastructure/template/docs/prompt-logs/TEMPLATE.md). Share the PR/repository link to your own repository before the next session. Disclose reused material and explain your contribution.

## Assessment
The [shared engineering rubric](../../../tools/agentic-mentor/evaluation-rubric.md) applies: context management, validation and correction, structural oversight, and system integrity, each worth 25%. Assess these against the required evidence above; missing evidence keeps the affected score provisional.

## Next
Week 10 uses incident and earlier workflow evidence to test a specific improvement.
