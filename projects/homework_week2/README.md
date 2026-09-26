# Task Board CLI

`board` is a command-line Kanban board for one person. You can add tasks, move them
between three fixed columns (`todo`, `in-progress`, `done`), edit them, delete them, and
filter the board. Tasks are stored in a local SQLite file, so they persist between runs.

- Behavior and acceptance criteria: [docs/spec.md](docs/spec.md)
- Project instructions for the coding agent: [CLAUDE.md](CLAUDE.md)
- Procedure for adding a command: [.claude/skills/add-cli-command/SKILL.md](.claude/skills/add-cli-command/SKILL.md)
- Session log: [docs/prompt-logs/week-02.md](docs/prompt-logs/week-02.md)

## Why Python + Typer + SQLite

- **Python 3.12+:** already set up from Week 1, and `sqlite3` is in the standard library.
- **Typer:** commands are plain functions with type hints, so argument parsing, `--help`,
  and usage errors come for free. `typer.testing.CliRunner` lets tests call commands
  in-process and check stdout, stderr, and exit codes separately.
- **SQLite instead of a JSON file:**
  - Writes are transactional, so a crash can't leave half-written data.
  - IDs come from `AUTOINCREMENT`, so they are never reused after a delete.
  - Updates touch one row instead of rewriting the whole file.
  - It needs no extra dependency.

  The tradeoff: the database is a binary file you can't read or diff by hand,
  and changing the schema later would need a migration.

## Setup (macOS)

This project uses pip and venv. Requires Python 3.12 or newer.

```bash
cd projects/homework_week2
python3 -m venv .venv
.venv/bin/pip install -e ".[dev]"
```

This installs the `board` command at `.venv/bin/board`. Run
`source .venv/bin/activate` to put `board` on your PATH.

## Usage

```
board add "Title" [--priority low|medium|high] [--due YYYY-MM-DD]
board list [--column todo|in-progress|done] [--priority ...] [--search TEXT]
board move <id> <column>
board edit <id> [--title ...] [--priority ...] [--due ...]
board delete <id> [--yes]
```

Tasks are stored in `~/.taskboard/tasks.db` by default. To use a different file, set `TASKBOARD_DB`:

```bash
TASKBOARD_DB=/tmp/scratch.db board list
```

### Example session

This is real output, captured on 2026-09-25:

```
$ board add "Write spec" --priority high --due 2026-10-01
Created task 1: Write spec
$ board add "Buy milk"
Created task 2: Buy milk
$ board add "File taxes" --priority high --due 2026-04-15
Created task 3: File taxes
$ board move 1 in-progress
Moved task 1 to in-progress.
$ board edit 2 --title "Buy oat milk" --priority low
Updated task 2.
$ board list
TODO
  #2   Buy oat milk                   low     due: -
  #3   File taxes                     high    due: 2026-04-15  OVERDUE
IN-PROGRESS
  #1   Write spec                     high    due: 2026-10-01
DONE
  (empty)
$ board list --priority high --search tax
TODO
  #3   File taxes                     high    due: 2026-04-15  OVERDUE
IN-PROGRESS
  (empty)
DONE
  (empty)
$ board delete 2 --yes
Deleted task 2.
$ board add "   "
Error: Title cannot be empty.
```

Errors go to stderr and exit with code `1`. Malformed command syntax, such as a
non-integer ID, gets Typer's usage error and exits with code `2`.

## Checks

```bash
.venv/bin/pytest                    # all tests (they use a temp DB via TASKBOARD_DB)
.venv/bin/ruff check .              # lint
.venv/bin/ruff format --check .     # formatting
```

## Layout

```
src/taskboard/models.py   Task dataclass, Priority/Column, validation, overdue rule, filters
src/taskboard/db.py       DB path, connection, schema, parameterized queries
src/taskboard/cli.py      Typer commands: parse, call, print, map errors to exit codes
tests/                    pytest: unit tests plus CLI tests (CliRunner and subprocess)
```

## Known limitations

- You can't clear a due date once it's set, because `edit --due` only replaces it. This is out of scope in the spec.
- There are no schema migrations. Changing the `tasks` table later would need a manual migration.
- Overdue is based on the machine's local date.
- `list` loads every task and filters in Python. That's fine for a personal board but not for very large ones.
- Long titles (over 30 characters) push the priority and due-date columns out of alignment.
- Tested only on macOS with Python 3.13. Concurrent use from several processes hasn't been tested.
- A database file that is valid SQLite but has a different `tasks` table isn't detected up front.
