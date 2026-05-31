# Product Note: Post-Loan ROI Correction Workflow

Last Edited: May 15, 2026 7:22 PM
PRD ETA: May 15, 2026
PRD Owner: Abhijeet Jha
Status: Pending review

## Background and Context

**Who is facing the problem:**

- Product Operations team, who currently execute post-loan ROI changes manually

**What is broken today?**

- ROI updates are done via a Python script run locally by Product Ops
- The operator has to prepare a CSV, refresh the Finflux auth token, run the script, and verify output manually
- There is no single system to create, track, execute, and audit these requests

**Why is it important?**

- Effort is high for a repetitive internal workflow

**Example scenario:**

- ET Money offers ROI of `9.99%` for the first 3 months
- After 3 months, ROI needs to be updated to `10.75%`
- Today, this is done only after business confirmation and script execution by Product Ops

---

## 1. Problem Scope

### In scope

**Task to be productized:**

- Enable Ops to execute post-loan ROI correction through Command Centre instead of a local script
- Support both single-loan ROI correction and batch ROI correction via CSV

**What are we solving?**

1. Manual execution dependency

**Who are we solving it for?**

- Product Operations
- Business team
- LSP

### Out of scope

- Customer-facing communication
- Partner or LSP self-serve workflow

---

## 2. Success Criteria

**Expected outcomes:**

1. Standard ROI correction cases move from script execution to Command Centre
2. Ops can execute approved ROI updates faster and with lower manual effort
3. Every request has a visible execution outcome: success, failure, or partial success

**Good post-launch state:**

- Ops can create single or batch requests in Command Centre
- System validates current ROI before update
- System verifies final ROI after update
- Loan-level outcomes are visible for both single and batch requests

---

## 3. Solution Scope

### Solution overview

We are implementing an internal **Post-Loan ROI Correction Workflow** in Command Centre to replace the current script-based process used by Product Ops.

- single-account ROI correction
- batch CSV upload
- business-approved or otherwise authorized internal ROI correction requests

### Inputs required

- `loan_account_number(FXLAN)`
- `current_interest_rate`
- `updated_interest_rate`

### Core workflow

1. Ops create a request in Command Centre
2. Operator enters request details or uploads CSV
3. System fetches current interest details from Finflux
4. System validates current effective ROI against the request input
5. System computes the required spread change and updates Finflux
6. System re-fetches loan details and verifies the final ROI
7. System marks each record as success or failure with reason

### Expected system outcome

- ROI is updated in Finflux for the target loan(s)
- Final ROI is verified after execution
- For batch mode, each loan gets an independent outcome and the batch gets an aggregate status

---

## 4. Operational / Control Considerations

**Controls to preserve from the current script flow:**

- Validate current ROI before update
- Update spread rate rather than blindly overriding ROI
- Verify final ROI after update
- Store request inputs and execution result

**Approval and audit expectations:**

- Current state requires business approval before execution
- Final maker-checker design remains a PM scoping decision
- Workflow should capture requestor, approval reference, requested values, execution result, and final verified outcome

**Key risks:**

- Wrong loan or wrong ROI value being submitted
- Current ROI in Finflux not matching the expected request input
- Finflux update failure or verification mismatch after update
- Duplicate or blind re-runs on the same loan
- Approval ownership remaining unclear if maker-checker is not finalized

**Fallback handling:**

- Failed records should show a clear failure reason
- Batch requests can complete partially
- Existing script can remain fallback during rollout

---

## 5. High Level System, User or Process Flow

`[REQUEST INITIATION]

↓

Business-approved ROI correction request is received

↓

Operator opens Command Centre

↓

Operator selects single-account or batch mode

↓

Operator enters request details / uploads CSV

↓

System fetches current interest details from Finflux

↓

System validates current ROI

↓

If valid, system computes spread delta and updates Finflux

↓

System re-fetches loan details

↓

System verifies updated ROI

↓

System marks record as Success / Failed

↓

For batch mode, aggregate status shown as Success / Partial Success / Failed`

**Failure scenarios covered:**

- current ROI mismatch
- auth / Finflux API failure
- verification mismatch
- partial batch failure

---

## 6. Appendix

### Current SOP Summary

- Prepare CSV input
- Refresh Finflux auth token
- Run Python script locally
- Review output CSV for final status

### Current Script Logic

- Fetch current interest details
- Validate current effective ROI
- Compute spread delta
- Update spread rate
- Re-fetch and verify final ROI

### Open Questions

- What should the final maker-checker flow be?
- What duplicate / re-run controls should be added?