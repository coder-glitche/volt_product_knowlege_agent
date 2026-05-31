# DSP: UPI Autopay Integration for PhonePe

: Gautam Mahesh
Created time: March 4, 2025 1:09 PM
Status: Done
Last edited: June 2, 2025 5:38 PM

# **What problem are we solving?**

- NBFCs using NACH mandates face delays in mandate registration and activation due to dependency on bank processing times (T+2 to T+7 days).
- Physical NACH mandates have high failure rates due to signature mismatches, and bank rejections, leading to delayed interest collection.
- Borrowers often drop off during NACH mandate registration because it requires physical forms, wet signatures, or authentication(Aadhaar, Netbanking, or debit card), leading to lower activation rates.

---

# **How do we measure success?**

- Registration Success Rate – Percentage of borrowers who successfully complete UPI Autopay registration.
- Mandate Rejection Rate – Percentage of mandates failing due to incorrect details, or bank rejections (lower is better).
- Turnaround Time (TAT) for Mandate Setup – Time taken to complete the UPI Autopay registration process.

---

# **What is the solution?**

UPI Autopay is the ideal solution for NBFCs looking to improve digital lending collections and interest payments. It offers a faster, easy to set up, cost-effective, and automated way to handle recurring payments compared to traditional NACH mandates.

### Key Features & Benefits of UPI Autopay

1. Instant Mandate Registration
    - Borrowers can set up mandates in real-time via UPI apps like PhonePe, Google Pay, and Paytm.
    - No need for physical forms or long approval timelines like NACH.
2. Lower Rejection Rates
    - Direct customer authorization via UPI reduces the risk of incorrect details or failed registrations.
3. Automated & Timely Debit Processing
    - Auto-debits occur on scheduled dates without customer intervention.
4. Real-time Status Tracking & Failure Handling
    - Instant callbacks & APIs provide real-time debit status updates.
    - Automatic retries (up to 8 times within 48 hours) for failed debits due to insufficient funds.
5. Flexible Debit Options
    - Supports multiple debits per day for high-ticket loans (split payments).
6. Seamless Integration
    - Can be integrated via APIs into existing NBFC loan management systems.

---

## User stories / User flow

**Registration**

- The user intending to take a loan against mutual funds enters through the PhonePe application.
- The user completes all necessary KYC steps, uploads a selfie, and provides additional data for the DSP lender on the PhonePe UI.
- PhonePe prompts the user to set up the UPI mandate on their verified bank accounts, with the data later to be shared with DSP.
- The user sets up the mandate via the PhonePe app and proceeds to open the DSP loan account.

---

## Requirements

The flow is broken into 2 parts-

1. Registration
2. Presentation

### Registration

- The user intending to take a loan against mutual funds enters through the PhonePe application.
- The user completes all necessary KYC steps, uploads a selfie, and provides additional data for the DSP lender on the PhonePe UI.
- PhonePe will not call DSP’s bank verification or mandate setup APIs. Instead, it will interact with PhonePe PG APIs to set up UPI autopay.
- Once the UPI mandate is successfully registered, the PhonePe lending team will call the mandate posting API exposed by DSP to share all mandate details. The attributes include:
    - Opportunity ID
    - UMN
    - Status
    - Timestamp
    - Bank Account Number
    - IFSC, etc.
- The mandate posting API will accept data only if the status is “Success.”
- In the DSP database, an entry will be created against the Opportunity ID and marked as completed. DSP will also generate the “Bank Utility Reference ID” and “Mandate Reference ID.”
- In the same mandate posting API response, DSP will share 2 utility reference IDs.
    - Bank Utility Reference ID
    - Mandate Utility Reference ID
