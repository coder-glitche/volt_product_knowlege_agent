# API and Transaction Logging

: Gautam Mahesh
Created time: October 1, 2024 5:25 PM
Status: In progress
Last edited: October 11, 2024 11:39 AM

# **What problem are we solving?**

Currently, we log all our API hits in our DB. However, this isn’t sufficient since this results in the below challenges.

- Lack of visibility at an API level
- Lack of visibility of API level HTTP codes
- Ease of access of API level error or status codes
- Ease of access of API level request and response timestamps
- Lack of storage of computation like name match, etc
- Considerable amount of bandwidth dedicated in extracting data
- Lack of visibility of product level metrics
- Lack of proactive/reactive alerting mechanisms

These challenges result in requiring product, analytics and even engineering spending time on extracting datapoints.

The solution to this problem is storage of API level as well as transaction level data that will help in teams to look at granular data and take decisions in an informed manner. This will also help in developing improved alerting mechanisms.

---

# **How do we measure success?**

Below are some of the ways to measure success.

- At least 95% of API hits to be stored in the required format
- Ability to query or extract insightful data for atleast 100K records
- Ability to extract API level TAT for at least 95% of the hits
- Ability to create product level funnels

---

# **How are others solving this problem?**

Most product & tech teams largely solve this problem by logging data holistically.

- Logging of each request & response payload
- Logging into a DB like MySQL or Mongo or similar platforms
- Use the data logged to build alerting for performance degradation or downtime
- Use a BI tool like Metabase to visualize and build dashboards and alerts

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

### Request Logging

Below are the items that we should log from an API or SDK request perspective.

- Opportunity ID
- Customer ID/Application ID
- Unique API request ID from Volt
- Unique transaction ID from Volt (if applicable)
- Request endpoint of the API
- Parameters of the request body
- Request timestamp upto milliseconds
- Asset where the request is logged (Web, iOS SDK, Android SDK)

### Response Logging

Below are the items that we should log from an API or SDK response perspective.

- Unique API request ID from the partner (bank, 3rd party, DSP)
- Unique transaction request ID from the partner (if applicable)
- API status code from the partner
- Status of the request (Success, Failure, Pending, etc)
- Status code of the request
- Error code of the request (S0000, E0001)
- Response message (Transaction processed successfully)
- Parameters of the response body
- Response timestamp upto milliseconds

### Webhook Logging

Below are the items that we should log from an webhook/callback perspective.

- Callback timestamp upto milliseconds
- Unique API request ID from the partner (bank, 3rd party, DSP)
- Unique transaction request ID from the partner (if applicable)
- API status code from the partner
- Status of the request (Success, Failure, Pending, etc)
- Status code of the request
- Error code of the request (S0000, E0001)
- Volt/DSP endpoint where the intimation is received
- Parameters of the callback/webhook body

## Requirements

The above requirements are to be incorporated for the below APIs on Volt.

| **Stage** | **APIs** | **Comments** |
| --- | --- | --- |
| OTP Login | Generate OTP |  |
| OTP Login | Validate OTP |  |
| PAN Validation | Validate PAN |  |
| MFC Fetch | Validate customer |  |
| MFC Fetch | Fetch funds (Validate OTP) |  |
| CAMS Fetch | Auth (Generate OTP) |  |
| CAMS Fetch | Fetch (Validate OTP) |  |
| KFIN Fetch | Auth (Generate OTP) |  |
| KFIN Fetch | Fetch (Validate OTP) |  |
| Digilocker | Initiate Session |  |
| Digilocker | Get Aadhaar |  |
| Digilocker | Get PAN |  |
| Digilocker | Status Callback |  |
| Selfie | Selife capture |  |
| KYC Pod |  | For Bajaj |
| Bank account validation | Penny Drop |  |
| Mandate Registration | Initiate Mandate |  |
| Mandate Registration | Get Mandate Status |  |
| Mandate Registration | Mandate Status Webhook |  |
| CAMS Pledge | Auth (Generate OTP) |  |
| CAMS Pledge | Fetch (Validate OTP) |  |
| KFIN Pledge | Auth (Generate OTP) |  |
| KFIN Pledge | Fetch (Validate OTP) |  |
| KFS | KFS Generation for DSP |  |
| Agreement | Generate Agreement |  |
| Withdrawal | Request Withdrawal |  |
| PG Repayment | Initiate session | Bajaj & TATA |
| PG Repayment | Status check | Bajaj & TATA |
| Unlien | Initiate unlien | Bajaj & TATA |
| Unlien |  Unlien status | Bajaj & TATA |
|  |  |  |
|  |  |  |

