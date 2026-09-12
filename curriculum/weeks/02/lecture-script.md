# Week 2 Presenter Notes

Follow the 75m instruction, 45m demo, and 60m practice agenda in `talk-outline.md`.

## Opening
“Last week you tried the tools. Today we start fresh and make the process deliberate. The goal is not a perfect first answer; it is a result you can explain and verify.” Discuss two field-report examples without assuming every failure had the same cause.

## Prompt and Context
“‘Add a filter’ is a task. The data model, existing filter conventions, expected behavior, and test output are context.” Show the same request with missing and useful information. Have students identify what the agent should inspect next. Explain tokens and finite context through a small observed example; avoid claims tied to a particular model's current capacity.

## Instructions and Skills
“Project instructions describe how work should happen here. A skill describes how to perform a recurring procedure. Neither replaces executable checks.” Show the chosen tool's actual loading mechanism. Ask students to identify the input and output of the validation skill, then use it twice during the demo.

## In the Loop
“Right now, you inspect between small steps. Read the diff, run the check, investigate the result. The tool can execute commands, but you remain responsible for accepting the change.” Explain why working UI alone does not establish persistence or input handling.

## Practice Debrief
Ask each pair: Which function changed? Which check would catch an incorrect implementation? What remains uncertain? Close by linking the fresh-project homework and explaining that Week 3 moves supervision to longer checkpoints.
