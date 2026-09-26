"""Task model, allowed values, validation, and board rules. No I/O."""

import re
from dataclasses import dataclass
from datetime import date
from enum import StrEnum

_DATE_PATTERN = re.compile(r"\d{4}-\d{2}-\d{2}")


class TaskboardError(Exception):
    """Base class for errors that are shown to the user as `Error: ...`."""


class ValidationError(TaskboardError):
    """User input that does not satisfy the spec."""


class TaskNotFoundError(TaskboardError):
    """No task with the requested id."""

    def __init__(self, task_id: int) -> None:
        super().__init__(f"Task {task_id} not found.")


class Priority(StrEnum):
    LOW = "low"
    MEDIUM = "medium"
    HIGH = "high"


class Column(StrEnum):
    TODO = "todo"
    IN_PROGRESS = "in-progress"
    DONE = "done"


@dataclass(frozen=True)
class Task:
    id: int
    title: str
    priority: Priority
    due: date | None
    column: Column

    def is_overdue(self, today: date) -> bool:
        """Due strictly before `today` and not yet done."""
        return self.due is not None and self.due < today and self.column != Column.DONE


@dataclass(frozen=True)
class TaskChanges:
    """Validated edits; `None` means leave that field unchanged."""

    title: str | None
    priority: Priority | None
    due: date | None


@dataclass(frozen=True)
class TaskFilter:
    """Validated `list` filters; `None` means don't filter on that field."""

    column: Column | None = None
    priority: Priority | None = None
    search: str | None = None

    @property
    def is_active(self) -> bool:
        return any(v is not None for v in (self.column, self.priority, self.search))

    def matches(self, task: Task) -> bool:
        return (
            (self.column is None or task.column == self.column)
            and (self.priority is None or task.priority == self.priority)
            and (self.search is None or self.search.casefold() in task.title.casefold())
        )


def _choices(enum_type: type[StrEnum]) -> str:
    return ", ".join(member.value for member in enum_type)


def validate_title(raw: str) -> str:
    title = raw.strip()
    if not title:
        raise ValidationError("Title cannot be empty.")
    return title


def parse_priority(raw: str) -> Priority:
    try:
        return Priority(raw.strip().lower())
    except ValueError:
        raise ValidationError(
            f"Invalid priority '{raw}'. Choose from: {_choices(Priority)}."
        ) from None


def parse_column(raw: str) -> Column:
    try:
        return Column(raw.strip().lower())
    except ValueError:
        raise ValidationError(
            f"Unknown column '{raw}'. Choose from: {_choices(Column)}."
        ) from None


def parse_due(raw: str | None) -> date | None:
    """Parse a strict YYYY-MM-DD date. `date.fromisoformat` alone is too lenient."""
    if raw is None:
        return None
    error = ValidationError(
        f"Invalid date '{raw}'. Use a real date in YYYY-MM-DD format."
    )
    if not _DATE_PATTERN.fullmatch(raw):
        raise error
    try:
        return date.fromisoformat(raw)
    except ValueError:
        raise error from None


def group_by_column(
    tasks: list[Task], only: Column | None = None
) -> dict[Column, list[Task]]:
    """Group tasks by column in fixed board order, sorted by id, keeping empties.

    With `only`, return just that column's group.
    """
    columns = [only] if only is not None else list(Column)
    groups: dict[Column, list[Task]] = {column: [] for column in columns}
    for task in sorted(tasks, key=lambda t: t.id):
        if task.column in groups:
            groups[task.column].append(task)
    return groups


def parse_changes(
    title: str | None, priority: str | None, due: str | None
) -> TaskChanges:
    """Validate every given field before anything is written."""
    if title is None and priority is None and due is None:
        raise ValidationError("Nothing to update. Pass --title, --priority, or --due.")
    return TaskChanges(
        title=validate_title(title) if title is not None else None,
        priority=parse_priority(priority) if priority is not None else None,
        due=parse_due(due),
    )


def parse_filter(
    column: str | None, priority: str | None, search: str | None
) -> TaskFilter:
    return TaskFilter(
        column=parse_column(column) if column is not None else None,
        priority=parse_priority(priority) if priority is not None else None,
        search=search,
    )


def filter_tasks(tasks: list[Task], task_filter: TaskFilter) -> list[Task]:
    """Keep tasks matching every given filter (AND)."""
    return [task for task in tasks if task_filter.matches(task)]
