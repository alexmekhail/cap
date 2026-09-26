import subprocess
import sys
from datetime import date
from pathlib import Path

import pytest

from helpers import sections
from taskboard import db


def assert_clean_error(result, message: str) -> None:
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == f"Error: {message}\n"
    assert "Traceback" not in result.output


def assert_board_empty(run) -> None:
    listed = run("list")
    assert sections(listed.stdout) == {
        "TODO": ["(empty)"],
        "IN-PROGRESS": ["(empty)"],
        "DONE": ["(empty)"],
    }


# --- add ---


def test_ac1_add_with_defaults(run) -> None:
    result = run("add", "Buy milk")
    assert result.exit_code == 0
    assert result.stdout == "Created task 1: Buy milk\n"
    [line] = sections(run("list").stdout)["TODO"]
    assert line.startswith("#1")
    assert "Buy milk" in line
    assert "medium" in line
    assert "due: -" in line


def test_ac2_add_with_priority_and_due(run) -> None:
    result = run("add", "Pay rent", "--priority", "high", "--due", "2026-10-01")
    assert result.exit_code == 0
    assert result.stdout == "Created task 1: Pay rent\n"
    [line] = sections(run("list").stdout)["TODO"]
    assert "Pay rent" in line
    assert "high" in line
    assert "due: 2026-10-01" in line


def test_ac3_add_trims_title(run, db_path: Path) -> None:
    result = run("add", "  Buy milk  ")
    assert result.stdout == "Created task 1: Buy milk\n"
    with db.connect(db_path) as conn:
        [task] = db.list_tasks(conn)
    assert task.title == "Buy milk"


def test_ids_increment(run) -> None:
    assert run("add", "A").stdout == "Created task 1: A\n"
    assert run("add", "B").stdout == "Created task 2: B\n"


# --- list ---


def test_ac4_persists_across_processes(db_path: Path) -> None:
    """Run the real installed `board` script twice as separate processes."""
    board = Path(sys.executable).parent / "board"
    env = {"TASKBOARD_DB": str(db_path), "PATH": "/usr/bin:/bin"}
    added = subprocess.run(
        [board, "add", "Buy milk"], env=env, capture_output=True, text=True
    )
    assert added.returncode == 0, added.stderr
    listed = subprocess.run([board, "list"], env=env, capture_output=True, text=True)
    assert listed.returncode == 0, listed.stderr
    [line] = sections(listed.stdout)["TODO"]
    assert line.startswith("#1") and "Buy milk" in line


def test_ac5_list_headers_in_fixed_order(run) -> None:
    run("add", "A")
    result = run("list")
    assert result.exit_code == 0
    assert list(sections(result.stdout)) == ["TODO", "IN-PROGRESS", "DONE"]
    assert sections(result.stdout)["IN-PROGRESS"] == ["(empty)"]


def test_ac5_list_sorted_by_id(run) -> None:
    for title in ("First", "Second", "Third"):
        run("add", title)
    lines = sections(run("list").stdout)["TODO"]
    assert [line.split()[0] for line in lines] == ["#1", "#2", "#3"]


@pytest.mark.parametrize(
    ("due", "overdue"),
    [
        ("2000-01-01", True),
        (date.today().isoformat(), False),
        ("2999-12-31", False),
        (None, False),
    ],
)
def test_ac6_overdue_marker(run, due: str | None, overdue: bool) -> None:
    args = ["add", "Task"] + (["--due", due] if due else [])
    run(*args)
    [line] = sections(run("list").stdout)["TODO"]
    assert ("OVERDUE" in line) is overdue


def test_ac7_empty_board(run) -> None:
    result = run("list")
    assert result.exit_code == 0
    assert_board_empty(run)


# --- errors ---


@pytest.mark.parametrize("title", ["", "   "])
def test_ac16_add_rejects_empty_title(run, title: str) -> None:
    assert_clean_error(run("add", title), "Title cannot be empty.")
    assert_board_empty(run)


def test_ac17_add_rejects_invalid_priority(run) -> None:
    result = run("add", "X", "--priority", "urgent")
    assert_clean_error(
        result, "Invalid priority 'urgent'. Choose from: low, medium, high."
    )
    assert_board_empty(run)


@pytest.mark.parametrize("due", ["10/01/2026", "2026-1-5", "tomorrow"])
def test_ac18_add_rejects_malformed_date(run, due: str) -> None:
    result = run("add", "X", "--due", due)
    assert_clean_error(
        result, f"Invalid date '{due}'. Use a real date in YYYY-MM-DD format."
    )
    assert_board_empty(run)


def test_ac19_add_rejects_impossible_date(run) -> None:
    result = run("add", "X", "--due", "2026-02-30")
    assert_clean_error(
        result, "Invalid date '2026-02-30'. Use a real date in YYYY-MM-DD format."
    )
    assert_board_empty(run)


# --- configuration ---


def test_ac23_env_var_sets_db_location(run, db_path: Path) -> None:
    assert not db_path.exists()
    run("add", "X")
    assert db_path.exists()


def test_ac23_default_location_created_under_home(
    tmp_path: Path, monkeypatch: pytest.MonkeyPatch
) -> None:
    from typer.testing import CliRunner

    from taskboard.cli import app

    monkeypatch.delenv("TASKBOARD_DB", raising=False)
    monkeypatch.setenv("HOME", str(tmp_path))
    result = CliRunner().invoke(app, ["add", "X"])
    assert result.exit_code == 0
    assert (tmp_path / ".taskboard" / "tasks.db").exists()
