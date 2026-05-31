# Current State: Ops Tools

> Auto-generated from 76 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Standard Operating Procedure Approving Uploaded Fi
**Status:** In progress | **Last edited:** September 27, 2024 10:40 AM

# Standard Operating Procedure: Approving Uploaded Files on CKYC ## Version Control - Version: 1.0 - Last Updated: 26 September 2024 - Drafted By: @Vaibhav Arora - Approved By: @Gautam Mahesh @Nishant Athmakoori (Please verify here) ## Purpose This SOP outlines the steps for approving an uploaded file on the Central KYC Records Registry (CKYCRR) system. This document covers the list of activities to undertaken by the operations team after the system has passed the data to CKYC for upload. The files that are accepted by CKYC are to be approved on the portal for the records to be finally accepted and updated at their end. ## Scope This procedure applies to all checker users responsible for authorising bulk uploads in the CKYCRR system. ## Prerequisites - Access to the CKYCRR system with checker privileges - Only following users can approve an uploaded file on Cersai dashboard: - Institutional admin - (Amrita and Priya) - Regional admin (For region level files) - No user as of now - Branch admin (for Branch level files) - No user as of now - Familiarity with the CKYCRR user interface Refer user manual attached below **Note**: Additional users can be added as needed. [User_Manual_CKYC1.pdf](Standard%20Operating%20Procedure%20Approving%20Uploaded%20Fi/User_Manual_CKYC1.pdf) ## Procedure 1. **Access the Bulk Upload Authorization Screen** - Log in to the CKYCRR system - Navigate to "KYC Management" in the main menu - Click on "Bulk KYC Authorization" 2. **Review Pending Uploads** - The screen will display a list of batches pending for checker approval - Each batch will show details such as Batch ID, Upload Date, Upload Type, and Number of Records 3. **Select a Batch for Review** - Click on the radio button next to the batch you want to review 4. **Examine Uploaded Data** - Click on the "Upload file" link to open and review the uploaded data file - Ensure the data complies with KYC requirements and institutional policies 5. **Make Approval Decision** - If the data is correct and compliant: - Click the "APPROVE" button - If there are discrepancies or issues: - Enter the reason for rejection in the "Remarks" field - Click the "REJECT" button 6. **Digital Signing (for Approval)** - When approving, a pop-up will appear to select your digital certificate - Select your registered digital certificate from the list - Click the "Sign" button to complete the approval process 7. **Confirmation** - Verify that the system displays

---

## #2 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #3 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #4 — Process note Creating a new user on Command Centre
**Status:** Done | **Last edited:** November 8, 2024 9:36 AM

# Process note: Creating a new user on Command Centre # Process Note: Creating a User on Command Centre ## Overview This document outlines the step-by-step process for creating a new user account on the Command Centre system. ## Prerequisites - Admin access to the Command Centre system - New user's details (full name, email address, role, department) - Approval from Head of Operations (@Nishant Athmakoori) [Access level details](https://docs.google.com/spreadsheets/d/1VSPMYia-Kmwob9X3pH-T3nMTYNZxXpEC_Afpfq27e-o/edit?gid=0#gid=0) ## Steps 1. Request for access on Email from the business counterpart, in this case, all access will be shared by @Nishant Athmakoori 1. Details required in the email: 1. Name 2. Designation 3. Role (Admin / Approver / Read only) 4. Employee ID 5. Mobile number 6. Email address (DSP Email address) Any requests without the aforementioned details will get rejected 2. Forward the access with consent and approval to tech-ops@dspfinance.com 3. Access will be shared within 1 working day of request. 4. Once access is shared (User name and password), logon to the command centre using the following URL: https://cc.dspfin.com/login 5. Once logged on, users will be able to use the command centre for the following utilities: 1. Client search (all roles) 2. Loan search (all roles) 3. Review client details (all roles) 4. Review client KYC details (all roles) 5. Review client risk details (all roles) 6. Review loan details (all roles) 7. Review transactions (money and collateral) (all roles) 8. View servicing tasks (Approver and admin only) 9. View collateral tasks (Approver and admin only) 10. View application tasks (Approver and admin only) 11. View NBFC operations tasks (Approver and admin only) 12. Approve or reject tasks (Approver and admin only) ## Post-Creation Steps - Document the new user creation in your system log or user management spreadsheet ## Troubleshooting If you encounter any issues during this process, please contact the IT support team at tech-ops@dspfinance.com

---

## #5 — Lodgement maker
**Status:** Pending Review | **Last edited:** November 29, 2024 4:43 PM

**Problem:**
are we solving?**

Users pledge securities before their loan account is created with the bank, users also pledge additional securities post origination. 

Scenarios can arise where the user has pledged securities, however the same have not been added to their loan account, ops team will need a capability through which they can manually lodge these securities into the user’s loan account via the command centre

---

**Solution:**
?**

We will create a maker task, where the ops agent will be able to select an RTA and basis RTA add a lien reference number (unique to one pledging request). 

Against which we will hit the lien status API and get all the securities pledged in that particular session as well as their current status. Once we have the status, we will give the ops agent to select the desired securities which they want to map to the loan account, and give the user the respective drawing power.

CAMS → Lien reference number

KFIN → KFIN session number

For the sake of convenience, we can call them as a common identifier for easy communication between operations team.

<aside>
⚠️

Note: This process will have to be done at a RTA level, that is if a user has pledged securities with the two RTAs, we will be crea

---

## #6 — NLP-736 Timestamp value is not captured with hh mm
**Status:** Not started | **Last edited:** November 19, 2024 7:41 AM

# NLP-736: Timestamp value is not captured with hh:mm:ss due to which the default value 05:30:00 is shown in the UI Command centre search result pages: Client creation date (client search) Expiry date (loan search) Bureau pull date (client details risk section) AML pull date (client details risk section) Mandate expiry date (loan details section) Expiry date (is in small case) KYC expiry date is comming as invalid date Completed on (repayment detail is coming as invalid detail)

---

## #7 — CC design QC
**Status:** Not started | **Last edited:** November 13, 2024 2:21 PM

