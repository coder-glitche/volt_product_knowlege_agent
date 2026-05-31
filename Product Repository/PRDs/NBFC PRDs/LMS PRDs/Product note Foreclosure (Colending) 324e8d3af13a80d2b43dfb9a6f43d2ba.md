# Product note: Foreclosure (Colending)

Last Edited: May 19, 2026 2:47 PM
PRD ETA: March 15, 2026
PRD Owner: Vaibhav Arora
Status: Completed

# **Background and Context**

Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges.

In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across:

- **Loan 90 (NBFC exposure)**
- **Loan 10 (Partner/Lender exposure)**

Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**.

### Who is impacted

- Borrowers initiating foreclosure
- Lending partners (colending participants)
- Operations teams processing closures
- Product and engineering teams responsible for transaction sequencing
- Finance teams responsible for settlement and accounting

### What is broken today

Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations:

1. **Incorrect foreclosure simulation**
    
    Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances.
    
2. **Pending transaction inconsistencies**
    
    Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations.
    
3. **Transaction sequencing issues**
    
    Loan closure and collateral release may occur without ensuring that:
    
    - Loan 90 and Loan 10 are closed
    - All charges and interest are posted
    - Excess settlement is completed
4. **Penalty and applicable charge dependency**
    
    Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment.
    
5. **Incorrect collateral release timing**
    
    Securities may be released before confirming that **both loan legs are closed**, which introduces risk.
    

### Why this is important

Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to:

- Incorrect payoff amounts shared with borrowers
- Operational rework due to partial closures
- Accounting mismatches across loan legs
- Risk of releasing collateral before loan closure creating financial exposure for the NBFC

This PRD defines a **colending foreclosure workflow** that ensures:

- Correct payoff simulation
- Transaction sequencing across loan legs
- Controlled collateral release
- Accurate excess settlement.

---

# **1. Problem Scope**

## **In Scope**

### **Colending foreclosure simulation**

Foreclosure simulation will incorporate balances from:

- Loan 100
- Loan 90
- Loan 10

to ensure accurate payoff computation.

---

### **Pending transaction validation**

Foreclosure requests must not be accepted if **pending transactions exist in CLMS that is foreclosure allowed flag should be false**

The simulation API may return values, but **foreclosure initiation must be blocked** when pending transactions exist. The API should fail with the message that foreclosure is not allowed as transactions are in progress for this account.

---

### **Charge and interest reconciliation**

Foreclosure simulation must reconcile balances across loan legs using the following logic if there are no pending transactions in CLMS, if there are Loan 100 values will be passed in the response with the foreclosure allowed flag is disabled:

Interest Due = Loan 100 interest due

Max(Loan100 Interest Due, Loan90 Interest Due + Loan10 Interest Due)

Interest Accrued = Loan 100 IA

Max(Loan100 Accrued Interest, Loan90 Accrued Interest + Loan10 Accrued Interest)

Charge Due = Loan 100 CD

Max(Loan100 Charge Due, Loan90 Charge Due + Loan10 Charge Due) + Applicable charges 

Principal Outstanding = Loan 100 POS

Max(Loan100 POS, Loan90 POS + Loan10 POS)

---

### **Penalty and applicable charge dependency**

Foreclosure must account for **applicable charges posted via Fenix jobs** (such as daily penalty computation).

This requires sequencing foreclosure processing with the applicable charge job.

---

### **Account freeze during foreclosure (Loan 100)**

Once foreclosure request is accepted:

- Loan account will be **frozen (Currently implemented)**
- No further withdrawals **(Currently implemented)**
- No collateral release requests **(Currently implemented)**
- No enhancement requests **(Currently implemented)**

---

### **Loan closure sequencing**

Loan closure must follow this sequence:

1. Close **Loan 90**
2. Close **Loan 10**
3. Process excess settlement on loan 100
4. Release collateral on loan 100 (with RTAs and in the LMS)
5. Close **Loan 100**

---

### **Collateral release**

Collateral will only be released **after Loan 90 and Loan 10 closure confirmation**.

---

### **Excess settlement in the foreclosure workflow**

If repayment exceeds payable amount:

- Excess funds will be used to settle:
    - accrued interest
    - applicable charges
- Remaining excess will be refunded to the customer.

---

### **Business hour processing rule**

Foreclosure simulation and processing follow business hour rules:

- **Before 6 PM:** same-day simulation
- **After 6 PM:** next-day simulation

This ensures applicable charges and penalties are applied before foreclosure and are also considered in both foreclosure simulation amount being passed to the user and being consumed in the LMS from a collections perspective

---

## **Out of Scope**

The following items are outside the scope of this enhancement.

### Foreclosure charges

There are currently **no foreclosure charges** defined in the product construct.

---

### UI changes in partner applications

Changes to LSP user interfaces are outside this scope.

---

# **2. Success Criteria**

### **Primary outcomes**

