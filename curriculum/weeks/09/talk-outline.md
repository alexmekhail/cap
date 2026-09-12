# Week 9: Incident Response and Regression Repair

## Teaching Purpose
Use evidence to diagnose a failure, write a regression check, and verify recovery while keeping the exercise isolated from real users and data.

## Entry Check
Bring a reproducible release and sanitized logs. Run the exercise in a disposable local/staging copy; do not inject faults into a service people depend on.

## Exit Evidence
A reproduced incident, evidence-backed diagnosis, failing regression test, verified fix, and short incident report.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). The assignment is in [homework.md](homework.md).

## Core Instruction
### 1. Observe before fixing (25m)
Record the symptom, scope, timeline, and last known good version. Separate user-visible impact from a suspected cause. Sanitize logs before sharing them with an agent; preserve useful timestamps and request identifiers.

### 2. Hypothesis and reproduction (25m)
Ask the agent for competing explanations and a check that distinguishes them. Use a deterministic fixture rather than hoping an intermittent fault appears. Write a regression test that fails before the fix.

### 3. Repair and recovery (25m)
Review the smallest sufficient change, run relevant regression and integration checks, and verify the original symptom is gone. Record what prevented earlier detection and which runbook or check needs to change.

## Instructor Demonstration Plan (45m)
In a disposable copy of the chosen classroom project, introduce a duplicate-write error-handling regression so a duplicate crashes rather than returning the contract response. Show a sanitized trace, state two hypotheses, run a focused failing test, restore correct transaction handling, and independently confirm both the regression and ordinary writes.

## Student Practice and Review (60m)
Form responder/observer pairs (10m), investigate a prepared fault (35m), then compare hypotheses and recovery evidence (15m).

## Misconception to Address
A failing test does not by itself prove the agent hallucinated. The cause may be a bad requirement, a changed dependency, an environment error, or a code defect; require evidence before attribution.

## Connection to the Next Stage
Week 10 uses incident and earlier workflow evidence to test a specific improvement.

## Further Reading
[FastAPI error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)
