# Product note: LMS integration with Tally

: Vaibhav Arora
Created time: December 10, 2025 11:42 AM
Status: Ready for Tech
Last edited: January 8, 2026 9:27 AM

## **Background and Context**

- 
    - Who is facing the problem (users, internal teams, partners)
    - What is the challenge that they are facing? What is broken today?
    - Why is it important? or What is getting impacted?

Most businesses record transactions across multiple ledgers to accurately classify income, expenses, assets, and liabilities arising from each business event such as product sales, and discounts.

For us as an NBFC, core business transactions include interest posting, charge application, payouts against sanctioned limits, and customer repayments.

Given the regulated nature of lending, NBFC accounting processes are subject to direct regulatory scrutiny by the RBI. It is therefore critical that accounting is accurate, automated, system-driven, and free from manual intervention.

Currently, accounting entries are generated in the LMS and then manually transformed and posted into the ERP. This manual handoff introduces operational and control risks.

This gap was highlighted as a key vulnerability in our statutory audit and must be addressed as a priority.

---

## **1. Problem scope**

### In scope

- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- **Manual ERP Posting Dependency**:
    
    Accounting entries are generated in Finflux (LMS) but are **manually transformed and uploaded into Tally**, creating operational dependency on the Finance team.
    
- **High Risk of Errors and Duplicates**:
    
    Manual handling increases the risk of:
    
    - Duplicate ledger postings
    - Incorrect ledger mapping
    - Debit / credit sign errors
    - Partial or missed uploads

**Lack of Idempotency & Control**:

There is currently:

- No system enforced idempotency for ERP postings
- No way to prevent re-posting of the same transaction
- Limited ability to trace an LMS transaction to a Tally voucher

**Delayed and Unpredictable TAT**:

Posting timelines depend on:

- Manual availability of the Finance team
- Ad-hoc batch preparation and uploads
    
    This leads to **inconsistent turnaround times**
    

**Access control**:

Current workflows do not consistently enforce:

- System-driven approvals
- Clear separation between generation, validation, and posting of accounting entries.

### Out of scope

- 
    - Call out on items out of scope
    - Rationale for exclusion
- Manual Reconciliation: Reconciliation between LMS (Finflux) and ERP (Tally) is currently manual and time-intensive, requiring cross-system data pulls and comparisons.

This will be picked as an enhancement once the current release is stabilised. ETA to be confirmed
- Delayed Detection of Breaks: Posting mismatches are detected late and the Root-cause analysis becomes reactive rather than proactive

---

## **2. Success Criteria**

- 
    
    Top 2-3 **clear outcomes that we are looking to achieve**.
    
    - Key success metrics (Conversion rate / Error rate / TAT)
    - Define post launch good state (Expected behaviour / uptime / SR)
    - Guardrail metrics (Metrics that should not degrade)
- **≥99% of LMS accounting transactions** are successfully posted to Tally via system integration with **no manual Finance intervention**.
- Manual uploads are limited to approved exception cases only.
- Zero to minimal duplicate and erroneous ledger posting to Tally

---

## **3. Solution Scope**

- Consumption of ledger entries from LMS: Consume final, transformed accounting entries from Finflux (LMS), grouped by transaction type and accounting event.
- Sanity validations: Entries will be validated before uploading to ensure ledger names, debit/credit types, and amounts are consistent with the chart of accounts.
- Idempotency of ledger posting:
    - Ledger entries will be processed on a **T+2 basis** (consuming T-2 dated transactions) to allow for reversals, corrections and finalisation of journals.
    - Each batch (Daily) and transaction will be assigned a **unique  ID**, which will be passed to Tally as the **external transaction reference** to ensure idempotency and prevent duplicate postings.
    - Re-posting will be blocked all corrections and back fills will be processed by the Finance team after analysing the consumed batch and response from the ERP.
