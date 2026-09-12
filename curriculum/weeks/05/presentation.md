---
marp: true
theme: default
paginate: true
---

# Production Entry: One Working Slice

Turn the AI workflow skills from Weeks 1–4 into a small application whose interfaces, data, and behavior you can explain.

---

# Scope and architecture

Choose one user, one operation, and one source of data. Draw the boundaries and identify one failure at each boundary. Compare a stateful application with batch/event alternatives; record why the simplest suitable pattern wins.

---

# Data and API contract

Explain keys, foreign keys, uniqueness, and input validation using the starter. Inspect the initial migration and generated OpenAPI. A schema diagram and contract should match the actual implementation.

---

# Integration and feedback

Trace a browser request through FastAPI to SQLAlchemy and back. Demonstrate loading, empty, success, and error states. Keep frontend work bounded by adapting the supplied reference.

---

# Demonstrate and Defend

A reproducible UI → API → database slice, a short ADR, an API contract, and an initial migration. This repository continues through Week 12.

---

# Homework

Build one complete domain-specific operation on the production starter or your compatible Week 4 app. Avoid a clone-sized feature list: for a library, add a book to a collection; for a marketplace, register a listing; for a content service, save metadata.
5–10 hours. Required criteria and evidence: homework.md.

---

# What Comes Next

Week 6 strengthens this slice and defines the access model before deployment. The follow-up data-preserving migration moves to Week 7 so Week 5 remains achievable.
