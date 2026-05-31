# Yes bank e-collect API integration for virtual accounts

: Vaibhav Arora
Created time: November 27, 2024 4:56 PM
Status: Done
Last edited: January 20, 2026 3:53 PM

# **What problem are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

Problems are divided between two key stakeholders:

- NBFC (operations/business/product)
- Customers

NBFC 

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted (Reconciliation also becomes very tough as we will not be able to recognise the source of payments made directly to our collections account and its corresponding attribution to the loan account)
- We want to ensure the repayment cost is kept to a minimum and hence the skip the cost of paying MDR for Netbanking/Debit Card to PG partners
- We want to receive the funds into our account directly from the borrower’s account without having an intermediary from a funds flow perspective to avoid any settlement TAT and delays between accounts

Customer

- We want to handle large ticket repayments from customers more seamless, especially for MFD channels where transaction value exceeds 1L
- We want to handle repayments from accounts which otherwise might not be catered to by the 10-12 banks on Netbanking

---

# **How do we measure success?**

Below are the metrics that will define our adoption.

- Number of transactions through virtual accounts
- Number of transactions per virtual account
- Number of unique customers transacting through virtual accounts

Below are the metrics we have from our existing flows

![image.png](Yes%20bank%20e-collect%20API%20integration%20for%20virtual%20acc/image.png)

