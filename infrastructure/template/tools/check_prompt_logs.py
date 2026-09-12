"""Validate log structure, not the quality or truth of the evidence."""
from pathlib import Path
import sys

HEADERS = ["## 1. Goal and Acceptance Criteria", "## 2. Context and Architecture",
           "## 3. Validation and Findings", "## 4. Agent Recovery and Human Intervention",
           "## 5. Outcome and Limits"]


def validate(folder):
    logs = sorted(p for p in Path(folder).glob("week-*.md") if p.name != "week-01.md")
    errors = []
    if not logs:
        errors.append("Add at least one actual structured weekly evidence log; templates do not count.")
    for log in logs:
        lines = log.read_text().splitlines()
        for header in HEADERS:
            if header not in lines:
                errors.append(f"{log}: missing {header}")
    return errors


if __name__ == "__main__":
    errors = validate(sys.argv[1] if len(sys.argv) > 1 else "docs/prompt-logs")
    for error in errors:
        print(error)
    if errors:
        sys.exit(1)
    print("Log structure verified; content still requires review.")
