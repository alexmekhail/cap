"""Typer commands only: parse input, call models/db, print output."""

from collections.abc import Iterator
from contextlib import contextmanager
from datetime import date
from typing import Annotated

import typer

from taskboard import db
from taskboard.models import (
    Task,
    TaskboardError,
    group_by_column,
    parse_changes,
    parse_column,
    parse_due,
    parse_priority,
    validate_title,
)

app = typer.Typer(help="A command-line Kanban task board.", no_args_is_help=True)


@app.callback()
def main() -> None:
    """Manage tasks across the todo, in-progress, and done columns."""


@contextmanager
def _user_errors() -> Iterator[None]:
    """Turn domain errors into `Error: ...` on stderr with exit code 1."""
    try:
        yield
    except TaskboardError as exc:
        typer.echo(f"Error: {exc}", err=True)
        raise typer.Exit(1) from None


def _format_task(task: Task, today: date) -> str:
    due = task.due.isoformat() if task.due else "-"
    line = f"  #{task.id:<3} {task.title:<30} {task.priority.value:<7} due: {due}"
    if task.is_overdue(today):
        line += "  OVERDUE"
    return line


@app.command()
def add(
    title: Annotated[str, typer.Argument(help="Task title.")],
    priority: Annotated[str, typer.Option(help="low, medium, or high.")] = "medium",
    due: Annotated[str | None, typer.Option(help="Due date, YYYY-MM-DD.")] = None,
) -> None:
    """Add a task to the todo column."""
    with _user_errors():
        clean_title = validate_title(title)
        parsed_priority = parse_priority(priority)
        parsed_due = parse_due(due)
        with db.connect() as conn:
            task = db.add_task(conn, clean_title, parsed_priority, parsed_due)
    typer.echo(f"Created task {task.id}: {task.title}")


@app.command(name="list")
def list_() -> None:
    """Show tasks grouped by column."""
    with db.connect() as conn:
        tasks = db.list_tasks(conn)
    today = date.today()
    for column, column_tasks in group_by_column(tasks).items():
        typer.echo(column.value.upper())
        if not column_tasks:
            typer.echo("  (empty)")
        for task in column_tasks:
            typer.echo(_format_task(task, today))


@app.command()
def move(
    task_id: Annotated[int, typer.Argument(help="Task id.")],
    column: Annotated[str, typer.Argument(help="todo, in-progress, or done.")],
) -> None:
    """Move a task to another column."""
    with _user_errors():
        target = parse_column(column)
        with db.connect() as conn:
            task = db.move_task(conn, task_id, target)
    typer.echo(f"Moved task {task.id} to {task.column.value}.")


@app.command()
def edit(
    task_id: Annotated[int, typer.Argument(help="Task id.")],
    title: Annotated[str | None, typer.Option(help="New title.")] = None,
    priority: Annotated[str | None, typer.Option(help="low, medium, or high.")] = None,
    due: Annotated[str | None, typer.Option(help="New due date, YYYY-MM-DD.")] = None,
) -> None:
    """Change a task's title, priority, or due date."""
    with _user_errors():
        changes = parse_changes(title, priority, due)
        with db.connect() as conn:
            task = db.update_task(conn, task_id, changes)
    typer.echo(f"Updated task {task.id}.")
