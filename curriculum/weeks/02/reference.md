# Week 2 Reference: Prompt, Context, Instructions, and Skills

## Concepts
- **Prompt:** The current request, including the outcome, constraints, and acceptance criteria.
- **Context:** Information available for the task: relevant source, interfaces, examples, previous decisions, and tool output. Ask the agent to inspect missing information rather than guessing or pasting an entire repository.
- **System instructions:** Tool/provider-controlled instructions that shape the agent's operation. A project Markdown file is not automatically a system prompt.
- **Project instructions:** Durable guidance for this repository. Names and discovery rules vary by tool; examples include `AGENTS.md` and `CLAUDE.md`. Check the selected tool's documentation and behavior. For a generic file, explicitly ask the agent to read it.
- **Skill:** A reusable task procedure with a purpose, inputs, steps, checks, and expected output. Native skill packaging varies; this course's plain Markdown examples can be explicitly supplied when automatic discovery is unavailable.
- **In the loop:** You inspect and decide between small steps.
- **On the loop:** You define boundaries and checks, then supervise at checkpoints and intervene when necessary. This is a choice of control strategy, not a promise that an agent cannot fail.

## Project-instruction Starter
Adapt this to your actual project and tool:

```text
Purpose: a local task board with saved tasks.
Map: identify the actual UI, state, persistence, and test files before editing.
Constraints: preserve existing data; no new dependency without an explanation.
Checks: record exact working test and run commands here after setup.
Workflow: propose a small change, inspect relevant files, implement, run checks.
Stop: acceptance criteria conflict, data may be lost, or checks remain unexplained.
Report: changed files, checks run with results, and remaining limitations.
```

## Reusable Skill: Review a Code Change

Compare three standalone versions of the same review task:

1. [Find problems](skills/diff-review/SKILL.md): a deliberately limited teaching example with no explicit pass outcome.
2. [Classify the change](skills/review-decision/SKILL.md): explicitly allows **accept**, **comment**, or **reject**.
3. [Classify with a refuter](skills/review-with-refuter/SKILL.md): challenges potential findings before deciding.

Use separate fresh conversations with the same request, diff, relevant code, and check results. These are alternatives, not a pipeline. None submits a PR review or changes code. The refuter is an additional review pass, not necessarily a separate agent.

Version 1 can encourage speculative criticism; it does not always find a problem. Versions 2 and 3 are not guaranteed to be better: compare whether their findings are supported. Try both the prepared defective change and a verified correct change so students can observe an opportunity to pass.

In a fix-and-review loop, accept ends the loop and comment leaves optional feedback. Act on supported blockers; obtain missing required evidence before deciding on a fix. Set an iteration limit and inspect recurring findings instead of continuing indefinitely.

Example invocation, after copying the skill into your project:

```text
Read skills/diff-review/SKILL.md and use it to review my staged changes
against this request: add an incomplete-tasks filter without deleting
saved tasks. Return findings with file references and any validation
still needed. Do not edit the code.

```

Repeat in fresh conversations, replacing the skill path with
`skills/review-decision/SKILL.md` and `skills/review-with-refuter/SKILL.md`.
Supply the same inputs; let each skill determine its output.

The course file is not automatically installed. Explicitly ask the agent to read it, or use your tool's supported skill installation mechanism.

### Classroom Example: Hiding Is Not Deleting

**Request:** Add an incomplete-tasks filter. Turning it off restores the full list. Preserve all saved tasks.

**Prepared defective diff** (illustrative JavaScript, not code to apply to the students' apps):

```diff
 function onFilterChange(enabled) {
   showIncompleteOnly = enabled;
+  if (enabled) {
+    tasks = tasks.filter(task => !task.completed);
+    localStorage.setItem('tasks', JSON.stringify(tasks));
+  }
   renderTasks();
 }
```

**Review finding:** Turning the filter on removes completed tasks from the task collection and overwrites saved data. Turning it off cannot restore them. The implementation should filter the displayed list while preserving the underlying task collection.

**Review decision: REJECT.** The finding is supported by the assignment to `tasks` and the saved-data write. This blocks acceptance because preserving completed tasks is an explicit requirement. Fix the behavior and provide validation before reconsideration.

**Follow-up validation:** Create one complete and one incomplete task. Toggle the filter on and off, then reload. Both tasks must remain saved; the filter changes only which tasks are displayed.

Review inspects the change and identifies concerns. Validation runs checks and exercises behavior. Use both before accepting a change.

## Reusable Skill: Validate a Small Change
**Input:** task criteria, changed files, known baseline, and working check commands.
1. Compare the diff with the requested behavior; identify unrelated changes.
2. Run the relevant checks and compare failures with the baseline.
3. Exercise one success and one failure case manually.
4. Inspect whether tests meaningfully assert the intended behavior.
5. Report evidence and limits; do not claim unrun checks passed.
**Output:** criteria met/unmet, commands/results, one risk, and next action.

Use this procedure twice and improve it from evidence. A persona such as “reviewer” is not a substitute for these operational steps.
