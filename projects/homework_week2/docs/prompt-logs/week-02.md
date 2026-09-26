# Week 2 prompt log: Task Board CLI

- **Date:** 2026-09-25
- **Agent:** Claude Code (Claude Opus 5.5), desktop app
- **Branch:** `week-02` on `alexmekhail/cap`, project in `projects/homework_week2/`

All command output quoted below comes from real runs in this session. Items marked
`TODO (Alex):` are my own judgment or reflection, and I'll fill them in myself.

---

## 1. Goal and Acceptance Criteria

**Goal:** build a small command-line Kanban board (`board`) with Typer and SQLite,
test-first, with the process documented well enough to be graded.

The acceptance criteria are in [`docs/spec.md`](../spec.md) and are written as command plus
expected output and exit code:
- **AC-1 to AC-23:** written in Phase 1.
  - Adding and listing: AC-1 to AC-7.
  - Moving, editing, deleting: AC-8 to AC-12.
  - Filters: AC-13 to AC-15.
  - Errors: AC-16 to AC-22 (empty title, bad priority, malformed date, impossible date, unknown column, missing ID, no tracebacks).
  - Database location: AC-23.
- **AC-24 to AC-26:** added after Phase 3 with Alex's approval. They cover an unusable DB path, all-or-nothing edits, and the filtered list layout.

**Setup decisions made before any code:**
- **`uv` wasn't installed** (`command not found`), so Alex chose **pip + venv**. The validation commands became `.venv/bin/pytest`, `.venv/bin/ruff check .` and `.venv/bin/ruff format --check .`.
- **Repo location:** `projects/homework_week2` was already inside the `cap` repo, so a separate `git init` would have nested one repo inside another. Alex chose a `week-02` branch of `cap` instead of a new `taskboard-cli` repo.
- **PR target:** Alex's fork, `alexmekhail/cap`, rather than `mageeb/cap`.
- **Past due dates** are allowed. That's how overdue tasks can exist.
- **Tool versions:** Python 3.13.7, typer 0.27.2, pytest 9.1.1, ruff 0.16.9. This Typer version no longer depends on Click, so I tested `CliRunner`, `typer.confirm` and stderr capture in a scratch script before relying on them.

## 2. Context and Architecture

| File | Responsibility |
|---|---|
| `models.py` | `Task`, `Priority`/`Column` enums, validation, the overdue rule, filters. Pure, no I/O. |
| `db.py` | Path resolution (`TASKBOARD_DB` or `~/.taskboard/tasks.db`), the `connect()` context manager, and parameterized queries. |
| `cli.py` | Typer commands only. Domain errors (`TaskboardError`) become `Error: ...` on stderr with exit code 1. |

**Decision: SQLite instead of a JSON file.**
- **Why SQLite:** writes are transactional, and `AUTOINCREMENT` IDs are never reused after a delete. A test checks this: after deleting task 2, the next task gets ID 3. Updates are single-row `UPDATE`s, and it needs no extra dependency.
- **Tradeoff:** the data file is binary, so you can't read or diff it by hand, and changing the schema later would need a migration. A JSON file would be easier to inspect, but it has to be rewritten in full on every change and can be corrupted by a crash partway through a write.

**A smaller decision:** filters (`--search` especially) run in Python rather than as SQL
`LIKE`. `LIKE` treats `%` and `_` in the search text as wildcards and only ignores case
for ASCII letters. There's a test that searching for `50%` matches nothing. The cost
is loading every task before filtering.

## 3. Validation and Findings

### Baseline vs. final

| Point | pytest | ruff check | ruff format --check |
|---|---|---|---|
| Phase 1 scaffold | `collected 0 items`, exit 5 (no tests yet) | All checks passed! | 6 files already formatted |
| After `add`+`list` | 52 passed | All checks passed! | 13 files already formatted |
| After `move` | 70 passed | All checks passed! | 14 files already formatted |
| After `edit` | 84 passed | All checks passed! | 15 files already formatted |
| After `delete` | 94 passed | All checks passed! | 16 files already formatted |
| After filters | 112 passed | All checks passed! | 17 files already formatted |
| After Phase 3 fix | 118 passed | All checks passed! | 18 files already formatted |
| **Final** | **120 passed** | **All checks passed!** | **18 files already formatted** |

