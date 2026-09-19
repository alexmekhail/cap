---
name: review-decision
description: Review a code change and classify it as accept, comment, or reject.
---

# 2. Classify the change

Input: the request, diff, relevant code, and available check results.

Check correctness and concrete maintainability problems using SOLID where applicable.
Flag significant performance opportunities supported by measurements or a clear
cost at realistic scale. Suggest design patterns only when the benefit is obvious
and outweighs added complexity; do not require patterns or SOLID compliance for its own sake.

Inspect the change and return one recommendation:
- **ACCEPT:** no actionable concerns; required checks are satisfied.
- **COMMENT:** useful feedback, but nothing that blocks acceptance.
- **REJECT:** a supported blocking defect or missing required evidence.

Give a short reason and file references for concerns. Accept is valid;
do not invent issues. Ask for essential missing context; do not guess.
Review only; do not edit, submit a review, or claim unrun checks passed.
