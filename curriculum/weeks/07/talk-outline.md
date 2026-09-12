# Week 7: Infrastructure & CI/CD

## Talk Outline: From Code to Container
### Technical Deep Dive (75m)
- **Dockerizing with AI:** How to safely generate `Dockerfile` and `docker-compose.yml`.
- **The CI/CD Pipeline:** Prompting for GitHub Actions workflows.
- **AI Security Threats:** Understanding how AI often hallucinates insecure defaults (e.g., exposing internal ports, omitting CSRF tokens) and how to explicitly prompt for secure configurations.
- **Persistence transition:** Apply the Week 5 migrations to an empty PostgreSQL database, seed it, and test constraints and query behavior. Document dialect differences; verify record counts and key relationships if transferring existing SQLite records.
- **Environment Parity:** Ensuring the AI understands the difference between local dev and production builds.

## Lab Instructions: Containerization
### Objective
Fully dockerize the Production-Grade Cloud Application (Backend, Frontend, and Database mock).

### Steps
1. **The Dockerfile:** Prompt the AI to create a multi-stage Dockerfile for the frontend (Stage 1: Node.js build, Stage 2: Nginx static serving) and an optimized Python 3.11 slim Dockerfile utilizing dependency caching for the backend.
2. **Compose:** Generate a `docker-compose.yml` that networks the backend, frontend, and a Postgres database container, injecting the `DATABASE_URL` into the backend via environment variables.
3. **Database verification:** Run migrations and the backend tests against PostgreSQL. Record migration, seed, and integrity evidence; do not assume SQLite passing results transfer unchanged.
4. **CI Expansion:** Ask AI to update your GitHub Actions workflow to build and test the Docker images on every PR.
5. **The Log:** Document the infrastructure prompts in `docs/prompt-logs/week-07.md`.

### Deliverable
A PR containing the Docker configuration, allowing the mentor to run the full stack via `docker-compose up`.
