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

## Reusable Skill: Validate a Small Change
**Input:** task criteria, changed files, known baseline, and working check commands.
1. Compare the diff with the requested behavior; identify unrelated changes.
2. Run the relevant checks and compare failures with the baseline.
3. Exercise one success and one failure case manually.
4. Inspect whether tests meaningfully assert the intended behavior.
5. Report evidence and limits; do not claim unrun checks passed.
**Output:** criteria met/unmet, commands/results, one risk, and next action.

Use this procedure twice and improve it from evidence. A persona such as “reviewer” is not a substitute for these operational steps.
