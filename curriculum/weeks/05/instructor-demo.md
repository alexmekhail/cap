# Week 5 Instructor Demonstration

## Objective
A reproducible UI → API → database slice, a short ADR, an API contract, and an initial migration. This repository continues through Week 12.

## Preparation
Use the [production reference](../../../infrastructure/template/README.md) where applicable, or a disclosed cohort reference with the same behavior. Record the base commit, runtime/tool versions, exact commands, and any account requirements. Prepare a working baseline, a deliberately failing checkpoint, and a verified recovery. Public reference solutions are acceptable when clearly identified.

## Demonstration Sequence
1. **Establish the claim (5m):** State the user-visible behavior and the acceptance check. Ask students to predict what will happen.
2. **Inspect the baseline (10m):** Show relevant code, configuration, and evidence. Distinguish what is known from what the agent needs to inspect.
3. **Perform the change/exercise (15m):** Use the inventory starter: create a Books category through the seed command, add an item from the UI, reload, then submit a duplicate and an unknown category. Trace the 409 and 422 responses through the client and backend. Open the migration and explain the foreign key. Have the agent propose a domain adaptation, inspect the proposed boundary changes, and implement one small part.
4. **Investigate the failure (10m):** Use a duplicate item or nonexistent category. The instructor should explain why those are different failures rather than mapping every error to a generic response.
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
