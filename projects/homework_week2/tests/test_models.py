from datetime import date

import pytest

from taskboard.models import (
    Column,
    Priority,
    Task,
    TaskChanges,
    TaskFilter,
    ValidationError,
    filter_tasks,
    group_by_column,
    parse_changes,
    parse_column,
    parse_due,
    parse_filter,
    parse_priority,
    validate_title,
)

TODAY = date(2026, 9, 25)


def make_task(
    task_id: int = 1,
    due: date | None = None,
    column: Column = Column.TODO,
) -> Task:
    return Task(id=task_id, title="T", priority=Priority.MEDIUM, due=due, column=column)


# --- title (AC-3, AC-16) ---


def test_validate_title_trims_whitespace() -> None:
    assert validate_title("  Buy milk  ") == "Buy milk"


@pytest.mark.parametrize("raw", ["", "   ", "\t\n"])
def test_validate_title_rejects_empty(raw: str) -> None:
    with pytest.raises(ValidationError, match=r"^Title cannot be empty\.$"):
        validate_title(raw)


# --- priority (AC-17) ---


@pytest.mark.parametrize(
    ("raw", "expected"),
    [("low", Priority.LOW), ("Medium", Priority.MEDIUM), (" HIGH ", Priority.HIGH)],
)
def test_parse_priority_accepts_any_case(raw: str, expected: Priority) -> None:
    assert parse_priority(raw) is expected


def test_parse_priority_rejects_unknown() -> None:
    with pytest.raises(ValidationError) as exc:
        parse_priority("urgent")
    assert str(exc.value) == (
        "Invalid priority 'urgent'. Choose from: low, medium, high."
    )


# --- due date (AC-18, AC-19) ---


def test_parse_due_none_is_none() -> None:
    assert parse_due(None) is None


def test_parse_due_valid() -> None:
    assert parse_due("2026-10-01") == date(2026, 10, 1)


@pytest.mark.parametrize(
    "raw",
    [
        "10/01/2026",
        "2026-1-5",
        "tomorrow",
        "",
        "20261001",  # accepted by date.fromisoformat on 3.11+, not by our spec
        "2026-W40-4",  # ISO week date, also accepted by fromisoformat
        "2026-02-30",  # impossible date
        "2025-02-29",  # not a leap year
        "2026-13-01",
    ],
)
def test_parse_due_rejects_bad_dates(raw: str) -> None:
    with pytest.raises(ValidationError) as exc:
        parse_due(raw)
    assert str(exc.value) == (
        f"Invalid date '{raw}'. Use a real date in YYYY-MM-DD format."
    )


def test_parse_due_accepts_leap_day() -> None:
    assert parse_due("2028-02-29") == date(2028, 2, 29)


# --- overdue (AC-6) ---


@pytest.mark.parametrize(
    ("due", "column", "expected"),
    [
        (date(2026, 9, 24), Column.TODO, True),
        (date(2026, 9, 24), Column.IN_PROGRESS, True),
        (date(2026, 9, 24), Column.DONE, False),
        (TODAY, Column.TODO, False),
        (date(2026, 9, 26), Column.TODO, False),
        (None, Column.TODO, False),
    ],
)
def test_is_overdue(due: date | None, column: Column, expected: bool) -> None:
    assert make_task(due=due, column=column).is_overdue(TODAY) is expected


# --- grouping (AC-5, AC-7) ---


def test_group_by_column_keeps_fixed_order_and_empty_columns() -> None:
    tasks = [
        make_task(3, column=Column.DONE),
        make_task(1, column=Column.TODO),
        make_task(2, column=Column.TODO),
    ]
    groups = group_by_column(tasks)
    assert list(groups) == [Column.TODO, Column.IN_PROGRESS, Column.DONE]
    assert [t.id for t in groups[Column.TODO]] == [1, 2]
    assert groups[Column.IN_PROGRESS] == []
    assert [t.id for t in groups[Column.DONE]] == [3]


# --- column (AC-8, AC-20) ---


@pytest.mark.parametrize(
    ("raw", "expected"),
    [
        ("todo", Column.TODO),
        ("In-Progress", Column.IN_PROGRESS),
        (" DONE ", Column.DONE),
    ],
)
def test_parse_column_accepts_any_case(raw: str, expected: Column) -> None:
    assert parse_column(raw) is expected


@pytest.mark.parametrize("raw", ["blocked", "in progress", "in_progress", ""])
def test_parse_column_rejects_unknown(raw: str) -> None:
    with pytest.raises(ValidationError) as exc:
        parse_column(raw)
    assert str(exc.value) == (
        f"Unknown column '{raw}'. Choose from: todo, in-progress, done."
    )


# --- edit changes (AC-9, AC-10) ---


def test_parse_changes_validates_only_given_fields() -> None:
    changes = parse_changes(title="  New  ", priority=None, due="2026-12-01")
    assert changes == TaskChanges(title="New", priority=None, due=date(2026, 12, 1))


def test_parse_changes_requires_at_least_one_field() -> None:
    with pytest.raises(ValidationError) as exc:
        parse_changes(title=None, priority=None, due=None)
    assert str(exc.value) == "Nothing to update. Pass --title, --priority, or --due."


def test_parse_changes_rejects_blank_title() -> None:
    with pytest.raises(ValidationError, match=r"^Title cannot be empty\.$"):
        parse_changes(title="  ", priority=None, due=None)


# --- filters (AC-13, AC-14) ---


def titled(task_id: int, title: str, priority: Priority, column: Column) -> Task:
    return Task(id=task_id, title=title, priority=priority, due=None, column=column)


FILTER_TASKS = [
    titled(1, "Buy milk", Priority.LOW, Column.TODO),
    titled(2, "Pay rent", Priority.HIGH, Column.TODO),
    titled(3, "MILK run", Priority.HIGH, Column.DONE),
]


def test_parse_filter_validates_values() -> None:
    task_filter = parse_filter(column="TODO", priority="High", search="milk")
    assert task_filter == TaskFilter(
        column=Column.TODO, priority=Priority.HIGH, search="milk"
    )


def test_parse_filter_rejects_bad_column_and_priority() -> None:
    with pytest.raises(ValidationError, match="Unknown column 'blocked'"):
        parse_filter(column="blocked", priority=None, search=None)
    with pytest.raises(ValidationError, match="Invalid priority 'urgent'"):
        parse_filter(column=None, priority="urgent", search=None)


@pytest.mark.parametrize(
    ("task_filter", "expected_ids"),
    [
        (TaskFilter(), [1, 2, 3]),
        (TaskFilter(column=Column.TODO), [1, 2]),
        (TaskFilter(priority=Priority.HIGH), [2, 3]),
        (TaskFilter(search="milk"), [1, 3]),
        (TaskFilter(column=Column.TODO, priority=Priority.HIGH), [2]),
        (TaskFilter(column=Column.DONE, priority=Priority.LOW), []),
        (TaskFilter(search="50%"), []),
    ],
)
def test_filter_tasks(task_filter: TaskFilter, expected_ids: list[int]) -> None:
    assert [t.id for t in filter_tasks(FILTER_TASKS, task_filter)] == expected_ids
