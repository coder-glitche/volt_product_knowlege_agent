# DSP: UPI Autopay Integration for NBFC

: Gautam Mahesh
Created time: January 27, 2025 3:49 PM
Status: In progress
Last edited: June 16, 2025 2:41 PM
Owner: Parikshit Kumar

[UPI Autopay Research Doc](UPI%20Autopay%20Research%20Doc%20190e8d3af13a80d5af7bdad27e1a5871.md)

[UPI Autopay Evaluation](UPI%20Autopay%20Evaluation%2018fe8d3af13a808495f5e03909b03345.md)

---

<aside>
💡

Please note that this PRD isn’t applicable for the PhonePe lending program and covers all other LSPs and Volt programs.

</aside>

# Structure

# **What problem are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.
- Physical NACH mandates have high failure rates due to signature mismatches, and bank rejections, leading to delayed interest collection.
- ESign NACH which covers ~450 banks gives registration confirmation after 2 working days which still has higher failure rates.
- Physical NACH mandates gives registration confirmation after 4-5 working days only, creating operational overheads.

---

# **How do we measure success?**

- Registration Success Rate – Percentage of borrowers who successfully complete UPI Autopay registration.
- Mandate Rejection Rate – Percentage of mandates failing due to incorrect details, or bank rejections (lower is better).
- Turnaround Time (TAT) for Mandate Setup – Time taken to complete the UPI Autopay registration process.
- Application TAT - Time taken for a customer or MFD or LSP to complete an application from fetch to mandate.

---

# **What is the solution?**

UPI Autopay is the ideal solution for NBFCs looking to improve digital lending collections and interest payments. It offers a faster, easy to setup, cost-effective, and automated way to handle recurring payments compared to traditional NACH mandates.

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
    - Automatic retries (up to 8 times) for failed debits due to insufficient funds.
5. Flexible Debit Options
    - Supports multiple debits per day for high-ticket loans (split payments).
6. Seamless Integration
    - Can be integrated via APIs into our loan management system.

---

## User Flow

### Pre-requisites

Below are the pre-requisites.

- DSP completes the integration with PhonePe for UPI mandates
- DSP sets up the SFTP with PhonePe for file exchange
- DSP creates a UPI ID. Sample : dspfinance.phonepe@ybl
- Mandate amount: 15K (this is the maximum amount permitted without AFA)
- Mandate tenure: 10 years
- Mandate MCC: 7322 (Loan repayments)
- Mandate cannot be revoked by users
- DSP creates a subscription at a customer level

### **Registration Flow**

Below is the mandate registration flow.

- The user intending to take a loan against mutual funds enters through Volt or any other 3rd party LSP like Groww, Indmoney, etc (Not PhonePe).
- The user completes all necessary KYC steps, uploads a selfie, and provides additional data for the DSP lender on the PhonePe UI.
- The user sees the UPI mandate option only if the drawing power is ≤20L. If the user has a drawing power > 20L, the user has to setup a mandate using NACH only.
- Alternatively, the user can always choose to setup a mandate using NACH for lower amount as well. Note: we might increase the DP limit for UPI mandates as we go basis our experience.
- The LSP prompts the user to set up the UPI mandate using one of the 3 modes. At this stage, we will prompt the customer to pay using the registered bank account only.
    - QR code - the user scans the QR code of the mandate and completes the registration flow. This flow is ideal for desktop flows.
    - Intent Link - the user clicks on the link a list of TPAPs (PhonePe, GPay, PayTm, etc) are opened up which are installed on the device. This flow is ideal for app or mobile web flows like in B2C or B2B channels.
    - Mandate link - the provider creates a link which is shared with DSP. DSP creates a wrapper on that link that can be shared with the customer. This will be a deep-link that can be opened on mobile. This is required for MFD channels.
    - Collect request - the provider triggers mandate setup against a VPA passed by DSP. In this case, the customer or the MFD needs to enter the VPA. This flow is ideal for desktop flows or where the customer is being assisted like in MFD channel.
