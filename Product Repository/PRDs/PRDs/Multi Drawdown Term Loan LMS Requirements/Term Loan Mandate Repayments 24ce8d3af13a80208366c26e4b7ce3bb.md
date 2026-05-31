# Term Loan: Mandate Repayments

# **What problem are we solving?**

- **Collections Reliability:**
    
    In Term Loans, fixed EMI dates require timely collections. Manual payments or ad-hoc transfers are prone to delays, user forgetfulness, and operational leakage.
    
- **Operational Efficiency:**
    
    Manual chasing of repayments increases Ops load, costs, and NPA risk.
    
- **Customer Experience:**
    
    Users don’t want to remember EMI dates or perform repetitive actions each month. Mandates automate this and prevent missed-payment penalties.
    
- **Regulatory Alignment:**
    
    NPCI/NACH mandates ensure collections happen through regulated, auditable channels with user consent and charge limits.
    

**Without mandates:**

- High bounce rates due to late or missed payments.
- Increased DPD (Days Past Due) bucket migration.
- Higher operational overhead to recover overdue amounts.

---

# **How do we measure success?**

- **Collection Efficiency Ratio (CER)**: % of total EMI value successfully collected through mandate vs billed amount.
- **Bounce Rate Reduction**: Drop in first-presentation bounce % compared to pre-mandate collections.
- **Manual Recovery Effort**: Reduction in Ops calls / follow-ups per loan account per month.

---

# **How are others solving this problem?**

| Player Type | Approach | Notes |
| --- | --- | --- |
| **Banks & NBFCs** | eNACH / UPI AutoPay mandates at loan booking. Present on EMI date. Retry if bounced. | Most large lenders use NACH for high-value EMIs (> ₹15k) and UPI mandates for smaller EMIs. |
| **Fintech Lenders** | Mandates via UPI AutoPay (fast, digital consent), fallback to eNACH. Present EMI amount + overdue in single debit. | Some split EMI into multiple smaller debits to reduce bounce chance. |
| **Aggregators (Razorpay, PayU, BillDesk)** | Offer APIs to set up & present mandates on behalf of lenders. Provide dashboards for tracking status & bounces. | Reduce tech overhead for lenders. |

---

# **What is the solution?**

## Requirements

### **Mandate Setup**

- Mandate will be set at the **Loan level**. There will only be a single active mandate at the Loan level in V0.

### Pre-emptive File

- There will be multiple due dates(ranging from 2nd to 7th of the Month) across customers(one customer will have one Due Date ) and the billing will also happen on the same day as the due date hence we need to prepare an internal consolidated batch file for all the due dates in order for Ops to review and approve.
- We need to generate a mandate file internally on the 1st of each month in order for the Ops team to validate and approve the file before the mandate presentations.
- This mandate file will contain all the mandates, which will be presented from 2nd to the 7th of the month.
- In the mandate file, we will have each line item at the loan level. These loan level details will include the details of all the tranches of the loan which are to be debited through the specific mandate.
- The mandate file format will be based on the file attached. [https://docs.google.com/spreadsheets/d/1nL0cPBBA6bmXZUEXYbSgS1g973Q7k4Lhv2a71JzF7fM/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1nL0cPBBA6bmXZUEXYbSgS1g973Q7k4Lhv2a71JzF7fM/edit?usp=sharing)
- The loan level dues will include the consolidated dues i.e. summation of dues from each tranche of the loan post the tranche tagged excess is adjusted from the tranche dues.
- Once Ops verifies all the details of the mandate file they will be approving the file on the same day.
- Any discrepancies related to any loan/mandate will lead to exclusion of those mandates from presentation until re-verified.

### **Billing Process**

- On the **bill date**, Finflux will generate the bill for all users with the same due date.
- Billing will happen **daily from 2nd to 7th of the month** as different users will have different due dates.
- Once billing is completed for a given day, the dues will get updated by Finflux for each Tranche.

### **Mandate Presentation**

For each user/mandate, the presentation amount will include all **overdue** and **due EMIs** across tranches.

**In case of CRED**:

- We will be providing CRED with a Presentation Value API using which they will be able to pull the latest dues for the user’s loan.
- Each loan level detail will have the consolidated Tranche level dues.
- The API will have the following mandatory parameter in the request body:
- **loanAccountId**
- The API response will have the following mandatory parameters:
- **monthlyMandateCollectionBatchItemId**
- **loanAccountId**
- **amount**: Total dues for the loan
- **umrn
- bankAccountNumber
- bankAccountIfsc**
- We also need to provide Tranche wise dues breakup to CRED. This will be passed in the same Presentation Value EMI. 
Tranche level parameters:
**1. TrancheID
2. Due Date
3. Principal Due
4. Interest Due
5. Excess**
- ***Note: Manual payments** won’t be allowed from Cred’s end when the mandate presentation is in progress.*
- If the presentation amount is less than Rs 10 then we won’t waive it off.

### **Post-Presentation Update**

- We need to build a Loan Level Mandate Posting API for Term Loan.
- This API will have the following body and parameters:

```
 "**monthlyMandateCollectionBatchItemId**": "MBITEM6424799296",
 "**fenixLoanAccountId**": "FXLAN48812556",
 "**umrn**": "UMRN1689762597832364",
 "**mandatePresentationDetails**": [
   {
     "**amount**": 1925.7,
     "**presentationInitiatedOn**": "2025-05-18T18:48:15",
     "**presentationCompletedOn**": "2025-05-18T18:49:15",
     "**remarks**": "remarks_196115d3e939abc",
     "**utrNumber**": "utrNumber_0d23eb4ba8070d9",
     "**mandateTransactionStatus**": "SUCCESS",
     "**externalId**":"190520250519812"
   }
 ],
 "isCollectionSkipped": false
}'
```

- Cred can choose to split the dues in order to collect through presentation of multiple mandates. In the above posting API each presentation will be passed in separate objects.
- We will be doing the below validations before proceeding with the repayment posting:

| **Validations** |  |
| --- | --- |
| Loan account exists and is not closed  | Required  |
| Tranche account exists and is not closed  | Required  |
| Non Terminal collection request(Mandate, Manual, Foreclosure, Sell off, shortfall) should not be present for any Tranche and Loan | Required |
- Once we receive the presentation details in the response and based on the validations we will post it at the loan level and accordingly Finflux will apportion based on the defined apportionment logic.
- Multiple UTRs can be posted against one batchitemid mandate collection.
- If Loan account does not exist or is closed: Since this case is currently not handled in OD as well, we will take it later.
- If any of the Tranche does not exist or is closed: then amount collected for the specific tranche will be transferred to the Loan excess and later will be refunded(based on excess refund logic) if there are no pending dues.
- In case there is a pending Non terminal collection request we will accept the mandate collection request. The processing will happen based on the separate workflows. Whichever process gets completed first the apportionment will happen accordingly. Post the completion of both the workflows whatever excess remains will either be parked at the Tranche level or at the Loan level given the scenario.
- In case a Tranche or the Loan is frozen then we will accept the mandate collection payment and Finflux will do the apportioning based on the apportionment logic.

---

# Settlement Reconciliation

This needs to be solutioned. As Cred/digio will settle to us in a single bulk payment so we will need all the UTRs corresponding to which the payment was received. Its a hard/necessary requirement.

# **Design**

---

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes