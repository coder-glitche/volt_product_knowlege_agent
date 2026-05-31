# Charges only handling for collection - DSP

: Ranjan kumar Singh
Created time: June 3, 2025 10:21 AM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

### Current Billing Logic:

For each billing cycle, the billing amount includes:

- Outstanding interest
- Outstanding charges

Once data is synced from the lender, Volt creates a billing record based on the following logic:

- **TCL Customers:**
    - A billing record is created if:
        - Interest amount ≥ ₹1 **OR**
        - Charges amount ≥ ₹1 **OR**
        - Interest + Charges ≥ ₹1
- **DSP Customers:**
    - A billing record is created if:
        - Interest amount ≥ ₹10 **OR**
        - Interest + Charges ≥ ₹10

### Gap at Volt End:

For **DSP customers**, if only charges are due and:

- Interest amount is **not due** and
- Charges amount is ≥ **₹10**,

then **no billing record is created**, but DSP hit the mandate to collect the charges and apply bounce charges if failed to collect and applies penal of RS 10 un till the overdue amount is recovered. Since we are not communicating about to charges due to our customer, we are getting escalation when mandate was presented or bounce charges was applied without informing the customer.

### Gap at **DSP's End**

DSP includes charges posted **after billing generation** (e.g., between 1st and 6th of the month) in the **mandate presentation**. These charges are not reflected in Volt’s billing records or communicated to the user, leading to further confusion.

### 🔄 Breakdown via Scenarios:

**Scenario 1: Charges Only, No Communication**

- Billing generated on 1st = ₹0
- DSP applies charges of ₹999 on 6th
- Volt does **not** update the billing record or send communication
- DSP presents a mandate for ₹999
- User is **unaware** of this amount and may raise a complaint

**Scenario 2: Partial Billing, Mismatched Communication**

- Billing generated on 1st = ₹1,000
- DSP applies charges of ₹999 on 6th
- Volt UI to show ₹1,000
- DSP presents a mandate for ₹1,999
- User receives a partial communication and is **surprised** by the increased deduction

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

**Requirement for Volt:**

1. Volt to start creating the billing records for below scenario.
    1. When interest is 0 and charges due are ≥10
    2. When interest + charges due are ≥10
2. Volt to sync billing details on daily basis to update the status and billing amount 
    1. Sync Interest amount and update the interest due and total due
    2. Sync Charges amount due and update the charges due and total due
    3. After syncing when Status is ‘DUE’ and Interest due + charges due becomes <10 then mark the record as settled.
    4. Do not apply rounding logic on the Charges due amount
    
    <aside>
    💡
    
    Charges due = chargesDue + penalChargesDue
    
    </aside>
    
    ```json
    {
    "fenixLoanAccountId": "FXLAN52644985",
    "clientId": "FXCID25992222",
    "fenixOpportunityId": "OPP8657979449",
    "productType": "LOAN_AGAINST_SECURITIES",
    "sanctionAmount": 20000000,
    "totalDrawingPower": 149025.25,
    "availableAmountForDisbursement": 149846.43,
    "principalOutstandingAmount": 0,
    "excessAmount": 821.18,
    "chargesDue": 0,
    "interestDue": 0,
    "penalChargesDue": 0,
    "accruingInterest": 0,
    "portfolioDrawingPower": 0,
    "regulatoryDrawingPower": 0,
    "coolingOffPeriodInDays": null,
    "loanStatus": "FROZEN",
    "originalStartDate": 1741323102620,
    "currentTermStartDate": 1741323102620,
    "currentTermEndDate": 1838073600000,
    "closedOnDate": null,
    "tenureInDays": 1119,
    "renewalDueDate": 1837468800000,
    "interestRate": 10.49,
    "totalOutstandingAmount": 0,
    "loanInterestDetails": null
    }
    ```
    

1. Volt to support populating charges amount also when billing record is created through sheet upload for all the lenders.

**Requirement for DSP:**

- DSP not to include charges in mandate presentation of last billing cycle which are applied b/w the 1st to 7th.
- Till the time this changes is implemented at the DSP end, Volt will continue to sync the charges applied after 1st and include in billing amount.

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=10421-40735&t=iGSDUXfd4AezRbqV-0](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=10421-40735&t=iGSDUXfd4AezRbqV-0)

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