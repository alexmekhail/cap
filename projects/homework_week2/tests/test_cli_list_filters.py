import pytest

from helpers import sections


def assert_clean_error(result, message: str) -> None:
    assert result.exit_code == 1
    assert result.stdout == ""
    assert result.stderr == f"Error: {message}\n"
    assert "Traceback" not in result.output


def ids(lines: list[str]) -> list[str]:
    return [line.split()[0] for line in lines if line != "(empty)"]


@pytest.fixture
def board(run) -> None:
    """Seed five tasks.

    #1 todo/low, #2 todo/high, #3 done/high,
    #4 in-progress/medium, #5 in-progress/high.
    """
    for args in (
        ["Buy milk", "--priority", "low"],
        ["Pay rent", "--priority", "high"],
        ["Rent receipt", "--priority", "high"],
        ["Milk the cow"],
        ["Write spec", "--priority", "high"],
    ):
        assert run("add", *args).exit_code == 0
    for task_id, column in (("3", "done"), ("4", "in-progress"), ("5", "in-progress")):
        assert run("move", task_id, column).exit_code == 0


def test_ac13_filter_by_column(run, board: None) -> None:
    result = run("list", "--column", "done")
    assert result.exit_code == 0
    groups = sections(result.stdout)
    assert list(groups) == ["DONE"]
    assert ids(groups["DONE"]) == ["#3"]


def test_ac13_filter_by_priority(run, board: None) -> None:
    groups = sections(run("list", "--priority", "high").stdout)
    assert list(groups) == ["TODO", "IN-PROGRESS", "DONE"]
    assert [ids(lines) for lines in groups.values()] == [["#2"], ["#5"], ["#3"]]


def test_ac13_search_is_case_insensitive_substring(run, board: None) -> None:
    groups = sections(run("list", "--search", "MILK").stdout)
    assert [ids(lines) for lines in groups.values()] == [["#1"], ["#4"], []]
    assert groups["DONE"] == ["(empty)"]


def test_ac14_combined_filters_are_anded(run, board: None) -> None:
    result = run("list", "--column", "todo", "--priority", "high", "--search", "rent")
    assert result.exit_code == 0
    groups = sections(result.stdout)
    assert list(groups) == ["TODO"]
    assert ids(groups["TODO"]) == ["#2"]


@pytest.mark.parametrize(
    "args",
    [
        ["--column", "done", "--priority", "low"],
        ["--search", "nothing-matches-this"],
        ["--column", "todo", "--search", "spec"],
    ],
)
def test_ac15_no_matches(run, board: None, args: list[str]) -> None:
    result = run("list", *args)
    assert result.exit_code == 0
    assert result.stdout == "No tasks match the given filters.\n"


def test_ac17_list_rejects_invalid_priority(run, board: None) -> None:
    assert_clean_error(
        run("list", "--priority", "urgent"),
        "Invalid priority 'urgent'. Choose from: low, medium, high.",
    )


def test_ac20_list_rejects_unknown_column(run, board: None) -> None:
    assert_clean_error(
        run("list", "--column", "blocked"),
        "Unknown column 'blocked'. Choose from: todo, in-progress, done.",
    )
