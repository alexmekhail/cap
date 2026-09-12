# Week 4 Reference: Agent Contracts and Harness Designs

## In the Loop and On the Loop
In-the-loop work uses human decisions between small steps. On-the-loop work executes within agreed boundaries between checkpoints. Select the mode based on uncertainty and the quality of checks; use human review where the harness cannot establish correctness.

## Agent Contract Template
```text
Role and purpose:
Task and acceptance criteria:
Inputs and source of truth:
Relevant context and skills:
Allowed tools and file/workspace ownership:
Output artifact and recipient:
Checks required before handoff:
Retry/time/usage budget:
Stop/escalation conditions:
```

Example: a persistence worker owns storage code and returns a documented interface, changed files, tests/results, and limitations to the integrator. A UI worker consumes that interface. The reviewer verifies acceptance independently and reports gaps rather than silently rewriting either worker's contract.

## Three Designs
| Design | Who directs execution? | Artifact flow | What to inspect |
|---|---|---|---|
| Script-driven | Python stages with explicit dependencies | Task JSON → worker result → check report → integration | Exit codes, validated inputs/outputs, timeouts, and bounded retries |
| Instruction-driven | Agent/orchestrator following a workflow playbook | Plan → role task → evidence → handoff → review | Whether instructions were followed and evidence actually exists |
| Hybrid | Supervisor agent using reviewed helper code | Goal → generated coordinator → worker results → supervisor decision | Generated code, ownership boundaries, changed plans, and final acceptance |

A harness is the surrounding process, checks, state, and controls that let agents do useful work repeatedly. Scripts alone need a model/tool adapter to invoke a real agent. An instruction document alone does not enforce permission or correctness boundaries.

## Reusable Workflow Playbook
1. Inspect the repository and agree acceptance criteria.
2. Decompose work by dependencies, not by arbitrary agent count.
3. Assign explicit ownership and a shared interface contract.
4. Dispatch ready tasks; record state and limits.
5. Require evidence at handoff. A worker's success claim is not a passed check.
6. Integrate in one designated workspace; handle conflicts explicitly.
7. Independently run acceptance checks and review changes to tests.
8. Stop or revise the plan on unexplained failures; report remaining limits.

## Handoff Template
```text
Task ID and owner:
Input contract/version:
Changed files or commit:
Output and interface:
Checks actually run/results:
Known issues and blocked dependencies:
Requested next action and recipient:
```

## Coordination Checklist
Do agents have enough context to act independently? Can they avoid writing the same files? Who owns the source of truth and integration? What happens when a worker fails or times out? Can the supervisor resume from recorded state? How will you know the final product meets the original specification?
