# BRD: Interest Refund via Credit Note - OD

Last Edited: March 19, 2026 9:44 PM
Status: Completed

---

## 1. Background & Objective

Interest is periodically accrued, posted, and collected from users as part of the loan lifecycle and recognized as **interest income** in the accounting system.

In specific business scenarios, a portion of **already posted and/or collected interest** may need to be reversed and refunded to the user.

Currently, interest refunds are handled manually or via ad-hoc adjustments, which introduces:

- Accounting inconsistencies
- Limited audit traceability
- Operational risk at scale

### Objective

Define a **system-driven, auditable** mechanism to refund interest via **Credit Note**, ensuring:

- Correct P&L reversal of interest income
- Correct user balance adjustment
- Alignment with existing Credit Note & Waiver accounting patterns

---

## 2. Scope

### In Scope

- Refund of interest already posted and/or collected
- Refund processed only via **Credit Note**
- Accounting treatment for:
    - Interest income reversal
    
- Support for partial and full interest refunds

### Out of Scope

- Interest waiver before posting

---

## 3. Key Definitions

| Term | Definition |
| --- | --- |
| Interest Refund | Reversal of interest already posted and/or collected |
| Credit Note (Interest) | LMS transaction representing interest refund |
| Intermittent Liability A/c | Temporary clearing account for refund settlement |
| Interest Income Reversal A/c | Contra-income account to reverse interest revenue |

---

## 4. Accounting Principles

The interest refund follows the **same two-step accounting construct** used for charge refunds:

1. User-level adjustment via **Credit Note**
2. Income reversal via **accounting journal**

This ensures:

- LMS reflects user truth
- Accounting reflects financial truth
- Refund execution remains decoupled from income correction

---

## 5. Accounting Scenarios

### 5.1 Interest Refund – Interest Collected (Credit Note Issued)

### Step 1: LMS Transaction – Credit Note (Interest)

Creates a refund obligation without impacting income directly.

| Account | Debit | Credit | Account Type |
| --- | --- | --- | --- |
| Intermittent Liability A/c | Interest Amount |  | Liability |
| As per apportionment of the credit note (independent of charge/interest waiver |  | Principal/interest/Charge/Excess | Asset / Liability |

**Impact**

- User balance reduced
- No P&L impact at this stage
- Refund liability created

---

### Step 2: Accounting Journal – Interest Income & GST Reversal

| Account | Debit | Credit | Account Type |
| --- | --- | --- | --- |
| Interest Income Reversal A/c | Refund Amount |  | Income |
| Intermittent Liability A/c |  | Refund Amount | Liability |

**Impact**

- Interest income reversed in P&L
- GST liability reversed (where applicable)
- Refund clearing account settled

---

| Scenario | LMS Transaction | Debit GL | Credit GL | Notes |
| --- | --- | --- | --- | --- |
| Interest Refund – Step 1 | Credit Note (Interest) | Intermittent Liability | User Interest / Excess | Creates refund obligation |
| Interest Refund – Step 2 | Accounting JV | Interest Income Reversal | Intermittent Liability | Reverses income  |

---

## 6. Product Configuration Requirements

### LMS

- New **Credit Note Type: Interest refund**
- Ability to configure:
    - Refund amount (partial / full)
    - Interest component selection
    - Reason codes

### Accounting

- New GL accounts:
    - Interest Income Reversal A/c
- Mapping aligned with charge refund GL structure

### Reporting & Audit

- Credit note reference ID
- Linked accounting voucher ID
- Full traceability from:
    - Original interest posting → Credit note → Income reversal

---

## 9. Success Metrics

- 100% traceability between LMS and accounting
- Zero manual income reversals
- No P&L leakage due to interest refunds
- Audit sign-off without exceptions

---

## 10. Risks & Mitigations

| Risk | Mitigation |
| --- | --- |
| Incorrect income reversal | Mandatory linkage to original interest posting |
| Duplicate refunds | Idempotent credit note validations |

---