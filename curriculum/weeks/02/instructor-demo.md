# Instructor Demo: Week 2 Validation Loop

**The Goal:** Demonstrate how to build a simple app (Terminal Pomodoro Timer) using the rigorous "Generate -> Validate -> Iterate" loop, rather than blindly accepting the first output.

## Step 1: The Context File & PRD
Show the students that you don't just open a chat box. You create a `GEMINI.md` (or `CLAUDE.md`) in your empty repo first.

```markdown
# Context
We are building a terminal-based Pomodoro Timer in Python.
- No external dependencies (use standard library `time`, `sys`, `os`).
- Must have a clear visual countdown.
- Must ring a bell (terminal bell `\a`) when time is up.
```

## Step 2: The First Prompt (Generation)
Open the AI tool and provide the first prompt.

**Prompt:** *"Read my GEMINI.md. Write the initial implementation in a single `pomodoro.py` file. Keep the logic simple."*

## Step 3: The Validation Loop (The most important part)
*Don't just copy and paste and move on.* Narrate your internal monologue:

1. **Read it:** "Okay, I see it's using a `while` loop and `time.sleep(1)`. That makes sense."
2. **Run it:** Execute `python pomodoro.py`.
3. **The Catch (Intentional Failure):** Let's say the countdown overwrites the whole terminal instead of clearing a single line, causing visual clutter. Or maybe the bell doesn't ring on Mac.
4. **Iterate (Surgical Prompting):** Do NOT say "it's broken, fix it." Say: *"The countdown logic works, but it's printing a new line every second. Modify the print statement to use `\r` (carriage return) so it overwrites the current line instead."*

## Step 4: The Final Review
Show them how to diff the changes. Validate that the AI *only* changed the print statement and didn't randomly refactor the rest of the code.

**Takeaway for Students:** "Notice how I spent more time reading and testing than the AI spent generating. That is the job now."
