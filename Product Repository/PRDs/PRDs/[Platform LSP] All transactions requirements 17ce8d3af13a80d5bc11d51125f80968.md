# [Platform/LSP] All transactions requirements

: Vaibhav Arora
Created time: January 15, 2025 7:57 AM
Status: Done
Last edited: January 22, 2025 6:38 PM

# **What problem are we solving?**

As a platform we provide multiple APIs so that our consumers in this case:

- Internal operations team
- Loan service providers (Volt / Indmoney / Groww)

Are able to consume and accordingly process the required information in an efficient manner. It is important that we provide the right amount of information for the following reasons:

- Optimise computation and processing of information at the consumer end
- Avoid polling and high frequency calls for information to our system
- Ensuring important information is shared with the consumer (to avoid downstream effects to our users).

We need a capability to show all transactions via an API so that the same can be used by the operations team as well as by other LSPs to be able to communicate and share relevant information with our users. 

Types of transactions:

| Transaction | Description | Debit/Credit | Transaction initiation source |
| --- | --- | --- | --- |
| Withdrawal | Withdrawals made by the user | Dr | User |
| Repayment - (PG) | Repayments made by the user  | Cr | User |
| Repayment - (Mandate collections) | Mandate collection made by the NBFC | Cr | NBFC  |
| Repayments - (Sell off) | Invocation collection made by the NBFC | Cr | NBFC  |
| Charge posting (Excluding penal) | Charges applied by the NBFC | Dr | NBFC  |
| Withdrawal reversal | Withdrawals reversed by the NBFC | Cr | NBFC  |
| Repayment reversal | Repayments reversed by the NBFC | Dr | NBFC  |
| Interest posting | Interest applied by the NBFC at the end of the billing cycle or at the time of foreclosure | Dr | NBFC  |
| Excess payment | Excess amount refunded back to the user by the NBFC (if the account was in excess) | Dr | NBFC/System  |
| Excess reversal | Excess amount reversal (in case the corresponding disbursement to the user fails) | Cr | NBFC/System  |
| Charge reversal | Charge posting reversed by the NBFC | Cr | NBFC/System  |
| Interest waiver | Interest waived for the user by the NBFC | Cr | NBFC/System  |
| Charges knock off | Charges knocked off (settled against a withdrawal) by the NBFC | Cr | NBFC/System  |
| Penal charge posting | Penal charges applied by the NBFC on the condition of the account becoming overdue | Dr | NBFC/System  |

User requested transactions are stored as requests in the system, and have pending states with a lifecycle that can be shared with the user. 

For example a withdrawal can have the following states:

- Pending disbursement
- Pending checker approval
- Awaiting beneficiary bank confirmation
- Pending SOA posting
- Completed/Failed

It is important for the LSP to be able to 1) Consume and 2) Propagate this information to the user to ensure that the users are able to track the status of their requests accurately. The LSP should also be able to show the corresponding states to the user and also manage conditions like:

- A user can only have one active withdrawal request at a time

The LSPs should also be able to track the repayment attempts that the user has made to ensure that they are able show failed attempts (if available) to the user.

(In case the user’s account is deducted: So that the user is able to track refunds of their requests in their bank account).

---

# **How do we measure success?**

We want to ensure that the LSPs are able to propagate the status of the transactions to their users clearly and the NBFC operations team are able to access transaction request information to support LSPs and direct customers accurately.

We are also assisting LSPs to go live quickly while enabling them to show lifecycle tracking of transactions to the users without building their own infrastructure by directly integrating with Volt APIs.

- # of tickets raised by users related to the status of their transactions
- TAT to resolve tickets raised by users related to the status of their transactions

---

# **How are others solving this problem?**

Most LSPs (Volt) maintain their own lifecycle management and NBFCs (TCL / BFL) offer a statement API that gives access to all the posted transactions (usually wrappers built on top of LMS transactions APIs)

---

# **What is the solution?**

We will be building capabilities for LSP/CC to show the following details:

- Withdrawal requests (with status of transactions)
- Repayment requests (with status of transactions)
- Repayment orders (to show failed or pending transaction orders)
- All completed transactions API (Statement API)

| Transaction | Description | Debit/Credit | Transaction initiation source | How will it be consumed via CC/LSP |
| --- | --- | --- | --- | --- |
| Withdrawal | Withdrawals made by the user | Dr | User | Withdrawal requests + all transactions |
| Repayment - (PG) | Repayments made by the user  | Cr | User | Repayment requests + all transactions |
| Repayment - (Mandate collections) | Mandate collection made by the NBFC | Cr | NBFC  | All transactions |
| Repayments - (Sell off) | Invocation collection made by the NBFC | Cr | NBFC  | All transactions |
| Charge posting (Excluding penal) | Charges applied by the NBFC | Dr | NBFC  | All transactions |
| Withdrawal reversal | Withdrawals reversed by the NBFC | Cr | NBFC  | Withdrawal requests (status will change to reversed) + all transactions |
| Repayment reversal | Repayments reversed by the NBFC | Dr | NBFC  | Repayment requests (status will change to reversed) + all transactions |
| Interest posting | Interest applied by the NBFC at the end of the billing cycle or at the time of foreclosure | Dr | NBFC  | All transactions |
| Excess payment | Excess amount refunded back to the user by the NBFC (if the account was in excess) | Dr | NBFC/System  | All transactions |
| Excess reversal | Excess amount reversal (in case the corresponding disbursement to the user fails) | Cr | NBFC/System  | All transactions |
| Charge reversal | Charge posting reversed by the NBFC | Cr | NBFC/System  | All transactions |
| Interest waiver | Interest waived for the user by the NBFC | Cr | NBFC/System  | All transactions |
| Charges knock off | Charges knocked off (settled against a withdrawal) by the NBFC | Cr | NBFC/System  | All transactions |
| Penal charge posting | Penal charges applied by the NBFC on the condition of the account becoming overdue | Dr | NBFC/System  | All transactions |

We have withdrawal requests and repayment requests API already created for the command centre. However their corresponding statuses will have to be generalised to make it easier for the LSPs to integrate and understand the responses.

Repayment orders API:

Repayments order API will have a lot of transactions at a user level, as an order is created every time a user tries to do a payment, this can be a big API call and may bring a lot of load on the system. To solve for the same, we will create it to be a filter API where repayment orders for a specific period will be called at a time.

<aside>
💡

We will build the API to support date ranges (without threshold) however we need capabilities to set a maximum threshold in terms of date range in the API to control the same for LSPs. By default the API will give details for orders in the last 30 days to the LSP (at a user level)

</aside>

Request structure:

```json
{
  "loan_account_number": "FXLAN12345678",
  "date_filter": {
    "from_date": "2024-12-15",  // Optional, defaults to current_date - 30 days
    "to_date": "2025-01-15"     // Optional, defaults to current_date
  }
}
```

Response structure (Success)

```json
{
  "status": "success",
  "data": {
    "loan_account_number": "FXLAN12345678",
    "orders": [
      {
        "order_id": "order_EKzX2WiEWbMxmx",
        "amount": 5000.00,
        "currency": "INR",
        "status": "CREATED",
        "created_at": "2025-01-10T14:30:00Z",
      },
      {
        "order_id": "order_EKzX2WiEWbMxmx",
        "amount": 5000.00,
        "currency": "INR",
        "status": "CAPTURED",
        "created_at": "2025-01-10T14:30:00Z",
      }
      }
    ]
}
```

Response structure (Failed)

```json
{
  "status": "error",
  "errorCode":"LOAN_NOT_FOUND"
}

(When a request is made for an invalid loan account)

{
  "status": "error",
  "errorCode":"DATE_RANGE_INVALID"
}

(When a request is made for an invalid date range (From date> To date))

{
  "status": "error",
  "errorCode":"INTERNAL_SERVER_ERROR"
}

(When system fails to process the request)
```

User stories / User flow

- NA

---

# **Design**

-NA

---

# **Analytics**

NA

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