The above requirements are to be incorporated for the below APIs on DSP.

| **Stage** | **APIs** | **Comments** |
| --- | --- | --- |
| PAN Validation | Validate PAN |  |
| MFC Fetch | Validate customer |  |
| MFC Fetch | Fetch funds (Validate OTP) |  |
| CAMS Fetch | Auth (Generate OTP) |  |
| CAMS Fetch | Fetch (Validate OTP) |  |
| KFIN Fetch | Auth (Generate OTP) |  |
| KFIN Fetch | Fetch (Validate OTP) |  |
| CIBIL Fetch | Fetch report |  |
| Digilocker | Initiate Session |  |
| Digilocker | Get Aadhaar |  |
| Digilocker | Get PAN |  |
| Bank account validation | Penny Drop |  |
| Mandate Registration | Initiate Mandate |  |
| Mandate Registration | Get Mandate Status |  |
| Mandate Registration | Mandate Status Webhook |  |
| CAMS Pledge | Auth (Generate OTP) |  |
| CAMS Pledge | Fetch (Validate OTP) |  |
| KFIN Pledge | Auth (Generate OTP) |  |
| KFIN Pledge | Fetch (Validate OTP) |  |
| Withdrawal | Initiate Payout |  |
| Withdrawal | Status check |  |
| Withdrawal | Payout status callback |  |
| PG Repayment | Initiate session |  |
| PG Repayment | Status check |  |
| PG Repayment | Callback |  |
| CKYC Upload | Upload records to CKYC |  |
| CKYC Upload | CKYC status check |  |
| Mandate Presentation | Initiate Mandate Presentation |  |
| Mandate Presentation | Get Mandate Status |  |
| Mandate Presentation | Mandate Status Webhook |  |

---

# **Design**

---

# **Analytics**

Analytics team needs to be informed about the changes. 

Below are the metrics that product team would want to measure.

| Metric | Time period |
| --- | --- |
| Number of API hits that are giving 4xx at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| Number of API hits that are giving 5xx at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| %age of API hits that are giving 4xx at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| %age of API hits that are giving 5xx at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| Error codes at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| Status codes at an API level | Daily, Weekly, Monthly, M-o-M, W-o-W |
| API TAT for specific APIs | Daily, Weekly, Monthly, M-o-M, W-o-W |
| Transaction TAT for specific APIs | Daily, Weekly, Monthly, M-o-M, W-o-W |
| B2B funnel | Daily, Weekly, Monthly, M-o-M, W-o-W |
| B2C funnel | Daily, Weekly, Monthly, M-o-M, W-o-W |
| B2B2C funnel | Daily, Weekly, Monthly, M-o-M, W-o-W |

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

No dependency

## Ops & Sales training

No dependency

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  Build funnels across the board
- [ ]  Business
    - [ ]  
- [x]  Design

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# Implementation Roadmap

Gautam to come back post discussion with engineering.

# Feature Roadmap

Below are the items we intend to build on top of this feature.

- Product and API level funnels
- Leverage error codes and messages for better messaging
- Build alerting for internal performance degradations
- Build alerting for external performance degradations
- Build alerting for internal downtimes
- Build alerting for external downtimes
- Customer alerting on UI (app/web/SDK)
- Customer journey resumption in case of disruption
- Build backup for capabilities where feasible

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes