# Product note: Razorpay PG integration Colending

Last Edited: April 7, 2026 3:38 PM
PRD ETA: March 26, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## **Background and Context**

- **Who is facing the problem**
    - NBFC (DSP) – Product, Engineering, Finance
    - Co-lenders (e.g., TCL)
    - Payment partner (Razorpay)
    - LSPs (Volt) and end customers
- **What is the challenge**
    - Current PG integration uses a **single MID (merchant account)** for all repayments
    - For **co-lended loans**, regulations require:
        - Funds to be collected directly into a **designated escrow account**
    - In Razorpay:
        - **MID determines settlement account**
        - Each MID has **separate API credentials**
    - System today:
        - Does not differentiate between **colending vs non-colending loans at MID level**
- **Why is it important**
    - Regulatory requirement → escrow-based fund flow
    - Incorrect MID usage → funds settle to wrong account
    - Breaks reconciliation and lender settlement
    - Scaling issue → multiple co-lenders = multiple MIDs

---

## **1. Problem scope**

### In scope

- Enable **dynamic MID selection** for PG repayments:
    - Colending loans → escrow-linked MID (at a contract level - Makes it extendable to multiple MIDs for multiple colending relationships)
    - Non-colending loans → DSP MID
- Store:
    - **MID at contract level**
- Fetch:
    - API credentials via **secret manager (not stored directly)**
- Ensure:
    - All Razorpay operations use the **same MID context**:
        - Order creation
        - Payment fetch
        - Payment validation
- Stakeholders:
    - Primary: Engineering, Finance
    - Secondary: Razorpay, LSPs

---

### Out of scope

- Changes to:
    - Razorpay API contracts (no change)
    - SDK integration at frontend (Volt continues as-is)
- Multi-MID fallback logic within a single contract
- Changes to repayment lifecycle or LMS posting

---

## **2. Success Criteria**

### Key outcomes

- **100% correct routing of PG funds** to escrow for colending loans
- **Zero reconciliation issues** due to incorrect MID usage
- Seamless experience for LSP and end user (no UX changes)

### Metrics

- % of PG transactions using correct MID (target: 100%)
- Payment success rate (no degradation post rollout)
- Reconciliation mismatches due to MID errors (target: 0)

### Post-launch good state

- MID selection is:
    - Fully automated
    - Invisible to end user
- All Razorpay flows work unchanged

### Guardrails

- No increase in:
    - Order creation failure rate
    - Payment verification failures
    - API latency

---

## **3. Solution Scope**

### Solution overview

We will introduce **contract-level MID configuration** and dynamically select the appropriate MID during repayment order creation.

All Razorpay API interactions will be executed in the context of the selected MID.

---

### Detailed solution scope:

### Core Logic

- On **Repayment Order Create API hit**:
    1. Identify loan
    2. Check:
        - If **colending loan** → fetch contract MID
        - Else → use default DSP MID
    3. Create Razorpay order using selected MID

---

### Razorpay Operations (All use same MID)

- Order creation
- Fetch order details
- Fetch payment details
- Payment validation before LMS posting

👉 Ensures consistency across full payment lifecycle

---

### SDK Flow (Volt / LSP)

- No change:
    - Backend creates order
    - Returns **order_id**
    - SDK invoked using order_id
- Since:
    - Order is already tied to correct MID
    → SDK works **out of the box**

---

### Contract-Level Configuration

New data point:

- MID (linked to escrow account for colending contracts)

---

### Credential Management

- No credentials stored in DB
- Flow:
    - MID → Secret Manager → Fetch credentials at runtime

---

### Use Cases

| Description | Details |
| --- | --- |
| Colending loan repayment | Order created using escrow-linked MID |
| Non-colending loan repayment | Order created using DSP MID |
| Payment verification | Done using same MID as order creation |
| Invalid MID mapping | Fail order creation |
| Missing credentials | Fail safely with error |

---

### Operational Impact

- **Engineering**
    - Introduce MID resolution layer
    - Integrate with secret manager
- **Finance**
    - Clean settlement to escrow vs DSP accounts
    - Reconciliation: Finance will have to use multiple reports from multiple accounts (Razorpay MIDs) to reconcile all payments
- **LSP / Customer**
    - No change in UX

---

## **5. High level system / process flow**

1. User initiates repayment via app
2. LSP calls **Create Repayment Order API**
3. System:
    - Identifies loan
    - Resolves MID:
        - Colending → contract MID
        - Else → DSP MID
4. System creates Razorpay order
5. Returns:
    - `order_id` to LSP
6. LSP invokes Razorpay SDK
7. Payment completed
8. System:
    - Fetches payment using same MID
    - Validates transaction
    - Posts repayment in LMS

---

### Edge cases

- Contract exists but MID missing → fail order creation
- Secret manager failure → retry / fail
- Payment fetched with wrong MID → reject (safety check)
- MID mismatch across lifecycle → block posting

---

## **6. Appendix (Optional)**

### Key Change from Existing System

| Area | Current | Proposed |
| --- | --- | --- |
| MID usage | Single MID | Dynamic per contract |
| Settlement account | DSP account | Escrow / DSP |
| Credential handling | Static | Secret manager आधारित |
| SDK flow | Static | Unchanged |

---

### Future Enhancements

- Multi-MID support per contract
- Intelligent routing (based on payment type/channel)
- MID-level analytics and reconciliation dashboards