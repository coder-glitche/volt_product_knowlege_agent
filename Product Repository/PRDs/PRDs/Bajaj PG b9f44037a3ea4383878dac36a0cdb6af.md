# Bajaj PG

: Ranjan kumar Singh
Created time: July 22, 2024 4:49 PM
Status: In progress
Last edited: February 19, 2026 7:14 PM
Owner: Lalit Bihani

# **What problem are we solving?**

- We need to integrate the **BAJAJ Payment Gateway** to streamline the collection of principal and interest repayments.
- Currently, with our **CC Avenue integration for BAJAJ repayment collection**, the repayment accounting process is manual, causing delays in reflecting repayments in the Statement of Account (SOA).
- By integrating the **BAJAJ Payment Gateway**, the repayment accounting process will be automated and realtime, similar to how it functions with the **TATA Payment Gateway**.

---

# **How do we measure success?**

- Collection complete to settlement TAT should get reduced (Mostly realtime when repayment done in business hours[8 AM - 6 PM])
    - Currently its 24 hours in happy case scenario with CCAVENUE
- Repayment accounting related tickets raised by customer should get reduced
    - 16 ticket was raised by customer related to repayment accounting from 7th oct to 15 oct
- Usage of admin action to settle BFL repayment should get reduced
    - Used 518 times from 1st sept to 15 Oct
- Man-hours spent by operations and support in answering queries and resolving should reduce.
- CSAT related to repayment should improve [not tracking CSAT right now]. This is proposed to be picked up in the [In app user review [Play store]](In%20app%20user%20review%20%5BPlay%20store%5D%20e9c6dfde05e4451b9c4b66f7e0a268c5.md) feature.

Guardrail metrics.

- Success rate of Bajaj PG should be same or higher than CCAvenue

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

### **1. Principal and interest repayment flow with BAJAJ PG**

**Required Config:** We need to keep current implementation [Integration with CCAvenue] as backup

- Flag based switching of PG should be possible
- PG identifiers are required to maintain [Sample: BAJAJ, CCAVENUE]
    - This identifiers will be used to identify the PG used to made the repayment

**Repayment flow:**

Step 1 : Create payment request

- When user initiate the repayment after entering the amount , Front end to create request using  the Form posting method.
- For more details: Follow API document to create payment request

[Payment_Request_Response.pdf](Bajaj%20PG/Payment_Request_Response.pdf)

Classification of repayment can be done by passing the parameter mentioned below:

- Request parameter for Principal repayment and interest repayment
- Pass “LAS_PARTPAYMENT” in AdditionalInfo3 for principal repayment
- Pass “LAS_OVERDUEPAYMENT” in AdditionalInfo3 for interest repayment

| **Parameter** | **Sample Value** | **Field Required** | **Description** |
| --- | --- | --- | --- |
| MerchantID | voltmoney | Mandatory | Mechant ID |
| Unique_id | 123451232 | Mandatory | Order Id |
| Amount | 1000.12 | Mandatory | Payment Amount |
| AdditionalInfo1 | hnv122wcj1 dwdcdj | Mandatory | CustomerID [VLAN] |
| AdditionalInfo2 | Ranjan Kumar Singh | Mandatory | Customer name |
| AdditionalInfo3 | LAS_PARTPAYMENT | Mandatory | Payment flag [Principal repayment or interest repayment] |
| ReturnURL | Webhook URL | Mandatory | Volt are required to create a webhook URL. This is the Link on which response of payment will receive  |

Step 2: User are redirected on BAJAJ checkout page

Step 3: User either Completes the payment, cancel the payment or payments gets failed

Step 4: Repayment status will be received on Webhook URL

Step 5: User will be redirected to Volt page based on the status

Step 6: For repayment which status are Failed, Notification will be shown to user, with Retry option on UI. User should be able to retry same repayment txn.

Step 7: For all terminal status like “PENDING” we need to poll the status API to get the latest status of the txn.

Step 8: For the SUCCESS [PG] status or COLLECTION_COMPLETE[Volt], we need to poll the SOA statement API to mark the repayment as settled [logic already exist]

**Handling of payment status and redirection** 

Flow: 

