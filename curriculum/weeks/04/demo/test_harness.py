import subprocess
import sys
import unittest
from pathlib import Path

from dispatch import dispatch
from verify import verify

ROOT = Path(__file__).parent


class HarnessTests(unittest.TestCase):
    def setUp(self):
        self.plan = {"tasks": [
            {"id": "storage", "depends_on": [], "owns": ["storage.py"]},
            {"id": "ui", "depends_on": ["storage"], "owns": ["ui.py"]}
        ], "contract": {"preference_key": "color"}}
        self.adapter = [sys.executable, str(ROOT / "replay_worker.py")]

    def test_valid_handoff(self):
        self.assertFalse(verify(dispatch(self.plan, self.adapter))["application_checked"])

    def test_mismatch_rejected(self):
        with self.assertRaisesRegex(ValueError, "mismatch"):
            verify(dispatch(self.plan, self.adapter + ["--mismatch"]))

    def test_missing_dependency(self):
        self.plan["tasks"].reverse()
        with self.assertRaisesRegex(ValueError, "Dependency"):
            dispatch(self.plan, self.adapter)

    def test_ownership_conflict(self):
        self.plan["tasks"][1]["owns"] = ["storage.py"]
        with self.assertRaisesRegex(ValueError, "ownership"):
            dispatch(self.plan, self.adapter)

    def test_failed_adapter_stops(self):
        with self.assertRaises(subprocess.CalledProcessError):
            dispatch(self.plan, [sys.executable, "-c", "raise SystemExit(1)"])

    def test_wrong_task_id_rejected(self):
        bad = [sys.executable, '-c', 'import json; print(json.dumps(dict(task_id="wrong", status="complete")))']
        with self.assertRaisesRegex(ValueError, "worker"):
            dispatch(self.plan, bad)


if __name__ == "__main__":
    unittest.main()
