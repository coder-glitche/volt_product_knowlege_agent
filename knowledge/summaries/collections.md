# Current State: Collections

> Auto-generated from 10 PRD(s). Most recently edited shown first.


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

## #2 — [Platform] Mandate collection BRE optimisation
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

## #3 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #4 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #5 — [DSP] Dues collection comms
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

## #6 — Enhancing Collections Efficiency Through Mid-Month
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #7 — Volt - Overdue Communication Enhancement
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

## #8 — [Platform] Mandate collection enhancement
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

## #9 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #10 — Postman collection
**Status:** Unknown | **Last edited:** Unknown

# Postman collection { "info": { "_postman_id": "unique-postman-id", "name": "Leegality UAT", "schema": "[https://schema.getpostman.com/json/collection/v2.1.0/collection.json](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)" }, "item": [ { "name": "Inventory check", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/series/list](https://sandbox.leegality.com/api/v3.0/series/list)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "series", "list" ] } }, "response": [] }, { "name": "E-sign request - copy to be sent to customer", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"mKJY8rA\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "E-sign request - copy to be stamped and NBFC signed", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"GpqF8Tf\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"stampSeries\": \"03\",\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "Sign on e-sign request", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"signUrl\": \"string\",\n \"profileId\": \"naq2t4g\",\n \"consent\": \"By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details.\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation](https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "docSigner", "invitation" ] } }, "response": [] }, { "name": "Download document", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId={{documentId}](https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId=%7B%7BdocumentId%7D)}&documentDownloadType={{documentDownloadType}}", "protocol": "https", "host": [ "sandbox", "leegality", "com"