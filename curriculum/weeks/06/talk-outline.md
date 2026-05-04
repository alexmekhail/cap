# Week 6: Engineering Quality

## Talk Outline: Verification as Sovereignty
### Technical Deep Dive (75m)
- **AI-Generated Testing:** How to ask AI for *meaningful* tests, not just coverage theater.
- **Edge Case Hunting:** Prompting AI to find flaws in its own code.
- **Automated Security:** Integrating tools to catch hallucinated secrets or vulnerable packages.

## Lab Instructions: The Quality Gate
### Objective
Use `pytest` and `pytest-cov` to achieve 80%+ coverage, and configure a GitHub Action to fail the build if coverage drops below this threshold or if `bandit`/`trufflehog` detects vulnerabilities.

### Steps
1. **Test Generation:** Prompt the AI to write a Pytest fixture that simulates a HTTP 429 "Too Many Requests" error and an incomplete JSON payload. Assert that your FastAPI backend correctly handles these with HTTP 422/400 status codes without crashing.
2. **The Coverage Run:** Run your local test suite. Iterate with the AI until coverage is acceptable.
3. **The Push:** Push to GitHub and trigger the `agentic-linter.yml`.
4. **The Log:** Document in `docs/prompt-logs/week-06.md` how the AI handled writing tests for edge cases.

### Deliverable
A green build in GitHub Actions proving test coverage and 0 security vulnerabilities.
