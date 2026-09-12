# Instructor Demo: Week 3 Codebase Navigation

Use Lobe Chat as a separate instructor example so students must transfer the method to Excalidraw. Before class, record a tested checkout, setup commands, and baseline test results. Rehearse a small, bounded change in that checkout; do not depend on an unverified file path or a spontaneous large feature build.

## 1. Map Before Editing
Ask the agent to locate session schema and state ownership, citing files and symbols. Open the sources and verify the claims. Discuss one incorrect or incomplete inference if it occurs; do not script a guaranteed hallucination.

## 2. Write a Bounded PRD
Choose one small metadata or validation change confirmed feasible during rehearsal. Define observable acceptance criteria, affected layers, and a test that would fail without the change. Keep the baseline and acceptance check ready as a fallback if setup fails live.

## 3. Implement and Validate
Work through the relevant layers in dependency order. Inspect each diff, run the documented checks, and compare against the baseline. Investigate failures rather than assuming their cause. Explain why you intervene or allow the agent to continue.

## 4. Transfer to the Assignment
Students use the same mapping, PRD, and validation process for the local comments brief. Their first checkpoint is one scene-anchored pin; persistence follows. Emphasize that a small, verified change is sufficient evidence of engineering skill.
