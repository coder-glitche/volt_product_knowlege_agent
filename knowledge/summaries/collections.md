# Current State: Collections

> Auto-generated from 109 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Master collections PRD (NBFC)
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

## #2 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #3 — [Platform] Callbacks for LSP APIs for core servici
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

## #4 — CAMS min_unit Validation for LAMF Lien Transaction
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

## #5 — LSQ Chat workflow - Phase 1
**Status:** In progress | **Last edited:** May 22, 2026 2:25 PM

**In scope:**
- Chat-to-ticket mapping for every incoming conversation
- Ticket lifecycle management (Open, Pending, Overdue, Resolved, Closed)
- SLA tracking (First Response Time, Resolution Time, Overdue)
- Automatic ticket creation for non-working hours and holidays
- Assignment of chats only to available agents
- Agent visibility into past chats and existing tickets
- Mandatory disposition capture for every

# LSQ Chat workflow - Phase 1 # **WhatsApp Customer Support – End-to-End Chat Process Note** # **Objective** The objective of this process is to transform WhatsApp-based customer conversations into a **structured, ticket-driven support system** using LeadSquared as the system of record. This process aims to ensure that every customer interaction is: - **Trackable** through ticket creation and lifecycle management - **Actionable** via proper routing, assignment, and SLA-based handling - **Contextual** through unified visibility of past interactions and tickets - **Measurable** using key metrics such as First Response Time (FRT), resolution time, and First Contact Resolution (FCR) - **Insight-driven** through mandatory disposition capture and outcome tracking - **Customer-centric** by enabling timely responses and feedback collection (CSAT) 👉 Ultimately, this enables **end-to-end visibility, operational control, and continuous improvement of customer experience and support performance**. ## Problem Statement (Final) The current WhatsApp-based support system, built on WATI, operates as a **messaging layer rather than a structured support system**, resulting in gaps across **execution, visibility, and performance measurement**. # 1. Execution Gaps - Chats are not systematically classified into open, pending, or closed states - Conversations received during non-working hours and holidays are not reliably captured or prioritized - Chats are assigned without validating real-time agent availability - There is no standardized workflow for handling, resolving, and closing chats Result: Customers experience **delayed responses, missed interactions, and inconsistent support journeys** | **Holiday Break Up** | | | | | | --- | --- | --- | --- | --- | | **Month** | **N** | **Y** | **Grand Total** | **%** | | Jan'26 | 5143 | 649 | 5792 | 11.21% | | Feb'26 | 6809 | 96 | 6905 | 1.39% | | Mar'26 | 5129 | 1399 | 6528 | 21.43% | | **Grand Total** | **17081** | **2144** | **19225** | **11.15%** | ### 2. Visibility & Control Gaps - There is no real-time view of active, unanswered, or overdue conversations - SLA metrics such as First Response Time (FRT) and resolution time are not consistently tracked or enforced - Missed chats (no response within SLA) are not identified or monitored Result: Operations function **reactively**, with limited ability to manage workload or ensure service quality | **Expired chats Break Up** | | | | | --- | --- | --- | --- | | **Month** | **N** | **Grand Total** | **%** | | Jan'26 | 41 | 5792

---

## #6 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #7 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #8 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #9 — Enhancement Of STP NSTP validations for Bulk sell
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

## #10 — STP validation for Bulk Sell off
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

## #11 — Consent Architecture FE requirements
**Status:** Not started | **Last edited:** May 15, 2026 5:50 PM

**Problem:**
are we solving?**

In reference to the recent RBI Digital lending guidelines directions (2025)as well as TRAI regulations , DSP need to capture few additional consents from the customer in the lending journey to be compliant .Following are the guidlines that shaped these consent requirements

1. Reserve Bank of India (Non-Banking Financial Companies – Credit Facilities) Directions, 2025 (Digital Lending)
2. Telecom Commercial Communications Customer Preference Regulations, 2018.
3. Digital Personal Data Protection (DPDP) Act, 2023 & its Rules. (This will be effective from May 2026, so currentl

**Solution:**
?**

---

## #12 — Dues Comms Updation
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

## #13 — [Platform] Foreclosure handling and enhancement
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

## #14 — Credit Bureau Reporting Comms
**Status:** Pending Review | **Last edited:** March 19, 2026 11:57 AM

**Problem:**
are we solving?

- DSP Finance is required by RBI regulations to report borrowers with outstanding interest dues to credit bureaus.
- Currently, **no communication is sent to borrowers at the time of reporting** — creating a regulatory compliance gap and leaving borrowers unaware of adverse credit events being filed against them.

- As reporting frequency increases from **2x/month (15th, EOM) to 4x/month (9th, 16th, 23rd, EOM) from July 1, 2026**, the gap scales without an automated solution in place.

---

**Solution:**
?

---

## #15 — Improving Mandate Conversions
**Status:** In progress | **Last edited:** March 17, 2026 4:46 PM

**Problem:**
are we solving?

- **Drop offs** in API-based eNACH mandates (due to vendor, bank or customer issues).
- **Drop-offs during Digio SDK invocation** due to performance/UI issues or trust gap.
- **Lack of modern mandate options** like UPI Autopay, which offers faster setup and better UX.
- **Inflexibility in fallback options**, e.g., esign/physical not clearly surfaced or too complex.
- **No recovery mechanisms**: Failed mandates are not followed up with retries, reminders, or alternate suggestion
- Problem identification
    - Digio SDK does not get invoked when the user chooses to set up autopa

**Solution:**
?

---

## #16 — Chat CSAT and DSAT Capture WATI
**Status:** Not started | **Last edited:** June 24, 2025 5:00 PM

# Chat CSAT and DSAT Capture <> WATI ## 🧩 **Objective** To capture structured customer satisfaction (CSAT) and dissatisfaction (DSAT) data via a chatbot workflow that can be automatically stored, tagged, and actioned via escalation or closure, based on customer responses. --- ## 📌 **Platform** **Tool Used:** **WATI** WATI is used to automate and manage the chatbot-based feedback collection journey on WhatsApp. --- ## 🧭 **User Journey Overview** 1. Agents initiates feedback collection chatbot after service interaction. 2. Customer gives a feedback rating (1 to 3 scale). 3. Depending on the rating: - DSAT (Not Satisfied1 or 2): Capture reason and offer callback. - CSAT (Satisfied)3): Thank the customer and end. 4. Store all responses in a Google Sheet and update chat status. --- ## 🤖 ⏳Wati CSAT Automation **Flow :** --- ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image.png) Updated Flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%201.png) Old Flow: ## Customer experience in the CSAT Automation flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%202.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%203.png) **Bot Auto closing the chat and ending the chatbot flow once the chatbot flow is completed by customer:** ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%204.png) Updated Journey: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%205.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%206.png) ## 🔧 **Flow Components** ### 1. **Initiation** - **Step:** Send Message - **Message:** Hi {{name}}, Can you please share with us your valuable feedback? Instead, it should be this *Hey!, How was your experience with us today?* *A) Satisfied* *B) It was okay/Average* *C) Not Satisfied* --- ### 2. **Tagging & Storage** - **Set Tags:** Mark feedback process started (e.g., `feedback_triggered`) - **Google Spreadsheet:** Record initial engagement - This tag is used to record the agent bot initiation time and also this can be used as the tat for resolving the ticket even if the customer do not fill the feedback options --- ### 3. **Feedback Rating** - **Step:** Button Input - **Message:** Please rate us from 1 to 3 - 1 (Not Satisfied) - 2 (Satisfied) - 3 (Very Satisfied) --- ### 4. **DSAT Handling (Rating 1 or 2)** - **Step:** Button Input - **Message:** We are sorry your experience wasn't great. Could you help us improve by sharing what went wrong? - Yes, Please Call Me - Just Share Feedback - **Step:** Button Input (Detailed Issue) Can you help us understand what went wrong? - Delay in Service - Poor Support - App/Portal Issues - **Storage:** Log issue category and callback preference to Google Sheet - **Tagging:** e.g., `CSAT`, `Feedback`, or `issue_logged` --- ### 5. **CSAT Handling (Rating 3)** - **Step:** Direct conditional path - **Message: @Name,**

---

## #17 — DSP UPI Autopay Integration for PhonePe
**Status:** Done | **Last edited:** June 2, 2025 5:38 PM

**Problem:**
are we solving?**

- NBFCs using NACH mandates face delays in mandate registration and activation due to dependency on bank processing times (T+2 to T+7 days).
- Physical NACH mandates have high failure rates due to signature mismatches, and bank rejections, leading to delayed interest collection.
- Borrowers often drop off during NACH mandate registration because it requires physical forms, wet signatures, or authentication(Aadhaar, Netbanking, or debit card), leading to lower activation rates.

---

**Solution:**
?**

UPI Autopay is the ideal solution for NBFCs looking to improve digital lending collections and interest payments. It offers a faster, easy to set up, cost-effective, and automated way to handle recurring payments compared to traditional NACH mandates.

---

## #18 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #19 — DSP UPI Autopay Integration for NBFC
**Status:** In progress | **Last edited:** June 16, 2025 2:41 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.
- Physical NACH mandates have hi

**Solution:**
?**

UPI Autopay is the ideal solution for NBFCs looking to improve digital lending collections and interest payments. It offers a faster, easy to setup, cost-effective, and automated way to handle recurring payments compared to traditional NACH mandates.

---

## #20 — Disbursement workflow optimisations
**Status:** In progress | **Last edited:** June 10, 2025 4:23 PM

**Problem:**
are we solving?**

---

- Currently if there is a disbursal failure due to debit cycle failure during a billing cycle change, then we are not able to execute a partial return because the SOA posting of charges have not been done. We have seen 4 such cases in the month of April and May
- Handling parallel disbursement requests from LSPs to solve for financial risk and multiple payouts

**Solution:**
?**

---

---

## #21 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #22 — [DSP] Mandate enhancements Handling of charge coll
**Status:** Pending Review | **Last edited:** July 25, 2025 3:49 PM

**Problem:**
are we solving?**

---

Finflux currently does not support configuring a future-dated due date while posting charges. This limitation results in a suboptimal customer experience in the following scenarios:

1. **Charges Posted Between 1st–7th of the Month**
    
    These charges, although intended to be due on the 7th of the *following* month, are treated as due within the *same* month. As a result, collection attempts are initiated prematurely, leading to confusion or dissatisfaction for users expecting the deduction only in the next billing cycle.
    
2. **Charges Posted Between 7th–19th o

**Solution:**
?**

---

## #23 — Axis bank e-collect API integration for virtual ac
**Status:** Done | **Last edited:** January 5, 2025 1:42 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

Problems are divided between two key stakeholders:

- NBFC (operations/business/product)
- Customers

NBFC 

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted (Reconciliation also becomes very tough as

**Solution:**
?**

DSP will be integrating with Axis bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

Steps for accepting a VA payment:

- NBFC gets a e-collect code
- NBFC appends a unique reference number (for each loan) and shares the virtual account with the customer (total length has to be less than or equal to 28 characters where first 6 characters would be the e-collect code).
    - To make the bank account more readable, we can optimise the account number 
    
    Benchmarking: (Two possible ways alphanumeric and numeric)
        - Account number: VCKYCDSPFINA8072 (CKYC)
        IFSC code: IBKL0000011
        - Account number: 2

---

## #24 — [Platform] Mandate collection BRE optimisation
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

## #25 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #26 — [Platform LSP] All transactions requirements
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

## #27 — [LSP] Total outstanding amount correction and over
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

## #28 — Yes bank e-collect API integration for virtual acc
**Status:** Done | **Last edited:** January 20, 2026 3:53 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

Problems are divided between two key stakeholders:

- NBFC (operations/business/product)
- Customers

NBFC 

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted (Reconciliation also becomes very tough as

**Solution:**
?**

DSP will be integrating with Yes bank ([refer this for benchmarking exercise](NBFC%20Virtual%20Accounts%20for%20Repayments%20(Alignment)%2034ec85249bc046dba5145ac1ea16858d.md)) e-collect APIs to create, validate and accept VA payments from customer.

Steps for accepting a VA payment:

- NBFC gets a e-collect code
- NBFC appends a unique reference number (for each loan) and shares the virtual account with the customer (total length has to be less than or equal to 28 characters where first 6 characters would be the e-collect code).
    - To make the bank account more readable, we can optimise the account number 
    
    Benchmarking: (Two possible ways alphanumeric and numeric)
        - Account number: VCKYCDSPFINA8072 (CKYC)
        IFSC code: IBKL0000011
        - Account number: 22

---

## #29 — [Platform] Handling of below 1 Rs transactions for
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

## #30 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #31 — Shortfall communication enhancement Ignoring accou
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

## #32 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #33 — Bajaj PG
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to integrate the **BAJAJ Payment Gateway** to streamline the collection of principal and interest repayments.
- Currently, with our **CC Avenue integration for BAJAJ repayment collection**, the repayment accounting process is manual, causing delays in reflecting repayments in the Statement of Account (SOA).
- By integrating the **BAJAJ Payment Gateway**, the repayment accounting process will be automated and realtime, similar to how it functions with the **TATA Payment Gateway**.

---

**Solution:**
?**

---

## #34 — Interest, shortfall, renewal table on partner dash
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

## #35 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #36 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #37 — In app user review [Play store]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We currently do not collect user experience feedback directly at key moments in the app journey, which has led to the following challenges. 

- **Missed Pain Points:** Without timely feedback, we risk missing critical pain points during specific stages of the app journey, such as loan applications, payments, or withdrawals. These missed insights can result in unresolved issues, leading to decreased user satisfaction.
- **Lost Improvement Opportunities:** Journey-based feedback offers real-time insights into what’s working and what needs improvement. Without this feedback, we

**Solution:**
?**

---

## #38 — Interest feature handling for TCL
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

## #39 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #40 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #41 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #42 — Repayment flow optimisation
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

## #43 — Rounding of Accrued Interest before Posting bill a
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**In scope:**
**

- Rounding logic implementation before **posting accrued interest** on billing date.
- Update interest posting jobs to use the rounded value.
- Update ledger to reflect the rounded amount.
- Audit log and internal reporting to capture both actual accrued and posted amount for reconciliation.
- Penal should only apply on overdue interest amount >100

---

## #44 — Setup new and fix existing MIS for lender BFL and
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Setup new and fix existing MIS for lender BFL and TCL

---

**Solution:**
?**

---

## #45 — Show interest virtual bank account to BFL customer
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

## #46 — Volt Mandate re-registration Post loan
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

In the current LOS journey, users are required to add their bank account and complete mandate registration as part of the loan application process. However, after the loan account is created, users may face situations where they need to re-register the mandate or update their bank account. These situations typically arise due to:

1. Initial mandate registration failure
2. Revocation of mandate by the user
3. User’s intention to change the previously added bank account (e.g., convenience, account freeze, operational issues) — applicable across all lending partners

At presen

**Solution:**
?**

- **Mandate and bank account details visibility:** On the account details page, show bank account information and mandate registration status (registered / not registered / pending).
- **Conditional Actions & Validations based on mandate status:**
    - If mandate is **registered**:
        - User can attempt to **add a new bank account (max 5 bank account is allowed to add from UI)** and **set up mandate** on the new account.
            - For both the lenders(DSP & TCL), Bank account for the disbursal and mandate should be always same.
            - Every time user try to setup mandate (switch mandate) on the bank account either new or old, bank verification using penny drop needs to be done for both DSP and TCL.
        - **Validation:** If the user **fails to add or verify the new

---

## #47 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #48 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #49 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #50 — TATA PG dulplicate refNo validations
**Status:** In progress | **Last edited:** December 9, 2024 5:43 PM

**Problem:**
are we solving?**

We're addressing a critical payment reconciliation issue where:

1. The bank occasionally generates duplicate reference numbers for two different payments.
2. This leads to failed accounting of repayments in the statement of accounts(SOA) of the customer in TATA for repayments with SUCCESSFUL transaction status from the TATA Payment Gateway.

---

**Solution:**
?**

---

## #51 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #52 — [Platform] Risk report
**Status:** Done | **Last edited:** December 20, 2024 2:26 PM

**Problem:**
are we solving?**

As an NBFC it is important to keep a keen eye on potential risk to the organisations, these risks can be in terms of:

- Financial risk (overdue customers)
- Operational risk (Customers without active mandate set ups)
- Compliance / Regulatory risk (Customers with high AML risk / Bureau risk / Expiring KYC)

We need to solve for visibility of the same so that the risk operations team can actively track and monitor potential risk to the organisation and accordingly take necessary measures.

---

**Solution:**
?**

We will be building a risk report, which will be scheduled to the risk operations team at a regular cadence. 

The operations team will also be able to generate this report via the command centre and download it for internal tracking. This report will be access controlled and will only be able to be tracked by the risk team.

Correspondingly we will be introducing a new role, “Risk operations” which will have access to a basic approval access and additionally will have access to the risk report within the report section.

---

## #53 — Cashfree PG integration
**Status:** Pending Review | **Last edited:** August 5, 2025 3:56 PM

**Problem:**
are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

**Solution:**
?**

---

## #54 — [Platform] RTA portfolio API integration
**Status:** Done | **Last edited:** August 25, 2025 8:02 PM

**Problem:**
are we solving?**

As an NBFC that offers loans against mutual fund, we have the capability to let the user fetch their securities, select eligible funds and then allowing them to pledge the corresponding securities in the name of the NBFC. 

This allows the NBFC to give the corresponding limit to the user in return, which they can then use for a myriad of use cases.

Since mutual funds (now) are a digital security, and only the pledge (contract between NBFC and the investor) there are potential collateral/potential risks that can arise between the user pledging/invoking/revoking the securitie

**Solution:**
?**

We will be integrating with portfolio APIs of the RTAs for three core collateral transactions in our system to validate the requests synchronously.

- Lodgement
- Revocation
- Invocation

The APIs give response at a combination of an ISIN + Folio + Lien marking number

KFIN Request body:

```json
{
"PortfolioLienRequest": {
"InvPan": "AECPC9871K",
"RequestID": "5000061609",
"AgentCode": "ANJ4718979"
}
}
```

KFIN API (Sample response):

```json
{
    "Dtinformation": [
        {
            "Return_Code": 0,
            "Return_Msg": "Success"
        }
    ],
    "DtData": [
        {
            "RequestID": "200003152175",
            "AgentCode": "ATE4719997",
            "mode": "Pledged",
            "InvestorPAN": "CLFPA9890J",
            "InvestorName": "Vaibhav Arora",
     

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

## #56 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

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

## #58 — VKYC Integration PRD
**Status:** In progress | **Last edited:** April 23, 2026 9:30 AM

**Problem:**
are we solving?**

We need to implement a regulatory-compliant, secure, and operationally resilient agent-assisted Video KYC(vKYC) process for LAMF customers that:

- Ensures completion within RBI-prescribed timelines (72-hour KYC window)
- Handles real-world Internet instability (call drops, reconnects)
- Maintains audit-grade recording integrity
- Enables structured governance via agent and auditor layers
- Enforces geo-validation (India-only compliance)
- Provides tamper-proof audit trails
- Prevents fraud via face match and SOP-based verification

Without this system:

- VKYC may breach re

**Solution:**
?

We will implement a DSP-orchestrated, Hyperverge-powered, DSP agent-assisted vKYC lifecycle with the following pillars:

---

## #59 — Admin tool migration to Appsmith
**Status:** In progress | **Last edited:** April 14, 2025 2:14 PM

**Problem:**
are we solving?**

- The support and ops teams currently rely on two separate tools (admin tool & service dashboard) to handle customer queries and unblock the customer
- The admin tool requires extensive training since its actions are standalone, lacking context on their use cases, and limitations
- Access control, error handling, education, high effort

---

**Solution:**
?**

---

---

## #60 — VA Repayment Handling [Volt LMS]
**Status:** Not started | **Last edited:** April 10, 2025 10:50 AM

**Problem:**
are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

**Solution:**
?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

---

## #61 — UPI Autopay
**Status:** In progress | **Last edited:** April 1, 2026 11:46 AM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

**Solution:**
?**

UPI Autopay is the ideal solution for NBFCs looking to improve digital lending collections and interest payments. It offers a faster, easy to setup, cost-effective, and automated way to handle recurring payments compared to traditional NACH mandates.

---

## #62 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #63 — Ai optimisation in current design workflow
**Status:** Unknown | **Last edited:** Unknown

# Ai optimisation in current design workflow - Prompt SO right now the design process at volt **AI is used by UX pros as a thought partner and reviewer** - Resources https://www.userinterviews.com/ai-in-ux-research-report There is around following major steps when it comes to designing - Problem identification - Prioritisation - Benchmarking - Building a user flow - Working on wireframes - Final design Methodologies for problem identification - User Interviews - Surveys - Synthesis of data - Requirements/Insights from the data Benchmarking - Exploration with competitors - Exploration of layout, components, illustrations Building user flow - User journey map - Information architecture - Technical capabilities - Information per screen and hierarchy - Scoping based on the existing designs Working on wireframes - Visual hierarchy - Communication clarity - Navigation - Need to evaluate screens based on :Navigation Ease, Information Clarity, Error Recovery Final designs - Emotional Triggers, Actionability, Consistency, - Illustration design - Interaction with motion --- ## Problem Identification ### User Research - **Automated data analysis** : Transcription, analysis, and synthesis of user research data. - **Sentiment analysis** to identify pain points from user feedback - **Pattern recognition** to spot recurring issues that humans might miss - **Natural language processing** to extract insights from unstructured user comments ### Desk Research - Scanning research papers on psychology eg. Indians’ behaviour in 2020, market trends Eg. How genZ interacts with money, etc, Understanding fintech domain Eg. Understanding how NACH and UPI Autopay works oversimplified. - Tools https://www.perplexity.ai/ https://consensus.app/ https://elicit.com/ ### Process - Designer/PM will take user interviews with the ‣ using ai to generate questionnaire based on the problem statement at hand. - Ai will help to synthesise the data analysis based on the user interview. # Current design workflow [https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system) # Optimized AI workflow 1. Qualitative data collection - Questionnaire for Surveys and User interviews - Desk research - Tools: Perplexity - Dashboard for CS Tickets - How to build this. ### **1. Centralize All Ticket Data** Export data from Zendesk, WhatsApp, etc. into a single table or sheet. Include fields like user message, date, channel, and status for context. --- ### **2. Analyze with AI (GPT or ML Tools)** Use GPT to extract pain points, tag themes, and identify patterns. Alternatively, use BERTopic or clustering models to detect recurring issues. --- ### **3. Summarize & Visualize Insights** Group findings by theme, volume, and sentiment in a dashboard or table. Highlight

---

## #64 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

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

## #66 — API flow for KFS and Agreement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

As a platform, there are multiple ways through which LSPs can integrate with our platform, our current implementation offers a redirection flow for collecting KFS consent and Agreement signatures.

In the redirection flow, the customer’s IP and acknowledgement/ signing timestamps are consumed. However not all LSPs would be comfortable with redirecting the users to a different URL for the following reasons:

- They want to own the customer experience (having a different UI will impact their user journey).
- Redirection URLs often require internal approvals to whitelist domain

**Solution:**
?**

We will be decoupling the existing sequential process of Key Fact Statement (KFS) and Agreement generation by building independent APIs. This will enable Loan Service Providers (LSPs) to:

- Generate KFS and Agreement documents separately.
- Collect KFS acknowledgements and Agreement signatures independently via APIs.

This modular approach enhances flexibility and improves integration capabilities for partner platforms.

Additional changes:

- **Validation Layer:** Implement robust validation mechanisms to ensure that all collected data and process flows remain compliant with regulatory guidelines and internal business rules.
- **Command centre changes:** Implement changes to enable operations team to identify, and accordingly handle different sign methodologies separately

---

## #67 — BRD Enhancements to Schedule & Derived Details Pro
**Status:** Completed | **Last edited:** Unknown

# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds) Last Edited: December 11, 2025 2:41 PM PRD Owner: Vaibhav Arora ## **1. Problem Statement** Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for: - Accurate repayment allocation - DPD computation - Interest/charge tracking - Reconciliation, reporting (internal and external) Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations. We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur. --- ## **2. Context: How It Should Work (High Level)** - Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule. - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule - When a transaction settles that obligation, the schedule and derived details should reflect: - obligation met - amount accounted - linkage to the transaction identifier - timestamps for audit - For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.). Finflux already follows this pattern for regular repayments. The gaps occur only for specific transaction types listed below. --- ## **3. Issues & Required Enhancements** --- ## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details*** ### **Current Behaviour** - During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line: - Accrued-but-not-yet-due interest is first made due. - Finflux then settles this newly created due using excess funds when the clear dues API is hit - However: - The **schedule table is not updated** to reflect the new temporary obligation. - The **obligation is not marked as met**. - **Derived details** are not populated with the settlement transaction. ### **Impact** - Reporting discrepancies (interest recognised vs. interest settled). - Incorrect DPD because obligations appear “unmet”. ### **Required Behaviour** Finflux should: 1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge). 2. **Immediately settle the obligation** and mark: - obligation_met = true - obligation_met_on = timestamp 3. **Populate derived details** with: - linkage to the

---

## #68 — BRD Interest Refund via Credit Note - OD - V2
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Refund of interest already posted and/or collected
- Refund processed only via Credit Note (Interest type)
- Support for partial and full interest refunds
- Integrated accounting and LMS impact
- Duplicate refund control with necessary dedupe validations

# BRD: Interest Refund via Credit Note - OD - V2 Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ## 1. Background & Objective Interest is periodically accrued, posted, and collected from users as part of the OD loan lifecycle and recognized as interest income in the accounting system. In certain business scenarios (pricing corrections, excess collection, grievance redressal, operational errors, etc.), a portion of already posted and/or collected interest may need to be refunded to the user. The objective of this document is to define a **system-driven, auditable mechanism** to process interest refunds via Credit Note with correct accounting treatment. The solution must ensure: - Accurate reversal of interest income in P&L - Correct user-level balance adjustment - Elimination of manual accounting interventions - Full audit traceability --- ## 2. Scope ### In Scope - Refund of interest already posted and/or collected - Refund processed only via Credit Note (Interest type) - Support for partial and full interest refunds - Integrated accounting and LMS impact - Duplicate refund control with necessary dedupe validations ### Out of Scope - Interest waiver before posting --- ## 3. Key Definitions | Term | Definition | | --- | --- | | Interest Refund | Reversal of interest already posted and/or collected | | Credit Note (Interest) | LMS transaction representing interest refund | | Interest Income Reversal A/c | Contra-income GL used to reverse recognised interest revenue | --- ## 4. Accounting Principles Interest refunds will follow a **single-step integrated accounting construct**. At the time of Credit Note processing: - User balance adjustment and income reversal will occur simultaneously - No intermediate liability or clearing account will be created - P&L impact will be immediate This ensures: - LMS reflects user truth - Accounting reflects financial truth - Reduced reconciliation complexity - No deferred clearing entries --- ## 5. Accounting Treatment ### 5.1 Interest Refund – Credit Note Issued At the time of processing Credit Note (Interest Refund): | Account | Debit | Credit | Account Type | | --- | --- | --- | --- | | Interest Income Reversal A/c | Refund Amount | | Contra Income | | User Interest / Excess / Principal (as applicable) | | Refund Amount | Asset / Liability | --- ### Impact - User outstanding reduces (or excess ledger adjusted) - Interest income reversed immediately in P&L - No clearing

---

## #69 — Charge details on Command centre
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently we have the following charges that we apply on customer loan accounts:

- Processing fee (Account opening)
- Margin pledge (When user pledges more securities)
- Dishonour (When user fails to clear their dues by the 8th of the next month (Due date))
- Penal charges (Applied daily for every day the customer remains in an overdue status (Interest is overdue))

Out of the 4 charges, the first three (barring penal charges) are applied via Fenix (internal LMS) while the fourth charge (Penal charges) are applied directly via Finflux (external LMS).

Our operations team, d

**Solution:**
?**

---

## #70 — Charge reversal enhancement V2
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges was manual, operationally intensive, and people-dependent. With the charge reversal enhancement now built and deployed, we have eliminated dependency on engineering/backend intervention, reduced friction for internal teams, and improved customer resolution time.

This PRD documents the final implemented solution — including the maker/checker workflow, credit note processing, validations, accounting flows, and the enhancements required to support charges with no GST and the productisation manual JV transaction posting

---

**Solution:**
?**

All components below are **implemented and live**.

We have created a **Charge Refund Maker/Checker workflow** that behaves as follows:

- **If a charge is completely outstanding** → it is waived.
- **If a charge is completely collected/paid** → a **Credit note** is issued to the loan account.
- **If a charge is partially collected** → a **Credit note** is issued to the loan account.

A new repayment type **“Credit note”** is now supported in LMS.

This repayment *does not* trigger any cash movement. Operations uses this type for reconciliation visibility.

The first set of supported use cases now live:

- Processing fees
- Margin pledge charges
- Dishonour fees
    
    (All as configured under ADHOC charges)
    

---

---

## #71 — Colending Disbursement and Charge knock off
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Designing a **system-level mechanism** to:
    - Handle **charge knock-off as part of the disbursement workflow**
    - Support **capitalised charges** that are:
        - Part of borrower POS
        - Owned by a specific lender
    - Correctly split:
        - Disbursements
        - Repayments
        - Outstanding balances
- Applicable for:
    - **Initial disbursement**
    - **Future disbu

# Colending: Disbursement and Charge knock off Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - **Internal teams**: Engineering, Finance, Ops, Risk, Product - **Partners**: DSP (originator / servicer), TCL (co-lender) - **Indirectly**: End customers (via statements, repayments, redraw behaviour) - **What is the challenge today** - Processing fees and other charges are **knocked off at disbursement**, but: - These charges are collected via disbursements by doing a short disbursement - Economically **owned by a specific partner (DSP)** - Current POS and split logic assumes: - A **single POS** - A **static co-lending ratio (10 / 90)** - This leads to: - Incorrect partner settlements - Over / under-recovery for lenders - Increasing complexity as multiple disbursements and future charges are introduced - **Why this is important** - Incorrect allocation impacts: - **Partner trust and reconciliation** - **Revenue recognition** - **Audit and regulatory confidence** - As the product evolves (OD-like behaviour, multiple charges), ad-hoc fixes will **compound risk and tech debt** - This needs a **foundational, extensible solution** --- ## **1. Problem Scope** ### In scope - Designing a **system-level mechanism** to: - Handle **charge knock-off as part of the disbursement workflow** - Support **capitalised charges** that are: - Part of borrower POS - Owned by a specific lender - Correctly split: - Disbursements - Repayments - Outstanding balances - Applicable for: - **Initial disbursement** - **Future disbursements** in OD / revolving facilities - **Multiple charge types** knocked off at disbursement (processing fee today, others in future) owned by different lenders. - Primary users: - Finance & Ops teams (reconciliation, settlement) - Engineering (LMS, accounting, settlement flows) - Secondary users: - Sales & onboarding teams (clear explanation of net disbursal vs loan amount) - Risk & Audit teams --- ### Out of scope - Interest accrual logic changes - Interest continues to follow existing borrower-level rules - Customer-facing UI redesign - No changes to how the customer views the loan, beyond correctness - Partner commercial renegotiation - Assumes existing ownership rules are final - Bureau reporting changes - Borrower-facing loan remains the single source for external reporting **Rationale**: These are orthogonal concerns and would delay solving the core accounting and settlement correctness problem. --- ## **2. Success Criteria** ### Primary outcomes 1. **Correct economic settlement** - Partner recoveries exactly match agreed ownership

---

## #72 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #73 — Dishonour charge enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Dishonour charges are applied to user loan accounts when monthly dues are not paid before the 7th of the month. However, the current application is tied to the outcome of mandate presentation, which results in inconsistent charge application across accounts.

**Problems Identified**

1. **Missed Charges Due to No Mandate:**
    
    Dishonour charges are **not applied** to users who do not have an active mandate (e.g., revoked mandates), even if they miss their due date.
    
2. **Incorrect Charges Despite Repayment:**
    
    Users who have already paid their dues manually

**Solution:**
?**

To make the application of dishonour charges **independent of the mandate presentation process** by introducing a post-due date review mechanism that ensures charges are applied fairly and consistently based on actual repayment behaviour.d

<aside>
⚠️

In case mandate is revoked or does not exist, if the collection amount is less than 10 Rs, it should be waived

</aside>

---

## #74 — Enhancing Collections Efficiency Through Mid-Month
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #75 — Finflux Product Setup for Co-Lending
**Status:** Completed | **Last edited:** Unknown

# Finflux Product Setup for Co-Lending Last Edited: March 19, 2026 9:44 PM PRD ETA: January 27, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context As part of the co-lending setup, loans are economically split between: - **10% exposure (CLA portion)** - **90% exposure (TCL)** - **100% loan representation** required for operational and accounting purposes Current state: - Finflux is running on a **single instance** supporting **OD and TL products** - All reporting, accounting, SMA/NPA tagging, and operational workflows are currently **instance-scoped** - Finflux manages collateral and exposure deduplication The setup needs to support: - Fast go-live - Clean accounting - Correct delinquency signaling to TCL - Minimal disruption to existing production flows --- ## 2. Problem Statement The co-lending structure introduces multiple complexities: - **Collateral deduplication risk** if multiple loans referencing the same securities exist in the same instance - **Client-level SMA/NPA contagion**, where delinquency in a small CLA exposure may impact unrelated production loans - **Accounting segregation** required across different exposure types - **Operational overhead** introduced by multiple Finflux instances - **Reporting and reconciliation complexity** across LMS, Finflux, and TCL --- ## 3. Design Options Considered ### Option A: Single Finflux Instance with Multiple Products - All co-lending loans (10% and 100%) reside in the same instance - Separation handled purely via product-level configurations **Challenges** - High risk of collateral dedupe conflicts - Client-level NPA impact across all loans - Heavy reliance on product-level filters across reporting and accounting - Higher regression risk for existing OD and TL products --- ### Option B: Multiple Finflux Instances for All Co-Lending Loans - Separate instances for 10% and 100% loans **Challenges** - Higher setup and maintenance effort - Configuration and version-sync risks - Increased reporting and reconciliation overhead - Multiple operational points of failure at launch --- ## 4. Final Recommendation (Chosen Approach) **Recommended Setup** - **10% co-lending loan (CLA exposure)** → Booked in the **existing Finflux instance** - **100% loan** → Booked in a **separate Finflux instance** - **90% exposure** → Booked in **TCL** This approach optimizes for **lower effort, faster go-live, and controlled risk**, while keeping core production flows isolated. --- ## 5. Rationale for the Recommendation ### 5.1 Faster Go-Live with Minimal Change Surface - Existing Finflux instance already supports: - Live products - Accounting - Reporting - Monitoring - Adding a **single CLA product (10%)** is significantly lower effort than: - Standing up and

---

## #76 — LAS CMS Confiscation and sale of securities
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

## #77 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #78 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #79 — PPSL UPI mandate presentation
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
The scope of this enhancement includes:

- Supporting UPI mandate registration through PPSL for PayTM-originated users
- Enhancing LOS mandate registration APIs to support explicit provider tagging
- Allowing PayTM to explicitly pass `provider = PPSL`
- Persisting provider information within LOS
- LMS consuming provider metadata from LOS
- LMS routing mandate presentation based on provider
- Suppo

# PPSL UPI mandate presentation Last Edited: May 25, 2026 10:00 PM PRD ETA: May 25, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** PayTM currently uses the existing DSP Finance (Fenix) mandate registration and presentation stack for both NACH and UPI mandates, where mandate registration is facilitated via Digio and mandate presentation is managed through DSP Finance workflows. PayTM intends to migrate mandate registration for a subset of users to the internal PPSL mandate stack. The primary motivation behind this change is to significantly improve the end-user registration experience by enabling native invocation of the UPI intent flow directly through the PayTM ecosystem. This removes dependency on external redirection-heavy flows and improves TPAP handoff reliability during mandate registration. Historically, the PPSL UPI mandate presentation workflow differed from the existing Digio-integrated flow: - Digio workflow: - Single consolidated API call - Automatically registers PDN and presents mandate together - Mandatory condition that mandate presentation occurs more than 24 hours in the future - PPSL workflow (earlier implementation): - PDN scheduling and mandate presentation were independent APIs/workflows - Required additional orchestration effort from LMS/LOS PPSL has now aligned its APIs and shared updated documentation enabling the required orchestration compatibility. However, this introduces an operational and technical challenge: - Certain PayTM customers will continue using Digio mandates - New customers may register mandates using PPSL - LMS presentation logic must identify which mandate provider was used during registration to correctly invoke downstream presentation workflows Currently, LOS internally maintains provider mapping through a provider column, however the external mandate registration APIs used by LSPs do not allow explicit provider selection. This creates ambiguity for LMS while determining presentation routing. To solve this, the mandate registration APIs will be enhanced to allow PayTM to explicitly pass the mandate provider during registration. --- # **1. Problem Scope** ## In Scope The scope of this enhancement includes: - Supporting UPI mandate registration through PPSL for PayTM-originated users - Enhancing LOS mandate registration APIs to support explicit provider tagging - Allowing PayTM to explicitly pass `provider = PPSL` - Persisting provider information within LOS - LMS consuming provider metadata from LOS - LMS routing mandate presentation based on provider - Supporting coexistence of: - Legacy Digio mandates - PPSL mandates - Maintaining the existing UPI mandate presentation logic at LMS layer: - Loan account level presentation creation - Collection batch item generation - Existing downstream presentation

---

## #80 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #81 — Product Note Interest Refund via Credit Note
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, e

# Product Note: Interest Refund via Credit Note Last Edited: January 23, 2026 8:15 PM PRD ETA: July 22, 2025 PRD Owner: Vaibhav Arora ## Background and Context **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged or goodwill interest waivers - Operations team processing interest refunds/waivers - Finance team managing manual accounting entries for interest reversals - Tech ops/Product handling backend interventions for interest adjustments **What is the challenge that they are facing? What is broken today?** - Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access - Process is operationally intensive with dependency on Jira ticket workflows - No standardized maker-checker workflow for interest refunds similar to charge refunds - Manual JV posting for interest reversals creates additional overhead for Finance team - Lengthy resolution time (2-3 days) impacting customer experience - No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period - Lack of visibility and tracking for interest refund requests across the loan lifecycle **Why is it important? What is getting impacted?** - Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests - Operational inefficiency with high manual effort required for each interest refund case - Risk of errors and duplicate processing without systematic validations - Finance team bandwidth consumed by repetitive manual JV entries - Lack of audit trail and reconciliation capabilities for interest reversals - Inconsistent treatment of interest refunds compared to the now-standardised charge refund process --- ## 1. Problem Scope ### In scope **What specific problems are we solving?** 1. **Slow Resolution Time:** - Interest refund requests take 2-3 days to resolve from initiation to completion - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product 2. **Operational Bottleneck and Dependency:** - Operations teams cannot independently process interest refunds or waivers - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention - Backend access and API calls are needed for what should be a routine operational task - Process creates unnecessary dependencies across multiple teams for resolution 3. **Risk of Duplicate Processing:** - No systematic validation exists to check if interest for a specific period has already been waived or refunded - Product team rely

---

## #82 — Product Note LAS Customer Consent Capture
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

We are introducing **structured consent capture for Loan Against Shares onboarding**.

This change introduces **explicit consent capture within the KYC verification screen**, ensuring users acknowledge the consent declaration before proceeding.

This includes:

- Displaying a **hyperlinked Consent Declaration** document in the KYC verification screen.
- Allowing users to **view the document wi

# Product Note: LAS Customer Consent Capture Last Edited: March 16, 2026 2:48 PM PRD ETA: March 11, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** **Loan Against Shares (LAS)** is a facility where customers pledge listed securities to obtain credit from DSP Finance. We must ensure that borrowers **explicitly acknowledge the risks and operational mechanics of pledged securities** to maintain compliance, risk, and operational coverage for taking necessary collection actions if the market falls significantly. Regulatory expectations from **SEBI (pledge of securities framework)** and **RBI digital lending guidelines** require lenders to ensure: - Customers provide **explicit consent for pledge enforcement and liquidation of securities**. - Customers acknowledge **market-linked risks** associated with pledged securities. - Customers consent to **digital communication and electronic execution of records**. - Lenders ensure the borrower **is not pledging promoter-held securities**, which may be subject to additional regulatory restrictions. Currently, the onboarding journey **does not capture an explicit promoter declaration nor structured consent acknowledgement**. This creates a **compliance and enforceability gap** if securities liquidation is required. Additionally: - The **risk disclosure document is not explicitly presented within the user journey**. - Users are **not asked to explicitly consent to the document during onboarding**. --- # **1. Problem Scope** ## **In scope** We are introducing **structured consent capture for Loan Against Shares onboarding**. This change introduces **explicit consent capture within the KYC verification screen**, ensuring users acknowledge the consent declaration before proceeding. This includes: - Displaying a **hyperlinked Consent Declaration** document in the KYC verification screen. - Allowing users to **view the document within the app/web (bottom sheet)** without leaving the journey. - **([Document](https://docs.google.com/document/d/1-v_MdBdQrdfxgLhRGK2A4SNq0RYtCBF3/edit))** - Capturing **explicit consent via checkbox acknowledgement**. - Recording consent metadata in the **DSP Additional Details API**. - Introducing **validation in Submit Opportunity** to ensure consent is captured when collateral type is shares. Primary users: - Customers applying for **Loan Against Shares** Secondary users: - Risk and compliance teams - DSP LOS integration - Customer support and collections teams --- ## **Out of scope** - Changes to the **core pledge creation flow with the depository participant (DP)**. - Any changes to **loan agreement documentation or e-sign flows**. - Changes to **collateral valuation or margin monitoring logic**. - Retrospective capture of consent for **existing users or existing loans**. These may be handled through **future compliance or document versioning initiatives**. --- # **2. Success Criteria** ### **Key outcomes** 1. Ensure **regulatory compliant capture of

---

## #83 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #84 — Product note Virtual account handling for Colendin
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **dynamic credit account routing** for VA collections based on:
    - Loan → Contract → Escrow account mapping
- Enhance **Validate API response** to return:
    - Correct **credit account (escrow / DSP account)**
- Support:
    - Colending loans → Escrow routing basis contract configuration
    - Non-colending loans → DSP account routing
- Store and manage:
    - **Contract-level credit 

# Product note: Virtual account handling for Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 25, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC (DSP) – Product, Ops, Finance teams - **What is the challenge** - In the current Virtual Account (VA) setup, all repayments are credited to a **single DSP collection account** - However, for **co-lended loans**, regulations mandate that: - Funds must flow into a **designated escrow account** (not DSP’s own account) - Yes Bank’s existing integration: - Identifies VA → calls our **Validate API** - Credits funds to a **pre-configured account** - This creates a gap: - System today does **not dynamically decide the destination account** - No linkage between **loan → colending contract → escrow account** - **Why is it important** - Regulatory non-compliance if funds are credited to incorrect accounts - Incorrect fund flows → breaks lender settlement and reconciliation - Operational risk → manual reversals, audit failures - Scaling issue → multiple co-lenders require dynamic routing --- ## **1. Problem scope** ### In scope - Enable **dynamic credit account routing** for VA collections based on: - Loan → Contract → Escrow account mapping - Enhance **Validate API response** to return: - Correct **credit account (escrow / DSP account)** - Support: - Colending loans → Escrow routing basis contract configuration - Non-colending loans → DSP account routing - Store and manage: - **Contract-level credit account mapping (DSP 100% should also be a contract)** - Stakeholders: - Primary: Ops, Finance, Lending Systems - Secondary: Yes Bank, LSPs, Customers --- ### Out of scope - Changes to: - VA generation logic (e-collect code remains same: 301301) - Checker workflows (remain unchanged), credit account should be added as a parameter in the checker task - Notify API structure (only extended usage, not redesigned) - Advanced validations: - Name match, whitelist accounts (Currently live - Remains unchanged) - Multi-account routing within a single contract - One contract can have one bank account as part of the proposed set up. --- ## **2. Success Criteria** ### Key outcomes - **100% compliance** with escrow routing for co-lending loans - **Zero misrouted transactions** (DSP vs Escrow) - **Seamless bank integration** without additional retries/failures ### Metrics - % of VA transactions correctly routed to escrow (target: 100%) - Validate API success rate (pass rate without checker approval > 98%) - Reconciliation

---

## #85 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #86 — Term loan gaps
**Status:** Unknown | **Last edited:** Unknown

# Term loan gaps Last Edited: July 24, 2025 5:10 PM PRD Owner: Vaibhav Arora ### **Spend & Convert Enhancements** - Support for **flat PF (Processing Fee)** values in spend and convert requests. - Allow **knockoff remarks** to be passed in the spend and convert payload. - Support passing **different charge types** and **collecting multiple charges** in a single spend and convert request. --- ### 🧾 **Repayment Logic** - Enable both **loan-level and line-level repayments** to co-exist for term loans. - Mark **repayment at loan level** as a current **gap** in configuration. - Support **EMI-level repayments**. - Include **apportionment details** in the repayment response (internal checks needed). - Support **loan-level excess refunds**. - **Excess amounts**: - Should remain **parked** after due generation (do not auto-settle dues via FIFO). - At **line level**, should **increase available limit**. --- ### 🧮 **Due/Bill Generation** - Bills should be generated **independent of the due generation job**—on demand. --- ### 📆 **Schedule and Simulation** - Provide a **preview schedule API** without needing to create a line. - Enable **tranche-level simulation API** for a given date. - All **date fields** must be passed as **EPOCH timestamps**. --- ### 🧠 **Tagging & Status Configurations** - SMA tagging should be **configurable**. - **NPA to be tracked at client level**, while **SMA is tracked at loan level**. --- ### 📉 **Interest & Limit Management** - Support **interest rate updates** on loans. - **Limit replenishment** should only occur when the **underlying loan is fully closed**, whether via EMI or part-payment.

---

## #87 — Volt - Overdue Communication Enhancement
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

## #88 — Volt - Shortfall Communication Enhancement – Due D
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

## #89 — [Platform] Decoupling of dishonour fees with manda
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently our dishonour charge application is coupled with mandate presentation, what that means is basis certain error codes that we get from Digio (presentation vendor), we either apply or do not apply dishonour charges

However that leaves the following gap, for customers where mandate was not registered, and presentation does not happen, we are not able to apply dishonour charges (which should have been applied).

How does scenarios arise where mandate is not registered for the user:

- User revokes existing mandate (cancels)
- User registers via Aadhaar Esign or Physica

**Solution:**
?**

We will be setting up a job on Finflux which will apply dishonour charges (Rs 590 - - 500 + GST) to users with interest overdue on the 8th of next month (Interest for January was posted on 1st Feb and was due on 7th Feb, dishonour fees if applicable will be posted on 8th Feb at 2 AM)

We will remove charge application logic from our mandate presentation workflow, mandate presentation will only post or not post transactions based on the status received from the vendor (extendable to current implementation with PhonePe)

---

## #90 — [Platform] Foreclosure handling to support Volt fo
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

## #91 — [Platform] Mandate collection enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Our LAMF credit line product follows a balloon repayment model, which essentially means that the customer is only obligated to pay the interest as per their principal outstanding (which is accrued daily and posted monthly). 

There are multiple ways through which a user can pay this amount:

- Making a repayment on their lo ch the NBFC automatically deducts the amount from the user’s bank account)

What amount is collected from the user’s account?

- Charges due + Penal charges due + Interest due are collected on the 7th via mandate presentation

As we are a platform, there 

**Solution:**
?**

We will be enhancing our current mandate presentation workflow to support the use case where an LSP will control the mandate presentation for the users and will have the following capabilities:

- Get mandate collection file: Mandate collection file which is generated every month and then approved by the operations team will be available as a file (csv) through a get API (for all eligible loan accounts for presentation) to the LSP with approval status
- Mandate collection posting API: LSP will have the capability to pass the mandate collection response to the user (broadly there can be the following scenarios)
    - Mandate was presented and collected successfully (Success)
    - Mandate was presented but failed (Fail)
    - Mandate was not presented (Pending) - LSP will not call the 

---

## #92 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #93 — Term Loan Apportionment Logic
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Apportionment Logic - Apportionment is the distribution of a paid sum of money across multiple components of a loan/tranche in order to knock off/settle these components. - Apportionment logic will be based in the order of IPC. - In case of a single tranche apportionment the order will be: Interest Overdue>Principal Overdue>Interest Due>Principal Due>Charge. In case there are multiple EMIs of the Tranche which are overdue then apportionment will start from the oldest EMI overdue. - In case of multiple tranches apportionment the order will be: Oldest EMI overdue(Interest>Principal)>Oldest EMI due(Interest>Principal)>Charges. In case of EMIs overdue across multiple tranches the oldest EMI across tranches will be apportioned first then the apportioning will be done for the next oldest EMI across the tranches and so on so forth. In case all the overdue EMIs are cleared/apportioned the next apportioning will be done for the oldest due EMI and once the oldest due EMI is apportioned then apportioning of the next oldest due EMI will be done and so on so forth. Once all the overdue and due EMIs are apportioned across tranches, apportionment of charges will start and it will also be done based in the order of the oldest charge getting apportioned first i.e. in the chronological order. - If after the apportionment of all the components there is an excess which remains then we will ask the user to select the tranche wherein the excess will be adjusted. The excess adjustment will happen in a way that either the Tenure of the Tranche is reduced or the EMI of the Tranche is reduced based on the user’s selection. Default option(in case user does not select) will always be to reduce the tenure keeping the EMI same for the oldest Tranche.

---

## #94 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #95 — Term Loan Communications
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Customers availing a **Term Loan under Loan Against Mutual Funds (LAMF)** must have timely, contextual, and transparent communication regarding their loan lifecycle.

- Customers often don’t receive clarity on loan disbursement, repayment schedules, EMI due dates, tranche-level updates, and closure status.
- Absence of structured communication increases inbound queries to customer support, delays repayments, and lowers customer trust.
- Regulatory and compliance requirements mandate that lenders provide customers with certain communications (e.g., SOA, NOC, repayment reminde

**Solution:**
?**

A structured, automated, and multichannel communication framework for **Term Loan against LAMF**, covering the entire lifecycle:

---

## #96 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #97 — Term Loan Excess Handling and Refund
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

## #98 — Term Loan Foreclosure
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

## #99 — Term Loan Mandate Repayments
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

- **Collections Reliability:**
    
    In Term Loans, fixed EMI dates require timely collections. Manual payments or ad-hoc transfers are prone to delays, user forgetfulness, and operational leakage.
    
- **Operational Efficiency:**
    
    Manual chasing of repayments increases Ops load, costs, and NPA risk.
    
- **Customer Experience:**
    
    Users don’t want to remember EMI dates or perform repetitive actions each month. Mandates automate this and prevent missed-payment penalties.
    
- **Regulatory Alignment:**
    
    NPCI/NACH mandates ensure collections hap

**Solution:**
?**

---

## #100 — Term Loan Manual Repayments(PG)
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

## #101 — Term Loan Sell off
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

## #102 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #103 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs

---

## #104 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #105 — Analytics requirement Repayment
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Repayment | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of repayments | (count of total repayments made today) | | | | | | | | | | Number of transactions automatically settled | (count of repayments made and settled today) | yesterday | | | | | | | | | Number of transactions pending settlement | (Count of repayments made today but pending settlement) | | | | | | | | | | Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours | | | | | | | | | | % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) | | | | | | | | | | | | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.collections ### Field: Collections: created_on - When payment was created Collections: settled_on - When payment was settled automatically Payment_status (If equals to settled - payment was settled either using admin action or automatically) ### Table: admin_action_audit (Credits) admin action name: UPDATE_COLLECTION_STATUS To identify which collections were settled manually Format: Email with CSV attached Sample query: ```sql SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*) FROM collections LEFT JOIN credits ON collections.credit_id = credits.credit_id WHERE lending_partner_id = 'Bajaj' AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY AND collection_status not in ('REQUESTED','CANCELLED','FAILED') group by collection_status,CAST(collections.created_on AS DATE) order by 1,2 ``` Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #106 — How banks and NBFCs manage rounding of interest an
**Status:** Unknown | **Last edited:** Unknown

# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases. ## **1. Regulatory & Industry Context** ### RBI Guidelines: RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in: - Customer charging - Auto-debit recovery - Tax invoicing - Reconciliation of ledgers So, banks and NBFCs need to: - Ensure **customers aren’t overcharged** - Match debits with invoices/statements - Maintain proper **audit trail** and **variance accounting** if rounding is applied --- ## 2. Rounding Methods Used by Banks & NBFCs | Type | Common Use Case | Real-world Examples | | --- | --- | --- | | **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs | | **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton | | **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs | | **Cumulative Rounding** | Long tenure loans | Used in housing finance | --- ## 3. Detailed Accounting Treatment by Banks/NBFCs ### **A. Exact Posting (No Rounding)** ### Use Case: - Processing fees + GST - Penal charges ### System Flow: 1. Fee computed: ₹100 2. GST @18% = ₹18 3. Total = ₹118.00 (posted and debited as-is) ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹118.00 | | | Processing Fee Income | | ₹100.00 | | GST Payable (Output) | | ₹18.00 | ✅ Matches invoice and is tax compliant --- ### **B. Round at Posting (Nearest Rupee)** ### Use Case: - Accrued interest - EMI interest - Installment schedules ### Example: - Accrued Interest: ₹199.48 → Rounded: ₹199 - Accrued Interest: ₹199.50 → Rounded: ₹200 ### System Flow: - Round value **at the point of debit** ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹200.00 | | | Interest Income | | ₹199.48 | | **Rounding Reserve GL (Internal)** | | ₹0.52 | > 🔸 If we round down, the 0.52 may be debited to an expense account. > ### Why Rounding Reserve GL? To track small deltas between system-calculated interest and posted amount. ✅ Fair

---

## #107 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #108 — Postman collection
**Status:** Unknown | **Last edited:** Unknown

# Postman collection { "info": { "_postman_id": "unique-postman-id", "name": "Leegality UAT", "schema": "[https://schema.getpostman.com/json/collection/v2.1.0/collection.json](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)" }, "item": [ { "name": "Inventory check", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/series/list](https://sandbox.leegality.com/api/v3.0/series/list)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "series", "list" ] } }, "response": [] }, { "name": "E-sign request - copy to be sent to customer", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"mKJY8rA\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "E-sign request - copy to be stamped and NBFC signed", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"GpqF8Tf\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"stampSeries\": \"03\",\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "Sign on e-sign request", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"signUrl\": \"string\",\n \"profileId\": \"naq2t4g\",\n \"consent\": \"By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details.\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation](https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "docSigner", "invitation" ] } }, "response": [] }, { "name": "Download document", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId={{documentId}](https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId=%7B%7BdocumentId%7D)}&documentDownloadType={{documentDownloadType}}", "protocol": "https", "host": [ "sandbox", "leegality", "com"

---

## #109 — DSP Finance Website Summary
**Status:** Unknown | **Last edited:** Unknown

# DSP Finance Website: Summary # Positioning We, at DSP Finance, want to be positioned as the ***Most innovative and cutting-edge lender with deep expertise in capital markets.*** - We want to stand out from the crowd as a new-age and customer-friendly lender - We want to stand out from traditional lenders (BFL, TCL) - We want to standout as a specialist lender in the capital markets # Branding We at DSP finance will continue to maintain the DSP brand themes (Colors). That said, we also want to have an independent identity. - Branding to reflect our identity as a new-age lender - Common color schemes as DSP group - Different iconography compared to DSP group # Layout Below are the pages for the new website. - Homepage **Objective**: This page will talk about DSP Finance at a high level to instill confidence in the visitor. **Hero Section –** Innovation at core**.** - **Headline:** *“India’s most innovative lender in the securities space.”* - **Sub-headline:** “A seamless bouquet of credit offerings built on a deep understanding of customers, enabled through cutting-edge technology” - Our partners: Band of existing LSP partners we have. - CTA: *“Explore Partnership”* | *“Request a Call Back”* **Overview section** - India’s leading LAFA player. - DSP Finance helps individuals & businesses unlock the value of their securities seamlessly. - DSP Finance, which is part of the DSP Group is the fastest growing digital lender in the space. - AUM - Rating - Customers **Offerings section** - Our product suite - **LAFA**: Liquidity at the finger-tips against financial securities spanning mutual funds and securities. Redirects to the product page. - **FSG**: Tailored solutions for businesses looking to unlock their business potential by leveraging their financial assets. Redirects to the product page. **DSP Advantage** - Our USP. - **Industry Expertise**: DSP Finance brings to the table, unparalleled expertise and business understanding of capital markets & Securities space. - **Technology First**: DSP Finance offers customers and partners the ease of leveraging technology for superior experience. - **Product Suite**: DSP Finance has the entire suite of products in the financial securities space to suit the needs of individuals and businesses. - **Transparency & Trust**: DSP Finance has very clear and easy to understand fees and charges, backed by the legacy of DSP Group. **FAQs -** Answering questions. **Testimonials** - Building trust in customers. - About Us **Mission & Vision -** Context