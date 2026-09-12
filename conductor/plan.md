# CAP 2.0: Agentic SDLC & Engineering Productivity

## 1. Educational Vision: Junior to Job-Ready AI Native Engineers
The goal of this program is to take junior engineers and turn them into AI-native, job-market-ready AI native engineers. Everything in the curriculum revolves around this transformation. The fundamental shift in modern software engineering is moving the "Human-in-the-loop" from *writer* to *architect/steer-er*. Modern SWE skill is measured by the ability to **manage the context window** and **recognize AI hallucinations** before they reach production. We are building Sovereign Engineers who direct AI to create production-ready systems, not passive consumers of code.

## 2. Project Archetypes: The Production-Grade Cloud Application
Students explore in Week 1, build a fresh project in Week 2, modify an existing codebase in Week 3, and tackle an orchestration challenge in Week 4. From Week 5 through Week 12 they develop an end-to-end "Production-Grade Cloud Application." This architectural pattern is chosen because it is too complex for "one-shot" prompting, forcing students to master architectural boundaries across the stack.

**The Application Architecture:**
*   **Data/Event Ingestion:** Handling user inputs, webhooks, or external API streams.
*   **Business Logic Layer:** A Python backend for complex rules, transactions, and transformations.
*   **Persistence:** PostgreSQL for the shared production path; alternative persistence requires an explicit equivalent learning plan.
*   **Interface:** A dashboard or consumer UI interacting with the backend.
*   **Infrastructure:** Full Dockerization and CI/CD.

**Approved Project Options:**
Students must select one of the following domains to apply this pattern to:
1.  **Content Streaming (Netflix Clone):** Ingesting video metadata, processing recommendation algorithms, and a content discovery UI.
2.  **Marketplace (Airbnb Clone):** Managing property ingestion, booking conflict resolution (concurrency), and a search interface.
3.  **Social Feed (Twitter Clone):** High-throughput tweet ingestion, timeline generation (transformation), and a real-time feed UI.
4.  **Ad Tech (Ads Auction System):** Real-time bidding ingestion, auction logic processing, and an advertiser reporting dashboard.
5.  **Inventory (Library Management System):** Tracking book availability, managing checkout states (race conditions), and a librarian dashboard.
6.  **Social Reading (Goodreads Clone):** Book metadata ingestion, user review processing, and social graph visualization.
7.  **Compliance (Legal Document Storage System):** Secure document ingestion, metadata extraction (OCR/LLM transformation), and role-based access UI.

## 3. The Standardized Agentic Workspace (SAW)
A unified environment enforcing rigorous SDLC practices.
*   **Repo Structure:** `/src`, `/tests`, `/infrastructure`, `/docs/prompt-logs`.
*   **Automated checks:** The reference workflow runs tests, lint, static security/dependency checks, frontend build, and log-structure validation. It does not run an AI grader. See the starter README for setup.

## 4. AI-Augmented Mentorship
Mentorship is strictly high-leverage (architecture, cloud, prompting strategies).
*   **The "2-Hour Hatch":** Change approach around 45m, inspect evidence by 90m, and seek targeted help by 120m. Access, data-loss, security, and spending blockers should be raised immediately. Document the diagnosis and attempted checks.
*   **Standardized Rubrics:** Mentors grade on:
    1.  **Context Management:** Did the student provide the right data to the AI?
    2.  **Iterative Correction:** Did their checks expose meaningful failures, and were their interventions justified?
    3.  **Structural Oversight:** Did the student catch when the AI changed the architecture?

## 5. Master Schedule (12 Weeks)

### Phase 1: Foundations
*   **W1 | Inspiration:** Three nontechnical builders present finished work, workflow evolution, and lessons learned, followed by Q&A. No classroom project; setup and exploration happen at home.
*   **W2 | Guided Practice:** Build a fresh app in VS Code. Prompt versus context, instruction layers, project instructions, reusable skills, and the human-in-the-loop validation cycle.
*   **W3 | Sustained Agent:** Terminal workflows with one agent: context discovery, plans, checkpoints, skills, acceptance checks, and on-the-loop supervision. A 30-minute classroom exercise prepares students for substantial Excalidraw homework.
*   **W4 | Orchestration:** Coordinate agents through script-driven, instruction-driven, and hybrid harnesses. Define roles, connections, ownership, stopping rules, and integration checks; use a harness for an open-ended hard build.

