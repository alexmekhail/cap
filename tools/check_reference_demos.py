"""Check the intentionally failing Week 3 fixture and the log validator."""
import importlib.util
import shutil
import subprocess
import sys
import tempfile
from pathlib import Path

root = Path(__file__).resolve().parents[1]
source = root / "curriculum/weeks/03/demo"
with tempfile.TemporaryDirectory() as folder:
    for name in ["seed.py", "test_seed.py"]:
        shutil.copy(source / name, Path(folder) / name)
    failed = subprocess.run([sys.executable, "-m", "unittest", "-v"], cwd=folder,
                            capture_output=True, text=True, check=False)
    assert failed.returncode != 0 and "Ran 4 tests" in failed.stderr, failed.stderr
    shutil.copy(source / "instructor_solution.py", Path(folder) / "seed.py")
    passed = subprocess.run([sys.executable, "-m", "unittest", "-v"], cwd=folder,
                            capture_output=True, text=True, check=False)
    assert passed.returncode == 0, passed.stderr
spec = importlib.util.spec_from_file_location("log_checks", root / "infrastructure/template/tools/check_prompt_logs.py")
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)
with tempfile.TemporaryDirectory() as folder:
    location = Path(folder)
    (location / "TEMPLATE.md").write_text("\n".join(module.HEADERS))
    assert module.validate(location), "Template-only folder must fail"
    (location / "week-01.md").write_text("Field report")
    assert module.validate(location), "Week 1 alone does not meet production evidence requirements"
    (location / "week-05.md").write_text("\n".join(module.HEADERS))
    assert not module.validate(location)
    (location / "week-05.md").write_text("Incomplete")
    assert module.validate(location)
print("Week 3 expected failure/recovery and evidence-log validation passed.")
