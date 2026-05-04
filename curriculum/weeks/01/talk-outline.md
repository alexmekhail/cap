# Week 1: Tools, Context, and AI-Native Setup

## Talk Outline: The Architect's Desk
### Technical Deep Dive (75m)
- **Writer vs. Steer-er:** The paradigm shift in modern software engineering.
- **Native Package Managers:** Why installing AI CLIs via `brew` or `apt` prevents pathing errors compared to raw HTTP installs.
- **Managing the Context Window:** How to feed AI the *right* data without overwhelming it.
- **Hyper-Specific Prompt Privacy:** Redaction protocols and data security. You must explicitly scrub GCP service account JSONs, billing IDs, and internal network paths before prompting.
- **The SAW Setup:** Introduction to the Production-Grade Cloud Application repository.

## Lab Instructions: Context Initialization
### Objective
Set up your local AI environment and establish your initial project context.

### Steps
1. **Tooling:** Install your native AI CLI or IDE extension (e.g., Gemini CLI, Copilot).
2. **The Context File:** Create a `AI_CONTEXT.md` or `CLAUDE.md` in your workspace. Define the core parameters of your Cloud Application (e.g., Python backend, GCP target).
3. **The First Prompt:** Use AI to generate a `.gitignore` and `requirements.txt` specifically tailored for a cloud application backend.
4. **The Log:** Document this first interaction in `docs/prompt-logs/week-01.md`.

### Deliverable
A configured local environment and a PR containing your base repository structure and first prompt log.
irst prompt log.
t log.
