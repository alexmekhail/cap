"""SQLite storage: database location, schema, and queries (parameterized only)."""

import os
import sqlite3
from collections.abc import Iterator
from contextlib import contextmanager
from datetime import date
from pathlib import Path

from taskboard.models import Column, Priority, Task

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


@contextmanager
def connect(path: Path | None = None) -> Iterator[sqlite3.Connection]:
    """Open the database (creating dirs and schema), commit on success, always close."""
    db_path = path if path is not None else get_db_path()
    db_path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(db_path)
    try:
        conn.execute(_SCHEMA)
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
