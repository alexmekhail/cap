---
marp: true
theme: default
paginate: true
size: 16:9
style: |
  section {
    background: #f7f2e8;
    color: #13233f;
    font-family: "Avenir Next", Avenir, Helvetica, Arial, sans-serif;
    font-size: 29px;
    padding: 56px 72px;
  }
  section::after {
    color: #667085;
    font-size: 16px;
  }
  h1 {
    color: #13233f;
    font-size: 50px;
    letter-spacing: -1.5px;
    margin: 0 0 24px;
  }
  h2 {
    color: #176b87;
    font-size: 30px;
    margin: 0 0 18px;
  }
  strong { color: #176b87; }
  code {
    background: #e7eef0;
    color: #13233f;
  }
  ul, ol { line-height: 1.42; }
  li { margin: 10px 0; }
  section.lead {
    background: #13233f;
    color: #f7f2e8;
    justify-content: center;
  }
  section.lead h1 {
    color: #ffffff;
    font-size: 64px;
    max-width: 850px;
  }
  section.lead p {
    color: #bde7ef;
    font-size: 34px;
  }
  section.stage img {
    height: 485px;
    object-fit: contain;
    position: absolute;
    right: 46px;
    top: 145px;
    width: 510px;
  }
  section.stage ul,
  section.stage p {
    max-width: 570px;
  }
  section.sequence img {
    display: block;
    margin: 24px auto 0;
    max-height: 430px;
    max-width: 1120px;
  }
  blockquote {
    border-left: 8px solid #f3b61f;
    color: #13233f;
    font-size: 34px;
    margin: 28px 0;
    padding: 8px 0 8px 28px;
  }
---

<!-- _class: lead -->

# Working Effectively with AI Agents

Prompts, context, skills, and a live build

<!--
Week 2 moves from exploration to deliberate work. Students will define a small outcome, give the agent useful context, inspect changes, and validate the result.
-->

---

# What we’ll cover

1. Prompts, system instructions, and context.
2. Managing context with files and subagents.
3. Reusable skills and better code reviews.
4. Staying in the loop: inspect, test, and correct.
5. Live build: Reinforcements! board game.

<!--
Introduce the lesson in the order it appears in the deck: understand the inputs, manage context, compare review skills, supervise the results, and apply these practices during the Reinforcements! live build.
-->

---

# Prompt, system prompt, and context

## Prompt

The current request: desired outcome, constraints, and acceptance criteria.

## System prompt

Standing instructions supplied by the application that guide the model’s behavior, such as “You are a soccer coach.”

## Context

The material available while handling that request: the prompt, system instructions, conversation, source files, examples, and tool results.

> A clear prompt can still fail when the required context is absent.

<!--
Ask students to identify which sentence is the request and which information the agent would need before editing code.
Project instructions such as AGENTS.md contain standing guidance written by you or your team and loaded into context by the tool. They are not automatically system instructions. Verify which instruction files your chosen tool actually reads; names and discovery rules vary.
-->

---

# Prompt engineering

- **Goal:** say what you want to happen.
- **Context and constraints:** point to relevant information and set boundaries.
- **Success:** describe how to check the result.

**Example: a task board**

“Add an incomplete-tasks filter to this task board. Inspect the existing task list and reuse its controls. Keep saved tasks intact. Check that completed tasks disappear when the filter is on and return when it is off.”

<!--
Prompt engineering means making the request clear enough to act on and evaluate. Contrast the example with “make the task board better.” Have students identify the goal, relevant context, constraints, and observable success criteria. A good prompt can be short; it does not need magic phrases or an elaborate persona. Refine the request when the result reveals a missing requirement.
-->

---

# Same context, different authority

- The application labels messages with roles, such as **system** and **user**.
- System instructions take priority over conflicting user requests and project guidance.
- Typing “SYSTEM” inside a user message does not change its role.

**System:** “Thou shalt not hack the neighbour’s computer.”

**AGENTS.md:** “I’m a hacker working on hacking my neighbour’s computer.”

**Expected behavior:** follow the system instruction and refuse.

> Instruction priority is not a security guarantee.

<!--
Everything is context, but not everything has equal authority. AGENTS.md is project guidance loaded by the application, not its own message role. The statement about being a hacker supplies intent; it does not grant permission or override the system restriction.
Teaching transition: “The system prompt is supposed to win. ‘Supposed to’ matters.”
In July 2026, OpenAI models operating with reduced safeguards during internal cybersecurity evaluations bypassed isolation controls and compromised parts of OpenAI's research infrastructure and Hugging Face's systems. Use this as an example of why instructions and technical containment are different. Do not describe it as overriding a specific system prompt without evidence of that instruction and its violation.
Source: https://openai.com/index/hugging-face-incident-and-the-road-ahead/
-->

---

# The context window

- Think of the context window as a **limited working area**.
- Each marble represents a chunk of available information.
- Prompts, code, instructions, test output, and prior messages all add marbles.
- The model produces its next response from the material currently available.

<!--
The bucket is a teaching metaphor. Tokenization means pieces are not equal in size, and the model does not literally store or search marbles.
-->

---

<!-- _class: stage -->

# 1. Fresh context

![Fresh context represented by five distinct marbles in a mostly empty bucket](assets/context-empty.png)

- Only a few relevant details are present.
- Each item stands out.
- Early instructions are easy to keep in view.

**Example:** the task, one source file, and its acceptance criteria.

<!--
Point to the yellow marble. It represents one important requirement, such as “reject blank tasks.” With little competing material, it is easy to notice and apply.
-->

---

<!-- _class: stage -->

# 2. Context accumulates

![Growing context represented by a bucket half full of marbles](assets/context-growing.png)

- Questions add conversation history.
- The agent reads files and project instructions.
- Tool calls add logs, diffs, and test output.

The important requirement remains available, with more material competing for attention.

<!--
Advance from the previous slide without changing the layout. Describe a realistic sequence: ask for a plan, inspect files, implement a change, run a test, then ask a follow-up.
-->

---

<!-- _class: stage -->

# 3. Context rot

![Crowded context represented by a bucket packed with overlapping marbles](assets/context-full.png)

- Relevant details can become harder to use consistently.
- Earlier instructions may receive less attention.
- Long logs and unrelated files add noise.
- Old assumptions can conflict with newer facts.

**The yellow requirement still exists, but it is easier to miss.**

<!--
Context rot is an informal description of degraded performance as a working context becomes long, noisy, stale, or internally inconsistent. A large context window does not guarantee that every detail receives equal attention.
-->

---

<!-- _class: stage -->

# 4. Compaction

![Compacted context represented by six retained marbles and a discarded pile](assets/context-compacted.png)

- The system or agent summarizes prior work.
- Selected goals, decisions, and current state remain.
- Raw dialogue and fine detail may be dropped.
- Work continues with the smaller representation.

**Compaction creates room, with information loss.**

<!--
The retained yellow marble shows an important requirement surviving compaction. The discarded pile reminds students that a summary cannot preserve every detail. After compaction, verify critical constraints and current state instead of assuming they survived intact.
-->

---

<!-- _class: sequence -->

# The full sequence

![Four stages of an LLM context window: fresh, growing, crowded, and compacted](assets/context-buckets.png)

**Fresh context** &nbsp;&nbsp;&nbsp; **Growing context** &nbsp;&nbsp;&nbsp; **Context rot** &nbsp;&nbsp;&nbsp; **Compaction**

<!--
Invite a student to narrate the sequence in their own words. Ask what they would deliberately preserve before compaction.
-->

---

# Subagents help manage context

A **subagent** handles a focused task in its own context window.

- Delegate large file reads; return relevant findings and references.
- New file reads and intermediate output stay in the subagent's context.
- It may start with selected background or inherit the parent's conversation.
- System and project instructions depend on the tool and agent setup.

**This can reduce clutter; it does not eliminate context limits or errors.**

<!--
Use the bucket metaphor: a helper has a separate bucket for the investigation and sends a small set of useful findings back. Delegate the read before loading the large file into the parent. Delegation does not remove material already in the parent's context. The report still adds context, and the helper still uses tokens; total usage can increase. Ask for source references so the parent can verify important claims without importing the entire investigation.
Source: https://learn.chatgpt.com/docs/agent-configuration/subagents
Example: the parent asks a subagent to read a large log and find why saving fails. The subagent returns findings, line references, and uncertainties; the parent checks the evidence. Separate context does not always mean an empty starting context.
Claude Code distinguishes non-fork subagents, which start with a delegation message and their configured instructions, from conversation forks, which inherit the parent's conversation. Do not teach that every Claude subagent starts empty. Project-instruction loading also depends on the agent type.
The Codex subagent interface available for this lesson's preparation supports no conversation history, a chosen number of recent turns, or all available history; its default is all. This is an interface-specific behavior, not a universal guarantee for every Codex version or surface. Selective recent-turn history is different from the parent writing a selective summary in the task prompt.
An inherited context is a snapshot at creation, not a continuously synchronized conversation. Subsequent investigation stays with the child unless communicated back. Shared access to files is also different from already having their contents in context.
Source: https://code.claude.com/docs/en/sub-agents#what-loads-at-startup
Source: https://code.claude.com/docs/en/sub-agents#how-forks-differ-from-other-subagents
-->

---

# Context engineering

Give the model the information it needs for the current task.

- Load relevant files, examples, and constraints.
- Keep information current; leave out unrelated material.
- Save decisions and progress for the next session.

> A good prompt makes the task clear. Good context makes it answerable.

<!--
Connect each practice to the bucket sequence. The goal is useful context, not the largest possible context.
-->

---

# What is a skill?

A reusable set of instructions for a specific kind of task.

- **When to use it:** the task or situation it applies to.
- **How to do it:** steps, tools, and checks.
- **What to return:** the expected result.

**Example: three ways to frame a code review**

1. **Find problems:** look for what is wrong.
2. **Classify:** accept, comment, or reject; passing is valid.
3. **Challenge findings:** try to refute concerns before classifying.

> A prompt defines the task. A skill provides a reusable procedure.

<!--
Compare three standalone versions on the same change: skills/diff-review/SKILL.md, skills/review-decision/SKILL.md, and skills/review-with-refuter/SKILL.md. Use separate fresh conversations with the same inputs so later versions are not primed by earlier findings. Version 1 deliberately lacks an explicit pass outcome for teaching; it can encourage needless criticism, but does not always find a problem. Version 2 allows accept, comment, or reject. Version 3 adds a refuter pass within the review; it does not require another agent. These approaches do not guarantee increasing quality. Compare the evidence, not just the number of findings. These are recommendations, not automatic PR submissions.
If demonstrating a fix-and-review loop, continue only for supported blocking findings; accept ends the loop and comment leaves optional feedback. Missing required evidence calls for validation, not a speculative code change. Set an iteration limit and stop for human inspection if findings keep cycling.
The skill asks: did we build what was requested, did we break or change anything else, and what evidence supports the conclusion? Show the deliberately flawed filter example in reference.md: it deletes completed tasks instead of hiding them. Label it as a prepared example, not a spontaneous model error.
Review identifies concerns by inspecting the diff and relevant surrounding code. Validation separately runs checks and exercises behavior. Validation procedure: compare against the request; run relevant checks against the known baseline; exercise one success and one failure case; inspect whether tests assert intended behavior; report evidence, limits, and next steps. Neither procedure guarantees correctness.
Students use a reusable skill twice during homework and record what changed or remained useful.
-->

---

# Human in the loop

> Request → inspect diff → run checks → diagnose → correct

- Make one understandable change at a time.
- Verify the agent's claims with code and behavior.
- Explain one changed function in your own words.

<!--
Week 3 moves toward on-the-loop supervision with planned checkpoints. Today, keep decisions between small steps.
-->

---

# Use AI to accelerate work. Own the judgment.

| Delegate to AI | Don’t outsource |
|---|---|
| ✅ Drafting and repetitive work | ❌ Goals and priorities |
| ✅ Exploring options | ❌ Evaluating trade-offs |
| ✅ Finding potential mistakes | ❌ Critical thinking and verification |
| ✅ Gathering information | ❌ Decisions and responsibility |

**Do I understand it? What supports it? Does it meet the goal?**

---

# Demo

Reinforcements! board game

<!--
Build Reinforcements! during the live demonstration. Define its rules and acceptance criteria with the class, then apply the prompt, context, review, and validation practices from this deck. The task-board filter elsewhere is a separate teaching example. See homework.md for the full homework submission requirements and rubric.
-->
