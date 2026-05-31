# Foreclosure and lien removal request validation

: Ranjan kumar Singh
Created time: September 6, 2024 12:01 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

# **How do we measure success?**

- Number of excess cases/issues for TATA should reduce
    - Note: Excess payment issue does not occur for **Bajaj**, as they manage excess amounts on their end. In cases of excess, the **BFL operations team** manually initiates the withdrawal request.
- Number of lien removal issues should reduce
- Success rate for foreclosure should increase

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

We should not allow user to raise the foreclosure request if below request status are in non terminal state.

Withdrawal request:

- INITIATED
- REQUESTED
- APPROVED
- QUEUED
- PENDING_CREDIT_APPROVAL [Not included in validation]

Repayment request: 

- PENDING_SETTLEMENT
- COLLECTION_COMPLETE
- SUCCESS_WITH_LENDER_RECON_FAILED

Remove pledge:

- REQUESTED
- QUEUED
- PENDING_LENDING_APPROVAL

We should not allow user to raise the un-lien request if below request status are in non terminal state.

Remove pledge [Already exist]

- REQUESTED
- QUEUED
- PENDING_LENDING_APPROVAL

Withdrawal request [Deprioritised]

- REQUESTED
- QUEUED
- PENDING_CREDIT_APPROVAL

---

## User stories / User flow

1. Why we need to block foreclosure request when user has raised the repayment request and in non terminal state
    
    Scenario: Inaccurate Net Payable Amount in Foreclosure Request
    
    When a user attempts to foreclose a loan while the repayment status is still in a non-terminal phase, there is a risk that the net payable amount shown may not be accurate. This is because the system might not account for all pending or partial repayments. If the repayment is completed after the foreclosure request has already been initiated, one of two outcomes may occur:
    
    **Excess Payment:** The user may end up paying more than the required foreclosure amount due to discrepancies between the repayment completion and the system’s foreclosure calculation.
    
    **Request Rejection:** The foreclosure request could be rejected if the system identifies inconsistencies, particularly if the repayment status changes to completed after the foreclosure request is initiated.
    
2. Why we need to block foreclosure request when user has raised the withdrawal request and in non terminal state.
    
    Scenario: Rejection of Foreclosure Request
    
    When a user attempts to foreclose a loan while the withdrawal status is still in a non-terminal phase, there is a risk that the net payable amount shown may not be accurate or foreclosure request gets rejected due to mismatch in outstanding amount[POS]. 
    
3. Why we need to block foreclosure request when user has raised the lien removal request and in non terminal state.
    
    Scenario: Rejection of foreclosure or lien removal request
    
    When a user attempts to foreclose a loan while the lien removal request status is still in a non-terminal phase, one more request will be created to remove lien as lien removal request also gets created to release all funds when user request foreclosure.
    

Note: If user has already placed the foreclosure request we do not allow user to place un-lien request and this is already handled.

## Requirements

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=11414-19686&t=PzjeKpuwIOZcnC1x-4](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=11414-19686&t=PzjeKpuwIOZcnC1x-4)

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

- Un-lien request are getting rejected when user place un-lien request post user has placed withdrawal (when in progress) and POS has become equal to DP. [We are not solving for this because this is user driven action and if user raise the request one of either withdrawal of lien removal request will be rejected from lender end]