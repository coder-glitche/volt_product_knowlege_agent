# [LSP] Total outstanding amount correction and overdue details

: Vaibhav Arora
Created time: January 16, 2025 7:43 AM
Status: Not started
Last edited: January 21, 2025 7:32 AM

# **What problem are we solving?**

For a loan account there are certain particulars that are maintained to understand what is the total due that the user has against their loan account. They are described as follows:

- Principal outstanding: This is sum of the amount that the user has withdrawn minus the repaid (as partial principal repayments) to the NBFC
- Interest due - This is the amount that is due for the user from the previous billing cycle, calculated as accruals based on their principal outstanding at a daily level (currently we follow a daily accrual model)
- Charges due - This is the sum of all outstanding charges against the user’s loan account
- Penal charges due - This is the sum of all the penal charges due for the customer
- Accrued interest not due - Interest that is accumulated in the current billing cycle but is not presently due for the user

Currently the total outstanding which is being communicated to the LSPs as well as to the operations team comprises of the following particulars:

- Interest due
- Charges due
- Principal due

This introduces a series of problems:

- LSP will not be able to accurately communicate penal charges and overdue interest applicable to the user which impact core servicing flows like:
    - Revocation: LSPs will not be able to maintain enough margin in terms of available limit and will only consider interest + charges + principal outstanding while retaining funds as limit for the user when they raise a revocation request - This also introduces a collateral risk for the NBFC
    - Foreclosure: LSPs will not be able to accurately communicate the total outstanding amount when the user tries to foreclose their account
- Operations team will not be able to accurately track the total outstanding amount for the user

---

# **How do we measure success?**

- # of revocation requests rejected due to unavailability of limit / Total revocation requests
- # of tickets raised on clarity of TOS by the user to LSP operations team and NBFC operations team

---

# **How are others solving this problem?**

- BFL and TCL pass overdue information in the foreclosure API as separate fields.
    - Total outstanding
    - Interest due
    - Interest accrued not due
    - Overdue amount

---

# **What is the solution?**

- We will start passing the overdue amount details to the LSP as well as on the command centre so that it can be shown to the user in an intuitive manner
- We will be updating our revocation request validation to avoid any collateral risk to the NBFC (move from TOS to TOS + Overdue amount)
- We will add additional parameters in the foreclosure API so that the same can be passed to the user at the time of foreclosing the account

## User stories / User flow

NA

## Requirements

Overdue API response:

```json
{
    "accountNumber": "000000203",
    "paylaterPrincipalDue": 0.000000,
    "paylaterInterestDue": 0.000000,
    "paylaterFeeChargeDue": 0.000000,
    "paylaterPenaltyChargeDue": 0.000000,
    "emiPrincipalDue": 0,
    "emiInterestDue": 0,
    "emiFeeChargeDue": 0,
    "emiPenaltyChargeDue": 0,
    "totalDueAmount": 1143.270000,
    "emiConvertedLoanDetails": [],
    "chargesData": [
        {
            "chargeIdentity": "PF1",
            "amount": 1768.82,
            "taxDetails": [
                {
                    "taxIdentifier": "CGST",
                    "amount": 134.91
                },
                {
                    "taxIdentifier": "SGST",
                    "amount": 134.91
                }
            ],
            "taxAmount": 269.82,
            "penalty": false,
            "amountSansTax": 1499.0,
            "isChargeImpactingAvailableLimit": false,
            "accountChargeId": 203
        },
        {
            "chargeIdentity": "PF1",
            "amount": 1768.82,
            "taxDetails": [
                {
                    "taxIdentifier": "CGST",
                    "amount": 134.91
                },
                {
                    "taxIdentifier": "SGST",
                    "amount": 134.91
                }
            ],
            "taxAmount": 269.82,
            "penalty": false,
            "amountSansTax": 1499,
            "isChargeImpactingAvailableLimit": false,
            "accountChargeId": 203,
            "accountChargeIdentifier": "57b3d679-4e46-44b9-b588-d320a69f9672"
        }
    ],
    "interestToBePostedTillDate": 1143.27,
    "excessAmountToBeAdjusted": 1143.270000,
    "totalPayable": 0.000000
}
```

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