# Week 8 Presenter Notes: Deployment and Operating Boundaries

## Opening
“Deploy a bounded demonstration that can be verified, observed, recovered, and shut down without confusing a public URL with production readiness.” Ask students to name the evidence they bring from the previous week. If that evidence is missing, identify the recovery task before introducing more scope.

## Explain the Three Decisions
### Choose one deployment path
Default to a single app container on Cloud Run with managed PostgreSQL; an equivalent provider is allowed when the student maps the same responsibilities. A same-origin UI avoids an unnecessary second-host integration problem. Review durable storage and connection limits.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Identity and configuration
Separate the deployer, runtime service identity, and application users. Attach an appropriate runtime identity and grant the needed resource access. Use the provider secret mechanism for database configuration; a service-account key JSON is not an IAM policy.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

### Release and operational checks
Review the access mode before public exposure. Establish a budget alert, low scaling limits appropriate to the demo, startup/liveness behavior, release smoke checks, and rollback/forward-repair steps. Budget alerts notify; they do not cap spending. Record cleanup steps and retain needed evidence.

Ask: “What would convince you this decision is correct for your project?” Follow with: “What would make you change your mind?” Use the student's actual domain rather than an abstract ideal architecture.

## During the Demonstration
Pause before the decisive check. Ask for a prediction, run it, and compare the result. Narrate why you let the agent continue or why you intervene; avoid narrating every keystroke. Label prepared defects and recordings honestly.

## Address the Misconception
Demonstrate a missing runtime permission in the instructor sandbox. Identify which identity needs which resource grant rather than adding broad administrator access. Keep this separate from app-user authorization.

## Practice Debrief
Ask each pair for one supported claim, one unresolved risk, and one next action. Make the feedback specific to the submitted evidence and the current milestone. Do not demand later-week skills prematurely.

## Closing
“Week 9 rehearses incident response in a disposable environment using the same release and observability habits.” Open `homework.md` and point out the core criteria, 5–10 hour budget, and submission artifacts. Record setup blockers and evidence gaps for focused follow-up.
