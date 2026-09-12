# Harness Artifact-Flow Reference

This executable Python example demonstrates dependency order, explicit ownership, adapter invocation, failure handling, and handoff validation. The supplied worker is a **deterministic replay**, not an LLM. It does not build an application. This is the account-free fallback and the starting point for the instructor's live adapter.

From this directory:

```sh
python3 plan.py > plan.json
python3 dispatch.py python3 replay_worker.py < plan.json > results.json
python3 verify.py < results.json
python3 -m unittest -v
```

Pass `--mismatch` after `replay_worker.py` to produce a conflicting handoff; verification must fail. Files are explicit checkpoints, so a failed stage cannot be mistaken for a successful end-to-end run. The tests also exercise missing dependencies, conflicting ownership, failed workers, and invalid task IDs.

## Live Adapter Contract
Replace the replay command with an instructor-reviewed adapter for the actual agent. It receives one JSON object on stdin containing `task`, `contract`, and dependency `handoffs`; it must emit a single JSON result with matching `task_id`, `status`, interface fields, and evidence. Keep progress diagnostics on stderr. Record tool/version, command, credentials mechanism, usage budget, and what happens on timeout. Do not put credentials in task JSON or source.

The coordinator checks declared ownership; it does not sandbox a live agent or enforce filesystem permissions. Use separate workspaces or tool permissions for real workers, and independently run application acceptance tests before claiming completion. A handoff schema check only validates the schema.

## Three Classroom Uses
- Script-driven: run the explicit stages and inspect their artifacts.
- Instruction-driven: have the chosen orchestrator follow the equivalent playbook in the weekly reference and compare actual evidence.
- Hybrid: let the supervisor propose a change to the coordinator, review it before execution, run these checks, and return results to the supervisor for the next decision.

The instruction-driven and hybrid live runs require the chosen agent/orchestrator setup; the replay does not substitute for student homework execution.
