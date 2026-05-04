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
Ensure you have documented your initial environment setup context in this file before asking AI to generate your first lines of code.
