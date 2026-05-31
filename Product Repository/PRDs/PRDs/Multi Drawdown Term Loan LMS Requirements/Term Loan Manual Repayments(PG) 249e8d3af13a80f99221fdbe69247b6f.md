# Term Loan: Manual Repayments(PG)

# **What problem are we solving?**

For Borrowers:

•	Multiple payment options: Cards, UPI, netbanking, etc.

•	On-demand payments: Can make ad-hoc part-payments, overdue clearance, or foreclosure instantly.

•	Better experience: Real-time confirmation and receipts. 

•	Convenience: Removes friction of doing manual transfers for loan repayment.

For Lenders:

•	Improved collections efficiency: Easier for customers to pay resulting in fewer missed EMIs.

•	Faster settlement: PGs provide quick transaction processing.

•	Reduced operational cost: Less manual reconciliation vs cheque/DD payments.

•	Scalable: Handles high volumes without proportional ops staff increase.

---

# **How do we measure success?**

From a product & business view, metrics split into collection, ops, and customer experience:

Collection/Revenue Metrics

•	% of EMI repayments through PG vs other channels(Mandate & VA)

•	Improvement in on-time repayment rate (DPD 0)

•	Reduction in delinquency rate

•	Volume/value of ad-hoc payments made through PG

Operational Metrics

•	Payment success rate

•	Reduction in manual reconciliation time/errors(Compared to VA & Mandate)

Customer Experience Metrics

•	% of customers doing PG repayments

---

# **How are others solving this problem?**

Banks & NBFCs

•	Direct PG integration on their portals/apps (Netbanking, UPI, card payments).

•	Some use aggregators like Razorpay, Billdesk, PayU for multi-mode collection.

•	EMI payment links sent via SMS/WhatsApp with a PG link.

Fintech Lenders

•	In-app PG flow: Integrated UPI, cards, and wallets directly in the lending app.

•	Automated reminders: Push notifications with PG deep-links for due EMIs.

•	Dynamic amounts: PG request auto-updates based on overdue + charges.

---

# **What is the solution?**

## Requirements

### **Manual Repayment (V0 Scope)**

### Requirement

**Payment Initiation**

- Users will be able to initiate manual payment via the LSP app.
- ~~Users should be able to manually pay the oldest due first.~~
- Users should be allowed to pay towards any Tranche irrespective of their Dues/Overdues.
- Below is an example to illustrate the above pointer:

Example: User has taken 3 Tranches on their Loan. Assuming that Tranche 1 has: one EMI in Overdue, one EMI in Due and one EMI in upcoming. Tranche 2 has one EMI in Due and one EMI in upcoming. Tranche 3 has 2 EMIs in upcoming. User can choose to pay in any of the below ways:
- User can choose Tranche 2 and pay a maximum amount of Due EMI + One Upcoming EMI - Tranche 2 excess 
- User can choose Tranche 1 and pay a maximum amount of Overdue EMI + Due EMI + One Upcoming EMI - Tranche 1 excess
- User can choose Tranche 3 and pay a maximum amount of One Upcoming EMI - Tranche 3 excess

[*CRED currently does not allow users to prepay an EMI of a Tranche if that Tranche has Due/Overdue EMI present. In CRED’s journey, customer should clear the Due/Overdue EMI of the Tranche first then only will they be able to do an upcoming EMI’s payment by initiating a new repayment.*]

**Payment Routing and Validations**

***[LSP PG (CRED using own PA/PG DPSPL)]***

- Customer initiates the manual payment through the LSP app.
- For the payment done by the user the LSP creates an order with their PA/PG passing the LAN of the user.
- The LSP then creates a repayment order using DSP’s Create repayment order API.
- In the Create repayment order API below are the parameters which Cred should pass:
    - Loan ID of the customer
    - Tranche ID for settlement
    - repaymentAmount
    - collectionMode
    - repaymentMethod
    - paymentTimestamp
    - payment reference id
    - externalId
- Once we receive the create repayment order request from Cred, we will use Get Payment Status API of Cred’s PA/PG to poll the status of the transaction.
- Once ‘success’ status is received by DSP for the transaction we will perform certain validations at our end before processing the repayment request. Below are the validations:

| Validations | Tranche |
| --- | --- |
| Loan account exists and is not closed  | Required  |
| Tranche account exists and is not closed  | Required  |
| No foreclosure request should be in progress/non-terminal state for same Tranche or Loan  | Required |
| Non Terminal collection request should not be present for same Tranche | Required |
- If any of the above check’s fail then we reject the repayment and accordingly send the response to the LSP.
- If all the above checks pass then DSP will create a repayment order for the Loan’s Tranche of the customer.
- Based on the below checks we will decide if the repayment should go through the STP or non-STP process. The checks are listed below:

| Checks | Flow |
| --- | --- |
| If the repayment value is greater than 20 Lacs for the Tranche repayment | non-STP |
| If the repayment count for the Tranche is more than 2 for the day  | non-STP |
- If none of the above checks pass and the repayment goes through the STP flow then we post it in our LMS.
- If any of the above checks is true then repayment goes through the non-STP flow wherein a checker process is created for the repayment. Once the Ops team approves the checker process then the repayment is posted in our LMS. If the Ops team rejects in the checker flow then the repayment will be rejected.
- The payment against the tranche is posted and apportionment based on tranche-level logic is done by Finflux.
- Once the balances of the Tranche are updated the SOA posting should happen. If the SOA posting successfully happens, the repayment flow gets completed.
- On successful SOA posting we send the acknowledgement response to the LSP with the updated balances of the Tranche.
- The LSP then updates the same to the customer.

---

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