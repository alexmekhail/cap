# Week 10 Homework: Workflow Audit and Measured Improvement

## Goal and Starting Point
Audit your own work and test one improvement. Choose a change such as better acceptance criteria, a reusable skill, a shorter context map, a checkpoint, or a different review boundary—not several changes at once.

Bring logs, PRs, and check results from Weeks 1–9, including the incident exercise. Include a case where autonomous work helped and one where manual investigation was justified.

## Required Acceptance Evidence
- Three linked cases from your own Weeks 1–9 artifacts with a supported explanation.
- One controlled comparison on a bounded task with the same baseline and acceptance checks.
- Recorded effort and outcome measures, including limitations and negative/inconclusive results.
- A concise AI Workflow SOP with concrete triggers, steps, and evidence requirements.
- At least one updated or removed instruction/skill justified by the comparison.
- An explanation of when extra agents were useful and when they added coordination overhead.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit `docs/ai-workflow-sop.md`, case-study links, comparison evidence, and `docs/prompt-logs/week-10.md`. Disclose model/tool changes that confound the comparison.

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
Week 11 tests whether students can explain and adapt this workflow under interview constraints.