# CC design QC ## To-do - [ ] QC approve buttons size - [ ] QC approve buttons color - [ ] Unify primary color across command center - [ ] Do a QC of color of tags used and standardise the colors according to use case - [ ] Toast colors ## Items to check | **Item** | Problem | **Action** | Notes | **Status** | | --- | --- | --- | --- | --- | | CTA size: QC/Approval | Button size is small | Update size from 22 → 32 | | | | | | | | | | Nav link selected item | Accessibility issues | - BG: #F1FCFA → Primary 50 - Text: #1CCDBC → Primary 600 | | | | CTA: filled | Brand green clashes with success | #1C8980 → Primary 600 | | | | CTA: filled | Unnecessary shadow | Remove shadow | | | | CTA: Link | Brand green clashes with success | #1C8980 → Primary 600 | | | | CTA: Outline | Brand green clashes with success | #1C8980 → Primary 600 | Used in: - Table: Action - | | | Pagination CTA | Brand green clashes with success | #1C8980 → Primary 600 | | | | Review CTA in Application table | | - Remove shadow - #1C8980 → Primary 600 | | | | Line tabs: active | Brand green clashes with success | #1C8980 → Primary 600 | Text + Underline color | | | Box tabs: active | Brand green clashes with success | #1C8980 → Primary 600 | Text + outline color | | | Box tabs: unselected | Unselected looks as if it’s selected | Text: #1C8980 → Indigo 900 | Tabs in QC | | | | | | | | | Radio | Brand green clashes with success | #1C8980 → Primary 600 | In “Search” modal | | | | | | | | | Tag refer img 1A | Wrong color | Green preset from AntD | Cust details → KYC → verified tag | | | Tag: Success, Active | Accessibility | Green preset from AntD | | | | Tag: Filter | | | | | | | | | | | | Loader | Aesthetics | Skeleton loader | Library to implement it | | ## Legend - Neon

---

## #8 — KYC Risk Status (NBFC Platform)
**Status:** Done | **Last edited:** November 12, 2024 6:05 PM

**Problem:**
are we solving?**

KYC risk status needs to be maintained against each client in the NBFC to maintain appropriate risk classification of customers in the LMS as well as in NBFC.

RBI requires us to maintain risk status for each customer under CDD and EDD measures, for all non face to face account based relationship openings, customer should be classified as high risk. 

For customers classified as high risk, their KYC should be evaluated every 2 years, (Re-KYC) unless a face to face KYC or VCIP is formed for the customer. 

To comply with the same, we need a method to store and display the KYC

**Solution:**
?**

Maintain KYC status and KYC expiry date (2 years post account opening) in LMS as well as internal storage at a client level. 

We will be storing the details at a client level in Finflux (datatables - clientkycdetails) and internally in Finflux against client ID.

The same will be visible for the operations and risk teams on the command centre on the client details and KYC details page

---

---

## #9 — PRD — Term Loan Repayment STP Threshold Update
**Status:** Not started | **Last edited:** May 29, 2026 5:51 PM

**Problem:**
are we solving?

- Current STP repayment thresholds are overly conservative, causing valid low-risk repayments to be unnecessarily routed to NSTP via `REPAYMENT_AMOUNT_LIMIT_EXCEEDED` (>₹15L) and `REPAYMENT_DAILY_COUNT_EXCEEDED` (>4 repayments/day per LAN).
- Jan–May 2026 production data shows minimal breach risk: only 3 of 1,952 customers (0.15%) made repayments above ₹15L (max observed: ₹20.1L), and no LAN exceeded 5 repayments in a day — indicating the limits can be safely relaxed.
- Unlike other LSPs (Razorpay for Volt, PhonePe dashboard for PhonePe), there is no Cred repayment dashboard a

---

## #10 — Custom Comms based for Ad-hoc situations v2
**Status:** Not started | **Last edited:** May 29, 2026 4:27 PM

**Problem:**
are we solving?

- High-urgency situations (system down, regulatory events, one-off campaigns) need immediate comms capability outside the automated pipeline. All comms today are system-triggered and their is no functionality in the system to generate ad-hoc customer communications
- Ops/compliance/analytics are dependent on the product team for any ad-hoc communications which needs to be sent.
- It is a very time consuming activity for even the product team as of today to send ad-hoc communications as it requires a lot of data crunching, template mapping and script creation
- Some comms depen

**Solution:**
?

**In scope:**
- Once comms creator has the batch file with all recipient details(with Ids, body and variables) of all recipients. He uses the Actions button and selects "Bulk Send Comms" option in Comms section.
- Maker flow
    - recipient batch file upload (xlsx)
    - remarks window
    - Validation flow
        - System auto-validates the uploaded excel before creating a checker task.
        - **Validation

---

## #11 — Sell-off Repayment Reconciliation — Maker Automati
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

## #12 — STP validation for Sell-off Repayment Reconciliati
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

## #13 — Lodgement STP optimisations
**Status:** Pending Review | **Last edited:** May 20, 2025 4:16 PM

**Problem:**
are we solving?**

- Currently about 15% of the lodgements are flowing through non-STP flow requiring a lot DSP Ops bandwidth and keeps the customers blocked
- The top 2 reasons for the non-STP cases are -
    - Facility value threshold being 10L
    - Pledging and lodgement date mismatch

---

**Solution:**
?**

---

## #14 — STP validation for Bulk Sell off
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

## #15 — Phase 0 LTV update to 70 (servicing)
**Status:** Pending Review | **Last edited:** May 15, 2026 5:47 PM

**In scope:**
- Enable LSPs to support migration of existing customers from LTV 45 to LTV 70 product
- Eligibility validation for existing contracts basis current holdings
- Offer generation with configurable commercial ranges:
    - ROI
    - AMC charges
    - Limit enhancement charges
    - Tenure
    - Eligible LTV
- Validation of selected offer parameters before offer acceptance
- Loan contract/KFS/agreemen

# Phase 0 : LTV update to 70 (servicing) # **Background and Context** - Existing customers on the LTV 45 product currently do not have a standardized flow for migrating to the higher LTV 70 product. - LSPs require a structured mechanism to: - Check customer eligibility for higher LTV products - Generate and validate eligible offers - Capture revised commercial terms like ROI, tenure, AMC and enhancement charges - Submit and operationalise the contract update - Multiple parallel business initiatives including tenure increase, AMC charge application, PTC and Put/Call related changes are also coupled on this migration framework. - Operations teams currently do not have a centralized approval and visibility workflow for such loan contract updates. - Without validations and approval workflows: - Incorrect offers may get accepted - Invalid ROI or fee configurations may get processed - Loan contract inconsistencies can occur - Operational tracking and auditability become difficult --- # **1. Problem Scope** ## In scope - Enable LSPs to support migration of existing customers from LTV 45 to LTV 70 product - Eligibility validation for existing contracts basis current holdings - Offer generation with configurable commercial ranges: - ROI - AMC charges - Limit enhancement charges - Tenure - Eligible LTV - Validation of selected offer parameters before offer acceptance - Loan contract/KFS/agreement generation for updated contract - Service request creation for operational approval - Checker approval workflow in Command Centre - Visibility enhancements in Command Centre for: - Request details - Loan details - Collateral details - Loan kit - Customer communications - Handling edge cases - Parallel add collateral request - Add collateral request post service request ### Primary users - LSPs - Operations team - Internal business teams ### Secondary users - Existing loan customers migrating to higher LTV product ## Out of scope - Automatic/STP approval of service requests - New loan onboarding journeys - Manual contract modification outside APIs - Automated handling of parallel collateral addition requests ### Rationale for exclusion - Approval workflow requires operational oversight in initial phases - Scope is restricted to existing contract enhancement use cases - Parallel request orchestration will initially follow controlled N-STP handling --- # **2. Success Criteria** - Successful migration of eligible LTV 45 customers to LTV 70 product through API-driven workflow - Reduction in operational dependency for manual contract validations - Accurate validation of: - ROI ranges - Fee ranges - LTV

