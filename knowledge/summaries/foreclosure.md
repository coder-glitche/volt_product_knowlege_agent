# Current State: Foreclosure

> Auto-generated from 97 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Manage Limit Error messaging handling
**Status:** Ready for Tech | **Last edited:** September 23, 2024 4:25 PM

**Problem:**
are we solving?**

- At Manage Limit page
    - Remove pledge
        - Copy in the modal that opens up in the un-pledging flow is not clear to the user & the ops leading to escalation
        - Explanation of buffer in case of BAJAJ
        - Error messaging in case the lender API throws 500 error
    - Pledge more & Increase limit
        - Copy in the modal that opens up in the un-pledging flow is not clear to the user & the ops leading to escalation
        - Error messaging in case the lender API throws 500 error

---

**Solution:**
?**

---

## #2 — LSQ Revamp Solution Doc
**Status:** Not started | **Last edited:** October 6, 2025 12:50 PM

**Problem:**
are we solving?**

Currently, both the **MFD activation journey** and the **customer LAMF journey** run through a **single combined flow**, which is leading to multiple challenges:

- Difficult to manage MFDs handling multiple applications/customers
- Limited ability to manage multiple products at the customer level
- Workflow and opportunity overlaps and causing confusion
- Lack of clarity on which opportunity belongs to which journey
- Inadequate visibility into MFD vs. customer progress tracking
- **Phone number as the primary identifier creates a constraint** — if an MFD and a customer sha

**Solution:**
?**

---

## #3 — Master collections PRD (NBFC)
**Status:** In progress | **Last edited:** October 3, 2024 1:50 PM

**Problem:**
are we solving?**

There are multiple instruments through which NBFC will acquire funds against outstanding of user’s loan account. Following are the one’s we are moving ahead with V1:

- Repayments (PG/Bank account transfer)
- Withdrawals (Collection of charges against withdrawal - Capitalisation)
- Mandate presentation
- Sell-off of collateral to recover funds (Shortfall/Overdue)

**Collections can be of two types:**

- User initiated (Withdrawal / Repayment / Sell-off)
- NBFC initiated (Mandate presentation (Interest and charges) / Sell-off)

This document unites all of the instruments into

**Solution:**
?**

- Withdrawal (Charges collection against withdrawal)
    
    When a user withdraws from their credit line against their pledged assets, we will identify if there are any associated charges due in the loan account. 
    
    If overdue charges are found, charges will be knocked off and the effective amount will be disbursed to the user
    
- Repayment
    
    When a user makes a repayment, their repayment will be accounted against different ledgers of the loan account as per the configured apportionment strategy
    
    Overdue interest -> Overdue charges -> Shortfall principal -> Due interest -> Due charges -> Principal -> Excess
    
- Mandate presentation (Interest collection)
    
    At the end of the billing cycle, outstanding interest (accumulated over the cycle) and due cha

---

## #4 — LOS and LMS admin actions (LSP with DSP as lender)
**Status:** In progress | **Last edited:** October 16, 2024 2:25 PM

**Problem:**
are we solving?**

We have developed multiple admin actions (ops controlled actions) that help in servicing our customers in the onboarding as well as the servicing journey. 

This requirement covers utilising the admin actions (where needed) to cover use cases currently served by LSP (for customers) with DSP as a lender.

---

**Solution:**
?**

---

## #5 — Bulk email automation
**Status:** Not started | **Last edited:** October 14, 2024 2:40 PM

**Problem:**
are we solving?**

- All emails that are directed to [operations@voltmoney.in](mailto:operations@voltmoney.in) trigger automatic ticket creation and assignment without distinction, leading to delays in addressing urgent queries. Lender query emails sent to [operations@voltmoney.in](mailto:operations@voltmoney.in) are not prioritized due to this.
- Individual lien removal emails are sent manually to BAJAJ along with bulk emails comprising of individual lien removal request, resulting in duplicate data being sent for the same case twice in a day.
- Improving the communication after Pledging and 

**Solution:**
?**

—> Lien Removal and Foreclosure emails should **not be sent** individually to lender(BAJAJ). For sending communications regarding Lien Removal and Foreclosure, we will send bulk reports as follows:

1. Update recipient and CC fields for individual Lien Removal and Foreclosure emails send to Volt:
- Change the recipient from [operations@voltmoney.in](mailto:operations@voltmoney.in) to [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in)
    
    This ensures that tickets are not created for each Lien Removal and Foreclosure request
    