User entered amount for repayment -> User clicked on pay button -> Payment request will be created using “Form posting” method → On successful request creation → User will be redirected to BAJAJ PG → User will complete the payment → User will redirected on Volt page & user will be the page based on status received in return URL.

BAJAJ PG STATUS mapping with Volt Status

| **PG status** | **Volt Status** | **Message on UI** | Redirection behaviour |
| --- | --- | --- | --- |
| NOT_INITIATED | REQUESTED | NA | Take user to Flexipay screen where user enters the repayment amount |
| INITIATED | REQUESTED | NA | Take user to Flexipay screen where user enters the repayment amount |
| SUCCESS | COLLECTION_COMPLETE |  | Take user to success screen |
| AWAITED | PENDING_SETTLEMENT |  | Take user to the In progress screen |
| INVALID | FAILED |  | Take user to the failure screen |
| FAILURE | FAILED |  | Take user to the failure screen |
| PENDING | PENDING_SETTLEMENT |  | Take user to the In progress screen |
| EXPIRED | FAILED |  | Take user to the failure screen |
| TIMEOUT | FAILED |  | Take user to the failure screen |
| UNSUCCESSFUL | FAILED |  | Take user to the failure screen |
| ABORTED | CANCELLED |  | Take user to the failure screen |
| REJECTED | FAILED |  | Take user to the failure screen |
| AUTO-REVERSED | FAILED |  | Take user to the failure screen |
| reversing | FAILED |  | Take user to the failure screen |
| FRAUD | FAILED |  | Take user to the failure screen |
| DATA NOT FOUND  | FAILED |  | Take user to the failure screen |
| ERROR | FAILED |  | Take user to the failure screen |
| When repayment reflected in SOA/ Accounting is complete | SETTLED |  |  |

**Handling of non-terminal status [Status API]**

Status API URL: 

UAT: https://bfl-api-dev.azure-api.net/Transaction/CHECK_PAYMENT_STATUS

PROD: https://bflapimprod.bajajfinserv.in/Transaction/CHECK_PAYMENT_STATUS

- We Need to poll the status check API for all terminal status to get the latest status of repayment.
- Polling behaviour should be same as implemented for TATA PG
    - Poll status API every hours for 3 days
- We will get the same status as mentioned above in status API

Status API request parameter

| Name | Data Type | Mandatory | Remarks |
| --- | --- | --- | --- |
| transactionid | String | Y | The unique ID which is sent
from the source in the
payment request API |
| Paymenttype | String | Y | Pass “LAS” as payment type |
| paymentplatform | String | Y | saltertechnologiesPL |
- Repayment status Response Parameter List
- Refer below doc to store txn details which we can get in response

[Check_Payment_Status_v2.1.pdf](Bajaj%20PG/Check_Payment_Status_v2.1.pdf)

prod sub key : 7669d6c35b6e469f85e9d0ebdb855fe7

### 2. Repayment Accounting logic

Overview: 

Repayment auto accounting will happen every day including weekends and holiday 8AM to 6PM, post 6PM the funds will be accounted on next day morning 8 AM

> On month end Payment made post 3 PM will be accounted on Next day
> 

**Principal repayment accounting based on business hours**

| **Repayment time** | **Accounting date** | **Remarks** |
| --- | --- | --- |
| 8 AM to 6 PM | Same day | If user repay principal b/w 8 AM to 6 PM then interest will be not charged for same day  |
| 6:01 PM to 11:59 PM | Next day 8 AM | If user repay principal b/w 6:01 PM to 11:59 PM then interest will be charged for same day |
| 12:00 AM to 7:59 AM | Same day post 8 AM | Interest will be not charged for same day |

## User stories / User flow

## Requirements

---

# **Design**

---

# **Analytics**

FE/BE amplitude analytics events:

