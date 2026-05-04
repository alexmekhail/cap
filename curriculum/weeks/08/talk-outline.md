# Week 8: Livesite & Deployment

## Talk Outline: Crossing the Finish Line
### Technical Deep Dive (75m)
- **Cloud Deployment:** Navigating GCP/AWS services using AI assistance.
- **IAM and Permissions:** The most common place AI hallucinations cause security breaches.
- **Cloud Cost Management:** Setting up billing alerts and budgets *before* you get a $10,000 surprise from runaway AI-generated infrastructure.
- **The Production Mindset:** What it means to have a "Livesite."

## Lab Instructions: The Public URL
### Objective
Deploy the Production-Grade Cloud Application to a production cloud environment.

### Steps
1. **Deployment Scripts:** Deploy the frontend to Vercel/Netlify. For the backend, prompt the AI to generate a Terraform script (`main.tf`) or explicit CLI commands (`gcloud run deploy`) to provision a Google Cloud Run or AWS App Runner service.
2. **IAM Review:** Ask the AI to generate a strict AWS IAM Policy or GCP Service Account JSON that grants *only* the minimum permissions needed to pull the Docker image and write to CloudWatch/Cloud Logging, explicitly avoiding `*:*` wildcards.
3. **The Launch:** Execute the deployment. Ensure the frontend can talk to the backend in the cloud.
4. **The Log:** Document your deployment strategy in `docs/prompt-logs/week-08.md`.

### Deliverable
A publicly accessible URL demonstrating the functional Production-Grade Cloud Application. This achieves the "functional skills" milestone of the program.