- Remove all other recipients and CCs, keeping [support.internal@voltmoney.in](mailto:support.internal@voltmoney.in) as the sole recipient
    
    This includes removing [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) and [l

---

## #6 — [IronGrid] Un-lien related issues
**Status:** Not started | **Last edited:** November 5, 2024 12:48 PM

# [IronGrid] Un-lien related issues ## Fund level status of un-pledge request **Phase 1** - Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED. - We will keep polling the status of all the funds until we get the terminal statuses of each of the funds - We keep polling the API for 4 days every hour until we get the status of all the fund - Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached) - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request - We will store the individual status of all the funds under the un-pledge request - API Documentation : [Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx) **Phase 2** - We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user. ## Excess margin handling in un-pledge request **For BFL (only need to make this change for BAJAJ)** - While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge. - 3 fields which are present in Foreclosure details API : - net payable = Total due - Excess Margin - Total Due - Excess Margin - For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding. ### **User not able to request un-lien request if stocks present in their holding** - **Issue** - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error - **Solution** - We will only

---

## #7 — Foreclosure handling for DSP
**Status:** Done | **Last edited:** November 18, 2024 12:09 PM

**Problem:**
are we solving?**

Users at this point in time can raise multiple requests at a time, these transactions can often cause the other to fail. 
For example, if a user, raises a withdrawal which is pending with the NBFC to process, and immediately raises a foreclosure, they will be able to, which may cause dangling transactions to be left at our end.

If a user raises a foreclosure request, when a mandate presentation transaction is still processing for them, and we close the loan account, we will have no way to post the proceeds from the presentation into their loan account. 

To solve for such s

**Solution:**
?**

Types of requests (Money/Collateral/Service):

| Type of request | Foreclosure blocked |
| --- | --- |
| Withdrawal | Yes |
| Repayment | Yes |
| Collateral removal | Yes |
| Collateral addition | Yes |
| Excess refund | Yes |
| Mobile update | No |
| Email update | No |
| Foreclosure | Yes |
| Withdrawal reversal | Yes |
| Repayment reversal | Yes |
| Charge reversal | Yes |
| Interest refund | Yes |
| Mandate presentation | Yes |

For any request which is pending, as per the above sheet, foreclosure request will not be processed instead we will pass an error message to the LSP.

Foreclosure cannot be processed as there is an existing pending request (Request ID: [Request ID]). Please resolve or complete the pending request to proceed with foreclosure.

In case there are multiple pen

---

## #8 — [Platform] Callbacks for LSP APIs for core servici
**Status:** In progress | **Last edited:** May 29, 2026 6:19 PM

**Problem:**
are we solving?**

There are core transaction and request lifecycles that need to be managed by the LSP. 

Volt as an LSP has built a lot of pollers and CRON jobs at specific days over existing lender APIs to solve for this. However this approach has a lot of challenges.

- Introduces a lot of computational load both at the LSP as well as the lender
- Not very accurate, as logic is based on top of hitting jobs on specific dates and times
- Requires a lot of maintenance at an engineering level across systems

Most of these APIs get data from core systems like the CTMS or the LMS, and this often

**Solution:**
?**

Building callbacks for core servicing flows:

- Due collection (lifecycle)
    - When interest becomes due
    - When mandate is presented
    - When mandate collection is successful
    - When mandate collection fails
    - When interest is settled
- Repayment
    - When a repayment is posted into the user’s loan account
- Shortfall
    - When shortfall is identified (daily job) in a user’s loan account
    - When shortfall updates for a loan account (change in amount/ageing)
    - When shortfall is settled for a user’s loan account
    - When shortfall crosses grace period (due date) and sell-off is initiated for the user
    - When sell off is completed
- Foreclosure
    - When a foreclosure request is approved for the user

---

## #9 — Sell-off Repayment Reconciliation — Maker Automati
**Status:** Not started | **Last edited:** May 29, 2026 3:39 PM

**Problem:**
are we solving?

- Today, the maker step for sell-off repayment reconciliation is entirely manual: the ops team downloads the bank statement and RTA/MFC payout reports, manually cross-references UTRs and amounts, and then maps each payout row transaction to a CDID before uploading the `bulk_unlodgement_post_sell_off` file into the Command Centre.
- This process is error-prone, time-consuming, and creates a daily dependency on ops/analytics bandwidth before the repayment posting flow can even begin.

**Solution:**
?

**In scope:**
- Daily automated UTR matching between payout reports (KFin, CAMS, MFC) and bank statement.
- Amount validation (BS settled amount vs. report expected deposit amount) at row level.
- Intra-report UTR deduplification before matching.
- PAN → FXLAN → SCRID → CDID key-based resolution per pledge source and repo type.
- CDID uniqueness enforcement with disambiguation logic for repeated sales.
- Row-le

---

## #10 — STP validation for Sell-off Repayment Reconciliati
**Status:** Not started | **Last edited:** May 27, 2026 3:11 PM

**Problem:**
are we solving?

- Today, all sell-off repayment reconciliation(approval) requests initiated via "Bulk Unlodgement Post Sell Off" in the Ops Command Centre go through the NSTP path — every record creates a checker task requiring manual review and approval.
- With an average of 173 requests per day (as of Jan–March 2026), manual processing introduces delay in repayment reconciliation execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.
- With the implementation of this feature we will be able to provide task description for ch

**Solution:**
?

**In scope:**
- For all UTRs in input file, UTR existence check against the bank statement.
- Settled Amount retrieval from the bank statement for the matched UTR.
- RTA report matching using the appropriate logic per RTA type — Folio + ISIN + Units + Session ID for KFintech, and Folio + ISIN + Lien Marking Number for CAMS.
- Bank-vs-RTA amount comparison, with auto-posting of matched records into the loan acco

---

## #11 — CAMS min_unit Validation for LAMF Lien Transaction
**Status:** Not started | **Last edited:** May 26, 2026 5:40 PM

**Problem:**
are we solving?

- CAMS RTA is introducing a mandatory scheme-level `min_unit` validation across all lien transaction APIs for LAMF. This is applicable to **CAMS RTA only** — KFintech RTA, CAMS MFC, and KFin MFC are not affected.
- Prior to this change, a lender could mark a lien of any unit quantity, and invoke or revoke any partial amount regardless of what remained. CAMS will now enforce a floor: any transaction that leaves `remaining_units < min_unit` for a scheme will be rejected at the API level.
- This impacts all three lien transaction types differently:
    - **Pledging (lien marking)

**In scope:**
- E2E fund selection algorithm — min_unit pre-flight for CAMS folios before invoke
- `min_unit_adjusted_flag` column in `fenix_sell_off_collaterals_request`
- Pledging UI validation (Volt LSP and 3rd party LSPs) — block mark if `lien_unit < min_unit`
- Revocation UI validation (Volt LSP) — inline error and helper CTAs for residual breach and legacy lien
- Revocation UI validation (3rd party LSPs) 

---

## #12 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #13 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #14 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #15 — Enhancement Of STP NSTP validations for Bulk sell
**Status:** In progress | **Last edited:** May 20, 2026 11:40 AM

**Problem:**
are we solving?**

[STP validation for Bulk Sell off](STP%20validation%20for%20Bulk%20Sell%20off%20336e8d3af13a802c8283d86e576f3220.md)

[E2E Sell-off Productisation V1 ](../LMS%20PRDs/E2E%20Sell-off%20Productisation%20V1%20352e8d3af13a80f9a75bed081dd798f0.md)

Initial STP/NSTP validation for bulk sell off approvals missed key sell-off logic, causing both false NSTP routing and incorrect STP approvals. 

- **Min redemption round-up missed:** Sell-off units are rounded up to meet minimum redemption requirements, increasing sell-off amount vs obligation — ~800/4,000 cases were wrongly pushed to 

**Solution:**
?

**In scope:**
- Per-CDID min_redemption_flag check and delta-tolerance  applied after standard STP formula.
- Replacement of partial overdue with full total_overdue (principal + interest + charges) from get_overdue_detail API in all DPD and Shortfall validation formulas.
- Reading dpd_trigger from fenix_sell_off_collaterals_request and selecting dpd_amount_75_trigger or dpd_amount_21_trigger from get_overdue_de

---

## #16 — STP validation for Bulk Sell off
**Status:** Done | **Last edited:** May 19, 2026 4:09 PM

**Problem:**
are we solving?

- Today, all sell-off requests initiate via the "Bulk Initiate Sell Off"  in the Ops Command Centre and go through the NSTP (Non-Straight-Through Processing) path — every record creates a checker task requiring manual review and approval.
- With average of 193 requests per day (as of Jan-March 2026), manual processing introduces delay in sell-off execution.
- Manual processing increases operational bandwidth consumption of OPS team and introduces human-prone errors.

**Solution:**
?

**In scope:**
- STP validation for Shortfall and DPD sell-off types .
- Auto-approval and dispatch for STP-eligible LANs (no checker task created)
- NSTP routing with reason codes for all non-eligible LANs
- Ongoing sell-off status check before STP approval
- Multi-row LAN aggregation (∑ across ISINs for CMV )and LTV fetch for CMV × (1 − LTV))
    - **Aggregation rule**
        
        > **Important**: A singl

---

## #17 — Dues Comms Updation
**Status:** Not started | **Last edited:** May 15, 2026 4:30 PM

**Problem:**
are we solving?

- Current SMS templates for due reminders, auto-debit alerts, overdue notices lack transparency, as they omit specific charges like collateral sell-off charges and fail to disclose the exact amounts for penal and dishonour charges.
- RBI guidelines require explicit disclosure of all applicable charges and reasons in all such communications.
- This gap creates a risk of non-compliance with RBI transparency and disclosure norms

**Solution:**
?

**In scope:**
- Migrating the existing communication events to the newly drafted SMS templates.
- Dynamo DB logging at a per-record level for all outcomes (success, failure) to maintain a compliance audit trail.

---

## #18 — [Platform] Foreclosure handling and enhancement
**Status:** Done | **Last edited:** March 3, 2025 2:13 PM

**Problem:**
are we solving?**

