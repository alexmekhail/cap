"""Helpers for reading `board list` output in tests."""

HEADERS = ("TODO", "IN-PROGRESS", "DONE")


def sections(output: str) -> dict[str, list[str]]:
    """Split `board list` output into {header: [task lines]}."""
    result: dict[str, list[str]] = {}
    current: str | None = None
    for line in output.splitlines():
        if line.strip() in HEADERS and not line.startswith(" "):
            current = line.strip()
            result[current] = []
        elif current is not None and line.strip():
            result[current].append(line.strip())
    return result
