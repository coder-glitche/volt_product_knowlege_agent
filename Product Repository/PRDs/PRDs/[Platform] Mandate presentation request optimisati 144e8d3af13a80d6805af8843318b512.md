# [Platform] Mandate presentation request optimisation

: Vaibhav Arora
Created time: November 20, 2024 3:46 PM
Status: Done
Last edited: December 31, 2024 11:49 AM

# **What problem are we solving?**

We are solving three problems via this enhancement:

- Mandate presentation UTR entries for the destination bank (User) are very general. Since the amount is deducted automatically from the user’s bank account, it often gets difficult to track why the amount was deducted (across services and products) while analysing bank account statements.
- Currently reconciliation for mandate presentations is built on top of item ids (shared by Digio) to us in response and also passed as a parameter in the report.

---

# **How do we measure success?**

- Number of queries raised by users on why their amount was debited post presentation
- Improved reconciliation hit rate with the reconciliation team

---

# **How are others solving this problem?**

P1:

Other players pass the mandate UTR to the user so that they can track the corresponding transactions in their account statement. Issue with this is they have to rely on the player’s interface and often discovery is difficult over multiple services (starts with looking at an un-identified transaction in bank account statement/SMS)

P2:

 Other players pass enrichment values to reconcile transactions with internal metrics

---

# **What is the solution?**

P1:

- We will be passing custom narrations in the user’s bank account statement
DSP Finance NACH debit for LAN: FXLAN534324

and UTR in the user’s loan account statement:
Loan repayment received against sale of security: IN9876543210 for account number: FXLAN6789012 with Ref ID:

P2:
We will be passing enrichment values in the presentation request for Digio to assist reconciliation with operations team

## Requirements overview (optional)

| **Field** | **Type** | **Description** | Updated value |
| --- | --- | --- | --- |
| id | string | Unique ID of created plan |  |
| status | string | Current status of created plan |  |
| upcoming_transaction | object | Details of transaction scheduled ahead |  |
| state | enum | Current state of the transaction |  |
|  |  | Allowed: SCHEDULED┃SKIPPED┃PROCESSING┃DELAYED┃FAILED┃AUTHENTICATED┃SUCCESS |  |
| present_at | date-time | Timestamp of presentation |  |
| scheduled_settlement_date | date-time | Date of settlement for the given transaction |  |
| customer | object | Details of customer |  |
| name | string | Name of the customer |  |
| destination_account_type | enum | Type of account of the customer |  |
|  |  | Default: SAVINGS Allowed: SAVINGS┃CURRENT┃OTHER |  |
| destination_ifsc | string | IFSC code of the bank |  |
| user_account_number | string | Masked account number of the customer |  |
| corporate | object | Details of corporate |  |
| name | string | Name of the corporate |  |
| utility_code | string | Utility code registered for the corporate |  |
| corporate_reference | string | Reference number against the corporate |  |
| sponsor_ifsc | string | IFSC code of the sponsor bank |  |
| sponsor_bank_code | string | Bank code for sponsor bank |  |
| corporate_account_number | string | Masked account number of the corporate |  |
| partner | object | Details of partner bank |  |
| name | string | Name of the partner bank |  |
| identifier | string | Email of the partner bank |  |
| details | object | Further details of schedule plan created |  |
| first_proposed_settlement_date | date-time | Date of the first settlement |  |
| next_scheduled_settlement_date | date-time | Date of the next scheduled settlement |  |
| payment_count | integer | Total number of payments to be made |  |
| paid_count | integer | Number of payments already made |  |
|  |  | Default: 0 |  |
| next_present_at | date-time | Date when the next payment should be presented |  |
| last_presented_at | date-time | Date when the last payment was presented |  |
| last_presented_settlement_date | date-time | Date of the last presented settlement |  |
| frequency | enum | Frequency of subscription payments |  |
|  |  | Allowed: onetime┃adhoc┃intraday┃daily┃weekly┃monthly┃quarterly┃semiannually┃yearly┃bimonthly |  |
| present_settlement_before_days | integer | Number of days before which the settlement should be presented |  |
|  |  | Default: 1 |  |
| narration | string | Narration or description of the payment schedule | DSPFIN FXLAN77569687

DSPFIN {{LAN}} |
| amount_in_paise | integer | Amount to be paid in paise |  |
| txn_reference | string | Transaction reference | Mandate request ID |
| product_type | string | Type of the product for which the schedule is created |  |
| ended_at | date-time | Date when the schedule ended |  |
| mandate_id | string | Mandate ID associated with the payment schedule |  |
| client_ref_id | string | Client reference ID for identification | FXCID {ID} |
| sub_user | object | Sub user details, if the request was containing sub-user identifier |  |
| id | string | Sub-user ID |  |
| identifier_value | string | Identifier used for sub-user, this is generally emailID or mobile number |  |
| identifier | enum | Type of identifier |  |
|  |  | Allowed: EMAIL┃MOBILE |  |
| email_id | string | Sub-user's email ID if registered |  |
| mobile | string | Sub-user's mobile number |  |
| created_at | date-time | Timestamp of plan creation |  |
| sponsor_bank_name | string | Name of the sponsor bank |  |

```json
{
    "umrn": "UMRN2984366445219389",
    "amount": 2.0, 
    "settlement_date" : "2019-04-10",
    "corporate_account_number" : "123456789",
    "corporate_config_id" : "TSE180110115609336HGUGFNECH30001",
    "destination_bank_id": "HDFC0000158",
    "customer_account_number" : "01581000136321",
    "customer_name" : "devesh",
    "frequency" : "monthly"
    "optional_attr" : {
       "utr_number" : "",
       "pg_bank_ref_number" : "",
       "member_id" : "",
       "client_id" : "",
       "bank_code" : "",
       "txn_type" : "",
       "additional_date" : "",
       "order_id" : "",
       "credit_utility_code" : "",
       "product_type" : "",
       "mis_shared_with" : "",
       "destination_bank_code": ""
    }
}
```

## User stories / User flow

## Requirements

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