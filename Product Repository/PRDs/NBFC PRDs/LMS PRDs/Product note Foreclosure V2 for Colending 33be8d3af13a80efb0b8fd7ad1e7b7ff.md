# Product note: Foreclosure V2 for Colending

Last Edited: April 24, 2026 7:43 AM
PRD ETA: April 7, 2026
PRD Owner: Vaibhav Arora
Status: Pending review

## **Background and Context**

Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges.

In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across:

- **Loan 90 (NBFC exposure)**
- **Loan 10 (Partner/Lender exposure)**

Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across Loan 90 and Loan 10 in the Colending Loan Management System (CLMS).

---

### **Who is impacted**

- Borrowers initiating foreclosure
- Lending partners (colending participants)
- Operations teams processing closures
- Product and engineering teams responsible for transaction sequencing
- Finance teams responsible for settlement and accounting

---

### **What is broken today**

1. **Incorrect foreclosure simulation**

Foreclosure amounts are often computed using Loan 100 without fully reconciling Loan 90 and Loan 10 balances.

1. **Pending transaction inconsistencies**

Foreclosure may be initiated even when pending transactions exist in CLMS, leading to incorrect payoff calculations.

1. **Transaction sequencing issues**

Loan closure and collateral release may occur without ensuring:

- Loan 10 and Loan 90 are closed
- All dues and interest are settled
- Excess is correctly handled
1. **Penalty and applicable charge dependency**

Charges (such as penal charges) may be posted after repayment due to system jobs, leading to foreclosure failures.

1. **Incorrect collateral release timing**

Collateral may be released before confirming closure of underlying loan legs.

1. **Excess handling gap in colending**
- Excess is parked in Loan 100
- Excess does not auto-settle dues or accrued interest
- There is no native way to use excess during foreclosure

This leads to:

- Incorrect net payable shown to users
- Failed foreclosure despite sufficient excess
- Manual intervention for settlement
- Reconciliation gaps

---

### **Why this is important**

Foreclosure is a **high-intent and customer-sensitive journey**.

Incorrect handling leads to:

- Poor customer experience
- Increased operational workload
- Financial and accounting mismatches
- Risk of incorrect collateral release

This PRD ensures:

- Accurate payoff computation
- Deterministic transaction sequencing
- Proper utilization of excess
- Correct closure and refund handling

---

# **1. Problem Scope**

## **In Scope**

### **1. Colending foreclosure simulation**

Foreclosure simulation will compute payoff using:

- Loan 100
- Loan 90
- Loan 10

Reconciliation logic:

- Principal Outstanding = POS Loan 100 = POS Loan 90 + POS Loan 10
- Interest Due = ID Loan 100 = ID Loan 90 + ID Loan 10
- Charges = C Loan 100 = C Loan 90 + C Loan 10
- Accrued Interest = AI Loan 100 = AI Loan 90 + AI Loan 10

---

### **2. Net payable computation (Excess-aware)**

For colending loans (get foreclosure detail API):

**Net Payable = (Total Due + Accrued Interest) - Excess**

- Excess is not auto-settled in LMS
- It is logically adjusted in the API response

Behaviour:

- If Net Payable < 0 → show 0 to user
- Remaining amount treated as refundable excess

---

### **3. Excess utilization during foreclosure**

- Excess will be utilized via **orchestrated transactions**
- Includes:
    - Excess Payment (for dues)
    - Clear Dues (for accrued interest)
    - Excess Refund (to consume excess)

---

### **4. Pending transaction validation**

- Foreclosure must not proceed if CLMS has pending transactions
- API may return values but:
    - `isForeclosureAllowed = false`
    

---

### **5. Account freeze during foreclosure**

Once foreclosure is initiated:

- No withdrawals
- No enhancement requests
- No collateral release requests
- No Repayments
- No service requests

---

### **6. Loan closure sequencing**

Closure must follow:

1. Settle dues and interest (Excess orchestration from Loan 100 to Loan 10 and Loan 90)
2. Close Loan 90
3. Close Loan 10
4. Release collateral
5. Close Loan 100
6. Process excess refund

---

### **7. Collateral release**

- Only after Loan 10 and Loan 90 closure confirmation
- Includes unpledge and LMS updates

---

### **8. Business hour dependency**

- Before 6 PM → same-day processing
- After 6 PM → next-day processing
- Ensures all charges are applied before closure

---

## **Out of Scope**

- Changes to Finflux core behaviour for auto excess usage
- UI changes in partner apps
- Foreclosure charges

---

# **2. Success Criteria**

### **Primary outcomes**

- Accurate foreclosure computation across all loan legs
- Successful foreclosure when Excess ≥ (Dues + AI)
- No manual intervention required
- Correct excess refund

---

### **Key Metrics**

- Foreclosure success rate > 99%
- Manual ops intervention minimal

---

### **Post-launch Behaviour**

