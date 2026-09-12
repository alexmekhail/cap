# Week 10: Evidence-Based Workflow Audit

## Goal
Students evaluate how their own engineering workflow changed from the Week 1 first attempt to the deployed capstone. Guest inspiration belongs to Week 1; this session uses students' own evidence to improve their practice.

## Workflow Reveal (45m)
The instructor compares an early prompt log with a later agent session: what context was verified, which checks caught failures, where intervention mattered, and what escaped detection. Show one case where manual investigation was the appropriate choice.

## Core Instruction (75m)
- **Evidence review (25m):** Review logs and PRs from Weeks 1–9. Distinguish model mistakes, incomplete requirements, environment problems, and weak acceptance tests.
- **Controlled improvement (25m):** Choose one recurring issue and change one part of the workflow. Compare before/after on the same bounded task, recording elapsed time, review effort, checks, and remaining defects. Treat a single trial as evidence for that task, not a universal tool ranking.
- **Personal operating procedure (25m):** Write actionable rules for context gathering, acceptance checks, budgets, escalation, and review. Explain when to supervise an agent and when to investigate directly.

## Lab: Audit the Capstone Workflow
1. Select three specific decisions or failures from Weeks 1–9 and link to their logs or diffs.
2. Explain the cause and the evidence; do not assume every failure was a bad prompt.
3. Test one workflow improvement and record its result, including an inconclusive or negative result.
4. Write `docs/ai-workflow-sop.md`, with rules grounded in those examples.
5. Record the experiment in `docs/prompt-logs/week-10.md` and use the SOP during Week 11 interview practice.

## Deliverable
A personal AI Workflow SOP, three linked case studies, and one measured improvement experiment. Grade the reasoning and validation evidence, not the number of tools used or the apparent speed of generation.
