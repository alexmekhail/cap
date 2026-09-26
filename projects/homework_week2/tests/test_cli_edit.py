from datetime import date
from pathlib import Path

import pytest

from taskboard import db
from taskboard.models import Column, Priority, Task


def assert_clean_error(result, message: str) -> None:
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == f"Error: {message}\n"
    assert "Traceback" not in result.output


def only_task(db_path: Path) -> Task:
    with db.connect(db_path) as conn:
        [task] = db.list_tasks(conn)
    return task


@pytest.fixture
def seeded(run, db_path: Path) -> Task:
    assert run("add", "Buy milk", "--due", "2026-10-01").exit_code == 0
    return only_task(db_path)


def test_ac9_edit_all_fields(run, db_path: Path, seeded: Task) -> None:
    result = run(
        "edit", "1", "--title", "Buy oat milk", "--priority", "low",
        "--due", "2026-12-01",
    )  # fmt: skip
    assert result.exit_code == 0
    assert result.stdout == "Updated task 1.\n"
    assert only_task(db_path) == Task(
        1, "Buy oat milk", Priority.LOW, date(2026, 12, 1), Column.TODO
    )


def test_ac9_edit_one_field_leaves_others(run, db_path: Path, seeded: Task) -> None:
    result = run("edit", "1", "--priority", "high")
    assert result.stdout == "Updated task 1.\n"
    after = only_task(db_path)
    assert after.priority is Priority.HIGH
    assert (after.title, after.due, after.column) == (
        seeded.title,
        seeded.due,
        seeded.column,
    )


def test_ac10_edit_nothing(run, db_path: Path, seeded: Task) -> None:
    result = run("edit", "1")
    assert_clean_error(result, "Nothing to update. Pass --title, --priority, or --due.")
    assert only_task(db_path) == seeded


@pytest.mark.parametrize(
    ("args", "message"),
    [
        (["--title", "  "], "Title cannot be empty."),
        (
            ["--priority", "urgent"],
            "Invalid priority 'urgent'. Choose from: low, medium, high.",
        ),
        (
            ["--due", "2026-02-30"],
            "Invalid date '2026-02-30'. Use a real date in YYYY-MM-DD format.",
        ),
        (
            ["--due", "10/01/2026"],
            "Invalid date '10/01/2026'. Use a real date in YYYY-MM-DD format.",
        ),
        # A valid field alongside an invalid one must not be partially applied.
        (["--title", "New", "--priority", "urgent"],
         "Invalid priority 'urgent'. Choose from: low, medium, high."),
    ],
)  # fmt: skip
def test_ac16_to_19_edit_rejects_invalid_input(
    run, db_path: Path, seeded: Task, args: list[str], message: str
) -> None:
    assert_clean_error(run("edit", "1", *args), message)
    assert only_task(db_path) == seeded


def test_ac21_edit_missing_task(run) -> None:
    assert_clean_error(run("edit", "99", "--title", "X"), "Task 99 not found.")
