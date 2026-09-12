"""Check course structure and local links; does not judge teaching quality."""
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
paths = subprocess.check_output(
    ["git", "ls-files", "--cached", "--others", "--exclude-standard"], cwd=ROOT, text=True
).splitlines()
errors = []
links = 0
for name in paths:
    path = ROOT / name
    if path.suffix != ".md" or not path.is_file():
        continue
    source = path.read_text()
    # Ignore examples in code fences when validating Markdown destinations.
    prose = re.sub(r"```.*?```", "", source, flags=re.DOTALL)
    for dest in re.findall(r"\]\(([^)]+)\)", prose):
        if "://" in dest or dest.startswith(("#", "mailto:")):
            continue
        target = dest.split("#")[0]
        if target and not (path.parent / target).exists():
            errors.append(f"{name}: missing link {target}")
        links += 1
for week in range(1, 13):
    folder = ROOT / "curriculum/weeks" / f"{week:02}"
    for name in ["README.md", "talk-outline.md", "homework.md", "reference.md",
                 "lecture-script.md", "presentation.md", "instructor-demo.md"]:
        if not (folder / name).is_file():
            errors.append(f"Week {week}: missing {name}")
    homework = folder / "homework.md"
    if homework.is_file():
        weights = [int(value) for value in re.findall(r"\| (\d+)% \|", homework.read_text())]
        if sum(weights) != 100:
            errors.append(f"Week {week}: rubric totals {sum(weights)}%")
if errors:
    raise SystemExit("\n".join(errors))
print(f"12 weekly packages, rubric totals, and {links} local links verified.")
