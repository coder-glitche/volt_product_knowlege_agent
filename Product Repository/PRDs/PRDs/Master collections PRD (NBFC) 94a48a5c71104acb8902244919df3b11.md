# Master collections PRD (NBFC)

: Vaibhav Arora
Created time: September 12, 2024 2:29 AM
Status: In progress
Last edited: October 3, 2024 1:50 PM
Assignee: Vaibhav Arora
Due Date: 13/09/2024

# **What problem are we solving?**

There are multiple instruments through which NBFC will acquire funds against outstanding of user’s loan account. Following are the one’s we are moving ahead with V1:

- Repayments (PG/Bank account transfer)
- Withdrawals (Collection of charges against withdrawal - Capitalisation)
- Mandate presentation
- Sell-off of collateral to recover funds (Shortfall/Overdue)

**Collections can be of two types:**

- User initiated (Withdrawal / Repayment / Sell-off)
- NBFC initiated (Mandate presentation (Interest and charges) / Sell-off)

This document unites all of the instruments into a consolidated collections requirement for the NBFC.

---

# **How do we measure success?**

| **Metric** | **Definition** | **Formula** | Expected success rate |
| --- | --- | --- | --- |
| Mandate Success Rate | Percentage of successful mandate presentations | (Successful Mandates / Total Mandates Presented) * 100 | 90% +- 5% |
| Repayment Success Rate | Percentage of successful repayments through PG/bank transfers | (Successful Repayments / Total Repayments Attempted) * 100 | 95% +- 5% |
| Cost of Collections | Total cost incurred as a percentage of the amount recovered | (Total Collection Costs / Total Amount Recovered) * 100 | Low cost of collections for efficiency |
| Invocation success rate | Success rate of invocation initiated digitally for pledged funds | (Total proceeds from invocation / Total amount of collateral initiated for invocation)*100 | 90% +- 5% |

---

# **What is the solution?**

- Withdrawal (Charges collection against withdrawal)
    
    When a user withdraws from their credit line against their pledged assets, we will identify if there are any associated charges due in the loan account. 
    
    If overdue charges are found, charges will be knocked off and the effective amount will be disbursed to the user
    
- Repayment
    
    When a user makes a repayment, their repayment will be accounted against different ledgers of the loan account as per the configured apportionment strategy
    
    Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess
    
- Mandate presentation (Interest collection)
    
    At the end of the billing cycle, outstanding interest (accumulated over the cycle) and due charges will be collected automatically from the user’s bank account via the set up mandate. 
    
- Sell-off
    
    There are three scenarios where a sell-off can be initiated:
    
    1. User initiated sell-off (when user requests sale of securities to reduce outstanding dues)
    2. Shortfall: After ageing of 7 of regulatory shortfall ( eg 50% LTV) NBFC will invoke securities to normalise the account (reduce POS from DP)
    3. Outstanding charges and interest: After an overdue of charges of 7 days (grace period) NBFC will invoke securities to recover the outstanding amount

Scenarios may arise where the different collection methods coincide with each other, this document will also cover handling on Fenix/LSP ends to handle overlap

## Requirements overview (optional)

## User stories / User flow

- Withdrawal:
    
    User opens an account → Processing fees and charges are posted on account opening (for eg Rs 2000) → User places their first withdrawal (eg Rs 50,000)→ Posted charges are knocked off and the effective amount in their bank account (Rs 48,000)
    
- Repayment:
    
    User makes a repayment via PG → Payment is confirmed by the PG → PG is sent to the LMS for accounting → LMS posts the transaction in the loan account → Amount gets apportioned as per the apportionment strategy
    
- Mandate presentation
    
    User utilises their limit for the month and has accrued interest against it → Accrued interest gets posted as outstanding interest on the first of next month → NBFC ops generates and verifies the presentation file → Outstanding mandate amount is deducted from the user’s bank account on the the presentation date → Corresponding repayment is posted in the user’s loan account and dues are cleared
    
