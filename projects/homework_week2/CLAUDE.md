# CLAUDE.md: Task Board CLI

## Purpose
`board` is a command-line Kanban task board: Typer for the CLI, stdlib `sqlite3` for
storage. This is a class assignment, and the process evidence is graded alongside the
code. `docs/spec.md` is the source of truth for behavior, and every change should
trace back to its acceptance criteria (AC-n).

## Key files and what each owns
| Path | Owns |
|------|------|
| `src/taskboard/models.py` | `Task` dataclass, `Priority`/`Column` values, all input validation (title, priority, date, column) and the overdue rule. Pure functions with no I/O. |
| `src/taskboard/db.py` | DB path resolution (`TASKBOARD_DB`, falling back to `~/.taskboard/tasks.db`), connection, schema, and all queries. |
| `src/taskboard/cli.py` | Typer commands only: parse args, call models/db, format and print output, and map domain errors to `Error: ...` on stderr with exit code 1. |
| `tests/` | pytest. CLI tests use `typer.testing.CliRunner` with `TASKBOARD_DB` pointed at `tmp_path`. Unit tests cover models/db directly. |
| `docs/spec.md` | Behavior spec and acceptance criteria. |
| `docs/prompt-logs/week-02.md` | Session log for the assignment. |
| `.claude/skills/add-cli-command/SKILL.md` | The procedure to follow when adding or changing any CLI command. |

## Conventions
- Type hints on every function signature. Keep functions small and single-purpose.
- **Parameterized SQL only** (`?` placeholders). Never build SQL from user input with f-strings or `%`.
- **No business logic in `cli.py`.** Validation and rules live in `models.py`, and persistence lives in `db.py`.
- Domain errors are raised as `TaskboardError` subclasses. Only `cli.py` turns them into messages and exit codes. No tracebacks reach the user.
- Error message text must match `docs/spec.md` exactly.
- Tests never touch `~/.taskboard`. They always set `TASKBOARD_DB` to a temp path.
- Anything date-dependent (overdue) takes `today` as a parameter so tests can control it.
- Follow `.claude/skills/add-cli-command/SKILL.md` for every command: write failing tests first.

## Setup (macOS, pip + venv)
```bash
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

## Validation commands (run all three before every commit)
```bash
.venv/bin/pytest
.venv/bin/ruff check .
.venv/bin/ruff format --check .
```

## Boundaries
- Don't create, modify, or delete files outside `projects/homework_week2/`. The exception is the git operations needed to commit and push on the `week-02` branch.
- Don't add dependencies beyond `typer`, `pytest`, and `ruff` without asking. `setuptools` is used only as the build backend.
- Don't weaken, skip, or delete tests to make them pass. If a test is wrong, say so and explain why before changing it.
- Don't change acceptance criteria in `docs/spec.md` without Alex's approval.
- Don't fabricate evidence. Command output in logs and PRs must come from real runs.
- Stop at each phase checkpoint for review.
