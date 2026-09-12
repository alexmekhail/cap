# Week 11 Homework: Interviews: Explain, Repair, and Defend

## Goal and Starting Point
Complete two mock interview rounds with a peer, switching interviewer and candidate. Include unaided explanation, permitted AI-assisted repair, architecture defense, and feedback. Practice on a variation rather than memorizing the public reference solution.

Bring the capstone architecture, Week 10 SOP, and one evidence-backed case study. The mock interviewer explicitly states whether AI is allowed for each section.

## Required Acceptance Evidence
- Explicitly recorded tool rules and a short unaided explanation of the code/data flow.
- A defect identified through behavior and evidence, not only a bad-looking prompt.
- A repair with positive and negative checks; distinguish SQL injection from missing authorization.
- A clear architecture defense including a rejected alternative and a known limitation.
- Peer feedback grounded in observable behavior and a follow-up practice action.
- A short truthful portfolio narrative linking to a project decision, test, and demonstration.

## Work Budget: 5–10 Hours
- Planning and baseline review: 1–2h.
- Main implementation or exercise: 2–4h.
- Independent checks and repair: 1–2h.
- Demonstration, reflection, and submission: 1–2h.

At the end of the budget, report required criteria as met, partial, or unmet with links. Incomplete work earns credit for demonstrated criteria, but it is not labeled complete. Resolve a broken core before optional extensions. Ask for targeted help with a concise diagnosis rather than spending the entire week repeating the same failed attempt.

## Submission
Submit the exercise PR, interview notes with both roles, check output, feedback, and `docs/prompt-logs/week-11.md`. Record only with the participant’s permission; written notes suffice.

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
Week 12 packages the verified work for a final demonstration and job applications.
