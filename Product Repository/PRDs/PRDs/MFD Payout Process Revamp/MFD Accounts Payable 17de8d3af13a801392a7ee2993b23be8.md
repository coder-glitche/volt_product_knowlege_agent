# MFD Accounts Payable

# Problem Statements

- Lack of real-time tracking for partner account balances, requiring monthly queries.
- Payout delays due to missing or incorrect bank details from MFDs.
- No centralized tool for viewing MFD transactions and balances.
- MFDs receive payout details via Excel files instead of a dashboard display.

## Expected Impact

- Reduce manual calculations and offline payout verification.
- Minimize payout delays by removing reliance on Puneet.
- Mitigate risk of data loss from local file storage.
- Free up analytics team bandwidth from payout calculations.
- Simplify payout calculation review, monitoring, and approval.
- Provide MFDs with performance visibility to enhance motivation.
- Enable future payout-related features, such as processing fees based on credit limits.

# Proposed Solution

The solution will be implemented in phases:

1. **Foundation Tech:** Automate live commission tracking and accrual calculation.
2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard.

## Bank Accounts

1. **Volt Bank Account:**
    - A dedicated account for payout-related transactions.
    - **Future:** API integration for real-time payment status.
2. **MFD Bank Account:**
    - Collect bank details during registration.
    - Notify MFDs about missing or incorrect details via dashboard alerts.
    - Additional fields for verification:
        - Joint account status.
        - Separate "Company Name" and "Bank Account Holder's Name."

## Accounts Payable/Receivable

- **AP/AR Table** linked to partner IDs to track accruals and payouts.
- Automated accruals based on:
    - Partner activity.
    - Commercial agreements.
- Balances cleared upon payout.
- **Account Ledger** for a clear record of credits (accruals) and debits (payouts).

# Requirements

## 1. Registration Process

MFDs must provide:

- Bank details (Name, Type, Joint Account indicator).
- GSTN and Company Name.

## 2. Earnings Page

A redesigned "Earnings Page" will feature:

1. **Payout Overview:** Real-time accrual tracking.
2. **Statements:**
    - Downloadable Commission Statements and GST invoices (PDF).
    - Real-time transaction data for accuracy.
3. **GST Invoice Management:**
    - "Raise GST Invoice" button.
    - E-signable invoice generation and automatic upload.
    - Downloadable copy for records.
4. **Payout Triggering:**
    - Without GST: Manual trigger by Volt.
    - With GST: Automated monthly consolidated payout.

# Implementation Details

## Domain Entities

### Partner

- **Partner:** Commission-earning entity.
- **Partner Company:** Legal entity representation.
- **Partner Bank:** Settlement banking details.
- **Partner Commercials:** Commission structures.

### Commission

- **Accrual:** Earned, unsettled commission.
- **Commission Base:** Base amount for calculation.
- **Trail Commission:** Recurring AUM-based commission.
- **Upfront Commission:** One-time commission.

### Transactions

- **Settlement Batch:** Grouped transactions for payout processing.
- **UTR:** Unique Transaction Reference.
- **Settlement Status:** Current payout stage.

### Payment

- **Accounts Payable:** Pending obligations.
- **Payment Route:** Execution channel.
- **Payment Status:** Current state.

### Tax

- **Partner GSTN and TDS details.**

### Calculation

- **Partner Activity:** PF, Trail, Offers.
- **Slabs:** AUM-based payout rules.
- **Partner Invoices/Receipts:** GST invoices and commission statements.

## Database Schema (WIP)

### Partners Table

| Column Name | Data Type | Description |
| --- | --- | --- |
| partner_id | VARCHAR(36) | Unique identifier |
| partner_name | VARCHAR(255) | Legal name |
| bank_account_number | VARCHAR(50) | Account number |
| account_type | VARCHAR(50) | Account type |
| created_at | TIMESTAMP | Creation timestamp |
| updated_at | TIMESTAMP | Last update timestamp |

### Accrual Transactions Table

