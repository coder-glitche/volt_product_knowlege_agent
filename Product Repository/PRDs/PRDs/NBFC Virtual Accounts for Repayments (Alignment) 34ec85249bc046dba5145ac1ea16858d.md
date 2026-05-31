# NBFC Virtual Accounts for Repayments (Alignment)

: Gautam Mahesh
Created time: September 9, 2024 2:39 PM
Status: In progress
Last edited: November 27, 2024 4:59 PM

# **What problem are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

The problems can be further distilled into.

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted
- We want to handle large ticket repayments from customers more seamless, especially for MFD channels where transaction value exceeds 1L
- We want to handle repayments from accounts which otherwise might not be catered to by the 10-12 banks on Netbanking
- We want to ensure the repayment cost is kept to a minimum and hence the skip the cost of paying MDR for Netbanking/Debit Card to PG partners
- We want to receive the funds into our account directly from the borrower’s account without having an intermediary from a funds flow perspective

The above problems can be solved using virtual accounts stack. The detailed flow can be found in the solution section.

---

# **How do we measure success?**

Below are the metrics that will define our adoption.

- Number of transactions through virtual accounts
- Number of transactions per virtual account
- Number of unique customers transacting through virtual accounts

Below are the metrics we have from our existing flows.

![image.png](Yes%20bank%20e-collect%20API%20integration%20for%20virtual%20acc/image%201.png)

---

# **How are others solving this problem?**

Most of the lenders solve the problems of large ticket repayments in one of the below manner.

- Virtual accounts (VA) on top of lender’s account: use the VA stack to collect repayments on lender’s current account through an intermediary or
- Virtual accounts (VA) on top of PA’s account: the LSP creates virtual accounts with a payment aggregator which settles to the lender’s account in bulk
- Payment gateway: many lenders/LSP on behalf of lenders integrate with a PG to accept large ticket repayments

Some lenders have multiple virtual accounts used for various use case and tag the repayments accordingly. For example Bajaj has separate virtual accounts per customer for principal and interest payments. (Use case when they do not have a default apportionment logic).

Some lenders restrict the per transaction value that can be paid by the borrower to avoid quick run-off of their principal.

Below is a quick comparison of the above options.

| **Parameter** | **VA on Lender’s account** | **VA on PA’s account** | **PG** |
| --- | --- | --- | --- |
| Transaction limit on repayment | None | None | None |
| Payment methods powered | IMPS/NEFT/RTGS/UPI | IMPS/NEFT/RTGS/UPI | IMPS/NEFT/RTGS/UPI/Debit card |
| Customer bank coverage | Near-100% | Near-100% | Near-100% across instruments |
| Customer : upper transaction limits | - 1L for UPI
- 5L for IMPS
- None for NEFT/RTGS | - 1L for UPI
- 5L for IMPS
- None for NEFT/RTGS | - 1L for UPI
- 5L for IMPS
- None for NEFT/RTGS
- Upto 5L for debit card
- Upto 5L for Netbanking |
| Customer : lower transaction limits | - 1 for UPI/IMPS/NEFT
- 2L for RTGS | - 1 for UPI/IMPS/NEFT
- 2L for RTGS | - 1 for UPI/IMPS/NEFT/ debit card/ Netbanking
- 2L for RTGS |
| Funds Settlement latency | - Immediately for UPI/IMPS
- Up to 3 hours for NEFT/RTGS | T+1/2 irrespective of payment method | T+1/2 irrespective of payment method |
| Multi-bank support (DSP accounts) | - Yes. Through an intermediary
- Else, we need to integrate directly | Yes | Yes |
| Transaction cost | - ~1/transaction | - ~1/transaction | - ~1/transaction for UPI
- ~12/transaction for netbanking
- ~1200/transaction for debit card (VISA/Master) |
| Settlements on bank holidays/weekends | Yes | No | - Yes. Requires additional fee |
| Operational effort/transaction | - 0. If integrated fully through APIs
- ~5 minutes with offline flow | - 0. If integrated fully through APIs
- ~5 minutes with offline flow | - 0. If integrated fully through APIs
- ~5 minutes with offline flow |

It makes commercial sense for DSP to directly integrate with Yes-bank’s e-collect API and manage virtual accounts for customers 

---

# **What is the solution?**

## Requirements overview

The recommended solution is as below.

- DSP finalizes the list of banks to collect funds for repayments (Yes and Axis to start)
- DSP leverages the capabilities of an intermediary for the below capabilties.
    - Creating a virtual account
    - View transactions against a VA
    - Reconciliation with the underlying account
