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
  .good { color: #27ae60; }
  .bad { color: #c0392b; }
---

# Week 2: The Engine Room
## The Pillars of AI Engineering & How LLMs Work

---

# From Inspiration to Execution

- Last week, you saw what's *possible* with AI-native engineering.
- But watching someone build is different from doing it yourself.
- **The Trap:** Most beginners treat AI like a magical human programmer. They ask it to code, it fails, and they get stuck.
- **The Reality:** It is an engine, not a human. If you understand how it works, you can steer it.

---

# The 4 Pillars of AI Engineering

To transition from "chatting with an AI" to "engineering with AI," you must master four pillars:

1. **Context Engineering:** What you feed the AI.
2. **Prompt Engineering:** How you ask the AI.
3. **Validation & Iteration:** How you verify the output.
4. **Tooling & The Workspace:** The environment you build in.

---

# Pillar 1: Context Engineering

- **The golden rule:** Garbage in, garbage out.
- **Surgical Context:** Do not paste your entire codebase into the chat. The more irrelevant information you provide, the worse the output.
- **What to include:** The specific file, the exact error trace, and your architectural constraints.

---

# Context Engineering: Examples

**<span class="bad">❌ BAD (The Dump)</span>**
> "My app won't start. Here is my entire `src/` folder." *(AI gets confused, hallucinates problems that don't exist).*

**<span class="good">✅ GOOD (The Surgeon)</span>**
> "I'm getting a `TypeError: undefined` on the `/users` endpoint. Here is `router.ts` and the exact stack trace. We use Express.js."

---

# Pillar 2: Prompt Engineering

- You aren't chatting. You are programming the AI.
- **Role Assignment:** Does telling it "You are a senior engineer" actually matter?
  - For a generic AI, maybe. For a dedicated coding agent, no.
  - **The Nuance:** Role matters for *perspective*. Telling it "You are a harsh Security Auditor" or "You are a UX Designer" changes the *lens* it uses to review your code.
- **Chain of Thought:** "First outline the steps, then write the code."

---

# Prompt Engineering: Examples

**<span class="bad">❌ BAD (Vague & Open-ended)</span>**
> "Make a login form."

**<span class="good">✅ GOOD (Structured & Constrained)</span>**
> "You are an accessibility-focused UX engineer. Write a React login form.
> Constraint: Use Tailwind and only standard HTML elements.
> Step 1: Outline the ARIA requirements.
> Step 2: Write the component."

---

# Pillar 3: Validation & Iteration 🔄

Never trust the first output. Never just copy, paste, and move on.

1. **Generate:** Prompt the AI.
2. **Validate:** Read it. Does it compile? Did it hallucinate a library?
3. **Iterate Surgically:** Give precise feedback to fix the error without rewriting the whole file.

---

# Validation & Iteration: Examples

**<span class="bad">❌ BAD (The Panic)</span>**
> *(AI outputs broken code)*
> "It didn't work. Fix it." *(AI panics, rewrites the entire file, introduces 3 new bugs).*

**<span class="good">✅ GOOD (The Surgical Correction)</span>**
> *(AI outputs broken code)*
> "The code failed at line 42 with `IndexError`. The rest of the logic is correct. Keep everything else exactly the same, but fix the loop iteration."

---

# Pillar 4: Tooling & The Workspace

- Move out of the web browser. You need tools tied to your filesystem (Cursor, Windsurf, Claude Code, Gemini CLI).
- **The Context File:** Create `GEMINI.md` or `CLAUDE.md` at your repo root. This dictates the global rules for the AI.
- **The Prompt Log:** Your debugging trail.

---

# Tooling & Workspace: Examples

**<span class="bad">❌ BAD (The Tourist)</span>**
> Copying code from VS Code, pasting it into ChatGPT in a browser, copying the answer back, and losing track of file paths.

**<span class="good">✅ GOOD (The Professional)</span>**
> Using an IDE Agent with a `GEMINI.md` file in the repo. The agent already knows the project uses Tailwind and Python 3.11 before you even type your first prompt.

---

# Mechanics: Under the Hood

To truly master the 4 pillars, you need to understand the machine.

- **Not a Database:** It does not "look up" answers.
- **A Prediction Engine:** Given a sequence of words, what is the most statistically likely next piece of a word?
- **Experiment:** Repeat a bounded prompt, compare outputs, and independently check correctness.

---

# The Tokenization Problem

- Inspect how a tokenizer splits prose, code, and numbers.
- Ask for a character count and verify it with code.
- Discuss the observed result; do not assume a predetermined failure.
- **Takeaway:** Use an independent check for exact claims.

---

# Context Windows & Hallucinations

- **The Attention Mechanism:** As the context window fills up, the AI's "attention" dilutes. It forgets instructions at the top.
- **Hallucinations:** LLMs are designed to complete patterns. They have no internal "fact checker".
- If you ask for a missing endpoint, it will confidently invent one that *looks* correct.
- **You are the fact-checker.**

---

# Instructor Demo

Let's put the 4 Pillars into practice.
Building a Terminal Pomodoro Timer... *properly*.
