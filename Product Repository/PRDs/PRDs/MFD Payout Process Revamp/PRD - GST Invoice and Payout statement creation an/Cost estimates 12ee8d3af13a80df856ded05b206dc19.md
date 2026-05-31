# Cost estimates

# AWS Infrastructure Cost Projections (2024-2026)

## Constants & Assumptions

| Parameter | Value | Notes |
| --- | --- | --- |
| Growth Rate | 2x yearly | Partner base doubles each year |
| Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) |
| Retention Period | 84 months | 7 years for regulatory compliance |
| Emails per Partner | 3/month | Registration, payout, GST notifications |
| API Calls per Partner | 20/month | Includes all interactions |
| Lambda Executions per Partner | 10/month | All automated processes |

## Growth & Cost Projections

| Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) |
| --- | --- | --- | --- |
| Active Partners | 2,500 | 5,000 | 10,000 |
| Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB |
| Cumulative Storage | 93 GB | 279 GB | 558 GB |
| Monthly Emails | 7,500 | 15,000 | 30,000 |
| Monthly API Calls | 50,000 | 100,000 | 200,000 |

## Monthly Cost Breakdown (USD)

| Service | Year 1 | Year 2 | Year 3 | Scaling Factor |
| --- | --- | --- | --- | --- |
| S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation |
| RDS | $45 | $65 | $110 | Step Function* |
| Lambda | $3 | $6 | $12 | Linear |
| SES (Email) | $0.75 | $1.50 | $3 | Linear |
| API Gateway | $5 | $10 | $20 | Linear |
| CloudWatch | $15 | $25 | $45 | Step Function* |
| Route 53 | $0.50 | $0.50 | $0.50 | Fixed |
| Step Functions | $2 | $4 | $8 | Linear |
| **Total Monthly** | **$73.39** | **$118.42** | **$211.33** |  |
| **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** |  |