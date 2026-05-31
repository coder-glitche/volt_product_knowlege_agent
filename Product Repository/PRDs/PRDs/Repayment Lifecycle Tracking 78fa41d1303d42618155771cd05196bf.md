# Repayment Lifecycle Tracking

: Vaibhav Arora
Created time: February 26, 2024 8:24 AM
Status: Not started
Last edited: July 22, 2024 10:29 AM
Owner: Vaibhav Arora
Tasks: Repayment, Lien removal , Loan foreclosure life cycle tracking (https://app.notion.com/p/Repayment-Lien-removal-Loan-foreclosure-life-cycle-tracking-501062868b8743339c5c748394887fe5?pvs=21)

# What problem are we solving?

- Users currently are not able to see the status of their transactions once a repayment is done till it is settled by the lender in their statement of accounts.
    - Users are not able to see the updated credit limit and the transaction and want to know the status of the transaction.
        - Payment takes 1-2 days to get updated in the loan account (Then it gets visible to the user)
    - This makes them follow up with our Ops/Support teams via support channels to confirm if their payment was received by us.
    - This consumes a lot of time for the support team and is creating a bandwidth crunch.

**Exhibit A:**

![Untitled](Repayment%20Lifecycle%20Tracking/Untitled.png)

---

# How do we measure success?

- Number of tickets enquiring about the status of their repayment transaction (zendesk) / total repayments

---

# What is the solution?

We are solving this problem for the user by the following ways:

- Add a pending transaction in transactions section with status in progress till the time it is settled by the lender (transactions section - ledger)
    - [**Transaction status management**](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- On payment success screen in the flexi pay screen, communicate to the user the steps and timeline for the settlement with the lender.
    - [UI and cases that need to be handled](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
    - [Accounting and Settlement](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- Actively sharing the status of the transaction made by the user (Transaction Success/ Transaction settled) on UI and via WhatsApp and Email to the user.
    - [User Comms](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- Reporting
    - Flagging cases to Ops where unsettled payments are not automatically settled, so that they can be raised to BFDL for settlement
    - [Reporting (Internal analytics + Ops flags and ticket creation)](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)

# Requirements Overview:

### **Transaction status management**

- As soon as the user makes the transaction, we will start showing the repayment amount in the transactions tab to the user.
- User will be able to click on the transaction and see the status and description of the current sheet in the payment detail screen.
    - Two states of transactions (Pending will only be visible when there are pending payments yet to settle with the lender).
    - Default state should be visible otherwise.

### UI and cases that need to be handled

- While the user makes the transaction, we will show that we have successfully received the user’s transaction and that it may take a couple of days for the transaction to settle with the lender (Bajaj). 
We will be following the following logic to show the expected transaction settlement day:
    - Payment time before 6 PM (on a lender working day), Expected settlement date (Day of transaction after D0).
    - Payment time after 6 PM (on a lender working day), Expected settlement date (Next working day of transaction after D0).
    - Payment time before 9 PM (on a lender holiday), Expected settlement date (Next working day for the lender after D0).
    - Payment time after 9 PM (on a lender holiday), Expected settlement date (Next working day for the lender after D0+1)
- Notification banner to be shown stating repayment transaction in progress, will get automatically removed after 2 days, user can continue to track settlement status in transactions ledger.

### Accounting and Settlement

- We will keep polling the statement of the account API by Bajaj to see transactions in the user’s loan account while maintaining repayments in a proxy pending state in our system.
    - Frequency of polling needs will be every 30 minutes till T+4
- Upon receiving repayment transactions (identifier - check keyword repayment in details), we will match it will all existing repayments in pending state and mark the transactions as settled in our DB in a FIFO manner.
- (Check with Arpit, if there is some key mapping for the respective transactions) - Done
    - Please note that only transactions in pending settlement (internal state) would be visible on UI
    - In case of multiple payments we will match transactions in FIFO manner and settle them internally in our DB
        - Why FIFO? (Is FIFO correct (Tech alignment pending)
- Once transactions are settled, we will hide them from UI while the actual settled corresponding payment will be visible in transactions as well as statement of account for the user.

### User Comms

When we receive a transaction from the user, we will be sharing a repayment receival confirmation to the user to instil confidence in the mind of the user. 

Repayment confirmation

<aside>
💬 Repayment of ₹25,000 received! We are updating your available balance

Dear <customer name>,

Your repayment of ₹25,000 was successful. ✅

**Note:** It may take 1-2 business days for payment to reflect in the account statement.

Track the status of your repayment on the Volt Money app <app link>

For any query or feedback, call us or WhatsApp us at +919611749097

Regards,
Team Volt Money

CTA: Track status
Email: d-4622a8912c2f476698625b9dec7f746b
Whatsapp: repayment_settled

</aside>

Repayment settled:

<aside>
💬 Repayment of ₹25,000 has been updated in your account statement!

Dear <customer name>,

Your repayment of ₹25,000 has been updated in your account statement. ✅

**Note:** It may take 1-2 business days for payment to reflect in the account statement.

Track the status of your repayment on the Volt Money app <app link>

For any query or feedback, call us or WhatsApp us at +919611749097

CTA: Track status

Email: d-340c6d0e5221409a928c884c55e93138
Whatsapp: repayment_processing_v1

</aside>

Repayment failed:

<aside>
💬 Repayment of ₹25,000 has failed!

Dear <customer name>,

Your repayment of ₹25,000 has failed. ❎

Note: Any amount deducted from your account will be refunded to your account in 5-7 business days.

For any query or feedback, call us or WhatsApp us at +919611749097

</aside>

### Reporting (Internal analytics + Ops flags and ticket creation)

- Admin action to settle transactions (change on UI) manually coordinated with Volt and BFDL Ops
- DB entries of cases where repayments were made but were not settled (Ledger) with following metrics (Stored once a day at 6 PM)
    - Application ID
    - Transaction ID
    - Transaction Status (Gateway)
    - Transaction Settlement Status (Unsettled/Settled) - Basis which we will control pending transactions on UI
    - Payment date and time (User payment timestamp)
    - Auto-settlement date and time (Internal API settling timestamp) - measure TAT
    - Manual Settlement Flag (true/false if transaction was settled manually by ops team using admin action)
- Automated Emails to Zendesk (T+Nth Business day) to create unsettled repayment ticket IDs for operations team to identify and follow up on cases with BFL.
- Backfill task (See all transactions completed before on a gateway level) and backfill them as settled.
- N should be controllable via admin action by ops team to handle BFL operational issues  (ask ops team if this is good to have)
- Automated Report to be sent daily indicating pending settlements for measuring product efficiency and raising outliers to ops.

[https://docs.google.com/spreadsheets/d/10gK_rXJ2PbsF3pZ1kUc4Xz_tMSsBu8szAh02rCbxN8M/edit#gid=0](https://docs.google.com/spreadsheets/d/10gK_rXJ2PbsF3pZ1kUc4Xz_tMSsBu8szAh02rCbxN8M/edit#gid=0)

|  | **T0** | **T-1** | **T-2** | Rest |
| --- | --- | --- | --- | --- |
| Number of repayments |  |  |  |  |
| Number of transactions automatically settled |  |  |  |  |
| Number of transactions pending settlement |  |  |  |  |
|  | **Today** | **This week** | **This month** |  |
| Average settlement TAT |  |  |  |  |
| % repayments settled automatically |  |  |  |  |
- We will stop sending repayment alerts for all repayments and instead will alert on cases only where transaction is not settled within two business days (Business calendar to be integrated and used).
    - **Sample reporting Email to Ops (automatically creates ticket)**
        
        Repayment Update - V402LAS00095711
        
        Hi,
        
        Repayment of 989 has been made towards the following LAS account.
        
        Amount : 989
        
        Customer Name : Abcd Arora
        
        Customer PAN : CLFPA8754J
        Payment Date : 26/02/2024 14:57:45
        Loan Account Number : V402LAS00095711
        Tracking ID : 113193133462
        Merchant ID : 1252896
        Bank reference Number : 442342347316
        Order status : Transaction Successful
        Currency : INR
        Payment Mode : Unified Payments
        
        Regards
        
        VOLT MONEY
        

# Design

Repayment Transaction post payment design:

https://www.figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=6223-25970&mode=design&t=lArG4Oci0f7D3BAP-0

Repayment pending (transaction ledger user section):

https://www.figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=12-1280&mode=design&t=VRUs90vay3DNHWug-0

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

[Transactions Key Mapping:](Repayment%20Lifecycle%20Tracking/Transactions%20Key%20Mapping%2012515bfba2f74c83a4dc49a3d781e017.md)

---

# **Appendix**

## Meeting notes

[Sameer Minde <> Vaibhav (1)](Repayment%20Lifecycle%20Tracking/Sameer%20Minde%20Vaibhav%20(1)%200df3c8eb6acd4bb9877a9d121981704d.md)

# Action Items:

- Check with tech team on internal statuses of repayments - Done
    - CANCELLED: 1231
    FAILED: 2874
    COLLECTION_COMPLETE: 3811	
    SUCCESS_WITH_LENDER_RECON_FAILED: 26	(Check with CCAvenue - When this status is received)
    PENDING_SETTLEMENT: 3
    REQUESTED: 40654
- Cover reporting of this release - Done
- Check failed screen communication (Any amount deducted, will get refunded back in x days) - Done
- Put designs in step by step order on Figma - Done
- Repurpose this for Repayment payment screen - Done
    - https://www.figma.com/file/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?type=design&node-id=1481-26839&mode=design&t=xXhYKtYUy6vvdZBF-0
- Discuss if modal or screen is a better way to show transaction details options - Done
- Add payment date Note - Done
- Copy review pending
- Create ticket on Ops (Zendesk) on T+2 (business days) list of payments - Done
    - Amount, Customer Name, PAN, VLAN, Loan contract number, date time of transaction, transaction ID (if multiple transactions then create multiple time).
    - Subject:
    - Create individual ticket
    - Backdated analysis
    - Formatting issues in payments (payment context)?
    - Admin action (transaction ID) to remove pending repayment from UI for the user.
    - On clicking back from payment screen, confirm with the user and cancel the session to keep requests clean
    - In case the payment was done by the user, but gateway could not handle it, send a message to the user and confirm if any amount was deducted pleaser reach out to us.
    - Backend controlled T+N days which can be edited as per Bajaj’s operational bandwidth

Design update

- User should focus on settlement - Change it to yellow - make text bold

### Analytics requirement

[Analytics requirement: Repayment](Repayment%20Lifecycle%20Tracking/Analytics%20requirement%20Repayment%20cfed92af4ebd44dcbefb84a34d1ef4bb.md)

[Analytics requirement: Revocation request](Repayment%20Lifecycle%20Tracking/Analytics%20requirement%20Revocation%20request%20987696701b154298bfeadf50d263724a.md)

[Analytics requirement: Foreclosure](Repayment%20Lifecycle%20Tracking/Analytics%20requirement%20Foreclosure%208e4d1f5d1a7d4b259dc52600e961084b.md)