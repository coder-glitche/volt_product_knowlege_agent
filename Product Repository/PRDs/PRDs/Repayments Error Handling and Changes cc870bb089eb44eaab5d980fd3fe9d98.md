# Repayments Error Handling and Changes

: Ayush Kumar
Created time: October 3, 2024 3:31 PM
Status: In progress
Last edited: November 6, 2024 1:24 PM

# **What problem are we solving?**

Customers are facing issue in receiving repayment confirmation from TATA due to SOA not getting updated from TATA’s end. This results in the below challenges.

- Customer satisfaction (CSAT) impacted
- Reduced retention due to poor customer experience
- Number of customer support tickets increase

These issues arise due to failure to account a successful payment at the Payment Gateway (PG) level to the Statement of Account(SOA) of the user due to an error in the saveLoanReceipt API.

Total failure rate ~ 3%

- Current failure rates for successful transactions is 1.37%
- Failed transactions due to downtime is 1.56%

---

# **How do we measure success?**

- Reduction in man-hours/application
- Decrease in average time to payment confirmation (TAT)
- Reduction in customer support tickets about pending payments

---

# **How are others solving this problem?**

Most lenders don’t rely on SOA flows and instead confirm the payment once a payment is confirmed by their payment gateway. However, most lenders do back-dated receipting of the repayment.

---

# **What is the solution?**

## Requirements overview

First we will implement the solution through admin action and test the retry mechanism by calling saveLoanReceipt API manually by the ops team.

If the payments are accounted in the SOA by manually calling the API, then after careful analysis we will implement the solution in our system.

- **Admin Tool:**
    - When a saveLoanReceipt API error occurs:
        - Log the error details, including timestamp, user ID and credit ID
        - Mark the transaction as "**SUCCESS_WITH_LENDER_RECON_FAILED**" in our system.
        - Display the status to the user in the app as: **IN_PROGRESS**
    - The analytics team prepare a excel sheet of customers whose Repayment PG transaction status is **SUCCESS** but the payment is not accounted in the SOA due to the failure of saveLoanReceipt API
    - This sheet will be sent daily to ops for manual settlement and accounting of the payment in SOA using the admin tool.
    
    ### **APIs Involved in the Repayments (TATA):**
    
    - TataPaymentGatewayConnector API
        
        **REQUEST:**
        
         INFO TataPaymentGatewayConnector RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Encrypted response string 5234aqxKmABM84KJ7sAE9USAscH1yh8lS9tRZh4UEVbdyhl0GrllneUvKdHcr0nWzvaqTFirLq0MepIlbBf9JzZWM+qVQdZDNuGAbYiCmz+FU9oA8acVV839EuvTI5wghJlB4qPfBRc/8waAODb18YvNee67bqy2IkaX/CaLTQokRYRIuvqT75i7mx5b9Sso1ndnEZQVA2goa35yPs5IdxXLPcRMH/7/qp9gPhqfIJogsl2/kJD27psPMEF15xUNBCDYquLwE6gJzmiTK8+wkA==
        
        **RESPONSE:**
        
        INFO TataPaymentGatewayConnector RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Original request
        {
        "totalAmount": "37000.00",
        "uniqueTransactionID": "8a8021899275b51d01927aac1c5868a0",
        "status": "Success",
        "tclTxnId": "11007525",
        "bankRefNo": "428561641893",
        "paymentMode": "Electronic Fund Transfer"
        }
        
    - saveLoanReceipt API
        
        **RESQUEST:**
        
        INFO NonStaticHttpUtility RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Creating post request for uri [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveLoanReceipt](https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveLoanReceipt) with body [
        {
        "LoanScheduleNo": "15022",
        "NBFCBankAccountName": "HDFC BANK - BILLDESK CONTROL ACCOUNT - 164051",
        "NBFCBankAccountNo": "164051",
        "ReceiptAmount": "37000.00",
        "ReceiptDate": "2024-10-11",
        "ReceiptMode": "R",
        "ReceiptValueDate": "2024-10-11",
        "RefNo": "428561641893",
        "UniqueRecordID": "827447804169556"
        }
        ]
        
        **RESPONSE:**
        
        INFO NonStaticHttpUtility RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - got a response with status 200, and body
        {
        "retStatus": "SUCCESS",
        "sysErrorMessage": "",
        "SaveReceiptData_Response": {
        "SaveReceiptData": [
        {
        "LoanAmount": "37000.00",
        "InterestAmount": "0.00",
        "RecordStatusCode": "0",
        "ExcessAmount": "0.00",
        "PenalInterestAmount": "0.00",
        "UniqueRecordID": "827447804169556",
        "Remarks": "Success",
        "ChargesAmount": "0.00"
        }
        ],
        "status": {
        "Status": "Success",
        "Remarks": "",
        "Code": "01"
        }
        },
        "sysErrorCode": ""
        }
        
    
    **ADMIN TOOL FUNCTIONALITY:**
    
    1. This admin tool will again send the request through saveLoanReceipt API.
    
    **Note:** In case of failure of saveLoanReceipt API,  RefNo. should not change during retry.
    
    **Note:** The ops team has to manually call the saveLoanReceipt API through this admin tool for accounting of the repayments in the SOA.
    
    **2. Process:**
    
    - The customer’s details can be accessed using the **collection_id** which can be accessed through the sheet sent by the analytics.
    - Details of customers to be verified and to be checked by the ops team before confirming to call the saveLoanReceipt API through the admin action:
    1. account_holder_name
    2. actual_amount_collected
    3. lan
    4. collection_id
    - The ops team has to match the customer details before confirming for the settlement of payment in the SOA.
    - On confirming the details of customers (For each retry):
        - Attempt to call the saveLoanReceipt API
        - If successful:
            - Update the collection status to "**SETTLED**" in the Backend
            - SUCCESS message should be displayed to the ops on successful retry.
        - If failed:
            - Log the retry attempt
            - Mark the collection as "**SUCCESS_WITH_LENDER_RECON_FAILED**" in our system.
            - Display the status to the user in the app as: **IN_PROGRESS**
            - FAILED message should be displayed to the ops on failure.
    - If the admin action shows FAILED result, then the ops team will prepare a sheet in the same format as sent by the analytics.
    - This sheet will be sent to TATA for manual reconciliation.

