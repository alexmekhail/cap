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


def group_by_column(tasks: list[Task]) -> dict[Column, list[Task]]:
    """Group tasks by column in fixed board order, sorted by id, keeping empties."""
    groups: dict[Column, list[Task]] = {column: [] for column in Column}
    for task in sorted(tasks, key=lambda t: t.id):
        groups[task.column].append(task)
    return groups
