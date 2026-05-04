# Week 2: AI-Driven Ideation

## Talk Outline: From Concept to Contract
### Technical Deep Dive (75m)
- **The Sounding Board Prompt:** How to ask AI to critique your ideas, not just write code.
- **Defining Boundaries:** Drafting clear API contracts and data schemas.
- **The Production-Grade Cloud Application:** Finalizing your specific application domain (e.g., Airbnb clone) and business goals.

## Lab Instructions: Generating the Blueprint
### Objective
Use AI to generate the foundational design documents for your pipeline.

### Steps
1. **Ideation:** Prompt the AI with 3 different data sources. Ask it to evaluate the complexity of ingesting each one.
2. **Schema Design:** Once a source is chosen, steer the AI to generate a JSON schema for the transformed data.
3. **API Contract:** Have the AI draft an OpenAPI/Swagger spec for the endpoint the frontend will eventually consume.
4. **The Log:** Document how many iterations it took to get a schema that actually made sense in `docs/prompt-logs/week-02.md`.

### Deliverable
A finalized API contract and data schema, reviewed by your mentor for Structural Oversight.