- The user is redirected to the TPAP UI where they see the mandate registration screen for intent/QR/link or navigates to the relevant app in case of collect request flow.
- The user authorizes the mandate with their MPIN on the TPAP UI. There will be a 1 INR debit from the customer which will be refunded automatically by PhonePe.
- If the user’s MPIN is valid, the mandate is setup an DSP receives a callback from PhonePe with the status of the mandate registration
- DSP records the status and takes the user to the next page.
- If the user faces an error after setting up an UPI mandate, the user can retry using NACH as well and setup a mandate using NACH.

### Registration Thresholds

Below is the average drawing power by channel/source with DSP as lender.

| Channel | <=2L | 2-5L | 5-10L | 10-20L | 20-50L | >50L | Grand Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B2B | 46,045 | 293,713 | 819,533 | 1,526,400 |  |  | 93,096 |
| B2C | 76,560 | 332,457 | 738,811 | 1,428,587 | 3,126,189 | 7,773,133 | 417,722 |
| MFD Corporate | 89,397 | 324,761 | 747,236 | 1,423,615 | 3,112,781 | 7,831,450 | 509,862 |
| MFD Direct | 95,885 | 326,158 | 734,145 | 1,429,144 | 3,026,364 | 9,380,043 | 817,896 |
| MFD SaaS | 83,493 | 338,093 | 738,663 | 1,270,604 | 2,931,141 | 8,624,000 | 814,363 |
| PhonePe | 59,007 | 305,671 | 712,324 | 1,351,400 | 2,836,475 |  | 118,549 |
| Grand Total | 70,567 | 322,832 | 735,993 | 1,411,278 | 3,042,352 | 8,786,263 | 422,629 |

Below is the count of applications by channel/source with DSP as lender.

| Channel | <=2L | 2-5L | 5-10L | 10-20L | 20-50L | >50L | Grand Total |
| --- | --- | --- | --- | --- | --- | --- | --- |
| B2B | 145 | 16 | 3 | 1 |  |  | 165 |
| B2C | 656 | 218 | 99 | 46 | 28 | 12 | 1059 |
| MFD Corporate | 312 | 155 | 77 | 46 | 27 | 4 | 621 |
| MFD Direct | 498 | 352 | 225 | 162 | 96 | 28 | 1361 |
| MFD SaaS | 75 | 43 | 32 | 23 | 17 | 4 | 194 |
| PhonePe | 1713 | 219 | 45 | 19 | 4 |  | 2000 |
| Grand Total | 3399 | 1003 | 481 | 297 | 172 | 48 | 5400 |

Below is the percentile based DP calculation by channels.

| Channel | 80th | 90th | 95th | 99th |
| --- | --- | --- | --- | --- |
| B2B | 1060900 | 1189050 | 1253125 | 1304385 |
| B2C | 164660 | 180780 | 188840 | 195288 |
| MFD Corporate | 50900 | 53600 | 54950 | 56030 |
| MFD Direct | 1211940 | 1331920 | 1391910 | 1439902 |
| MFD SaaS | 391880 | 432090 | 452195 | 468279 |
| PhonePe | 673600 | 695300 | 706150 | 714830 |
| Total | 467480 | 992480 | 1769340 | 4708664 |

Below is the illustrative calculation of monthly interest for customers from different channels on DSP. 

| Channel | Drawing Power | Monthly Interest @ 12% |
| --- | --- | --- |
| B2C | 300,000 | 3,000 |
| B2B | 200,000 | 2,000 |
| B2B2C | 1,000,000 | 10,000 |
| B2B2C - Large Ticket | 5,000,000 | 50,000 |
| B2B2C - Exceptional | 50,000,000 | 500,000 |

Basis the above logic, we will be able to cover the below %age of applications in each channel where monthly interest will be ≤ 15000 (DP ≤ 15L).

- B2C: 99.7%
- B2B: 99.5%
- PhonePe: 99.8%
- MFD Corporate: 99.9%
- MFD SaaS: 99.8%
- MFD Direct: 99.8%

### **Billing Flow**

Below is the billing flow.

