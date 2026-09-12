---
marp: true
theme: default
paginate: true
---

# Quality, Access, and Evidence

Establish checks that expose important failures and define who may perform each operation before the application is made public.

---

# Contract-focused testing

Choose checks from the user contract: valid input, invalid input, missing records, duplicate writes, persistence, and state changes. Separate upstream timeout/rate-limit failures from client validation. Decide the mapping in your contract and assert it.

---

# Access and security

Identify trusted/untrusted inputs and write endpoints. Choose a read-only synthetic public demo or implement tested authentication and object-level authorization. A user ID provided by the caller is not proof of identity. Use two actors to test ownership rules.

---

# Quality gates and interpretation

Run tests, coverage, lint, static security, dependency audits, and log-structure checks. Teach that a green scan means no findings from that tool/configuration, not zero vulnerabilities. Treat assessment as human-reviewed evidence, not a count of prompts.

---

# Demonstrate and Defend

A useful test suite and CI gate, an explicit access model, and evidence that an incorrect implementation is rejected.

---

# Homework

Strengthen the Week 5 project and make the release access decision. Configure the provided checks for your project, add meaningful failure cases, and demonstrate at least one intentionally incorrect implementation failing a relevant test.
5–10 hours. Required criteria and evidence: homework.md.

---

# What Comes Next

Week 7 transports the tested app into containers and verifies its database behavior on PostgreSQL.
