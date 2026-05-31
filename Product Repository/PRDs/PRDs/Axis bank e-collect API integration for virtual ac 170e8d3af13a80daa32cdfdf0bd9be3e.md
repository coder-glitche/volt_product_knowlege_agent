# Axis bank e-collect API integration for virtual accounts

: Vaibhav Arora
Created time: January 3, 2025 12:56 PM
Status: Done
Last edited: January 5, 2025 1:42 PM

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

DSP will be integrating with Axis bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

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
    
    IFSC Code: UTIB0CCH274 (Fixed from yes bank)
    
    **Constraints:**
    
    - VAN will begin with a 4 digit e-collect code (unique to the NBFC) followed by a custom string
    - VAN has to be unique at a loan account level
    - VAN can be alphanumeric or numeric with a maximum length of 15 characters
    - It cannot start from 0, and 9.
    
    **Impact:**As per an analysis that we did, almost 10% repayments happen outside of the Volt platform (for BFL), a large chunk of which can be attributed towards virtual accounts. (out of a sample of 27k repayments in the last 3 months).
    
    **User flow:**
    
    Users when making a repayment via a virtual account can take two flows, making a repayment via adding the account as a beneficiary, or directly making the payment in the account (Quick pay/ UPI). **Findings:**
    
    - Based on a control research of 8 individuals, it was found that numeric bank accounts are more comfortable to users on user interfaces (6 out of 8 found alphanumeric bank accounts confusing).
    - Certain banks do not support transactions to alphanumeric banks
    - Adding a beneficiary flows on major banks (HDFC/SBI/Axis) and major UPI apps while making a transaction to a bank account support copying and pasting account number
    
    Given the following findings, we are moving with the following approach, please share feedback or queries on the same:
    
    VAN: {4 Digit e-collect code} + {Custom string}
    
    **4 digit e-collect code: (subject to availability)**
    
    **Custom string:**
    
    Zero starting with 8 numbers of user's loan account number (FXLAN**34325433**)
    
    VLAN: 1234-34325343 (example) Reasoning:
    
    - By default unique at a loan level
    - Only numbers hence avoids confusion or possible banking errors
    - Easy for ops team to remember and verify when approving transactions or communicating to the user
    - No PII implications (Reasoning for not using user mobile number)
    </aside>
    
- Customer makes a repayment to the appended string (bank account number) and a shared IFSC code
- Axis bank then hits a validate API (REST JSON) (prepared by DSP) which can give two responses to yes bank:
    - Accept (payment is accepted funds are passed to the collection account of the NBFC)
    - Reject (payment is rejected, amount is refunded back to the source account of the user)
    - 400 (Axis bank will retry for 4 minutes till they get a terminal status from request)
    
    - Axis bank has a default behaviour for all transactions that are not approved or rejected we can either accept the payment by default or refund it back to the user (for now we will be refunding them back to the user) - For now we will be reversing the transaction back to the user if not confirmed as a default behaviour
- Once funds are received the NBFC will receive the corresponding callbacks in a subscribed URL

## Requirements overview (optional)

## User stories / User flow

- **Payment Initiation**:
    - A borrower initiates a loan repayment via NEFT, RTGS, IMPS, or UPI to a virtual account (VA) provided by Axis Bank.
- **Bank Notification to Validate API**:
    - Axis Bank detects the incoming payment and sends a **Validate API** request to your system.
    - When the validate API is hit for a repayment (Fenix will create a repayment request for the user)
    - Fenix will then send a callback for the corresponding repayment request to the LSP (so that they can record that as a transaction from the user). (Transaction request will move to pending checker approval)
    - The request contains transaction details, such as:
        - Remitter details (account number, IFSC, name, etc.).
        - Beneficiary details (VA number, IFSC, name, etc.).
        - Payment details (amount, timestamp, UTR, etc.).
        
        (Same will be recorded in our system)
