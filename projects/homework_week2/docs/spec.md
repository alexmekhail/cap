# Task Board CLI: Specification

## Purpose

`board` is a small command-line Kanban board for one person. Tasks live in a local
SQLite database, so they persist between runs. Every task sits in exactly one of
three fixed columns: `todo`, `in-progress`, `done`.

## Data model

| Field      | Type            | Rules                                                        |
|------------|-----------------|--------------------------------------------------------------|
| `id`       | integer         | Assigned by the database. Never reused after a delete.       |
| `title`    | text            | Required. Leading and trailing whitespace is trimmed. Must not be empty afterwards. |
| `priority` | `low` / `medium` / `high` | Defaults to `medium`. Input is case-insensitive.   |
| `due`      | date or none    | Optional. Must be `YYYY-MM-DD` and a real calendar date. Past dates are allowed. |
| `column`   | `todo` / `in-progress` / `done` | New tasks start in `todo`. Input is case-insensitive. |

**Overdue** means the task has a due date strictly before today's local date and
is not in `done`. A task due today is not overdue.

## Storage

- The default database path is `~/.taskboard/tasks.db`. Parent directories are created if missing.
- If the `TASKBOARD_DB` environment variable is set, that path is used instead. Tests always use this.

## User workflow

```bash
board add "Write spec" --priority high --due 2026-10-01   # Created task 1: Write spec
board add "Buy milk"                                        # Created task 2: Buy milk
board list                                                  # tasks grouped by column
board move 1 in-progress                                    # Moved task 1 to in-progress.
board edit 2 --title "Buy oat milk" --priority low          # Updated task 2.
board list --column todo --priority low --search milk       # filtered view
board delete 2                                              # asks, then: Deleted task 2.
```

## Output conventions

- Success messages go to **stdout**, and the exit code is `0`.
- Error messages go to **stderr** as `Error: <message>`, and the exit code is `1`.
- Malformed command-line syntax is handled by Typer, for example a missing argument or a non-integer ID. Typer prints a usage error and exits with code `2`.
- A Python traceback is never shown to the user.

`board list` prints column headers in this fixed order: `TODO`, `IN-PROGRESS`, `DONE`.
Under each header there is one line per task, sorted by ID:

```
TODO
  #2  Buy milk                        medium  due: -
  #3  File taxes                      high    due: 2026-04-15  OVERDUE
IN-PROGRESS
  #1  Write spec                      high    due: 2026-10-01
DONE
  (empty)
```

The exact spacing may vary. The acceptance criteria below check the content (ID,
title, priority, due date, `OVERDUE` marker, and which header a task appears under),
not the column widths.

## Acceptance criteria

Every criterion assumes a fresh, empty database unless it says otherwise.

### Adding and listing

- **AC-1: Add with defaults.** `board add "Buy milk"` prints `Created task 1: Buy milk` and exits `0`. The task is in `todo` with priority `medium` and no due date.
- **AC-2: Add with options.** `board add "Pay rent" --priority high --due 2026-10-01` exits `0`. `board list` then shows `Pay rent` with `high` and `2026-10-01`.
- **AC-3: Title is trimmed.** `board add "  Buy milk  "` stores and prints the title as `Buy milk`.
- **AC-4: Persistence.** After AC-1, a separate `board list` invocation that uses the same `TASKBOARD_DB` shows `#1` and `Buy milk` under `TODO`.
- **AC-5: Grouped list.** Given tasks in all three columns, `board list` exits `0` and prints `TODO`, `IN-PROGRESS`, `DONE` in that order. Each task appears under the header of its column. An empty column shows `(empty)`.
- **AC-6: Overdue marker.** A `todo` or `in-progress` task due `2000-01-01` shows `OVERDUE`. A task due today, a task due in the future, a task with no due date, and a `done` task due `2000-01-01` do not.
- **AC-7: Empty board.** `board list` on an empty database exits `0` and shows all three headers, each with `(empty)`.

### Moving, editing, deleting

