# Instructor Demo: A Check That Catches a Real Failure

## Preparation
Copy `demo/seed.py`, `demo/test_seed.py`, and `demo/pyproject.toml` into a fresh disposable directory. Keep `instructor_solution.py` outside the agent's workspace. This fixture uses Python's standard library and in-memory SQLite; no API keys or running services are needed. Install Ruff in the demo environment before class and record the Python/Ruff versions used in rehearsal.

Run these commands in the disposable directory:

```sh
python3 -m unittest -v
ruff check .
```

The starter intentionally fails the acceptance suite. The tests exercise requested row counts, uniqueness, repeatable seeding, and invalid input. The lint configuration is supplied, rather than merely mentioned in the narration.

## 1. Establish the Contract
Read `test_seed.py` with students. Predict the failures before running it. Explain why a count check alone would not establish safe repeatability or input handling.

Create the chosen agent's instruction file or explicitly supply these instructions:

```text
Implement seed_users(connection, count) against the supplied acceptance tests.
Use Python standard library and SQLite. Modify only seed.py.
Do not change acceptance tests or lint configuration.
Run python3 -m unittest -v and ruff check . after changes.
Stop after three unsuccessful correction attempts and summarize the evidence.
Stop and ask before changing scope or adding dependencies.
```

## 2. Observe the Baseline
Run the tests and explain the actual failures. Show that the starter inserts one user regardless of the requested count. The repeat run also violates the unique constraint. These are deliberate fixture defects, not predictions about what an AI will do.

## 3. Supervise Recovery
Ask the agent to fix the implementation under the supplied contract. Observe its real actions. Let it correct failures within the agreed scope; intervene if it weakens tests or expands scope. If it succeeds immediately, review why the checks are useful without inventing extra iterations.

## 4. Review the Result
Re-run both commands yourself and inspect the diff. Check parameterized SQL, input validation before writes, unique values, and repeatable seeding. As a demonstration of the checks' sensitivity, substitute the original starter in the disposable directory and show the tests fail again; restore the reviewed implementation afterward.

If the live agent or environment fails, use the instructor reference as a clearly labeled fallback and run the same checks. Do not present it as live-generated work.

## Transfer to the Capstone
This short fixture teaches the control loop, not the full application. Students apply it to FastAPI/SQLAlchemy, API failure cases, relational integrity, and Alembic migrations. Add API and migration checks before delegating those parts. Set budgets and review boundaries; instructions alone do not enforce them.