| Journey | Events name | Events property | Sample value | Trigger from | Remarks | Working on staging? | Working on prod? |
| --- | --- | --- | --- | --- | --- | --- | --- |
| - User clicks on repay CTA after entering repayment amount 
- User initiate repayment of interest
- User initiate repayment of withdrawal | REPAYMENT_INITIATED | pg-type | - BFL_PG
- CCA | FE |  |  |  |
|  |  | amount | 12000 |  |  |  |  |
|  |  | collection_type | principal |  |  |  |  |
| When user redirected to PG page | BFL_PG_PAGE_LOADED | status | true/false | FE |  |  |  |
|  |  | reason | {{error}} |  |  |  |  |
| Repayment status received from webhook or status API | REPAYMENT_STATUS | pg-type | - BFL_PG
- CCA | BE |  |  |  |
|  |  | amount | 12000 |  |  |  |  |
|  |  | collection_type | principal |  |  |  |  |
|  |  | status | {{PG_STATUS}} |  |  |  |  |
|  |  |  |  |  |  |  |  |

---

**Reporting requirement:**

1. **Total Repayments via** BAJAJ

- Breakdown of repayments by collection type (e.g., Principal, Interest, etc.)
- Repayment Status count of all transactions based on Volt status (refer: BAJAJ PG STATUS mapping with Volt Status table for repayment status list)
- Repayment Status count of all transactions based on PG status (refer: BAJAJ PG STATUS mapping with Volt Status table for repayment status list)
- Success and failure rate

2. **Principal Repayments via** BAJAJ

- Count and status of repayments made between 8 AM and 6 PM
- Count and status of repayments made between 6 PM and 8 AM
- Success and failure rate

3. **Interest Repayments via** BAJAJ

- Count and status of interest repayments made between the 1st and 6th of the month
- Count and status of interest repayments made after the 6th of the month
- Success and failure rate
1. **List of customer who repaid via** BAJAJ
    1. Required customer details: 
        1. Phone
        2. PAN
        3. Name
    2. Required credit details:
        1. Credit id/loan number
        2. Mandate status
    3. Required collection details:
        1. Collection type
        2. Collection id
        3. Collection amount
        4. Collection status
        5. Collection method (UPI, Debit Card, Netbanking)
2. List of customer who has made repayment via CCAVENUE

# **Timeline/Release Planning**

---

# **Go to market**

### **Project timelines:**

| **Action items** | **ETA** | **Remarks** |
| --- | --- | --- |
| Development | Completed |  |
| QA | 21 OCT |  |
| UAT | 22 OCT | Subject to QA completion |
| Internal training(Sales/ops) | 23 OCT |  |
| CUG | 23 OCT |  |
| First roll out (Production release) | 24 Oct |  |
| Roll out for B2B platform[SDK version upgrade] | TBD |  |

### **Detailed Plan:**

1. UAT on staging environment 
    1. Testing of BFL PG repayment feature and flow
    2. Testing of firebase rollout
    
2. **Internal training:**
- Sales and ops training about the release plan
- Training about the behaviour of PG
- Training about the accounting of each type of repayment like principal, interest.
- OPS training to handle the accounting of the repayment made through CCavenue

1. **CUG on prod:**
- We need to do **CUG** on production for internal employee account
    - Whitelist Manish kumar and Amrit account on production for testing
    - **CUG** on x-platform like Android, iOS Web
    - **CUG** for B2B platform, PLJ, Partner platform
        - Pending: Need to answer how to test for B2B platforms, Connect with Sagar
    - Verify repayment reporting which we send to BFL for accounting

1. **Production release plan post UAT/CUG:**
    
    <aside>
    💡
    
    **Prerequisite:** 
    
    - Feature should be available on WEB, android and iOS.
        - Need force update to be enabled on android and iOS
    - Repayment reporting is setup
        - Analytics team to only send the repayment report for accounting to BFL which is made via the CCAvenue.
    </aside>
    
     
    
- We need to user Firebase rollout config to incrementally rollout the feature
    - Rollout structure:
        
        
        | Rollout% | Time gap per increment | Condition |
        | --- | --- | --- |
        | 10% | - | Default |
        | 20% | 48 | Post review of performance metrics on 10% |
        | 50% | 48 | Post review of performance metrics on 20% |
        | 100% | 48 |  |
- Release plan based on platform:
    - SDK:
        - For partner who are using Android, IOS, React native SDK, they will required to update the SDK version to get this feature reflected for their customers.
            - Customers will still be able to repay via CCAVENUE
        - Those who are using JS SDK, this feature will work out of box.
        - For partners who are using new SDK version, feature will be available based on the Roll out structure.
            - Pending: Mention SDK version on which feature will be available [Need more clarity from sagar[Dev]]
        - Onboard Keyur to get the SDK version updated from all partners.
    - BAU platform: Based on above Rollout structure.

