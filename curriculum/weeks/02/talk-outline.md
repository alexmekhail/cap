# Week 2: Guided Practice — Building in VS Code

## Learning Goals
Start a fresh application, supply useful context, inspect and validate generated changes, and explain one correction. Introduce project instruction files and one reusable skill this week.

## Core Instruction (75m)
- **From Week 1 to a deliberate workflow (10m):** Use field reports to distinguish unclear requirements, missing context, environment errors, and implementation defects.
- **Prompt versus context (20m):** A prompt specifies the current task; context includes relevant code, examples, constraints, and tool results. Explain tokenization and context limits using observed examples, without relying on a fixed model limit or a guaranteed failure.
- **Instruction layers and skills (20m):** Distinguish tool-controlled system instructions, project guidance, and task requests. Create the instruction file supported by the chosen agent and explicitly verify it is used. Introduce a reusable validation skill with inputs, steps, and expected output.
- **Human in the loop (25m):** Request → inspect diff → run checks → diagnose → correct. Teach when to ask for a plan and how to verify an agent's claim. Explain that on-the-loop supervision will move decisions to checkpoints in Week 3.

## Instructor Demonstration (45m)
Build a fresh local task-board app in VS Code using the [demo guide](instructor-demo.md). Students see files, diffs, commands, and results together. Use one supported agent for the demonstration; students may use their own.

## Student Practice and Review (60m)
Students implement a small change in their own fresh app (40m), then pair-review one decision and its evidence (20m). Keep the focus on deliberate interaction rather than autonomous long runs.

## Assignment
See [homework.md](homework.md) for the fresh-project task, submission requirements, and rubric. The [reference](reference.md) includes reusable instruction and skill examples.
