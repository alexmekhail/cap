# Week 6: Quality, Access, and Evidence

## Teaching Purpose
Establish checks that expose important failures and define who may perform each operation before the application is made public.

## Entry Check
Bring the Week 5 slice, contract, migrations, and a working local check command. If setup is incomplete, pair on an instructor-selected example to learn the checks while recording the gap in your own project.

## Exit Evidence
A useful test suite and CI gate, an explicit access model, and evidence that an incorrect implementation is rejected.

## Session Plan (180 minutes)
Core instruction (75m), an instructor demonstration (45m), and student practice/review (60m). Inspect student entry evidence before expanding scope. The required assignment is in [homework.md](homework.md); avoid maintaining a second specification in slides.

## Core Instruction
### 1. Contract-focused testing (25m)
Choose checks from the user contract: valid input, invalid input, missing records, duplicate writes, persistence, and state changes. Separate upstream timeout/rate-limit failures from client validation. Decide the mapping in your contract and assert it.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 2. Access and security (25m)
Identify trusted/untrusted inputs and write endpoints. Choose a read-only synthetic public demo or implement tested authentication and object-level authorization. A user ID provided by the caller is not proof of identity. Use two actors to test ownership rules.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

### 3. Quality gates and interpretation (25m)
Run tests, coverage, lint, static security, dependency audits, and log-structure checks. Teach that a green scan means no findings from that tool/configuration, not zero vulnerabilities. Treat assessment as human-reviewed evidence, not a count of prompts.

**Check for understanding:** Ask a student to apply this idea to their own project and identify the evidence that would support the decision.

## Instructor Demonstration (45m)
Run the chosen classroom project’s tests, then deliberately remove the unknown-category guard or bypass an acceptance assertion in a disposable copy and observe the consequences. Show a real rejection of duplicate writes. Compare an ownership test for two users with a test that merely checks login exists. Review an example CI workflow and explain its permissions and project-specific setup.

Use [instructor-demo.md](instructor-demo.md) for preparation, checkpoints, and fallback. Ask students to predict the outcome before running the check, then reconcile their prediction with the evidence.

## Student Practice and Review (60m)
Write the access matrix (15m), implement a failure test or ownership check (30m), then have a peer try to invalidate the claimed result (15m).

## Misconception to Address
The old curriculum conflated upstream 429 responses with malformed user input. Use a concrete contract: invalid request → 422; duplicate → 409; a bounded unavailable dependency may produce 503 or another explicitly justified server-side response. Do not rewrite upstream failures as client mistakes by default.

## Close the Session
Have students name one decision, the evidence supporting it, and the next missing check. Confirm they can find the homework and know what to submit. Do not equate partially demonstrated behavior with a completed milestone.

## Connection to the Next Stage
Week 7 transports the tested app into containers and verifies its database behavior on PostgreSQL.

## Materials
[Presenter notes](lecture-script.md) · [Slides](presentation.md) · [Student reference](reference.md) · [Homework](homework.md)