**Note:** There will be no separate communications to be sent to user on successful accounting of the Repayment in the SOA

## User stories / User flow

- Customer repays on our app using TATA PG
- Volt receives a confirmation from TATA through a webhook/polar
- Volt receives a successful status confirmation from TATA and hits the saveLoanReceipt API for receipting
- If Volt receives successful confirmation from TATA for saveLoanReceipt API, the customer is informed of the same
- If Volt receives failure confirmation from TATA for saveLoanReceipt API, the customer is informed and Volt will retry hitting the saveLoanReceipt API in an exponential manner till we receive success or 24 hours, whichever is earlier.

Below are the scenarios that can occur.

| Customer messaging | Action | Repayment | Receipting |
| --- | --- | --- | --- |
| Inform customer that repayment is successful | None | Successful | Successful |
| Inform customer that repayment is completed but pending settlement | Hit saveLoanReceipt API  | Successful | Unsuccessful |
| Inform customer that repayment failed and ask the customer to retry | None | Unsuccessful | NA |

## Requirements

### **APIs Involved in the Repayments:**

- TataPaymentGatewayConnector API
    
    **REQUEST:**
    
     INFO TataPaymentGatewayConnector RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Encrypted response string 5234aqxKmABM84KJ7sAE9USAscH1yh8lS9tRZh4UEVbdyhl0GrllneUvKdHcr0nWzvaqTFirLq0MepIlbBf9JzZWM+qVQdZDNuGAbYiCmz+FU9oA8acVV839EuvTI5wghJlB4qPfBRc/8waAODb18YvNee67bqy2IkaX/CaLTQokRYRIuvqT75i7mx5b9Sso1ndnEZQVA2goa35yPs5IdxXLPcRMH/7/qp9gPhqfIJogsl2/kJD27psPMEF15xUNBCDYquLwE6gJzmiTK8+wkA==
    
    **RESPONSE:**
    
    INFO TataPaymentGatewayConnector RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Original request
    {
    "totalAmount": "37000.00",
    "uniqueTransactionID": "8a8021899275b51d01927aac1c5868a0",
    "status": "Success",
    "tclTxnId": "11007525",
    "bankRefNo": "428561641893",
    "paymentMode": "Electronic Fund Transfer"
    }
    
- saveLoanReceipt API
    
    **RESQUEST:**
    
    INFO NonStaticHttpUtility RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - Creating post request for uri [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveLoanReceipt](https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveLoanReceipt) with body [
    {
    "LoanScheduleNo": "15022",
    "NBFCBankAccountName": "HDFC BANK - BILLDESK CONTROL ACCOUNT - 164051",
    "NBFCBankAccountNo": "164051",
    "ReceiptAmount": "37000.00",
    "ReceiptDate": "2024-10-11",
    "ReceiptMode": "R",
    "ReceiptValueDate": "2024-10-11",
    "RefNo": "428561641893",
    "UniqueRecordID": "827447804169556"
    }
    ]
    
    **RESPONSE:**
    
    INFO NonStaticHttpUtility RRId= RId=e74ee433-1028-4aca-815f-338abc9c7565, CreditId=, UId= - got a response with status 200, and body
    {
    "retStatus": "SUCCESS",
    "sysErrorMessage": "",
    "SaveReceiptData_Response": {
    "SaveReceiptData": [
    {
    "LoanAmount": "37000.00",
    "InterestAmount": "0.00",
    "RecordStatusCode": "0",
    "ExcessAmount": "0.00",
    "PenalInterestAmount": "0.00",
    "UniqueRecordID": "827447804169556",
    "Remarks": "Success",
    "ChargesAmount": "0.00"
    }
    ],
    "status": {
    "Status": "Success",
    "Remarks": "",
    "Code": "01"
    }
    },
    "sysErrorCode": ""
    }
    

