"""Shared fixtures: every test gets its own temp database via TASKBOARD_DB."""

from collections.abc import Callable
from pathlib import Path

import pytest
from typer.testing import CliRunner, Result

from taskboard.cli import app


@pytest.fixture
def db_path(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    path = tmp_path / "tasks.db"
    monkeypatch.setenv("TASKBOARD_DB", str(path))
    return path


@pytest.fixture
def run(db_path: Path) -> Callable[..., Result]:
    runner = CliRunner()

    def _run(*args: str, input: str | None = None) -> Result:
        return runner.invoke(app, list(args), input=input)

    return _run
