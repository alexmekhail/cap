# Week 1: Inspiration — The Art of the Possible

## Purpose
Students see three nontechnical builders demonstrate finished products and explain how their ways of working with AI evolved. The session should create ambition and useful questions: what can I build, how do people actually get there, and what must I learn to produce work I can trust?

This is a showcase and discussion, not a coding lecture. There is no classroom project. Students make their first exploratory attempt at home; the first guided classroom build starts in Week 2.

## What Students Should Leave With
- Three concrete examples of useful software built by people without traditional software-engineering backgrounds.
- An understanding that the finished product came from decisions, iteration, and recovery—not just a single impressive prompt.
- Observations about how builders supplied information, checked results, and changed their methods as projects grew.
- A small idea to try at home, confidence using their own tools, and questions to bring to Week 2.

## Session Shape
Plan for **120 minutes**: a short introduction, three substantial showcases, a shared Q&A, and an instructor-led synthesis. Keep technical explanations brief and tied to what the speakers actually show. The later weeks will name and practice the techniques.

| Segment | Time | Instructor responsibility |
|---|---|---|
| Welcome and framing | 10m | Establish what students should notice and how this connects to the residency |
| Speaker 1 | 25m | Surface the first attempt and the path to a working product |
| Speaker 2 | 25m | Draw attention to a different workflow or problem domain |
| Speaker 3 | 25m | Surface how the method changed as the project became harder |
| Joint Q&A | 25m | Compare methods, investigate failures, and bring in student questions |
| Synthesis and homework briefing | 10m | Turn the examples into an at-home experiment and questions for Week 2 |

The speakers need not fit predetermined categories. Use differences in their actual experiences to make comparisons. Protect the Q&A and closing time; if a demo fails, move to prepared screenshots rather than consuming the session troubleshooting.

## 1. Welcome and Framing (10m)

### Set the ambition
Explain that the residency is about becoming an employable engineer who can use AI to deliver and defend working software. Students already know programming and Git. The next challenge is learning how to direct the work, understand what changed, and judge the result.

Introduce why the guests are nontechnical: their experiences make the possibilities visible and expose methods students can learn from. Do not frame the guests as less capable or imply that an impressive demo establishes production readiness. Invite curiosity about both what they accomplished and how they accomplished it.

### Give students a listening task
Ask them to take notes under four headings:
1. **Built:** What does the product do, and for whom?
2. **Method:** How did the builder work with AI?
3. **Turning point:** What failure or limitation changed that method?
4. **Evidence:** How did they decide the result worked?

### Establish course expectations briefly
All material is on GitHub. Students bring their own GitHub account and paid agent with VS Code and terminal support. Independent work is 5–10 hours each week. Today is inspiration; at-home work establishes comfort with the tools before Week 2's fresh build.

## 2. Three Builder Showcases (25m Each)

Brief each guest on the following structure in advance:
- **Problem and finished work (8m):** Show a complete user journey and explain why they wanted the product.
- **How they built it (7m):** Walk through the tools, requests, files, or other information they used and the steps they handled themselves.
- **How their method evolved (7m):** Compare an early approach with their current one. Show a specific failure, the change they made, and the result.
- **One takeaway and transition (3m):** Name one practice they would repeat and one unresolved limitation.

Presentation slides, screenshots, recorded sessions, and finished-product demonstrations are all appropriate. A live coding change is optional; the point is a credible account of the work, not a risky performance.

### What you do while guests present
Listen for concrete evidence and write a short comparison on screen or a board. If an account is too abstract, ask one brief clarifying question: “Can you show the request or the change that made the difference?” Save longer discussion for the panel.

Capture each speaker's **early method → turning point → current method**. Avoid converting the showcase into an early lecture on context windows, skills, or orchestrators. Students will learn those concepts after they have an experience to connect them to.

## 3. Joint Q&A (25m)

### Compare the workflows (5m)
Start with an observation from the presentations: “You both reached a similar result, but one of you planned extensively and the other built a small version first. What led you to that approach?” Use actual examples rather than a predetermined conclusion.

### Take student questions (15m)
Invite questions about both the product and the process. Use these prompts if the discussion stalls:
- What was your first request to the AI, and how would you write it today?
- When did the work stop being straightforward? What did you change?
- What information did you have to give the AI before it could help?
- How did you recognize a result that looked convincing but was wrong?
- How did you recover when a change broke something that already worked?
- Which part did you keep doing yourself, and why?
- What would be the first additional check before other people depended on this product?

### Close with transferable advice (5m)
Ask each speaker: “What is one thing students should try this week, and one trap they should watch for?” Keep advice specific enough to test at home.

## 4. Instructor Synthesis and Homework Briefing (10m)

### Connect the examples (5m)
Return to the comparison you captured. Identify two or three practices supported by what the guests showed: for example, narrowing a request, supplying an example, testing a complete workflow, or saving a working version before changing it. Distinguish observations from guarantees; different tasks may need different approaches.

Ask students to write down one method they want to try and one question they cannot yet answer. Explain the progression: Week 2 makes the interaction deliberate in VS Code, Week 3 develops sustained terminal-agent work, and Week 4 introduces orchestration.

### Make the next step concrete (5m)
Point students to [homework.md](homework.md). They will verify their setup, create or fork a small repository, try something at home, investigate a confusing result, and write a field report. A working product is welcome but not required in Week 1. The purpose is an honest first experience, not polished output.

Have students check that they know where the assignment is on GitHub and what link they must submit. Capture access blockers for follow-up rather than turning the close into a full installation tutorial.

## Preparation and Follow-through
- Ask each guest to prepare a product walkthrough and screenshots or a recording as fallback. Confirm permission to share their material on GitHub and remove private data or credentials before publishing.
- Review the guests' examples beforehand so introductions and comparison questions refer to their real work.
- After class, add shareable guest materials to this week's GitHub folder and record unanswered questions.
- Before Week 2, review field reports and select a few examples that will make prompting, context, and validation instruction concrete.