| Column Name | Data Type | Description |
| --- | --- | --- |
| accrual_id | VARCHAR(36) | Unique accrual ID |
| partner_id | VARCHAR(36) | Reference to partners table |
| month | DATE | Accrual month |
| avg_aum | DECIMAL(15,2) | Average AUM |
| total_commission | DECIMAL(15,2) | Total commission |
| gst_amount | DECIMAL(15,2) | GST amount |
| total_payout | DECIMAL(15,2) | Final payout amount |
| created_at | TIMESTAMP | Creation timestamp |

### Settlement Transactions Table

| Column Name | Data Type | Description |
| --- | --- | --- |
| settlement_id | VARCHAR(36) | Unique settlement ID |
| accrual_id | VARCHAR(36) | Reference to accrual_transactions |
| utr_number | VARCHAR(50) | UTR number |
| transaction_amount | DECIMAL(15,2) | Payment amount |
| transaction_status | VARCHAR(20) | Status (settled/pending) |
| created_at | TIMESTAMP | Creation timestamp |

## Dashboard Enhancements

| Feature | Current | Proposed |
| --- | --- | --- |
| Payout amount | In an Excel file at payout | Daily or application-level accrual display |
| Download Statement | XLSX, difficult to read | PDF, user-friendly |
| Apply for GST | Manual GST application | One-click e-sign and upload |
| Payout Transactions | Multiple transactions | One consolidated monthly payout |
| Instant Payouts | Not available | Instant payouts for certain offers |

# Next Steps

- Finalize database schema.
- Develop API integrations.
- Design and implement dashboard updates.
- Establish payout automation workflows.

# **Problem Statements**

- Inability to track the balance of a partner account. As we run monthly queries to check Monthly balances.
- Delays in payouts due to incorrect or missing bank details from MFDs (Mutual Fund Distributors).
- Lack of tools to view MFD transactions and account balances at a glance.
- MFDs cannot view their payout details on the dashboard; payouts are communicated via Excel files on the day of payment.

**Expected Impact** 

- Reduced Dependency on manual Calculation and Offline processing an verifying payout calculations on a monthly basis.
- Reduced Risk of Payout delays as the The current process is Dependent on Puneet
- Reducing risk of Data loss as Calculation and Files are stored on Puneet’s device.
- Free up analytics team bandwidth from payout calculations
- Simplify the Payout calculation Review and monitoring and approval from current manually verifying each GST invoice
- Provide MFD with Visibility on their performance and act as more motivation
- Allow Us to plan more Payout related features like paying processing fees as a Percentage of Credit limit.

# **Proposed Solution**

To address these issues, the solution will be phased:

1. Build foundational tech to show live commission amounts and automate accrual tracking.
2. Redesign the UI to improve MFDs' experience by integrating these new features.

### **Bank Accounts**

1. **Volt Bank Account**
    - Create a dedicated account for all payout-related transactions.
    - **V2:** Explore API integration for real-time payment status updates.
2. **MFD Bank Account**
    - Promptly collect bank account details during MFD registration.
    - Notify MFDs via the dashboard if details are incomplete or incorrect.
    - Add features for:
        - Indicating whether the account is joint.
        - Separating fields for "Company Name" and "Bank Account Holder's Name" for verification purposes (BAV).

## **Accounts Payable/Receivable**

- Build an **AP/AR Table** linked to partner IDs to track accruals and payouts.
- Automatically accrue amounts to the "Accounts Payable" table based on:
    - Partner activity.
    - Partner commercial agreements.
- Clear the accrued balance in the Accounts Payable table upon payout.
- Provide a detailed **Account Ledger** displaying all credits (accruals) and debits (payouts).

# **Requirements**

## **1. Registration Process**

- MFDs must:
    - Add bank details, including:
        - Bank Name.
        - Account Type (e.g., Savings, Current).
        - Joint Account indicator.
    - Add GSTN and Company Name.

## **2. Earnings Page**

