# Week 2: Guided Practice — Building in VS Code

## Learning Goals
Start a fresh application, supply useful context, inspect and validate generated changes, and explain one correction. Introduce project instruction files and one reusable skill this week.

## Core Instruction (75m)
- **From Week 1 to a deliberate workflow (10m):** Use field reports to distinguish unclear requirements, missing context, environment errors, and implementation defects.
- **Prompt versus context (20m):** A prompt specifies the current task; context includes relevant code, examples, constraints, and tool results. Explain tokenization and context limits using observed examples, without relying on a fixed model limit or a guaranteed failure.
- **Instruction layers and skills (20m):** Distinguish tool-controlled system instructions, project guidance, and task requests. Create the instruction file supported by the chosen agent and explicitly verify it is used. Introduce a reusable validation skill with inputs, steps, and expected output.
- **Human in the loop (25m):** Request → inspect diff → run checks → diagnose → correct. Teach when to ask for a plan and how to verify an agent's claim. Explain that on-the-loop supervision will move decisions to checkpoints in Week 3.

## Instructor Demonstration Plan (45m)
### Preparation
Use your paid agent's VS Code integration and a new repository. Rehearse one simple browser app with local persistence. Prepare a starting checkpoint, a working checkpoint, and a deliberately broken persistence example; share those checkpoints on GitHub once prepared. Verify installation and check commands on the machine used in class.

### Live Sequence
1. **Specify (5m):** “Build a local task board: add a task, mark it complete, and retain it after reload. Reject blank tasks.” Keep this visible as the acceptance contract.
2. **Context and instructions (8m):** Ask for a file plan, inspect it, and write the chosen tool's project instructions. Show the distinction between that file and the current task prompt.
3. **Build interactively (12m):** Generate one small change at a time. Show diffs and run the app. Explain one generated function rather than narrating every line.
4. **Validate and correct (12m):** Use the [validation procedure](reference.md#reusable-skill-validate-a-small-change). Check blank input and reload behavior. If the live build has no defect, clearly label the prepared broken example and demonstrate diagnosis; do not pretend it was generated live.
5. **Reuse and debrief (8m):** Add a small filter and invoke the same skill again. Ask what was reusable, what context changed, and what evidence justified accepting the result.

This is an in-the-loop demonstration. Terminal commands may appear inside VS Code, but sustained terminal-agent supervision is the Week 3 focus. Students start their own fresh homework projects.

## Student Practice and Review (60m)
Students implement a small change in their own fresh app (40m), then pair-review one decision and its evidence (20m). Keep the focus on deliberate interaction rather than autonomous long runs.

## Assignment
See [homework.md](homework.md) for the fresh-project task, submission requirements, and rubric. The [reference](reference.md) includes reusable instruction and skill examples.
