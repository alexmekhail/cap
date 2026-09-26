from pathlib import Path

import pytest

from taskboard import db


def assert_clean_error(result, message: str) -> None:
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == f"Error: {message}\n"
    assert "Traceback" not in result.output


def task_ids(db_path: Path) -> list[int]:
    with db.connect(db_path) as conn:
        return [task.id for task in db.list_tasks(conn)]


@pytest.fixture
def seeded(run) -> None:
    assert run("add", "Buy milk").exit_code == 0


PROMPT = 'Delete task 1 "Buy milk"? [y/N]: '


def test_ac11_delete_confirmed(run, db_path: Path, seeded: None) -> None:
    result = run("delete", "1", input="y\n")
    assert result.exit_code == 0
    assert result.stdout == f"{PROMPT}y\nDeleted task 1.\n"
    assert task_ids(db_path) == []


@pytest.mark.parametrize("answer", ["n\n", "\n"])
def test_ac11_delete_declined(run, db_path: Path, seeded: None, answer: str) -> None:
    result = run("delete", "1", input=answer)
    assert result.exit_code == 0
    assert result.stdout == f"{PROMPT}{answer}Cancelled.\n"
    assert task_ids(db_path) == [1]


@pytest.mark.parametrize("flag", ["--yes", "-y"])
def test_ac12_delete_with_yes_skips_prompt(
    run, db_path: Path, seeded: None, flag: str
) -> None:
    result = run("delete", "1", flag)
    assert result.exit_code == 0
    assert result.stdout == "Deleted task 1.\n"
    assert task_ids(db_path) == []


@pytest.mark.parametrize("args", [["99", "--yes"], ["99"]])
def test_ac21_delete_missing_task_does_not_prompt(run, args: list[str]) -> None:
    result = run("delete", *args, input="y\n")
    assert_clean_error(result, "Task 99 not found.")
