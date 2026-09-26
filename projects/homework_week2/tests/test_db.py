from datetime import date
from pathlib import Path

import pytest

from taskboard import db
from taskboard.models import Column, Priority, TaskNotFoundError


def test_db_path_uses_env_override(db_path: Path) -> None:
    assert db.get_db_path() == db_path


def test_db_path_default_is_home_taskboard(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    monkeypatch.delenv("TASKBOARD_DB", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    assert db.get_db_path() == tmp_path / ".taskboard" / "tasks.db"


def test_connect_creates_parent_dirs(tmp_path: Path) -> None:
    path = tmp_path / "nested" / "dir" / "tasks.db"
    with db.connect(path):
        pass
    assert path.exists()


def test_add_and_list_round_trip(db_path: Path) -> None:
    with db.connect(db_path) as conn:
        first = db.add_task(conn, "A", Priority.HIGH, date(2026, 10, 1))
        second = db.add_task(conn, "B", Priority.LOW, None)
    with db.connect(db_path) as conn:
        tasks = db.list_tasks(conn)
    assert [t.id for t in tasks] == [first.id, second.id] == [1, 2]
    assert tasks[0].title == "A"
    assert tasks[0].priority is Priority.HIGH
    assert tasks[0].due == date(2026, 10, 1)
    assert tasks[0].column is Column.TODO
    assert tasks[1].due is None


def test_move_task_changes_column_and_persists(db_path: Path) -> None:
    with db.connect(db_path) as conn:
        task = db.add_task(conn, "A", Priority.LOW, None)
        moved = db.move_task(conn, task.id, Column.DONE)
    assert moved.column is Column.DONE
    with db.connect(db_path) as conn:
        assert db.get_task(conn, task.id).column is Column.DONE


def test_move_missing_task_raises(db_path: Path) -> None:
    with db.connect(db_path) as conn, pytest.raises(TaskNotFoundError) as exc:
        db.move_task(conn, 99, Column.DONE)
    assert str(exc.value) == "Task 99 not found."


def test_get_missing_task_raises(db_path: Path) -> None:
    with db.connect(db_path) as conn, pytest.raises(TaskNotFoundError):
        db.get_task(conn, 1)
