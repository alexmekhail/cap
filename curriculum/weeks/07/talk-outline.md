# Week 7: Containers, PostgreSQL, and Delivery

## Teaching Purpose
Reproduce the application outside the development machine and make database changes without losing the evidence or data the system depends on.

## Entry Check
Bring the Week 6 application, passing local checks, initial migration, and access policy. Install Docker before class; a setup blocker must be recorded rather than hidden behind a successful local run.

## Exit Evidence
A containerized app connected to PostgreSQL, with explicit migration steps, data-preservation evidence, and CI image build checks.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). Inspect student entry evidence before expanding scope. The required assignment is in [homework.md](homework.md); avoid maintaining a second specification in slides.

## Core Instruction
### 1. Build and runtime boundaries (25m)
Inspect the multi-stage reference Dockerfile: Node builds static React assets; Python serves the API and assets on the same origin. Dependencies used at build time differ from runtime dependencies. Keep secrets out of layers and inspect the runtime user.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 2. Database transition and migrations (25m)
Run migrations on PostgreSQL, seed records, and verify constraints and query behavior. SQLite results alone do not establish PostgreSQL behavior. Add a nullable field, upgrade against existing data, and compare IDs and relationships afterward.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 3. Delivery and recovery (25m)
Separate image build, migration, and app startup. Define health checks, rollout verification, and what happens if migration or startup fails. Do not have every replica race to run migrations. A rollback may require forward repair rather than a destructive downgrade.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

## Instructor Demonstration (45m)
Walk through the supplied Compose file, build the image, start PostgreSQL, run the initial migration and seed as one-off commands, then start the app. Create an item and restart only the app to demonstrate persistence. Apply an additive description-column migration in a disposable database and compare saved records before and after.

Use [instructor-demo.md](instructor-demo.md) for preparation, checkpoints, and fallback. Ask students to predict the outcome before running the check, then reconcile their prediction with the evidence.

## Student Practice and Review (60m)
Trace configuration and networking (15m), run the supplied Compose sequence or inspect a labeled recording if Docker is unavailable (30m), then review migration/recovery plans (15m).

## Misconception to Address
Change the database hostname to an invalid service name in a disposable environment. Read the failure and fix the configuration. Contrast this with schema mismatch: identical symptoms at the UI may require different repairs.

## Close the Session
Have students name one decision, the evidence supporting it, and the next missing check. Confirm they can find the homework and know what to submit. Do not equate partially demonstrated behavior with a completed milestone.

## Connection to the Next Stage
Week 8 deploys the tested image with managed persistence and an explicit release/access decision.

## Materials
[Presenter notes](lecture-script.md) · [Slides](presentation.md) · [Student reference](reference.md) · [Homework](homework.md)