### **Test scenario to be referred at time of QA/UAT/CUG:**

- BFL PG should work for all type of repayment like principal, interest, shortfall, foreclosure
- Page redirection should work based on the requirement mentioned under requirement overview section “BAJAJ PG STATUS mapping with Volt Status”
    - Check PG status mapping with Volt DB
    - Repayment details [Collection] should be made available on retool, service desk and Audit DB for analytics and reporting.
- Should work on all platform like Android, iOS, Web, B2B platform and PLJ
    - Platform level feature test checklist
    
    | Flow | Android | iOS | Web | B2B platform | PLJ | Partner platform | Remarks |
    | --- | --- | --- | --- | --- | --- | --- | --- |
    | Principal repayment | Yes [Sample] |  |  |  |  |  |  |
    | Interest repayment | No[Sample] |  |  |  |  |  | Interest repayment account as principal [Sample] |
    | Shortfall repayment |  |  |  |  |  |  |  |
    | Foreclosure repayment |  |  |  |  |  |  |  |
    | Renewal repayment |  |  |  |  |  |  |  |
    | Loan expired repayment |  |  |  |  |  |  |  |
    | 1 user making repayment on different platform, using BFL PG & CCavenue |  |  |  |  |  |  |  |
- Accounting of repayment should work based on the business hours. refer: Requirement overview section no 2.
    - Repayment accounting behaviour test checklist:
        
        
        | Cases | Expected behaviour | Result |
        | --- | --- | --- |
        | Principal repayment made b/w 8 AM to 6 PM | - Repayment amount reflected in SOA in real time
        - POS is updated in SOA
        - Getting updated POS, DP in API
        - Shortfall margin should get adjusted |  |
        | Principal repayment made 6:01 PM to 11:59 PM | - Repayment not reflected in SOA in same day
        - Same txn reflected in SOA on next day post 8 AM
        ——POS is updated in SOA
        ——Getting updated POS, DP in API |  |
        | Principal repayment made 12:00 AM to 7:59 AM | - txn reflected in SOA on next day post 8 AM
        ——POS is updated in SOA
        ——Getting updated POS, DP in API |  |
        | Principal repayment made on month end post 3 PM | - Repayment not reflected in SOA in same day
        - Same txn reflected in SOA on next day post 8 AM
        ——POS is updated in SOA
        ——Getting updated POS, DP in API |  |
        | Interest repayment made b/w 1st to 6th[before BFL EOD] of the month when interest is due | - Interest amount accounted as advance interest
        - Advance interest reflected on SOA
        - Advance interest amount coming in foreclosure API
        - If not foreclosed, interest amount to settle with Interest on 6th [POST EOD]
        - Mandate not to be presented if interest is settled |  |
        | Interest repayment made b/w 1st to 6th when not due | - Interest amount to remain in advance interest
        - Advance interest should get settled at time of foreclosure |  |
        | Interest repayment made b/w 6th [POST EOD] to month end when due and not due | - Interest amount to remain in advance interest
         |  |
        | BFL mandate presentation status is pending then in-app interest payment will not be accounted, and amount will remain in advance interest, if mandate is presented then do bounce charges will be applied [POST 6th of the month] | Need to check/test |  |
        | Partial interest repayment made b/w 1st to 6th and mandate is registered | - Amount paid will get settled with interest
        - Mandate will be presented for remaining amount [If due≥10] |  |
- Switching between BFL PG and CCAvenue
    - We should be able to switch PG based on platform and flow and feature should work as expected.

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  
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

PG URL:

UAT: [https://uatpayments.bajajfinserv.in/Paymentgateway/Payments/Direct_Loan_Payment](https://uatpayments.bajajfinserv.in/Paymentgateway/Payments/Direct_Loan_Payment)

Prod: [https://payment.bajajfinserv.in/Paymentgateway/Payments/Direct_Loan_Payment](https://payment.bajajfinserv.in/Paymentgateway/Payments/Direct_Loan_Payment)