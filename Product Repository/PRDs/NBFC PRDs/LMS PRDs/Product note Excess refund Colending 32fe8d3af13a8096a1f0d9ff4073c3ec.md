# Product note: Excess refund Colending

Last Edited: April 7, 2026 3:38 PM
PRD ETA: March 26, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## **Background and Context**

- **Who is facing the problem**
    - NBFC Ops & Finance teams
    - Customers (end borrowers)
    - LMS / Payments systems
- **What is the challenge**
    - In the current system:
        - Excess funds in a loan are:
            - **Auto-adjusted against dues**
            - **Available for withdrawal**
    - However, in **co-lending loans**:
        - Excess:
            - **Cannot be used for withdrawal**
            - **Cannot auto-adjust against dues (parked excess)**
    - This creates:
        - Customer dissatisfaction (funds blocked)
        - Operational dependency on batch refunds
        - Regulatory and reconciliation sensitivity (escrow flows)
- **Why is it important**
    - Excess funds belong to the borrower → must be returned timely
    - Blocked excess reduces trust and impacts CX
    - Co-lending construct mandates **controlled fund flows**
    - Need a **unified system** that works for both:
        - DSP 100% loans
        - Co-lending loans

---

## **1. Problem scope**

### In scope

- Enable **excess refund flow compatible with both loan types**:
    - DSP loans (auto-adjust + withdrawal allowed)
    - Co-lending loans (parked excess, no withdrawal)
- Introduce:
    - **Maker-checker flow for excess refunds**
    - **Validation layer to compute refundable excess**
- Enable:
    - Manual refund by Ops
    - Automated daily refund via CRON
- Stakeholders:
    - Primary: Ops, Finance
    - Secondary: Customers

---

### Out of scope

- Enabling:
    - Real-time auto-adjustment of excess for co-lending (future scope)

---

## **2. Success Criteria**

### Key outcomes

- **Timely refund of excess** for co-lending loans
- **Zero incorrect refunds** (over/under refund)
- Reduced dependency on manual ops intervention

### Metrics

- % excess refunded within T+1 (target: >95%)
- Excess refund error rate (target: <1%)
- Manual intervention rate (should reduce over time)

### Post-launch good state

- Excess:
    - Not withdrawable (co-lending)
    - Automatically refunded via system or ops
- Ops:
    - Can trigger instant refunds via maker-checker

### Guardrails

- No:
    - Over-refunding beyond eligible excess
    - Refunds during foreclosure / invalid states
    - Impact on repayment posting / accounting

---

## **3. Solution Scope**

### Solution overview

We will introduce a **unified excess refund framework** with:

- **Validation engine** → determines refundable excess
- **Maker-checker flow** → enables controlled manual refunds
- **Daily CRON** → ensures timely automated refunds

System behavior will differ based on loan type:

- DSP loans → existing behavior continues
- Co-lending loans → excess is parked and refunded

---

### Detailed solution scope:

### Core Concepts

- **Excess (parked)**:
    - Not available for withdrawal (co-lending)
    - Not auto-adjusted against dues
- **Refundable Excess**:

```
Refundable Excess = Excess - Accrued Interest (Retention)
```

---

### Validation Logic (Eligibility for Refund)

Refund allowed only if:

- No **non-terminal foreclosure request** exists
- Account is **not in shortfall**
- No **existing excess refund (non-terminal)**
- Excess amount > 1 and > Accrued interest

---

### Use Cases

| Description | Details |
| --- | --- |
| DSP loan excess | Continues existing behavior (auto-adjust + withdrawal) |
| Co-lending excess | Parked, not withdrawable |
| Manual refund (Ops) | Maker-checker based refund trigger |
| Automated refund | Daily CRON at 6 PM |
| Refund blocked | Foreclosure / shortfall / pending refund |
| Partial excess scenario | Refund only eligible amount after retention |

---

### Maker-Checker Flow (New)

- **Maker (Ops)**:
    - Initiates excess refund request
    - System computes eligible amount
- **Checker**:
    - Validates and approves
- Post approval:
    - Excess is settled in LMS
    - Payout triggered via Cashfree

---

### Daily CRON

- Runs at **6 PM daily**
- Identifies:
    - Eligible excess accounts
- Executes:
    - Settlement of excess in LMS
    - Payout to registered bank account

---

### Operational Changes

- **Ops**
    - Gains ability to:
        - Trigger instant refunds
        - Track refund status
- **Customer**
    - No withdrawal option (co-lending)
    - Receives refund automatically

---

## **5. High level system / process flow**

### Automated Flow

1. System identifies excess
2. Validation engine checks eligibility
3. If valid:
    - Excess settled in LMS
    - Payout initiated via Cashfree
4. Status updated

---

### Manual Flow (Ops)

1. Ops identifies excess case
2. Maker creates refund request
3. Checker approves
4. System:
    - Settles excess
    - Initiates payout

---

### Edge Cases

- Foreclosure initiated → refund blocked
- Shortfall account → no refund
- Duplicate refund request → blocked
- Accrued interest > excess → no refund

---

## **6. Appendix (Optional)**

### Key Differences (DSP vs Co-lending)

| Behavior | DSP Loan | Co-lending Loan |
| --- | --- | --- |
| Excess usage | Auto-adjust + withdraw | Parked |
| Withdrawal | Allowed | Not allowed |
| Refund dependency | Optional | Mandatory |
| Ops intervention | Low | Medium |

---

### Future Enhancements

- Real-time excess auto-refund
- Excess auto-adjustment for co-lending
- Smart retention logic (beyond accrued interest)
- Customer visibility of refund timeline