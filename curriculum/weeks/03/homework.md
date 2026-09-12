# Week 3 Homework: A Substantial Excalidraw Feature

## Goal
Fork [Excalidraw](https://github.com/excalidraw/excalidraw) and implement a substantial feature using **one sustained terminal agent**. The assignment tests context discovery, project instructions, reusable skills, planning, and supervision in a large unfamiliar codebase. Do not dump the repository into a chat or substitute a new standalone drawing app.

## Choose a Different Challenge
Students may choose either track below, or propose an equivalent feature with comparable state, interaction, and persistence complexity. Record the chosen track and acceptance criteria before implementation. Full polish is not expected within one week, but a working core and credible validation are.

### Track A: Tabs and Drawing Workspaces
- Create, name, switch between, and delete drawing tabs without mixing their content.
- Persist tabs and the active drawing across reload.
- Duplicate a tab with independently editable content.
- Copy selected elements between tabs and explain ID/reference handling.
- Verify drawing isolation, deletion behavior, duplication, and persistence.
- **Extension:** Overlay another tab at adjustable opacity for comparison. Explain coordinate alignment and how you avoid editing the reference layer accidentally.

### Track B: Comments and Review
- Select one or more elements and attach a comment thread to that selection.
- Select a pin or thread to reveal the corresponding comment and associated elements.
- Support replies and resolving/reopening threads.
- Keep comment positioning meaningful while panning, zooming, and moving elements; document the policy for deleted elements.
- Persist comments per drawing across reload and avoid cross-drawing leakage.
- Verify selection association, coordinate behavior, thread actions, and persistence.
- See [comments-brief.md](comments-brief.md) for the interaction and acceptance details. No paid Excalidraw account is needed.

## Required Engineering Method
1. Fork the repository, record the exact base commit, and follow its checked-out setup documentation. Record runtime/package-manager versions and working commands. Establish relevant baseline tests; separate existing failures from regressions.
2. Map the actual files and symbols for rendering, state, persistence, selection, and your feature. Verify claims by opening the source. Document the map and one architectural decision.
3. Write project instructions appropriate to your chosen agent and at least one reusable skill that helps navigate or validate this codebase. Show how they were used and revised.
4. Define a feature plan and acceptance checks. Use one agent for sustained implementation with explicit limits and checkpoints. A couple of hours may be appropriate for a work session; do not keep an idle or failing agent running merely to satisfy a clock.
5. Demonstrate a checkpoint/resume: persist completed work, evidence, open issues, and next steps, then have the agent continue from that state.
6. Review diffs and independently rerun checks. Add meaningful tests for state/persistence and manual evidence for interactive behavior.

## Budget (5–10 hours)
Setup and map (1–2h); specify and configure (1–2h); implement in checkpoints (2–4h); verify and report (1–2h). At the end of the budget, report each acceptance criterion as met, partial, or unmet with evidence. Do not silently redefine completion or trade validation for visual polish.

## Submission
A PR to your own fork with the feature specification, architecture/context map, project instructions, skill, tests, and `docs/prompt-logs/week-03.md` using the [shared template](../../../infrastructure/template/docs/prompt-logs/TEMPLATE.md). Include setup commands, base commit, a checkpoint/resume excerpt, and a short demo covering core interactions. Explain what you trusted, checked, corrected, and left incomplete. Share before the next class; do not send the assignment PR upstream unless independently appropriate.

## Assessment
| Criterion | Weight |
|---|---|
| Working core feature and clear acceptance evidence | 30% |
| Verified architecture, context management, and reusable skill | 25% |
| Sustained supervision, useful checkpoints, and justified interventions | 20% |
| Tests, integration integrity, and honest technical defense | 25% |

Extensions enrich a completed core; they do not replace required behavior. Cite public reference code you reused and explain your contribution.
