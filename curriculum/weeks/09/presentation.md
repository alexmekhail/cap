---
marp: true
theme: default
paginate: true
---

# Incident Response and Regression Repair

Use evidence to diagnose a failure, write a regression check, and verify recovery while keeping the exercise isolated from real users and data.

---

# Observe before fixing

Record the symptom, scope, timeline, and last known good version. Separate user-visible impact from a suspected cause. Sanitize logs before sharing them with an agent; preserve useful timestamps and request identifiers.

---

# Hypothesis and reproduction

Ask the agent for competing explanations and a check that distinguishes them. Use a deterministic fixture rather than hoping an intermittent fault appears. Write a regression test that fails before the fix.

---

# Repair and recovery

Review the smallest sufficient change, run relevant regression and integration checks, and verify the original symptom is gone. Record what prevented earlier detection and which runbook or check needs to change.

---

# Demonstrate and Defend

A reproduced incident, evidence-backed diagnosis, failing regression test, verified fix, and short incident report.

---

# Homework

Inject one controlled defect into a disposable branch or test environment: a serialization mismatch, duplicate-write failure, or query-count regression. Diagnose it with AI assistance, protect the fix with a regression check, and explain recovery.
5–10 hours. Required criteria and evidence: homework.md.

---

# What Comes Next

Week 10 uses incident and earlier workflow evidence to test a specific improvement.
