# Product note: Virtual account handling for Colending

Last Edited: April 7, 2026 3:38 PM
PRD ETA: March 25, 2026
PRD Owner: Vaibhav Arora
Status: Completed

## **Background and Context**

- **Who is facing the problem**
    - NBFC (DSP) – Product, Ops, Finance teams
- **What is the challenge**
    - In the current Virtual Account (VA) setup, all repayments are credited to a **single DSP collection account**
    - However, for **co-lended loans**, regulations mandate that:
        - Funds must flow into a **designated escrow account** (not DSP’s own account)
    - Yes Bank’s existing integration:
        - Identifies VA → calls our **Validate API**
        - Credits funds to a **pre-configured account**
    - This creates a gap:
        - System today does **not dynamically decide the destination account**
        - No linkage between **loan → colending contract → escrow account**
- **Why is it important**
    - Regulatory non-compliance if funds are credited to incorrect accounts
    - Incorrect fund flows → breaks lender settlement and reconciliation
    - Operational risk → manual reversals, audit failures
    - Scaling issue → multiple co-lenders require dynamic routing

---

## **1. Problem scope**

### In scope

- Enable **dynamic credit account routing** for VA collections based on:
    - Loan → Contract → Escrow account mapping
- Enhance **Validate API response** to return:
    - Correct **credit account (escrow / DSP account)**
- Support:
    - Colending loans → Escrow routing basis contract configuration
    - Non-colending loans → DSP account routing
- Store and manage:
    - **Contract-level credit account mapping (DSP 100% should also be a contract)**
- Stakeholders:
    - Primary: Ops, Finance, Lending Systems
    - Secondary: Yes Bank, LSPs, Customers

---

### Out of scope

- Changes to:
    - VA generation logic (e-collect code remains same: 301301)
    - Checker workflows (remain unchanged), credit account should be added as a parameter in the checker task
    - Notify API structure (only extended usage, not redesigned)
- Advanced validations:
    - Name match, whitelist accounts (Currently live - Remains unchanged)
- Multi-account routing within a single contract - One contract can have one bank account as part of the proposed set up.

---

## **2. Success Criteria**

### Key outcomes

- **100% compliance** with escrow routing for co-lending loans
- **Zero misrouted transactions** (DSP vs Escrow)
- **Seamless bank integration** without additional retries/failures

### Metrics

- % of VA transactions correctly routed to escrow (target: 100%)
- Validate API success rate (pass rate without checker approval > 98%)
- Reconciliation breaks due to incorrect credit account (target: 0)

### Post-launch good state

- Yes Bank:
    - Always receives correct credit account in Validate response
- System:
    - Automatically routes based on contract
- Ops:
    - No manual intervention for routing decisions

### Guardrails

- No increase in:
    - Validate API latency
    - Transaction failure rate
    - Pending/timeout cases

---

## **3. Solution Scope**

### Solution overview

We will enhance the **Validate API response** to dynamically return the **credit account number** (escrow or DSP account) based on the **colending contract mapped to the loan**.

This is enabled via:

- **Contract-level configuration of credit account**
- Runtime lookup during Validate API call

This approach:

- Keeps existing VA flows intact
- Introduces minimal changes to bank integration
- Ensures regulatory compliance

---

### Detailed solution scope:

### Core Logic

- On Validate API call from Yes Bank:
    1. Identify **loan using VA (bene_account_no)**
    2. Get customer details and validate the transaction as per STP and non STP
    3. if STP
    4. Fetch **contract linked to loan**
    5. Check:
        - If **colending loan** → fetch escrow account
        - Else → use DSP collection account
    6. Return:
        - `decision = pass`
        - `credit_account_no = <mapped account>`
    7. If NSTP create a checker task, and pass pending till the checker task is unapproved, when approved follow step 4,5,6 and await notify call (credit confirmation for credit confirmation)
    8. If checker task rejected, pass reject and await notify call for refund confirmation)

---

### Use Cases

| Description | Details |
| --- | --- |
| Colending loan repayment | Validate API returns escrow account mapped at contract level |
| Non-colending loan repayment | Validate API returns DSP collection account |
| Invalid VA | Reject transaction |
| Loan inactive/closed | Reject transaction |
| Contract mapping missing | Fail-safe → reject |
| Pending approval (maker-checker) | Return `pending` as per existing flow |
| Retry handling | Yes Bank retries based on existing logic |

---

### Notify API Handling

- Yes Bank will send:
    - **Remitter account details**
    - **Beneficiary (credited) account details**
- System will:
    - Validate that credited account matches expected mapping
    - Post repayment to loan
    - Maintain audit trail for:
        - Escrow vs DSP routing

---

### Contract-Level Configuration

New data points at contract level:

- **Escrow account number (NEW)**
- Escrow IFSC

---

### Operational Impact

- **Ops team**
    - No change in maker-checker flow
    - Additional visibility:
        - Credited account (escrow vs DSP) in the checker task
- **Finance**
    - Cleaner reconciliation:
        - Direct escrow credits for co-lending
- **LSP**
    - No change in user flow
    - VA shared remains same

---

## **5. High level system / process flow**

### Step-by-step flow

1. Customer initiates payment to VA
2. Yes Bank detects transaction
3. Yes Bank calls **Validate API**
4. System processing:
    - Identify loan via VA
    - Fetch contract
    - Determine:
        - Escrow account (colending) OR
        - DSP account (non-colending)
5. System responds:

```
{
  "validateResponse": {
    "decision":"pass",
    "credit_account_no":"ESCROW_ACCOUNT_NUMBER"
  }
}
```

(As per Yes Bank enhancement)

1. Yes Bank credits the specified account
2. Yes Bank triggers **Notify API**:
    - Includes:
        - Remitter account
        - Beneficiary (credited) account
3. System:
    - Confirms transaction
    - Posts repayment to loan
    - Triggers LSP callback

---

### Edge cases

- Contract not found → reject
- Escrow account missing → reject (compliance critical)
- Duplicate UTR → NSTP
- Delay in maker-checker → pending → auto-reject via CRON

---

## **6. Appendix (Optional)**

### Key Change from Existing System

| Area | Current | Proposed |
| --- | --- | --- |
| Credit account | Static DSP account | Dynamic (Escrow / DSP) |
| Routing logic | None | Contract-driven |
| Compliance | Not enforced | Fully compliant |
| Bank response | Decision only | Decision + credit account |

---

### Future Enhancements

- Multi-escrow support per contract
- Smart routing based on payment type
- Real-time reconciliation with bank
- Automated audit flags for mismatches