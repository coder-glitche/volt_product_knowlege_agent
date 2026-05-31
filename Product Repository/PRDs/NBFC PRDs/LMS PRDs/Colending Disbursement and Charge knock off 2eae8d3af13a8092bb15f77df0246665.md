# Colending: Disbursement and Charge knock off

Last Edited: March 19, 2026 9:44 PM
PRD ETA: January 16, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## **Background and Context**

- **Who is facing the problem**
    - **Internal teams**: Engineering, Finance, Ops, Risk, Product
    - **Partners**: DSP (originator / servicer), TCL (co-lender)
    - **Indirectly**: End customers (via statements, repayments, redraw behaviour)
- **What is the challenge today**
    - Processing fees and other charges are **knocked off at disbursement**, but:
        - These charges are collected via disbursements by doing a short disbursement
        - Economically **owned by a specific partner (DSP)**
    - Current POS and split logic assumes:
        - A **single POS**
        - A **static co-lending ratio (10 / 90)**
    - This leads to:
        - Incorrect partner settlements
        - Over / under-recovery for lenders
        - Increasing complexity as multiple disbursements and future charges are introduced
- **Why this is important**
    - Incorrect allocation impacts:
        - **Partner trust and reconciliation**
        - **Revenue recognition**
        - **Audit and regulatory confidence**
    - As the product evolves (OD-like behaviour, multiple charges), ad-hoc fixes will **compound risk and tech debt**
    - This needs a **foundational, extensible solution**

---

## **1. Problem Scope**

### In scope

- Designing a **system-level mechanism** to:
    - Handle **charge knock-off as part of the disbursement workflow**
    - Support **capitalised charges** that are:
        - Part of borrower POS
        - Owned by a specific lender
    - Correctly split:
        - Disbursements
        - Repayments
        - Outstanding balances
- Applicable for:
    - **Initial disbursement**
    - **Future disbursements** in OD / revolving facilities
    - **Multiple charge types** knocked off at disbursement (processing fee today, others in future) owned by different lenders.
- Primary users:
    - Finance & Ops teams (reconciliation, settlement)
    - Engineering (LMS, accounting, settlement flows)
- Secondary users:
    - Sales & onboarding teams (clear explanation of net disbursal vs loan amount)
    - Risk & Audit teams

---

### Out of scope

- Interest accrual logic changes
    - Interest continues to follow existing borrower-level rules
- Customer-facing UI redesign
    - No changes to how the customer views the loan, beyond correctness
- Partner commercial renegotiation
    - Assumes existing ownership rules are final
- Bureau reporting changes
    - Borrower-facing loan remains the single source for external reporting

**Rationale**:

These are orthogonal concerns and would delay solving the core accounting and settlement correctness problem.

---

## **2. Success Criteria**

### Primary outcomes

1. **Correct economic settlement**
    - Partner recoveries exactly match agreed ownership (principal + capitalised charges)
2. **Extensibility**
    - New charge types can be knocked off at disbursement **without new split logic**
3. **Operational simplicity**
    - No manual adjustments during partner reconciliation

---

### Key success metrics

- **Zero reconciliation breaks** between DSP and TCL post-launch
- **100% accuracy** in partner settlement amounts for disbursement and collections
- **No increase** in repayment or disbursement failure rates

---

### Post-launch “good state”

- Single disbursement workflow handles:
    - Net disbursement
    - Capitalised charges
    - Partner splits
- Repayment logic remains **generic and invariant**
- Shadow balances always reconcile to borrower POS

---

### Guardrail metrics

- No degradation in:
    - Disbursement TAT
    - Repayment success rate
    - Customer statement accuracy
- No increase in:
    - Ops manual interventions
    - Finance reconciliation effort

---

## **3. Solution Scope**

### Solution overview

- Introduce a **borrower-facing loan** and **partner shadow loans**
- All charges knocked off at disbursement are:
    - Short disbursed on the borrower loan (DSP 100)
    - Economically owned via shadow loans (DSP10 and TCL90)
- Disbursement, repayment, and reconciliation operate on a **single invariant**:
    
    > Sum of shadow loan balances must always equal borrower loan POS
    > 

This solution is scoped to be **foundational**, avoiding future rewrites as new charges or partners are added.

---

### Detailed solution scope

### Core concepts

- **DSP 100 loan**
    - Borrower-facing, legally enforceable loan
    - Used for:
        - Customer UI
        - Statements
        - Bureau reporting
    - Contains:
        - Principal
        - All capitalised charges knocked off at disbursement
- **Shadow loans (DSP 10, TCL 90)**
    - Internal only
    - Represent **economic ownership**
    - Do **not** originate charges or interest independently
    - Only mirror ownership of borrower obligations

---

### Supported use cases

| Description | Details |
| --- | --- |
| Disbursement with charge knock-off | Disbursement request includes charges to be knocked off; borrower POS reflects gross amount |
| Capitalised DSP-only charges | Charges appear once on borrower loan, owned via DSP shadow loan |
| Multiple disbursements (OD behaviour) | Subsequent disbursements increase shadow POS only in principal proportions |
| Repayments (partial / full) | Applied to borrower loan, allocated to shadow loans pro-rata |
| Future charge types | New charges can be introduced without changing repayment logic |
| Partner reconciliation | Based entirely on shadow loan balances and movements |

---

### Key edge cases handled

- Partial repayment followed by redraw
- Multiple disbursements with charges only on some draws
- Early foreclosure
- Charge reversal (future-safe)

---

### Operational & user impact

- **Ops / Finance**
    - Simplified reconciliation
    - Clear separation of borrower vs partner economics
- **End user**
    - No visible change
    - Correct loan amount and repayment behaviour
- **Sales / Onboarding**
    - Clear explanation: “Loan amount includes capitalised charges; net disbursed may be lower”

---

## **5. High-level system / process flow**

- Disbursement request created with:
    - Gross amount
    - Charges to be knocked off
- System:
    1. Creates borrower loan POS (gross)
    2. Applies charge knock-off
    3. Allocates economic ownership via shadow loans
- Repayment:
    - Applied to borrower loan
    - Automatically distributed to shadow loans
- Reconciliation:
    - Partner settlements driven only by shadow loans

Edge cases:

- Validation if shadow POS ≠ borrower POS
- Blocking redraw if invariants are violated

---

## **6. Appendix (Optional)**

### Benchmarking

- Shadow-ledger based co-lending models used in:
    - OD and CC products
    - Securitisation-ready lending systems
    - Multi-partner lending platforms

### User feedback / Calling

- Finance & Ops feedback indicates:
    - Manual adjustments today are error-prone
    - Desire for deterministic, system-led settlement logic