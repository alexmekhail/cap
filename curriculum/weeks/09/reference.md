# Week 9 Student Reference

## Working Principle
Use evidence to diagnose a failure, write a regression check, and verify recovery while keeping the exercise isolated from real users and data.

## Concepts to Apply
### Observe before fixing
Record the symptom, scope, timeline, and last known good version. Separate user-visible impact from a suspected cause. Sanitize logs before sharing them with an agent; preserve useful timestamps and request identifiers.

### Hypothesis and reproduction
Ask the agent for competing explanations and a check that distinguishes them. Use a deterministic fixture rather than hoping an intermittent fault appears. Write a regression test that fails before the fix.

### Repair and recovery
Review the smallest sufficient change, run relevant regression and integration checks, and verify the original symptom is gone. Record what prevented earlier detection and which runbook or check needs to change.

## Decision Record
For the week's main decision, record: the problem, evidence, chosen approach, rejected alternative, check performed, and remaining limitation. Link to actual code or artifacts rather than relying on a transcript alone.

## Watch for This Mistake
A failing test does not by itself prove the agent hallucinated. The cause may be a bad requirement, a changed dependency, an environment error, or a code defect; require evidence before attribution.

## Primary References
[FastAPI error handling](https://fastapi.tiangolo.com/tutorial/handling-errors/)

Read documentation for the version/service you actually use. These references support the concepts; exact environment setup must be recorded in your repository.

## Assignment
[Homework and submission requirements](homework.md). The production reference is [here](../../../infrastructure/template/README.md).