- **Validation by Command Centre**:
When a repayment is made to a virtual account, Axis bank hits us with a request on our validate API. Fenix will validate the request basis some checks:
    - Does an account number exist (last 8 digits) of VAN, pass if exists else fail the request with reason reject
    - If an account exists its status should be either “Active” or “Frozen”, if the account is closed, fail the request with reason reject
    - Does the remitter bank account number and IFSC code is the same as the one stored with us (bank account associated with the user’s client) if yes accept, if no,
        - Does the remitter name match with the client associated with the loan account number: Use Digio’s name verification API, if score is 90 and above (Pass) else (Reject).
        
        ![image.png](Axis%20bank%20e-collect%20API%20integration%20for%20virtual%20ac/image.png)
        

- Once a request is validated, we will wait for a notify calllback for the repayment. Once we get the notify callback, an approval task will be created for the Operations team to verify the repayment. Once verified and approved, posting will be done for the user’s loan account.

![image.png](Axis%20bank%20e-collect%20API%20integration%20for%20virtual%20ac/image%201.png)

<aside>
⚠️

For launch, we will not be building rejection (automated payouts) back to the user however if enough volume and a strong use case is observed, we will handle the same

</aside>

## Requirements

Yes bank request parameters:

| **Field** | **Parameter Name** | **Parameter Type** | **M/O** | **Details** |
| --- | --- | --- | --- | --- |
| Identifier | Appl_User_ID | Integer(50) not null | M | Checksum key + userID Key is given below |
| Request UUID | Req_id | Char(50) not null | M | Unique ID for each request |
| Request Details | Req_dtls | Char(100) not null | M | Each parameter is separated by | (UTR | Bank account | Customer name) |
| Request DateTime | Req_dt_time | Char(20) not null | M | YYYY-MM-DD HH24:MI:SS |
| Corporate code | Corp_code | Char(10) not null | M | Each corporate code will be shared and the same must be populated for requests. |

```json
Sample Request body:

{
    "Appl_User_ID": 12345678,
    "Req_id": "REQ-UUID-123e4567-e89b-12d3-a456-426614174000",
    "Req_dtls": "UTR123456789|234234234343|Vaibhav Arora",
    "Req_dt_time": "2025-01-05 14:30:45",
    "Corp_code": "CORP123456"
}
```

Expected Response (from our API to Axis Bank):

| **Field** | **Parameter Name** | **Parameter Type** | **M/O** | **Details** |
| --- | --- | --- | --- | --- |
| Identifier | Appl_User_ID | Integer(50) not null | M | Hash code/Checksum key + userID Key |
| Request UUID | Req_id | Char(50) not null | M | Unique ID for each request |
| Request Details | Req_dtls | Char(100) not null | M | Each parameter is separated by “ |
| Status Flag | Stts_flg | Char(2) not null | M | Y - Success, F - Failed |
| Corporate code | Corp_code | Char(10) not null | M | Each corporate code will be shared and the same must be populated for requests. |
| Error Code | Err_cd | Char(5) | O | Error code will be provided in case any error occurs |
| Error Description | Err_desc | Char(50) | O | Error description details |

Response parameters:

```json
Sample success response:
{
    "Appl_User_ID": 12345678,
    "Req_id": "VAL-20250105-001",
    "Req_dtls": "UTR123456789|",
    "Stts_flg": "Y",
    "Corp_code": "1234"
}

Sample fail response:
{
    "Appl_User_ID": 12345678,
    "Req_id": "VAL-20250105-001",
    "Req_dtls": "UTR123456789|",
    "Stts_flg": "F",
    "Corp_code": "1234",
    "Err_cd": "E001",
    "Err_desc": "Invalid UTR number"
}
```

| Error scenario | Error code | Error description |
| --- | --- | --- |
| Loan account number does not exist | E001 | Transaction made to an invalid loan account |
| Loan account number closed | E002 | Transaction made to a closed loan account |
| Bank account verification and name verification both failed | E003 | Transaction made from an unauthorised bank account |

Notify API (callbacks):

