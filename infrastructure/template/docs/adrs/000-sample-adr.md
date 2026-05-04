# ADR 000: Architecture Choice for Library Management

## Status
Accepted

## Context
We need to build the persistence layer and backend for the Library Management System. The system requires complex transactional integrity (e.g., checking out a book concurrently) and predictable reporting capabilities.

## Decision
We chose the **Stateful Container Pattern** (Cloud Run + Cloud SQL PostgreSQL). 

## Rejected Options
1. **Event-Driven Serverless (Firestore + Cloud Functions):** Rejected because Firestore's NoSQL model makes enforcing strict relational inventory constraints (e.g., ensuring copies available > 0) difficult without complex manual transactional logic, whereas PostgreSQL handles row-level locking natively.
2. **Scheduled Batch (BigQuery):** Rejected because our primary use case is transactional CRUD operations (checkout/return), not analytical data warehousing.

## Consequences
- We will have higher baseline costs due to the running Cloud SQL instance compared to pure serverless NoSQL.
- We benefit from robust relational integrity and can safely use SQLAlchemy to map our models.