- DSP operations team will have the flexibility of choosing the underlying account
- DSP operations team shares the VA number with the customer upfront.

## Process flow

Below is the recommended process flow for accepting repayments through virtual accounts.

### Creating a virtual account

Below is the process for creating a virtual account.

- Loan booking happens at DSP’s end and account number is created on LMS
- Report needed from Analytics for the list of accounts created in a day
- Ops creates a VA in bulk through vendor dashboard
- VA creation confirmed by the vendor
- Ops shares the VA with the support/biz teams

<aside>
💡

Ops can whitelist the remitter bank account from vendor’s dashboard.

</aside>

### Transacting through a virtual account

Below is the process for transacting using a virtual account.

- Customer transfers funds to the VA from their bank account through one of the below methods.
    - IMPS
    - UPI
    - NEFT
    - RTGS
- Vendor confirms the transaction to the bank partner
- Funds flows into our Bank account
- Ops can login to vendor dashboard and see the transaction

<aside>
💡

As of now, remitter whitelisting isn’t recommended by default

</aside>

### Reconciling transactions

Below is the process for reconciling transactions.

- Ops downloads the transaction report from the vendor dashboard
- Ops reconciles the transactions with the bank account statement using UTR
- Ops uses the Maker checker to post manual repayments through command center
- Data is pushed to LMS after the checker approves the repayment on command center
- Customer’s TOS is adjusted as per the repayment strategy

## Pre-requisites

Below are the pre-requisites for DSP to use the VA stack.

- Finalize the Ecollect code with a bank partner (4/6 digit code prefix).
- Finalize the bank partner for collections (Yes followed by Axis).
- Close the agreement and commercials with the intermediary.
- Share the ecollect code as well as link the intermediary with the bank account

## User stories / User flow

Below are the user stories that will be covered by product.

- Create a virtual account when the loan is booked by hitting the vendor’s APIs
- Operations shares the virtual account with the customer for repayment
- Customer transfers funds into the VA using their preferred mode
- Transaction is settled to DSP’s bank account basis the method (NEFT/RTGS take time).
- Transaction is visible on the vendor’s dashboard including remitter details
- Operations downloads the transaction report from vendor’s dashboard.
- Operations reconciles the transactions from statement with the dashboard.
- Operations does a repayment maker of the transaction from CC - this is pending development.
- Operations does a repayment checker of the transaction from CC.
- Transaction is pushed to LMS as a repayment item.
- Customer can view the repayment line item on the app.

## Requirements

Below are the requirements from a product perspective.

- Virtual accounts (VA) to be created for each customer
- Customer can pay to the VA using any method of choice
- DSP has the option to reject a transaction if not from customer (optional)
- Customer should receive acknowledgement instantly
- DSP should receive the funds in the account within a minute for UPI/IMPS and 2 hours for NEFT/RTGS
- All transactions including reversals should be available on the dashboard

## Bank Integration Flow

Below is the list of integration items that need to be handled by DSP.

| **Item** | **Capability available at Bank** | **Comments** |
| --- | --- | --- |
| Create a virtual account | No | DSP will need to create a virtual account on its own using the 4/6 digit Ecollect code and build the complete VA number |
| Acknowledge the validate callback | Yes | DSP will need to confirm if we want the transaction from the remitter. If we reject, the funds are sent back to source |
| Acknowledge the notify callback | Yes | DSP will need to acknowledge the callback. Funds are credited to our account once this callback is received  |
| Account whitelisting | No | DSP will need to handle if we want to accept repayments from specific accounts |
| Transaction limits | No | DSP will need to handle any transaction limits of the repayment transaction |

## Build (Bank) vs. Buy (Vendor)

Below the are the points of evaluation of building in-house with a bank vs. using a vendor. (Bold is the preferred option).

| **Capability** | **Priority** | **Bank Rating** | **Vendor Rating**  |
| --- | --- | --- | --- |
| Settlement TAT  | High | **High (Immediate)** | **High (Immediate)** |
| Commercials | Medium | **High (no charges from bank)** | Medium (vendors charges fees) |
| Effort for integration | High | Low (each bank has integration effort) | **High (Low effort)** |
| Effort for support | High | Low (each bank has integration effort) | **High** |
| Ability to create VAs | High | Low (banks don’t offer this capability) | **High** |
| Ability to deactivate VAs | High | Low (banks don’t offer this capability) | **High** |
| Remitter whitelisting | Medium | Low (banks don’t offer this capability) | **High** |
| Transaction limits | Medium | Low (banks don’t offer this capability) | **High** |

