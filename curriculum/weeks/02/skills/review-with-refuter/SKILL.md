---
name: review-with-refuter
description: Review a code change, challenge potential findings, then classify the result.
---

# 3. Classify with a refuter

Input: the request, diff, relevant code, and available check results.

1. Check correctness, concrete SOLID-related maintainability problems, and
   significant performance opportunities with evidence at realistic scale.
   Suggest design patterns only for an obvious benefit that outweighs complexity.
   Give potential findings triggers and file references.
2. Try to refute each: does surrounding code handle it? Can it occur?
   Is the performance impact significant? Would the pattern actually simplify it?
   Is the SOLID concern a concrete problem or merely a preference?
3. Drop disproved findings; label unresolved concerns as uncertain.
4. Return **ACCEPT** (no actionable concerns; required checks satisfied),
   **COMMENT** (non-blocking feedback), or **REJECT** (supported blocker
   or missing required evidence). Explain retained and dropped findings.

Accept is valid. Ask for essential missing context rather than guessing.
Review only; do not edit, submit a review, or claim unrun checks passed.