- DSP generates the interest for the previous month on the 1st of the next month basis the usage
- DSP communicates the billed amount to LSPs via a web-hook and customers (via LSPs) through communication channels.
- Customers can come to Volt or LSP app and pay the due amount and the same is adjusted against the outstanding interest and principal (in that order)
- The final amount to be presented for UPI based mandates will need to be finalized on 5th 6 PM since DSP needs to intimate PhonePe for debiting funds at least 24 hours before the actual debit
- The UPI mandate presentation file will be generated similar to NACH and will be available on CC, which will be approved by operations before presentation
- If the customer pays before the above cut-off, the interest amount is adjusted by the amount paid towards interest

### **Presentation Flow**

Below is the mandate presentation flow.

- DSP initiates a debit notification with debit date as 7th and triggers the API call to PhonePe on the 6th at 8 AM.
- PhonePe initiates a pre-debit notification (PDN) to the customers immediately and informs DSP of the status after retries.
- If PDN fails, DSP re-triggers PDN to PhonePe immediately so that the debit can be placed next day where feasible
- DSP intimates the customers in case of PDN failure due to customer level issues like bank account issue, VPA issue, insufficient funds, etc
- If PDN succeeds, PhonePe triggers the debit notification to NPCI at its end at a customer level on 7th at 8 AM
- PhonePe receives the status from NPCI at a customer level which is propagated to DSP through a callback
- If DSP receives a successful confirmation from PhonePe for a debit, DSP posts an entry in the LMS which apportions the funds towards the due/overdue amount.
- DSP informs the LSP through APIs of successful debit through a webhook to the configured end-points of the LSP.
- If DSP receives a failure intimation from PhonePe due to customer level issue, DSP levies a bounce charge on the customer and re-triggers a debit for 9th.

**Points to Note**

- The number of retries for debit needs to be finalized
- Customer isn’t levied a bounce charge for UPI mandates unlike NACH
- A minimum of 24 hours TAT is required between PDN and debit

---

## Requirements

The flow is broken into 2 parts.

1. Registration
2. Presentation

### Registration

- The user reaches the mandate step after adding the bank account step.
- The user is shown the mandate if the offer selected is ≤ 10L.
- The user confirms on setting up an UPI mandate.
- The user is given the option on UI to setup a mandate through one of the below modes.
    - QR (only for laptop)
    - Intent link (only for mobile)
    - Collect request
