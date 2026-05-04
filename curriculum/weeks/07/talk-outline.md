# Week 7: Infrastructure & CI/CD

## Talk Outline: From Code to Container
### Technical Deep Dive (75m)
- **Dockerizing with AI:** How to safely generate `Dockerfile` and `docker-compose.yml`.
- **The CI/CD Pipeline:** Prompting for GitHub Actions workflows.
- **AI Security Threats:** Understanding how AI often hallucinates insecure defaults (e.g., exposing internal ports, omitting CSRF tokens) and how to explicitly prompt for secure configurations.
- **Environment Parity:** Ensuring the AI understands the difference between local dev and production builds.

## Lab Instructions: Containerization
### Objective
Fully dockerize the Production-Grade Cloud Application (Backend, Frontend, and Database mock).

### Steps
1. **The Dockerfile:** Prompt the AI to create a multi-stage Dockerfile for the frontend (Stage 1: Node.js build, Stage 2: Nginx static serving) and an optimized Python 3.11 slim Dockerfile utilizing dependency caching for the backend.
2. **Compose:** Generate a `docker-compose.yml` that networks the backend, frontend, and a Postgres database container, injecting the `DATABASE_URL` into the backend via environment variables.
3. **CI Expansion:** Ask AI to update your GitHub Actions workflow to build and test the Docker images on every PR.
4. **The Log:** Document the infrastructure prompts in `docs/prompt-logs/week-07.md`.

### Deliverable
A PR containing the Docker configuration, allowing the mentor to run the full stack via `docker-compose up`.
