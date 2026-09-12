# Standardized Agentic Workspace (SAW)

## The Architect/Steer-er Protocol
As an engineer in CAP 2.0, you are not writing code from scratch; you are steering AI. To do this safely, you must follow the SAW protocol:

1.  **Prompt Privacy:** NEVER send proprietary data, PII, or internal credentials to an external LLM. Redact all secrets before prompting.
2.  **The Prompt Log:** You must maintain a log of your prompts in `docs/prompt-logs/`. This is how mentors evaluate your Context Management and Iterative Correction skills.
3.  **Verification First:** Do not merge AI code that lacks tests. The Automated Agentic Linter will reject PRs that lower test coverage.

## Project: Production-Grade Cloud Application
This repository will house your 12-week project.
- `/src`: Backend Python logic and Frontend UI.
- `/tests`: Verification suites.
- `/infrastructure`: Dockerfiles and CI/CD.
- `/docs/adrs`: Your Architectural Decision Records.

## Getting Started
From Week 2 onward, record your environment and verification commands here and explicitly provide this file to your chosen agent, or use its supported instruction-file mechanism. Week 1 uses a lightweight exploratory setup and field report instead. Instructions guide behavior; executable checks and review verify it.
