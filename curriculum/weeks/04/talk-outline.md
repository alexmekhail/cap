# Week 4: Orchestration — Building and Using Harnesses

## Learning Goals
Use a harness to build a difficult application on the loop. Explain agent responsibilities, connections, context boundaries, coordination, and final verification. Students need not build a production orchestrator from scratch.

## Core Instruction (75m)
- **Control modes (15m):** Compare Week 2's in-the-loop work with Week 3's on-the-loop supervision. With multiple agents, someone must still own goals, acceptance, and integration.
- **What makes a useful agent (20m):** Define purpose, inputs, outputs, tools, context, permissions, acceptance criteria, failure reporting, and stop conditions. A persona is a useful perspective, not an operational contract.
- **Three harness designs (25m):** Script-driven stages connected through artifacts; an instruction-driven workflow governed by a detailed playbook; a hybrid supervisor that generates bounded coordination code and remains in control. Compare inspectability, flexibility, and failure modes.
- **Connections and coordination (15m):** Task dependencies, file/workspace ownership, handoff contracts, bounded retries, integration, and independent review. Parallelize only work with clean boundaries.

## Instructor Demonstration (45m)
Bring one rehearsed orchestrator setup. Gas Town is an optional candidate, not a student requirement. Use the [demo guide](instructor-demo.md) to show how AI helps create a simple Python-script pipeline, how the same task works under a detailed workflow instruction, and how a supervising agent can generate coordination code while retaining control. Show a real or clearly labeled prepared integration failure.

## Student Workshop (60m)
Choose a hard application and write acceptance criteria (15m); define roles, task dependencies, and handoffs (15m); run a small harness-driven slice and inspect the result (20m); defend the control choices (10m).

## Homework
Use [homework.md](homework.md) for the open-ended build and assessment. Week 4 is a substantial project, but continuation into Week 5 is optional.
