# Week 4 Presenter Notes

Use `talk-outline.md` for the 75m instruction, 45m demo, and 60m workshop.

## Control Modes
“Last week we gave one agent a sustained task and supervised its checkpoints. Today we coordinate responsibilities. More agents do not remove the need for someone to own the goal, interfaces, and final acceptance.”

## What Makes an Agent Useful?
“‘You are a brilliant designer’ gives a perspective. It does not specify the input, deliverable, allowed files, recipient, tests, or stopping point.” Build one agent contract with the class. Ask what would happen if two agents changed the same interface differently.

## Harness Designs
“In the script-driven version, code decides the stages. In the instruction-driven version, the workflow document guides orchestration. In the hybrid, the supervisor generates helper code but remains responsible for what happens next.” Use the same task in all three so the comparison is about control rather than app complexity.

## Connections and Failure
Draw the task dependencies and ownership boundaries. Show how handoff evidence differs from a worker saying ‘done.’ Discuss timeouts, repeated failure, missing context, conflicting work, and changes to acceptance tests. Teach independent verification of the integrated application.

## Homework Briefing
“Build a paint app—or an equivalently hard application. You define the product contract, use a harness, and show your evidence. We assess the product, coordination, checks, and your engineering defense. You may continue in Week 5 or start fresh.”