Its recommended to use a vendor like Cashfree or a similar player if we are looking go live fast with low to no tech effort. However, if we are open to spending time and effort on integrating with each bank, we can integrate with each bank.

## Vendor Evaluation

Below the are the points of evaluation.

| **Item** | **Expectation** | **Priority** |
| --- | --- | --- |
| Banks Supported | Yes, Axis | Must Have |
| Connected banking (on DSP account) | Needs to be supported | Must Have |
| Ability to create VA through dashboard (single) | Ability to create VA by punching customer details | Must Have |
| Ability to create VA through dashboard (bulk) | Ability to create VA by uploading a list of customer details | Must Have |
| Transaction report through dashboard | Report/ view that has transaction detail | Must Have |
| Validate Webhook capability to DSP’s endpoints | Bank/vendor to trigger webhook for validate (accept or reject) | Must Have |
| Notify Webhook capability to DSP’s endpoints | Bank/vendor to trigger webhook for intimation of credit into account | Must Have |
| Remitter whitelisting | Ability to accept funds from a set of accounts only | Must Have |
| Auto-accept transactions | Ability to configure the capability to auto-accept transactions | Must Have |
| Callback TAT | <1 minute from transaction receipt | Must Have |
| Minimal parameters for creating a VA | Not more than 3 parameters. | Must Have |
| Deactivate a VA | Ability to deactivate a VA and incoming transactions getting rejected | Must Have |
| Reject a transaction for deactivated VA | Ability to deactivate a VA and incoming transactions getting rejected | Must Have |
| Dashboard with multi-user access |  | Must Have |
| Dashboard with role-based access |  | Must Have |
| Report format to have all details | Remitter name, Remitter bank account details/VPA, Payment method, Transaction timestamp, UTR, Amount, DSP bank account, VA | Must Have |
| Create VA commercials | 0 | Must Have |
| Transaction commercials | 1 per transaction | Must Have |
| Transaction controls | Not allow transactions < 10K (TBD) | Must Have |
| Commission debits | Postpaid or not from underlying account | Must Have |

Below are the points of evaluation across vendors.

| **Item** | **Cashfree** | **Razorpay** | **Decentro** |
| --- | --- | --- | --- |
| Banks Supported | - Yes
- Axis
- ICICI
- IDFC
- Kotak | - Yes
- Axis
- RBL
- IDFC | - Yes
- Axis
- IDFC |
| Connected banking (on DSP account) | Yes | Yes | Yes |
| Ability to create VA through dashboard (single) | Yes | Yes | Yes |
| Ability to create VA through dashboard (bulk) | Yes | Yes | No |
| Transaction report through dashboard | Yes | Yes | Yes |
| Validate Webhook capability to DSP’s endpoints | Yes | Yes | Yes |
| Notify Webhook capability to DSP’s endpoints | Yes | Yes | Yes |
| Remitter whitelisting | Yes | Yes | Yes |
| Auto-accept transactions | Yes | Yes | Yes |
| Callback TAT |  |  |  |
| Minimal parameters for creating a VA |  |  |  |
| Deactivate a VA |  |  |  |
| Reject a transaction for deactivated VA |  |  |  |
| Dashboard with multi-user access |  |  |  |
| Dashboard with role-based access |  |  |  |
| Report format to have all details |  |  |  |
| Create VA commercials |  |  |  |
| Transaction commercials |  |  |  |
| Transaction controls |  |  |  |
| Commission debits |  |  |  |

---

# **Design**

There’s no design involvement at this stage.

---

# **Analytics**

There’s no analytics involvement at this stage. However, we do intend to track the below items.

- Number of virtual accounts created
- Number of transactions through virtual accounts
- Number of transactions per virtual account
- Number of unique customers transacting through virtual accounts
- Transaction details like payment method, payer name, UTR, etc
- Transaction status like reversal, success, etc
- Transactions from account which don’t belong to the customer.
- Transactions from account which aren’t whitelisted or in our DB.
- Average transaction amount by payment method.

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
    - [ ]  Evaluate partners
    - [ ]  Evaluate banks (YBL, Axis)
    - [ ]  Finalize the product process
    - [ ]  Close commercials with partners
- [ ]  Operations
    - [ ]  Setup SOP for handling flows
- [x]  Design

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

Discussion with Nishant.

- Talk to YBL on their VA capabilities
- Take a demo from YBL on their dashboard capabilities.

Discussion with Cashfree (Rohit) - 16th Sep’24.

- Supports all leading banks.
- VA will become part of the PG product.
- Dashboard has capabilities to support creation of VAs as well as transaction download.
- No need for any tech involvement to go live.
- Commercials - TBD