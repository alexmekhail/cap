# Week 4 Lecture Script: "The Harness"

*This is your detailed speaking guide for the Week 4 lecture.*

## 1. The Paradigm Shift: In-the-Loop vs. On-the-Loop (15 mins)
**Speaker Notes:** Introduce the core concept of agentic workflows.
- "For the past 2 weeks, you have been 'In-the-Loop'. You write a prompt, wait for the AI, read the output, validate it, and write the next prompt. You are turning the crank manually. This is exhausting at scale."
- "Today, we move 'On-the-Loop'. You define the goal, the constraints, and the validation criteria. The AI executes in a loop autonomously. You supervise, review, and intervene only when the AI gets stuck."
- "This is the difference between being a bricklayer and being an architect. You are no longer writing the code; you are building the *harness* that ensures the AI writes good code."

## 2. The Flywheel Concept (10 mins)
**Speaker Notes:** Explain the mechanics of autonomous generation.
- "An agent needs a Flywheel to operate. The Flywheel consists of three parts:"
  1. **Context/Instructions:** What are the rules?
  2. **The Agent:** The LLM executing the code.
  3. **The Validation Layer:** Automated checks (tests, linters) that tell the agent if it succeeded or failed.
- "If the tests fail, the agent reads the error and tries again. Your job is to build the flywheel, push it, and watch it spin."

## 3. Building the Harness: The Context File (10 mins)
**Speaker Notes:** Deep dive into configuration.
- "Your `GEMINI.md` or `CLAUDE.md` is no longer just a description. It is the agent's brain."
- "You must write it like a configuration file. Specify the exact tech stack, the architectural patterns, and strict rules (e.g., 'All functions must have type hints', 'No raw SQL queries')."
- "If the agent hallucinates, you don't just fix the code. You fix the *harness*. You update `GEMINI.md` to say 'NEVER do X again.' Then add a check that can detect recurrence; instructions alone do not guarantee compliance."

## 4. The Safety Net: Automated Validation (10 mins)
**Speaker Notes:** Why tests are non-negotiable in agentic workflows.
- "You cannot run an autonomous agent without a safety net. If you don't have tests, the agent will confidently write garbage and tell you it succeeded."
- "Before you ask the agent to build a feature, *you* (or the agent) must write the test for it. This is Test-Driven Development (TDD) for AI."
- "We use linters (like Ruff or ESLint) and type checkers (like Mypy or TypeScript). These act as automated mentors, slapping the agent's wrist when it makes a syntax mistake so you don't have to."

## 5. Modeling Data Without Users (5 mins)
**Speaker Notes:** A crucial skill for building realistic prototypes.
- "You are about to build a massive capstone project. But you have no real users. A demo with 3 hardcoded users looks like a toy."
- "We use AI to write seed scripts (using libraries like Faker). We can generate 500 realistic users, 2,000 orders, and 10,000 log entries in seconds."
- "Use the data to test relationships, invalid inputs, and query behavior. Record counts alone do not prove production readiness."

*(Proceed to Instructor Demo of the Agentic Harness)*

---

## 6. Capstone Design Checkpoint (25 mins, including the short demo)

- Continue this repository from Week 4 through Week 12.
- Use FastAPI, SQLAlchemy, Alembic, and local SQLite; integrate the provided UI in Week 5.
- Before generation: review an architecture ADR, API contract, and relational schema.
- Demonstrate a migration that preserves seeded data and a check that catches a real failure.
- Stop for unexplained failures, weakened tests, or changes outside the plan.
- Grade engineering judgment and verification, not app size.
