# Week 2: "The Engine Room"
## How LLMs Actually Work & Coding With Them Properly

**Goal:** Students understand what's happening under the hood when they prompt an LLM, learn the techniques that separate "using AI" from "engineering with AI," and build something properly this time — applying what they learned from their Week 1 struggles.

> 💡 **Why this lands now:** Students already tried AI cold in Week 1. They hit hallucinations, got bad code, didn't know what to include in prompts. This session puts names to those problems and gives them the tools to fix them.

---

## Talk Outline (75m)

### Part 1: Under the Hood (25m)
- **What is an LLM?** — Not a database, not a search engine. A next-token prediction machine trained on internet-scale text.
- **Tokens, not words** — Tokenization demo. Compare how a tokenizer splits prose, identifiers, and numbers. Ask for a character count, verify it with code, and discuss the observed result without assuming the model will fail.
- **The Context Window** — What 128K tokens actually means. Why "bigger window" ≠ "dump everything in." The attention mechanism in plain English: the model weighs relevance, and long-range signal gets diluted.
- **Temperature & Sampling** — Why the same prompt gives different answers. Compare repeated outputs where sampling controls are available; validate results rather than assuming a setting guarantees correctness.
- **Why LLMs Hallucinate** — They're completing patterns, not looking things up. No internal "fact checker." They're confident and wrong in the same voice as confident and right.
- **🔗 Connect to W1:** "Remember when [common W1 struggle]? That happened because [technical reason]."

### Part 2: Prompting for Code (25m)
- **The Prompt is a Program** — System prompt, user prompt, assistant response. The prompt IS the API. Garbage in, garbage out.
- **Context Management** — What to include: file contents, error messages, constraints. What NOT to include: entire repos, irrelevant files, secrets.
- **The Validation Loop** — Never trust first output. Read it. Run it. Test it. The 3-step cadence: *Generate → Validate → Iterate*.
- **Prompt Patterns That Work:**
  - Role assignment ("You are a senior Python engineer…")
  - Constraint injection ("Do NOT use any external libraries")
  - Step-by-step decomposition ("First outline the approach, then implement")
  - Showing examples (few-shot)
- **Prompt Privacy** — Never paste API keys, service account JSONs, billing IDs, internal URLs. Redaction is non-negotiable.
- **🔗 Connect to W1:** Review 2–3 anonymized student field reports. "Here's what went wrong, here's the technique that would have fixed it."

### Part 3: Setting Up Your Workspace Properly (25m)
- **Pick Your Weapon** — Live demo of at least 2:
  - **Chat-based:** ChatGPT, Gemini, Claude (web UI)
  - **CLI-based:** Gemini CLI (`gemini`), Claude Code (`claude`)
  - **IDE-integrated:** Copilot, Cursor, Windsurf
- **The Context File** — Creating `GEMINI.md` / `CLAUDE.md` / `AI_CONTEXT.md` in your repo root. What goes in it: project description, tech stack, conventions, constraints.
- **The Prompt Log** — Why we document every AI interaction. Not busywork — it's your debugging trail and your proof of learning. Intro to `docs/prompt-logs/`.
- **Live Demo:** Instructor takes a broken W1-style project and rebuilds it properly using the techniques from this session, narrating decisions, catching hallucinations, showing the validation loop.

---

## Assignment: "Build Me Something — Properly"

### Objective
Build a **simple but complete** working application from scratch — this time using the techniques you learned. Compare the experience to your Week 1 attempt.

### Constraints
- Must be functional (runs, does something useful or fun)
- Must use Python or JavaScript
- Must include a README explaining what it does and how to run it
- Must set up a proper context file (`GEMINI.md` / `CLAUDE.md`)
- Must include `docs/prompt-logs/week-02.md` documenting your AI interactions
- Must use a **different AI tool** than you used in Week 1

### Suggested Scope (pick one or propose your own)
- A CLI quiz game
- A personal expense tracker (terminal-based)
- A markdown-to-HTML converter
- A Pomodoro timer with terminal UI
- A URL shortener (local, no deployment needed)

### The Comparison
At the end of your prompt log, write a brief section: **"Week 1 vs. Week 2"**
- How was this experience different from Week 1?
- What techniques made the biggest difference?
- What are you still struggling with?

### Deliverable
A GitHub repo (or PR to your SAW repo) with working code, a README, a context file, and a prompt log with the comparison section.

### Grading Focus

| Dimension | Weight |
|---|---|
| **Does it work?** | 30% |
| **Context File Quality** — Is it well-crafted and useful? | 20% |
| **Prompt Log Quality** — Shows validation loop, iteration, technique application | 25% |
| **W1 vs. W2 Comparison** — Honest, specific reflection | 25% |
