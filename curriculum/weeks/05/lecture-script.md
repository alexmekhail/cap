# Week 5 Presenter Notes: Production Entry: One Working Slice

## Opening
“Turn the AI workflow skills from Weeks 1–4 into a small application whose interfaces, data, and behavior you can explain.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Scope and architecture
Choose one user, one operation, and one source of data. Draw the boundaries and identify one failure at each boundary. Compare a stateful application with batch/event alternatives; record why the simplest suitable pattern wins.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Data and API contract
Explain keys, foreign keys, uniqueness, and input validation using a small example from the instructor’s chosen project. Inspect the initial migration and generated OpenAPI. A schema diagram and contract should match the actual implementation.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Integration and feedback
Trace a browser request through FastAPI to SQLAlchemy and back. Demonstrate loading, empty, success, and error states. Keep frontend work bounded by adapting the supplied reference.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
Use a duplicate item or nonexistent category. The instructor should explain why those are different failures rather than mapping every error to a generic response.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
