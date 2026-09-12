# Agentic Mentor: Engineering Evidence Rubric

## Use
Week 1 uses its exploratory field-report rubric. Weeks 2–4 use the weights in their dedicated `homework.md`; use the dimensions below to interpret evidence without applying a second grade. Weeks 5–12 use all four dimensions equally unless the assignment publishes different weights. Assess only skills taught by that milestone.

Neither app size, number of prompts, nor autonomous recovery determines quality. A student may earn full credit by configuring effective checks and reviewing the outcome without manually correcting every error. Missing evidence is not proof of failure: request a specific artifact and keep the affected score provisional.

## Shared Scale
1. **Unverified:** Accepts an outcome without relevant checks or supporting evidence.
2. **Developing:** Attempts checks but leaves important gaps unexplained.
3. **Competent:** Verifies the core outcome and explains major decisions and limitations.
4. **Strong:** Tests meaningful failure cases, limits change scope, and justifies intervention.
5. **Excellent:** Demonstrates robust checks, evidence-backed tradeoffs, and a clear account of what remains uncertain.

## Dimensions
### 1. Context Management
Look for verified source references, relevant contracts, useful instructions, and a plan for gathering missing context. Reward accurate navigation and maintained context. Do not use file count as a proxy for quality.

### 2. Validation & Iterative Correction
Look for checks that can expose a real failure, before/after results, and a supported diagnosis. Credit both agent recovery within established checks and human intervention when checks are insufficient. Review test changes for weakened assertions. Do not demand a fabricated hallucination or penalize the number of iterations.

### 3. Structural Oversight
Look for a justified architecture decision, preserved boundaries, explicit data/API contracts, and review of changes outside the plan. Explain acceptable tradeoffs in relation to the taught milestone. For W3, assess the existing project's architecture; for W4, assess the chosen harness project; from W5, assess the production project.

### 4. System Integrity
Look for functioning core behavior, negative cases, data integrity, migration evidence where required, and honest limitations. Seed counts and coverage percentages alone are insufficient. Assess production operations only after their corresponding lessons.

## Mentor Feedback
- **Strongest evidence:** Link to a log, test result, diff, or decision.
- **Gap and implication:** State what remains unverified and why it matters.
- **Next action:** One concrete improvement appropriate to the student's current week.
- **Assessment:** Published weekly weights or four equally weighted dimensions; label provisional scores and missing evidence.
