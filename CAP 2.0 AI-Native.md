# **CAP 2.0: AI Native Software Engineering Residency**

## **Overview & Educational Vision**
The goal of this program is to take junior engineers and transform them into job-market-ready **AI Native Engineers**.

The fundamental shift in modern software engineering is moving the "Human-in-the-loop" from being a *writer* of code to an *architect and steer-er* of AI systems. Modern engineering skill is no longer just syntax memorization; it is measured by the ability to **manage the context window**, strictly enforce API contracts, and **recognize AI hallucinations** before they reach production.

This residency does not teach students how to be passive consumers of AI. It trains them to be Sovereign Engineers who command AI to build reliable, production-grade systems.

---

## **Program Goals & Constraints**

| Parameter | Description |
| :---- | :---- |
| **Entry Prerequisites** | Students must enter with basic programming logic (Python/JS), SQL fundamentals, and Git basics. This is not a "learn to code" bootcamp; it is a residency to master architectural AI steering. |
| **Duration** | 12 weeks total, structured progressively from Foundations to Mastery. |
| **Format** | Weekly core instruction paired with a long-running, complex take-home project. |
| **Mentorship** | High-leverage coaching capped at 30-60 mins per mentee weekly. Mentors focus on architecture and AI steering, not syntax debugging. |
| **The "2-Hour Hatch"** | Students must attempt to unblock themselves via AI for 2 hours, documenting their prompt strategy in a structured log, before requesting human mentor intervention. |

---

## **The Project: The Production-Grade Cloud Application**
To prevent students from relying on simple "one-shot" prompts, the residency develops an end-to-end **Production-Grade Cloud Application** from Week 4 through Week 12, following exploratory work in Weeks 1–3. This architecture is deliberately complex, forcing students to master architectural boundaries across the stack.

**The Application Architecture:**
1.  **Data/Event Ingestion:** Handling user inputs, webhooks, or external API streams.
2.  **Business Logic Layer:** A Python backend for complex rules, transactions, and transformations.
3.  **Persistence:** Cloud-native databases (PostgreSQL/Firestore).
4.  **Interface:** A dashboard or consumer UI interacting with the backend (Strict TypeScript).
5.  **Infrastructure:** Full Dockerization and automated CI/CD.

**Approved Domains (Students select one):**
*   **Content Streaming (Netflix Clone):** Video metadata ingestion, recommendation processing, and content UI.
*   **Marketplace (Airbnb Clone):** Property ingestion, booking conflict resolution, and search interface.
*   **Social Feed (Twitter Clone):** High-throughput tweet ingestion, timeline transformation, real-time feed UI.
*   **Ad Tech (Ads Auction System):** Real-time bidding ingestion, auction logic processing, advertiser reporting.
*   **Inventory (Library Management):** Tracking availability, managing checkout race conditions, librarian dashboard.
*   **Social Reading (Goodreads Clone):** Metadata ingestion, review processing, social graph visualization.
*   **Compliance (Legal Storage):** Secure document ingestion, metadata extraction (OCR/LLM), role-based UI.

---

## **The Standardized Agentic Workspace (SAW)**
Students work out of a unified repository environment that automatically enforces rigorous SDLC practices.
*   **Structure:** `/src`, `/tests`, `/infrastructure`, and specifically `/docs/prompt-logs`.
*   **The Automated Linter:** An AI-powered GitHub Action that automatically blocks Pull Requests failing to meet Test Coverage, Security, or Prompt Quality standards.

---

## **AI-Augmented Mentorship & Evaluation**
Mentors do not grade on whether the code compiles. To protect mentor capacity (limiting their involvement to 5-10 minutes per PR), we use a highly automated **"LLM-as-a-Judge"** pipeline.

**Automation Breakdown (80% AI / 20% Manual):**
*   **AI Auto-Grader:** A GitHub Action automatically parses the student's PR diff and mandatory **Prompt Logs**. It proposes evidence-backed, provisional 1-5 scores for mentor review in:
    1.  **Context Management:** Did the log show surgical file selection, or did they dump the whole repo?
    2.  **Iterative Correction:** Did they diagnose failures, establish effective automated checks, and intervene when those checks were insufficient?
*   **Manual Mentor Review:** The AI Grader outputs a "Mentor Time-Saver Summary," flagging specific architectural risks. The human mentor spends their 5-10 minutes verifying the final two dimensions:
    3.  **Structural Oversight:** Did the student strictly enforce architectural boundaries against the AI's tendency to write monolithic code?
    4.  **System Integrity:** Does the system actually perform under load, handle edge cases, and maintain security correctly without blind reliance on AI?

---

## **The 12-Week Progressive Curriculum**

### **Phase 1: Foundations (Weeks 1-4)**
*Focus: Establishing the baseline for AI collaboration, context management, and practical engineering skills.*
*   **W1 | Potential:** Guest Speakers & First Attempt (Practitioners demo real AI-built projects, students try AI coding unguided).
*   **W2 | Mechanics:** The Engine Room (How LLMs work technically, prompting patterns, context management, validation loops, workspace setup).
*   **W3 | Practice:** Working in the Wild (AI-assisted engineering in a large existing OSS codebase — code analysis, PRDs, surgical changes, testing).
*   **W4 | Harness:** The Flywheel (Agent supervision, API contracts, architecture decisions, relational integrity, migrations, and the first local capstone milestone).

### **Phase 2: Production (Weeks 5-8)**
*Focus: Building, testing, and deploying the core cloud application to ensure functional skills are gained.*
*   **W5 | Integration:** Strengthen the Week 4 capstone API and integrate the provided React/TypeScript frontend scaffold.
*   **W6 | Quality:** Engineering Quality (Pytest fixtures for 429/422 errors, coverage enforcement, security scans via `bandit`).
*   **W7 | CI/CD:** Infrastructure (Optimized multi-stage Dockerfiles, `docker-compose` networking, GitHub Actions).
*   **W8 | Livesite:** Deployment (Vercel frontend, GCP Cloud Run/AWS App Runner, strict IAM permission reviews, Cloud Cost Budgets).

### **Phase 3: Mastery & Workflows (Weeks 9-12)**
*Focus: Advanced operational debugging, interview prep, and workflow optimization.*
*   **W9 | Incident Response:** Break the app (e.g., N+1 queries, serialization crashes). Students must use AI to analyze raw stack traces, isolate the failure, and write regression tests before generating the fix.
*   **W10 | Workflow Audit:** Evaluate the capstone workflow using evidence from Weeks 1–9, test one improvement, and write a personal AI Workflow SOP.
*   **W11 | Interviews:** AI-Enabled SWE Interviews (Prompt audits of vulnerable code, refactoring with strict engineering constraints).
*   **W12 | Demos:** Project Demos & Workflow Sharing. Students present their live end-to-end pipelines and a "Prompt Case Study" showing Before/After code.

**Assessment alignment:** Week 1 uses the field-report rubric; Weeks 2–4 use their published assignment weights, with the shared engineering rubric supplying evidence anchors. Weeks 5–12 use the shared rubric. Credit verified outcomes, architecture decisions, and justified intervention; do not reward app size or penalize iteration count by itself.