- Sell-off
    
    NAV of user falls making principal outstanding lower than min DP (Regulatory shortfall) → Ageing is calculated against the shortfall as per the following logic → If ageing breaches a count of 7 NBFC initiates sale of securities via digital invocation → Funds are received manually in the NBFC bank account → Post credit of funds, repayment in the respective loan account is posted for the user
    
    ```r
    First check for shortfall condition (SA = POS - DP)
    - If SA > 0 (Shortfall occured).
    - If SA < 0 (Not a shortfall).
    - If there is no shortfall with aging >0 against the loan id, create a new record in shortfallAnalysis(AGING = 1, SA = POS - DP))
    - If there exist Active shortfall with aging >1 against line, than aging logic will be applied as follows
    -- If Last Shortfall Amount (LSA) < Current Shortfall Amount (CSA), simply create a new record with aging 1. And increase all the remaining records against that shortfall id by 1.
    -- If LSA > CSA, reduce all the shortfall records by diff (where diff = LSA - CSA).
    --- If the updated shortfall amount is greater than 0, increase the aging by 1.
    --- Else update shortfall amount as 0 and aging as 0.
    ```
    

## Requirements

---

### Repayment ([Technical specification document for Fenix](https://docs.google.com/spreadsheets/d/1Lu7Xrau7Sd6OuKtiWojtOMV-L6OrWqTULfHH8EmbKxk/edit?gid=268780732#gid=268780732))

**Repayments requests may be initiate from 2 sources**

- LSP app (in app transaction)
- Command center UI (updating bank transaction)