- Using these utility reference IDs, the PhonePe lending team will call the Generate Loan Contract API.
- The Generate Loan Contract API will function only if all utility reference IDs are in a successful state. For mandate verification, DSP will rely on PhonePe PG APIs, and for bank verification, DSP will rely on mandate posting done by PhonePe lending.
- PhonePe PG team will share a registration summary report(MIS) on a T+1 basis which will include all the successful and failed registrations.
- DSP will reconcile the list of mandates registered using the UMN field from the PhonePe PG MIS against the DSP database.
- Two possible ways for going wrong-
    - Mandate data missing in PhonePe PG MIS report
    - Data is available in PhonePe PG MIS but mandate posting is not done by PhonePe Lending.
    
    In both the above cases, there should be a SOP to address the issues.
    
- DSP to rely on PhonePe PG MIS reports as the first source of truth.

![image.png](DSP%20UPI%20Autopay%20Integration%20for%20PhonePe/image.png)

- Mandate Posting API - Request Body
    
    ```json
    {
      "entityCode": "PhonePe",  // Predefined code representing the entity initiating the request
      "entityReqId": "PhonePeTxnId123",  // Unique identifier for the lender's whitelisted entity
      "mandateType": "UPI_Autopay",  // Type of mandate being created (e.g., UPI_AUTOPAY, NACH)
      "opportunityId": "OPP123",  // Opportunity ID associated with the lender
      "loanId": "LN123456789",  // (Could be null) Unique identifier for the loan associated with the mandate
      "merchantTxnId": "TXN987654321",  // Merchant’s transaction ID for tracking the mandate request
      "bankAccNo": "123456789012",  // Bank account number linked to the mandate
      "bankAccType": "Savings",  // Type of bank account (e.g., Savings, Current)
      "ifscCode": "HDFC0001234",  // IFSC code identifying the bank branch
      "accHolderName": "John Doe",  // Name of the individual or entity holding the bank account
      "umn": "UMN987654321",  // Unique Mandate Number issued for this mandate
      "mandateStatus": "Success",  // Mandate status (e.g., Success, Pending, Failed)
      "instrumentType": "NACH",  // Type of financial instrument (e.g., ECS, NACH)
      "mandateExpiryDate": "2026-12-31",  // Expiration date of the mandate in yyyy-MM-dd format
      "mandateMaxAmount": 50000.00,  // Maximum transaction amount allowed under this mandate
    }
    ```
    
- Mandate Posting API - Response Body (Success)
    
    ```json
    {
      "status": "Success",
      "message": "Mandate created successfully",
      "bankUtilityReferenceId": "URBANK9143527826",
      "mandatUtilityReferenceId": "URMNDT4945818111",
      "mandateDetails": {
        "entityReqId": "ENTREQ987654321",
        "loanId": "LN123456789",
        "opportunityId": "OPP123",
        "umn": "UMN987654321",
        "mandateStatus": "Active",
        "mandateExpiryDate": "2026-12-31",
        "mandateMaxAmount": 50000.00
      }
    }
    ```
    
- Mandate Posting API - Response Body (Error)
    
    ```json
    {
      "status": "Error",
      "message": "Internal server error. Please try again later.",
      "errorCode": "ERR_SERVER_500"
    }
    ```
    
- Mandate Posting API - Response Body (Mandate is not in success state)
    
    ```json
    {
      "status": "Error",
      "message": "Mandate status is not in success",
      "errorCode": "Bad_Request"
    }
    ```
    

- PhonePe lending team will be calling our mandate posting API only once during the registration process.
- For mandates, which are being cancelled, paused or unpaused by users DSP expects PhonePe Lending team to share the callbacks.
- DSP will mark the status of the mandate according to the callback received.
- PhonePe PG team to treat UMN as the primary identifier in the callback.

