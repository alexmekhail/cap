import pytest

from helpers import sections


def assert_clean_error(result, message: str) -> None:
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == f"Error: {message}\n"
    assert "Traceback" not in result.output


def test_ac8_move_to_in_progress(run) -> None:
    run("add", "Buy milk")
    result = run("move", "1", "in-progress")
    assert result.exit_code == 0
    assert result.stdout == "Moved task 1 to in-progress.\n"
    groups = sections(run("list").stdout)
    assert groups["TODO"] == ["(empty)"]
    [line] = groups["IN-PROGRESS"]
    assert line.startswith("#1") and "Buy milk" in line


def test_ac8_move_is_case_insensitive(run) -> None:
    run("add", "A")
    result = run("move", "1", "DONE")
    assert result.stdout == "Moved task 1 to done.\n"


def test_ac5_tasks_listed_under_their_columns(run) -> None:
    for title in ("Todo task", "Doing task", "Done task"):
        run("add", title)
    run("move", "2", "in-progress")
    run("move", "3", "done")
    groups = sections(run("list").stdout)
    assert list(groups) == ["TODO", "IN-PROGRESS", "DONE"]
    assert [len(lines) for lines in groups.values()] == [1, 1, 1]
    assert "Todo task" in groups["TODO"][0]
    assert "Doing task" in groups["IN-PROGRESS"][0]
    assert "Done task" in groups["DONE"][0]


@pytest.mark.parametrize(
    ("column", "overdue"), [("in-progress", True), ("done", False)]
)
def test_ac6_overdue_depends_on_column(run, column: str, overdue: bool) -> None:
    run("add", "Old", "--due", "2000-01-01")
    assert run("move", "1", column).exit_code == 0
    [line] = sections(run("list").stdout)[column.upper()]
    assert line.startswith("#1")
    assert ("OVERDUE" in line) is overdue


def test_ac20_move_rejects_unknown_column(run) -> None:
    run("add", "A")
    result = run("move", "1", "blocked")
    assert_clean_error(
        result, "Unknown column 'blocked'. Choose from: todo, in-progress, done."
    )
    [line] = sections(run("list").stdout)["TODO"]
    assert "A" in line


def test_ac21_move_missing_task(run) -> None:
    assert_clean_error(run("move", "99", "done"), "Task 99 not found.")


def test_ac22_non_integer_id_is_usage_error(run) -> None:
    result = run("move", "abc", "done")
    assert result.exit_code == 2
    assert "'abc' is not a valid int" in result.output
    assert "Traceback" not in result.output
