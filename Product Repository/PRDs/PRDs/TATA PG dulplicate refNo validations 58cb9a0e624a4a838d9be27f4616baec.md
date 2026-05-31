# TATA PG dulplicate refNo. validations

: Ayush Kumar
Created time: December 6, 2024 2:24 PM
Status: In progress
Last edited: December 9, 2024 5:43 PM

# **What problem are we solving?**

We're addressing a critical payment reconciliation issue where:

1. The bank occasionally generates duplicate reference numbers for two different payments.
2. This leads to failed accounting of repayments in the statement of accounts(SOA) of the customer in TATA for repayments with SUCCESSFUL transaction status from the TATA Payment Gateway.

---

# **How do we measure success?**

- Reduction in the number of repayments with Collection status as SUCCESS_WITH_LENDER_RECON_FAILED due to “Duplicate Reference No found” error remark.
- Reduction in the tickets related to failed accounting of payments in the SOA in TATA

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

When a user makes a repayment through TATA Payment Gateway, 

**TataPaymentGatewayConnector API**

- REQUEST:
    
    ```jsx
    INFO TataPaymentGatewayConnector RRId= RId=45cc1b80-dd6d-411f-a473-9233ca57852a, CreditId=, UId= - Encrypted response string 5234aqxKmABM84KJ7sAE9TlnfM8XIoVYzN8Q9f9fdjVnYo6sz9pCbQ2All6Ac9hhlqaBSYQGhMdOETZj+frUngwmSHUhgZbOe2M6wh6/Proa177YUXSR3n6blH0aDodlL9/c/fqdtlaIj8XQdmIcPCBzJtZ16wvoOxDYHRO6pJjyOKXth49b9tTu5fXTPE1sN7NfwoyspnrMvXm0PJC03qxlKrr/utL6pi/oo1xey7ym42zg589J0q+22AtwZorI
    ```
    
- RESPONSE:
    
    ```jsx
     INFO TataPaymentGatewayConnector RRId= RId=45cc1b80-dd6d-411f-a473-9233ca57852a, CreditId=, UId= - Original request 
    {
        "totalAmount": "150000.00",
        "uniqueTransactionID": "8a80700893837acc0193883446bb50a5",
        "status": "Success",
        "tclTxnId": "11680883",
        "bankRefNo": "032076",
        "paymentMode": "Electronic Fund Transfer"
    }
    ```
    

To account the successful payment in the SOA of customer, we send the request through the saveLoanReceipt API.

**saveLoanReceipt API**

- REQUEST:
    
    ```jsx
     INFO TataConnector RRId= RId=45cc1b80-dd6d-411f-a473-9233ca57852a, CreditId=, UId= - got saveLoanReceipt 
    {
        "LoanScheduleNo": "13826",
        "NBFCBankAccountName": "HDFC BANK - BILLDESK CONTROL ACCOUNT - 164051",
        "NBFCBankAccountNo": "164051",
        "ReceiptAmount": "150000.00",
        "ReceiptDate": "2024-12-03",
        "ReceiptMode": "R",
        "ReceiptValueDate": "2024-12-03",
        "RefNo": "032076",
        "UniqueRecordID": "765151397823413"
    }
     for lender: Tata
    ```
    

If the payment is accounted successfully, we receive the below response and the collection status is marked as SETTLED.

- RESPONSE:
    
    ```jsx
    INFO NonStaticHttpUtility RRId= RId=45cc1b80-dd6d-411f-a473-9233ca57852a, CreditId=, UId= - got a response with status 200, and body 
    {
        "retStatus": "SUCCESS",
        "sysErrorMessage": "",
        "SaveReceiptData_Response": {
            "SaveReceiptData": [
                {
                    "LoanAmount": "147863.00",
                    "InterestAmount": "2137.00",
                    "RecordStatusCode": "0",
                    "ExcessAmount": "0.00",
                    "PenalInterestAmount": "0.00",
                    "UniqueRecordID": "765151397823413",
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
    ```
    

If the payment is not accounted successfully due to “Duplicate Reference No found” error remark, we receive the below response and the collection status is marked as SUCCESS_WITH_LENDER_RECON_FAILED.

- RESPONSE:
    
    ```jsx
    INFO NonStaticHttpUtility RRId= RId=986ddd70-e4de-43d3-a2cb-d7bee8f21453, CreditId=, UId= - got a response with status 200, and body 
    {
        "retStatus": "FAILURE",
        "sysErrorMessage": "Functional error occured at SaveLoanReceipt details application.",
        "SaveReceiptData_Response": {
            "SaveReceiptData": [
                {
                    "LoanAmount": "0.00",
                    "InterestAmount": "0.00",
                    "RecordStatusCode": "1",
                    "ExcessAmount": "0.00",
                    "PenalInterestAmount": "0.00",
                    "UniqueRecordID": "594869185655874",
                    "Remarks": "Duplicate Reference No found, ",
                    "ChargesAmount": "0.00"
                }
            ],
            "status": {
                "Status": "Success",
                "Remarks": "",
                "Code": "01"
            }
        },
        "sysErrorCode": "ERRMILES213"
    ```
    

## Requirements

In the request of saveLoanReceipt API, we pass the **RefNo** parameter which we receive in the response to the successful payment through TataPaymentGatewayConnector API

Note: A payment reference number is **a unique identifier for a financial transaction**, such as bank transfers, card payments, and direct debits.

Validations for RefNo : **The character Limit for the parameter RefID is 25 and it does not allow special characters**

**CHANGES:**

Now, we will pass the **RefNo** as {{LoanContractNo}}V{{bankRefNo}} in the saveLoanReceipt API to account for the payment in the SOA. This RefNo will be unique and we will not encounter the error while accounting the payment in the SOA

**Note:** If the RefNo with the above combination of LoanContractNo and bankRefNo exceeds the length of 25 character then truncate the RefNo to 25 characters.

---

# **Design**

No design requirement since there is no FE changes. 

---

# **Analytics**

- We will monitor the count of “Duplicate Reference No found” error remark on a daily basis for a period of 7 days.
- We will monitor the count of collection status as “SUCCESS_WITH_LENDER_RECON_FAILED” on a daily basis for a period of 7 days through Operational Excellence sheet.

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

- [x]  Product
    - [ ]  -
- [x]  Business
    - [ ]  -
- [x]  Design
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