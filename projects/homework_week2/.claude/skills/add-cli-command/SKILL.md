---
name: add-cli-command
description: Procedure for adding or changing a `board` CLI command test-first, with validation and evidence. Use for any new command, new option, or change to command behavior in the Task Board CLI.
---

# Add or change a CLI command

## Inputs (write these down before starting)
1. **Command name**, for example `move`.
2. **Arguments and options**, with types and defaults, for example `<id:int> <column:str>`.
3. **AC IDs** from `docs/spec.md` that this change satisfies, for example AC-8, AC-20, AC-21.
4. **Error cases**: each invalid input, with its exact `Error: ...` message and exit code.

If an input can't be traced to an AC, stop and update the spec first (step 1).

## Steps
1. **Spec check.** Read the relevant ACs in `docs/spec.md`. If behavior is missing or ambiguous, propose the spec edit to Alex and wait for approval. Don't change ACs on your own.
2. **Failing tests first.**
   - Add CLI tests in `tests/test_cli_<command>.py` with `CliRunner`, using the shared fixture that sets `TASKBOARD_DB` to `tmp_path`.
   - Cover at least **one happy path** and **one error case** per AC, and name each test after its AC, for example `test_ac8_move_to_in_progress`.
   - Add unit tests in `tests/test_models.py` / `tests/test_db.py` for any new validation or query.
   - Assert the exit code, the exact message, and which stream it went to (stdout or stderr). For errors, also assert that `Traceback` is absent and that the DB is unchanged.
   - Run `.venv/bin/pytest` and **save the failing output**. The tests must fail for the expected reason (missing command or behavior), not because of a typo or import error.
3. **Implement the domain logic** in `models.py`: validation, rules, and `TaskboardError` subclasses.
4. **Implement persistence** in `db.py` with parameterized SQL only.
5. **Wire up the CLI** in `cli.py`: parse, call, print, and map errors. No business logic goes here.
6. **Run all validation commands** and save the output:
   ```bash
   .venv/bin/pytest
   .venv/bin/ruff check .
   .venv/bin/ruff format --check .
   ```
   If formatting fails, run `.venv/bin/ruff format .` and rerun the check.
7. **Run the command manually** against a scratch DB, including one error case:
   ```bash
   export TASKBOARD_DB="$(mktemp -d)/manual.db"
   .venv/bin/board <command> ...
   echo "exit=$?"
   ```
8. **Commit** with a message that names the command and the ACs, for example `Add move command (AC-8, AC-20, AC-21)`.

## Expected evidence (report this back after every use)
- Failing test output from step 2 (the relevant lines).
- Passing test output from step 6 (the summary line).
- `ruff check` and `ruff format --check` output.
- A sample manual run from step 7, with exit codes.
- **Skill note**: one line on what this skill helped with or missed this time. If a step was missing or wrong, propose an edit to this file instead of silently working around it.
