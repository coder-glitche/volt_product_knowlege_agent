# Term Loan: Manual Repayments(VA)

# **What problem are we solving?**

Customers rely on LSP app or automated mandate flows for repayments. However, some customers may want to make repayments directly to DSP (e.g., via bank transfer). There is no simple mechanism for customers to pay directly outside the LSP ecosystem.

Without a Virtual Account (VA) option:

- Customers lack flexibility in repayment methods.
- Ops team faces reconciliation challenges for direct transfers.

---

# **How do we measure success?**

- Number and % of VA repayments
- Number and % of successful transactions made through VA
- TAT of settlement of transaction made through VA

---

# **How are others solving this problem?**

- **Banks/NBFCs**: Provide static or dynamic virtual accounts for repayments, mapped per customer or per loan.
- **Fintechs**: Share UPI IDs/VA numbers in loan onboarding or reminder communications, allow repayment anytime.
- **Industry Standard**: Excess repayments are usually either refunded or adjusted towards principal with tenure/EMI adjustment. Some lenders offer customer choice; others default to tenure reduction.

---

# **What is the solution?**

Enable repayments via static Virtual Accounts (VA) mapped per customer. Customers can transfer funds directly to DSP, and the repayment will be posted in the Loan Management System (LMS) with appropriate apportionment, re-amortisation, or foreclosure handling.

---

## **Requirements Overview**

- Provide each customer a static VA for direct repayments.
- Support repayments of any amount (paise precision).
- Handle repayments as **loan-level repayments**.
- Automate apportionment → dues first, then excess to re-amortisation/foreclosure.
- Allow re-amortisation choice (Tenure reduction / EMI reduction).
- Support STP and non-STP flows.
- Implement business-hour rules for posting.

---

## **User Stories / User Flow**

### User Stories

1. As a customer, I want to receive a static VA number so I can repay directly to DSP anytime.
2. As a customer, I want my repayment to be adjusted against dues automatically so I don’t have to track tranche-level obligations.
3. As a customer, if I pay excess, I want to choose how my loan is re-amortised (tenure reduction or EMI reduction).
4. As an ops team member, I want to approve and reconcile high-value or exceptional cases (non-STP flows).

### Requirement Flow

1. **VA Sharing:** VA number provided at account opening mail and in due reminders.
2. **Payment Initiation(Same as OD):** Customer transfers money to VA by logging into their either their registered bank account or any of their other bank account. Customer adds the VA account number and pays any amount to DSP.
3. **Payment Handling(Same as OD):** Once the customer makes a VA payment it will reflect into our Yes Bank account with the status of Pending validation on the Yes bank console. Based on the STP/nSTP checks the payment will either go through STP or nSTP flow.  

| **Checks** | **Flow** |
| --- | --- |
| If Repayment amount is greater than 20 Lacs | nSTP flow |
| If more than 2 VA repayments within the same day | nSTP flow |
| If the payment was done through a bank account different from the registered bank account of the user | nSTP flow |
|  |  |
1. **Ops Intervention(Same as OD):** If the payment goes through the nSTP flow then a checker task is created on Command Center which is then approved by the Ops team if the details match. In case of Ops approval the payment status will get changed to credited on the Yes bank console and will be considered for LMS posting. In case of Ops rejection the payment is automatically refunded back to the customer. 
2. **LMS Posting:** Once the VA payment goes through either the STP flow or is approved during the nSTP flow then we will perform the below validations before posting the payment.

| **Validations**  | **OD Product** |
| --- | --- |
| Loan account Exist | Same as OD |
| VA number should be linked to the Loan Account | Same as OD |
| The UTR number should not be duplicate | Same as OD |
|  |  |

In case any of the above validations fail we send a response to Yes bank and it refunds the amount to the customer. If all the validations pass then we will post the payment to finflux and loan level apportionment will happen.

1. **Business Hour Rules(Same as OD):**
    - If payment received between 12 AM–6 PM we will post it on the same day.
    - If payment received between 6 PM–12 AM we will post it on the next day.
2. **Apportionment & Excess Handling:**
    - The amount will be apportioned by Finflux towards clearing all the pending dues based on the Apportionment logic.
    - Post the clearing of the dues the excess amount will be held in Loan Level excess.
    - If the account is not in shortfall then the Loan Level excess needs to be refunded to the customer by EOD.
    - If account is in Shortfall i.e. DP-POS < 0 then refer to the Excess handling prd for detailed solutioning.
3. Based on the posting and apportionment the schedule of Tranche/s will get updated.
4. **Update to LSP:** Repayment confirmation sent to LSP via a webhook.

---