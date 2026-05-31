# Virtual Accounts for LSPs

: Ameya Aglawe
Created time: June 16, 2025 10:22 AM
Status: Pending Review
Last edited: June 20, 2025 11:32 AM

# **What problem are we solving?**

---

- Currently partner LSPs are looking for an alternate payments methods than the payment like because -
    - They have an existing UI flow ready to support VA accounts (SmallCase)
    - They want to provide a back-up repayment option in case payment link is down

# **How do we measure success?**

---

- Number of transactions via VA
- Number of successful transactions made through VA
- TAT of settlement of transaction made through VA

# **How are others solving this problem?**

---

- Lenders like BFL and TCL have exposed their VAs with partner LSPs
    - BFL has exposed separate VAs for interest and principal repayments (to handle apportionment efficiently)
    - TCL has a common VA for interest and principal repayments (handle apportionment through a logic)
- TCL and BFL have shared a logic to get a VA number unique at a loan account level

# **What is the solution?**

- DSP will expose APIs that enable each partner LSP to retrieve a virtual account (VA) number uniquely mapped to a customer’s loan account. Instead of embedding the VA generation logic within each LSP’s system, this design centralizes the logic at DSP’s end. As a result, if DSP ever modifies the way VAs are generated—due to regulatory, operational, or technical changes—no updates are required on the LSP side.
- This decouples the VA logic from partner implementations and ensures long-term scalability, consistency, and ease of maintenance across all integrations.
- LSPs will get the status of VA repayment through the repayment order status update web hook

## Requirements

---

- User journey
    - User comes to the repayment screen of the LSP app.
    - LSPs call the VA APIs to fetch VA details in their repayment screen
    - Users gets the VA details and pays the due amount
- VA API Payload
    - Request
        
        ```jsx
        {
              fenixLoanAccountId : FXLAN81888552
        }
        ```
        
    - Response
        
        ```jsx
        {
        
          "virtualAccountNumber": "30130181888552",
            "virtualAccountIFSCCode": "YESB0CMSNOC",
            "fenixLoanAccountId": "FXLAN81888552",
            "beneficiaryName": "DSP Finance Private Limited",",
            "bankName": "YES BANK",
            "beneficiaryType" : "Merchant"
            "branchName" : "Cms National Operating Centre Mmr",}
        ```
        
- Web hook
    - Payload
        
        ```jsx
        {
        "fenixRequestId": "RPOID388324548569",
        "fenixLoanAccountId": "{{fenixLoanAccountId}}",
        "fenixRequestType": "REPAYMENT_ORDER_STATUS_UPDATE",
        "status": "SETTLED",
        "eventTimestamp": "2024-11-14T10:25:30Z",
        "eventDetails": {
        "fenixLoanAccountId": "FXLAN48398934",
        "orderId": "RPOID388324548569",
        "amount": 1000,
        "payInOrderId": "8a8142aa92d2dee8019310940f690075",
        "paymentGatewayOrderId": "order_PJBLREmVoVv0PW",
        "utrNumber": "5757665",
        "payInOrderType": "VIRTUAL_ACCOUNT",
        "status": "SETTLED",
        "paymentLink": "https://rzp.io/rzp/ci9vDpA",
        "paymentLinkExpiryDate": 1731236359000,
        "redirectionUrl": "https://app.staging.voltmoney.in",
        "repaymentAttributionType": null,
        "preferredPaymentMethod": null,
        "linkedRepaymentRequestId": "RPRID322181838459",
        "payInPaymentDetails": [
        {
        "payInPaymentId": "8a8142aa92d2dee80193109492480076",
        "payInPaymentGatewayId": "pay_PJBLYS17A4bgys",
        "amount": 1000,
        "paymentMethod": "NETBANKING",
        "paymentStatus": "CAPTURED",
        "errorDescription": null,
        "utrNumber": "5757665",
        "requestedOn": null,
        "settledOn": 1731149989000,
        "lastUpdatedOn": 1731149997310
        }
        ]
        ,
        "remarks": "Repayment of amount 1000.00",
        "requestedOn": 1731149958920,
        "completedOn": 1731149989000
        }
        }
        
        ```
        
    - Web hook statuses
        
        
        | Statuses (DSP Internal) | Terminal state | Will be triggered to LSPs |
        | --- | --- | --- |
        | CREATED | No | Yes |
        | PENDING_PAYMENT_CONFIRMATION | No | No  |
        | REJECTED | No | No  |
        | SETTLED | Yes | Yes |
        | REFUNDED | Yes | Yes |

# **Design**

---

# **Analytics**

---

- Number of transactions via VA (breakup by sourcing channel)
- Number of successful transactions made through VA
- TAT of settlement of transaction made through VA

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