# Week 3 Reference: Sustained Single-Agent Work

## Terminal Preparation
Use your own agent's documented terminal entry point. Confirm the current repository/branch, installation requirements, relevant baseline checks, and usage limits. VS Code remains useful for inspecting diffs; one agent performs the sustained task.

## Context Map Template
- Goal and chosen feature track.
- Repository base commit and setup/check commands.
- Relevant files and symbols, with evidence for each claim.
- State ownership, key interfaces, persistence boundaries, and architectural decisions.
- Known baseline failures and unresolved questions.

Keep the map concise and update it after discoveries. Reference files the agent can inspect; do not copy the full repository into it.

## Skill Example: Trace and Verify a Change
**Input:** feature request, repository map, and baseline.
1. Locate the entry interaction and trace state changes through persistence/rendering.
2. Cite actual files and symbols; mark guesses explicitly.
3. Identify likely change boundaries and existing tests.
4. Propose a bounded implementation order and acceptance checks.
5. After implementation, run checks and inspect unintended changes.
**Output:** verified map, plan, changed boundaries, evidence, and unresolved risks.

Use the packaging supported by your chosen agent, or explicitly ask it to read this procedure. A file's name alone does not guarantee discovery.

## Checkpoint/Resume Brief
```text
Goal and acceptance criteria:
Current branch/commit:
Completed changes:
Checks actually run and results:
Known failures and open questions:
Relevant files and decisions:
Next bounded action:
Retry/time budget and stop conditions:
```

## Supervision
In the loop: decide between small implementation steps. On the loop: let agreed work proceed between checkpoints, inspect evidence, and intervene for repeated failures, weakened tests, destructive changes, or scope drift. Neither mode removes responsibility for review. Preserve a checkpoint before switching context; a handoff without current evidence is incomplete.

The [homework](homework.md) offers tabs or comments. Read source documentation from the exact checkout, not remembered paths from an older release.
