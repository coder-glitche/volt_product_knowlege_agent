# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds)

Last Edited: December 11, 2025 2:41 PM
PRD Owner: Vaibhav Arora
Status: Completed

## **1. Problem Statement**

Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for:

- Accurate repayment allocation
- DPD computation
- Interest/charge tracking
- Reconciliation, reporting (internal and external)

Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations.

We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur.

---

## **2. Context: How It Should Work (High Level)**

- Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule.
    - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule
- When a transaction settles that obligation, the schedule and derived details should reflect:
    - obligation met
    - amount accounted
    - linkage to the transaction identifier
    - timestamps for audit
- For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.).

Finflux already follows this pattern for regular repayments.

The gaps occur only for specific transaction types listed below.

---

## **3. Issues & Required Enhancements**

---

## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details***

### **Current Behaviour**

- During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line:
    - Accrued-but-not-yet-due interest is first made due.
    - Finflux then settles this newly created due using excess funds when the clear dues API is hit
- However:
    - The **schedule table is not updated** to reflect the new temporary obligation.
    - The **obligation is not marked as met**.
    - **Derived details** are not populated with the settlement transaction.

### **Impact**

- Reporting discrepancies (interest recognised vs. interest settled).
- Incorrect DPD because obligations appear “unmet”.

### **Required Behaviour**

Finflux should:

1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge).
2. **Immediately settle the obligation** and mark:
    - obligation_met = true
    - obligation_met_on = timestamp
3. **Populate derived details** with:
    - linkage to the clear-dues transaction
    - interest/fee/penalty break-up
    - accounted amounts
4. Apply this consistently across **all schedule-related tables**, not limited to the two referenced.

---

## **3.2 Issue 2: *Interest Waiver does not update schedule and derived details correctly***

### **Current Behaviour**

- Interest waiver transactions waive only **due** interest (never accrued).
- An obligation already exists on the schedule line.
- When a waiver happens:
    - The obligation reduces with the waived amount.
    - Derived details do not correctly reflect the waived amounts or transaction linkage with the interest waiver transaction.

### **Impact**

- Incorrect ageing/DPD because waived amounts appear still outstanding.
- Derived details under-report interest adjustments, impacting MIS and reconciliations.
- Line-level interest summary becomes inaccurate.

### **Required Behaviour**

Finflux should:

1. **Update the existing obligation** on the schedule to reflect that the waived amount has been met via waiver.
2. **Populate derived details** with:
    - transaction identifier of the waiver
    - amount waived (ledger-wise split)
3. Ensure the loan’s obligation state reflects that no dues remain for that component.

---

## *3.3 Issue 3: *Incorrect Waiver behaviour (FIFO instead of LIFO) and not at a transaction level*

### **Current Behaviour**

- For OD, when waiving interest, Finflux applies a **FIFO logic** — (latest interest is waived first).
- Operationally and from a DPD-minimisation standpoint, the **waiver should apply to the oldest due interest first (LIFO)**.
- As an NBFC we need the use case where we are able to define at a transaction level or at a schedule level as to what interest has to be waived for the user.
    - Use case 1: Waiver to user in case of transaction issues, that way DPD benefit should be passed to the user.
    - Use case 2: If for a specific month, interest calculation has been impacted, or repayment posting were delayed, we would to give interest benefit to the user for that specific month.

### **Impact**

- DPD optimisation fails:
    - Older dues remain open even though waivers were applied.
- Customer delinquency status becomes inaccurate.
- Impacts reporting, bureau logic and internal risk metrics.

### **Required Behaviour**

- Change interest waiver allocation logic for OD products at an interest level:
    - We should be able to define which interest either by transaction ID or by schedule ID for the interest
- Ensure schedule and derived details consistently reflect this ordering to prevent reconciliation mismatches.

---

## **4. Functional Requirements Summary (High-Level)**

Finflux should make enhancements so that:

1. **All transactions that impact dues (clear dues, interest waiver, charge reversals, etc.) correctly update:**
    - schedule tables
    - derived details
    - all associated internal tables that represent obligations, accounting states, or transaction-to-schedule mapping
2. **Every due created must have:**
    - a corresponding schedule obligation
    - a source transaction mapping which created the schedule
    - a settlement or waiver event recorded in derived details
3. **Every settlement/waiver must:**
    - reduce or close the obligation
    - update accounted amounts against the right components
4. **Allocation logic for OD interest waivers must follow LIFO if not specified, else should be at a source transaction/schedule level.**
5. **Enhancements should not be limited to the two tables shared; Finflux must review and update all relevant LMS tables** involved in:
    - schedule representation
    - settlement mapping
    - obligation tracking
    - derived transaction details
    - interest/fee/penalty accounting

---

## **5. Success Criteria**

- No orphan obligations for clear-dues or waiver transactions.
- Schedule reflects accurate billed vs. settled vs. waived status at all times.
- Derived details always show correct transaction mapping and break-ups.
- LIFO ordering for OD interest waivers consistently applied.
- Downstream reporting (DPD, ageing, reconciliation, interest income) aligns with LMS behaviour without manual adjustments.

---