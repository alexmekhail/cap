# Week 5: Production Entry: One Working Slice

## Teaching Purpose
Turn the AI workflow skills from Weeks 1–4 into a small application whose interfaces, data, and behavior you can explain.

## Entry Check
Start anew or continue Week 4 work. Use the supplied inventory starter as an executable reference, then choose one approved domain and one narrow user journey. A new stack is not an extra-credit exercise.

## Exit Evidence
A reproducible UI → API → database slice, a short ADR, an API contract, and an initial migration. This repository continues through Week 12.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). Inspect student entry evidence before expanding scope. The required assignment is in [homework.md](homework.md); avoid maintaining a second specification in slides.

## Core Instruction
### 1. Scope and architecture (25m)
Choose one user, one operation, and one source of data. Draw the boundaries and identify one failure at each boundary. Compare a stateful application with batch/event alternatives; record why the simplest suitable pattern wins.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 2. Data and API contract (25m)
Explain keys, foreign keys, uniqueness, and input validation using the starter. Inspect the initial migration and generated OpenAPI. A schema diagram and contract should match the actual implementation.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 3. Integration and feedback (25m)
Trace a browser request through FastAPI to SQLAlchemy and back. Demonstrate loading, empty, success, and error states. Keep frontend work bounded by adapting the supplied reference.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

## Instructor Demonstration (45m)
Use the inventory starter: create a Books category through the seed command, add an item from the UI, reload, then submit a duplicate and an unknown category. Trace the 409 and 422 responses through the client and backend. Open the migration and explain the foreign key. Have the agent propose a domain adaptation, inspect the proposed boundary changes, and implement one small part.

Use [instructor-demo.md](instructor-demo.md) for preparation, checkpoints, and fallback. Ask students to predict the outcome before running the check, then reconcile their prediction with the evidence.

## Student Practice and Review (60m)
Pairs map the reference request path (15m), adapt one domain operation (30m), and review the ADR and contract against the running result (15m).

## Misconception to Address
Use a duplicate item or nonexistent category. The instructor should explain why those are different failures rather than mapping every error to a generic response.

## Close the Session
Have students name one decision, the evidence supporting it, and the next missing check. Confirm they can find the homework and know what to submit. Do not equate partially demonstrated behavior with a completed milestone.

## Connection to the Next Stage
Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.

## Materials
[Presenter notes](lecture-script.md) · [Slides](presentation.md) · [Student reference](reference.md) · [Homework](homework.md)