### Error Types and Validations:

- Functional Error Occurred at saveLoanReceipt API
    
    Sometimes the Payment Gateway (PG) status is successful, but the saveLoanReceipt API returns an error: "Functional error occurred at saveLoanReceipt API".
    
    ## Proposed Solution
    
    **1. Immediate Error Handling**
    
    - When a saveLoanReceipt API error occurs:
        - Log the error details, including timestamp, user ID and credit ID
        - Mark the transaction as "SUCCESS_WITH_LENDER_RECON_FAILED" in our system.
        - Display the Transaction status to the user in the app: PENDING_SETTLEMENT
    
    **2. Automated Retry Mechanism**
    
    - Implement a retry mechanism with exponential backoff.
        - Initial retry after 10 minutes
        - Second retry after 20 minutes
        - Subsequent retries at 40 minutes intervals, up to a maximum of 24 hours
    
    **3. Retry Process**
    
    - For each retry:
        - Attempt to call the saveLoanReceipt API
        - If successful:
            - Update the transaction status to "SETTLED"
            - Remove the transaction from the retry queue
        - If failed:
            - Log the retry attempt and schedule the next retry
    
    **4. Failsafe Mechanism**
    
    - If a transaction remains unconfirmed after 24 hours:
        - Flag it for reconciliation with TATA's system.
        - Automatically mark it as "SETTLED" in our system

- TATA miles downtime
    
    When TATA miles has a downtime, we do not get the response to the saveLoanReceipt API
    
    ## Proposed Solution
    
    **1. Immediate Error Handling**
    
    - When a saveLoanReceipt API error occurs:
        - Log the REQUEST details, including timestamp, user ID and credit ID
        - Mark the transaction as "PENDING_SETTLEMENT" in our system.
        - Display the Transaction status to the user in the app: PENDING_SETTLEMENT
    
    **2. Automated Retry Mechanism**
    
    - Implement a retry mechanism with exponential backoff.
        - Initial retry after 15 minutes
        - Second retry after 30 minutes
        - Subsequent retries at 1-hour intervals, up to a maximum of 24 hours
    
    **3. Retry Process**
    
    - For each retry:
        - Attempt to call the saveLoanReceipt API
        - If successful:
            - Update the transaction status to "SETTLED"
            - Remove the transaction from the retry queue
        - If failed:
            - Log the retry attempt and schedule the next retry
    
    **4. Failsafe Mechanism**
    
    - If a transaction remains unconfirmed after 24 hours:
        - Flag it for reconciliation with TATA's system.
        - Automatically mark it as "SETTLED" in our system

- Failed to update database "Vantage_Prod" because the database is read-only
    
    It is an issue at miles end as suggested by Chandrama from TATA
    
    ## Proposed Solution
    
    **1. Immediate Error Handling**
    
    - When a saveLoanReceipt API error occurs:
        - Log the error details, including timestamp, user ID and credit ID
        - Mark the transaction as "SUCCESS_WITH_LENDER_RECON_FAILED" in our system.
        - Display the Transaction status to the user in the app: PENDING_SETTLEMENT
    
    **2. Automated Retry Mechanism**
    
    - Implement a retry mechanism with exponential backoff.
        - Initial retry after 15 minutes
        - Second retry after 30 minutes
        - Subsequent retries at 1-hour intervals, up to a maximum of 24 hours
    
    **3. Retry Process**
    
    - For each retry:
        - Attempt to call the saveLoanReceipt API
        - If successful:
            - Update the transaction status to "SETTLED"
            - Remove the transaction from the retry queue
        - If failed:
            - Log the retry attempt and schedule the next retry
    
    **4. Failsafe Mechanism**
    
    - If a transaction remains unconfirmed after 24 hours:
        - Flag it for reconciliation with TATA's system.
        - Automatically mark it as "SETTLED" in our system

- String or binary data would be truncated
    
    We get this error when we do not pass the reference number in the specified format and the bank refno is like **“refNo=00000000-0000-0000-2404-170939075300”**
    

- Duplicate Reference No Found
    
    **Description**
    
    This error occurs when the send duplicate request for the same transaction to the saveLoanReceipt API.
    

- Receipt Date Should Be Between Posting Date And EOD+1 Date
    
    **Description**
    
    This is a validation error that TATA plans to remove soon.
    
    **Validation**
    
    - No validation required as per the provided information.

- Receipt Date Should Not Be Backdated Date
    
    **Description**
    
    This error occurs when a repayment request is sent to the saveLoanReceipt API after TATA's End of Day (EOD) processing, which happens around 6:00 PM. Any request sent after EOD with the current day date is considered backdated by TATA's system, resulting in this error.
    

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