---

## #16 — Product Note LTV update to 70
**Status:** Not started | **Last edited:** May 12, 2026 10:39 AM

# Product Note : LTV update to 70 --- # **1. Problem Statement** --- ## **2. Objective** --- ## **3. Scope** --- - LTV update task - Finflux - Multiple approved script management - Validations - Any sort of handling - Fenix - Multiple approved scripts handling - Risk and RMS validations required - Impact of all collateral transactions - Collateral addition - Collateral removal - Collateral invocation - Shortfall handling - Communications and statements - ROI auditing - Current offer visibility for NBFC and LSPs - Volt - Journey - Enhancement (Fetch/Pledge/Offer/Agreement) - Nudges - B2B2C & B2C - PF/ROI changes - Journey - Admin actions (PF increase to work out of the box) - Payout - Scope reduction - Loan offer - PF/ROI - Contract level - Volt UI --- - Nudge - Current limit - Updated Limit - Current ROI - New ROI - LTV update charges - KFS/Agreement - Task name - Service request approval - Left panel - Request details - Request ID - Service request type : Limit enhancement - Requested on - Current collateral limit - Additional collateral limit - Updated collateral limit - Limit enhancement charges - AMC charges - Substatus - Maker name - Maker remark - Maker created on - Collateral details - ISIN - Asset type - Collateral sub type - Folio - Value - Existing limit - New limit - Right panel - Client details - Loan details - With loan contract - Transactions - Collaterals - Collaterals with details (LTV) - Loan kit - KFS - Agreement - Generate offer what happens? - Request - FXLAN (with collateral details) - Response - Funds with higher LTV - Limit enhancement charge ranges - AMC charge ranges - ROI ranges - Accept offer - Request - Fund with LTV, charges & ROI details - Response - Offer ID - Service request and collateral addition in parallel, what validations to happen

---

## #17 — Term loan CC enhancements
**Status:** Not started | **Last edited:** May 11, 2026 11:26 AM

**In scope:**
- Providing visibility for automatically closed tranches within Command Centre
- Displaying granular excess margin breakdown:
    - Total excess margin
    - Refundable excess margin
    - Non-refundable excess margin (tranche-tagged)
- Displaying the above excess details within:
    - Loan details page
    - Checker task screens
- Displaying due details/TOS visibility within collateral release ch

# Term loan CC enhancements # **Background and Context** - Operations teams currently face multiple visibility and workflow challenges while managing term loans in Command Centre. - Closed tranches automatically disappear from Command Centre once they are closed, resulting in complete loss of visibility for the Ops team for historical tracking and issue resolution. - Excess refund handling for term loans differs from OD loans. Tranche-tagged excess margins are non-refundable, however Command Centre currently does not provide a granular split between refundable and non-refundable excess. This creates inconsistencies between excess refund tasks and the loan details page, making it difficult for Ops teams to follow existing SOPs. - During collateral release approval flows, Ops teams need to validate whether requested DP for un-pledge is within permissible limits `(Unpledge requested DP <= Total DP - TOS)`. Currently, checker tasks do not display TOS or due details, forcing Ops users to manually navigate to loan details pages to retrieve data, leading to delays and increased chances of operational errors. - These gaps impact operational efficiency, increase dependency on manual checks, and create risks of incorrect approvals/refunds. --- # **1. Problem scope** ### In scope - Providing visibility for automatically closed tranches within Command Centre - Displaying granular excess margin breakdown: - Total excess margin - Refundable excess margin - Non-refundable excess margin (tranche-tagged) - Displaying the above excess details within: - Loan details page - Checker task screens - Displaying due details/TOS visibility within collateral release checker tasks - Supporting operational workflows for: - Excess refund handling - Collateral release approval validation - Historical tranche visibility ### Out of scope - Any modification in tranche closure logic - Changes in excess refund business rules or refund eligibility logic - Any customer-facing UI changes - Automation of collateral release approval decisions - SOP/process changes outside visibility enhancements --- # **2. Success Criteria** - Reduction in Ops dependency on manual loan detail verification during checker approvals - Elimination of visibility gaps for closed tranches within Command Centre - Alignment of excess margin values across: - Excess refund tasks - Loan details page - Checker tasks - Reduction in operational TAT for: - Excess refund processing - Collateral release approvals - Reduction in manual operational errors caused due to context switching between pages ### Guardrail metrics - No degradation in Command Centre task loading latency - No incorrect excess classifications post launch - No impact

---

## #18 — [Platform] Unpledging of unlinked funds bulk appro
**Status:** Pending Review | **Last edited:** March 5, 2025 10:35 AM

**Problem:**
are we solving?**

There can arise scenarios where the user pledges securities with the NBFC and changes their mind and does not end up taking a loan with the NBFC. 