The Reserve bank of India asks us to round off [due](https://www.rbi.org.in/commonman/English/Scripts/CustomerServiceGuidelines.aspx#:~:text=00%2F2006%2D07dated%20July%201,the%20next%20higher%20rupee%20and) amount for the user to the nearest integer. However our LMS tracks all transactions up to 2 decimals. 

Link to guideline by RBI: [https://www.rbi.org.in/commonman/English/Scripts/CustomerServiceGuidelines.aspx#:~:text=00%2F2006-07dated July 1,the next higher rupee and](https://www.rbi.org.in/commonman/English/Scripts/CustomerServiceGuidelines.aspx#:~:text=00%2F2006%2D07d

**Solution:**
?**

We will be rounding up or down the foreclosure amount based on the half even rounding strategy where:

- If due amount at the time of foreclosure is more than or equal to N.5 it will be rounded up to N+1
- If due amount is less than N.5 it will be rounded down to N

The same will be passed on to the LSP as foreclosure amount. When the user makes the corresponding payment, we will collect it and accept the foreclosure request.

There can be two corresponding cases post the transaction is posted into the loan account:

- Account is in excess of an amount less than 1 Rs
- Account has an outstanding of an amount less than 1 Rs

**Scenario 1:**

Post collection of the foreclosure amount, we will be doing an excess refund with a transaction type: Round up adjustment

**Note:** No payout wil

---

## #19 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #20 — Foreclosure lifecycle tracking + Tata EOD report
**Status:** Done | **Last edited:** March 23, 2025 6:31 PM

**Problem:**
are we solving?**

- Users currently are not able to track the exact status of their request.
- Users do not get information and respective ETAs for the different steps involved in the process of their foreclosure request.
- Due to lack of clarity and involvement of 3P flows in the process, users feel that it is Volt that is causing delay in their application causing misinformation and instilling distrust in the minds of the user.

![User raises support ticket due to lack of clarity on status - tonality suggests that they feel that Volt is not doing anything to solve their issue](Foreclosure%2

**Solution:**
?**

We are solving this problem for the user by the following ways:

- Post making the foreclosure request, clearly describe the steps in the process to the user with accurate ETAs for each step.
- Descriptive UI screen describing the status along with steppers describing the journey of a foreclosure requests of the user
- Actively sharing the status of the request made by the user (foreclosure success/ foreclosure processed) on UI and via WhatsApp and Email to the user.
- Tata excess interest case handling - Foreclosure requests where we pay excess interest but it is not posted in the settlement account.
- Alerts
    - Flagging cases to Ops where requests are not automatically settled, so that they can be raised to BFL and Tata for settlement

---

## #21 — Product note Co-lending foreclosure - Deprecated -
**Status:** In progress | **Last edited:** March 15, 2026 8:49 PM

**In scope:**
- Designing a **safe and consistent foreclosure experience** for co-lended LAMF loans
- Ensuring customers interact with **only one loan experience**, despite multiple lender loans
- Enabling DSP to **orchestrate foreclosure end-to-end** while respecting lender-level closures
- Validations and error handling
- CC Maker checker for foreclosure processing
- Foreclosure repayment settlement(handling 

# Product note: Co-lending foreclosure - Deprecated - ignore ## **Background and Context** - **Who is facing the problem** - Customers foreclosing co-lended loan. - DSP Operations, Vol and DSP Support, Tech Ops teams handling servicing - TCL NBFC operations and finance teams managing their loan books - **What is the challenge / what is broken today** - In a co-lending setup, a single customer loan is split across **two NBFCs (DSP 10%, TCL 90%)** - Customers expect a **single foreclosure action**, while lenders require **independent loan closure and settlement** - Without a clearly designed orchestration: - Foreclosures risk becoming partially completed - Example: Foreclosure can partially succeed—closing one lender’s loan while the other remains open—and if collateral is released at that point, one lender is left with an unsecured loan, which is a major regulatory risk. - Ops teams face manual reconciliation and escalations - **Why is it important / what is impacted** - Foreclosure is a **high-trust moment** in secured lending - Any error directly impacts: - Customer trust and NPS - Regulatory compliance around pledge release - DSP’s credibility as the servicing NBFC - As co-lending is a **new product vertical**, getting this wrong early creates long-term operational debt. --- ## **1. Problem scope** ### In scope - Designing a **safe and consistent foreclosure experience** for co-lended LAMF loans - Ensuring customers interact with **only one loan experience**, despite multiple lender loans - Enabling DSP to **orchestrate foreclosure end-to-end** while respecting lender-level closures - Validations and error handling - CC Maker checker for foreclosure processing - Foreclosure repayment settlement(handling of accrued amount and excess management) and accounting **Primary users** - Retail customers foreclosing co-lended loans **Secondary users** - DSP operations and DSP Finance team - Volt sales and support teams - Volt Tech Ops - TCL NBFC Ops & Finance teams ### Out of scope - Payouts --- ## **2. Success Criteria** - ### Primary outcomes - Customers can foreclose co-lended loans through **one clear and predictable flow** - Repayments are getting posted without and disputes, All three loans are getting closed, collaterals are getting released and NOC is provided to the users. - Minimal manual intervention for standard foreclosure cases ### Key success metrics - Foreclosure completion success rate ≥ **99%** - Average foreclosure TAT ≤ **1 business day** - Ops/manual intervention rate ≤ **5% of cases** ### Post-launch good state - Foreclosure journey live and

---

## #22 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #23 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #24 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #25 — [Platform] Mandate collection BRE optimisation
**Status:** Done | **Last edited:** January 30, 2025 5:01 PM

**Problem:**
are we solving?**

There are multiple ways through which an NBFC can collect dues from customers:

- Accepting direct user initiated payments (VA/PG)
- Collecting payments via debiting user’s bank accounts (mandate)
- Invoking securities to clear dues (Sell off)

All repayment methods have different use cases and scenarios in which they are triggered. Mandate collection repayments are done for the following use case:

- User convenience and financial health: Amount is automatically deducted from the user’s bank account and ensures that their loan account does not become overdue
- NBFC portfoli

**Solution:**
?**

- We will be integrating with the Finflux (LMS) overdue API which gives us due level information:
    - Due type (Interest / Charge / Penal charge / Interest overdue)
    - Due amount
    - Due from
    - Due date
- Based on this information we will run a BRE to select which dues are eligible for collection via mandate from the user:
    - Any due where due date is below the last day of the billing cycle is of the type (interest + charges + penal charges) is eligible for collection.
- We will rename the bounce charges to make them dishounour charges to make it explicit for the user that since their account is in an overdue state, they are being charged an overdue fee.

Charge short name: DC (Deployed in UAT)
- Users will only be charged an dishounour charges if there was an interest o

---

## #26 — B2B Platform Dashboard v1
**Status:** Pending Review | **Last edited:** January 29, 2025 10:56 AM

**Problem:**
are we solving?**

There are around 8 B2B platforms (partners) giving business to Volt. As of now, all of them are being serviced offline by the program team (Keyur) like giving visibility of applications, reports, etc. This results in the below challenges.

- Poor perception of Volt by the partner
- Risk of data being shared outside the required accesses
- Possible chance of incorrect data being shared
- Considerable man-hours spent in generating and managing reports
- Partners’ operations/business teams can’t self-service themselves
- Enterprise partners like TDL expect a complete dashboard 

**Solution:**
?**

---

## #27 — [Platform LSP] All transactions requirements
**Status:** Done | **Last edited:** January 22, 2025 6:38 PM

**Problem:**
are we solving?**

As a platform we provide multiple APIs so that our consumers in this case:

- Internal operations team
- Loan service providers (Volt / Indmoney / Groww)

Are able to consume and accordingly process the required information in an efficient manner. It is important that we provide the right amount of information for the following reasons:

- Optimise computation and processing of information at the consumer end
- Avoid polling and high frequency calls for information to our system
- Ensuring important information is shared with the consumer (to avoid downstream effects to our 

**Solution:**
?**

We will be building capabilities for LSP/CC to show the following details:

- Withdrawal requests (with status of transactions)
- Repayment requests (with status of transactions)
- Repayment orders (to show failed or pending transaction orders)
- All completed transactions API (Statement API)

| Transaction | Description | Debit/Credit | Transaction initiation source | How will it be consumed via CC/LSP |
| --- | --- | --- | --- | --- |
| Withdrawal | Withdrawals made by the user | Dr | User | Withdrawal requests + all transactions |
| Repayment - (PG) | Repayments made by the user  | Cr | User | Repayment requests + all transactions |
| Repayment - (Mandate collections) | Mandate collection made by the NBFC | Cr | NBFC  | All transactions |
| Repayments - (Sell off) | Invocation coll

---

## #28 — [LSP] Total outstanding amount correction and over
**Status:** Not started | **Last edited:** January 21, 2025 7:32 AM

**Problem:**
are we solving?**

For a loan account there are certain particulars that are maintained to understand what is the total due that the user has against their loan account. They are described as follows:

- Principal outstanding: This is sum of the amount that the user has withdrawn minus the repaid (as partial principal repayments) to the NBFC
- Interest due - This is the amount that is due for the user from the previous billing cycle, calculated as accruals based on their principal outstanding at a daily level (currently we follow a daily accrual model)
- Charges due - This is the sum of all ou

**Solution:**
?**

- We will start passing the overdue amount details to the LSP as well as on the command centre so that it can be shown to the user in an intuitive manner
- We will be updating our revocation request validation to avoid any collateral risk to the NBFC (move from TOS to TOS + Overdue amount)
- We will add additional parameters in the foreclosure API so that the same can be passed to the user at the time of foreclosing the account

---

## #29 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #30 — [CC] Showcase the reason for freezing on CC
**Status:** Not started | **Last edited:** February 4, 2025 6:15 PM

**Problem:**
are we solving?**

Account freezing or suspension is a temporary restriction that prevents an account holder from accessing specific or all account features. This occurs for several reasons:

- Suspicious activity detection
- Policy violations
- Legal requirements
- Payment issues
- Security concerns

We have the operations team, risk team and the development team who can place an account under suspension or frozen state. 

The frozen state **also** occurs when an active account undergoes foreclosure procedure so as to prevent the user from initiating any debit transactions.

When an account g

**Solution:**
?**

We allow the maker to add a reason to freezing of an account. This reason is taken as a service request and we will be storing this in our database.

When we fetch the reasons for the freezing of an account and showcase it as a separate column on the CC when a specific loan id if fetched.

Categorising the reasons for freezing into 2 major categories:

1. Suspicious Activity
2. Credit Risk includes (these individual options which can be selected):
    1. Invalid collateral addition or valuation
    2. Incorrect Repayment addition
    3. Invalid bank account
3. Foreclosure 

The Maker via the CC can select anyone of the above reasons for freezing (feature to select the reason is already available). The account will be immediately frozen and the reason should be visible to the the opera

---

## #31 — [Platform] Handling of below 1 Rs transactions for
**Status:** Done | **Last edited:** February 3, 2025 8:48 AM

**Problem:**
are we solving?**

When a user makes repayment to their loan account for either part payment or foreclosing their account, or initiates a sell off there can arise scenarios where the user’s account goes into excess.
This excess if the account is not under foreclosure, is automatically refunded via a daily CRON job that identifies loan accounts in excess, and initiates a payout of an amount equal to excess to regularise the account.

However there can arise scenarios, where this amount is less than Rs 1, if such an amount is found in excess, the corresponding payout for the account fails, as Ca

**Solution:**
?**

We will be making enhancements in our excess job and foreclosure job to solve this problem:

- Excess job will only have accounts where excess amount will be greater than 1
- If an account has an active foreclosure request, or a pending disbursement, it will not be eligible for an excess refund and will be ignored in the excess refund job
- We will be creating transaction type “excess_adjustment” for excess refund transactions, the same will be passed as a type when doing a excess transaction
- We will be setting up transaction type accounting events for excess refund for two scenarios:
    - Excess refund below 1 Rs (liability transfer)
        - Excess COA (liability): Debit
        Excess refund liability: Credit
    - Excess refund above and equal to 1 Rs
        - Excess COA (lia

---

## #32 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #33 — Customer Lifecycle Tracking - Lien Unmarking → Rep
**Status:** In progress | **Last edited:** February 24, 2024 2:31 PM

**Problem:**
are we solving?**

- 

---

**Solution:**
?**

- Actively communicating the stages of the respective request to the user on the app.
    - Using lender APIs to automatically capture status of the user’s request and breaking down the process into steps to reduce operational load as well as aligning the user on the development of their request.
- Making the request in progress banner less apparent in the user journey to avoid creating artificial urgency in the mid of the user. (Lien removal)
- End state for foreclosure requests when loan is closed (application closed → user should be able to initiate a new journey)

---

## #34 — Shortfall communication enhancement Ignoring accou
**Status:** Pending Review | **Last edited:** February 23, 2025 8:17 PM

**Problem:**
are we solving?**

A sell off is the process of invocation of a lien on a user’s security. That is when the lender or the pledgee, invokes their right to redeem the units of a security pledged by the user with the lender.

There are two types of sell off:

- Lender initiated sell off
    - Lender initiates sell off of securities to recover outstanding amount (30 DPD)
    - Lender initiates sell of to regularise the user’s loan account (shortfall)
- User requested sell off
    - User requests a sell off due to inability to fulfil their commitments towards the credit line

Lifecycle of a sell of

**Solution:**
?**

We will be ignoring accounts under shortfall under the following condition:

V1: If an account has a non terminal collateral sell off transaction (hit collateral transactions API)

V2: If an account has an active sell off follow the following condition:

If Sum of all sale value of all collaterals ((Units blocked for sell off)*NAV(for corresponding ISIN at the time of raising sell off)) < Regulatory shortfall then include in the shortfall communication else ignore

---

## #35 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #36 — Foreclosure payment handling (EOD) repayment in fo
**Status:** Done | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

BAJAJ:

- When user foreclose the loan on Volt UI after 6 PM, we do not consider interest of same days in Net dues payable.
- This led the foreclosure rejection from the lender end.

TATA:

- We do not ask user to pay accrue penal charges and due to this foreclosure are getting rejected.

---

**Solution:**
?**

---

## #37 — Interest, shortfall, renewal table on partner dash
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- MFDs lack visibility regarding their customers' interest details, shortfall occurrences, and loan status.
    - MFDs inquire about the interest status, mandate status and interest calculation.
    - MFDs do not inform their customers about the shortfall, resulting in escalation from the customer's end.
- B2B2C customers depend on advisors to oversee their loan accounts, resulting in reduced attention to direct reminders sent by Volt.

---

**Solution:**
?**

---

## #38 — Capture foreclosure reasons from customer
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We experiencing an increasing trend in loan foreclosures, which negatively impacts AUM and retention. 

Here are the reason for foreclosure we have identified so far based on the user calling and collecting the feedback from the sales and support team:

**PRODUCT POSITIONING e(Priority 0)**

- We position ourselves as a **short term requirement**, so when the user's requirement is fulfilled the user looks to close the loan.

**LIEN REMOVAL CONFUSION (Priority 0)**

- Users don't understand how to release their collateral and hence assume that account closure is the only way 

**Solution:**
?**

- **Product Education Through FAQs - Phase 2**
    - Create categorized FAQs to address basic product queries and prevent foreclosures caused by product understanding gaps
    - Resources:
        - FAQ Management System: [[Link](FAQ%20Management%20System%20189e8d3af13a8003a2a5ff6abd88b33f.md)]
        - FAQ Content Document: [[Link](https://docs.google.com/document/d/1ojvtyjkUJdytxImRudTC5hqS6BpokB3HF8LjXxxa1W0/edit?usp=sharing)]
- **Targeted Intervention for Foreclosure Requests - Phase 1**
    - Collect specific reasons for foreclosure request
    - Present contextual benefits and alternatives based on selected reasons
    - Guide users to better solutions than foreclosure
- **Operations Team Review Process - Phase 1**
    
    A. Initial Review
    
    - Operations/Customer Succe

---

## #39 — Comms config - OTP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and *

**Solution:**
s:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

---

## #40 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #41 — Foreclosure repayment - Handle PenalInterestAccrue
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- In foreclosure request we have not handled the “PenalInterestAccruedNotDue” field in the calculation of net payable amount which is leading to the rejection of foreclosure request.

---

**Solution:**
?**

- Include the "PenalInterestAccruedNotDue" field in the calculation of the net payable.
- Display the "PenalInterestAccruedNotDue" amount on the UI.
    - The backend (BE) needs to send this field with its value to the frontend (FE), so the FE can display it on the UI and use it to calculate the amount shown to the user.
    - Outstanding interest amount should include the value of “PenalInterestAccruedNotDue”

---

## #42 — Handle excess amount in foreclosure request [TCL]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- There are no handling of excess amount for TATA customer in foreclosure flow

---

**Solution:**
?**

- When user loan account are in excess and user want to foreclose the loan then we should initiate the withdrawal for the amount equal to excess amount and once withdrawal is success then initiate the foreclosure request.
- How to identify if user account are in excess:
    - In the foreclosure details, If netPayable are in Negative then we can say that user loan account has a excess amount.
    - If NetPayable are Positive then user has to repay the amount and if NetPayable amount is in Negative then we need to raise the withdrawal amount equal to the NetPayable amount.
- Prerequisite: Need to handle “PenalInterestAccruedNotDue”
    - PRD link: [https://www.notion.so/volt-money/Foreclosure-repayment-Handle-PenalInterestAccruedNotDue-10ae8d3af13a8023b658d2852b6477f4?pvs=4](https://www

---

## #43 — Interest feature handling for TCL
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

TCL has changed the interest posting date from 1st of every month to 3rd of every month and currently interest lifecycle is handled based on 1st a posting date.

Now since TCL will post the interest on 3rd, any interest repayment made during 1st to 3rd(till interest is not posted) will get settled as Overdue interest → Overdue charges → Principal. 

---

**Solution:**
?**

1. Create interest in Volt system using admin action by upload the interest + charges due sheet manually.
2. Do not allow user to repay the interest on and before 3rd of the month via APP.
3. Do not nudge users to pay the interest amount in comms content when interest is due.
4. Payment summary page to be updates for TCL customers
    1. If users are repaying the amount b/w 1st to 3rd the settlement logic shown on the UI needs to be updated accordingly.
5. Lien removal and foreclosure Sanity needs to be done

---

## #44 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #45 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #46 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #47 — Project Elevate - LMS
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

BFL has restricted our customer to increase the credit limit.

---

**Solution:**
?**

Implement a system that enables customers to create additional loan accounts with DSP when they need higher credit limits, while providing a seamless experience to manage multiple credit lines within our platform.

Same solution should work to migrate TCL customer

---

## #48 — Repayment flow optimisation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

- When users repay amounts through the FlexiPay flow, the repayment is allocated towards charges (when due) and interest repayment (when due) for TCL and DSP customers. However, users are not explicitly informed about how their repayment is distributed across charges, interest, and principal, leading to confusion after payment completion.
    - The interest amount and status are not updated if the repayment is made through the FlexiPay flow.
    - Users are not informed that auto-debit will still be executed if repayment is made between the 1st of the month and the due 

**Solution:**
?**

---

## #49 — Shortfall experience optimisation
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- When users experience a shortfall and fail to meet it on time, lenders sell the funds on the 7th day by 12 PM. However, our app UI and communications indicate that users have 7 days to meet the shortfall.

---

**Solution:**
?**

- We need to ask user to meet short-fall within 6 days instead of 7 days
- Portfolio will be sold-off on 7th day
- Repayment of shortfall has to be done on or before 6th days before 6 PM

---

## #50 — Show interest virtual bank account to BFL customer
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Customers are using the Principal Virtual Account displayed on the Volt app for BFL customers to make their interest repayments.
- Since customers are unaware that the displayed bank account is for principal repayments only, they are mistakenly making interest payments, assuming it will cover the interest balance.
- As a result, these repayments are being allocated against the principal, leaving the interest overdue, which leads to sell-offs and customer escalations.

---

**Solution:**
?**

---

## #51 — TCL foreclosure API integration
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We are currently using the `getSummary` API to fetch foreclosure details for TCL loans. However, this approach is resulting in multiple issues that are affecting both user experience and operational efficiency.

**Solution:**
?**

<aside>
💡

The scope of this PRD is to first solve the foreclosure flow and then address the loan expiry experience.

Phase 2 will be picked up separately 

</aside>

To address the limitations of the current `getSummary` API, the following solutions have been implemented by TCL:

1. **Dedicated Foreclosure API**
    - TCL has developed a **new Foreclosure API** specifically to fetch foreclosure-related details.
    - This API will returns only the necessary data which are required to raise the foreclosure.
    - This API will also work for Expired loans.
2. **Enhancement to Receipt Posting**
    - Changes have been made to the **Receipt Post API** to allow manually posting of payments which **are not yet due**.
3. **Accurate Net Payable Calculation**
    - Once the not-due amount is 

---

## #52 — DSP Handling Sell-Off Dependencies
**Status:** Not started | **Last edited:** February 18, 2025 2:22 PM

**Problem:**
are we solving?**

The user can request to initiate a voluntary sell-off of his collateral to pay their interest or total outstanding or principle amounts. 

---

**Solution:**
?**

---

## #53 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #54 — Show accrued interest on UI
**Status:** Not started | **Last edited:** December 26, 2024 5:50 PM

**Problem:**
are we solving?**

- Users are not able to track their interest before the due date of their interest cycle
    - Users are not able to plan their withdrawals and repayments basis accrued interest on their line (it is an important decision making parameter for them)
    - Ops team estimates this basis the current POS of the user and gives approximate answers
    - Users also like to estimate their monthly interest basis accrued interest and current POS and are currently not able to do it to resolve their queries

![Screenshot 2024-05-30 at 5.13.21 PM.png](Show%20accrued%20interest%20on%20UI/Sc

**Solution:**
?**

Users will be able to track the accrued interest accumulated over the month on the dashboard

---

## #55 — [DSP] Dues collection comms
**Status:** Done | **Last edited:** August 22, 2025 3:28 PM

**Problem:**
are we solving?**

- Currently DSP is not sending collection related communications to the user -
    - ***Poor customer experience :*** This leads to user being unaware of the due dates, leading to them missing the payments, incurring bounce/penal charges
    - ***Business risk :*** This puts DSP finance (as an NBFC) at an compliance risk, as it is mandatory for NBFCs to send collections related communications to the user as per RBI regulations

---

**Solution:**
?**

---

## #56 — [Platform] Validation to Stop Un-pledging, closure
**Status:** Done | **Last edited:** April 4, 2025 2:21 PM

**Problem:**
are we solving?**

Account freezing or suspension is a temporary restriction that prevents an account holder from accessing specific or all account features. This occurs for several reasons:

- Suspicious activity detection
- Policy violations
- Payment issues
- Security concerns

We have the operations team, and risk team who can place an account under suspension or frozen state. 

The frozen state **ALSO** occurs when an active account undergoes foreclosure procedure so as to prevent the user from initiating any debit transactions while the account closure is in process.

Freezing an account

**Solution:**
?**

We will be adding some validations to stop foreclosure and un-pledging of the manually frozen accounts.

The foreclosure check will include:

1. If the account is active/expired, freeze it and continue the foreclosure process
2. In case if an account is frozen before the initiation of the foreclosure by the user, it has to be rejected.

The un-pledging check will include:

1. If the account had been frozen, don’t go forward with the un-pledging
2. If is active, then continue with the pledging

---

## #57 — E2E Sell-off Productisation 34ae8d3af13a80928d80d8
**Status:** Not started | **Last edited:** April 30, 2026 5:35 PM

**Problem:**
are we solving?

- Today, sell-off execution is a fully manual, analytics-dependent process — ops teams rely on daily risk reports, manually compute DPD and shortfall sell off amounts, select funds, prepare maker file, and initiate sell-offs via the Command Centre.
- With an average of 193 sell-off requests per day (Jan–March 2026) and a peak of upto 4000 DPD requests (as on 21st Apr 2026), this introduces significant delay between trigger and execution.
- Any error in selecting accounts for sell off , sell off amount computation, fund selection, or file preparation by analytics and ops direct

**Solution:**
?

**In scope:**
- Daily automated identification of shortfall-eligible LANs (`shortfall_ageing >= 7`) and DPD-eligible LANs (DPD > 75 trigger 1st and then 21st-of-month trigger)
- Shortfall amount and DPD amount computation per LAN using get overdue detail API and shortfall ageing data
- Ongoing sell-off detection from `fenix_sell_off_collaterals_request` and appropriate skip/adjustment logic
- 5% execution buffe

---

## #58 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #59 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #60 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #61 — Volt Plugin Knowledge Base
**Status:** Unknown | **Last edited:** Unknown

# Volt Plugin Knowledge Base # Introduction This project aims to build a unified UX writing system for Volt based on fintech best practices. The goal is to have a unified, brand-aligned tone of voice across screens, touchpoints, and teams. ## Problem - Right now we handle error case copies differently throughout the app. - Different writers/designers use different tones, leading to a fragmented experience. - No shared rules for writing error messages, CTAs, success screens, etc. - Designers or PMs often write placeholder text or inconsistent copy due to lack of writing support & time constraints. ## Solution A self-serve figma plugin where anyone can write first version of the copy that’s on-brand, on-tone, and compliant without needing support ## Approach - Align stakeholders on a unified brand voice - Setup brand voice guidlines (Tone) for cases like success, error, New features and so on. - Present guidelines that will be used as the first config for the figma app - Create the figma plugin with the help of Devs - Present a working model, to stakeholders - Take feedback and iterate if necessary - Replace copy throughout app using the figma plugin ## Brand Voice Based on the conversation with Lalit this is what volt stands for. based on these I want to define what the tone of language we want through out the app. - Call with Lalit on volt brand 1. If volt was a person how would you describe it? 1. Supportive 2. Reliable and Fast to help 3. Motivating 4. Enabler to achieve your financial needs 5. A saviour when you need most 2. Describe Volt in 3-4 words 1. Transparent, Trustworthy, Easy, Fast <aside> 💡 **Interacting with Volt should feel like:** Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless. - **Like a smart, supportive money guide** - **Your effortless, goal-driven money companion** </aside> Voice: **Smart, Supportive, Calm, and Clear.** <aside> 💡 Volt speaks like a modern financial guide — someone who knows money inside out, and explains it with warmth & clarity, not jargon. </aside> ## Scenarios / Possible Usecases - Error like PAN verification failed, No CKYC data found and so on - Success like Completion of Payment, Loan application, Increase limit and so on - Onboarding like App screenshots

---

## #62 — Loan foreclosure reasons
**Status:** Developed | **Last edited:** Unknown

# Loan foreclosure reasons Assign: Karuna Sankolli Charter: LMS Pod # Context - [x] Get list of reasons from Ranjan - [x] Make a table with what we will sell for every reason selected. - [x] Redesign FAQs page - [ ] Work with Ranjan for the FAQs page - [ ] Foreclosure landing page 3 options - [ ] Reasons for foreclosure 3 options - [ ] Reconsider page 3 options - [ ] Status of payment page 3 component 3 options - [ ] Last tracking foreclosure page options - [ ] Ability to cancel foreclosure --- [Capture foreclosure reasons from customer](../PRDs/PRDs/Capture%20foreclosure%20reasons%20from%20customer%20170e8d3af13a80ec8d7bff6a6e988d1f.md) ‣ # Figma [https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system)

---

## #63 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #64 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #65 — E2E Sell-off Productisation V1
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?

- Today, sell-off execution is a fully manual, analytics-dependent process — ops teams rely on daily risk reports, manually compute DPD and shortfall sell off amounts, select funds, prepare maker file, and initiate sell-offs via the Command Centre.
- With an average of 193 sell-off requests per day (Jan–March 2026) and a peak of upto 4000 DPD requests in a single day(on 21st Apr 2026), this introduces significant delay between trigger and execution.
- Any error in selecting accounts for sell off , sell off amount computation, fund selection, or file preparation by analytics an

**Solution:**
?

**In scope:**
- Daily automated identification of shortfall-eligible LANs (`shortfall_ageing >= 7`) and DPD-eligible LANs (DPD > 75 trigger 1st and then 21st-of-month trigger)
- Shortfall amount and DPD amount computation per LAN using get overdue detail API and shortfall ageing data
- Ongoing sell-off detection from `fenix_sell_off_collaterals_request` and appropriate skip/adjustment logic
- 5% execution buffe

---

## #66 — BRD Enhancements to Schedule & Derived Details Pro
**Status:** Completed | **Last edited:** Unknown

# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds) Last Edited: December 11, 2025 2:41 PM PRD Owner: Vaibhav Arora ## **1. Problem Statement** Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for: - Accurate repayment allocation - DPD computation - Interest/charge tracking - Reconciliation, reporting (internal and external) Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations. We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur. --- ## **2. Context: How It Should Work (High Level)** - Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule. - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule - When a transaction settles that obligation, the schedule and derived details should reflect: - obligation met - amount accounted - linkage to the transaction identifier - timestamps for audit - For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.). Finflux already follows this pattern for regular repayments. The gaps occur only for specific transaction types listed below. --- ## **3. Issues & Required Enhancements** --- ## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details*** ### **Current Behaviour** - During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line: - Accrued-but-not-yet-due interest is first made due. - Finflux then settles this newly created due using excess funds when the clear dues API is hit - However: - The **schedule table is not updated** to reflect the new temporary obligation. - The **obligation is not marked as met**. - **Derived details** are not populated with the settlement transaction. ### **Impact** - Reporting discrepancies (interest recognised vs. interest settled). - Incorrect DPD because obligations appear “unmet”. ### **Required Behaviour** Finflux should: 1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge). 2. **Immediately settle the obligation** and mark: - obligation_met = true - obligation_met_on = timestamp 3. **Populate derived details** with: - linkage to the

---

## #67 — Disbursement simulation - LMS
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
- Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula.
- Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen.
- Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum a

# Disbursement simulation - LMS Last Edited: May 22, 2026 3:49 PM PRD ETA: May 5, 2026 PRD Owner: Vaibhav Arora ## Background and Context - **Who is affected** - Borrowers using Volt (DSP Finance's LSP) who initiate withdrawal requests from their Loan Against Mutual Fund (LAMF) accounts. - All LSP partners integrated with DSP Finance's disbursement infrastructure. - DSP Finance's Risk Operations team, who are exposed to collateral shortfall risk when disbursements breach the safe limit. - **What is broken today** - The current Available Limit calculation — `AL = min(DP, SL) - POS + EM` does not account for accrued interest, charges, or scenarios where non-principal exposure grows to exceed the margin held against collateral. Two specific scenarios expose DSP Finance to risk: - **Case 1 — Collateral Removal:** After a borrower repays principal and requests maximum collateral removal, the remaining collateral may only cover the Drawing Power. Any subsequent withdrawal creates a situation where accrued interest (once booked as Interest Due) pushes total exposure above collateral value. - **Case 2 — Voluntary Sell-off:** After a sell-off settles principal, the sell-off proceeds inflate Excess Money, which inflates the Available Limit. A borrower can withdraw this excess, creating a POS that, combined with accrued interest becoming due, exceeds the remaining collateral value. - Today, the Loan Detail API value is trusted by all downstream systems (Fenix, Volt, and LSP partners) as the authoritative available limit. There is no pre-disbursement validation layer that applies the updated risk-safe AL formula before funds are transferred. - **Why it matters** - Collateral shortfall represents direct credit risk for DSP Finance — in cases of default, outstanding dues cannot be fully recovered. - The gap grows over time as accrued interest compounds, making early intervention critical. - LSP partners rely on the available limit shown to borrowers; without a simulation gate, disbursements that breach exposure limits will be processed without any check. --- ## 1. Problem Scope ### In scope - Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula. - Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen. - Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum allowed amount and enabling re-entry. - API design contract documentation to be shared with

---

## #68 — LAS CMS Confiscation and sale of securities
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

When securities are lien marked in favour of DSP Finance, it also gives the capability to the NBFC to invoke the lien to redeem the securities, this gives the proceeds from the sale of securities to the NBFC which is posted in the security holder’s loan account.

The following reasons are why there is a need for this capability:

- If the user goes into a shortfall, and is unable to regularise (DP>POS) their loan account within a stipulated time period (7 working days as defined by RBI), the NBFC is required to invoke securities to regularise the account
- If the user is ove

**Solution:**
?**

- **PMR-based validation** – Since no lien verification API is available, removal will rely on accurate and timely ingestion of PMR data.
- **Derived removal requests** – The system will generate internal removal requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – confiscation will only be approved once checker confirms task on Command centre
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Removal)

---

## #69 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #70 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #71 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #72 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #73 — Product note Excess refund Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **excess refund flow compatible with both loan types**:
    - DSP loans (auto-adjust + withdrawal allowed)
    - Co-lending loans (parked excess, no withdrawal)
- Introduce:
    - **Maker-checker flow for excess refunds**
    - **Validation layer to compute refundable excess**
- Enable:
    - Manual refund by Ops
    - Automated daily refund via CRON
- Stakeholders:
    - Primary: Ops, Fi

# Product note: Excess refund Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 26, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC Ops & Finance teams - Customers (end borrowers) - LMS / Payments systems - **What is the challenge** - In the current system: - Excess funds in a loan are: - **Auto-adjusted against dues** - **Available for withdrawal** - However, in **co-lending loans**: - Excess: - **Cannot be used for withdrawal** - **Cannot auto-adjust against dues (parked excess)** - This creates: - Customer dissatisfaction (funds blocked) - Operational dependency on batch refunds - Regulatory and reconciliation sensitivity (escrow flows) - **Why is it important** - Excess funds belong to the borrower → must be returned timely - Blocked excess reduces trust and impacts CX - Co-lending construct mandates **controlled fund flows** - Need a **unified system** that works for both: - DSP 100% loans - Co-lending loans --- ## **1. Problem scope** ### In scope - Enable **excess refund flow compatible with both loan types**: - DSP loans (auto-adjust + withdrawal allowed) - Co-lending loans (parked excess, no withdrawal) - Introduce: - **Maker-checker flow for excess refunds** - **Validation layer to compute refundable excess** - Enable: - Manual refund by Ops - Automated daily refund via CRON - Stakeholders: - Primary: Ops, Finance - Secondary: Customers --- ### Out of scope - Enabling: - Real-time auto-adjustment of excess for co-lending (future scope) --- ## **2. Success Criteria** ### Key outcomes - **Timely refund of excess** for co-lending loans - **Zero incorrect refunds** (over/under refund) - Reduced dependency on manual ops intervention ### Metrics - % excess refunded within T+1 (target: >95%) - Excess refund error rate (target: <1%) - Manual intervention rate (should reduce over time) ### Post-launch good state - Excess: - Not withdrawable (co-lending) - Automatically refunded via system or ops - Ops: - Can trigger instant refunds via maker-checker ### Guardrails - No: - Over-refunding beyond eligible excess - Refunds during foreclosure / invalid states - Impact on repayment posting / accounting --- ## **3. Solution Scope** ### Solution overview We will introduce a **unified excess refund framework** with: - **Validation engine** → determines refundable excess - **Maker-checker flow** → enables controlled manual refunds - **Daily CRON** → ensures timely automated refunds System behavior will differ based on loan type: - DSP loans

---

## #74 — Product note Foreclosure (Colending)
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure (Colending) Last Edited: May 19, 2026 2:47 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**. ### Who is impacted - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting ### What is broken today Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations: 1. **Incorrect foreclosure simulation** Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances. 2. **Pending transaction inconsistencies** Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations. 3. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring that: - Loan 90 and Loan 10 are closed - All charges and interest are posted - Excess settlement is completed 4. **Penalty and applicable charge dependency** Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment. 5. **Incorrect collateral release timing** Securities may be released before confirming that **both loan legs are closed**, which introduces risk. ### Why this is important Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to: - Incorrect payoff amounts shared with borrowers - Operational rework due to partial closures - Accounting mismatches across loan legs - Risk of releasing collateral before loan closure creating financial exposure for the NBFC This PRD defines a **colending foreclosure workflow** that ensures: - Correct payoff simulation - Transaction sequencing across loan legs - Controlled collateral release - Accurate excess settlement. --- # **1. Problem Scope** ## **In Scope** ### **Colending foreclosure simulation** Foreclosure simulation will incorporate balances from: - Loan

---

## #75 — Product note Foreclosure V2 for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure V2 for Colending Last Edited: April 24, 2026 7:43 AM PRD ETA: April 7, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across Loan 90 and Loan 10 in the Colending Loan Management System (CLMS). --- ### **Who is impacted** - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting --- ### **What is broken today** 1. **Incorrect foreclosure simulation** Foreclosure amounts are often computed using Loan 100 without fully reconciling Loan 90 and Loan 10 balances. 1. **Pending transaction inconsistencies** Foreclosure may be initiated even when pending transactions exist in CLMS, leading to incorrect payoff calculations. 1. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring: - Loan 10 and Loan 90 are closed - All dues and interest are settled - Excess is correctly handled 1. **Penalty and applicable charge dependency** Charges (such as penal charges) may be posted after repayment due to system jobs, leading to foreclosure failures. 1. **Incorrect collateral release timing** Collateral may be released before confirming closure of underlying loan legs. 1. **Excess handling gap in colending** - Excess is parked in Loan 100 - Excess does not auto-settle dues or accrued interest - There is no native way to use excess during foreclosure This leads to: - Incorrect net payable shown to users - Failed foreclosure despite sufficient excess - Manual intervention for settlement - Reconciliation gaps --- ### **Why this is important** Foreclosure is a **high-intent and customer-sensitive journey**. Incorrect handling leads to: - Poor customer experience - Increased operational workload - Financial and accounting mismatches - Risk of incorrect collateral release This PRD ensures: - Accurate payoff computation - Deterministic transaction sequencing - Proper utilization of excess - Correct closure and refund handling --- # **1. Problem Scope** ## **In Scope** ### **1. Colending foreclosure simulation** Foreclosure simulation will compute payoff using: -

---

## #76 — Risk management system LAS
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

For loans against collateral with dynamically priced assets like:

- Shares
- Mutual funds

It becomes important to ensure that all transactions and exposure given out to user against loans committed by the NBFC, are validated. As of now only the LMS was responsible for doing these validations, but as our systems and products get more complex, there is an additional need for a separate system with logic separation to validate all transactions.

Traditionally, validation of disbursals, top-ups, sell-offs, or withdrawals was handled solely within the LMS (Loan Management Syste

**Solution:**
?**

The RMS module performs the following responsibilities:

- Ingest and store market data for all pledged securities every 15 minutes.
- Compute real-time LTV (Loan-to-Value) and exposure metrics using pledged quantity and live prices.
- Raise alerts for LTV or exposure breaches.
- Raise alerts to customers on exposure breaches
- Validate user transactions that may impact risk thresholds—like disbursals, release requests, or sell-offs—against real-time metrics before allowing execution.

---

## #77 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #78 — Volt - Overdue Communication Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
The following enhancements are included in this release:

- Update overdue communication copies to include **clear repayment instructions**
- Explicitly instruct customers to **pay at least one day before the sell-off date**
- Update communication templates across:
    - SMS
    - WhatsApp
    - Email
- Improve clarity around:
    - overdue payment
    - penal charges
    - lender sell-off timelin

# Volt - Overdue Communication Enhancement Last Edited: April 3, 2026 11:14 AM PRD ETA: March 9, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Volt Money sends overdue payment alerts to customers when **interest dues are not paid by the scheduled repayment date** for their Loan Against Mutual Funds (LAMF). These communications are sent across: - SMS - WhatsApp - Email The purpose of these communications is to ensure customers are aware that: - Their **interest payment is overdue** - **Penal charges are being applied** - Failure to repay may lead to **portfolio sell-off by the lender** Currently, the communication does not clearly encourage customers to **make payment before the lender sell-off deadline**, which can result in customers attempting payment **on the last day**. Because payment settlement may take time, last-day payments can still result in **security sell-off**, leading to: - Customer confusion - Customer disputes - Increased support queries Additionally, communications do not explicitly guide customers to **make payment at least one day prior to the sell-off date**. To improve clarity and reduce disputes, Volt will update overdue communications to **explicitly instruct customers to make payment at least one day before the lender sell-off date**. **Important:** This enhancement will apply **only to DSP as a lending partner** and will **not apply to BFL or TCL portfolios**. --- # **1. Problem Scope** ## In scope The following enhancements are included in this release: - Update overdue communication copies to include **clear repayment instructions** - Explicitly instruct customers to **pay at least one day before the sell-off date** - Update communication templates across: - SMS - WhatsApp - Email - Improve clarity around: - overdue payment - penal charges - lender sell-off timeline Primary users: - Customers with **interest overdue on Volt Money LAMF accounts** Secondary users: - Customer support teams handling repayment queries - Risk and collections teams managing overdue accounts --- ## Out of scope The following items are not included in this enhancement: - Changes to **overdue calculation logic** - Changes to **sell-off trigger logic** - Changes to **penal charge calculation** - Changes to **repayment workflows in the Volt app** - Changes to overdue communications for **BFL and TCL portfolios** Rationale: This initiative focuses only on **communication clarity improvements**, without modifying underlying **collections or risk processes**. --- # **2. Success Criteria** ### Primary Outcomes **1. Reduce disputes during sell-off events** Customers clearly understand the **repayment deadline

---

## #79 — Volt - Shortfall Communication Enhancement – Due D
**Status:** Completed | **Last edited:** Unknown

**In scope:**
The following enhancements are included in this release:

- Replace **“days left” communication with an explicit due date**
- Introduce **due_date variable in shortfall communications**
- Update communication templates across:
    - SMS
    - WhatsApp
    - Email
- Introduce **penultimate-day reminder communication**
- Validate and align **overdue date logic with DSP implementation**
- Encourage r

# Volt - Shortfall Communication Enhancement – Due Date Based Messaging Last Edited: March 31, 2026 11:28 AM PRD ETA: March 9, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, Volt Money sends **shortfall alerts using a “days remaining” format** in SMS, WhatsApp and Email communications. **Who is facing the problem** - Customers with active **Loan Against Mutual Funds (LAMF)** accounts experiencing shortfall - Volt **customer support team** - Volt **risk and operations teams** **What is the challenge today** Shortfall communications currently mention the **number of days left to resolve the shortfall**, instead of clearly communicating the **exact last date by which the account must be regularised**. This creates confusion because: - Customers interpret the timeline differently - Customers attempt repayment **on the last day** - Payments may **not settle in time**, triggering **collateral sell-off** This results in customers contacting support claiming they **were not aware of the final resolution deadline**. **Why this is important** - RBI regulations require the **RE to regularise the account within 7 days of shortfall** - Operationally, customers must repay **before the deadline** to allow settlement - Current communication format leads to: - Increased **customer support queries** - Poor **customer experience during sell-offs** - Higher **dispute probability** To improve clarity, Volt will move from **“days remaining” communication to a clear due-date based communication format**. --- # **1. Problem Scope** ## In scope The following enhancements are included in this release: - Replace **“days left” communication with an explicit due date** - Introduce **due_date variable in shortfall communications** - Update communication templates across: - SMS - WhatsApp - Email - Introduce **penultimate-day reminder communication** - Validate and align **overdue date logic with DSP implementation** - Encourage repayment **before the due date** to allow processing time Primary users: - Customers with shortfall in their Volt Money credit line Secondary users: - Customer support team handling shortfall related queries - Risk and collections teams managing collateral sell-offs --- ## Out of scope The following items are not included in this enhancement: - Changes to **shortfall calculation logic** - Changes to **liquidation timelines** - UI changes inside the Volt customer dashboard Rationale: This initiative focuses only on **communication clarity improvements**, without modifying underlying **risk management processes**. --- # **2. Success Criteria** ### Primary Outcomes **1. Reduce customer confusion during sell-off events** - Reduction in **support tickets related to shortfall deadline confusion** **2. Improve shortfall resolution behaviour** -

---

## #80 — [Platform] Foreclosure handling to support Volt fo
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

A loan account has the following particulars:

- Charges due
- Penal charges due
- Interest due
- Principal oustanding
- Interest accrued not due
- Excess

Whenever a user makes a repayment, it goes through a set apportionment strategy:

Interest overdue → Charges overdue → Interest due → Charge due → Principal outstanding → Excess

Note that the repayments cannot settle interest accrued as it is not due, interest accrued is posted at the end of the billing cycle (becomes due) and then can be settled either via making repayments or via mandate presentation to the user’s loan

**Solution:**
?**

We will allow the LSP to pass an optional parameter called (Is foreclosure payment) in the create repayment order request.

<aside>
🚨

Please note that we will not be validating the amount (and if it satisfies foreclosure validations) for the account

</aside>

For this repayments, there will be an additional step in the payment workflow for the following validation:

- If Excess amount ≥ Accrued interest and TOS=0, clear dues
- If Excess amount < Accrued interest or TOS≠0 then do not clear dues

<aside>
⚠️

Please note that these payments will not go through a checker approval workflow

</aside>

---

## #81 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #82 — LSQ Swach
**Status:** Unknown | **Last edited:** Unknown

# LSQ Swach **Title:** LSQ Opportunity Management – Solution Document **Date:** 18/07/2025 **Version:** v1.0 --- ## 🔷 Section 1: Customer Journey Solutioning ### 🔹 Objective To transition from a lead-centric to an opportunity-centric model in LSQ, enabling granular tracking across different types of customer interactions and ensuring all workflows are governed through opportunity objects. --- ### ✅ Key Requirements ### 1. Opportunity Types Configuration for Customers Set up the following distinct opportunity types in LSQ: - **Main Application (LAMF)** - **Enhancement** - **Foreclosure** - **LAS** (To be configured at a later stage) - **Renewal** Each opportunity type must be independently configurable, with distinct stages, activities, and associated automations. --- ### 2. Opportunity Attribute Support - All relevant **lead fields** (except name, email, and phone) will be replicated in the opportunity object. - A one-time schema sync between the LSQ backend and opportunity fields will be done to maintain consistency. - The Opportunity object will act as the **source of truth** for all downstream processes and reporting. --- ### 3. Lead to Opportunity Migration - All existing leads (excluding core identifiers: name, email, phone) will be migrated into new opportunities. - Migration logic will ensure backwards compatibility and data integrity. - **The migration from lead to opportunity will be interdependent, as all current flows are tightly integrated. Changes must be deployed simultaneously—partial implementation without complete migration is not feasible.** --- ### 4. Activity Management - Activities will be recorded and managed at the opportunity level, based on opportunity type. - Post-activity workflows will be executed based on opportunity state transitions. --- ### 5. Field Directionality - **One-way sync** from Opportunity → Lead for core fields (name, email, phone). - No data will flow from Lead → Opportunity to avoid overwrites. --- ### 6. Lead Automation Deprecation - Legacy lead-level automations (routing, field updates) will be **disabled**. - All process automations will now be driven by opportunity logic and configuration. --- ## 🔷 Section 2: Partner Journey Solutioning ### 🔹 Objective To establish a dedicated flow for managing the lifecycle of Partner (MFD) leads and activities using a structured, opportunity-driven model. --- ### ✅ Key Requirements ### 1. New Partner Lead Table - Introduce a **dedicated database table** for Partner (MFD) leads. - This will sync with LSQ and create a new partner lead distinct from the customer lead table. --- ### 2. New Opportunity Type: **MFD Activation** - Dedicated opportunity type

---

## #83 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #84 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #85 — Term Loan Customer Statements
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers availing term loans against mutual funds will want to have a clear visibility of their **collateral, loan obligations, tranche-level details, and closure status**. These statements will help in solving the below:

- Customer confusion on pledged securities and their valuation.
- Lack of transparency around principal outstanding, EMI dues, and charges at the loan and tranche level.
- Difficulty in obtaining official proof of loan closure (No Dues Certificates).
- Increased customer support queries and operational overhead for servicing teams.

We need a standardized

**Solution:**
?**

We will design and deliver **five standard customer statements** for the Term Loan Against Mutual Funds product in V0:

1. **Holding Statement**
    - We will be providing this to the customer so that they are informed about their Holdings with us.
2. **Statement of Accounts (Loan and Tranche)**
    - These documents will help the customer with an understanding about their Dues and transactions.
3. **Loan and Tranche No Dues Certificates (NOC) - Loan and Tranche**
    - When a Loan or a Tranche is closed/foreclosed we will be providing these statements.

---

Documents which CRED shares with their customers in their current product:

At loan level:

- sanction letter
- ⁠holding document

At each Tranche level:

- Loan agreement
- ⁠ key fact statement

If Tranche is closed

- NOC docum

---

## #86 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #87 — Term Loan Excess Handling and Refund
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, all repayments (via VA or PG) can result in excess funds being received from the borrower due to multiple reasons such as pre payments, duplicate transactions, or rounding differences.

Without a clear and automated excess handling logic, this can lead to:

- Incorrect allocation of payments across tranches or dues.
- Customer confusion and complaints regarding refund timelines.
- Operational inefficiencies due to manual intervention in refund processing.
- Incorrect accounting treatment if prepayment or refund rules are not consistently applied.

We aim to design

**Solution:**
?**

---

## #88 — Term Loan Foreclosure
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

For Borrowers:

•	Interest burden: Reduces overall interest paid over the loan/tranche tenure.

•	Debt-free sooner: Achieves financial freedom earlier than planned.

•	Flexibility: Allows reallocation of capital or freeing up of credit limits.

For Lender/Business:

•	Reduces credit risk: Full repayment eliminates the risk of future defaults.

•	Recycling capital: Frees up capital for new disbursements, improving portfolio turnover.

---

**Solution:**
?**

---

## #89 — Term Loan Manual Repayments(PG)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

For Borrowers:

•	Multiple payment options: Cards, UPI, netbanking, etc.

•	On-demand payments: Can make ad-hoc part-payments, overdue clearance, or foreclosure instantly.

•	Better experience: Real-time confirmation and receipts. 

•	Convenience: Removes friction of doing manual transfers for loan repayment.

For Lenders:

•	Improved collections efficiency: Easier for customers to pay resulting in fewer missed EMIs.

•	Faster settlement: PGs provide quick transaction processing.

•	Reduced operational cost: Less manual reconciliation vs cheque/DD payments.

•	Scalable: Hand

**Solution:**
?**

---

## #90 — Term Loan Manual Repayments(VA)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers rely on LSP app or automated mandate flows for repayments. However, some customers may want to make repayments directly to DSP (e.g., via bank transfer). There is no simple mechanism for customers to pay directly outside the LSP ecosystem.

Without a Virtual Account (VA) option:

- Customers lack flexibility in repayment methods.
- Ops team faces reconciliation challenges for direct transfers.

---

**Solution:**
?**

Enable repayments via static Virtual Accounts (VA) mapped per customer. Customers can transfer funds directly to DSP, and the repayment will be posted in the Loan Management System (LMS) with appropriate apportionment, re-amortisation, or foreclosure handling.

---

---

## #91 — Term Loan Prepayments and Excess Handling
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
Are We Solving?**

- Customers need to be provided with an option to pay their EMIs as and when they want in order to avoid higher delinquencies and bad customer experience.
- Customers needs a structured way to prepay specific tranches/EMIs in their term loans.
- This creates customer dissatisfaction, potential regulatory risk, and inefficient fund management for the lender.
- Without proper foreclosure/prepayment support, customers may:
    - Face higher effective interest costs.
    - Avoid early repayment, reducing lender’s portfolio efficiency.

**Problem Statement:**

We need to design a

**Solution:**
?**

---

## #92 — Term Loan Sell off
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
Are We Solving?**

- When customers miss repayment obligations / goes into shortfall / goes into high risk category, the lender faces credit risk exposure and delayed recovery of dues.
- Without a transparent process, collateral liquidation may lead to:
    - Operational inefficiencies.
    - Customer disputes regarding how proceeds are applied.
    - Regulatory compliance gaps.
- There is a need for a standardized, rule-based collateral sell-off mechanism to ensure timely recovery and clear apportionment of proceeds

---

**Solution:**
?**

---

## #93 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #94 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #95 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #96 — Content
**Status:** Unknown | **Last edited:** Unknown

# Content 1. Title: Loan offer 2. Hero details: 1. Selected loan amount. 2. Credit limit available. 3. Benefits: 1. Trusted lender Tata capital 2. Unlimited withdrawals 3. Repay principal anytime 4. Pay interest only on what you withdraw 5. Monthly Interest only EMI of only ₹862 for ₹1,00,000 withdrawal at 10.49% interest (Interest should be communicated upfront) 4. Charges: 1. Interest rates: 10.49% p.a. 2. Early repayment/ foreclosure: Free 3. Withdrawals: within 4 hours 4. One time processing fee (excl. GST): ₹840 1. Processing fee is charged once in the whole term 5. Stamp duty (as per registration state): ₹260 6. Term: 36 months (Renewal available) 5. CTA: 1. Withdraw in 4 steps

---

## #97 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Pledging will not affect the growth, Financial goal for which you started, long term plan gets hampered, no cibil requirement, Repay any time, Being in control, Reducing interest, Kevin (Servicing): unpledge request 10% buffer, shortfall, bad sell off experience, change in Sanction limit Mahesh: NBFC license, TATA and Bajaj, Names: Trust Naveen: - No brand val - GST india - NBFC license - Lenders