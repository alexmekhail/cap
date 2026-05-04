# Security Taxonomy for AI Native Engineers

As an AI Native Engineer, you must protect your system against both traditional and AI-specific threats. This taxonomy maps the threats you must verify against AI-generated code.

## 1. Insecure Defaults & Hallucinated Configurations (Covered in Week 7)
*   **Risk:** AI generates infrastructure code (e.g., Dockerfiles, `docker-compose.yml`) that exposes internal ports, runs as root, or omits standard security middleware (like CORS/CSRF protections).
*   **Defense:** Explicitly mandate secure configurations in your prompts (e.g., "Ensure the Docker container runs as a non-root user and only exposes port 8080"). Always verify the generated network boundaries.

## 2. Insecure Direct Object Reference (IDOR) (Covered in Week 10)
*   **Risk:** AI generates APIs that fetch data via simple IDs (e.g., `/user/123`) without checking if the requester owns the data.
*   **Defense:** Manually enforce authorization checks on every endpoint. AI often hallucinates the "happy path" and skips auth checks.

## 3. SQL / NoSQL Injection
*   **Risk:** AI generates raw SQL strings via string formatting instead of using parameterized queries.
*   **Defense:** Enforce the use of an ORM (like SQLAlchemy) and reject any PR where raw queries interpolate user data.

## 4. Misconfigured IAM (Over-Privileged Roles) (Covered in Week 8)
*   **Risk:** AI scripts suggest granting `*:*` or `AdministratorAccess` to quickly unblock a cloud deployment error.
*   **Defense:** Apply the Principle of Least Privilege. Only grant exactly what the service needs (e.g., `roles/cloudsql.client`).

## 5. Hardcoded Secrets (Covered in Week 1 & SAW Linter)
*   **Risk:** Pushing API keys or database credentials to GitHub.
*   **Defense:** The `agentic-linter.yml` uses `gitleaks`. Always use environment variables (`.env`) and `.gitignore`.