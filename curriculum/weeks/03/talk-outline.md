# Week 3: One Sustained Agent in the Terminal

## Learning Goals
Set up and supervise one agent over a substantial task. Students deliberately gather context, maintain project instructions and skills, define acceptance checks, and resume work from evidence-backed checkpoints. Excalidraw is the homework, not the classroom demo.

## Core Instruction (75m)
- **Terminal operating setup (15m):** Work in a repository/branch, establish baseline checks, record tool access and commands, and inspect changes from VS Code when useful.
- **Context for a large repository (20m):** Ask the agent to discover relevant files and verify its map. Record interfaces and decisions in concise project context; use skills for recurring exploration and validation. Avoid assuming the entire repository fits or that more pasted text is always better.
- **In the loop to on the loop (20m):** Establish a goal, constraints, acceptance checks, retry/time limits, and checkpoints. Supervise a single agent without approving every micro-step; stop for unexplained failures or scope changes.
- **Sustained execution (20m):** Plan → implement → check → report → continue. Demonstrate a resume brief with current state, completed checks, unresolved questions, and the next task. A longer run is justified by the work, not a duration quota.

## Exercise Preparation
Copy [seed.py](demo/seed.py), [test_seed.py](demo/test_seed.py), and [pyproject.toml](demo/pyproject.toml) to a disposable repository. Python and in-memory SQLite suffice for the tests; install Ruff in the chosen demo environment before class. The [instructor solution](demo/instructor_solution.py) is available for comparison after attempting the exercise. Record tool versions and rehearse commands before teaching.

```sh
python3 -m unittest -v
ruff check .
```

The starter intentionally inserts only one row and mishandles repeat/invalid requests. Four acceptance checks expose row count, uniqueness, idempotence, and invalid-input behavior. Keep a baseline commit, a verified reference checkpoint, and screenshots/recording as fallback.

## Instructor Demonstration Plan (45m)
1. **Baseline (5m):** Run checks and inspect the failures before invoking the terminal agent.
2. **Context and skill (10m):** Reuse [Week 2’s validation procedure](../02/reference.md#reusable-skill-validate-a-small-change), add a repository map, and write the current task contract.
3. **Supervised execution (15m):** Ask one agent to implement `seed_users(connection, count)`, modifying only `seed.py`, retaining tests and lint settings, and running checks after changes. Stop after three unsuccessful corrections or ten minutes and report evidence. Observe actual behavior rather than scripting a hallucination.
4. **Checkpoint/resume (10m):** Have it write completed work, changed files, checks/results, unresolved issues, and next action. Resume from that brief. Explain how this pattern supports a larger work session; show a clearly labeled prepared longer-task checkpoint if available.
5. **Independent review (5m):** Run checks yourself, inspect the diff, and discuss when intervention was justified. Demonstrate that substituting the starter makes the tests fail again.

## Student Hands-on (30m)
- 0–5m: copy fixture, create branch, and capture baseline.
- 5–10m: write instructions, acceptance criteria, and limits.
- 10–20m: supervise one terminal agent fixing the implementation.
- 20–25m: write and use a checkpoint/resume brief.
- 25–30m: independently run checks and explain one decision to a peer.

If tooling is unavailable, students inspect the disclosed reference and compare it to the failing starter, recording that fallback honestly. This does not replace the sustained-agent evidence required in homework.

## Debrief and Homework (30m)
Compare interventions and checkpoints (15m), then explain the Excalidraw feature choices and help students identify their initial mapping questions (15m). Homework scope, evidence, and grading are in [homework.md](homework.md).

Use the [context map and checkpoint templates](reference.md) for the exercise and homework.
