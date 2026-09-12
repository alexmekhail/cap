FROM node:24-bookworm-slim AS frontend
WORKDIR /ui
COPY src/frontend/package*.json ./
RUN npm ci
COPY src/frontend/ ./
RUN npm run build

FROM python:3.12-slim
WORKDIR /app
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY src/backend/ src/backend/
COPY src/__init__.py src/__init__.py
COPY migrations/ migrations/
COPY alembic.ini ./
COPY --from=frontend /ui/dist src/frontend/dist
RUN useradd --create-home appuser && chown -R appuser:appuser /app
USER appuser
ENV PORT=8080
EXPOSE 8080
CMD ["sh", "-c", "exec uvicorn src.backend.app:app --host 0.0.0.0 --port ${PORT:-8080}"]