Final run (2026-09-25 18:21):
```
$ .venv/bin/pytest
============================= 120 passed in 0.80s ==============================
$ .venv/bin/ruff check .
All checks passed!
$ .venv/bin/ruff format --check .
18 files already formatted
```
Tests per file: test_models 46, test_cli_add_list 21, test_db 12, test_cli_edit 9,
test_cli_list_filters 9, test_cli_move 8, test_negative_db_path 8, test_cli_delete 7.

I also ran the README setup steps in a fresh venv (`python3 -m venv` + `pip install -e ".[dev]"`),
and `board add` worked (exit 0).

### Phase 3: negative test (before and after)

**Assumption challenged:** AC-22 says the user never sees a Python traceback. Every test
up to that point had used a valid, writable DB path. The suggested cases (impossible
date, whitespace title, filters with no results) already had tests from Phase 2
(AC-19, AC-16, AC-15), so I tested an unusable `TASKBOARD_DB` instead: a directory, a
non-SQLite file, and a path whose parent is a regular file. The test in
`tests/test_negative_db_path.py` runs the real `board` script as a subprocess, because
`CliRunner` catches unhandled exceptions and would hide the traceback.

**Before the fix:** `6 failed`. The real output of `board list` was a 36-line Rich traceback:
```
╭───────────────────── Traceback (most recent call last) ──────────────────────╮
│ .../src/taskboard/cli.py:81 in list_                                         │
...
DatabaseError: file is not a database
```
The other cases ended in `OperationalError: unable to open database file` and
`FileExistsError: [Errno 17] File exists: '.../plain-file'`.

**Fix:** `db.py` now wraps the mkdir, connect and schema steps (not the queries that
follow) in `StorageError(TaskboardError)`.

**After the fix:** `6 passed`, and 118 passed overall.
```
$ TASKBOARD_DB=<scratch>/neg/notes.txt board list
Error: Cannot open task database at <scratch>/neg/notes.txt: file is not a database.
exit=1
```

**Follow-up, approved by Alex:** the parent-is-a-file case said `File exists.`, which is
misleading. I added a test first. It failed at depth 1 (`- Not a directory.` / `+ File exists.`),
while depth 2 already passed because `mkdir` raises `NotADirectoryError` there. After I mapped
`FileExistsError` to "Not a directory", it went to 8/8 passing and 120 overall.

## 4. Agent Recovery and Human Intervention

**Things the agent caught and corrected itself:**
1. **Connections were never closed.** Using a `sqlite3.Connection` as a context manager
   commits but doesn't close. Running `pytest -W error::ResourceWarning` showed
   `52 passed, 36 warnings`. `db.connect()` became a `@contextmanager` that
   commits, or rolls back on error, and always closes. After that: `52 passed`, no warnings.
2. **A test asserted too much.** `test_ac3_add_trims_title` checked exact spacing
   (`"#1  Buy milk "`), but the spec says `list` spacing may vary. The test now
   checks the stored title in the DB, which is a stronger check of what AC-3 means.
3. **Import errors were hiding failures.** In skill uses #1 and #2, tests failed at
   collection with `ImportError` / `ModuleNotFoundError`, which hid every other test.
   I added stubs that raise `NotImplementedError`, giving per-test failures
   (52 failed, then 16 failed).
4. **Two tests passed before `move` existed:**
   - `test_ac22` passed because "No such command" also exits 2.
   - `test_ac6[done]` passed because the move silently failed and "no OVERDUE" held trivially.

   Both were tightened, then all 8 `move` CLI tests failed before being implemented.
5. **Ruff findings:** I001 import order (twice, auto-fixed) and E501 on one test docstring (rewrapped by hand).
6. **Unrelated commit in the PR base.** `fork/main` was one commit behind local `main`. The extra commit was
   `d168cae` (checkers game), which lives on `fork/add-checkers-game`. I rebased `week-02`
   onto `fork/main` so the PR contains only this project. That rewrote the commit hashes,
   and the hashes below are the post-rebase ones.

**Where Alex intervened:**
- Chose pip/venv over `uv`, a `week-02` branch of `cap` over a new repo, and the fork as the PR target.
- Approved the skill edits after the first two uses.
- Approved AC-24 to AC-26 and the "Not a directory" message after Phase 3.
- TODO (Alex): note any other points where you stepped in, redirected the agent, or rejected something, and why.

## 5. Outcome and Limits

**Outcome:** all five commands and the filters work end to end, and data persists
across processes. A subprocess test runs `board add` and then `board list` as separate processes.
There are 26 acceptance criteria and 120 passing tests, and ruff lint and format are clean.