- Mandate Cancel Callback (UMN is not in the request body)
    
    ```json
    {
        "type": "SUBSCRIPTION_CANCELLED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "CANCELLED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    
- Mandate Revoked Callback
    
    ```json
    {
        "type": "SUBSCRIPTION_REVOKED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "REVOKED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    
- Mandate Pause
    
    ```json
    {
        "type": "SUBSCRIPTION_PAUSED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "PAUSED",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": 1708798426196,
            "pauseEndDate": 1708885799000
        }
    }
    ```
    
- Mandate Unpause
    
    ```json
    {
        "type": "SUBSCRIPTION_UNPAUSED",
        "payload": {
            "merchantSubscriptionId": "MS1708797962855",
            "subscriptionId": "OMS2402242336054995042603",
            "state": "ACTIVE",
            "authWorkflowType": "TRANSACTION",
            "amountType": "FIXED",
            "maxAmount": 200,
            "frequency": "ON_DEMAND",
            "expireAt": 1737278524000,
            "pauseStartDate": null,
            "pauseEndDate": null
        }
    }
    ```
    

### Presentation

- Once the mandate is successfully registered and posted by PhonePe Lending, DSP will process it accordingly.
- DSP will bill the customers of PhonePe on the 1st of every month basis for the utilization of the credit line.
- PhonePe Lending team will refer to DSP loan summary API to find the interest due to be collected from the user.
- PhonePe Lending team will be doing the e2e presentation of mandate.
    - PDN
    - Debit
- PhonePe Lending team will define the logic of retries for PDN & debit.
- For every successful transaction, the PhonePe Lending team would call DSPs presentation posting API.

- Mandate Presentation API (Request)
    
    ```json
    {
      "accountId": "ACC123456",  // The account ID associated with the lender's application for the transaction
      "uniqueId": "PP123456789",  // PhonePe unique identifier for the transaction
      "receiptAmount": 10000.50,  // The payment amount received
      "loanNo": "FXL987654321",  // The loan number associated with the lender
      "transactionRefNumber": "UTR1234567890",  // The transaction reference number (UTR)
      "receiptDateTime": "2025-02-07",  // The date and time when the receipt was issued, formatted as yyyy-MM-dd
      "status": "Success"
    }
    ```
    
- Response
    
    ```json
    {
      "status": "Success",
      "message": "Payment recorded successfully",
      "receiptDetails": {
        "accountId": "ACC123456",
        "uniqueId": "PP123456789",
        "receiptAmount": 10000.50,
        "loanNo": "LN987654321",
        "transactionRefNumber": "UTR1234567890",
        "receiptDateTime": "2025-02-07",
        "status": "Success"
      }
    }
    ```
    
- Response - Bad Request
    
    ```json
    {
      "status": "Failure",
      "message": "Invalid loan number",
      "errorCode": "ERR_LOAN_INVALID"
    }
    ```
    
- Response - ISE
    
    ```json
    {
      "status": "Error",
      "message": "Internal server error. Please try again later.",
      "errorCode": "ERR_SERVER_500"
    }
    ```
    

### SFTP Setup

This SFTP is for MIS reports exchange between PhonePe PG & DSP. PhonePe PG to share the SFTP setup guide.

### LMS Posting

@Vaibhav Arora needs alignment from internal stakeholders. Blocked for now.

---

# **Analytics**

### Automated **Reconciliation**

[Settlement Report.xlsx](DSP%20UPI%20Autopay%20Integration%20for%20PhonePe/Settlement_Report.xlsx)

[FORWARD_TRANSACTION_Sample.csv](DSP%20UPI%20Autopay%20Integration%20for%20PhonePe/FORWARD_TRANSACTION_Sample.csv)

The Analytics team will build an automated reconciliation process for mandate registration and presentation.

### **Mandate Registration Reconciliation**

- Data Sources: PhonePe PG MIS & DSP Database
- Reconciliation Fields:
    - Unique Mandate Number (UMN)
    - Status
    - Maximum Amount
    - Expiry Date
    - Bank Account Details

### **Mandate Presentation Reconciliation**

- Data Sources: PhonePe PG & DSP Database
- Reconciliation Fields:
    - Unique Mandate Number (UMN)
    - Loan Account
    - Amount
    - Status
    - Date & Time

### **Discrepancy Handling**

- If any discrepancies are found, a new `.csv` file will be generated.
- The file will be shared with the PhonePe Lending team for further review and resolution.

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