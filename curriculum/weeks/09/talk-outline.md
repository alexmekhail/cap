# Week 9: Incident Response & Analysis

## Talk Outline: When the AI is Wrong in Production
### Technical Deep Dive (75m)
- **Reading Logs with AI:** How to sanitize and feed production logs to an LLM.
- **The "Chaos" Mindset:** Intentionally breaking things to understand recovery.
- **Writing Bug Fixes:** Using AI to write the regression test *before* fixing the code.

## Lab Instructions: The Fire Drill
### Objective
Diagnose and fix an intentional bug injected into your pipeline.

### Steps
1. **The Sabotage:** Simulate a specific production failure: introduce an N+1 query problem, or modify data transformation logic so it occasionally returns a string instead of a float to trigger a FastAPI serialization crash.
2. **The Investigation:** Export the raw stack trace or slow query log. Paste the exact log into the LLM and prompt: "Analyze this stack trace, pinpoint the failing file/line, and generate a Pytest regression test that reproduces this failure before writing the code fix."
3. **The Fix:** Apply the generated fix and confirm the regression test passes.
4. **The Log:** Document the entire incident response process in `docs/prompt-logs/week-09.md`.

### Deliverable
A merged PR that fixes the bug, includes a regression test, and a detailed prompt log showing effective log analysis.
