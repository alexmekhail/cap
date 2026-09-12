# CAP Production Reference Starter

A small inventory application: React/TypeScript → FastAPI → SQLAlchemy → SQLite locally, with Alembic and a PostgreSQL/Compose exercise. Copy the **contents of this folder**, including dotfiles, into your own new repository. Do not nest it under another directory unless you adjust workflow paths.

This is a teaching reference, not a finished production system. It has no authentication or per-user authorization. Use synthetic data only. Week 6 must establish the access model before any public write endpoint is deployed. The reference UI lists up to 50 records; edit/delete, pagination, authorization, and domain behavior are student work.

## Local Setup
Use Python 3.12+ and Node 22.12+ (Node 24 is used in the container).

```sh
python3 -m venv .venv
source .venv/bin/activate
python -m pip install -r requirements-lock.txt
alembic upgrade head
python -m src.backend.seed
uvicorn src.backend.app:app --host 127.0.0.1 --port 8000
```

In a second terminal, from `src/frontend`:

```sh
npm ci
npm run dev
```

Open the local Vite URL. Its `/api` proxy targets port 8000. Add an item and reload. API documentation is at `/docs` on the backend. Export the OpenAPI document as your contract baseline and review changes to it.

## Checks
From the repository root with the virtual environment activated:

```sh
pytest --cov=src/backend --cov-fail-under=80
ruff check src/backend tests
bandit -r src/backend -q
python tools/check_prompt_logs.py
```

The log check intentionally fails until you add an actual `docs/prompt-logs/week-05.md`; the template alone is not evidence. Dependency audits in CI require network access. From `src/frontend`, run `npm run build` to type-check and bundle. The committed Python and npm lockfiles record the reviewed environment. Regenerate them deliberately when updating dependencies and rerun the checks. `requirements.txt` and `requirements-dev.txt` describe the intended dependency bounds.

## Migration Exercise
Create a revision with `alembic revision -m "add item description"`, inspect it, and implement an additive nullable description column. Seed an item before upgrading; verify its ID/name/category afterward. Decide how older app versions behave. Practice on disposable data before considering rollback. Never use a destructive downgrade as a substitute for a recovery plan.

## Week 7: Local PostgreSQL and Containers
With Docker available, from the root:

```sh
docker compose build
docker compose up -d db
docker compose run --rm app alembic upgrade head
docker compose run --rm app python -m src.backend.seed
docker compose up -d app
```

Open `http://127.0.0.1:8080`. Verify data persists after restarting the app. `docker compose down` preserves the named database volume; deleting that volume deletes its data. The included password is deliberately local-only and must never be reused in a deployed environment. Migrations run explicitly once, not on every application startup.

## Deployment Boundary
Week 8 adapts the single app image and a managed PostgreSQL service. Inject the database URL through the selected host's secret mechanism. Deploy a read-only synthetic demonstration or implement and test real authentication/authorization before exposing writes. Do not deploy SQLite on ephemeral container storage and call it durable persistence.

## What Is Automated?
The included GitHub workflow installs dependencies, runs tests/lint/static security and dependency checks, builds the UI, and validates evidence-log structure. It does not call an LLM or assign a grade. The mentor prompt in the course repository is a separate, optional assisted-review procedure.