- **Tally Cloud Setup & API-Based Integration**:
    - A **dedicated cloud-hosted Tally instance** will be provisioned for ERP accounting.
    - A secure **POST API** will be exposed from Tally to accept accounting vouchers.
    - Fenix will act as the **orchestration layer**, consuming entries from Finflux and posting them to Tally via API eliminating the need for manual intervention.
    - API responses (success, partial success, failure) will be captured and stored for downstream reconciliation and audit.
- Audit: All inbound LMS payloads, outbound ERP requests, and ERP responses will be stored with timestamps and reference IDs.
- Access control:
    - New role for the Finance team will be created for the Command Centre
    - The daily accounting batch job will generate an **approval task** in the Operations section of the Command Centre.
    - The Finance team will be able to:
        - **Approve** the batch for posting to Tally, or
        - **Regenerate** the batch (similar to the existing mandate batch workflow) in case of discrepancies.

### Solution overview

- 
    
    Explain in 2-3 lines the overview of the solution
    
    - Explain overview of the solution with key product and system changes
    - Explain the rationale on scoping/phasing of the solution
    - Call out scope that has been scoped out and explain the rationale

**Overview of the Solution (Key Product & System Changes)**

- Automated consumption of final accounting entries from Finflux and posting to Tally via API and cloud instance set up of Tally.
- Introduction of T+2 batch processing, idempotent transaction IDs, and Finance-led approval workflows in the Command Centre.
- End-to-end audit trail covering LMS payloads, ERP requests, and ERP responses.
- Alerting of failed journal postings to Tally

**Out of scope**

- Automated retries are scoped out to avoid systemic accounting errors and to preserve maker–checker discipline.
- System-driven reconciliation is deferred until posting stability and error patterns are well understood.

### Detailed solution scope:

- 
    
    Bullet list of user and system use cases that are supported:
    
    - Define all use cases applicable and what are in scope
    - Core happy path
    - Key edge cases that must be handled at launch
    - Consider all the stakeholders that are impacted
    - Has to answer questions like:
        - How does this change existing operational SOPs?
        - How does this change the experience for the end user?
        - How does this impact sales or onboarding conversations?

| Description | Details |
| --- | --- |
| **Daily Accounting Batch Generation** | System-generated daily batch of final, transformed accounting entries from Finflux (LMS). |
|  | Entries grouped by transaction type and accounting event |
| **Finance Approval Workflow** | Batch surfaced in the Command Centre for Finance review. |
|  | Finance can approve or regenerate the batch prior to ERP posting. |
| **Automated ERP Posting** | Approved batches are posted to Tally via secure APIs through Fenix. |
|  | Each accounting transaction is posted with a unique external reference ID to ensure idempotency. |
| **Audit & Traceability** | End-to-end storage of LMS payloads, ERP requests, and ERP responses. |
|  | One-to-one traceability between LMS transaction, batch ID, and Tally voucher. |

---

## **5.  High level s***ystem, user or process flow*

- 
    - Cover the overview of the process or the journey
    - Include error cases or edge cases (Optional)
1. Fenix consumes final accounting entries for T-2 from Finflux.
2. System validates entries and creates a daily batch.
3. Finance reviews and approves the batch in the Command Centre.
4. Batch is posted automatically to Tally via API.
5. ERP response is captured and stored for audit.

### Key Edge Cases Handled at Launch

- Partial ERP posting failures within a batch (captured and surfaced).
- Duplicate posting prevention via idempotency checks.
- Batch regeneration in case of validation or mapping issues.
- Clear failure states with no retries.

### Impact on Operational SOPs

- Manual ledger uploads to Tally are **eliminated**. Please note that Finance team will continue to reconcile entries, the batch generation and upload will be done systemically.
- Finance SOPs shift from **data preparation, approval and exception handling**.

### Impact on End User Experience

- No direct customer-facing changes.
- No change to sales or onboarding flows.

---

## **6.  Appendix (Optional)**

### Benchmarking:

### User feedback / Calling: