# Week 7 Presenter Notes: Containers, PostgreSQL, and Delivery

## Opening
“Reproduce the application outside the development machine and make database changes without losing the evidence or data the system depends on.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Build and runtime boundaries
Inspect a multi-stage Dockerfile in the chosen classroom project: Node builds static React assets; Python serves the API and assets on the same origin. Dependencies used at build time differ from runtime dependencies. Keep secrets out of layers and inspect the runtime user.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Database transition and migrations
Run migrations on PostgreSQL, seed records, and verify constraints and query behavior. SQLite results alone do not establish PostgreSQL behavior. Add a nullable field, upgrade against existing data, and compare IDs and relationships afterward.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Delivery and recovery
Separate image build, migration, and app startup. Define health checks, rollout verification, and what happens if migration or startup fails. Do not have every replica race to run migrations. A rollback may require forward repair rather than a destructive downgrade.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
Change the database hostname to an invalid service name in a disposable environment. Read the failure and fix the configuration. Contrast this with schema mismatch: identical symptoms at the UI may require different repairs.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 8 deploys the tested image with managed persistence and an explicit release/access decision.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
