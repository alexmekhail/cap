"""Typer commands only: parse input, call models/db, print output."""

import typer

app = typer.Typer(help="A command-line Kanban task board.", no_args_is_help=True)


@app.callback()
def main() -> None:
    """Manage tasks across the todo, in-progress, and done columns."""
