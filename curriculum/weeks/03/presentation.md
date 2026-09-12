---
marp: true
theme: default
paginate: true
style: |
  section {
    background-color: #f8f9fa;
    font-family: 'Inter', sans-serif;
  }
  h1 {
    color: #2c3e50;
  }
---

# Week 3: Working in the Wild
## AI-Assisted Engineering in an Existing Codebase

---

# Greenfield vs. Brownfield

- **Greenfield (Week 2):** Building from scratch. Fun, fast, but rarely reality.
- **Brownfield (Real World):** You land in a codebase with 100,000+ lines of code.
- You didn't pick the framework, the naming conventions, or the architecture.
- Your job: Add a feature without breaking everything else.

---

# AI-Assisted Codebase Navigation

Use AI to accelerate onboarding; verify its map against actual files and symbols.

- **Architecture:** *"Explain the architecture of this project. What are the main modules?"*
- **Tracing:** *"Trace the flow from the React component down to the database write."*
- **Blast Radius:** *"If I modify this data model, what other files will break?"*

---

# The "Just Rewrite It" Trap ⚠️

- AI hates messy, legacy code.
- Its instinct is to delete a 500-line function and rewrite it "cleanly".
- **Do not let it do this.**
- Working code has survived edge cases. You want *surgical changes*, not global refactors.

---

# The Implementation Loop

1. **Write a PRD:** What are we changing? Why? What is the acceptance criteria?
2. **Implement with Guardrails:** Give the AI the file and the PRD. "Show me ONLY the diff of what needs to change."
3. **Validate:** Run the existing test suite. Compare against the baseline; investigate failures before assigning a cause.

---

# Common Hallucination Traps

- **Global Refactoring:** Randomly changing tabs to spaces or renaming variables.
- **Invented APIs:** Assuming a helper function exists because it "usually" does in similar frameworks.
- **Ignoring Patterns:** Writing Zustand code in a Redux project. Force the AI to respect existing architecture!

---

# This Week's Challenge: Excalidraw

- We are cloning `excalidraw/excalidraw`.
- Use the instructor-tested checkout and record its commit.
- HTML5 Canvas rendering (not React DOM).
- **Core task:** One persistent comment with a pin that follows pan and zoom.
- Follow `comments-brief.md`; no paid account is required.
- Replies, reactions, and resolution are optional extensions.
- Submit evidence for coordinate math, persistence, and preserved drawing behavior.
