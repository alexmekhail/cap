"""SQLite storage: database location, schema, and queries (parameterized only)."""

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import date
from pathlib import Path

from taskboard.models import (
    Column,
    Priority,
    Task,
    TaskboardError,
    TaskChanges,
    TaskNotFoundError,
)

_SCHEMA = """
CREATE TABLE IF NOT EXISTS tasks (
    id       INTEGER PRIMARY KEY AUTOINCREMENT,
    title    TEXT NOT NULL,
    priority TEXT NOT NULL,
    due      TEXT,
    col      TEXT NOT NULL
)
"""

_SELECT = "SELECT id, title, priority, due, col FROM tasks"


def get_db_path() -> Path:
    """`TASKBOARD_DB` if set, otherwise `~/.taskboard/tasks.db`."""
    override = os.environ.get("TASKBOARD_DB")
    if override:
        return Path(override)
    return Path.home() / ".taskboard" / "tasks.db"


class StorageError(TaskboardError):
    """The database file can't be created, opened, or read."""

    def __init__(self, db_path: Path, exc: Exception) -> None:
        if isinstance(exc, FileExistsError):
            # mkdir(exist_ok=True) raises this only when a parent is a regular file.
            reason: object = "Not a directory"
        elif isinstance(exc, OSError) and exc.strerror:
            reason = exc.strerror
        else:
            reason = exc
        super().__init__(f"Cannot open task database at {db_path}: {reason}.")


def _open(db_path: Path) -> sqlite3.Connection:
    """Create parent dirs, connect, and ensure the schema; wrap failures."""
    try:
        db_path.parent.mkdir(parents=True, exist_ok=True)
        conn = sqlite3.connect(db_path)
    except (OSError, sqlite3.Error) as exc:
        raise StorageError(db_path, exc) from None
    try:
        conn.execute(_SCHEMA)
    except sqlite3.Error as exc:
        conn.close()
        raise StorageError(db_path, exc) from None
    return conn


@contextmanager
def connect(path: Path | None = None) -> Iterator[sqlite3.Connection]:
    """Open the database (creating dirs and schema), commit on success, always close."""
    conn = _open(path if path is not None else get_db_path())
    try:
        yield conn
        conn.commit()
    except BaseException:
        conn.rollback()
        raise
    finally:
        conn.close()


def _row_to_task(row: tuple[int, str, str, str | None, str]) -> Task:
    task_id, title, priority, due, column = row
    return Task(
        id=task_id,
        title=title,
        priority=Priority(priority),
        due=date.fromisoformat(due) if due else None,
        column=Column(column),
    )


def add_task(
    conn: sqlite3.Connection, title: str, priority: Priority, due: date | None
) -> Task:
    cursor = conn.execute(
        "INSERT INTO tasks (title, priority, due, col) VALUES (?, ?, ?, ?)",
        (title, priority.value, due.isoformat() if due else None, Column.TODO.value),
    )
    task_id = cursor.lastrowid
    assert task_id is not None
    return Task(task_id, title, priority, due, Column.TODO)


def list_tasks(conn: sqlite3.Connection) -> list[Task]:
    rows = conn.execute(f"{_SELECT} ORDER BY id").fetchall()
    return [_row_to_task(row) for row in rows]


def get_task(conn: sqlite3.Connection, task_id: int) -> Task:
    row = conn.execute(f"{_SELECT} WHERE id = ?", (task_id,)).fetchone()
    if row is None:
        raise TaskNotFoundError(task_id)
    return _row_to_task(row)


def move_task(conn: sqlite3.Connection, task_id: int, column: Column) -> Task:
    cursor = conn.execute(
        "UPDATE tasks SET col = ? WHERE id = ?", (column.value, task_id)
    )
    if cursor.rowcount == 0:
        raise TaskNotFoundError(task_id)
    return get_task(conn, task_id)


def update_task(conn: sqlite3.Connection, task_id: int, changes: TaskChanges) -> Task:
    """Apply non-None fields; COALESCE keeps the stored value for the rest."""
    cursor = conn.execute(
        """
        UPDATE tasks
        SET title = COALESCE(?, title),
            priority = COALESCE(?, priority),
            due = COALESCE(?, due)
        WHERE id = ?
        """,
        (
            changes.title,
            changes.priority.value if changes.priority else None,
            changes.due.isoformat() if changes.due else None,
            task_id,
        ),
    )
    if cursor.rowcount == 0:
        raise TaskNotFoundError(task_id)
    return get_task(conn, task_id)


def delete_task(conn: sqlite3.Connection, task_id: int) -> None:
    cursor = conn.execute("DELETE FROM tasks WHERE id = ?", (task_id,))
    if cursor.rowcount == 0:
        raise TaskNotFoundError(task_id)