- Data
    
    ```sql
    select 
    transactions.transaction_id,
    credits.credit_id,
    transactions.amount,
    transactions.settled_on,
    transactions.description,
    transactions.transaction_type,
    transactions.long_description,
    CASE 
            WHEN long_description LIKE '%loan No - By%' THEN 1 
            ELSE 0 
        END AS va_transaction_flag,
    case
            when substr(platform_name, 1, 4) = 'Volt' and partner_account_type = 'INDIVIDUAL' then 'B2B2C'
            when substr(platform_name, 1, 4) != 'Volt' then 'B2B'
                else 'B2C' end as business_channel
    from transactions
    left join credits on credits.credit_id=transactions.credit_id
    left join VoltReportingDatabase.public.credit_applications_entity on credits.application_id=VoltReportingDatabase.public.credit_applications_entity.application_id
    left join VoltReportingDatabase.public.partner_accounts on VoltReportingDatabase.public.partner_accounts.account_id=VoltReportingDatabase.public.credit_applications_entity.partner_account_id
    left join VoltReportingDatabase.public.platform_accounts on VoltReportingDatabase.public.platform_accounts.account_id=VoltReportingDatabase.public.credit_applications_entity.platform_account_id
    where transaction_type='CREDIT'
    and description!='Credit'
    and year(cast(transactions.settled_on as date))=2024
    and month(cast(transactions.settled_on as date))>8
    and lending_partner_id='Bajaj'
    
    SELECT *
    FROM collections
    LEFT JOIN credits ON credits.credit_id = collections.credit_id
    WHERE collection_status = 'SETTLED'
      AND year(DATE(collections.created_on)) = 2024
      AND DATE(collections.created_on) > DATE('2024-07-28')
      AND lending_partner_id = 'Bajaj'
    ORDER BY collections.created_on DESC;
    ```
    
    [https://docs.google.com/spreadsheets/d/1IiX74jONHw6tRQH7LmYqdv-SAboQe9xwkTtNZoqXzc0/edit?gid=136488709#gid=136488709](https://docs.google.com/spreadsheets/d/1IiX74jONHw6tRQH7LmYqdv-SAboQe9xwkTtNZoqXzc0/edit?gid=136488709#gid=136488709)
    

![image.png](Yes%20bank%20e-collect%20API%20integration%20for%20virtual%20acc/image%201.png)

---

# **How are others solving this problem?**

Most of the lenders solve the problems of large ticket repayments in one of the below manner.

- Virtual accounts (VA) on top of lender’s account: use the VA stack to collect repayments on lender’s current account through an intermediary or
- Virtual accounts (VA) on top of PA’s account: the LSP creates virtual accounts with a payment aggregator which settles to the lender’s account in bulk
- Payment gateway: many lenders/LSP on behalf of lenders integrate with a PG to accept large ticket repayments

Some lenders have multiple virtual accounts used for various use case and tag the repayments accordingly. For example Bajaj has separate virtual accounts per customer for principal and interest payments. (Use case when they do not have a default apportionment logic).

Some lenders restrict the per transaction value that can be paid by the borrower to avoid quick run-off of their principal.

---

# **What is the solution?**

DSP will be integrating with Yes bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

Steps for accepting a VA payment:

- NBFC gets a e-collect code
- NBFC appends a unique reference number (for each loan) and shares the virtual account with the customer (total length has to be less than or equal to 28 characters where first 6 characters would be the e-collect code).
    - To make the bank account more readable, we can optimise the account number 
    
    Benchmarking: (Two possible ways alphanumeric and numeric)
        - Account number: VCKYCDSPFINA8072 (CKYC)
        IFSC code: IBKL0000011
        - Account number: 2223221499366062  (Clayo technologies)
        IFSC code: UTIB000RAZP
    
    <aside>
    💡
    
    IFSC Code: YESB0CMSNOC (Fixed from yes bank) 
    
    **Constraints:**
    
    - VAN will begin with a 6 digit e-collect code (unique to the NBFC) followed by a custom string
    - VAN has to be unique at a loan account level
    - VAN can be alphanumeric or numeric with a maximum length of 28 characters
    - It cannot start from 0,1,2,8, and 9.
    
    **Impact:**As per an analysis that we did, almost 10% repayments happen outside of the Volt platform (for BFL), a large chunk of which can be attributed towards virtual accounts. (out of a sample of 27k repayments in the last 3 months).
    
    **User flow:**
    
    Users when making a repayment via a virtual account can take two flows, making a repayment via adding the account as a beneficiary, or directly making the payment in the account (Quick pay/ UPI). **Findings:**
    
    - Based on a control research of 8 individuals, it was found that numeric bank accounts are more comfortable to users on user interfaces (6 out of 8 found alphanumeric bank accounts confusing).
    - Certain banks do not support transactions to alphanumeric banks
    - Adding a beneficiary flows on major banks (HDFC/SBI/Axis) and major UPI apps while making a transaction to a bank account support copying and pasting account number
    
    Given the following findings, we are moving with the following approach, please share feedback or queries on the same:
    
    VAN: {6 Digit e-collect code} + {Custom string}
    
    **6 digit e-collect code: (subject to availability)**
    
    345678Reasoning: Sequential numbers are easy to remember and type. Starting from 3 avoids disallowed digits and looks intuitive. It reduces cognitive load when copying.567890Reasoning: Sequential with a recognizable progression pattern. Includes mid-range digits, ensuring clarity and no confusion with boundaries like 0 or 9.
    
    **Custom string:**
    
    Zero starting with 7 numbers of user's loan account number (FXLAN**3432543**)
    
    VLAN: 3456780-3432543 (example)Reasoning:
    
    - By default unique at a loan level
    - Only numbers hence avoids confusion or possible banking errors
    - Easy for ops team to remember and verify when approving transactions or communicating to the user
    - No PII implications (Reasoning for not using user mobile number)
    </aside>
    
- Customer makes a repayment to the appended string (bank account number) and a shared IFSC code
- Yes bank then hits a validate API (REST JSON) (prepared by DSP) which can give three responses to yes bank:
    - Accept (payment is accepted funds are passed to the collection account of the NBFC)
    - Reject (payment is rejected, amount is refunded back to the source account of the user)
    - Pending (Yes bank will retry 4 additional times in every 3-4 minutes if it still gets pending for all three attempts, then it will keep retrying every 30 mins (for 24 hours)
    - Yes bank has a default behaviour for all transactions that are not approved or rejected we can either accept the payment by default or refund it back to the user (for now we will be refunding them back to the user) - For now we will be reversing the transaction back to the user if not confirmed as a default behaviour
- Once funds are received the NBFC will receive the corresponding callbacks in a subscribed URL

## Requirements overview (optional)

## User stories / User flow

- **Payment Initiation**:
    - A borrower initiates a loan repayment via NEFT, RTGS, IMPS, or UPI to a virtual account (VA) provided by Yes Bank.
- **Bank Notification to Validate API**:
    - Yes Bank detects the incoming payment and sends a **Validate API** request to your system.
    - When the validate API is hit for a repayment (Fenix will create a repayment request for the user)
    - Fenix will then send a callback for the corresponding repayment request to the LSP (so that they can record that as a transaction from the user). (Transaction request will move to pending checker approval)
    - The request contains transaction details, such as:
        - Remitter details (account number, IFSC, name, etc.).
        - Beneficiary details (VA number, IFSC, name, etc.).
        - Payment details (amount, timestamp, UTR, etc.).
        
        (Same will be recorded in our system)
- **Validation by Command Centre**:
When a repayment is made to a virtual account, yes bank hits us with a request on our validate API. This is when we will create a virtual account repayment request (similar to an order of PG)
Then we will validate the request, if it passes the sanity checks (as defined below) we will create a repayment request and send a callback to the LSP to update the status for a transaction

```sql
 -- Add callback structure here-- 
```

- Our Validate API processes the request and performs internal checks, such as:
    - Is the underlying account active or frozen (payment will get rejected automatically if the account is closed)
    - Is the VA mapped to a loan account (if not mapped, repayment will get rejected by default)
- Your system responds to Yes Bank with:
    - **`pass`**: Transaction is valid. (when maker checker is approved)
    - **`reject`**: Transaction is invalid (e.g.,invalid transaction). (when maker checker is rejected)
    - **`pending`**: Transaction requires further verification (Yes Bank retries every 30 minutes) for 24 hours.
- **Bank Action Based on Validate Response**:
    - **If `pass`**: Yes Bank credits the NBFC VA collection account.
    - **If `reject`**: Yes Bank stops processing the transaction.
    - **If `pending`**: Yes Bank retries validation as per the retry logic.
- **Notification to Notify API**:
    - Upon successful crediting of the VA, Yes Bank sends a **Notify API** request to your system.
    - The notification includes details of the credited transaction:
        - Beneficiary account details, transaction status, timestamp, and amount. (Upon receiving this request, I will post the transaction to the SOA, till then it will remain in pending_bank_confirmation)
- **System Updates Loan Account**:
    - Your system processes the notification and updates the borrower’s loan account:
        - Credits the payment against their outstanding loan balance.
        - Logs the transaction for reporting and reconciliation.

## Requirements

We need to provide Yes Bank with the endpoint URL and the expected JSON structure. 

```json
{
  "validate": {
    "customer_code": "TESTX1",
    "bene_account_no": "1234567890",
    "bene_account_ifsc": "YESB0CMSNOC",
    "bene_full_name": "John Doe",
    "transfer_type": "NEFT",
    "transfer_unique_no": "UTR123456789",
    "transfer_timestamp": "2024-11-27 10:30:00",
    "transfer_ccy": "INR",
    "transfer_amt": 5000.00,
    "rmtr_account_no": "9876543210",
    "rmtr_account_ifsc": "HDFC0123456",
    "rmtr_account_type": "CA",
    "rmtr_full_name": "Jane Doe",
    "rmtr_address": "Mumbai, India",
    "rmtr_to_bene_note": "Loan repayment",
    "attempt_no": 1
  }
}
```

Expected Response (from our API to Yes Bank):

Scenario (Pass / Reject / Pending)

```json
{
  "validateResponse": {
    "decision": "pass"
  }
}

{
  "validateResponse": {
    "decision": "reject",
    "reject_reason": "Invalid remitter details"
  }
}

{
  "validateResponse": {
    "decision": "pending"
  }
}
```

**Payment verification logic:**

For now our validation will be built on customer code (FXLAN) in future we can build validations on following use cases:

- Name verification with source account (Phase 2)
- Whitelisted bank account only (Phase 2)
- **Active loan accounts only (Phase 1)**

Notify API (callbacks):

Successful transaction: (When we receive the credited callback (repayment will be posted into the loan account) with the existing configured remarks and payment type as VA (for internal tracking and reconciliation)

(Corresponding callback needs to be sent to the LSP)

```json
{
  "notify": {
    "customer_code": "TESTX1",             // Unique code for your system.
    "bene_account_no": "1234567890",      // Virtual account number.
    "bene_account_ifsc": "YESB0CMSNOC",   // IFSC of the virtual account.
    "bene_full_name": "John Doe",         // Beneficiary's name (optional).
    "transfer_type": "NEFT",              // Payment method.
    "transfer_unique_no": "UTR123456789", // Unique transaction identifier.
    "transfer_timestamp": "2024-11-27 10:30:00", // Payment timestamp.
    "transfer_ccy": "INR",                // Currency.
    "transfer_amt": 5000.00,              // Payment amount.
    "rmtr_account_no": "9876543210",      // Remitter's account number.
    "rmtr_account_ifsc": "HDFC0123456",   // Remitter's IFSC.
    "rmtr_account_type": "CA",            // Remitter's account type (optional).
    "rmtr_full_name": "Jane Doe",         // Remitter's name.
    "rmtr_address": "Mumbai, India",      // Remitter's address (optional).
    "rmtr_to_bene_note": "Loan repayment", // Note from remitter (optional).
    "attempt_no": 1,                      // Retry attempt number (optional).
    "status": "CREDITED",                 // Transaction status.
    "credit_acct_no": "1234567890123",    // Virtual account credited.
    "credited_at": "2024-11-27 11:00:00"  // Time of credit.
  }
}
```

Returned direction: (When we receive this notification, status of the repayment request will get reversed). (Corresponding callback needs to be sent to the LSP)

```json
{
  "notify": {
    "customer_code": "TESTX1",
    "bene_account_no": "1234567890",
    "bene_account_ifsc": "YESB0CMSNOC",
    "bene_full_name": "John Doe",
    "transfer_type": "NEFT",
    "transfer_unique_no": "UTR123456789",
    "transfer_timestamp": "2024-11-27 10:30:00",
    "transfer_ccy": "INR",
    "transfer_amt": 5000.00,
    "rmtr_account_no": "9876543210",
    "rmtr_account_ifsc": "HDFC0123456",
    "rmtr_account_type": "CA",
    "rmtr_full_name": "Jane Doe",
    "rmtr_address": "Mumbai, India",
    "rmtr_to_bene_note": "Loan repayment",
    "attempt_no": 1,
    "status": "RETURNED",
    "credit_acct_no": "1234567890123",
    "returned_at": "2024-11-27 12:00:00"
  }
}
```

We will be storing the generated virtual account number for each loan against the loan entity, the same will be validated when a repayment is received from the loan account.

This virtual account number should can be taken via an API for the user. Will have to create a separate contract so that we can control the usage of the utility at an LSP and a partner level. 

LSP will be able to get the virtual account for the customer at an ad hoc basis and will be share the same with the customer. 

**Daily CRON (to expire maker checker tasks):**

When a repayment is under confirmation with Yes bank (they will keep polling our validate API) till a certain period. After the period, the checker becomes null and void, we will automatically reject the checker if it is not completed within a stipulated time.

CRON job will run at 10:00 AM in the morning, and will reject all pending checkers (For VA repayments) under the following logic:

- If the repayment request was made on T-1 before 12 PM (reject)
- if the repayment request was made on T-1 after 12 PM (ignore)

**Enhancements in repayment approval task:**

We will have to pass additional parameters (in case of virtual account repayments) in the checker approval, corresponding adjustments have been made in the approval tasks sheet

Ops agent will do the following checks:

- Match source bank account with customer bank account
- Match source bank IFSC with customer bank account
- Match source bank (associated customer name) with customer’s name
- Check if a repayment with the same bank reference number has not already been posted as a transaction

[https://docs.google.com/spreadsheets/d/1jVKAnJZUNI8VeihT4B6Wdtbletytx-wrLQOE8Dor3XM/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1jVKAnJZUNI8VeihT4B6Wdtbletytx-wrLQOE8Dor3XM/edit?gid=0#gid=0)

**Ops reporting for VA transactions and alerting:**

Ops team will need a report for tracking VA transactions, the report will be a daily report (for following transactions):

Reports:

- Approved transactions which are pending collection (callback is pending): Will be sent everyday at 6 PM for VA transactions which were approved but are pending collection confirmation from bank

Template: d-2fd8dcc81d054e31b567b12bc3202b95
Variable: {{date}}
- Rejected transactions which have not been reversed (callback is pending): Will be sent everyday at 6 PM for VA transactions which were rejected but are pending rejection confirmation from bank

Template: d-663fc03836f949e6ae2c8c3eec210145
Variable: {{date}}
- Pending approval transactions: will be sent everyday at 6 PM for VA transactions which were raised but have not been approved or rejected yet 

Template: d-9bdf0237aca3424ea39388a8d83cf9ca
Variable:{{date}}

[https://docs.google.com/spreadsheets/d/1MiRLPJicH1d6ZbnOjnvXT52ZaBKp3T5etmRwU1u3ucg/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1MiRLPJicH1d6ZbnOjnvXT52ZaBKp3T5etmRwU1u3ucg/edit?gid=0#gid=0)

Dependencies for LSPs (how should they handle these transactions on UI) - @Ameya Aglawe 

- LSPs will require an interface to show VAs which can be then used to make repayments by users to their loan accounts
- LSPs will have to handle three callbacks (VA payment completed pending checker approval, VA payment collected, VA payment reversed)

---

# **Design**

- Command centre (Ops agent should be share the virtual account of the customer via the command centre) - Loan details page (@Karuna Sankolli)
- Approval for transactions on command centre (via operations) (@Karuna Sankolli)
- LSP designs (to show users their VA) - Volt (@Ranjan kumar Singh @Ameya Aglawe)

---

# **Analytics**

- Number of VA repayment requests made @Vihari Kandian
- Number of VA repayments approved on CC
- Number of VA repayments collected successfully
- Number of VA repayments rejected on CC
- Number of VA repayments reversed successfully
- Number of VA repayments that were approved on CC but were reversed to customer (due to inability in approving on time)

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
    - [ ]  Finalize the Ecollect code - @Gautam Mahesh
    - [ ]  Close the indemnity letter - @Gautam Mahesh
- [ ]  Business
    - [ ]  
- [ ]  Tech
    - [ ]  Share the SRS sheet with YBL - @Vinay Vyas
    - [ ]  Share the APIs with YBL - @Vinay Vyas

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