# Week 4: Persistence & Data Modeling

## Talk Outline: The Data Foundation
### Technical Deep Dive (75m)
- **Database Fundamentals:** Why AI fails at schema design (Missing foreign keys, poor normalization, missing indexes).
- **Choosing the Persistence Layer:** When to use PostgreSQL vs. Firestore/NoSQL.
- **ORMs and Migrations:** Safely prompting AI to write SQLAlchemy models and Alembic migrations without destroying data.

## Lab Instructions: The Database Schema
### Objective
Design a robust database schema using an ORM and generate safe database migrations.

### Steps
1. **Schema Design:** Prompt the AI to define your core database tables using SQLAlchemy. *Constraint: You must enforce strict relational integrity (Foreign Keys, cascading deletes) and define at least one composite index.*
2. **Migrations:** Prompt the AI to initialize Alembic and generate the initial migration script.
3. **The Indexing Defense:** Intentionally ask the AI to write a complex query. Analyze the AI's generated SQL to ensure it hits your defined index instead of causing a full table scan.
4. **The Log:** Document your iterations in `docs/prompt-logs/week-04.md`. Specifically, note how you forced the AI to correct a missing database constraint.

### Deliverable
A committed SQLAlchemy schema, the generated Alembic migration file, and a Mentor review focusing on your "Structural Oversight" score.
