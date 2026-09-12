# Week 9 Presenter Notes: Incident Response and Regression Repair

## Opening
“Use evidence to diagnose a failure, write a regression check, and verify recovery while keeping the exercise isolated from real users and data.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Observe before fixing
Record the symptom, scope, timeline, and last known good version. Separate user-visible impact from a suspected cause. Sanitize logs before sharing them with an agent; preserve useful timestamps and request identifiers.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Hypothesis and reproduction
Ask the agent for competing explanations and a check that distinguishes them. Use a deterministic fixture rather than hoping an intermittent fault appears. Write a regression test that fails before the fix.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Repair and recovery
Review the smallest sufficient change, run relevant regression and integration checks, and verify the original symptom is gone. Record what prevented earlier detection and which runbook or check needs to change.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
A failing test does not by itself prove the agent hallucinated. The cause may be a bad requirement, a changed dependency, an environment error, or a code defect; require evidence before attribution.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 10 uses incident and earlier workflow evidence to test a specific improvement.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
