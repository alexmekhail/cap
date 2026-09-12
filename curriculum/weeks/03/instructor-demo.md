# Week 3 Demo: One Terminal Agent, Verified Checkpoints

## Preparation
Copy `demo/seed.py`, `demo/test_seed.py`, and `demo/pyproject.toml` to a disposable repository. Python and in-memory SQLite suffice for the tests; install Ruff in the chosen demo environment before class. The public `demo/instructor_solution.py` is a disclosed reference, not the exercise output. Record tool versions and rehearse commands before teaching.

```sh
python3 -m unittest -v
ruff check .
```

The starter intentionally inserts only one row and mishandles repeat/invalid requests. Four acceptance checks expose row count, uniqueness, idempotence, and invalid-input behavior. Keep a baseline commit, a verified reference checkpoint, and screenshots/recording as fallback.

## Instructor Demonstration (45m)
1. **Baseline (5m):** Run checks and inspect the failures before invoking the terminal agent.
2. **Context and skill (10m):** Reuse Week 2's validation procedure, add a repository map, and write the current task contract.
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

## Transfer
Excalidraw homework adds context discovery across a large repository and a substantial feature. The classroom fixture demonstrates the control loop; it is deliberately much smaller than that assignment.
