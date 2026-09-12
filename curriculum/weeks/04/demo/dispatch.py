"""Run a bounded adapter per task. Adapter: JSON stdin -> JSON stdout."""
import json
import subprocess
import sys


def dispatch(plan, adapter, timeout=30):
    completed = {}
    owned = set()
    for task in plan["tasks"]:
        if task["id"] in completed:
            raise ValueError("Duplicate task ID")
        if any(dep not in completed for dep in task["depends_on"]):
            raise ValueError("Dependency not ready")
        if owned.intersection(task["owns"]):
            raise ValueError("Conflicting ownership")
        payload = {"task": task, "contract": plan["contract"],
                   "handoffs": {dep: completed[dep] for dep in task["depends_on"]}}
        run = subprocess.run(adapter, input=json.dumps(payload), capture_output=True,
                             text=True, timeout=timeout, check=True)
        result = json.loads(run.stdout)
        if result.get("task_id") != task["id"] or result.get("status") != "complete":
            raise ValueError("Missing or unsuccessful worker result")
        completed[task["id"]] = result
        owned.update(task["owns"])
    return {"contract": plan["contract"], "results": completed}


if __name__ == "__main__":
    if len(sys.argv) < 2:
        raise SystemExit("Supply an explicit adapter executable and arguments")
    print(json.dumps(dispatch(json.load(sys.stdin), sys.argv[1:])))