As per an RBI regulation, the REs are supposed to release all the original movable / immovable property documents and remove charges registered with any registry within a period of 30 days after full repayment/ settlement of the loan account. ([Link](https://www.rbi.org.in/Scripts/BS_CircularIndexDisplay.aspx?Id=12535&utm_source=chatgpt.com))

While the regulation does not explicitly mention the scenario where the loan is not tak

**Solution:**
?**

We will be making a bulk operations maker, which will allow the NBFC operations agent to upload a file (at a security / ISIN / Lien reference number level). 

Bulk (file based) checker task for validation of the bulk unpledging file by the operations team (Manual verification of the initially lodged file)

NBFC currently supports unpledging requests only at a loan account level, a loan account is created only when the origination process (loan application) is completed by the user. We will be creating an opportunity level unpledging workflow (using step functions) to support the complete unpledging process.

Each bulk maker job (like bulk lodgement) will create independent unpledging requests at an opportunity level, these independent requests will be present in the applications secti

---

## #19 — Custom Comms based for Ad-hoc situations
**Status:** Not started | **Last edited:** March 27, 2026 2:28 PM

**Problem:**
are we solving?

- All comms today are system-triggered and automated — ops, compliance, and analytics have zero ability to send ad hoc communications without a tech deployment.
- High-urgency situations (system or service down , regulatory events, manual outreach, one-off campaigns) require immediate comms capability that bypasses the automated pipeline.
- Today adhoc communcoation are sent by product using a script, this consumes a lot of product effort
- There are a few communications which are dependent on flows are in itself are not produtised, hence it is challenching to productise commu

**Solution:**
?

---

## #20 — Product note Co-lending foreclosure - Deprecated -
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

## #21 — Margin pledge charges
**Status:** Pending Review | **Last edited:** June 19, 2025 4:24 PM

**Problem:**
are we solving?**

Currently, DSP Finance offers a maximum sanction limit of ₹2,00,00,000, allowing users to pledge collaterals post-account opening up to this limit (calculated as NAV × LTV × Units) to access credit.

However, this leads to cost implications such as lien marking charges, ongoing tech maintenance, and operational overheads, which are not being recovered from users today. To address this and improve monetisation, we plan to introduce pledge invocation charges, applicable when users pledge additional securities to increase their credit limit.

---

- Increased IRR (Internal rate

**Solution:**
?**

We will be applying margin pledge charges (Additional pledge charges) on the user’s loan account. Margin pledge charges will be applied. The same will be added in the product construct.

---

## #22 — Disbursement workflow optimisations
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

## #23 — Making Mobile & Email Verification Log Optional LO
**Status:** Not started | **Last edited:** July 18, 2025 12:17 PM

**Problem:**
are we solving?**

As per RBI’s CDD guidelines, verifying ~~either~~ the customer’s ~~mobile number or~~ email is mandatory. Currently, LSPs must verify ~~the mobile number and submit mobile verification &~~ email and pass the verification logs via the `mobile_verification_log`/`email_verification_log` APIs respectively. The resulting utility IDs are required in the `Submit Opportunity` API to create the loan application at DSP’s end.

However, some LSPs have highlighted friction in integrating these additional API, noting that both mobile number & email are already verified on their end and c

**Solution:**
?**

To reduce integration friction while maintaining regulatory compliance, we propose making the ~~mobile verification log API &~~ email verification log API optional. Instead, DSP will include a clause in the LSP agreement mandating that LSPs verify the ~~mobile number/~~email  shared with DSP during opportunity creation and ensure that ~~mobile &~~ email verification logs can be furnished offline, on demand, whenever requested by DSP to meet audit and compliance requirements

~~This exemption is **not applicable** if:~~

- ~~The LSP does **not** use DSP’s fund fetch or lien marking APIs, or~~
- ~~The LSP allows the user to update/change the mobile number before initiating DSP’s fund fetch or pledge flow.’~~

---

## #24 — Implementing UTR dedupe for repayment postings
**Status:** Pending Review | **Last edited:** July 14, 2025 3:52 PM

**Problem:**
are we solving?**

---

- We currently do not perform a deduplication (dedupe) check on incoming repayment requests from Lending Service Providers (LSPs), which poses a risk of **duplicate repayment postings**. This issue becomes critical as we scale with more LSPs like PayTM and PhonePe initiating repayments through their own Payment Gateways (PGs).
- Additional complexity arises because **UTR (Unique Transaction Reference) numbers are only unique at the bank level**, not globally. Hence, simply using UTR for deduplication is not sufficient and can lead to false positives or missed duplicates

**Solution:**
?**

---

## #25 — [Platform] BRE configurations for approval tasks
**Status:** Done | **Last edited:** January 9, 2025 10:54 PM

**Problem:**
are we solving?**

Requests raised by the users in relation to their loan account and application journey go through STP and non STP flow. Non STP transactions go through an approval mechanism on the command centre.

As we continue to launch the DSP platform across channels, we will require platform and request level checks and rule engines to control approval mechanisms and handle teething phases for launch across channels.

---

**Solution:**
?**

Partner and channel level BRE configurations:
We will be building partner and channel level BRE capabilities to define STP and non STP rule engine which will govern the approval of a task.

<aside>
💡

For example: We may approve STP lodgements for Volt while keeping it an approval flow for a new partner like Groww or IndMoney

</aside>

Request level BRE configurations:

We will be building request level rules which will govern if the said request will be going through an STP flow or a non STP flow (checker approval).

Each rule can have a threshold value which can be different at a request/channel level.

<aside>
💡

For example: We have a rule to auto approve lodgement requests with a limit under 10 lakh for Volt and 2 lakhs for Groww

While the parameter here is credit limit, it can

---

## #26 — [Platform] Mandate collection BRE optimisation
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

## #29 — [Platform] QC rejection handling
**Status:** Ready for Tech | **Last edited:** January 21, 2025 2:16 PM

**Problem:**
are we solving?**

To ensure a valid application, we have developed a quality check flow on the command centre through which operations team can verify core aspects of an application and decide to either approve or reject it.

If a discrepancy is found in the QC application, the operations team is supposed to reject the QC, however the corresponding outflow of information to the customer and the LSP is not handled. 

This impacts the user’s application experience  (as by then the securities are pledged by the user) and increases TAT for an application to get processed. It also consumes signifi

**Solution:**
?**

We will be sending callbacks to the LSP for the corresponding rejections on the application. LSPs basis the callback will handle the corresponding orchestration to handle the user’s application.

Send backs can occur due to the following broad scenarios (in one or multiple sections):

- Value mismatch / Discrepancy (Eg: Photo of the customer and OVD does not match) - Soft reject
- Policy breach (Eg: Policy allows applicants aged 21–60, but the customer is 19 or 65) - Soft reject
- Other (Remarks) (Eg: There are issues with document uploads or system errors during processing.) - Soft reject

It will be the LSPs decision and responsibility to handle the corresponding orchestration. 

Following are the scenarios that we will be handling in V1:

| **Section** | **Subsection** | **Details*

---

## #30 — [Fenix] Lodgement maker bulk approval
**Status:** Done | **Last edited:** January 16, 2026 7:47 PM

**Problem:**
are we solving?**

We operate with two RTAs, CAMS and KFIN, while CAMS currently offers synchronous lien marking of funds (will soon move to asynchronous pledging), KFIN’s lien marking process is asynchronous.

That is upon submitting a lien marking request, we get a request successfully accepted status, post which we poll for a confirmation of lien marking with KFIN using lien status API to get a confirmation. 

Following requirements and discussions will be specific (as per current implementation) to KFIN pledging but would be designed in a way to support both CAMS and KFIN asynchronous pled

**Solution:**
?**

We will be building a bulk lodgement maker which will enable DSP operations team to manually lodge securities into a loan account of users which were previously rejected / or were failed to be raised for lodgement by the NBFC.

(Customers can directly reach DSP Finance support team for lodgements if their requests are not supported by the LSP)

While we give this functionality to the operations team, it is of utmost important to build validations both via operations (maker/checker) and system (validations) to ensure there are no invalid lodgements into the loan account of the user.

If a lodgement is incorrectly lodged into the loan account of the user, it will expose the NBFC to open financial risk, where the user can withdraw more than they could have causing LTV breaches and even s

---

## #31 — [CC] Lodgement Enhancement
**Status:** Not started | **Last edited:** February 7, 2025 6:19 PM

**Problem:**
are we solving?**

The operations team needs to verify loan collateral before lodgement for the following conditions:

1. Loan Value over 10L: To ensure we are not in credit risk in cases with large amounts
2. Date mismatch (more than a day): To ensure the funds which are up for lodgements are still pledged and no un-pledging request for those funds have been raised.

These ensure that we minimise credit risk (assign accurate credit limit to right loan accounts).

- **Current steps to approve a lodgement considering there are two folios, one for CAMS and another for Kfintech**
    1. Login to 

**Solution:**
?

Following are the solutions we will be implementing to increase the efficiency of the Ops team and reduce the time taken to approve lodgements:

---

## #32 — [CC] Showcase the reason for freezing on CC
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

## #33 — [LSP] Document upload support for maker
**Status:** Done | **Last edited:** February 3, 2025 8:55 AM

**Problem:**
are we solving?**

We have made developed maker tasks which enable the operations team to perform certain actions on to the loan accounts of the user and support them with their needs or solving for operational use cases.

For example:

- Reversing a charge
- Posting a charge
- Reversing a repayment
- Posting a repayment
- Suspending a loan account
- Un suspending a loan account
- Bank account update

However, all operations performed by the operations team, impact the user experience and accordingly should be done carefully, most of these requests have to be either linked to a user request, o

**Solution:**
?**

---

## #34 — [Volt] Photo and Bank Deviations enhancement
**Status:** Not started | **Last edited:** February 25, 2025 9:00 PM

**Problem:**
are we solving?**

Over 165 users have provided the same bank account and supporting details when their application goes into a bank deviation. Also, in the case of photo verification, several users attempt and re-try upto 47 times (because of rejection and/or going into deviation) before getting approved.

In the case of Bank Deviation, if the applicant is rejected by the checker they are brought back to the screen to continue the application process without any communication regarding the deviation being rejected.

Its the same case with photo deviation rejections.

This hampers the user exp

**Solution:**
?**

No communication to our user after a rejection of a bank deviation is the main causer for this issue.

---

## #35 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #36 — DSP Bank Account Update and Mandate Re-Registratio
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

 

This document outlines the requirements for enabling both **LSPs** and **internal DSP operations teams** to initiate **bank account updates** and **mandate re-registration** for customers, through streamlined APIs and a user-friendly interface.

**Solution:**
?**

We need to develop the following capabilities:

1. **Wrapper APIs for LSPs**
    - So they can integrate the ability to verify bank, update primary bank accounts and initiate mandate registration directly from their platforms for post loan customers.
2. **Mandate Re-registration Workflow on Command Center**
    - Enable internal DSP Ops teams to:
        - Re-initiate mandates from the Command Center (without DIGIO dashboard dependency)
        - Send mandate registration links via email/SMS to customers
            - Perform both single-customer and bulk actions to generate mandate link
3. **Report Generation and Bulk Communication**
    - Identify customers whose mandates are not registered
    - Export this list with customer details, bank details, sourcing channel and mandate stat

---

## #37 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #38 — Revocation MIS - TCL customer
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. Send Revocation MIS to TCL for post loan cases so that act on the releasing securities faster
    1. TCL lien removal tool checker failure cause delay in processing of request.
2. Send revocation MIS to TCL for pre loan cases so that they can release the collateral for those user who has pledged but not taken any loan in 30 days.

---

**Solution:**
?**

1. MIS for post loan [P0]
    1. Send MIS report on daily basis at 6 PM for the request timeframe = 6:00 PM of T-1 to 5:59 PM of T
    2. MIS file name: REVOCATION_FOR_ACTIVE_LOAN
    3. MIS file format: https://docs.google.com/spreadsheets/d/1HrbePFE-uFyI4KmCIE0_XcXHmHBnPCsV/edit?usp=sharing&ouid=113729949292157260894&rtpof=true&sd=true
2. MIS for pre loan [P1]
    1. Customer who has pledged their funds and has not completed the loan application with lender which means credit does not exist but asset is pledged for more then 30 days
    2. Check 30 days from pledge date 
    3. MIS file name: REVOCATION_FOR_NO_ACTIVE_LOAN
    4. MIS file format: https://docs.google.com/spreadsheets/d/1HrbePFE-uFyI4KmCIE0_XcXHmHBnPCsV/edit?usp=sharing&ouid=113729949292157260894&rtpof=true&sd=true

---

## #39 — Ticketing Tool Evaluation Document
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# Ticketing Tool Evaluation Document ## 1. Introduction ### Purpose of Evaluation The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation. ### Scope and Objectives This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include: - Analyzing feature sets and usability - Evaluating system performance and reliability - Reviewing security and compliance standards - Assessing cost-effectiveness and support options DATA sharing over WA and 1:1 WA chat with MFD - PI Data and any other data ## 2. Current Challenges ## Agent Challenges/process gap | # | Challenge | Impact | Priority | | --- | --- | --- | --- | | 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 | | 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 | | 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 | | 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 | | 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 | | 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 | | 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 | | 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 | | 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 | | 10 | No visibility into **TAT of internal ticket and resolution TAT from the 3P** | Inability to provide ETAs to customers | P0 | | 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 | |

---

## #40 — AppSmith Enhancement
**Status:** Pending Review | **Last edited:** February 10, 2025 11:43 AM

**Problem:**
are we solving?**

- Currently sales and ops team face information insufficiency while dealing with customers

---

**Solution:**
?**

---

## #41 — Attribution for Volt applications
**Status:** In progress | **Last edited:** December 9, 2024 5:07 PM

**Problem:**
are we solving?**

Currently, our LOS has limitations in processing and attributing applications of the same customer (PAN number being unique) across channels, platforms and partners.

The impact of this can be categorized into below buckets.

- Number of applications which convert are impacted
- Partner experience is impacted due to their applications not being serviced
- Incentives of internal team members are impacted
- Impact on funnel in terms of application to account opening
- Internal users don’t have the complete context of the customer
- Impact on customer satisfaction score due to 

**Solution:**
?**

---

## #42 — Mobile email dedupe check in case on in-progress m
**Status:** Pending Review | **Last edited:** December 25, 2024 6:42 PM

**Problem:**
are we solving?**

- Users can request a mobile number update (e.g., from P1 to P2) for lenders BFL/DSP.
- The mobile number update involves a processing time (TAT) due to:
    - Maker-checker flow at DSP.
    - Operational flow at BFL.
- During this processing time, if a user:
    - Logs in with the new mobile number (P2), or
    - Fetches their Mutual Fund portfolio using P2,
    a new application is created in our system with P2.
- Once the mobile number update is processed:
    - The system ends up with two accounts linked to the same mobile number (P2).
- This results in complications suc

**Solution:**
?**

**Mobile update in progress**

- User can create a new application through following 3 routes
    - MFC fetch
    - In app login
    - Login through SDKs
- Action for each of these routes
    - MFC fetch - Block the user (UI handling)
        
        ![Screenshot 2024-12-23 at 6.21.21 PM.png](Mobile%20email%20dedupe%20check%20in%20case%20on%20in-progress%20m/Screenshot_2024-12-23_at_6.21.21_PM.png)
        
    - In app login - Block the user (UI handling)
        
        ![Screenshot 2024-12-23 at 6.20.54 PM.png](Mobile%20email%20dedupe%20check%20in%20case%20on%20in-progress%20m/Screenshot_2024-12-23_at_6.20.54_PM.png)
        
    - Login through SDKs - Throw an error in the createCustomer/getCustomer API
        
        ```jsx
        {
            "message": "Lead with the same

---

## #43 — [Platform] Agent session management
**Status:** In progress | **Last edited:** December 22, 2024 1:03 PM

**Problem:**
are we solving?**

As an NBFC, it is important to maintain access control across applications due to the sheer amounts of PII information that is passed to respective stakeholders based on their roles and functions.

While it is important to ensure the right person sees the right information based on their respective functions, it is also important to control it by external factors (so that unauthorised access to the information cannot be gained).

Command centre manages this by the following features:

- 2 factor authentication (User ID + Password + Email OTP)
- Permission based access contro

**Solution:**
?**

---

## #44 — [Platform] Risk report
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

## #45 — Volt DLS 2 0
**Status:** In progress | **Last edited:** December 12, 2024 1:59 PM

# Volt DLS 2.0 # Why —————————————————— - Reduce front end effort to create new features and products - Reduce effort of maintaining multiple DLS - Faster design + dev time: Faster decision making and alignment on design - Significantly higher consistency - Easier onboarding for new joinees <aside> 🎯 **Goal:** To create a singular org level DLS that helps build all our products: Core, web, dashboards, command center, etc. </aside> # What —————————————————— ### Process 1. Brand positioning doc - : *in progress* [Brand Positioning Doc](Volt%20DLS%202%200/Brand%20Positioning%20Doc%207b616b64989b4dd68419a624c15997eb.md) 2. User research: *in progress* 3. Market research/Competitor analysis - benchmarking [Market research](Volt%20DLS%202%200/Market%20research%20856a208a18e54d899487aa1703345e80.md) 4. Heuristic evaluation of current design 5. Finalise tokens 1. Keyword mapping 2. Options 1. UI language 2. Typography scale + tokens 3. Color scale + tokens 4. Components In-depth implementation [WIP]: [https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing) ## Scope [Scope](Volt%20DLS%202%200/Scope%20ad8083b8d6fd44fa8e0d2d347d7c5fe0.md) **Tokenization representation** - L3: Mapped - L2: Alias - L1: Primitives [https://thedesignsystem.guide/design-tokens](https://thedesignsystem.guide/design-tokens) [https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676) ![image.png](Volt%20DLS%202%200/image.png) ## ⛳️ Typography scale - Ability to update Heading font style separately than Body - Allow having capitalisation in subheaders, tags etc - Allow using singular token for a style which auto switches between mobile (14px), web, MFD, DSP (16px), command center (12px) ### **How →** - Primitives: xs, sm, md, lg… ,etc. - Alias (Text styles) - Tokens: H1, H2, H3, H4… B1, B2, B3, B4… - Theme: Core-mobile, Core-web, DSP-mobile, DSP-web ## ⛳️ Color scale - Allow switching themes for light and dark mode - Allow switching primary, secondary, success, etc colors for different products/brands/SDKs - Allow modifying individual component level colors. Eg: borders, CTAs, headings, secondary text, disabled, etc ### **How (WIP) →** - Primitives: blue (50, 100, 200…900), turquoise (50, 100, 200… 900)… red (50, 100… 900) - Alias - Primary (50, 100… 900), Secondary (50, 100… 900), Success (50, 100… 900) - Theme: Core, DSP - Mapped - Types: - Text (primary, secondary, action, disabled, success, warning…) - Surface (background, primary, secondary, info, action…) - Border (primary, secondary, warning, error…) - Icon (primary, action, error…) - Theme: Light, Dark ## ⛳️ Component level - Allow switching component styles (corner radius, padding, color…etc.) for different use-cases: Core, DSP, dashboards, command center etc. ### Priority components: 1. Top header bars 2. Buttons 3. Bottom sheet 4. Input fields 5. Form logic + behaviour 6. Bottom nav bars 7. Toasts, notification 8. Tabs - Refer to small case filter screen + chips + tabs inside MF selection 9.

---

## #46 — [Lending stack] Command centre - QC
**Status:** Not started | **Last edited:** August 29, 2024 11:56 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #47 — [DSP] Dues collection comms
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

## #48 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #49 — [Platform] Validation to Stop Un-pledging, closure
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

## #50 — E2E Sell-off Productisation 34ae8d3af13a80928d80d8
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

## #51 — Admin tool migration to Appsmith
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

## #52 — VA Repayment Handling [Volt LMS]
**Status:** Not started | **Last edited:** April 10, 2025 10:50 AM

**Problem:**
are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

**Solution:**
?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

---

## #53 — Appsmith design
**Status:** Ready for kickoff | **Last edited:** Unknown

# Appsmith design Charter: LMS Pod Priority: P0 # Context [Admin tool migration to Appsmith](../PRDs/PRDs/Admin%20tool%20migration%20to%20Appsmith%20196e8d3af13a80c6897bee9558cf7197.md) # Process - [x] Start with User details - [ ] Work on bulk actions # Figma

---

## #54 — Lodgement addition and removal maker
**Status:** Ready for kickoff | **Last edited:** Unknown

# Lodgement addition and removal maker Assign: Karuna Sankolli Charter: NBFC Pod Task type: Sprint # Context [https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469](https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469) **MOM** 1. Discovery you can maker for lodgement 2. Upload 3. Review 1. Dedupe check -> Already lodegd or not 2. Pledge check -> Pledged with the LSP 4. Data points 1. Folio 2. Loan acct number -Future 3. PAN number 4. Investor name 5. Units 6. Scheme name 7. Lien ref number CAMs 8. IHNO Kfintech 9. ISIN 10. Status 11. Remarks 5. Do I want to ops to work on the file, RTA level 6. Grouping based on PAN & Loan acct number # Figma [https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system)

---

## #55 — E2E Sell-off Productisation V1
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

## #56 — API flow for KFS and Agreement
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

## #57 — Additional details enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

To support underwriting and assess the end use of funds, we currently collect the following additional user details:

- Marital status
- Educational qualification
- Mother's first and last name
- Father's first and last name
- Loan purpose
- Income range
- Employment status

While this information is essential, requiring users to fill seven separate fields has contributed to a noticeable drop-off rate—ranging from **1% to 5% across different LSPs**—which negatively impacts the top of the funnel.

---

**Solution:**
?**

- V2 API with optional and mandatory fields
    - Mandatory fields:
        - Employment details
        - Income range
        - Father’s name
        - Loan purpose
    - Optional fields
        - Educational qualification
        - Mother’s name
- Handling UI changes on Command centre to make it intuitive for the operations team

---

## #58 — Approved Scrips productisation
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
We are solving for:

- A governed, audited maker-checker flow for all approved scrip updates in Command Centre
- Support for the following scrip operations via this flow:
    - **Approve new ISIN** — add a new ISIN (Mutual fund or Share) to the approved scrip with all required parameters
    - **Stop new lodgements** — set min LTV to zero for an ISIN (blocks new pledges without impacting existing 

# Approved Scrips productisation Last Edited: May 8, 2026 12:03 PM PRD ETA: April 21, 2026 PRD Owner: Vaibhav Arora ## Background and Context The approved scrip list is the master reference that controls which ISINs can be pledged as collateral in the LMS, and at what LTV. It has two layers: - **Finflux approved scrip** — Global NBFC-level list managed in the LMS (Finflux). Stores min LTV and max LTV per ISIN and enforces that no lodged collateral exceeds max LTV. (Min LTV for default LTV value, Max LTV as a ceiling validation) - Finflux max LTV should be equal to Risk LTV and Finflux min LTV should be equal to Fenix min LTV - **Fenix approved scrip** — Internal list managed at a co-lender relationship (contract) level (colending vs non-colending) and product level (LAS and LAMF). Fenix carries three LTV values per ISIN: Regulatory LTV (= max LTV), Risk LTV (internal ceiling set by the risk team, ≤ Regulatory LTV), and Min LTV. Today, updates to both scrips require manually calling APIs in Fenix and Finflux separately. This is done by anyone with API access and without any audit trail, approval gate, or role-based control. **Who is affected:** - Risk ops team (makers) who need to update scrips frequently but have no safe, governed tool to do so - Risk managers (checkers) who have no visibility into what changed, when, and by whom - End users and LSPs who are indirectly impacted by incorrect LTV values (inflated or deflated offers, wrong shortfall calculations) **What is broken today:** - Fenix and Finflux scrips are updated separately and can fall out of sync — they should be updated atomically - Direct API updates are error-prone. A documented past incident set LTVs to 50 instead of 50% causing 100x limit inflation - No audit log exists for scrip changes — there is no way to trace who changed what and when - No role-based control — anyone with API access can make changes with immediate live impact on offer generation and shortfall computation **Why it matters now — three upcoming catalysts:** 1. **Colending expansion** — More colending relationships mean more contract-level approved scrip variants, increasing change frequency 2. **LTV increase to 70%** — Moving from 45% to 70% introduces higher risk volatility and requires more frequent scrip tuning by the risk team 3. **Loan against Shares launch** — Shares are more

---

## #59 — Charge details on Command centre
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

## #60 — Charge reversal enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges for a user is manual, operationally intensive, and people-dependent process. Not only does this make it error prone, it introduces friction across internal teams and impacts customer experience. The key issues we’re addressing include:

---

**Solution:**
?**

We will be creating a charge waiver task for command centre which will behave in the following manner:

- If a charge is completely outstanding, that is the amount that was applied has not been collected from the user, will be waived.
- If a charge is completely paid/collected from the user, we will be passing a credit note to the user’s loan account

<aside>
🚨

If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error). - We will now be passing a credit note for this as well

</aside>

- If a charge is partially paid/collected, we will not allow it to be waived or refunded - (Validation error).

We will be creating a new payment type called “CREDIT_NOTE” this repayment will not have a corresponding money transaction associated with it.

---

## #61 — Charge reversal enhancement V2
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

## #62 — LAS CMS Lodgement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

For collateral lodgement, DSP Finance needs to verify that pledged securities have been successfully marked in its name before associating them with user loan accounts and extending drawing power.

Unlike non-demat holdings handled by RTAs (CAMS/KFIN), where lien verification capabilities exist, depositories (CDSL/NSDL) do not provide a programmatic lien status check. This gap creates an operational dependency: DSP Finance cannot directly validate lien marking in real time.

To address this, DSP Finance will rely on ingestion of the PMR (Pledge Master Report) provided by dep

**Solution:**
?**

- **PMR-based validation** – Since no lien verification API is available, lodgement will rely on accurate and timely ingestion of PMR data.
- **Derived pledging requests** – The system will generate internal pledging requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – Lodgement will only be approved once reconciliation confirms DSP’s lien.
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Lodgement)

---

## #63 — LAS CMS Unlodgement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

For collateral removal, DSP Finance needs to verify that requested securities for removal are successfully marked in its name before removing them from user loan accounts to ensure that no financial exposure is created for the NBFC.

Unlike non-demat holdings handled by RTAs (CAMS/KFIN), where lien verification capabilities exist, depositories (CDSL/NSDL) do not provide a programmatic lien status check. This gap creates an operational dependency: DSP Finance cannot directly validate lien marking in real time.

Additionally, unlike RTAs, digital removal of securities via APIs

**Solution:**
?**

- **PMR-based validation** – Since no lien verification API is available, removal will rely on accurate and timely ingestion of PMR data.
- **Derived removal requests** – The system will generate internal removal requests from PMR entries and reconcile them against originator-reported transactions.
- **Reconciliation-first approval** – Revocation will only be approved once checker confirms task on Command centre
- **Exception handling** – Any mismatches between pledged securities and PMR entries will be flagged for manual resolution.
- **Lifecycle management**: Management of add collateral request via CMS (Removal)

---

## #64 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #65 — PMR consumption
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?

Today, Pledge Master Reports (PMRs) are received over email at [collaterals@dspfin.com](mailto:collaterals@dspfin.com). The ops team shares these with engineering, who manually hit an API to consume the report - creating an operational bottleneck that directly impacts loan account opening timelines for the Loan Against Shares (LAS) program.

We need to eliminate this manual handoff by automating PMR ingestion the moment the email arrives, while preserving a checker workflow for validation and audit.

In a Loan Against Securities (LAS) setup, collateral positions are dynamic se

**Solution:**
?

---

## #66 — Product Note Interest Refund via Credit Note
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, e

# Product Note: Interest Refund via Credit Note Last Edited: January 23, 2026 8:15 PM PRD ETA: July 22, 2025 PRD Owner: Vaibhav Arora ## Background and Context **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged or goodwill interest waivers - Operations team processing interest refunds/waivers - Finance team managing manual accounting entries for interest reversals - Tech ops/Product handling backend interventions for interest adjustments **What is the challenge that they are facing? What is broken today?** - Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access - Process is operationally intensive with dependency on Jira ticket workflows - No standardized maker-checker workflow for interest refunds similar to charge refunds - Manual JV posting for interest reversals creates additional overhead for Finance team - Lengthy resolution time (2-3 days) impacting customer experience - No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period - Lack of visibility and tracking for interest refund requests across the loan lifecycle **Why is it important? What is getting impacted?** - Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests - Operational inefficiency with high manual effort required for each interest refund case - Risk of errors and duplicate processing without systematic validations - Finance team bandwidth consumed by repetitive manual JV entries - Lack of audit trail and reconciliation capabilities for interest reversals - Inconsistent treatment of interest refunds compared to the now-standardised charge refund process --- ## 1. Problem Scope ### In scope **What specific problems are we solving?** 1. **Slow Resolution Time:** - Interest refund requests take 2-3 days to resolve from initiation to completion - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product 2. **Operational Bottleneck and Dependency:** - Operations teams cannot independently process interest refunds or waivers - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention - Backend access and API calls are needed for what should be a routine operational task - Process creates unnecessary dependencies across multiple teams for resolution 3. **Risk of Duplicate Processing:** - No systematic validation exists to check if interest for a specific period has already been waived or refunded - Product team rely

---

## #67 — Product Note Post-Loan ROI Correction Workflow
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**Task to be productized:**

- Enable Ops to execute post-loan ROI correction through Command Centre instead of a local script
- Support both single-loan ROI correction and batch ROI correction via CSV

**What are we solving?**

1. Manual execution dependency

**Who are we solving it for?**

- Product Operations
- Business team
- LSP

# Product Note: Post-Loan ROI Correction Workflow Last Edited: May 15, 2026 7:22 PM PRD ETA: May 15, 2026 PRD Owner: Abhijeet Jha ## Background and Context **Who is facing the problem:** - Product Operations team, who currently execute post-loan ROI changes manually **What is broken today?** - ROI updates are done via a Python script run locally by Product Ops - The operator has to prepare a CSV, refresh the Finflux auth token, run the script, and verify output manually - There is no single system to create, track, execute, and audit these requests **Why is it important?** - Effort is high for a repetitive internal workflow **Example scenario:** - ET Money offers ROI of `9.99%` for the first 3 months - After 3 months, ROI needs to be updated to `10.75%` - Today, this is done only after business confirmation and script execution by Product Ops --- ## 1. Problem Scope ### In scope **Task to be productized:** - Enable Ops to execute post-loan ROI correction through Command Centre instead of a local script - Support both single-loan ROI correction and batch ROI correction via CSV **What are we solving?** 1. Manual execution dependency **Who are we solving it for?** - Product Operations - Business team - LSP ### Out of scope - Customer-facing communication - Partner or LSP self-serve workflow --- ## 2. Success Criteria **Expected outcomes:** 1. Standard ROI correction cases move from script execution to Command Centre 2. Ops can execute approved ROI updates faster and with lower manual effort 3. Every request has a visible execution outcome: success, failure, or partial success **Good post-launch state:** - Ops can create single or batch requests in Command Centre - System validates current ROI before update - System verifies final ROI after update - Loan-level outcomes are visible for both single and batch requests --- ## 3. Solution Scope ### Solution overview We are implementing an internal **Post-Loan ROI Correction Workflow** in Command Centre to replace the current script-based process used by Product Ops. - single-account ROI correction - batch CSV upload - business-approved or otherwise authorized internal ROI correction requests ### Inputs required - `loan_account_number(FXLAN)` - `current_interest_rate` - `updated_interest_rate` ### Core workflow 1. Ops create a request in Command Centre 2. Operator enters request details or uploads CSV 3. System fetches current interest details from Finflux 4. System validates current effective ROI against the request input

---

## #68 — Product note Credit note for TL
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

We are solving:

# Product note: Credit note for TL Last Edited: April 28, 2026 4:45 PM PRD ETA: April 17, 2026 PRD Owner: Vaibhav Arora # **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)** --- ## **Background and Context** **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged interest - Operations team handling refund/waiver requests - Finance team managing manual income reversals and reconciliation - Product/Tech teams currently intervening via backend/API --- **What is the challenge today?** - Interest refunds require **manual intervention via engineering or Finflux access** - No standardized **maker-checker workflow** - **Not supported for Term loans, currently productised and implemented only for OD** - Manual JV posting required for income reversal - No **system-driven dedupe or validation** - No **tranche-level visibility or audit tracking** - Turnaround time is **2–3 days**, impacting CX --- **Why is it important?** - Poor customer experience due to delays - High operational dependency and inefficiency - Risk of duplicate or incorrect refunds - Manual accounting overhead for finance - Lack of audit trail and reconciliation visibility --- ## **1. Problem Scope** ### **In Scope** We are solving: ### **1. Operational Independence** - Enable Ops to process **interest refunds without engineering dependency for Term loans** - Introduce **maker-checker workflow** --- ### **2. Standardized Accounting** - Eliminate manual JV posting - Introduce **credit note + automated income reversal** --- ### **3. Tranche-Level Refund Handling** - Refunds applied at **tranche level (not line level)** - Excess created is: - Initially **tranche-tagged** - **Not usable across tranches while tranche is active** - Becomes **line-level usable only after tranche closure** --- ### **4. Validation & Dedupe** - Prevent duplicate refunds via: - Schedule validation - Credit note existence checks --- ### **5. Audit & Traceability** - Full linkage: - Interest → Credit Note → JV - Tranche-level enrichment and reporting --- ### **Out of Scope** - Principal refunds - Bulk refund processing - Automated eligibility rules - Reversal of incorrect refunds (no reversal flow) --- ## **2. Success Criteria** ### **Outcomes** - Maker → Checker → Accounting completion within **1 hour** - **>90% reduction** in Jira dependency - Capability to refund interest for Term Loan - **Zero duplicate refunds** at tranche-month level --- ### **Post-launch Good State** - All refunds processed via maker-checker - Credit notes posted correctly at tranche level - Automated JV posted for income reversal - Finance can reconcile via

---

## #69 — Product note Excess refund Colending
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

## #70 — Product note Virtual account handling for Colendin
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

## #71 — [Platform] Foreclosure handling to support Volt fo
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

## #72 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #73 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #74 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #75 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #76 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can