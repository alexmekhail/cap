# Week 8 Instructor Demonstration

## Objective
A deployed synthetic-data demonstration, release evidence, least-privilege identity decisions, and a runbook for verification, recovery, and cleanup.

## Preparation
Select an existing small application or an instructor-prepared example with the required behavior. The examples below specify what to demonstrate; no application is supplied by this curriculum. Record the base commit, runtime/tool versions, exact commands, and any account requirements. Prepare a working baseline, a deliberately failing checkpoint, and a verified recovery. Public reference solutions are acceptable when clearly identified.

## Demonstration Sequence
1. **Establish the claim (5m):** State the user-visible behavior and the acceptance check. Ask students to predict what will happen.
2. **Inspect the baseline (10m):** Show relevant code, configuration, and evidence. Distinguish what is known from what the agent needs to inspect.
3. **Perform the change/exercise (15m):** Use a pre-rehearsed instructor project with synthetic data. Inspect the image/version, runtime identity, secret reference, and managed database connection before deploying. Run a browser success check, forbidden-write check, restart/persistence check, and log lookup. Show the release runbook and cleanup path; use a labeled recording if cloud access is unavailable.
4. **Investigate the failure (10m):** Demonstrate a missing runtime permission in the instructor sandbox. Identify which identity needs which resource grant rather than adding broad administrator access. Keep this separate from app-user authorization.
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
