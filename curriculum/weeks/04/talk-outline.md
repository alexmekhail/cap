# Week 4: "The Harness"
## From In-the-Loop to On-the-Loop

**Goal:** Students learn to configure AI agents that work autonomously within guardrails — the "flywheel." They compare manual and automated validation, then choose where agent autonomy is appropriate using evidence from a local capstone milestone.

> ⚠️ **The shift:** Weeks 1–3 you were IN the loop — prompting, reading, validating, iterating manually. This week, you set up the system so AI operates in a loop and you SUPERVISE. You're the architect, not the builder.

---

## Talk Outline (75m)

### Part 1: The Concept — In-the-Loop vs. On-the-Loop (15m)
- **In-the-loop:** You prompt → AI responds → you validate → you prompt again. Every iteration requires your attention. This is where you've been.
- **On-the-loop:** You define the goal, the constraints, and the validation criteria. AI executes in a loop. You review outputs and intervene only when needed. This is where the industry is going.
- **The Flywheel:** Context file → Agent instructions → Automated validation (tests, linting) → AI iterates until green. Your job is to build the flywheel, not to turn it by hand.
- **When NOT to use the harness** — Exploratory work, security-critical code, novel architecture decisions. The harness is for known patterns at scale.

### Part 2: Building the Harness (20m)
- **The Context File as Configuration:**
  - `GEMINI.md` / `CLAUDE.md` — not just a description, but *instructions* for the agent
  - Coding standards, forbidden patterns, required testing, architectural constraints
  - Live demo: writing a context file that actually constrains agent behavior
- **Agent-Mode Tools:**
  - Gemini CLI agent mode
  - Claude Code with extended thinking
  - Cursor/Windsurf in agent mode
  - How they differ from chat: they read files, run commands, iterate on errors automatically
- **The Validation Layer — Your Safety Net:**
  - Automated tests (pytest, jest) — if the agent's code doesn't pass, it tries again
  - Linting (ruff, eslint) — enforce style automatically
  - Type checking (mypy, tsc) — catch structural errors
  - The agent works within a stated retry/time budget and stops for unexplained failures or changes outside scope
- **Live Demo:** Instructor uses the supplied seed-data fixture with executable acceptance tests and configured linting. The agent works autonomously. Instructor narrates what's happening and when to intervene.

### Part 3: Architecture, Contracts & Data (25m)
- **Design checkpoint (10m):** Select an approved course domain. Draw the UI → API → business logic → database boundaries. Write `docs/adrs/001-architecture.md` comparing a simple stateful application with batch and event-driven alternatives; defer the provider decision to deployment preparation. Draft an OpenAPI contract with request/response validation and error cases before generation.
- **Data checkpoint (10m):** Model primary/foreign keys, uniqueness, deletion behavior, and an index justified by a real query. Create an initial Alembic migration and demonstrate a subsequent schema change against seeded data without losing records. Discuss what must be revalidated when moving from SQLite to PostgreSQL in Week 7.
- **Seed-data exercise (5m):** Generate varied, reproducible records and one edge case that exposes a bug.
- **The Test User Problem** — Your apps don't have real users. So how do you build something user-facing?
- **Seed Data & Factories:**
  - Using AI to generate realistic seed data (faker, factory_boy)
  - Creating 100+ test users with diverse profiles in seconds
  - Seeding a SQLite or PostgreSQL database with meaningful data
- **Why This Matters** — Record counts help exercise behavior; they do not establish production readiness. Validate relationships, invalid inputs, and query behavior.
- **Live Demo:** Use AI agent to scaffold a user model, generate seed data, and populate a database.

### Part 4: The Capstone Kickoff (15m)
- What you're building (see assignment below)
- Architecture walkthrough
- How to structure your harness for this specific build
- Timeline and checkpoints

---

## Capstone Assignment: "The Full Build"

### Objective
Build a **substantial, multi-component application** using the harness/flywheel approach. This is the first local milestone of the same capstone you will improve and present in Week 12. It demonstrates architecture decisions, automated checks, and supervised implementation.

### The Application
Choose one approved domain from the master curriculum and build a narrow full-stack slice. Keep this repository through Week 12. Use the shared stack so later labs build on your work:


1. **A SQLite database** with at least 4 related tables (SQLAlchemy with Alembic migrations)
2. **A Python backend** (FastAPI) with RESTful endpoints for CRUD operations
3. **A simple frontend** (HTML/JS or a lightweight framework) that consumes the API
4. **Seed data** — at least 100 test users and proportional associated data, generated programmatically (faker / factory_boy)
5. **A test suite** — at least 10 meaningful tests, including invalid input, relational constraints, and a regression for a demonstrated failure
6. **A context file** for your chosen agent that records architecture boundaries, commands for tests/lint/type checks, and intervention rules
7. **Design artifacts** — the architecture ADR, API contract, schema diagram, and initial plus follow-up migration with data-preservation evidence

The table/user/test counts are scope targets, not separate quality scores. Agree a smaller equivalent scope with the mentor where it provides the same evidence.

### Checkpoints and Continuation
- **Before generation:** Review the ADR, contract, schema, and acceptance tests.
- **Midweek:** Demonstrate one complete API-to-database workflow and a check that catches a real failure.
- **End of week:** Show the local UI, migration evidence, and a clean validation run. Budget 6–8 hours outside class; document unfinished work and prioritize the core slice with your mentor.
- **Next:** W5 strengthens the API and replaces or integrates the simple UI with the provided React/TypeScript scaffold; W6 adds quality gates; W7 migrates to PostgreSQL and containerizes; W8 deploys.

### The Harness Requirement
You must document **how you used the harness approach**:
- Show your context file
- Show your agent session (prompt logs or session recordings)
- Highlight moments where the agent iterated autonomously vs. where you intervened, and justify both
- Set a retry/time budget. Stop for unexplained failures, destructive migrations, changed acceptance tests, or new dependencies outside the agreed plan; inspect the diff before resuming
- Treat context instructions as guidance; enforce checks with executable commands and review any changes to those checks
- Reflect: what worked, what didn't, what you'd change about your harness setup

### Deliverable
- GitHub repo with all code, seed data scripts, tests, and context file
- `docs/prompt-logs/week-04.md` — the most detailed log yet
- A brief written reflection (1 page): "How I set up my harness and what I learned"

### Grading Focus

| Dimension | Weight |
|---|---|
| **Application Completeness** — Does it work end-to-end? | 25% |
| **Harness Quality** — Is the context file well-crafted? Did tests catch real errors? | 25% |
| **Engineering Judgment** — Justified architecture and data decisions; verified migrations and meaningful failure detection | 25% |
| **Reflection Quality** — Honest assessment of harness strengths/weaknesses | 25% |
