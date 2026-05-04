# Week 5: Backend API & Pre-Built UI Integration

## Talk Outline: The API Contract
### Technical Deep Dive (75m)
- **FastAPI & Pydantic:** Building strict API boundaries.
- **Network Resilience:** Handling timeouts and retries using `httpx` and `tenacity`.
- **Integrating the UI Scaffold:** Why we use a pre-built React template to avoid frontend scope creep.

## Lab Instructions: The Logic Engine
### Objective
Use AI to generate a FastAPI service and hook it up to the provided React frontend scaffold.

### Steps
1. **The Interface First:** Prompt the AI to define Pydantic schema models for your data with explicit typing and constraints (e.g., `EmailStr`, string length limits).
2. **The Fetcher:** Generate a Python `httpx` client wrapper to hit an external public API. Prompt the AI to include explicit timeout handling and retry logic using the `tenacity` library.
3. **UI Integration:** Using the pre-built React/Next.js dashboard scaffold in `/src/frontend`, ask the AI to write a React Query hook to securely fetch your new FastAPI endpoints.
4. **The Log:** Document the integration process in `docs/prompt-logs/week-05.md`.

### Deliverable
A working FastAPI backend serving data to the pre-built frontend scaffold.