Successful transaction: (When we receive the credited callback (repayment will be posted into the loan account) with the existing configured remarks and payment type as VA (for internal tracking and reconciliation)

| **Field** | **Parameter Name** | **Parameter Type** | **M/O** | **OTC-O NEFT-N RTGS-R** | **Details** |
| --- | --- | --- | --- | --- | --- |
| Identifier | Appl_User_ID | Integer(50) not null | M |  | Hash code/Checksum key + userID Key |
| Request UUID | Req_id | Char(50) not null | M |  | Unique ID for each request |
| Transaction No | txn_nmbr | Char(30) not null | M |  |  |
| Request DateTime | Req_dt_time | Char(20) not null | M |  | YYYY-MM-DD HH24:MI:SS |
| Corporate code | Corp_code | Char(10) not null | M |  | Each corporate code will be shared and the same must be populated for requests. |
| Transaction Amount | Txn_amnt | Number(16,4) | M |  | Decimal allowed |
| PaymentMode | pmode | Char(1) not null | M |  | Default “2” |
| Transaction Date | Chq_date | Char(10) | O | N/A if Nor R | YYYY-MM-DD |
| UTR Number | Chq_nmbr | Char(10) | O | N/A if Nor R | Numeric |
| Payment Flag | Stts_flg | Char(3) | M |  | “000” - success“111” - failed |

```json
Request

{
    "Appl_User_ID": "Integer(50)",   // Mandatory - Checksum key + userID
    "Req_id": "Char(50)",           // Mandatory - Unique ID for each request
    "txn_nmbr": "Char(30)",         // Mandatory - Transaction number
    "Req_dt_time": "Char(20)",      // Mandatory - YYYY-MM-DD HH24:MI:SS
    "Corp_code": "Char(10)",        // Mandatory - Corporate code shared by bank
    "Txn_amnt": "Number(16,4)",     // Mandatory - Amount with up to 4 decimal places
    "pmode": "Char(1)",            // Mandatory - Default "2"
    "Chq_date": "Char(10)",        // Optional - YYYY-MM-DD (N/A for NEFT/RTGS)
    "Chq_nmbr": "Char(10)",        // Optional - Numeric (UTR number, N/A for NEFT/RTGS)
    "Stts_flg": "Char(3)"          // Mandatory - "000"=success, "111"=failed
}

Sample request (Success): Create approval task for CC

{
    "Appl_User_ID": 12345678,
    "Req_id": "CONF-20250105-001",
    "txn_nmbr": "TXN123456",
    "Req_dt_time": "2025-01-05 14:30:45",
    "Corp_code": "1234",
    "Txn_amnt": 1000.00,
    "pmode": "2",
    "Chq_date": "2025-01-05",
    "Chq_nmbr": "UTR987654321",
    "Stts_flg": "000"
}

Sample request (fail): Throw alert

{
    "Appl_User_ID": 12345678,
    "Req_id": "CONF-20250105-001",
    "txn_nmbr": "TXN123456",
    "Req_dt_time": "2025-01-05 14:30:45",
    "Corp_code": "1234",
    "Txn_amnt": 1000.00,
    "pmode": "2",
    "Chq_date": "2025-01-05",
    "Chq_nmbr": "UTR987654321",
    "Stts_flg": "111"
}

```

Response:

| **Field** | **Parameter name** | **Parameter Type** | **M/O** | **Details** |
| --- | --- | --- | --- | --- |
| Identifier | Appl_User_ID | Integer(50) not null | M | Checksum key+ userid Key is given below |
| Request UUID | Req_id | Char(50) not null | M | Unique id for each request |
| Transaction Id | txn_id | char(30) not null | M | A unique txn id will be provided |
| YTS Unique ID | Clt_txn_id | Char(30) not null | M | YTS's Unique confirmation number |
| Corporate code | Corp_code | Char(10) not null | M | Each corporate code will be shared and same to be populated while sending for request. |
| Successflag | Stts_flg | Char(5) | M | 000- success "111"- Failed |
| ErrorCode | Err_cd | Char(5) | O | Error Code will be provided in case any error is occurred |
| Error Description | Err_desc | Char(50) | O | Error description details |

There are no scenarios here as the tranasction is valid, however if the approval task creation fails, we need to send the following response:

| Error scenario | Error code | Error description |
| --- | --- | --- |
| Failed to create an approval task post notify callback | E004 | Failure in processing repayment request |

```json
{
    "Appl_User_ID": "Integer(50)",   // Mandatory - Same as request
    "Req_id": "Char(50)",           // Mandatory - Same request ID
    "txn_id": "Char(30)",           // Mandatory - Unique transaction ID provided by bank
    "Clt_txn_id": "Char(30)",       // Mandatory - YTS's Unique confirmation number
    "Corp_code": "Char(10)",        // Mandatory - Same corporate code
    "Stts_flg": "Char(5)",          // Mandatory - "000"=success, "111"=failed
    "Err_cd": "Char(5)",            // Optional - Error code if any error occurred
    "Err_desc": "Char(50)"          // Optional - Error description details
}

Success response object:
{
    "Appl_User_ID": 12345678,
    "Req_id": "CONF-20250105-001",
    "txn_id": "AXIS123456789",
    "Clt_txn_id": "YTS987654321",
    "Corp_code": "1234",
    "Stts_flg": "000"
}

Failure response object:
{
    "Appl_User_ID": 12345678,
    "Req_id": "CONF-20250105-001",
    "txn_id": "AXIS123456789",
    "Clt_txn_id": "YTS987654321",
    "Corp_code": "1234",
    "Stts_flg": "111",
    "Err_cd": "E004",
    "Err_desc": "Failure in processing repayment request"
}
```

We will be storing the generated virtual account number for each loan against the loan entity, the same will be validated when a repayment is received from the loan account.

This virtual account number should can be taken via an API for the user. Will have to create a separate contract so that we can control the usage of the utility at an LSP and a partner level. 

LSP will be able to get the virtual account for the customer at an ad hoc basis and will be share the same with the customer. 

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

[https://docs.google.com/spreadsheets/d/1MiRLPJicH1d6ZbnOjnvXT52ZaBKp3T5etmRwU1u3ucg/edit?gid=0#gid=0](https://docs.google.com/spreadsheets/d/1MiRLPJicH1d6ZbnOjnvXT52ZaBKp3T5etmRwU1u3ucg/edit?gid=0#gid=0)

### Callbacks to LSP:

![image.png](Axis%20bank%20e-collect%20API%20integration%20for%20virtual%20ac/image%202.png)

```json
Payment received:
{
    "transactionId": "string",
    "utrNumber": "string",
    "amount": "number",
    "timestamp": "ISO8601 datetime",
    "status": "RECEIVED",
    "postingStatus": "PENDING",
    "paymentDetails": {
        "remitterName": "string",
        "remitterAccount": "string",
        "remitterBank": "string",
        "remitterName":"Vaibhav Arora",
        "paymentMode": "NEFT/RTGS",
        "receivedAt": "ISO8601 datetime"
    }
}

Payment rejected:
{
    "transactionId": "string",
    "utrNumber": "string",
    "amount": "number",
    "timestamp": "ISO8601 datetime",
    "status": "REJECTED",
    "reversalStatus": "PENDING",
    "rejectionReason": "string",
    "paymentDetails": {
        "remitterName": "string",
        "remitterAccount": "string",
        "remitterName":"Vaibhav Arora",
        "remitterBank": "string",
        "paymentMode": "NEFT/RTGS",
        "rejectedAt": "ISO8601 datetime"
    }
}

Payment posted:

{
    "transactionId": "string",
    "utrNumber": "string",
    "amount": "number",
    "timestamp": "ISO8601 datetime",
    "status": "COMPLETED",
    "postingStatus": "SUCCESS",
    "loanDetails": {
        "loanAccountNumber": "string",
        "postedAmount": "number",
        "postedAt": "ISO8601 datetime",
        "postingReference": "string"
    }
}

Payment reversed:
{
    "transactionId": "string",
    "utrNumber": "string",
    "amount": "number",
    "timestamp": "ISO8601 datetime",
    "status": "REVERSED",
    "reversalStatus": "COMPLETED",
    "reversalDetails": {
        "reversalReference": "string",
        "reversalAmount": "number",
        "reversedAt": "ISO8601 datetime",
        "rejectionCode":"Error code",
        "originalRejectionReason": "Error description"
    }
}
```

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
- [ ]  Business
    - [ ]  
- [ ]  Tech
    - [ ]  Share the SRS sheet with Axis Bank - @Vinay Vyas

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