### Phase 2: Production
*   **W5 | Production Entry:** Start a new cloud application or carry forward a suitable Week 4 project; establish architecture, data model, migrations, API contracts, and an integrated frontend.
*   **W6 | Quality:** Engineering Quality (AI-generated tests, linting, security scans).
*   **W7 | CI/CD:** Infrastructure (Dockerfiles, GitHub Actions).
*   **W8 | Livesite:** Deployment (GCP deployment, public URL).

### Phase 3: Mastery & Workflows
*   **W9 | Incident Response:** Break the app, use AI to analyze logs, write regression tests, and fix bugs.
*   **W10 | Workflow Audit:** Evaluate the capstone workflow using evidence from Weeks 1–9, test one improvement, and write a personal AI Workflow SOP.
*   **W11 | Interviews:** AI-Enabled SWE Interviews (Collaborative coding, Prompt audits).
*   **W12 | Demos:** Project Demos & Workflow Sharing.

## 6. Operational Cadence
*   **Workflow Reveal (45m):** A session showing how an experienced AI Native Engineer tackles the week's challenge using architectural rigor and hallucination catching.
*   **Core Instruction (75m):** Technical and prompting strategies tailored for junior engineers.
*   **Standups & Spot Checks (60m):** Reviewing student "Prompt Logs" and failure recoveries.

*(Note: Guest speakers have been moved to Week 1 to lead with inspiration before instruction).*

**Assessment alignment:** Week 1 uses the field-report rubric; Weeks 2–4 use their published assignment weights, with the shared engineering rubric supplying evidence anchors. Weeks 5–12 use the shared rubric. Credit verified outcomes, architecture decisions, and justified intervention; do not reward app size or penalize iteration count by itself.

## Weekly Materials and Delivery

The weekly folders are the source of classroom and assignment materials. Each week has a talk outline, presenter notes, a demo or speaker guide, slide source, student reference, and a separate authoritative homework document. Presenter notes and reference solutions are visible to students; use them openly and disclose reuse in submissions.

| Week | Start here | Homework |
|---|---|---|
| 1 | [Inspiration materials](../curriculum/weeks/01/README.md) | [Setup and first attempt](../curriculum/weeks/01/homework.md) |
| 2 | [Guided practice materials](../curriculum/weeks/02/README.md) | [A fresh application](../curriculum/weeks/02/homework.md) |
| 3 | [Terminal and sustained-agent materials](../curriculum/weeks/03/README.md) | [Excalidraw feature choice](../curriculum/weeks/03/homework.md) |
| 4 | [Orchestration materials](../curriculum/weeks/04/README.md) | [An open-ended hard build](../curriculum/weeks/04/homework.md) |
| 5 | [Week 5 materials](../curriculum/weeks/05/README.md) | [Assignment and assessment](../curriculum/weeks/05/homework.md) |
| 6 | [Week 6 materials](../curriculum/weeks/06/README.md) | [Assignment and assessment](../curriculum/weeks/06/homework.md) |
| 7 | [Week 7 materials](../curriculum/weeks/07/README.md) | [Assignment and assessment](../curriculum/weeks/07/homework.md) |
| 8 | [Week 8 materials](../curriculum/weeks/08/README.md) | [Assignment and assessment](../curriculum/weeks/08/homework.md) |
| 9 | [Week 9 materials](../curriculum/weeks/09/README.md) | [Assignment and assessment](../curriculum/weeks/09/homework.md) |
| 10 | [Week 10 materials](../curriculum/weeks/10/README.md) | [Assignment and assessment](../curriculum/weeks/10/homework.md) |
| 11 | [Week 11 materials](../curriculum/weeks/11/README.md) | [Assignment and assessment](../curriculum/weeks/11/homework.md) |
| 12 | [Week 12 materials](../curriculum/weeks/12/README.md) | [Assignment and assessment](../curriculum/weeks/12/homework.md) |

Week 2 introduces project instructions and skills with a small example; Week 3 develops them into tools for maintaining context across sustained work. Week 4 extends supervision to multiple agents. Gas Town is a possible instructor demonstration, not a required student purchase or a finalized course dependency. The instructor brings one working orchestrator setup and contrasts it with three harness designs.

