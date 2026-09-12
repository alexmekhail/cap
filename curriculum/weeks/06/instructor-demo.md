# Week 6 Instructor Demonstration

## Objective
A useful test suite and CI gate, an explicit access model, and evidence that an incorrect implementation is rejected.

## Preparation
Select an existing small application or an instructor-prepared example with the required behavior. The examples below specify what to demonstrate; no application is supplied by this curriculum. Record the base commit, runtime/tool versions, exact commands, and any account requirements. Prepare a working baseline, a deliberately failing checkpoint, and a verified recovery. Public reference solutions are acceptable when clearly identified.

## Demonstration Sequence
1. **Establish the claim (5m):** State the user-visible behavior and the acceptance check. Ask students to predict what will happen.
2. **Inspect the baseline (10m):** Show relevant code, configuration, and evidence. Distinguish what is known from what the agent needs to inspect.
3. **Perform the change/exercise (15m):** Run the chosen classroom project’s tests, then deliberately remove the unknown-category guard or bypass an acceptance assertion in a disposable copy and observe the consequences. Show a real rejection of duplicate writes. Compare an ownership test for two users with a test that merely checks login exists. Review an example CI workflow and explain its permissions and project-specific setup.
4. **Investigate the failure (10m):** The old curriculum conflated upstream 429 responses with malformed user input. Use a concrete contract: invalid request → 422; duplicate → 409; a bounded unavailable dependency may produce 503 or another explicitly justified server-side response. Do not rewrite upstream failures as client mistakes by default.
5. **Defend the result (5m):** Independently rerun the decisive check. Show the diff/artifacts, remaining limitations, and where the evidence lives.

## Fallback and Honesty
Use a clearly labeled prepared recording or replay if the live environment fails. Explain the missing dependency and do not describe prerecorded execution as a live agent result. Students still need their own assignment evidence.

## Before Calling the Demo Ready
- Rehearse from the documented baseline.
- Verify both the expected failure and the successful outcome.
- Remove private data and credentials from shared artifacts.
- Check that commands work in the stated environment and time budget.
- Confirm that the linked homework assesses what the demonstration teaches.

## Debrief
Ask what made the result believable, which alternative was rejected, and what remains outside the evidence. Return to [talk-outline.md](talk-outline.md) for practice and transitions.