**Details required: (In case** 

- UTR (payment reference number)
- Payment date
- Payment amount
- Apportionment logic
- Payment type (Repayment type: Adjustment/bank transfer/PG name)
- Remarks (char lim 70)

**Remarks from Fenix (in SOA):**
Repayment received for loan account number: FXLAN7890123

**Validations:**

- Repayment amount cannot be greater than total outstanding (While creating order for repayment) - Validation to be placed on LSP
- Command centre should be able to add repayments (sell off/adjustment/waive off use cases)
- Credit should be active or expired for an order to be generated, an order against a credit cannot be generated if status is closed

**Apportionment:**

The repayments posted in the loan account will be apportioned basis the following logic:
Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess

**Scenario:**

- **Total Repayment Amount**: Rs. 50,000
- **Overdue Interest**: Rs. 5,000
- **Overdue Charges**: Rs. 3,000
- **Shortfall Principal**: Rs. 10,000
- **Due Interest**: Rs. 8,000
- **Due Charges**: Rs. 2,000
- **Principal**: Rs. 20,000
- **Excess**: Any remaining amount after all other particulars are settled.

**Apportionment:**

| **Particular** | **Amount Due (Rs.)** | **Apportioned Amount (Rs.)** | **Remaining Repayment Amount (Rs.)** |
| --- | --- | --- | --- |
| Total Repayment Amount | - | Rs. 50,000 | Rs. 50,000 |
| Overdue Interest | Rs. 5,000 | Rs. 5,000 | Rs. 45,000 |
| Overdue Charges | Rs. 3,000 | Rs. 3,000 | Rs. 42,000 |
| Shortfall Principal | Rs. 10,000 | Rs. 10,000 | Rs. 32,000 |
| Due Interest | Rs. 8,000 | Rs. 8,000 | Rs. 24,000 |
| Due Charges | Rs. 2,000 | Rs. 2,000 | Rs. 22,000 |
| Principal | Rs. 20,000 | Rs. 20,000 | Rs. 2,000 |
| Excess | - | Rs. 2,000 | Rs. 0 |

**Overriding apportionment strategy:**

Borrowers may request customized allocation to address specific preferences.

For example, a borrower may prioritize reducing the principal balance over paying accrued interest or fees to prevent sell off in case of sell off.

The LMS should allow loan officers or API to override the standard apportioning logic and adjust allocation priorities based on borrower requests

Fenix should be able to define the apportioning logic basis the condition of the account. Currently there are two states but more states can be added:

- Mandate presentation
- Account in shortfall

**Status:**

- A repayment can be in the following states (in the complete lifecycle):
    - PENDING_PAYMENT_CONFIRMATION (Repayment is currently under confirmation by PG - will not arise in case of manual payments added by the command centre)
    - PENDING_CHECKER_APPROVAL (Repayment needs to be approved via checker on the command centre)
    - REJECTED  (Repayment rejected by checker)
    - PENDING_SOA_POSTING (Repayment has been approved by the checker and is now being posted in the user’s loan account)
    - FAILURE (Posting of the transaction in the user’s loan account failed)
    - SUCCESS (Repayment has been successfully posted into the user’s loan account)

**Gateway integration:**

- Late authorisation is configured on Gateway i.e. if a payment is not confirmed within 10 minutes, the amount will get automatically refunded to source
- Frontend will create an order, order number will be given to frontend, SDK will be integrated with react native SDK.
- We will open the flow, FE will handle the callback, and call BE, BE will fetch state of the transaction to get the deterministic state.
- [Razorpay PG SDK integration: DSP ](Razorpay%20PG%20SDK%20integration%20DSP%200e31bc4eaacf4dd99a80a3a1835b951b.md)

### Withdrawal ([Technical specification document for Fenix](https://docs.google.com/spreadsheets/d/1YYvCaOuxbwZs0E7FmB7YTUVGXUk49RegWc8OkexkbDw/edit?gid=0#gid=0))

Withdrawal requests may be initiate from 2 sources

- LSP app
- Fenix UI

**Withdrawal request will have the following parameters:**

- UTR (payment reference number)
- Payment date
- Payment amount
- Payment type (Repayment type: Adjustment/bank transfer/PG name)
- Remarks (char lim 70)

Remarks from Fenix in SOA:
Amount disbursed for loan account number: FXLAN1231432

**Settlement of charges at the time of withdrawal**

If charge are outstanding, then they will be deducted from withdrawal amount (charges will be knocked off, total amount will be sent to Finflux LMS)

**Status handling:**

Following status of withdrawal should be managed in Fenix:

- Accepted - (request was validated by fenix hasnt reached cashfree yet)
- Pending_maker_checker_approval - (maker checker was applicable and is pending)
- Maker_checker_rejected - (Maker checker request was rejected)
- Pending_business_hour (request is pending for business hour logic)
- Pending fund transfer
- Pending SOA posting
- Failure
- Success

### Sell off ([Technical specification document for Fenix](https://docs.google.com/spreadsheets/d/1S87YEcmaDIb0U-egyfxOtOxfuNZTxltbp0w1qaxopNI/edit?gid=1104469637#gid=1104469637))

**Request discovery:**
Ops agent will be initiating sell requests against lodged assets against a line. Ops agent will be able to select securities and request sell-off for the same

**Scenarios**

1. NBFC initiated sell-offs (for collection): (User consent not needed/ Ops agent selects securities)
2. User initiated sell-offs: (User consent needed / User selects securities)

In both scenarios ops agent will search the loan account and then manually initiate sell-off requests against the collaterals

**Request initiation:**

- Ops agent searches for the client (and then loan account) or the loan account in which the securities need to be sold (This will be a loan account level operation).
- Ops agent will navigate to the respective loan account

**Request form:**

- Ops agent will be able to do a line level operation to sell securities to a loan account. Upon clicking an interface will open where the ops agent will select the securities one by one. Ops agent should be able to select multiple securities at once to sell.
- Request level parameters (loan account in which the collateral needs to be sold off will be automatically picked from the interface to avoid logging errors)
- Collateral level details will be selected manually

**Required parameters:**

- assetType (Approved list detail fetched from ISIN added by ops agent)
- amfiCode (Approved list detail fetched from ISIN added by ops agent)
- quantity (Input required)
- folioNumber (Fetched directly from the lodged asset details)
- emailId (Fetched directly from the lodged asset details)
- isin (Fetched directly from the lodged asset details)
- securityType (Approved list detail fetched from ISIN added by ops agent)
- scripNumber (Approved list detail fetched from ISIN added by ops agent)
- requestRefNumber (Fetched directly from the lodged asset details)
- lienMarkingNumber (Fetched directly from the lodged asset details)
- lienRefNumber (Fetched directly from the lodged asset details)
- ihNumber (Fetched directly from the lodged asset details)
- kfinRefNumber (Fetched directly from the lodged asset details)
- costValue (Fetched directly from the lodged asset details)
- mobileNumber (Fetched directly from the lodged asset details)
- modeOfHolding (Fetched directly from the lodged asset details)
- ltv (Fetched directly from the lodged asset details)
- Parameters to be entered by ops agent for each security:
- Security selected for sell-off
- Quantity
- Attachment of proof (optional)

**Parameters visible to the ops agent while selecting securities:**

- Total value of securities selected
- Total limit for loan against the securities selected
- POS of the loan account
- IOS of the loan account
- COS of the loan account
- Accrued interest
- DP of loan account
- Ops agent will be able to select multiple collaterals for sell-off in one request
- 

**Validations:**

- Request validation to be placed at the time of initiating sell-off (Limit)
- Limit of selected funds <= (DP - TOS(1 + buffer) - accrued interest)
- Ops agent will be able to sell all securities if needed against a line to recover outstanding amount

**Sell off repayment:**

Post selling off the securities, ops agent will have to add the proceeds received against the sell-off requests into the user's loan account. This process will be manually done by the ops agent

- Proceeds received from the sell-off request can be different (in value) than what was sold at the time of initiating the request
- Proceeds from the sell-off request will be received at a Folio level in the dedicated NBFC bank account
- Reconciliation of sell-off proceeds will be have to done to ensure the right repayments are settled into the bank account.
- Sell-off workflow will contain two approval tasks within itself.
- Ops agent will be able to close a sell-off request only when repayment proceeds have been received against all sold securities (need business alignment)

**Request discovery:**

Ops agent will discover the approval task in the approval section of the loan approvals screen. Ops agent will be able to manually add transactions (multiple at a time against the collateral sell-off request)

**Request initiation:**

Ops agent searches for the loan account and goes to the sell-off repayment action in the respective loan account. Will only be available if there is a incomplete sell-off request in progress where the sell-off of collateral has been completed.

(Sell-off repayment can only be done against an already existing sell-off request in a approved collateral sell-off state)

**Request form:**

Ops agent will be able to do a line level operation to add repayment against sold securites to a loan account. Upon opening the interface, ops agent should be able to see the securities against which collateral sell-off was initiated and will be able to add the corresponding repayment.

- Collateral parameters to be visible to the ops agent are covered already
- **Repayment parameters:**
    - Repayment amount
    - Repayment date
    - Reference number (Folio number against which proceeds are received)
    - UTR (Reference number)
    - Repayment mode (To be populated automatically as Collateral sell-off)
    - Remarks (Amount received against sell-off of collaterals)

**Validation:**

- Repayment against all proceeds should be available in the maker task
- UTR level dedupe should be done to submit transactions

**Sell of status handling:**

Selling of a collateral will include the following high level steps to complete the request (in order):

- Collateral selection (Validation)
- Initiating sell-off
- Blocking of collateral (DP of user reduces)
- Approval task is created
- Approval task is completed
- Sell-off process starts (Digitally for digitally pledged collateral and operationally for physically pledged collaterals)
- Sell-off completes and proceeds from AMCs are received in bank account
- Reconciliation of proceeds (Operationally)
- Adding of repayment to loan account (Proceeds)
- Approval task is created
- Approval task is completed
- Charges posting against sell-off

**Lifecycle:**

- Pending Verification : Collateral is selected for sell-off but verification is pending
- Pending collateral approval: Collateral is blocked but checker approval is pending
- Sell off initiated
- Sell off completed
- Repayment pending
- Pending repayment approval
- Repayment posting in progress
- Completed
- **Sell off handling for LSP (UI)**
    
    **How will the LSP identify if there is a shortfall on the loan account?**
    
    Shortfall will occur when DP of the loan account goes below the existing POS of the loan account. Fenix will share a webhook of shortfall amount along with ageing and shortfall creation date.
    
    LSP will render the same as per the current implementation with the following due date logic:
    
    <aside>
    ⚠️
    
    Apportionment for DSP works in a way, that if the account has a shortfall, it will automatically be prioritised over interest and charges due for the loan account and will settle the shortfall amount first
    
    **Repayment apportionment strategy in V1:**
    
    Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess **(Currently implemented)**
    
    **Repayment apportionment strategy in V2 (to be implemented):**
    
    Overdue interest -> Overdue charges -> Due interest -> Due charges -> Shortfall principal -> Principal -> Excess (Mandate presentation)
    
    Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess (Any other repayment)
    
    </aside>
    
    | **Shortfall inception date** | **Shortfall due date** |
    | --- | --- |
    | 1st of month | 8th day |
    | 2nd of month | 9th day |
    | 3rd of month | 10th day |
    | Last day of month | 7th day of M+1 |
    | Any date | Shortfall date + 7 |
    
    **What will be the frequency of shortfall updation?**
    
    Fenix will run a daily CRON job post NAV update (Time to be closed with Business) and will send webhooks accordingly
    
    **Shortfall due date to be shown to the user**
    
    Shortfall due date will be shown as per the aforementioned logic, shortfall card should get removed if (Shortfall status is not initiated (sell-off) and DP>POS otherwise the user should be able to see the shortfall card
    
    **Shortfall sell off initiation status handling**
    
    Fenix to maintain shortfall initiation flag, whenever sell-off is initiated by CC against a loan account, a flag to be maintained to describe that a shortfall repayment has been initiated (to be exposed to LSP). 
    Secondary logic: If shortfall breaches ageing of 7, shortfall card should be visible to the user (till T+3 business days) of due date
    
    **Fenix webhooks for respective events:**
    
    - When shortfall is created in the user’s loan account (CRON job)
    - When ageing/shortfall amount changes for the loan account (CRON job)
    - When sell off is initiated against a loan account for the shortfall

### Mandate presentation ([Technical specification document for Fenix](https://docs.google.com/spreadsheets/d/1S87YEcmaDIb0U-egyfxOtOxfuNZTxltbp0w1qaxopNI/edit?gid=1104469637#gid=1104469637))

Interest and charges:

- Identifying interest and charges and letting LSP know that interest and charges are due
    
    **How will LSP identify that interest has been posted for the loan account?**
    
    What are the possible options:
    
    - CRON job (LSP handling for Tata)
    - Sheet upload (LSP handling for BFL)
    - Get API for mandate collection request (LSP syncs collection amount directly with NBFC)
    - Webhook on mandate file creation to LSP / Updates when presentation amount is changed to LSP
    
    **When the interest will be posted for the loan account?**
    
    Interest will be posted on the 1st of the following month for DSP. Corresponding mandate file will also be generated for the same month including outstanding charges and interest.
    
    **What will be the mandate presentation amount?**
    
    Mandate presentation amount will be the total interest outstanding for the last billing month + charges posted in the last month and will be collected via mandate the next month on the 7th
    
    **When IOS+COS≤10**
    
    Amount will get settled and mandate presentation will be skipped 
    
    (User will be shown outstanding card on UI)
    
    **If mandate is not registered for the user:**
    
    Mandate presentation will be skipped and dues will be posted in the loan account
    
    When IOS+ COS≥10 and mandate is registered, mandate collection request will be scheduled for the user 
    
    Volt will be able to track the mandate collection request against a loan account for the user, and will accordingly render the card for the user.
    
    If the outstanding amount is refreshed for the user (the amount should get updated for LSP as well). 
    
    **If interest due changes (billing job) runs again for the LMS, how will it get updated for the user?**
    
    Amount will change, Volt will sync with the mandate presentation request with Fenix. Fenix will send a webhook to LSP for amount to be collected when mandate presentation file is approved by ops. 
    LSP to store collection amount for the user and show in the interest card.
    
    **Fenix webhooks for respective events:**
    
    - When billing is completed for the user (Mandate status will also be shared for LSP to handle UI)
    - When mandate collection amount is approved (Maker checker approval by ops)
    - When mandate presentation is completed (Success/Failed) along with mandate registration status
    
    **Maintenance of mandate status?** 
    
    Reverse file, if mandate presentation is failed due to mandate for specific reasons, as described below, the status of the mandate should get updated in Fenix
    
    Correspondingly the card handling on UI should change.
    
    If mandate presentation fails, user should be able to pay the outstanding amount on their application.
    
    [[https://docs.google.com/spreadsheets/d/1KoT9Rso6bNU3nw7COUp0cYBwICnfP4C6ZPodZkoMCRE/edit?gid=756291093#gid=756291093](https://docs.google.com/spreadsheets/d/1KoT9Rso6bNU3nw7COUp0cYBwICnfP4C6ZPodZkoMCRE/edit?gid=756291093#gid=756291093)](https://docs.google.com/spreadsheets/d/1KoT9Rso6bNU3nw7COUp0cYBwICnfP4C6ZPodZkoMCRE/preview?gid=756291093#gid=756291093)
    
    **What happens when mandate presentation fails? How will NBFC collect the amount?**
    
    User will have to pay the outstanding amount by making a repayment on their loan account
    
- User notification (LSP) on UI to notify on auto debit and handling for respective scenarios
    
    As soon as a collection request is consumed by the LSP, the respective status handling should get done on UI for the user
    
- **Status management of collection by LSP**
    
    LSP will track the mandate collection request to maintain the status of collection for the user
    
- Handling of concurrent charges and charges posted after due

**Request initiation:**

After billing cycle, ops agent will be able to generate the mandate generation file on UI for a respective month. Post generation and downloading the file, automatically an approval task for the mandate file will be generated for the team to approve.

Ops agent will only be able to generate one file for the mandate registration process, post generation, if another file has be generated post corrections, the earlier approval task of the originial mandate file will have to be rejected.

Ops agent will be able to download the file from the section after generation, and will have another CTA to regenerate report to create a new report with updated values. Ops agent should be able to see the File number for approval.

**Request processing:**

For all customers in the respective amount, amount collected via mandate will be calculated (Interest outstanding + Charges outstanding), and will be created in a file as covered earlier in the mandate requirement

<aside>
⚠️

Charges outstanding should only be for the billing month

</aside>

**Request initiation:**

As soon as the file is generated for review an approval task on command centre UI will be created for the ops agent to review.

**Request processing:**

Ops agent will either be able to approve or reject the mandate presentation file and will see the following details:

- File number
- Mandate file (link to the generated file)
- Month and year of presentation

Ops agent will be able to track the status of the mandate presentation transaction against a specific loan account on command centre.

The respective transaction will be visible in the transactions tab for the user and the following details against the transaction will be visible for the user:

- Transaction date time
- Transaction amount
- Transaction method - Mandate
- Transaction status
- Transaction sub status
- UTR

### Shortfall collections ([Technical specification document for Fenix](https://docs.google.com/spreadsheets/d/1Y_UHnHrbdYzQBZjIfYvO9zXVqszU2uUxPnI9QbHH58Q/edit?gid=0#gid=0))

# **Design**

---

**Repayment (PG/Mandate) and Sell - off tracking on loan details page:**

https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS-command-center?node-id=10-24650&node-type=canvas&t=4XM9GI8rXVyL7HHu-0

**Sell off workflows (initiated by ops agent) (Repayment posting + initiating sell off):**

https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS-command-center?node-id=12-25210&node-type=canvas&t=4XM9GI8rXVyL7HHu-0

**Approval screens for maker checker:**

https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS-command-center?node-id=187-23199&node-type=canvas&t=4XM9GI8rXVyL7HHu-0

**Mandate presentation workflow:**

https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS-command-center?node-id=12-25210&node-type=canvas&t=4XM9GI8rXVyL7HHu-0

# **Analytics**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Frequently asked questions (FAQs)

## Ops & Sales training

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