# Week 3 Lecture Script: "Working in the Wild"

*This is your detailed speaking guide for the Week 3 lecture.*

## 1. The Reality of Software Engineering (10 mins)
**Speaker Notes:** Set the stage. Burst the "greenfield" bubble.
- "In Week 2, you built something from scratch. That is called 'greenfield' development. It's fun, it's fast, and it is almost *never* what you do in the real world."
- "Real engineering is 'brownfield'. You land in a codebase with hundreds of thousands of lines of code. You didn't pick the framework, you don't understand the naming conventions, and the original author left the company three years ago. Your job is to add a feature without breaking everything else."
- "The #1 challenge for a junior engineer is the 'Onboarding Problem'—figuring out where to even start. Fortunately, this is what AI is best at."

## 2. AI-Assisted Codebase Navigation (15 mins)
**Speaker Notes:** Teach them how to use AI as an exploration tool, not just a typing tool.
- **The Architecture Prompt:** "When you open a massive repo, your first prompt shouldn't be to write code. It should be: *'Explain the architecture of this project. What are the main modules and how do they interact?'*"
- **Dependency Tracing:** "You need to find the thread. Ask the AI: *'I clicked a button on the UI. Trace the flow from the React component, through the API, down to the database write.'*"
- **Finding the Blast Radius:** "Before you change a file, you must know what it impacts. *'If I modify this data model, what other files will break?'*"

## 3. The "Just Rewrite It" Trap (10 mins)
**Speaker Notes:** A critical warning about AI behavior.
- "AI hates messy, legacy code. If you ask it to fix a bug in a 500-line function, its instinct is to delete the whole function and rewrite it 'cleanly'. **Do not let it do this.**"
- "Working code is valuable because it has survived edge cases. If you let the AI rewrite it, you are throwing away years of bug fixes."
- "The goal is *surgical changes*. You must explicitly tell the AI: *'Modify ONLY lines 40-50. Do not refactor the rest of the file.'*"

## 4. The PRD → Implement → Validate Loop (15 mins)
**Speaker Notes:** How to execute a feature in a massive repo.
- **Write the PRD First:** "In a massive codebase, you cannot wing it. Before touching code, write a 3-sentence Product Requirements Document. What are we changing? Why? What is the exact acceptance criteria?"
- **Implementation with Guardrails:** "When generating code, you must give the AI the existing file and say, 'Here is the file. Here is my PRD. Show me ONLY the diff of what needs to change.'"
- **Validation is King:** "How do you know you didn't break the app? You run the existing test suite. Compare failures with your baseline. Inspect the changed behavior and environment before deciding whether to correct or revert the change. A failed test alone does not identify the cause."

## 5. Common Hallucination Traps in Big Codebases (10 mins)
**Speaker Notes:** Prepare them for what they will face in the lab.
- **Global Refactoring:** "The AI will randomly decide to change tabs to spaces, or rename variables across the file. Catch this in your diff review."
- **Invented APIs:** "The AI will assume a helper function exists because it 'usually' exists in similar frameworks. It will hallucinate `utils.formatDate()` and your code will crash. Always verify imports."
- **Ignoring Project Patterns:** "If the project uses Redux for state, but the AI likes Zustand better, it will try to write Zustand code. You must force the AI to respect the existing architectural patterns."

*(Proceed to Instructor Demo using Lobe Chat)*

## Assignment Brief (15 mins)
Walk through `comments-brief.md`: one comment, scene anchoring, local persistence, and drawing isolation. Demonstrate expected pan/zoom behavior with a sketch. Explain the 4–6 hour timebox, core validation evidence, and optional extensions.
