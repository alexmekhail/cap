"""Emit a small dependency plan for the public harness exercise."""
import json

if __name__ == "__main__":
    print(json.dumps({"tasks": [
        {"id": "storage", "role": "persistence", "depends_on": [], "owns": ["preferences.py"]},
        {"id": "ui", "role": "interface", "depends_on": ["storage"], "owns": ["palette.py"]}
    ], "contract": {"preference_key": "color"}}))
