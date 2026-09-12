---
marp: true
theme: default
paginate: true
style: |
  section {
    background-color: #f8f9fa;
    font-family: 'Inter', sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
---

# Week 4: The Harness
## From In-the-Loop to On-the-Loop

---

# The Paradigm Shift

- **In-the-Loop (Weeks 2-3):** You prompt → AI responds → you validate → you prompt. You turn the crank manually.
- **On-the-Loop (Today):** You define the goal, constraints, and validation. AI executes autonomously. You supervise.
- You are no longer writing the code; you are building the *harness* that ensures the AI writes good code.

---

# The Flywheel ⚙️

An agent needs a Flywheel to operate safely:

1. **Context/Instructions:** What are the rules?
2. **The Agent:** The LLM executing the code.
3. **The Validation Layer:** Automated checks (tests, linters) that tell the agent if it succeeded or failed.

---

# Building the Harness: Context

- `GEMINI.md` or `CLAUDE.md` is no longer just a description. It is the agent's brain.
- Specify exact tech stack, architectural patterns, and strict rules.
- If the agent hallucinates, don't just fix the code. **Fix the harness.** Update the instructions and add a regression check; verify the behavior on the next run.

---

# The Safety Net: Validation

- You cannot run an autonomous agent without a safety net.
- If you don't have tests, the agent will confidently write garbage and tell you it succeeded.
- **TDD for AI:** Write the test first. If the test fails, the agent reads the error and tries again.
- Use linters and type checkers as automated mentors.

---

# Modeling Data Without Users

- A demo with 3 hardcoded users looks like a toy.
- Use AI to write seed scripts (e.g., Faker).
- Generate 500 users, 2,000 orders, and 10,000 logs in seconds.
- Use the data to test relationships and query behavior; counts alone do not prove production readiness.

---

# Instructor Demo

Building an Agentic Flywheel...

---

# Capstone Design Checkpoint

- Continue this repository from Week 4 through Week 12.
- Use FastAPI, SQLAlchemy, Alembic, and local SQLite; integrate the provided UI in Week 5.
- Before generation: review an architecture ADR, API contract, and relational schema.
- Demonstrate a migration that preserves seeded data and a check that catches a real failure.
- Stop for unexplained failures, weakened tests, or changes outside the plan.
- Grade engineering judgment and verification, not app size.