The Week 4 problem need not become the production capstone. At Week 5, students may begin anew or continue if their project fits the production learning objectives. Do not assume a Week 4 Python backend, SQL schema, or migration history. Week 5 establishes a narrow slice and initial migration; Week 7 teaches follow-up migration and PostgreSQL transition.

**Entry and workload:** Students already run projects, use Git branches, read Python/JavaScript, debug basic errors, and know SQL fundamentals. They bring GitHub accounts and their own paid agents supporting VS Code and terminal from day one. All materials are shared in full on GitHub. Plan 5–10 hours of homework per week. Week 1 has a guest-session format; Weeks 2–4 retain the existing three-hour classroom planning envelope, with a 30-minute hands-on exercise in Week 3.

## Curriculum Ownership and Maintenance

Codex owns curriculum development and consistency across all 12 weeks: learning progression, technical accuracy, instructional pacing, presenter guidance, demos, student references, homework, assessment, and transitions into the production project and job preparation. The instructor sets direction through feedback; routine instructional and implementation decisions should be resolved without returning them as questions.

Maintain the existing repository structure. The root curriculum overview defines the program; this plan records delivery decisions; weekly folders contain the teaching and student materials. Homework documents are the authoritative assignment specifications. Keep schedules, outlines, notes, slides, references, and grading aligned whenever a decision changes.

For each week, check that students have been taught the prerequisites for the assignment, the work fits the 5–10 hour budget, the instructor has an actionable session guide, and assessment rewards demonstrable engineering understanding. Preserve the agreed progression through inspiration, guided practice, sustained single-agent work, and orchestration before production engineering. Do not equate autonomous execution with verified correctness.

Distinguish written demo plans from runnable, rehearsed demonstrations. Validate what can be checked locally and state remaining tool/account-dependent preparation precisely. All material is shared through GitHub; reference reuse must be disclosed rather than prevented through hidden materials.

Commit and push completed, verified revisions on the existing feature branch. Do not merge without the instructor's explicit authorization. Do not create separate planning documents that duplicate this structure. Ownership does not imply background work or scheduled runs; continue the curriculum work in active sessions and report outcomes and material limitations.

## Full-Course Review and Delivery Status

The complete 12-week sequence now has a weekly index, actionable outline, presenter notes, slide source, student reference, standalone homework, and instructor demo guide. Weeks 1–4 retain the agreed inspiration → guided VS Code → sustained terminal agent → orchestration progression. Week 5 starts or adapts one production slice; Week 6 defines quality and access; Week 7 covers PostgreSQL, follow-up migrations, and containers; Weeks 8–12 cover release, incident response, workflow improvement, interviews, and portfolio defense.

The supplied production reference includes a working React/TypeScript and FastAPI/SQLAlchemy inventory slice, initial Alembic migration, seed command, tests, Docker/Compose configuration, dependency locks, and a copyable CI workflow. It uses synthetic data and intentionally leaves production authentication/authorization to the Week 6 access decision. The workflow performs deterministic checks and log-structure validation; LLM-assisted assessment remains a separate, optional mentor procedure.

Local verification covers all weekly material links and rubric totals, the single-agent failure/recovery fixture, harness handoff checks, the authorization exercise, backend tests/coverage/lint/static security, dependency audits, frontend build, and browser create/reload/error behavior. Hosted CI additionally builds and exercises the PostgreSQL container reference. Check its result for the reviewed commit before treating that path as verified.

### Cohort Preparation Still Required
- Confirm three Week 1 speakers and permission to publish their materials.
- Verify the cohort's chosen agent access in VS Code and terminal, and rehearse the provider-specific Week 4 adapter/orchestrator. The included harness replay is explicitly not live AI execution.
- Pin and rehearse an Excalidraw checkout before Week 3; record its commands and baseline results rather than assuming upstream setup remains unchanged.
- Rehearse the selected cloud account/project, runtime identity, managed database, and budget configuration before Week 8. No cloud deployment is performed by editing this curriculum.
- Publish the Week 12 presentation order and use parallel review groups when cohort size exceeds the single-room capacity.

These are delivery prerequisites involving guests, cohort tools, or live infrastructure. They are distinguished from the repository review and locally executable reference checks rather than represented as already completed.
