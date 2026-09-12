# Week 6 Presenter Notes: Quality, Access, and Evidence

## Opening
“Establish checks that expose important failures and define who may perform each operation before the application is made public.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Contract-focused testing
Choose checks from the user contract: valid input, invalid input, missing records, duplicate writes, persistence, and state changes. Separate upstream timeout/rate-limit failures from client validation. Decide the mapping in your contract and assert it.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Access and security
Identify trusted/untrusted inputs and write endpoints. Choose a read-only synthetic public demo or implement tested authentication and object-level authorization. A user ID provided by the caller is not proof of identity. Use two actors to test ownership rules.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Quality gates and interpretation
Run tests, coverage, lint, static security, dependency audits, and log-structure checks. Teach that a green scan means no findings from that tool/configuration, not zero vulnerabilities. Treat assessment as human-reviewed evidence, not a count of prompts.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
The old curriculum conflated upstream 429 responses with malformed user input. Use a concrete contract: invalid request → 422; duplicate → 409; a bounded unavailable dependency may produce 503 or another explicitly justified server-side response. Do not rewrite upstream failures as client mistakes by default.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 7 transports the tested app into containers and verifies its database behavior on PostgreSQL.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
