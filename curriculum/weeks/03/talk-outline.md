# Week 3: "Working in the Wild"
## AI-Assisted Engineering in an Existing Codebase

**Goal:** Students learn that real engineering is almost never greenfield. They use AI to navigate, analyze, and modify a production-quality open-source codebase they've never seen before.

> ⚠️ **The shift:** Weeks 1–2 were "build from scratch." This week is "land in someone else's code and get productive fast." This is what the actual job looks like.

---

## Talk Outline (75m)

### Part 1: Why Existing Codebases Are Different (15m)
- **Greenfield vs. Brownfield** — In the real world, you inherit code. You don't get to pick the architecture, the naming conventions, or the framework version.
- **The Onboarding Problem** — A new engineer's #1 challenge is understanding what already exists. AI is absurdly good at this if you prompt it correctly.
- **The Risk of "Just Rewrite It"** — AI will happily rewrite working code. Your job is to make *surgical changes* that don't break what's already working.

### Part 2: AI-Powered Code Analysis (20m)
- **The Codebase Tour Prompt** — "Explain the architecture of this project. What are the main modules and how do they interact?"
- **Dependency Mapping** — "Trace the flow from [endpoint X] to [database write Y]. What files are involved?"
- **Finding Where to Change** — "I need to add [feature]. Which files would I need to modify and why?"
- **Live Demo:** Instructor drops into the **selected OSS project** cold. Uses AI to understand the architecture, find the right files, and map a feature.

### Part 3: The PRD → Implementation → Validation Loop (25m)
- **Write the PRD First** — Before touching code, use AI to draft a mini Product Requirements Document: What are we changing? Why? What's the acceptance criteria?
- **Implementation with Guardrails:**
  - Constrain AI to only modify specific files
  - Require AI to explain what each change does
  - Diff review: read every line before committing
- **Validation:**
  - Run existing tests — did you break anything?
  - Write NEW tests for your change
  - Manual smoke test
- **Live Demo:** Instructor implements a small feature/fix in the OSS project using this full loop, narrating every decision.

### Part 4: Common Traps (15m)
- AI "improving" code you didn't ask it to touch
- AI changing import styles, formatting, or variable names globally
- AI hallucinating internal APIs that don't exist in the codebase
- AI ignoring the project's existing patterns and inventing new ones

---

## The OSS Project: Excalidraw

Students work in a fork of `https://github.com/excalidraw/excalidraw`. The instructor supplies a tested checkout and setup instructions for the cohort before class. Record the exact commit, runtime/package-manager versions, install command, start command, and baseline test results in the cohort README; rehearse on a clean checkout. Locate rendering and element modules from that checkout rather than assuming paths from an older release.

The instructor demo uses a separate project so students practice transferring the method. The assignment specification is [the local comments brief](comments-brief.md); no paid account or trial is required.

## Lab: Codebase Analysis & Architecture (90m)

### Task 1: Architecture Mapping (45m)
Use AI to locate the drawing renderer, element data model, viewport transforms, and state ownership. Verify each claim against a file and symbol in the checked-out source. Explain the distinction between a shape painted on the canvas and a DOM comment pin overlaid on it. Run the existing relevant tests and record the baseline before editing.

### Task 2: PRD and First Checkpoint (45m)
Write a short PRD from the supplied brief: user need, core acceptance criteria, files likely to change, and validation plan. Demonstrate one pin at a scene coordinate before adding persistence. Review the plan with a peer or mentor.

## Assignment: One Persistent Comment

### Objective
Implement one complete comment workflow in an unfamiliar codebase while preserving its existing drawing behavior. Budget 4–6 hours outside class; submit a documented partial implementation and next step if the timebox expires.

### Core Requirements
1. Create a text comment at a canvas location using an explicit comment action.
2. Display a DOM pin anchored to the scene coordinate; keep it aligned during pan and zoom.
3. Select the pin to read its text in a panel.
4. Persist the comment locally so it survives reload for the same drawing, without leaking into another drawing.
5. Follow the project's architecture, keeping comment state separate from drawing elements, and explain the ownership and persistence decision.
6. Add focused tests for coordinate conversion and persistence, run the relevant existing tests, and manually check drawing interactions.

### Optional Extensions
Multiple threads, replies, reactions, resolution, element anchoring, and export/import support are extensions after the core acceptance criteria pass. They do not substitute for missing core validation and are not required for full marks.

### Deliverable
A PR against your own fork with the implementation, PRD, tests, and `docs/prompt-logs/week-03.md`. Include before/after test evidence, a screenshot or recording of pan/zoom and reload behavior, and one evidence-backed architectural decision. Explain any incomplete criterion and its next step.

### Grading Focus

| Dimension | Weight |
|---|---|
| **Architecture & State** — Justified ownership, persistence, and limited change scope | 25% |
| **Viewport & Persistence Validation** — Tests and manual evidence for the core behavior | 30% |
| **Context & Intervention** — Verified navigation, useful sequencing, and justified corrections | 25% |
| **Core Workflow** — Creation, selection, and readable persisted text | 20% |