- An enhanced "Earnings Page" will provide:
    1. **Payout Overview:**
        - Real-time display of payout amounts accrued.
    2. **Statements:**
        - Option to download Commission Statements and GST invoices in PDF format.
        - Pull the transactions in Real-time querying from the database for accuracy.
    3. **GST Invoice Management:**
        - A "Raise GST Invoice" button next to the payout amount.
        - Upon clicking, a modal opens to:
            - Generate an e-signable invoice.
            - Automatically upload the GST invoice after signing.
            - Download a user copy for MFD records.
    4. **Payout Triggering:**
        - Without GST: - Manually Triggered Payout from Volt
        - With GST:- Once GST requirements are addressed (e.g., uploading invoices), the payout is consolidated into a single monthly payment.

## Implementation Details

Tentative Database schema for tracking partner transactions from accrual to settlement, including commission calculations and payment processing.

**Domain Entities** 

Partner

- **Partner:** An entity that earns commissions through business activities
- **Partner Company:** Legal entity representing the partner
- **Partner Bank:** Banking details for settlements
- **Partner Commercials:** Agreed-upon commission structures

Commission

- **Accrual:** Earned but unsettled commission
- **Commission Base:** Amount on which commission is calculated
- **Trail Commission:** Recurring commission based on AUM
- **Upfront Commission:** One-time commission on new business

Transactions

- Settlement Batch: Group of transactions for processing
- UTR: Unique Transaction Reference for payments
- Settlement Status: Current state of settlement process

Payment 

- Accounts Payable: Pending payment obligations
- Payment Route: Channel for executing payments
- Payment Status: Current state of payment

TAX

- Partner GSTN details
- Partner TDS details

Calculation 

- Partner activity: PF,Trail,Offers
- Slabs: AUM based rules for payout calculation
- Partner Invoices /Receipts :- GST invoices and Commission statement

A transaction is initiated with the partner’s bank, linked to the partner company and partner account. This transaction is based on partner activity, calculated using the agreed commercial terms and tax details. Initially, it is recorded as an entry in the partner’s accounts payable. The settlement details, including invoices, receipts, and UTRs, are then saved for reference.

![MFD channel  (1).png](MFD%20Accounts%20Payable/MFD_channel__(1).png)

## Database Tables (WIP)

### 1. Partners Table partners

| Column Name | Data Type | Constraints | Description |
| --- | --- | --- | --- |
| partner_id | VARCHAR(36) | PRIMARY KEY | Unique identifier for partner |
| partner_name | VARCHAR(255) | NOT NULL | Legal name of partner entity |
| Partner_Company_name |  |  |  |
| Partner_Bank_name |  |  |  |
| Partner_Bank_account_number | VARCHAR(50) |  | Partner's bank account number |
| Partner_Bank_account_Type | VARCHAR(50) |  | Type of partner account |
| created_at | TIMESTAMP | DEFAULT NOW() | Record creation timestamp |
| updated_at | TIMESTAMP | ON UPDATE | Last modification timestamp |

### 2. Accrual Transactions Table (accrual_transactions)

| Column Name | Data Type | Constraints | Description |
| --- | --- | --- | --- |
| accrual_id | VARCHAR(36) | PRIMARY KEY | Unique identifier for accrual record |
| partner_id | VARCHAR(36) | FOREIGN KEY | Reference to partners table |
| financial_year | VARCHAR(9) | NOT NULL | Financial year of transaction |
| month | DATE | NOT NULL | Month of accrual |
| new_credit_lines | INT |  | Number of new credit lines |
| total_credit_lines | INT |  | Total number of credit lines |
| avg_aum | DECIMAL(15,2) |  | Average Assets Under Management |
| upfront_amount | DECIMAL(15,2) |  | Upfront commission amount |
| trail_amount | DECIMAL(15,2) |  | Trail commission amount |
| total_commission | DECIMAL(15,2) |  | Total commission (upfront + trail) |
| offer_amount | DECIMAL(15,2) |  | Special offer amount if applicable |
| gst_amount | DECIMAL(15,2) |  | GST amount |
| tds_amount | DECIMAL(15,2) |  | TDS amount |
| total_payout | DECIMAL(15,2) |  | Final payout amount |
| agreement_rate | DECIMAL(6,2) |  | Agreed commission rate |
| base_rate | DECIMAL(6,2) |  | Base rate for calculations |
| payout_rate | DECIMAL(6,2) |  | Actual payout rate |
| payout_base | DECIMAL(15,2) |  | Base amount for payout calculation |
| category | VARCHAR(50) |  | Transaction category |
| reason_for_payment | VARCHAR(100) |  | Payment reason/description |
| frequency | VARCHAR(20) |  | Payment frequency (monthly/quarterly) |
| created_at | TIMESTAMP | DEFAULT NOW() | Record creation timestamp |

