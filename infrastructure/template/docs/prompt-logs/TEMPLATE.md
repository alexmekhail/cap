# Prompt Log Template

**Instructions:** You MUST use this template for every prompt log you submit. Raw dumps of 40-page chat transcripts will be automatically failed by the Agentic Mentor. Mentors grade on how you *steer*, not just the final result.

---

## 1. The Goal
*(What were you trying to build or fix? E.g., "Implementing the FastAPI POST endpoint for data ingestion.")*

## 2. Initial Context Provided
*(What specific files, schemas, or constraints did you provide in your first prompt? E.g., "I provided `schema.py` and strictly told it to use Pydantic V2.")*

## 3. The AI Hallucination / Error
*(What did the AI get wrong on its first try? E.g., "It hallucinated an external `fetch_data` method that doesn't exist in our API contract.")*

## 4. The Correction Strategy
*(How did you steer it back? Quote your specific corrective prompt. E.g., "I told it: 'That method does not exist. Use the httpx library with the tenacity retry block we defined earlier.'")*

## 5. Final Outcome
*(Did the final code pass your tests? Link to the PR or commit.)*
