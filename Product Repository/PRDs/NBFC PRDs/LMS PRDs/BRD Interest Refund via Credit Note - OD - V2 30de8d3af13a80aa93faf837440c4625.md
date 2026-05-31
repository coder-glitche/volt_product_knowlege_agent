# BRD: Interest Refund via Credit Note - OD - V2

Last Edited: March 19, 2026 9:44 PM
PRD Owner: Vaibhav Arora
Status: Completed

## 1. Background & Objective

Interest is periodically accrued, posted, and collected from users as part of the OD loan lifecycle and recognized as interest income in the accounting system.

In certain business scenarios (pricing corrections, excess collection, grievance redressal, operational errors, etc.), a portion of already posted and/or collected interest may need to be refunded to the user.

The objective of this document is to define a **system-driven, auditable mechanism** to process interest refunds via Credit Note with correct accounting treatment.

The solution must ensure:

- Accurate reversal of interest income in P&L
- Correct user-level balance adjustment
- Elimination of manual accounting interventions
- Full audit traceability

---

## 2. Scope

### In Scope

- Refund of interest already posted and/or collected
- Refund processed only via Credit Note (Interest type)
- Support for partial and full interest refunds
- Integrated accounting and LMS impact
- Duplicate refund control with necessary dedupe validations

### Out of Scope

- Interest waiver before posting

---

## 3. Key Definitions

| Term | Definition |
| --- | --- |
| Interest Refund | Reversal of interest already posted and/or collected |
| Credit Note (Interest) | LMS transaction representing interest refund |
| Interest Income Reversal A/c | Contra-income GL used to reverse recognised interest revenue |

---

## 4. Accounting Principles

Interest refunds will follow a **single-step integrated accounting construct**.

At the time of Credit Note processing:

- User balance adjustment and income reversal will occur simultaneously
- No intermediate liability or clearing account will be created
- P&L impact will be immediate

This ensures:

- LMS reflects user truth
- Accounting reflects financial truth
- Reduced reconciliation complexity
- No deferred clearing entries

---

## 5. Accounting Treatment

### 5.1 Interest Refund – Credit Note Issued

At the time of processing Credit Note (Interest Refund):

| Account | Debit | Credit | Account Type |
| --- | --- | --- | --- |
| Interest Income Reversal A/c | Refund Amount |  | Contra Income |
| User Interest / Excess / Principal (as applicable) |  | Refund Amount | Asset / Liability |

---

### Impact

- User outstanding reduces (or excess ledger adjusted)
- Interest income reversed immediately in P&L
- No clearing or intermittent liability account involved

---

## 6. Scenario Representation

| Scenario | LMS Transaction | Debit GL | Credit GL | Notes |
| --- | --- | --- | --- | --- |
| Interest Refund | Credit Note (Interest) | Interest Income Reversal | User Interest / Excess | Single-step income reversal and user adjustment |

---

## 7. Product Configuration Requirements

### LMS

- New Credit Note Type: Interest Refund
- Ability to configure:
    - Refund amount (partial / full)
    - Interest component selection
    - Reason codes
- Mandatory linkage to original interest posting reference

### Accounting

- GL Mapping:
    - Interest Income Reversal A/c (Debit)
    - User ledger (Credit)
- No intermittent liability GL required

---

## 8. Reporting & Audit

The system must maintain full traceability from:

Original Interest Posting → Credit Note → Income Reversal Entry

Required references:

- Credit Note ID
- Linked GL voucher ID
- Original interest transaction reference

Audit objectives:

- 100% traceability
- Zero manual income reversals
- No P&L leakage
- Clean audit trail without reconciliation breaks

---

## 9. Risks & Mitigations

| Risk | Mitigation |
| --- | --- |
| Incorrect income reversal | Mandatory linkage to original interest posting |
| Duplicate refunds | Idempotent credit note validations |
| P&L mismatch | Single-step accounting construct |