Commits on `week-02` (post-rebase):
```
e0de15b Scaffold Task Board CLI: spec, CLAUDE.md, add-cli-command skill
0d48742 Add add and list commands (AC-1..AC-7, AC-16..AC-19, AC-23)
889bc71 Add move command (AC-8, AC-20, AC-21, AC-22; completes AC-5, AC-6)
c226c53 Refine add-cli-command skill after first two uses
07998eb Add edit command (AC-9, AC-10, AC-16..AC-19, AC-21)
456ce7a Add delete command with confirmation (AC-11, AC-12, AC-21)
adf26e4 Add list filters: --column, --priority, --search (AC-13..AC-15, AC-17, AC-20)
ee51bae Show a clean error when TASKBOARD_DB is unusable (AC-22)
aa30696 Add AC-24..AC-26 to spec; report "Not a directory" for file parents
```
The commit that adds this log and the README comes after these.

**Limits** (see also the README):
- You can't clear a due date once it's set.
- There are no schema migrations.
- Overdue uses the local date.
- `list` loads every task.
- Long titles break the column alignment.
- Only tested on macOS with Python 3.13.
- A valid SQLite file with a different `tasks` schema isn't detected.

---

## Week 1 vs. Week 2

| | Week 1 | Week 2 |
|---|---|---|
| Scope | Environment setup only | A working CLI app with persistence |
| Spec | None | `docs/spec.md` with 26 numbered, observable ACs |
| Tests | None | 120 pytest tests, written before the code they cover |
| Agent instructions | None | `CLAUDE.md` with file ownership, conventions, validation commands and boundaries |
| Reusable procedure | None | `add-cli-command` skill, used 5 times and revised once from evidence |
| Evidence | — | Failing and passing output for each cycle, plus a real before/after for the negative test |

TODO (Alex): your reflection on how having a spec, tests, and project instructions changed
the way you worked with the agent compared to Week 1.

## Changed function explanation

TODO (Alex): write this yourself. Good candidates:
1. **`db._open()` / `db.connect()`** (`src/taskboard/db.py`). Changed twice: first to always close connections, then in Phase 3 to turn open failures into `StorageError`. It shows why the wrapper covers opening but not the queries that follow.
2. **`models.parse_due()`** (`src/taskboard/models.py`). It uses a strict regex plus `date.fromisoformat`, because `fromisoformat` on 3.11+ also accepts `20261001` and `2026-W40-4`, which the spec doesn't allow.
3. **`db.update_task()`** (`src/taskboard/db.py`). It uses `COALESCE(?, column)` with parameterized SQL so that options you don't pass stay unchanged (AC-9).

## What I trusted, checked, and corrected

TODO (Alex): what you accepted from the agent without checking, what you verified yourself (for
example, running `board` by hand or reading the tests), and what you pushed back on.

## Skill usage log (`.claude/skills/add-cli-command/SKILL.md`)

| # | Command | ACs | Failing first | Passing after | What the skill helped with or missed |
|---|---|---|---|---|---|
| 1 | `add` + `list` | AC-1 to 7, 16 to 19, 23 | Collection error, then 52 failed after stubs | 52 passed | Helped: saving the failing output exposed that a collection error was hiding the CLI tests. Missed: no guidance for testing code that doesn't exist yet. |
| 2 | `move` | AC-8, 20 to 22 (+5, 6) | Collection error, then 16 failed / 54 passed. 2 tests passed without `move` existing. | 70 passed | Helped: checking the failing output caught 2 tests passing for the wrong reason. Missed: nothing warned about tests passing before the code existed. |
| — | *Skill revised* | | | | Approved by Alex: stubs first, "explain or tighten any test that passes early", assert content rather than spacing, `ruff check --fix` in step 6. |
| 3 | `edit` | AC-9, 10, 16 to 19, 21 | 14 failed, 70 passed | 84 passed | The stubs step worked: no collection error and no early passes. |
| 4 | `delete` | AC-11, 12, 21 | 10 failed, 84 passed | 94 passed | Worked as written. The manual run also checked that deleting a deleted task fails cleanly and that IDs aren't reused. |
| 5 | `list` filters | AC-13 to 15, 17, 20 | 18 failed, 94 passed | 112 passed | Missed: `--fix` doesn't handle E501, so one docstring needed rewrapping by hand. The spec was silent on filtered layout, which later became AC-26. |
