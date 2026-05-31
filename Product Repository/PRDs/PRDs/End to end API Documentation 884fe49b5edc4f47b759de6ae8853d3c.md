# End to end API Documentation

: Ameya Aglawe
Created time: October 16, 2024 7:28 PM
Status: Not started
Last edited: February 12, 2025 5:50 PM

# **What problem are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

# **How do we measure success?**

- Reduction in man hours spent in de-bugging
- Reduction in touch points required at the time of de-bugging or understanding APIs

---

# **How are others solving this problem?**

---

# **What is the solution?**

### For TATA

| **Functionality**  | **API**  | **Log name** | Significance  |
| --- | --- | --- | --- |
| Loan creation  | createClient | 1. got createClient
2. got createClient response |  |
|  | createLoan  | 1. got createLoan
2. got createLoan response  |  |
|  | updateSanction | 1. got updateSanctionLimit
2. got updateSanctionLimit response |  |
|  | updateLoan  | 1. got updateLoanLimit
2. got updateLoanLimit response |  |
|  | saveLoanContract | 1. got saveLoanContract
2. got saveLoanContract response  |  |
|  | adhocCharges | 1. got adhocCharges 
2. got adhocCharges response |  |
| Disbursal  | getDisbursementInfo | 1. got getDisbursementInfo
2. got getDisbursementInfo response  |  |
|  | saveDisbursement | 1. got saveDisbursement
2. got saveDisbursement response |  |
|  | DisbursementStatus | 1. got getDisbursementStatus
2. got getDisbursementStatus response |  |
| Repayment | paymentStatus | 1. Getting payment status for collectionId 
2. got getPaymentStatus response  |  |
|  | saveLoanReceipt | 1. got saveLoanReceipt
2. got saveLoanReceipt response |  |
| Un-pledge  | getSummary | 1. got getSummary
2. got getSummary response |  |
|  | Release Securities | 1. got releaseSecurities request
2. got releaseSecurities response |  |
| Foreclosure | getSummary | 1. got getSummary
2. got getSummary response |  |

---

### BAJAJ

| **Functionality**  | **API**  | **Logs** | **Significance** |
| --- | --- | --- | --- |
| Loan creation  | GET_LOAN_STATEMENT_URI | 1. got loan statement request for lan-number
2. got loan statement response for lan-number |  |
|  | GET_HOLDING_STATEMENT_URI | 1. got holding statement request for fas-number
2. got holding statement response for fas-number |  |
|  | GET_HOLDING_DATA_URI | 1. got holding data request for fas-number
2. got holding data request for fas-number |  |
| Disbursal  | GET_DISBURSEMENT_INFO_URI | 1. got getDisbursementInfo request for lan-number
2. got getDisbursementInfo response for lan-number |  |
|  | SAVE_DISBURSEMENT_URI | 1. got saveDisbursement request for lan-number
2. got saveDisbursement response for lan-number |  |
|  | CHECK_DISBURSEMENT_STATUS_URI | 1. got checkDisbursalStatus request for lan-number
2. got checkDisbursalStatus response for lan-number |  |
| Repayment | BAJAJ repayment API integration in progress |  |  |
| Un-pledge  | ForeClosureDetails | GetForeClosureStatementResponse |  |
|  | ReleaseShares | 1. got release share request for  lan-number
2. got loan statement response for lan-number |  |
|  | ReleaseShares status  | 1. got check release share status request for  lan-number
2. got check release share status response for lan-number  |  |
| Foreclosure  | GET_FORECLOSURE_STATEMENT_URI | 1. "got foreclosure statement request for fas-number {}, request {}", loanNumber, request
2. "got foreclosure statement request for fas-number {}, response {}", loanNumber, response |  |

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