- If the user chooses Collect request, the user needs to enter the VPA. At this stage, DSP hits the [Validate UPI ID API](https://developer.phonepe.com/v1/reference/upi-address-validate-api) to validate the VPA
- If the VPA is invalid, the user is shown a message as ‘Invalid UPI ID. Please enter a valid UPI ID or use other modes to setup the mandate’
- If the VPA is valid but name match with NSDL is <70%, the user is shown a message as ‘Please enter a VPA that belongs to the applicant’.
- Only if the VPA is valid and the name match with NSDL is ≥ 70% is the user allowed to proceed if its a collect flow.
- If the user chooses QR/Intent, the user isn’t asked for any details on UI.

**Validate VPA API**

- DSP Will call PhonePe’s Validate VPA API to check if a VPA entered is valid and belongs to the same individual as the customer.

Below is the request payload for this API.

| Parameter | Value | Mandatory | Comments |
| --- | --- | --- | --- |
| `*type*` | VPA | Y | Static value for now |
| `*vpa*` | VPA entered by the user | Y | Sample value: 9999999999@ybl, john.doe@okhdfcbank, etc |

PhonePe validates this API and responds as below.

| Parameter | Value | Mandatory | Comments |
| --- | --- | --- | --- |
| `*valid*` | true/false | Y | True if VPA is valid and False is VPA is invalid |
| `*name*` | VPA name | Y | Name as per VPA. Might not match the name in the bank account at times |

If valid = true and name match b/w name field and NSDL PAN verification ≥ 70% is when we consider the VPA to be valid. Post this stage is when we will allow the use to go ahead with the mandate setup.

**Create Subscription API**

- This API is used to create a mandate for a customer with PhonePe
- DSP will call PhonePe’s [create subscription API](https://developer.phonepe.com/v1/reference/subscription-v2-setup/) with the below parameters to create a mandate order.

| Parameter | Value | Mandatory | Comments |
| --- | --- | --- | --- |
| merchantOrderId | Order ID | Y | Unique order for each request |
| amount | 100000 | Y | Static value for now |
| expireAt | 900000 | N | Default - 10 minutes or 600000ms |
| `*paymentFlow.type*` | SUBSCRIPTION_SETUP | Y | Static value for now |
| `*paymentFlow.merchantSubscriptionId*` |  | Y |  |
| `*paymentFlow.authWorkflowType*` |  PENNY_DROP | Y | Hardcoded value for now |
| `*paymentFlow.amountType*` | VARIABLE | Y | Needs to be set to VARIABLE to handle debits of varying amounts |
| `*paymentFlow.maxAmount*` | 100000 | Y | Maximum limit for UPI mandate |
| `*paymentFlow.frequency*` | ON_DEMAND | Y | Frequency of presentation |
| `*paymentFlow.expireAt*` | 10 Years in ms | N | Default Value : 30 years. We will be going ahead with 10 years for now |
| `*paymentFlow.paymentMode*` | If customer chooses QR/intent, we will pass *UPI_INTENT*. 
If customer chooses collect, we will pass *UPI_COLLECT* | Y | Possible Values :*{    “type”: “UPI_INTENT”,    “targetApp”: “com.phonepe.app”}{    “type”: “UPI_COLLECT”,    “details”: {        “type”: “VPA”,        “vpa”: “1234567890@ybl”    }}*

 |
| `*paymentFlow.paymentMode.targetApp*` |  |  | To be clarified with PhonePe |
| `*deviceContext.deviceOS*` |  |  | To be clarified with PhonePe |
| `*metaInfo.udf1*` | Fenix LAN |  | User defined fields propagated in status check & callbacks |
- **Create** **Subscription Sample Request for Intent**
    
    {
    "merchantOrderId": "MO1709025658932",
    "amount": 200,
    "expireAt": 1709058548000,
    "metaInfo": {
    "udf1": "some meta info of max length 256",
    "udf2": "some meta info of max length 256",
    "udf3": "some meta info of max length 256",
    "udf4": "some meta info of max length 256",
    "udf5": "some meta info of max length 256"
    },
    "paymentFlow": {
    "type": "SUBSCRIPTION_SETUP",
    "merchantSubscriptionId": "MS1709025658932",
    "authWorkflowType": "TRANSACTION",
    "amountType": "FIXED",
    "maxAmount": 200,
    "frequency": "ON_DEMAND",
    "expireAt": 1737278524000,
    "paymentMode": {
    "type": "UPI_INTENT",
    "targetApp": "com.phonepe.app"
    }
    },
    "deviceContext": {
    "deviceOS": "ANDROID"
    }
    }
    
- **Create** **Subscription Sample Request for Collect**
    
    {
    "merchantOrderId": "MO1709025691805",
    "amount": 200,
    "expireAt": 1709058548000,
    "metaInfo": {
    "udf1": "some meta info of max length 256",
    "udf2": "some meta info of max length 256",
    "udf3": "some meta info of max length 256",
    "udf4": "some meta info of max length 256",
    "udf5": "some meta info of max length 256"
    },
    "paymentFlow": {
    "type": "SUBSCRIPTION_SETUP",
    "merchantSubscriptionId": "MS1709025691805",
    "authWorkflowType": "TRANSACTION",
    "amountType": "VARIABLE",
    "maxAmount": 2000,
    "frequency": "ON_DEMAND",
    "expireAt": 1737278524000,
    "paymentMode": {
    "type": "UPI_COLLECT",
    "details": {
    "type": "VPA",
    "vpa": "999@ybl"
    }
    }
    }
    }
    
- DSP receives the response from PhonePe with the below fields.

| Parameter | Value | Mandatory | Comments |
| --- | --- | --- | --- |
| `*orderId*` | Order ID | Y | Unique order for each request |
| `*state*` | Pending | Y | Default - Pending |
| `*intentUrl*` | Link | N | Only passed for intent flow |
- By default, the status of the mandate will be in ‘Pending’ state.
- In case of collect request, the user receives a SMS and notification from the TPAP where the VPA is registered (PhonePe, GPay, etc.)
- If the user has requested for intent, DSP receives a complete link from PhonePe. When the user clicks on this link, the user is redirected to a TPAP of their choice where the user can authorize using their MPIN
- If the user has requested for QR, DSP converts the intent URL into a dynamic QR code using a library ([sample library](https://www.qrcodechimp.com/qr-code-generator-for-upi)). This code is displayed on the UI to the user
- The user scans the QR code from the TPAP of their choice and authorizes the mandate using the MPIN
- If the user has entered a valid or invalid MPIN, PhonePe sends a [callback](https://developer.phonepe.com/v1/reference/subscription-v2-callback) to DSP’s endpoint with the status.
- PhonePe sends the below datapoints in the callback.

| Parameter | Value | Mandatory | Comments |
| --- | --- | --- | --- |
| `*merchantSubscriptionId*` |  | Y | orderId passed by DSP to PhonePe at the time of mandate setup |
| `*subscriptionId*` | PhonePe’s subscription ID |  | Needs to be stored for presentation |
|  |  |  |  |
| `*state*` | ACTIVE,
CANCELLED,
REVOKED,
PAUSED | Y | Default value - ACTIVE |
| *authWorkflowType* |  | Y |  |
| `*amountType*` | PENNY_DROP | Y | Value passed by DSP to PhonePe at the time of mandate setup |
| `*maxAmount*` | 100000 | Y | Maximum limit for UPI mandate |
| `*frequency*` | ON_DEMAND | Y | Frequency of presentation as passed at the time of mandate setup |
| `*expireAt*` | 10 Years in ms | N | Default Value : 30 years. We will be going ahead with 10 years for now |
| `*pauseStartDate*` |  | Y | Possible Values :*{    “type”: “UPI_INTENT”,    “targetApp”: “com.phonepe.app”}{    “type”: “UPI_COLLECT”,    “details”: {        “type”: “VPA”,        “vpa”: “1234567890@ybl”    }}* |
| `*paymentFlow.paymentMode.targetApp*` |  |  | To be clarified with PhonePe |
| `*deviceContext.deviceOS*` |  |  | To be clarified with PhonePe |
| `*metaInfo.udf1*` | Fenix LAN |  | User defined fields propagated in status check & callbacks |
- DSP checks the status of the mandate using the state field. If the value = ACTIVE, DSP allows the user to move forward.

### Billing

- 

### Presentation

### **PDN Retry Logic:**

1. The PDN is automatically retried internally, requiring no action from DSP.
2. Only terminal status will be shared with DSP.
    1. Success
    2. Failure

### Debit Retry Logic

Below are the attributes of PDN API & it’s logic-

1. Autodebit: True, Retry Strategy: Standard
    - The merchant passes `autodebit=true and redemptionRetryStrategy=standard` while calling the notification API.
    - PhonePe sends the PDN and, upon successful PDN, automatically retries up to 10 times over the next 48 hours.
    - Merchant will receive the webhook once the transaction has reached terminal status.
2. Autodebit: False, Retry Strategy: Standard
    - The merchant must call the debit API 24 hours after the PDN call.
    - Once the debit API is triggered, PhonePe will attempt retries up to 10 times over 48 hours.
    - Merchant will receive the webhook once the transaction has reached terminal status.
3. Autodebit: False, Retry Strategy: Custom
    - The merchant must manually call the debit API for each retry.
    - A callback is sent for every retry attempt.
    - The merchant can initiate up to 10 retries within 48 hours, ensuring a minimum interval of 1 hour between each attempt.

### Merchant Callbacks

- Pre-debit Notification Callback
    
    ```json
    {
      "type": "SUBSCRIPTION_NOTIFICATION_COMPLETED/SUBSCRIPTION_NOTIFICATION_FAILED",
      "payload": {
        "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855",
        "orderId": "OMO12344",
        "amount": 100,
        "state": "NOTIFIED",
        "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        }
      }
    }
    ```
    
- Callback for Redeemed State -
    - Order can be success & debit might be success/ failed.
    - Once order state is in completed, then no more retries allowed for debit. Reached terminal state.
    
    ```json
    {
      "type": "SUBSCRIPTION_REDEMPTION_ORDER_COMPLETED/SUBSCRIPTION_REDEMPTION_ORDER_FAILED",
      "payload": {
       "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855"
        "orderId": "OMO12344",
        "state": "COMPLETED",
        "amount": 100,
       "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        },
        "errorCode": <PRESENT ONLY IF STATE IS FAILED>
        "detailedErrorCode": <PRESENT ONLY IF STATE IS FAILED>  
        "paymentDetails": [
            {
                "amount": 100
                "paymentMode": "UPI_AUTO_PAY",
                "timestamp": 1620891733101      
                "transactionId": "OM124",
                "state": "COMPLETED", // FAILED, PENDING
                "rail": {
                    "type": "UPI",
                    "utr": "2",
                    "vpa": "abcd@ybl",
                    "umn": "544fcc8819d04cb08e26faa1fb07eee7@ybl"
                },
                "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXX2312",
                    "ifsc": "VISA",
                    "accountHolderName": "Venkat",
                    "accountType": "SAVINGS"
                },
                "errorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
               "detailedErrorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
            }
        ]
      }
    }
    ```
    
- Callback for Redemption Attempt State-
    - When order is in pending state & first/ past debit attempts are not successful.
    
    ```json
    {
      "type": "SUBSCRIPTION_REDEMPTION_TRANSACTION_COMPLETED/SUBSCRIPTION_REDEMPTION_TRANSACTION_FAILED",
      "payload": {
       "merchantId": "SWIGGY8",
        "merchantOrderId": "MO1708797962855"
        "orderId": "OMO12344",
        "state": "PENDING",
        "amount": 100,
       "expireAt": 1620891733101,
        "paymentFlow": {
          "type": "SUBSCRIPTION_REDEMPTION",
          "merchantSubscriptionId": "MS121312",
          "redemptionRetryStrategy": "CUSTOM",
          "autoDebit": true,
          "validAfter": "1628229131000",
          "validUpto": "1628574731000",
          "notifiedAt": "1622539751586"
        },
        "errorCode": <PRESENT ONLY IF STATE IS FAILED>
        "detailedErrorCode": <PRESENT ONLY IF STATE IS FAILED>  
        "paymentDetails": [
            {
                "amount": 100
                "paymentMode": "UPI_AUTO_PAY",
                "timestamp": 1620891733101      
                "transactionId": "OM124",
                "state": "COMPLETED", // FAILED, PENDING
                "rail": {
                    "type": "UPI",
                    "utr": "2",
                    "vpa": "abcd@ybl",
                    "umn": "544fcc8819d04cb08e26faa1fb07eee7@ybl"
                },
                "instrument": {
                    "type": "ACCOUNT",
                    "maskedAccountNumber": "XXX2312",
                    "ifsc": "VISA",
                    "accountHolderName": "Venkat",
                    "accountType": "SAVINGS"
                },
                "errorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
               "detailedErrorCode": <PRESENT ONLY IF ATTEMPT IS FAILED>
            }
        ]
      }
    }
    ```
    

### Mandate Cancel API

This API is used to cancel the registered mandates & In-progress mandates.

- “merchantSubscriptionId” is required to cancel the mandate. Even for registered/ In-progress mandates.

```json
curl --location --globoff --request POST 'https://api-preprod.phonepe.com/apis/pg-sandbox/subscriptions/v2/{merchantSubscriptionId}/cancel' \
--header 'Accept: application/json' \ ''
--header 'Authorization: O-Bearer 
```

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

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