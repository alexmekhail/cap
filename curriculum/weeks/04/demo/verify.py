"""Check handoff compatibility, not application correctness."""
import json
import sys


def verify(report):
    expected = report["contract"]["preference_key"]
    if not report["results"]:
        raise ValueError("No worker results")
    for task, result in report["results"].items():
        if result.get("preference_key") != expected:
            raise ValueError(f"{task}: interface mismatch")
    return {**report, "handoff_check": "passed", "application_checked": False}


if __name__ == "__main__":
    print(json.dumps(verify(json.load(sys.stdin))))
