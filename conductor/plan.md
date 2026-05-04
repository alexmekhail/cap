# CAP 2.0: Agentic SDLC & Engineering Productivity

## 1. Educational Vision: Junior to Job-Ready AI Native Engineers
The goal of this program is to take junior engineers and turn them into AI-native, job-market-ready AI native engineers. Everything in the curriculum revolves around this transformation. The fundamental shift in modern software engineering is moving the "Human-in-the-loop" from *writer* to *architect/steer-er*. Modern SWE skill is measured by the ability to **manage the context window** and **recognize AI hallucinations** before they reach production. We are building Sovereign Engineers who direct AI to create production-ready systems, not passive consumers of code.

## 2. Project Archetypes: The Production-Grade Cloud Application
Students will spend 12 weeks building an end-to-end "Production-Grade Cloud Application." This architectural pattern is chosen because it is too complex for "one-shot" prompting, forcing students to master architectural boundaries across the stack.

**The Application Architecture:**
*   **Data/Event Ingestion:** Handling user inputs, webhooks, or external API streams.
*   **Business Logic Layer:** A Python backend for complex rules, transactions, and transformations.
*   **Persistence:** Cloud-native databases (PostgreSQL/Firestore).
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
*   **The Automated Linter:** An AI agent (GitHub Action) that automatically reviews PRs for Test Coverage, Security Vulnerabilities, and Prompt Quality (ensuring logs show iterative improvement).

## 4. AI-Augmented Mentorship
Mentorship is strictly high-leverage (architecture, cloud, prompting strategies).
*   **The "2-Hour Hatch":** A structured escalation path: 45m prompt strategy shift -> 90m reading logs manually -> 120m mentor intervention. All attempts must be documented.
*   **Standardized Rubrics:** Mentors grade on:
    1.  **Context Management:** Did the student provide the right data to the AI?
    2.  **Iterative Correction:** How many rounds did it take to fix a hallucination?
    3.  **Structural Oversight:** Did the student catch when the AI changed the architecture?

## 5. Master Schedule (12 Weeks)

### Phase 1: Foundations
*   **W1 | Setup:** Tools, Context, and AI-Native Setup (Native CLIs, Prompt Privacy).
*   **W2 | Ideation:** AI-Driven Ideation (Sounding boards, API contracts).
*   **W3 | Architecture:** Cloud E2E Design (ADRs, Starter Cloud Patterns: Scheduled Batch, Event-Driven Serverless, Stateful Container).

### Phase 2: Production
*   **W4 | Backend:** Code Gen (Python logic, steering, hallucination management).
*   **W5 | Frontend:** Code Gen (UI, state management, API integration).
*   **W6 | Quality:** Engineering Quality (AI-generated tests, linting, security scans).
*   **W7 | CI/CD:** Infrastructure (Dockerfiles, GitHub Actions).
*   **W8 | Livesite:** Deployment (GCP deployment, public URL).

### Phase 3: Mastery & Workflows
*   **W9 | Incident Response:** Break the app, use AI to analyze logs, write regression tests, and fix bugs.
*   **W10 | Industry Workflows:** Industry Expert Workflows (Guest lectures: Citizen vs. Pro).
*   **W11 | Interviews:** AI-Enabled SWE Interviews (Collaborative coding, Prompt audits).
*   **W12 | Demos:** Project Demos & Workflow Sharing.

## 6. Operational Cadence
*   **Workflow Reveal (45m):** A session showing how an experienced AI Native Engineer tackles the week's challenge using architectural rigor and hallucination catching.
*   **Core Instruction (75m):** Technical and prompting strategies tailored for junior engineers.
*   **Standups & Spot Checks (60m):** Reviewing student "Prompt Logs" and failure recoveries.

*(Note: Week 11 features a special guest session with two non-engineer speakers who successfully built apps from scratch using AI, highlighting alternative workflows and the democratization of app creation).*
ative workflows and the democratization of app creation).*
p creation).*