- Foreclosure always reflects true exposure
- Excess is fully and correctly utilized
- Loans are closed in correct sequence
- No reconciliation gaps

---

### **Guardrails**

- No incorrect refunds
- No partial closures
- No premature collateral release
- No mismatch between Loan 100 and Loan 10/90

---

# **3. Solution Scope**

## **Solution Overview**

The solution enhances foreclosure for colending loans by:

- Introducing **excess-aware net payable calculation**
- Using **explicit transaction orchestration** to utilize excess
- Ensuring **strict sequencing across Loan 100, 90, and 10**

Excess is not auto-used — it is **converted into repayment through controlled transactions**.

---

## **Detailed Solution Scope**

---

### **1. Foreclosure Simulation API**

Response fields:

- outstandingPrincipal
- outstandingInterest
- outstandingCharges
- outstandingPenalCharges
- totalDue
- excessAmount
- interestAccruedNotDue
- netPayable
- isForeclosureAllowed

---

### **Net Payable Logic**

**Net Payable = (totalDue + interestAccruedNotDue) - excessAmount**

- If negative → return 0
- Excess reflected separately

---

### **2. Foreclosure Validation**

At time of foreclosure:

Let:

- E = Excess
- O = Pending processing repayment order amount passed in foreclosure request
- D = Total Due
- AI = Accrued Interest

Validation:

- If E + O < (D + AI) → foreclosure not allowed
- Else → proceed

---

### **3. Foreclosure Execution Logic**

---

### **Scenario 1: E +** O **> D + AI**

In this scenario we will first wait for O - repayment order to get settled before starting the foreclosure workflow

**Step 1: Settle Dues**

- Trigger Excess Payment = D (Due amount)
- Settles dues across in loan 100
- Following this transaction initiate Payin’s as per repayment splitting logic in Loan 90 and Loan 10 (Keep reference of these payins with the initiated excess payment)

**Step 2: Settle Accrued Interest**

- Trigger Clear Dues (AI)
- Trigger Excess Refund with payment type (’Accrued interest settlement’) = AI (no user payout)
- Initiate Payins as per accrued interest splitting logic across Loan 90 and Loan 10(Get Loan 90 and Loan 10)

**Step 3: Loan Closure**

- Close Loan 90
- Close Loan 10
- Release collateral
- Close Loan 100

**Step 4: Refund**

- Refund = E - D - AI

---

### **Scenario 2: E = D + AI**

- Same flow
- No refund

---

### **Scenario 3: E < D + AI**

- Foreclosure blocked

---

### **4. Transaction Behaviour**

### **Excess Payment**

- Source: excess balance
- Behaviour: same as repayment
- Allocation: standard hierarchy

### **Clear Dues**

- Converts accrued interest → due
- Settles it

### **Excess Adjustment**

- Internal transaction
- Reduces excess
- No actual payout

---

### **5. Loan Closure steps in workflow**

1. Foreclosure request is created in loan 100
2. Excess Payment to settle dues if anything is outstanding 
3. Loan 90 and Loan 10 payins as per split logic of excess payment of loan 100
4. Clear Dues for accrued interest in loan 100
5. Excess refund equal to clear dues amount in loan 100
6. ~~Loan 90 and Loan 10 payins as per split logic~~ of accrued interest in loan 90 and loan 10
7. Release collateral in Loan 90
8. Close Loan 90
9. Release collateral in Loan 10
10. Close Loan 10
11. Release collateral in loan 100
12. Refund excess
13. Close loan 100

---

## **Description Table**

| Description | Details |
| --- | --- |
| Foreclosure simulation | Uses Loan100 + Loan90 + Loan10 |
| Net payable | Adjusted using excess |
| Validation | Blocks if insufficient excess |
| Excess handling | Orchestrated via transactions |
| Closure sequencing | Loan10 → Loan90 → Loan100 |
| Collateral release | After CLMS closure |
| Refund | Post settlement |

---

# **5. High Level Flow**

### **Foreclosure Simulation**

1. Fetch Loan 100, 90, 10 balances
2. Apply reconciliation logic
3. Compute dues, AI, excess
4. Adjust net payable
5. Return response

---

### **Foreclosure Processing**

1. User initiates foreclosure
2. Validate pending transactions
3. Freeze account
4. Validate E ≥ D + AI
5. Trigger:
    - Excess Payment
    - Clear Dues
    - Excess Adjustment
6. Close Loan 10
7. Close Loan 90
8. Release collateral
9. Close Loan 100
10. Refund excess
11. Generate closure confirmation

---

# **6. Appendix**

## **Key Design Principles**

- Finflux acts as **execution/ledger system**
- Orchestration layer controls:
    - When excess is used
    - How much is used
    - Sequence of transactions

---

## **Operational Benefits**

- No manual excess adjustment
- Reduced closure errors
- Cleaner reconciliation
- Improved customer experience