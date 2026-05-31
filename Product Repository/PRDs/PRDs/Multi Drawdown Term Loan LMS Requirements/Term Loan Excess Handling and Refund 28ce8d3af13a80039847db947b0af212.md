# Term Loan: Excess Handling and Refund

## **What problem are we solving?**

Currently, all repayments (via VA or PG) can result in excess funds being received from the borrower due to multiple reasons such as pre payments, duplicate transactions, or rounding differences.

Without a clear and automated excess handling logic, this can lead to:

- Incorrect allocation of payments across tranches or dues.
- Customer confusion and complaints regarding refund timelines.
- Operational inefficiencies due to manual intervention in refund processing.
- Incorrect accounting treatment if prepayment or refund rules are not consistently applied.

We aim to design a standardized and automated excess handling and refund mechanism that operates distinctly for loan-level and tranche-level payments, ensuring compliance with loan agreements and operational SOPs.

---

## **How do we measure success?**

1. **Operational Efficiency**
    - Majority of excess cases auto-refunded at EOD without manual intervention.
    - Low exceptions requiring manual refund intervention.
2. **Customer Experience**
    - Customer complaints regarding refund delays or incorrect allocation.
    - Transparent communication of prepayment/excess treatment in the SOA.
3. **Compliance & Finance Accuracy**
    - 100% adherence to refund timelines as per SOP.
    - No accounting mismatches between excess ledgers and refund transactions.
    - Accurate recognition of prepayment benefit(for tranche-level payments) post go-live of benefit feature.

---

## **How are others solving this problem?**

**Banks:**

- In case of excess repayment, banks typically reamortize the loan schedule to adjust future EMIs or park the excess amount in the borrower’s savings account.
- When parked in a savings account, interest is provided on the excess balance as per the prevailing savings rate.
- This ensures the excess remains liquid for the borrower while maintaining interest accrual consistency for the lender.

**NBFCs:**

- Most NBFCs restrict customers from paying more than one advance EMI.
- These excess amounts are held without any interest benefit to the customer.
- Only a few NBFCs offer reamortization options where the loan schedule is recalculated based on the prepayment, though this is generally operationally intensive and used selectively.

**Our Approach:**

- We adopt a hybrid structure that balances operational simplicity with customer transparency:
    - For loan-level payments, excess will be refunded automatically at EOD, ensuring no ambiguity or holding period.
    - For tranche-level payments, excess will be retained and used to compute prepayment benefit at the tranche ROI, implemented post–go-live.

---

## **What is the solution?**

### **Payment Types**

There will be two distinct types of repayments:

- **Loan-level payments** – through Virtual Account (VA) / Mandate / Shortfall / Sell-off collections.
- **Tranche-level payments** – through Payment Gateway (PG) transactions, where the customer selects a specific tranche.

---

### **Loan-Level Payments (**VA / Mandate / Shortfall / Sell-off**)**

**a. Collection & Apportionment Logic**

- All these payments are received at the loan level.
- Payments shall be apportioned using the following sequence(Charge and Penalty not part of V0 for Cred):
    1. Interest overdue
    2. Principal overdue
    3. Interest due
    4. Principal due
    5. Charges Overdue
    6. Charges due
    7. Excess (loan level)
- Oldest EMI shall be paid first (FIFO logic for multiple EMIs ageing the same), handled at Finflux’s end.

**b. Excess Handling**

- Any excess balance created after apportionment will be parked in the Loan level excess without any tranche tagging and shall be refunded to the borrower at EOD as per SOP.
- The loan agreement provides up to 7 days for refunding excess amounts, but SOP mandates same-day refund(EOD of every working day).

**c. Shortfall Cases**

When **DP – POS < 0**, the system shall treat the shortfall as covered by existing excess funds (loan or tranche-tagged). Refunds will be processed only for any remaining loan level excess beyond shortfall coverage. Below are the various excess scenarios for shortfall coverage along with their handling and refund:

1. **Only Tranche-Tagged Loan-Level Excess**
    - This excess is currently covering for account shortfall.
    - During next billing, this tagged excess will be used to settle tranche dues.
    - Once dues are settled and there is either no excess which remains or the remaining excess is not able to cover for the shortfall i.e. if **DP – POS + Excess remains negative**, the account will **continue to show shortfall**.
    - **No refund** will be triggered in this scenario.
2. **Both Loan-Level Excess and Tranche-tagged Loan-Level Excess**
    - Both collectively cover for the account shortfall. If there is any additional unutilized excess beyond what’s needed to cover the shortfall, that amount shall be refunded at EOD from the Loan level excess and not from Tranche tagged loan level excess.
    - During next billing, tranche dues will be settled using tranche-tagged excess.
    - Any dues(across tranches or on loan) which remains will be settled using the Loan level excess
    - Post this if there is either no excess which remains or the remaining excess is not able to cover for the shortfall i.e. if **DP – POS + Excess remains negative**, the account will **continue to show shortfall**.
3. **Only Loan-Level Excess (No Tranche Tagging)**
    - Loan-level excess shall be utilized to cover any pending dues first. Post which if the account is in Shortfall then the excess will be parked/held in order to cover for the shortfall.
    - If there is any unutilized Loan-level excess beyond what’s needed to cover the shortfall, that amount shall be refunded at EOD.
    - When next billing happens and there are dues which are generated then the Loan level excess, maintained for covering shortfall, will be used to settle the dues.
    - Post the dues settlement, if there is either no excess which remains or the remaining excess is not able to cover for the shortfall i.e. if **DP – POS + Excess remains negative**, the account will **continue to show shortfall**.
- No prepayment or interest benefit shall be provided for any excess amount held as margin for Shortfall cases.

---

### **Tranche-Level Payments (PG & Pre Payments)**

**a. Collection & Customer Flow**

- PG repayments shall be made at the tranche level, with the customer selecting the tranche for which payment is being made.
- Customer shall be allowed to select any tranche, irrespective of the due/overdue status of other tranches.
- As a best practice, LSPs will be instructed to display overdue/due tranches first to improve collections and reduce sell-off risk.
- In case the customer pre-pays an amount upto a maximum of one EMI(assuming all dues are cleared for the Tranche) then the prepaid amount will be parked in the tranche tagged loan level excess. When billing happens then this Tranche tagged loan level excess will be used to settle the EMI.
- In case customer pays an amount more than one upcoming EMI then we won’t reject the payment. We will park the entire amount in Tranche tagged Loan level excess.

**b. Apportionment Logic**

- For each tranche(Charge and Penalty not part of V0 for Cred):
    1. Interest overdue
    2. Principal overdue
    3. Interest due
    4. Principal due
    5. Charges Overdue
    6. Charges due
    7. Excess (tranche tagged loan level excess)
- Oldest EMI shall be paid first.

**c. Excess Handling**

- Excess created at the tranche level shall not be refunded to the customer.
- The excess will be used to settle the upcoming EMI when it becomes due on the due/billing date. This settlement won’t happen automatically by Finflux, we need to trigger the settlement.

**d. Prepayment Benefit(Not part of V0 and will be detailed out later)**

- Benefit shall be provided at the same rate as the tranche ROI for the excess held at the Tranche level based on the number of days it is held for.
- This feature will require additional development to:
    - Calculate and post interest benefits.
    - Generate corresponding accounting entries.
- **Timeline:**
    - Prepayment benefit feature completion: By 31 Dec 2025

---