- **AC-8: Move.** `board move 1 in-progress` prints `Moved task 1 to in-progress.` and exits `0`. `board list` then shows task 1 under `IN-PROGRESS`.
- **AC-9: Edit.** `board edit 1 --title "Buy oat milk" --priority low --due 2026-12-01` prints `Updated task 1.` and exits `0`, and all three fields change. Fields that are not passed stay unchanged. For example, `board edit 1 --priority high` changes only the priority.
- **AC-10: Edit with nothing to change.** `board edit 1` with no options prints `Error: Nothing to update. Pass --title, --priority, or --due.` to stderr and exits `1`.
- **AC-11: Delete with confirmation.** `board delete 1` prompts `Delete task 1 "Buy milk"? [y/N]:`. Answering `y` prints `Deleted task 1.` and exits `0`. Answering `n` or pressing Enter prints `Cancelled.`, exits `0`, and leaves the task in place.
- **AC-12: Delete with --yes.** `board delete 1 --yes` deletes without prompting, prints `Deleted task 1.`, and exits `0`.

### Filters

- **AC-13: Single filters.** `board list --column done` shows only the `DONE` group. `board list --priority high` shows only high-priority tasks. `board list --search milk` shows only tasks whose title contains `milk`, ignoring case.
- **AC-14: Combined filters.** `board list --column todo --priority high --search rent` shows only tasks that match all three filters.
- **AC-15: No matches.** If the filters match nothing, `board list` prints `No tasks match the given filters.` and exits `0`.

### Errors and invalid input

All of these exit `1`, print `Error: ...` to stderr, and leave the database unchanged.

- **AC-16: Empty or whitespace title.** `board add ""` and `board add "   "` print `Error: Title cannot be empty.`, and so does `board edit 1 --title "  "`.
- **AC-17: Invalid priority.** `board add "X" --priority urgent` prints `Error: Invalid priority 'urgent'. Choose from: low, medium, high.` The same check applies to `edit --priority` and `list --priority`.
- **AC-18: Malformed date.** `board add "X" --due 10/01/2026`, `--due 2026-1-5`, and `--due tomorrow` each print `Error: Invalid date '<value>'. Use a real date in YYYY-MM-DD format.`
- **AC-19: Impossible date.** `board add "X" --due 2026-02-30` prints `Error: Invalid date '2026-02-30'. Use a real date in YYYY-MM-DD format.`
- **AC-20: Unknown column.** `board move 1 blocked` prints `Error: Unknown column 'blocked'. Choose from: todo, in-progress, done.` The same check applies to `list --column`.
- **AC-21: Nonexistent task.** `board move 99 done`, `board edit 99 --title X`, and `board delete 99 --yes` each print `Error: Task 99 not found.`
- **AC-22: No tracebacks.** None of the outputs for AC-10 and AC-16 through AC-21 contain `Traceback`. A non-integer ID such as `board move abc done` gives Typer's usage error and exit code `2`, also without a traceback.

### Configuration

- **AC-23: Database location.** With `TASKBOARD_DB=/some/dir/x.db`, `board add "X"` creates that file and writes the task to it. When the variable is unset, the database is `~/.taskboard/tasks.db`, and missing parent directories are created.

### Added after Phase 2/3 review (approved by Alex)

- **AC-24: Unusable database path.** If `TASKBOARD_DB` points to a path that can't be created or isn't a SQLite database, any command prints `Error: Cannot open task database at <path>: <reason>.` and exits `1`, with no traceback. When a parent of the path is a regular file, the reason is `Not a directory`. Examples of unusable paths: a directory, a non-SQLite file, or a path under a regular file.
- **AC-25: Edits are all-or-nothing.** `board edit` validates every given option before writing. If any option is invalid, for example `board edit 1 --title New --priority urgent`, the error for the invalid option is printed and nothing is changed, including the valid options.
- **AC-26: Filtered list layout.** With `--priority` and/or `--search` but no `--column`, `board list` still prints all three headers, and a column with no matching tasks shows `(empty)`. With `--column`, only that column's header is printed. If no task matches at all, AC-15 applies.

## Out of scope

- Clearing a due date once it has been set.
- Custom columns, multiple boards, users, or syncing.
- Reordering tasks within a column.