### 3. Settlement Transactions Table (settlement_transactions)

| Column Name | Data Type | Constraints | Description |
| --- | --- | --- | --- |
| settlement_id | VARCHAR(36) | PRIMARY KEY | Unique identifier for settlement |
| transaction_id | VARCHAR(50) | NOT NULL | External transaction reference |
| accrual_id | VARCHAR(36) | FOREIGN KEY | Reference to accrual_transactions |
| utr_number | VARCHAR(50) |  | UTR number from bank |
| transaction_amount | DECIMAL(15,2) |  | Actual payment amount |
| payment_date | DATE |  | Date of payment |
| credit_account_number | VARCHAR(50) |  | Recipient account number |
| bank_ref_number | VARCHAR(50) |  | Bank reference number |
| bank_narrative | TEXT |  | Bank transaction narrative |
| transaction_status | VARCHAR(20) |  | Status (settled/pending/failed) |
| debit_account_name | VARCHAR(255) |  | Source account name |
| credit_account_holder_name | VARCHAR(255) |  | Recipient account holder name |
| type_of_payment | VARCHAR(50) |  | Payment type classification |
| remarks | TEXT |  | Additional remarks |
| actionables | TEXT |  | Required actions if any |
| created_at | TIMESTAMP | DEFAULT NOW() | Record creation timestamp |

### 4. Tax Details Table (tax_details)

| Column Name | Data Type | Constraints | Description |
| --- | --- | --- | --- |
| tax_id | VARCHAR(36) | PRIMARY KEY | Unique identifier for tax record |
| accrual_id | VARCHAR(36) | FOREIGN KEY | Reference to accrual_transactions |
| gst_transaction_id | VARCHAR(50) |  | GST transaction reference |
| gst_amount | DECIMAL(15,2) |  | GST amount |
| gst_remarks | TEXT |  | GST-related remarks |
| tds_transaction_id | VARCHAR(50) |  | TDS transaction reference |
| tds_amount | DECIMAL(15,2) |  | TDS amount |
| tds_remarks | TEXT |  | TDS-related remarks |
| created_at | TIMESTAMP | DEFAULT NOW() | Record creation timestamp |

## Relationships

1. `partners` to `accrual_transactions`: One-to-Many
    - A partner can have multiple accrual transactions
    - Each accrual transaction belongs to one partner
2. `accrual_transactions` to `settlement_transactions`: One-to-Many
    - An accrual can have multiple settlement transactions
    - Each settlement transaction relates to one accrual
3. `accrual_transactions` to `tax_details`: One-to-One
    - Each accrual transaction has one tax detail record
    - Each tax detail record belongs to one accrual transaction

## 

## Dashboard

- The MFD should be able to see there earning in the Partner portal

- The MFD should be able to see the
- 

| Feature  | Current  | Proposed |
| --- | --- | --- |
| Payout amount | In the Excel file created at the time of payout  | The Commission accrued amount displayed on the dashboard , updated on a Daily or Application level |
| Download Statement | XLXS file , hard to understand  | PDF file, easy to read  |
| Apply for GST | Have valid GSTN | Click on Apply for GST or Send GST invoice, E-sign and upload to the portal and MFD gets a copy  |
| Payout Transaction | Multiple transaction for Payouts, offers, GST | One payout per month inclusive of all payments |
| Instant payouts | Not available  | Ability to payout Instantly for some offers  |
|  |  |  |
|  |  |  |

# 

calculation file ,