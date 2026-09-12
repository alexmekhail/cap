# Week 4 Demo: Three Ways to Coordinate Agents (45m)

## Before Class
Bring **one working, rehearsed orchestrator setup** using your existing agent access. Gas Town may be selected after rehearsal, but no named orchestrator is mandatory. Record the exact tool/version, account requirements, invocation commands, and known limits in the demo repository before class. Do not assume a subscription automatically covers every adapter or concurrent run.

Use a small shared task: add color selection and saved tool preferences to a minimal drawing app. Prepare a baseline app and checks, a working result, and an integration-mismatch checkpoint. Keep all references in GitHub and disclose prepared results. The course does not yet pin a specific orchestrator or provider adapter; these are instructor preparation requirements.

## 1. Frame the Roles (5m)
Show the running orchestrator and define a UI worker, persistence worker, and integrator/reviewer. Agree the preference schema first. Assign non-overlapping files. Explain why both workers must use the same contract.

## 2. Script-driven Harness (12m)
Ask AI to create a few simple Python scripts connected through files or JSON:

```text
Generate a small coordinator with plan.py, dispatch.py, verify.py, and report.py.
Use an explicit task JSON schema, dependency IDs, owned paths, and output artifacts.
Dispatch through the existing agent adapter I supply; do not invent its API.
Use subprocess argument arrays, checked exit codes, per-task timeouts, and bounded retries.
Stop if a worker output is missing, invalid, or contradicts the agreed interface.
Do not execute generated code until I have inspected it.
```

Inspect the generated code and connect it to the rehearsed adapter. Run a bounded task through the stages and show an artifact moving between them. Explain the difference between a real agent invocation and a deterministic replay used as fallback.

## 3. Instruction-driven Harness (10m)
Use the same app, role contracts, and checks with the playbook in `reference.md`. Ask the orchestrator to plan, assign, require evidence, and integrate according to that document. Show which decisions moved from Python into instructions. Verify actual execution; a narrative saying “the reviewer approved” is not evidence that review ran.

## 4. Hybrid Harness (12m)
Keep a supervisor agent responsible for the goal. Ask it to generate a small helper that dispatches ready tasks and collects reports, using the same known adapter. Review and run that helper. Return results to the supervisor for the next decision; do not let the helper silently redefine the task or acceptance tests.

Introduce a prepared schema mismatch, such as one worker returning `colour` where the agreed interface uses `color`. Show the integration check rejecting it and the supervisor routing a correction. If demonstrated through replay, label it clearly.

## 5. Compare and Debrief (6m)
Where was control located? What was mechanically enforced? What depended on instructions? Which evidence justified acceptance? When would one agent have been simpler? Point students to the open-ended homework: use a harness, demonstrate coordination, and defend the integrated result.

## Fallback
Show the published checkpoints and artifact flow if live tooling fails. Never imply a replay was live agent work. Students may adapt the provided setup, but their submissions must show their own execution and verification evidence.