1. Foreclosure amounts accurately computed across **Loan 100, Loan 90, and Loan 10**.
2. Foreclosure requests blocked when **pending transactions exist**.
3. Correct sequencing of **loan closure, excess refund, and collateral release**.

---

### **Key Metrics**

| Metric | Target |
| --- | --- |
| Foreclosure computation accuracy | 100% |
| Foreclosure closure success rate | >99% |
| Collateral release sequencing errors | 0 |

---

### **Expected Post-Launch Behaviour**

- Foreclosure amount reflects **true loan exposure across loan legs**
- No foreclosure initiated when **transactions are pending**
- Collateral released **only after loan closure confirmation**

---

### **Guardrail Metrics**

- No increase in foreclosure API latency
- No incorrect loan closures
- No premature collateral release

---

# **3. Solution Scope**

## **Solution Overview**

The foreclosure workflow will be enhanced to support **colending loan structures** by integrating data from **Loan 100, Loan 90, and Loan 10** and enforcing strict transaction sequencing.

The solution introduces:

- Colending foreclosure simulation
- Pending transaction validation
- Controlled loan closure sequencing
- Penalty and applicable charge synchronization
- Correct collateral release timing

---

# **Detailed Solution Scope**

### **1. Foreclosure Simulation API**

The foreclosure API will return the total payoff amount including:

- Principal outstanding
- Interest due
- Accrued interest
- Charges
- Applicable charges

The API will compute the values using the **maximum exposure across Loan 100 and combined Loan 90 + Loan 10 balances**.

---

### **2. Pending Transaction Validation**

Before initiating foreclosure:

- CLMS will be checked for **pending transactions**
- If pending transactions exist:
    
    Foreclosure simulation may still return values
    
    but **foreclosure request will not be accepted**
    

---

### **3. Foreclosure Request API**

The foreclosure initiation API will remain consistent with the current contract.

Example request:

```
{
  "loanAccountId":"FXLAN65378191",
  "repaymentId":"RPOID179353511525",
  "makerNotes":"request raised from the COMMAND_CENTER"
}
```

If repayment has already been processed in Loan 100:

- repayment amount will be ignored

If repayment order is successful but not posted in LMS:

- repayment amount will be used for validation.

---

### **4. Account Freeze**

After foreclosure request is accepted:

Loan account will be frozen to prevent:

- withdrawals
- enhancement requests
- collateral release requests.

---

### **5. Repayment Processing**

Once repayment is posted:

Net payable is calculated as:

Net Payable =

Principal Outstanding + Interest Due + Accrued Interest + Charge Due + Applicable Charges

If Net Payable ≤ 0:

- foreclosure workflow proceeds.

---

### **6. Penalty Job Dependency**

Applicable charges such as **penal charges** may be posted through the **Fenix daily charge job**.

To avoid closure failures:

- Foreclosure requests raised **after 6 PM** will be processed **next morning (10 AM)**.

This ensures:

- penalty job runs
- applicable charges are posted before closure.

---

### **7. Loan Closure Sequencing**

Loan closure must follow this order:

1. Close Loan 10 in CLMS
2. Close Loan 90 in CLMS
3. Process excess settlement
4. Release securities
5. Close Loan 100

This ensures that borrower-visible loan closure occurs **only after partner obligations are settled**.

---

### **8. Collateral Release**

Once Loan 90 and Loan 10 are successfully closed:

- securities will be **unpledged**
- securities will be **unlodged from LMS**

---

### **9. Excess Refund**

If excess amount exists after settlement:

- refund will be initiated to the borrower.

---

| Description | Details |
| --- | --- |
| Foreclosure simulation | Uses Loan100 + Loan90 + Loan10 |
| Pending transaction validation | Blocks foreclosure request |
| Penalty dependency | Wait for Fenix charge job |
| Account freeze | Prevents further transactions |
| Closure sequencing | Loan10 → Loan90 → Loan100 |
| Collateral release | After CLMS closure |
| Excess refund | Processed before final closure |

---

# **5. High Level System Flow**

### **Foreclosure Simulation**

1. User requests foreclosure amount
2. System fetches Loan100 balances
3. Fetch Loan90 and Loan10 balances
4. Apply reconciliation rules
5. Return foreclosure amount.

---

### **Foreclosure Processing**

1. Foreclosure request initiated
2. Account freeze applied
3. Repayment processed
4. Pending transaction validation
5. Net payable check
6. Loan10 closure
7. Loan90 closure
8. Excess settlement
9. Collateral release
10. Loan100 closure
11. Confirmation + No Dues Certificate issued.

---

# **6. Appendix**

## **Benchmarking**

Most modern colending LMS architectures implement **multi-loan foreclosure sequencing** where borrower-visible accounts are closed only after underlying loan exposures are settled.

This approach ensures:

- correct partner settlement
- correct collateral handling
- accurate borrower communication.

---

### **User Feedback / Operational Inputs**

Operations teams highlighted issues with:

- foreclosure attempts failing due to pending transactions
- sequencing errors during loan closure
- incorrect payoff simulations

This enhancement directly addresses those operational constraints.