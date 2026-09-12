# Week 4: Orchestration — Building and Using Harnesses

## Learning Goals
Use a harness to build a difficult application on the loop. Explain agent responsibilities, connections, context boundaries, coordination, and final verification. Students need not build a production orchestrator from scratch.

## Core Instruction (75m)
- **Control modes (15m):** Compare Week 2's in-the-loop work with Week 3's on-the-loop supervision. With multiple agents, someone must still own goals, acceptance, and integration.
- **What makes a useful agent (20m):** Define purpose, inputs, outputs, tools, context, permissions, acceptance criteria, failure reporting, and stop conditions. A persona is a useful perspective, not an operational contract.
- **Three harness designs (25m):** Script-driven stages connected through artifacts; an instruction-driven workflow governed by a detailed playbook; a hybrid supervisor that generates bounded coordination code and remains in control. Compare inspectability, flexibility, and failure modes.
- **Connections and coordination (15m):** Task dependencies, file/workspace ownership, handoff contracts, bounded retries, integration, and independent review. Parallelize only work with clean boundaries.

## Instructor Demonstration Plan (45m)
### Preparation
Bring **one working, rehearsed orchestrator setup** using your existing agent access. Gas Town may be selected after rehearsal, but no named orchestrator is mandatory. Record the exact tool/version, account requirements, invocation commands, and known limits in the demo repository before class. Do not assume a subscription automatically covers every adapter or concurrent run.

Use a small shared task: add color selection and saved tool preferences to a minimal drawing app. Prepare a baseline app and checks, a working result, and an integration-mismatch checkpoint. Keep all references in GitHub and disclose prepared results. The course does not yet pin a specific orchestrator or provider adapter; these are instructor preparation requirements.

### 1. Frame the Roles (5m)
Show the running orchestrator and define a UI worker, persistence worker, and integrator/reviewer. Agree the preference schema first. Assign non-overlapping files. Explain why both workers must use the same contract.

### 2. Script-driven Harness (12m)
Ask AI to create a few simple Python scripts connected through files or JSON:

```text
Generate a small coordinator with plan.py, dispatch.py, verify.py, and report.py.
Use an explicit task JSON schema, dependency IDs, owned paths, and output artifacts.
Dispatch through the existing agent adapter I supply; do not invent its API.
Use subprocess argument arrays, checked exit codes, per-task timeouts, and bounded retries.
Stop if a worker output is missing, invalid, or contradicts the agreed interface.
Do not execute generated code until I have inspected it.
```

Inspect the generated code and connect it to the rehearsed adapter. Run a bounded task through the stages and show an artifact moving between them. Show the actual agent invocation and its result.

### 3. Instruction-driven Harness (10m)
Use the same app, role contracts, and checks with the [workflow playbook](reference.md#reusable-workflow-playbook). Ask the orchestrator to plan, assign, require evidence, and integrate according to that document. Show which decisions moved from Python into instructions. Verify actual execution; a narrative saying “the reviewer approved” is not evidence that review ran.

### 4. Hybrid Harness (12m)
Keep a supervisor agent responsible for the goal. Ask it to generate a small helper that dispatches ready tasks and collects reports, using the same known adapter. Review and run that helper. Return results to the supervisor for the next decision; do not let the helper silently redefine the task or acceptance tests.

Introduce a prepared schema mismatch, such as one worker returning `colour` where the agreed interface uses `color`. Show the integration check rejecting it and the supervisor routing a correction. Label this as a prepared failure case.

### 5. Compare and Debrief (6m)
Where was control located? What was mechanically enforced? What depended on instructions? Which evidence justified acceptance? When would one agent have been simpler? Point students to the open-ended homework: use a harness, demonstrate coordination, and defend the integrated result.

## Student Workshop (60m)
Choose a hard application and write acceptance criteria (15m); define roles, task dependencies, and handoffs (15m); run a small harness-driven slice and inspect the result (20m); defend the control choices (10m).

## Homework
Use [homework.md](homework.md) for the open-ended build and assessment. Week 4 is a substantial project, but continuation into Week 5 is optional.
