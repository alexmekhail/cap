# Agentic Mentor: Standardized Evaluation Rubric

## Purpose
Mentors should use this rubric when evaluating student PRs and Prompt Logs. We do not grade students on syntax; we grade them on their ability to steer the AI.

## Grading Scale (1-5)
1. **Fail:** Blindly accepts AI output; no verification.
2. **Novice:** Attempts verification but fails to isolate issues; relies on AI for architecture.
3. **Pass:** Steers AI reasonably well but misses subtle structural issues.
4. **Proficient:** Catches subtle logic flaws and enforces contracts, but takes too many iterations.
5. **Sovereign:** Acts as an architect; provides perfect context; catches all hallucinations immediately.

## Evaluation Criteria

### 1. Context Management (Score: __ / 5)
*Did the student provide the right data to the AI?*
- **1:** Sent the entire codebase at once; overwhelmed the context window.
- **2:** Sent relevant files, but missed crucial environmental constraints.
- **3:** Provided the right file, but missed giving architectural constraints.
- **4:** Provided good context, but required multiple prompts to clarify boundaries to the AI.
- **5:** Provided surgical context (only the exact interfaces/schemas needed) and clearly stated constraints (e.g., "Do not use external libraries").

### 2. Iterative Correction (Score: __ / 5)
*How effectively did the student fix hallucinations?*
- **1:** "It doesn't work, fix it" (No debugging effort).
- **2:** Copied stack traces blindly without attempting to understand the root cause.
- **3:** Pointed out the error but relied entirely on the AI to find the solution.
- **4:** Identified the root cause but allowed the AI to implement a messy fix.
- **5:** Identified the exact line the AI hallucinated and provided the specific documentation/logic to correct it.

### 3. Structural Oversight (Score: __ / 5)
*Did the student protect the architecture?*
- **1:** Allowed the AI to introduce a new database or framework without an ADR.
- **2:** Allowed the AI to bypass established API contracts for "ease of use".
- **3:** Caught major architectural shifts but allowed minor anti-patterns.
- **4:** Protected the main architecture but allowed leaky abstractions or duplicate types.
- **5:** Strictly enforced the API contracts and rejected "lazy" AI workarounds.

### 4. System Integrity (Score: __ / 5)
*Is the resulting system robust, performant, and secure?*
- **1:** Shipped fragile code; fails edge cases or contains basic security flaws (e.g., SQL injection, hardcoded secrets).
- **2:** Code passes happy-path tests but fails under minor load or edge case inputs.
- **3:** Code is functionally correct but lacks proper logging, error handling, or performance optimization.
- **4:** Code handles edge cases and errors well, but relies heavily on tooling rather than fundamental understanding of the system's limits.
- **5:** Shipped production-ready code with comprehensive error handling, documented performance tradeoffs, and a clear understanding of systemic failure modes.

## Mentor Feedback Template
- **Strongest Prompting Moment:** [Highlight a great steer]
- **Missed Hallucination:** [Highlight a bug they missed]
- **Next Week's Focus:** [e.g., "Focus on providing tighter context windows"]
