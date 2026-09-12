"""Deterministic replay adapter. No model calls or application building occur."""
import json
import sys

request = json.load(sys.stdin)
key = "colour" if "--mismatch" in sys.argv and request["task"]["id"] == "ui" else "color"
print(json.dumps({"task_id": request["task"]["id"], "status": "complete",
                  "preference_key": key, "mode": "deterministic-replay",
                  "evidence": "Reference artifact only; no application checks executed."}))
