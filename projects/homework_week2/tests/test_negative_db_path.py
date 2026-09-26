"""Phase 3: challenge AC-22 ("no tracebacks") with an unusable TASKBOARD_DB.

These run the real `board` script in a subprocess, because CliRunner catches
unhandled exceptions and would hide a traceback from the test.
"""

import subprocess
import sys
from pathlib import Path

import pytest

BOARD = Path(sys.executable).parent / "board"


def run_board(db: Path, *args: str) -> subprocess.CompletedProcess[str]:
    env = {"TASKBOARD_DB": str(db), "PATH": "/usr/bin:/bin"}
    return subprocess.run(
        [BOARD, *args], env=env, capture_output=True, text=True, check=False
    )


def directory(tmp_path: Path) -> Path:
    return tmp_path


def not_a_database(tmp_path: Path) -> Path:
    path = tmp_path / "notes.txt"
    path.write_text("this is not a sqlite database\n" * 100)
    return path


def parent_is_a_file(tmp_path: Path) -> Path:
    parent = tmp_path / "plain-file"
    parent.write_text("x")
    return parent / "tasks.db"


@pytest.mark.parametrize("make_path", [directory, not_a_database, parent_is_a_file])
@pytest.mark.parametrize("args", [["list"], ["add", "X"]])
def test_unusable_db_path_gives_clean_error(
    tmp_path: Path, make_path, args: list[str]
) -> None:
    result = run_board(make_path(tmp_path), *args)
    assert "Traceback" not in result.stderr
    assert result.returncode == 1
    assert result.stdout == ""
    assert result.stderr.startswith("Error: Cannot open task database at ")
