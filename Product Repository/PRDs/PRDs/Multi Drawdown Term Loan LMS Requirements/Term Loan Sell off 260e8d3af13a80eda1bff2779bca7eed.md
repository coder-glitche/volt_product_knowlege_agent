# Term Loan: Sell off

# **What Problem Are We Solving?**

- When customers miss repayment obligations / goes into shortfall / goes into high risk category, the lender faces credit risk exposure and delayed recovery of dues.
- Without a transparent process, collateral liquidation may lead to:
    - Operational inefficiencies.
    - Customer disputes regarding how proceeds are applied.
    - Regulatory compliance gaps.
- There is a need for a standardized, rule-based collateral sell-off mechanism to ensure timely recovery and clear apportionment of proceeds

---

# **How Do We Measure Success?**

**Business Metrics:**

- % of overdue cases successfully resolved via collateral liquidation.
- Reduction in overdue loan book.
- Recovery turnaround time(from default to sell-off settlement).

**Customer Metrics:**

- Reduction in customer disputes/complaints regarding recoveries.
- Transparent communication of units sold, amount realized, and dues cleared.

**Operational/Compliance Metrics:**

- Zero reconciliation mismatches in proceeds apportionment.
- 100% adherence to RBI regulatory guidelines on pledged security liquidation.

---

# **How Are Others Solving This Problem?**

**Banks & NBFCs (India):**

- Trigger sell-off after multiple mandate bounces.
- Proceeds are typically applied first to overdue interest/principal, then to charges.
- Excess, if any, is either adjusted to future EMIs or refunded.
- Process is often manual or semi-automated, with limited transparency to customers.

**Fintech Lenders:**

- Use automated sell-off workflows integrated with AMC redemption systems.
- Provide real-time updates via app/email/SMS.
- Offer transparent breakups of collateral sold, NAV applied, and dues cleared.
- Some adopt a "just-enough liquidation" approach instead of liquidating larger buffers.

---

# **What is the solution?**

## Requirements

## **Use Cases / Triggers**

Ops or Client should be able to initiate collateral sell-off request in below cases:

- Client defaults on **EMI (Principal + Interest)** repayment.
- Client fails to repay **shortfall amount**.
- Loan tenure ends (loan expired) and **TOS (Total Outstanding)** remains unpaid.
- **Loan Recall**: Client falls in to the high risk category for any of the following reasons: PEP, AML, etc.
- Client voluntarily asks for Collateral sell off to recover the amount for any of the above use cases.

---

## **Sell-off Dates**

- **EMI Default:** 21st of the month
- **Shortfall:** When Aging = 7
- **Loan Expiry:** Month-end after maturity.
- **Loan Recall:** 3 Days from the intimation
- **Voluntary/Customer Request:** Adhoc

---

## **Collateral Value for Sell-off**

- **EMI Overdue**: In this case the **Recoverable Amount** is: **Due EMIs + Due Charges**. Sell off will be triggered for a **Collateral Value** of: **Recoverable amount + 5%(for buffer)**.
- **Shortfall**(Same as OD): Sell off will be triggered for a **Collateral Value** of: **[Shortfall Amount / (1-LTV)].**
- **Loan Recall**(Same as OD)**:** Sell off will be triggered for a **Collateral Value** of: **Total Outstanding + 5%(for buffer)**

---

## Sell-off Scenarios

- Sell-off of collateral will be done at a Loan level. No tranche level sell-off will happen.
- For Overdues on single/multiple tranche/s the sell-off will be done for the combined Dues.
- In case Overdue and Shortfall sell-off needs to happen on the same day then the Sell-off value will be based on the combination of the dues and shortfall amount. Here shortfall amount will be less given Principal will be included in the Dues. The formula/logic for the Sell-off amount calculation will be shared later once finalized by business.
- The apportionment will happen based on the specified apportionment logic.

## **Process Flow**

### **Ops Initiated or Client Requested Sell off(Same as OD)**

1. Client requests sell-off for any of the above mentioned cases.
2. OPs selects funds to sell off
3. Maker(Ops) uploads the sell off file through CC along with the reason for sell off.
4. Validation of funds, provided in the uploaded sell off file, at Fenix end.
5. Fenix calls the Collateral Block API and Finflux blocks funds.
6. Checker task created in Command Center for Ops approval.
7. Ops approves request post verifying if the necessary funds are blocked.
8. Fenix sends Lien removal and sell-off request to RTA.
9. RTA processes the request and remits funds to DSP bank account.
10. Ops posts repayment txn after mapping the proceeds with the loan account.
11. Finflux apportions the payment based on the specified apportionment logic and updates SOA:
    - EMI Overdue/Shortfall, etc. cleared.
    - Excess (if any) gets posted on the loan level.
12. Unlodgement checker request is created. Ops verifies and approves.
13. Finflux unblocks and removes Collateral from the Loan.
14. Request closed.

### **Checker Rejection**

- Checker can reject complete request or individual funds for sell-off.
- Approved funds will be sent for sell-off.
- Rejected funds will be unlocked.

---

## **Sell-off Rejection / Failure**

- **OPs Rejection:** Sell off request can be rejected by DSP Ops with a reason, subject to maker-checker.
- **RTA rejection:** Auto-unblocking of the collaterals
- **AMC rejection:** Funds will remain blocked.

---

## **Excess Handling**

- Ops posts repayment manually after mapping the proceeds and UTRs to the loan account through file upload on CC.
- Finflux apportions the amounts based on the specified apportionment logic.
- **Excess flow:**
    - Any excess amount will be posted as loan excess.
    - This excess will remain parked at the loan level. It will be handled in the same manner as specified in the Excess handling prd.
    - Excess amount will be refunded in user’s bank account with approval flow in case of loan expiry, loan recall.
    - Once refund is completed, post refund transaction on SOA.

---

## **Charges**

- Sell off charges won’t be charged for CRED.

---

## **Loan Attribute Updates (Post Blocking)**

- Total Drawing Power
- Available Amount For Disbursement
- Outstanding Principal
- Next EMI due
- Repayment Schedule

---

## **APIs**

### For LSP

- Request sell-off(with reason as a parameter) with request status

### For Command Center(Same as OD)

- Initiate sell-off (Ops trigger).
- Post charges.
- Initiate refund.

---

## **Validations**

- Selected collateral should be lodged.
- RTA sell-off confirmation mandatory before removing collateral from loan.
- DP of the funds requested for sell-off to be blocked.
- Funds requested for sell-off should be "blocked for unpledging" to avoid both sell-off and unpledging of the funds simultaneously
- Funds requested for sell-off should be "blocked for sell-off" to avoid double sell-off
- Rejected funds to be made available for sell-off.
- Rejected funds to be made available for unpledging
- Sell-off of unlodged funds should not be allowed

---

## **Reconciliation(To be closed)**

- Ops sees all collateral sell-off txns linked to EMI buckets.
- Ops reconciles against RTA reports (upload feature in Command Center).

---

## **Command Center UI(Will be detailed out in CC prd)**

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

##