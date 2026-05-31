# Term Loan: Prepayments and Excess Handling

# **What Problem Are We Solving?**

- Customers need to be provided with an option to pay their EMIs as and when they want in order to avoid higher delinquencies and bad customer experience.
- Customers needs a structured way to prepay specific tranches/EMIs in their term loans.
- This creates customer dissatisfaction, potential regulatory risk, and inefficient fund management for the lender.
- Without proper foreclosure/prepayment support, customers may:
    - Face higher effective interest costs.
    - Avoid early repayment, reducing lender’s portfolio efficiency.

**Problem Statement:**

We need to design a clear, transparent, and compliant prepayment mechanism for term loan that allows customers to target tranche-level prepayment.

---

# **How Do We Measure Success?**

**Customer Success Metrics (External):**

- % of customers opting for prepayment functionality within 3 months of launch.
- Reduction in customer complaints/queries related to payments.

**Business Success Metrics (Internal):**

- Increase in early repayments → lower credit risk exposure
- Improved customer retention
- Reduction in manual intervention by Ops team for handling excess payments.

---

# **How Are Others Solving This Problem?**

**Banks & NBFCs (Market Practice):**

- **Prepayments:** Customers can prepay part of a loan by specifying EMI/tranche.
- **Excess Handling:**
    - Some lenders keep excess as "advance EMI" without providing interest benefit.
    - Progressive lenders credit savings account-linked interest or apply loan ROI on excess balances.
- **Benefit Calculation:**
    - Conservative approach → No interest benefit credited on excess.
    - Customer-centric approach → Credit benefit at IBLR / weighted ROI.

**Benchmark Examples:**

- **HDFC Bank / ICICI Bank:** Excess usually adjusted against upcoming EMI; limited/no interest benefit.
- **Fintech NBFCs:** More flexibility — offer ROI-based daily interest benefit on wallet/excess balances.
- **Global Lending (e.g., US/UK):** Overpayments usually reduce principal immediately; customer saves interest automatically (transparent).

---

# **What is the solution?**

## Requirements

### ~~Prepayment Prerequisites~~

- ~~Customers will only be able to initiate prepayment for a particular Tranche if there are no dues on any of the Tranche/s.~~
- ~~They will only be allowed to prepay an amount less than equal to single EMI of a Tranche i.e. the upcoming EMI.~~

---

### Prepayment Initiation

- Customers will be able to initiate prepayment through the LSP app.
- Customer will select the **tranche/EMI** they wish to prepay.
- Once the customer initiates the payment, the transaction flow and handling will be in the same manner as for Manual PG repayments.

---

### Validations and checks

- Once DSP receives a successful payment confirmation from Cred’s PG we will perform the below validations before proceeding with the payment processing:

| **Validations** | **Tranche** |
| --- | --- |
| Loan account exists and is not closed  | Required  |
| Tranche account exists and is not closed  | Required  |
| Loan/Tranche account is not frozen | Required  |
| If dues exist on the same Tranche then the prepayment shouldn’t go ahead | Required  |
| If no dues exist for a Tranche(against which prepayment is done) but it exists for other Tranches then the prepayment shouldn’t be allowed  | Required  |
| The UTR number provided by the LSP should be unique if its not unique then the payment should move to the nSTP flow | Required  |
| No foreclosure request should be in progress/non-terminal state for same Tranche and Loan  | Required |
| Non Terminal collection request(Mandate, Sell-off, shortfall, PG, Prepayment, etc.) should not be present for same Tranche and Loan | Required |
| If an excess tagged to the tranche is already present which is equal to or greater than the EMI amount then prepayment should not be allowed. | Required |
- If any of the above check’s fail then we reject the payment and accordingly send the response to the LSP.
- If all the above checks pass then DSP will park the amount received in Loan level excess with a Tranche level tagging(Will be provided by Finflux).

### Handling Excess Payment(Tranche Level)

- Any excess from the prepayment shall be **apportioned to the corresponding tranche**.
- Excess shall be maintained at the loan ****level with the tranche level tagging until the end of the billing cycle.
- If not utilized for prepayment, excess shall be maintained at the **loan level** for future dues.

---

### End-of-Billing Cycle Processing

At the time of posting dues, the following process shall be followed:

1. **Prepayment Benefit(Tranche Level)**
    - No interest benefit will be provided(subject to change).
2. **Posting of Dues**
    - Interest and principal dues shall be created.
    - Dues shall first be collected from the tranche-level excess tagged at the loan level.
    - Any remaining dues shall be collected from loan-level excess(not tagged to any tranche) as per apportionment logic.
3. **Treatment of Charges**
    - Any charges posted during the day shall be adjusted from excess before calculating EOD excess balance.

---

### Loan-Level Excess Handling

If excess remains at the loan level:

- No Interest benefit(subject to change) shall be provided to the customer for maintaining excess towards future dues.
- Any Tranche dues not getting settled from the Tranche level excess(tagged on loan level) will be adjusted from the Loan level excess.
- Any charges due on the loan will be adjusted from the Loan level excess, before the mandate presentation.
- If all tranches are closed and no dues/outstanding present on the loan then the Loan level excess will be refunded to the customer’s bank account.

---

## Open Pointers

- Ask Finflux to provide an API wherein we pass a line id and they give us the repayment schedule for all the tranches on that line. This is to ensure that we don’t have to call multiple APIs to get schedule for each tranche because sometime it might happen that one of the apis fail. Stretchy report api
- How is cred going to do validations/or we will do validations and share the eligibility api with cred(extra efforts but preferrable way)
- Each tranche level excess: API required from Finflux give requirement
This API Finflux will provide but it's still in dev. API contract not finalized yet
- Any Tranche dues not getting settled from the Tranche level excess(tagged on loan level) will be adjusted from the Loan level excess. Have we aligned this with M2P? Check with Vaibhav
Ans: This is aligned with M2P
- Check with CRED if they will allow repayments across multiple tranches because then we might be doing wrong validations

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

---

#