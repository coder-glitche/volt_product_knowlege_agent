# Current State: B2B

> Auto-generated from 98 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — SDK for b2b2c SAAS partners
**Status:** Not started | **Last edited:** September 30, 2024 6:06 PM

# SDK for b2b2c SAAS partners ### **Interest Details Management Table** | **Attribute** | **Description** | | --- | --- | | View Interest and Charges | Access current month due interest and charges details with respective statuses. | | Filtering | Filter by mandate status, interest status, and lender name (TATA, BAJAJ). | | Search | Search the interest details table. | | Interest Calculator | Provide tools for calculating interest. | | Pre-defined Messaging | WhatsApp messages based on interest and mandate statuses. | | Pagination | Support pagination with 50 records per page. | ### **Shortfall Management Table** | **Attribute** | **Description** | | | --- | --- | --- | | View Shortfall Amounts | Access details of shortfall amounts and aging information. | | | Sorting and Filtering | Sort by due date and filter by aging and lender name. | | | Search | Search within the shortfall details table. | | | Educational Content | Provide information on what a shortfall means. | | | Pre-defined Messaging | WhatsApp messages for communicating shortfalls to customers. | | | Pagination | Support pagination with 50 records per page. | | ### **Loan Renewals Management Table** | **Attribute** | **Description** | | --- | --- | | View Loan Renewal Details | Access loan renewal information, including statuses and due dates. | | Sorting and Filtering | Filter by lender name and status; sort by customers nearest to renewal dates. | | Search | Search within the loan renewal details. | | Educational Content | Provide information about the benefits and consequences of non-renewal. | | Pre-defined Messaging | WhatsApp messages based on loan status (Active, Expired with/without amounts). | | Pagination | Support pagination with 50 records per page. | ### **General Features Table** | **Feature** | **Description** | | --- | --- | | Tab and Page Deep Linking | Allow access to functionalities via deep links on all platforms (web, Android). | | Dynamic Tab Visibility | Display or hide tabs based on customer counts (hide when count is zero). | | Consistent Data Display | Ensure uniform data presentation across SDK and internal dashboard. | ### **Detailed Customer Information Table** | **Attribute** | **Description** | | --- | --- | | Customer Name | Name of the customer. | | Phone Number | Contact number of the customer. | | Due

---

## #2 — Additional documents upload for Bajaj for AS ES DI
**Status:** Ready for Tech | **Last edited:** September 20, 2024 3:06 PM

**Problem:**
are we solving?**

We are solving for autofilling these documents for the user and integrating them in the journey to improve the loan booking experience of joint holders of mutual funds.

Broadly, there are two ways to own a mutual fund:

1. Individual ownership (single account holder)
2. Joint ownership
    1. Joint (Approval of both parties is required) (2 account holders)
    2. Anyone or survivor (AS) (anyone can manage the account without seeking the other person’s approval) (up to 3 account holders)
    3. Either or survivor (ES) (both can manage the account without seeking other’s appr

**Solution:**
?**

We will be recreating digital versions of forms (Update)

For the scope of first development we are only picking co-borrower and addendum form:

[Bajaj ECS Mandate.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/Bajaj_ECS_Mandate.pdf)

[coborrower.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/coborrower.pdf)

[_ADDENDUM SAMPLE new new (1) (1).pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/_ADDENDUM_SAMPLE_new_new_(1)_(1).pdf)

[__CO APPLICANT FORM SAMPLE.pdf](Additional%20documents%20upload%20for%20Bajaj%20for%20AS%20ES%20DI/__CO_APPLICANT_FORM_SAMPLE.pdf)

Self attested PAN (photo of the document signed by the user)

Self attested Aadhaar (photo of the document signed by the user)

```html
<!DOCTYPE html>

<he

---

## #3 — BAJAJ GetMilesAccountDetails
**Status:** On Hold | **Last edited:** September 2, 2024 11:37 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #4 — Bajaj PAN verification API
**Status:** Not started | **Last edited:** September 19, 2024 6:26 PM

**Problem:**
are we solving?**

Currently Bajaj KYC fails for the following cases:

1. Full name (First, middle and last) is not shared / shared incorrectly in the KYC pod request. 
2. PAN is not already fetched in Digilocker

---

**Solution:**
?**

---

## #5 — PhonePe Landing page requirement - 15th April
**Status:** Not started | **Last edited:** September 17, 2024 12:13 PM

**Problem:**
are we solving?**

1. **What is LAMF?** - Not a personal loan
2. Filter junk leads
3. Education about LAMF
4. **Product features- ROI, No FC, 3 hour disbursement**
5. **Use cases of this loan**
6. **Trust- TATA & Bajaj as lending partners**
7. **Steps to take loan**
8. Testimonials

---

**Solution:**
?**

---

## #6 — BAJAJ Dedupe API
**Status:** Done | **Last edited:** September 12, 2024 5:02 PM

**Problem:**
are we solving?**

Users who have their lender assigned as BAJAJ (either through BRE or Hardcode) when have an already existing loan account with BAJAJ then we come to know about this only after the user has completed the application process. 

---

**Solution:**
?**

We will hit the BAJAJ dedupe APIs -  

1. At the step of lender assigning through BRE 
2. Whenever there is a lender change from TATA to BAJAJ through admin panel  

 Following are cases which we will consider - 

1. When the user comes to the “SET LIMIT PAGE” & “USER CONFIRMED THE LIMIT”, lender is assigned to the application either through BRE or it is hardcoded for various MFDs. 
    1. **In case of MFDs : (sending comms is de-prioritised as confirmed with Ranjan/Nishant, kindly ignore)**
        1. if BAJAJ is hardcoded, and there is a dedupe, then we’ll change the lender to TATA, while also sending the comms to the MFD. 
        2. The comms to the MFD will be, when we send the comms for application completed, we can also show : 
        ***”The lender for this user has been chan

---

## #7 — BAJAJ New KFS+Agreement flow
**Status:** Done | **Last edited:** October 8, 2024 1:04 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload

---

**Solution:**
?**

---

## #8 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #9 — Email Validation Approach PhonePe
**Status:** Not started | **Last edited:** October 22, 2025 1:32 PM

**Problem:**
are we solving?**

PhonePe captures user email IDs without verification, posing compliance and communication risks. To avoid delaying go-live, an interim solution is needed to ensure basic email validity without enforcing strict verification.

---

**Solution:**
?**

- **Phase 1 (pre-Sept 30):** Use email delivery status as a proxy for verification. Undelivered cases follow a manual Ops-led validation via alternate email + OTP or fallback checks.
- **Phase 2 (post-Sept 30):** PhonePe to implement OTP-based or other standard email verification mechanisms within their frontend journey.

---

## #10 — Simplify B2B Partner Redirection Journey
**Status:** In progress | **Last edited:** October 11, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #11 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

**Solution:**
?**

---

## #12 — LSQ misattribution b2c of B2b2c data
**Status:** Ready for Tech | **Last edited:** November 27, 2024 11:25 AM

# LSQ misattribution b2c of B2b2c data # B2C to B2B2C Lead Update Specification ## Background When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues: 1. Lead tracking inefficiencies 2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams) 3. MFD partner dissatisfaction with direct customer contact ## Objective Reduce misattributed leads - Reduce Creation of the new Misattributed leads. - Update LSQ with admin action (tech pickup) - Backfill data to correct misattribution Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database. ## Technical Implementation ### API Details - **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate) - **Identifier**: Mobile Number (unique in LSQ) ### Required Field Updates ```json { "LeadDetails": [ {"Attribute": "mx_Channel", "Value": "B2B2C"}, {"Attribute": "Source", "Value": "MFD Referral"}, {"Attribute": "mx_Referred_By", "Value": "MFD"}, {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"}, {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"}, {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"}, {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"}, {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"}, {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"}, {"Attribute": "SearchBy", "Value": "Phone"} ] } ``` ## Data Migration Plan ### Initial Data Reconciliation - Tech team to provide excel export of leads updated via admin actions - Data to be shared with LSQ team for backfill - Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count) ### Scope Limitations - Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ - Focus on forward data synchronization and provided historical data only ### MFD Status Handling - Automated daily updates for partially-activated MFD status ## Requirements ### Technical Requirements 1. Admin action implementation for borrower-partner relationship updates 2. API integration with error handling 3. Comprehensive update logging for audit purposes ### Acceptance Criteria 1. Successful lead type transition (B2C to B2B2C) 2. Accurate referrer information mapping 3. Proper API response handling 4. Complete audit logging 5. Visual verification in LSQ dashboard ## Important Notes - Mobile Number serves as the unique identifier in LSQ - Lead merges occur when same email is used with different phone numbers - Implementation must include robust error handling for API failures - API failures should be notified to the team.

---

## #13 — TCL Credit Referral Automations & optimisations
**Status:** In progress | **Last edited:** November 26, 2024 4:15 PM

**Problem:**
are we solving?**

Daily 20 credit referral tickets are being created and it is taking a lot of Ops bandwidth for reviewing each of these applications, approving it from their end and keeping a track over these application for lender approval. 

---

**Solution:**
?**

- Credit referral current handling
    
    
    | **Step**  | **Check**  | **Action** |
    | --- | --- | --- |
    | KYC_Documents | PAN-Aadhar name match score | - <70% : Credit referral
    - > 70% : User continues the application |
    | KYC_Documents | Match score between user’s live photo and KYC photo  | - <70% : Credit referral
    - > 70% : User continues the application |
    | CIBIL_Check | CIBIL score check  | - < 650 : Hard reject (Ops gets a mail) 
    - > 650 : User continues the application |
    |  | Posidex check  | - Negative : Credit referral
    - Positive (001) : User continues the application |
    | Bank verification  | PAN-Bank name match score  | - <70% : Credit referral 
    - > 70% : User continues the application 
     |
- Documents taken at each of the s

---

## #14 — Volt B2B Redirection Enhancement - Park+
**Status:** Pending Review | **Last edited:** November 25, 2024 2:01 PM

**Problem:**
are we solving?**

Users experience an 80% drop-off rate during the Volt journey due to redundant mobile, email, and PAN verifications after being redirected from Park+. This creates a poor user experience, especially for non-financial platforms like Park+, where user intent is already low.

Note: This API will be generic & should be able to be consumed by other B2B partners as well. This solution is not limited to Park+.

---

**Solution:**
?**

Provide an API for Park+ to pass pre-verified user data directly to Volt, allowing users to bypass redundant verification steps.

---

## #15 — TCL getDisbursementAPI logic updation
**Status:** In progress | **Last edited:** November 18, 2024 7:44 PM

**Problem:**
are we solving?**

TCL is changing the logic for showing the DP & availableAmountForDisbursement field in the getDisbursementAPI 

---

**Solution:**
?**

- getDisbursementInfo response
    
    ```jsx
    {
        "GetDisbursementInfo_Response": {
            "DisbursementDetails": [
                {
                    "ExcessMargin": "2530.00",
                    "InterestDue": "0.00",
                    "ThirdPartyBankAccount": [],
                    "ClientBankAccount": [
                        {
                            "ClientBankName": "HDFC Bank",
                            "ClientParyBankIFSC": "HDFC0003236",
                            "ClientBankAccountNo": "178233567676"
                        }
                    ],
                    "LoanAccount": "302522",
                    "IsAdhocChargesPosting": "0",
                    "AvailableAmountForDisbursement": "2864.65",
                    "LoanNo": "144493"

---

## #16 — White-labelled Redirection Journey for B2B Partner
**Status:** In progress | **Last edited:** November 14, 2024 7:27 PM

**Problem:**
are we solving?**

Smaller B2B partners want to go live with Volt’s offering but don’t to spend a lot of bandwidth in validating the demand. Hence, they choose to opt for the redirection based offering.

The current redirection based offering presents the below challenges.

- Customers sourced from partners not having trust as they don’t know Volt
- Partners not being comfortable in bringing Volt to the flow
- Customers dropping off on Volt’s homepage
- Partners not opting to go-live with Volt
- Time taken to go-live for partners increase impacting adoption

The above challenges can be attribu

**Solution:**
?**

---

## #17 — PhonePe Contact support changes - 12th April 2024
**Status:** Not started | **Last edited:** May 6, 2024 9:14 AM

**Problem:**
are we solving?**

1. PhonePe has sent a requirement to stop lead leakage due to Volt support number available on the landing page. 
2. Number of junk inbound calls has increase 4x

---

**Solution:**
?**

---

## #18 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #19 — PhonePe press release - 30th May 2024
**Status:** Not started | **Last edited:** May 30, 2024 10:11 AM

**Problem:**
are we solving?**

Creating a static landing page for PhonePe press release due to release on 30th May. 

---

**Solution:**
?**

---

## #20 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #21 — LSQ Chat workflow - Phase 1
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

## #22 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #23 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #24 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #25 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #26 — DSP PhonePe PG Integration for PhonePe
**Status:** In progress | **Last edited:** March 8, 2025 1:25 PM

**Problem:**
are we solving?**

- Recording PG repayments from PhonePe offline will take considerable time and effort for our operations team
- Reconciling PG repayments from PhonePe will take time and will impact the SLAs from a customer experience perspective
- Delay in posting transactions will impact our accounting and result in backdated transactions, opening up a backdoor for a lot of issues

---

**Solution:**
?**

DSP will expose an API to accept payments through PG on PhonePe UI.

---

---

## #27 — PN Storing Commercial Data at Credit Level
**Status:** Pending Review | **Last edited:** March 3, 2025 12:37 PM

# PN: Storing Commercial Data at Credit Level ## Problem Statement Currently, we do not store Platform-level commercial data directly at the Credit level. Instead, this data is maintained in external Excel sheets, which creates inefficiencies in the payout calculation process. The data team must manually add these commercial details when creating payout files, resulting in: - Increased processing time - Higher risk of manual errors - Difficulty in data reconciliation - Lack of data integrity between systems ## Proposed Solution Implement a dedicated commercial data object at the Credit application level that will store all relevant commercial parameters at the time of application processing. ## Key Data Points to Store The Credit level commercial data object should include: - **Lender**: The financial institution providing the loan - **Base ROI**: Original interest rate from lender pricing grid - **Base PF**: Original processing fee from lender pricing grid - **PF Split**: Processing fee revenue distribution between platform and partners - **ROI Split**: Interest revenue distribution between platform and partners - **Payout Amount PF**: Calculated processing fee payout amount - **Payout ROI**: Calculated interest-based payout amount ## Implementation Benefits 1. **Data Integrity**: Single source of truth for commercial terms at the application level 2. **Audit Trail**: Historical record of commercial terms applied to each application 3. **Streamlined Reporting**: Direct data access for reporting without manual intervention 4. **Efficient Payout Processing**: Automated payout file generation based on stored values 5. **Reduced Manual Effort**: Elimination of manual data enrichment processes ## Considerations - Create a new data structure to store commercial data as part of the credit application object - Implement data validation to ensure complete commercial information - Add timestamp and user attribution for commercial data changes ## Example data table | **S_No** | **Platform** | **Type** | **Tata Interest base rate** | **Bajaj Interest base rate** | **DSP Interest base rate** | **Tata PF base rate** | **Bajaj PF base rate** | **DSP PF base rate** | **PF Sharing** | **Trail Sharing** | **PF Sharing %** | **Trail Sharing %** | **Comments** | Signoff | Actionable | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 | Advisorkhoj | Partner | | | | | | | | 0.5 | | | | | | |

---

## #28 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #29 — [B2B2C] GST payouts and reconciliation optimisatio
**Status:** In progress | **Last edited:** March 19, 2026 5:03 PM

**Problem:**
are we solving?**

---

- Currently processing of payouts is handled manually by the business and finance team end to end, this takes up a lot of bandwidth as the payouts involve multiple back & forth for approvals till the final payment processing takes place.
- Processing GST payouts takes more than 60% of overall payout processing of the business team, as it involves manually reconciling invoices of more than 600 partners monthly, reconciling the status of the GST payout and co-ordinating with marketing team to ensure timely communications

**Solution:**
?**

---

---

## #30 — Credit Bureau Reporting Comms
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

## #31 — [B2B2C] Modification for financial terms functiona
**Status:** In progress | **Last edited:** March 17, 2026 11:55 AM

**Problem:**
are we solving?**

---

- Business partners (MFDs, Brokers, CAs) frequently request changes on financial terms such as PF, ROI, Margin Pledge charges, and AMC based on customer negotiations and other factors.
- We currently receive ~170 such requests every month. These are manually processed by the sales team through admin actions, consuming bandwidth and increasing the risk of manual errors. These manual errors directly impact partner payout calculations.
- Around 10% of these requests result in increased business impact for Volt (e.g., partners increasing any financial term above the base va

**Solution:**
?**

---

---

## #32 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #33 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #34 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #35 — Bajaj KYC Coborrower enhancement and renewal
**Status:** Not started | **Last edited:** June 5, 2024 1:29 PM

**Problem:**
are we solving?**

1. Currently users with joint holdings can not do KYC.
2. Customer with Bajaj lender will not be able to enhance or renew their line. 

---

**Solution:**
?**

---

## #36 — Increase Credit Utilization via Whatsapp Drips
**Status:** In progress | **Last edited:** June 3, 2024 1:31 PM

**Problem:**
are we solving?**

- Increase the utilization of allocated credit lines among users.
- Boost AUM/principal outstanding without aggressive promotion or breaching partnership agreements.
- Enhance user engagement and retention through personalized communication.

---

**Solution:**
?**

---

## #37 — Unlock credit limit revamp
**Status:** Not started | **Last edited:** June 24, 2024 10:53 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #38 — DSP UPI Autopay Integration for PhonePe
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

## #39 — PhonePe KFS & Agreement
**Status:** In progress | **Last edited:** June 13, 2025 11:10 AM

**Problem:**
are we solving?**

In PhonePe’s integration with DSP, they are looking to fetch the KFS & Agreement PDF from DSP and get the customer consent on their UI. The consent will then be passed to DSP via API.

We need to solve the below challenges.

- Build a flow that’s different from current integrated KFS & Agreement flow
- Capture consent for KFS & Agreement
- Build the backend flow that captures the consent and triggers the agreement counter-signing and stamping workflow

---

**Solution:**
?**

---

## #40 — B2B Zype integration FE and SDK callbacks
**Status:** Not started | **Last edited:** June 12, 2024 3:23 PM

**Problem:**
are we solving?**

1. Zype integration requires changes on the FE side. 
2. They also require a number of SDK callbacks

Following PRD covers these requirements.

---

**Solution:**
?**

---

## #41 — [Jupiter] Unlock credit limit page changes
**Status:** Not started | **Last edited:** July 31, 2024 5:41 PM

**Problem:**
are we solving?**

Change copies on the verify interest and charges page for partners with MFC fetch. 

---

**Solution:**
?**

---

## #42 — [B2B2C] Fixed deposits via partner dashboard
**Status:** Pending Review | **Last edited:** January 8, 2026 4:23 PM

**Problem:**
are we solving?**

---

- Volt is looking to improve partner engagement by helping partners monetise their existing clients better and sell multiple financial products through one platform. Adding Fixed Deposits (FDs) as a product offering allows partners to offer a popular, high-value product along with loans.
- The objective of this initiative is to integrate FD booking and servicing into the existing Volt Partner Dashboard, leveraging Fixxera for the booking journey while providing partners with a unified interface to initiate, track, and manage FD applications.

**Solution:**
?**

---

## #43 — Reduce Phonepe Drop-offs
**Status:** Done | **Last edited:** January 7, 2025 2:01 PM

**Problem:**
are we solving?**

1. Users coming from PhonePe who are eligible for loans are experiencing a 40% drop-off after the MFC fetch step.
2. The on-screen text (copies) is irrelevant, causing confusion and leading to user drop-offs during the journey.

---

**Solution:**
?**

**Note:** This document is iterative and will be updated in phases until the goal is achieved.

---

## #44 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #45 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #46 — B2B Platform Dashboard v1
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

## #47 — TCL EOD Status Check Integration
**Status:** In progress | **Last edited:** February 4, 2025 2:21 PM

# TCL EOD Status Check Integration ## 1. Overview Integration of TCL's EOD status check API to prevent transaction processing during EOD window and avoid backdated transactions posting. Sample Adhoc charge posting API and request: ```json https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/adhocCharges with body [ { "Amount": "200", "ChargesSID": "5", "Date": "2025-01-28", "LoanAccountName": "Avinash Goutam", "LoanContractNo": "41211", "Narration": "Stamping Charges", "Type": "charges", "UniqueRecordID": "1881575495221406782", "UserName": "adminiaf" } , { "Amount": "799", "ChargesSID": "3", "Date": "2025-01-28", "LoanAccountName": "Avinash Goutam", "LoanContractNo": "41211", "Narration": "Processing Fee", "Type": "charges", "UniqueRecordID": "2630159110274265629", "UserName": "adminiaf" } ] ``` ## 2. API Details [https://docs.google.com/spreadsheets/d/18RGjvVKQBvT9UHgKA_Vagjy_1b14LA9f8b3dBwAK5Uk/edit?usp=sharing](https://docs.google.com/spreadsheets/d/18RGjvVKQBvT9UHgKA_Vagjy_1b14LA9f8b3dBwAK5Uk/edit?usp=sharing) ### 2.1 Base Information - **API Purpose**: Check EOD process status in TCL LMS - **Endpoint**: `/miles/EodStatus` - **Base URL**: `https://miles-uat-apicast.apps.tclprdservices.tatacapital.com:443/rest/v1.0` - **Method**: POST ### 2.2 Request Parameters ```json { "SOURCE_NAME": "Miles" // Mandatory, String(10) } ``` ### 2.3 Response States 1. EOD Not Started ```json { "retStatus": "SUCCESS", "response": [], "sysErrorMessage": "", "errorMessage": "", "sysErrorCode": "" } ``` 1. EOD In Progress ```json { "retStatus": "SUCCESS", "response": [{ "EODDate": "2024-10-19 00:00:00", "Remarks": "EOD is in Progress" }] } ``` ## 3. Business Rules ### 3.1 API Execution Rules - Start checking EOD status after 7:00 PM daily - Implement polling mechanism with intervals: - Every 15 min till 11:00 PM ### 3.2 Status-based Actions | Status | System Behavior | Next Action | Impact | | --- | --- | --- | --- | | Null/Not Started | Continue normal operations | Use current system date | No impact | | In Progress | Pause charge posting API calls and queue the request | Poll status at defined intervals | Credit opening TAT | | Completed | Resume all operations | Use current date + 1 when posting adhoc charge | No impact | | 400/500 or any other error | Pause charge posting API calls and queue the request | Queue the request and process when we get completed status and if we do not get completed status till 11 PM, then process queued request after 12 AM with current date | Credit opening TAT | ### 3.3 State Machine ```mermaid stateDiagram-v2 [*] --> CheckEOD: After 7 PM CheckEOD --> NotStarted: Status Null CheckEOD --> InProgress: Status In Progress CheckEOD --> Completed: Status Completed NotStarted --> NormalOps: Continue Current Date InProgress --> PauseOps: Queue charge posting APIs PauseOps --> PollingState: Wait 15 min PollingState --> CheckEOD Completed --> NextDayOps: Use Current Date + 1 ``` ##

---

## #48 — PhonePe PG Implementation
**Status:** Not started | **Last edited:** February 28, 2025 3:28 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

Authorisation:

This is used to authorise the subsequent API calls between the Merchant & PhonePe backend.

- **Request Headers**
    
    
    | **Header Name** | **Header Value** |
    | --- | --- |
    | `*Content-Type*` | application/x-www-form-urlencoded |
- Request Parameters
    
    
    | **Parameter Name** | **Description** |
    | --- | --- |
    | `*client_id*` | Client ID shared by PhonePe |
    | `*client_version*` | In case of **UAT**, client_version value should be 1.In case of **PROD**, use the value as received in credentials email. |
    | `*client_secret*` | Client secret shared by PhonePe |
    | `*grant_type*` | Value will be “client_credentials” |
- Request Body
    
    ```json
    {
    "client_id": "<your_client_id>",
    "client_version": 1,
    "client_secr

---

## #49 — B2B2C RM Flows
**Status:** In progress | **Last edited:** February 25, 2025 5:07 PM

# B2B2C RM Flows Problem statements - Agents have no context on the Incoming calls as they only see the Mobile number - There is no place to Use this mobile number to see the details of the MFD calling and past context - If the MFD has a chat with other RM then i can’t see there messages - Disposition forms in the RUNO and Zendesk are not MECE for the need of RMs - Tech Tickets status don’t get auto updated - RM have to remember to follow up with MFDs, they don’t have a workflow requiring it - [tech issues ](B2B2C%20RM%20Flows/tech%20issues%201a5e8d3af13a8016b001f22540049447.md)

---

## #50 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #51 — Attribution for Jupiter
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to create a BRE which will allow Jupiter platform to create customer even if customer account exist.

---

**Solution:**
?**

---

## #52 — Bajaj PG
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

## #53 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #54 — Handle excess amount in foreclosure request [TCL]
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

## #55 — Handle physical mandate cases for BAJAJ
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

When a physical mandate is required, the document step is not automatically added to the flow. Instead, ops/sales are required to use the admin action to add the document step to show, download and upload physical mandate form.

- Currently we have “Approve mandate” admin action which allow ops/sales user to skip the e-mandate step.
- We have another admin action “Enable document step” which allow ops/sales user to add document step in journey.
- Now, when customer are required to do the physical mandate, ops need to use two admin action to skip e-mandate and add document st

**Solution:**
?**

Provide single admin action which enables ops to skip the e-mandate and add document step using single admin action.

**Context:**

Admin action: Enable document step

- Document upload step gets added

Admin action: Approve mandate

- RM/OPS use this action in two cases
    - When user are required to do physical mandate
    - Mandate is completed but call back didn’t received.
- Problem With above admin action
    - E-mandate marked as approved and document upload step doesn't come when they do not use Enable document.
    - Sales user has to use two admin action to skip digital mandate and add document upload flow.

**Solution:**

- Change current admin action name: From “Approve mandate” to “Approve or skip e-mandate”
- Provide toggle button to add document step
    - When toggle 

---

## #56 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #57 — Interest feature handling for TCL
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

## #58 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #59 — Revocation MIS - TCL customer
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

## #60 — TCL Dynamic repayment schedule
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

To meet compliance requirements, we need to introduce a new functionality that enables TCL customers to download their repayment schedule directly from the app.

---

**Solution:**
?**

We will implement a dynamic repayment schedule generation and download feature that integrates with TCL's API to provide customers with up-to-date repayment schedules.

**Implementation Strategy:**

- **Phase 1**: Direct UI download with real-time API integration
- **Phase 2**: Email delivery option based on API performance analysis

---

## #61 — TCL foreclosure API integration
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

## #62 — B2B2C DSP ops handling
**Status:** Not started | **Last edited:** February 17, 2025 12:47 PM

# B2B2C DSP ops handling Problems 1. Sales team raise a ticket to Volt ops , Volt ops send the cases to DSP over E-Mail. 2. Sales team do select the lender 3. What is the FRT form the DSP ops 4. What is the TAT end to end. 5. Volt ops use Zendesk and DSP ops use ZOHO 6.

---

## #63 — Update user details (for TCL, BFL, DSP)
**Status:** In progress | **Last edited:** December 31, 2024 1:18 PM

**Problem:**
are we solving?**

---

Users have no option to update their phone, email, bank account & mandate details on our app after completing the loan application

**Solution:**
?**

---

- User details need to be updated
    - The user details implementation will be picked up in 2 phases. Following is the phase-wise plan
    
    | Lender | Email  | Phone  | Bank & Mandate |
    | --- | --- | --- | --- |
    | BFL  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
    | TCL  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
    | DSP  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
- High level handling of update details
    - BFL
        
        
        | User detail  | Handling |
        | --- | --- |
        | Email  | - collate all the details update requests
        - Mail daily report to BFL [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) keeping [shrineel.kakade1@bajajfinserv.in](mailto:shrineel.kakad

---

## #64 — [B2B2C] Improving lead quality in partner journey
**Status:** In progress | **Last edited:** December 29, 2025 2:56 PM

**Problem:**
are we solving?**

---

- A large volume of junk leads are entering the **partner journey funnel**, primarily contributed by customers mistakenly starting the partner flow. As a result, the **sales team spends significant time manually validating ARNs on AMFII** and calling these users to verify details — consuming bandwidth that could otherwise be used for genuine partner outreach. This noise severely impacts sales efficiency and delays engagement with actual, high-quality partners.

**Solution:**
?**

---

- **Analysis**
    - From a retrospective analysis of the ARNs and the name match scores between the ARN name and partner entered name in the dashboard, following were the insights -
        
        ![Screenshot 2025-10-13 at 10.12.16 AM.png](%5BB2B2C%5D%20Improving%20lead%20quality%20in%20partner%20journey/Screenshot_2025-10-13_at_10.12.16_AM.png)
        
        - Partners with valid ARNs and name match scores >50% generated 7x more business (average applications per partner) than those with invalid ARNs.
        - Within the valid ARN group, higher name match scores correlated strongly with higher business activity (avg. # of applications per partner)
        - To improve sales efficiency, our goal is to ensure that the sales team receives only validated and ranked leads, mi

---

## #65 — B2B Zype integration webhook
**Status:** Not started | **Last edited:** August 12, 2024 8:25 PM

**Problem:**
are we solving?**

In addition to current webhooks, create another webhook for partner platforms to get an understanding of when was withdrawal initiated by a user on their platform. 

**Note:** While this requirement was raised by zype this webhook will be created for the complete SDK, any partner can choose to consume it. 

---

**Solution:**
?**

---

## #66 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #67 — Bajaj KYC Pod Requirements
**Status:** Not started | **Last edited:** April 4, 2024 1:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #68 — B2B2C call incoming reduction
**Status:** In progress | **Last edited:** April 17, 2025 11:41 AM

# B2B2C call incoming reduction [Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md) [](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md) # Detailed Breakdown of Customer Call Issues ## Loan Application Issues - **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval. - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times. - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."* - The withdrawal interface appears to lack clear instructions for first-time users. - **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process. - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."* - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs. - **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations. - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."* - The fee structure appears to be disclosed incompletely during the application process. - **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements. - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."* - The eligibility criteria seem inconsistently communicated across different channels. - **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process. - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."* - These timeouts appear to occur most frequently during document upload or verification steps. Payment Processing Issues - **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments. - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."* - These delays severely

---

## #69 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #70 — PhonePe requirements
**Status:** Done | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #71 — B2B Theme issues
**Status:** Not started | **Last edited:** Unknown

# B2B Theme issues Charter: Design Initiatives ![image.png](B2B%20Theme%20issues/image.png) ![image.png](B2B%20Theme%20issues/image%201.png) ![image.png](B2B%20Theme%20issues/image%202.png) ![image.png](B2B%20Theme%20issues/image%203.png) Screen recording link: https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1184224081308?sessionReplayId=128b9366-93bd-4630-9872-8f471fdcc59a/1749276669544&sessionStartTime=1749276669543 1. NEED HELP button is not themed properly, Primary Back ground surface color is not looking good. 2. Home icon is blue when it should be in primary color. 3. Profile icon color is also blue? 4. Updating benefits for you section icons 5. Can we check the redendering of font in SDKs Why is Popping in serif? 6. Primary button color changes when user comes to increase limit screen.

---

## #72 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #73 — BRD Interest Refund via Credit Note - OD - V2
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Refund of interest already posted and/or collected
- Refund processed only via Credit Note (Interest type)
- Support for partial and full interest refunds
- Integrated accounting and LMS impact
- Duplicate refund control with necessary dedupe validations

# BRD: Interest Refund via Credit Note - OD - V2 Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ## 1. Background & Objective Interest is periodically accrued, posted, and collected from users as part of the OD loan lifecycle and recognized as interest income in the accounting system. In certain business scenarios (pricing corrections, excess collection, grievance redressal, operational errors, etc.), a portion of already posted and/or collected interest may need to be refunded to the user. The objective of this document is to define a **system-driven, auditable mechanism** to process interest refunds via Credit Note with correct accounting treatment. The solution must ensure: - Accurate reversal of interest income in P&L - Correct user-level balance adjustment - Elimination of manual accounting interventions - Full audit traceability --- ## 2. Scope ### In Scope - Refund of interest already posted and/or collected - Refund processed only via Credit Note (Interest type) - Support for partial and full interest refunds - Integrated accounting and LMS impact - Duplicate refund control with necessary dedupe validations ### Out of Scope - Interest waiver before posting --- ## 3. Key Definitions | Term | Definition | | --- | --- | | Interest Refund | Reversal of interest already posted and/or collected | | Credit Note (Interest) | LMS transaction representing interest refund | | Interest Income Reversal A/c | Contra-income GL used to reverse recognised interest revenue | --- ## 4. Accounting Principles Interest refunds will follow a **single-step integrated accounting construct**. At the time of Credit Note processing: - User balance adjustment and income reversal will occur simultaneously - No intermediate liability or clearing account will be created - P&L impact will be immediate This ensures: - LMS reflects user truth - Accounting reflects financial truth - Reduced reconciliation complexity - No deferred clearing entries --- ## 5. Accounting Treatment ### 5.1 Interest Refund – Credit Note Issued At the time of processing Credit Note (Interest Refund): | Account | Debit | Credit | Account Type | | --- | --- | --- | --- | | Interest Income Reversal A/c | Refund Amount | | Contra Income | | User Interest / Excess / Principal (as applicable) | | Refund Amount | Asset / Liability | --- ### Impact - User outstanding reduces (or excess ledger adjusted) - Interest income reversed immediately in P&L - No clearing

---

## #74 — BRD Interest Refund via Credit Note - OD
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Refund of interest already posted and/or collected
- Refund processed only via **Credit Note**
- Accounting treatment for:
    - Interest income reversal
    
- Support for partial and full interest refunds

# BRD: Interest Refund via Credit Note - OD Last Edited: March 19, 2026 9:44 PM --- ## 1. Background & Objective Interest is periodically accrued, posted, and collected from users as part of the loan lifecycle and recognized as **interest income** in the accounting system. In specific business scenarios, a portion of **already posted and/or collected interest** may need to be reversed and refunded to the user. Currently, interest refunds are handled manually or via ad-hoc adjustments, which introduces: - Accounting inconsistencies - Limited audit traceability - Operational risk at scale ### Objective Define a **system-driven, auditable** mechanism to refund interest via **Credit Note**, ensuring: - Correct P&L reversal of interest income - Correct user balance adjustment - Alignment with existing Credit Note & Waiver accounting patterns --- ## 2. Scope ### In Scope - Refund of interest already posted and/or collected - Refund processed only via **Credit Note** - Accounting treatment for: - Interest income reversal - Support for partial and full interest refunds ### Out of Scope - Interest waiver before posting --- ## 3. Key Definitions | Term | Definition | | --- | --- | | Interest Refund | Reversal of interest already posted and/or collected | | Credit Note (Interest) | LMS transaction representing interest refund | | Intermittent Liability A/c | Temporary clearing account for refund settlement | | Interest Income Reversal A/c | Contra-income account to reverse interest revenue | --- ## 4. Accounting Principles The interest refund follows the **same two-step accounting construct** used for charge refunds: 1. User-level adjustment via **Credit Note** 2. Income reversal via **accounting journal** This ensures: - LMS reflects user truth - Accounting reflects financial truth - Refund execution remains decoupled from income correction --- ## 5. Accounting Scenarios ### 5.1 Interest Refund – Interest Collected (Credit Note Issued) ### Step 1: LMS Transaction – Credit Note (Interest) Creates a refund obligation without impacting income directly. | Account | Debit | Credit | Account Type | | --- | --- | --- | --- | | Intermittent Liability A/c | Interest Amount | | Liability | | As per apportionment of the credit note (independent of charge/interest waiver | | Principal/interest/Charge/Excess | Asset / Liability | **Impact** - User balance reduced - No P&L impact at this stage - Refund liability created --- ### Step 2: Accounting Journal – Interest Income & GST Reversal | Account

---

## #75 — Credit note PRD
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?**

Today, waiving or refunding charges for a user is manual, operationally intensive, and people-dependent process. This introduces friction across internal teams and impacts customer experience. The key issues we’re addressing include:

---

**Solution:**
?**

We will be creating a new payment type called “CREDIT_NOTE” this repayment will not have a corresponding money transaction associated with it. Operations team will use the payment type to identify the transactions and accordingly handle in reconciliation.

The first use case that we will be covering will be the refunds of adhoc charges placed by the NBFC:

- Processing fees
- Margin pledge charges
- Dishonour fees`

---

## #76 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #77 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #78 — Product Note Interest Refund via Credit Note
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, e

# Product Note: Interest Refund via Credit Note Last Edited: January 23, 2026 8:15 PM PRD ETA: July 22, 2025 PRD Owner: Vaibhav Arora ## Background and Context **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged or goodwill interest waivers - Operations team processing interest refunds/waivers - Finance team managing manual accounting entries for interest reversals - Tech ops/Product handling backend interventions for interest adjustments **What is the challenge that they are facing? What is broken today?** - Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access - Process is operationally intensive with dependency on Jira ticket workflows - No standardized maker-checker workflow for interest refunds similar to charge refunds - Manual JV posting for interest reversals creates additional overhead for Finance team - Lengthy resolution time (2-3 days) impacting customer experience - No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period - Lack of visibility and tracking for interest refund requests across the loan lifecycle **Why is it important? What is getting impacted?** - Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests - Operational inefficiency with high manual effort required for each interest refund case - Risk of errors and duplicate processing without systematic validations - Finance team bandwidth consumed by repetitive manual JV entries - Lack of audit trail and reconciliation capabilities for interest reversals - Inconsistent treatment of interest refunds compared to the now-standardised charge refund process --- ## 1. Problem Scope ### In scope **What specific problems are we solving?** 1. **Slow Resolution Time:** - Interest refund requests take 2-3 days to resolve from initiation to completion - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product 2. **Operational Bottleneck and Dependency:** - Operations teams cannot independently process interest refunds or waivers - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention - Backend access and API calls are needed for what should be a routine operational task - Process creates unnecessary dependencies across multiple teams for resolution 3. **Risk of Duplicate Processing:** - No systematic validation exists to check if interest for a specific period has already been waived or refunded - Product team rely

---

## #79 — Product note Credit note for TL
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

We are solving:

# Product note: Credit note for TL Last Edited: April 28, 2026 4:45 PM PRD ETA: April 17, 2026 PRD Owner: Vaibhav Arora # **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)** --- ## **Background and Context** **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged interest - Operations team handling refund/waiver requests - Finance team managing manual income reversals and reconciliation - Product/Tech teams currently intervening via backend/API --- **What is the challenge today?** - Interest refunds require **manual intervention via engineering or Finflux access** - No standardized **maker-checker workflow** - **Not supported for Term loans, currently productised and implemented only for OD** - Manual JV posting required for income reversal - No **system-driven dedupe or validation** - No **tranche-level visibility or audit tracking** - Turnaround time is **2–3 days**, impacting CX --- **Why is it important?** - Poor customer experience due to delays - High operational dependency and inefficiency - Risk of duplicate or incorrect refunds - Manual accounting overhead for finance - Lack of audit trail and reconciliation visibility --- ## **1. Problem Scope** ### **In Scope** We are solving: ### **1. Operational Independence** - Enable Ops to process **interest refunds without engineering dependency for Term loans** - Introduce **maker-checker workflow** --- ### **2. Standardized Accounting** - Eliminate manual JV posting - Introduce **credit note + automated income reversal** --- ### **3. Tranche-Level Refund Handling** - Refunds applied at **tranche level (not line level)** - Excess created is: - Initially **tranche-tagged** - **Not usable across tranches while tranche is active** - Becomes **line-level usable only after tranche closure** --- ### **4. Validation & Dedupe** - Prevent duplicate refunds via: - Schedule validation - Credit note existence checks --- ### **5. Audit & Traceability** - Full linkage: - Interest → Credit Note → JV - Tranche-level enrichment and reporting --- ### **Out of Scope** - Principal refunds - Bulk refund processing - Automated eligibility rules - Reversal of incorrect refunds (no reversal flow) --- ## **2. Success Criteria** ### **Outcomes** - Maker → Checker → Accounting completion within **1 hour** - **>90% reduction** in Jira dependency - Capability to refund interest for Term Loan - **Zero duplicate refunds** at tranche-month level --- ### **Post-launch Good State** - All refunds processed via maker-checker - Credit notes posted correctly at tranche level - Automated JV posted for income reversal - Finance can reconcile via

---

## #80 — tech issues
**Status:** Unknown | **Last edited:** Unknown

# tech issues ## ### KYC & Authentication Issues 1. **KYC verification process fails with no clear error messaging** - Example (VTS-9511): "AKGPV3060R - Not able to move forward in kyc step" - Customer was stuck during verification with no indication of what went wrong or how to proceed. - Example (VTS-9981): "Stuck in kyc summary" - Process halted after completing verification with no error details provided to the customer. 2. **Digilocker integration failures during KYC verification** - Example (VTS-9770): "9415307644 - VIKAS KUMAR - KYC issue with digilocker's end" - API connection to Digilocker failing, preventing document verification. - Example (VTS-9964): "Discrepancies in CKYC record associated with the KYC Identifier: 50072772797161" - Records in Digilocker not matching with application data. 3. **Unusual KYC errors without diagnostic information** - Example (VTS-9711): "Unusual KYC Error" - Generic error message without actionable details for troubleshooting. - Example (VTS-10138): "CFCPS2351M - Facing error on KYC Page" - Customer encountered undefined error with no clear next steps. ### Pledging Process Failures 1. **KFin OTP delivery system failures** - Example (VTS-10085): "8928846293 - ATUL TIWARI - not getting otp at pledging for kfintech" - Customer attempted multiple times from web and app but never received OTP. - Example (VTS-10227): "8884052766 - DINESH KUMAR INALA - Kfintech pledging OTP issue" - System-wide failure in OTP delivery when pledging through KFin. 2. **Pledging failure despite eligibility** - Example (VTS-9396): "EQSPK8350P - KFin Pledging error" - "Fund is in approved list of TATA and is also visible when we did 15sec eligibility check" but still failing. - Example (VTS-9358): "DIWPP4809P - Unable to pledge Kfin funds" - Eligible funds appearing in portfolio but pledge transaction failing. 3. **Funds pledged but not lodged in system** - Example (VTS-9884): "Lodgment issue -ANNPS4596F" - "One of the pledged funds of the above client is not lodged in the system yet". - Example (VTS-10044): "BEPPB3956Q, Units pledged but lodgment not done" - Pledge transaction completed but credit not applied to account. ### API Integration Failures 1. **Timeouts in partner integrations** - Example (VTS-9597): "Frequent API Timeout Issues" - FundsIndia experiencing frequent API timeouts, preventing operations completion. - Example (VTS-9529): "Assistance Required: User Facing PAN Mobile Number Error in SDK" - API timeout causing user verification failures. 2. **Document API failures** - Example (VTS-9346): "Volt - Documents are Missing" - "I checked the webtops and I am unbale to find. Requesting you to

---

## #81 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #82 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #83 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #84 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #85 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #86 — SDK
**Status:** Unknown | **Last edited:** Unknown

# SDK - JS sdk - IOS sdk - Android SDK - RN sdk - partner mobile APP, web , PLJ - Iframe - webhook for partner , v-kyc done or not to partners - API exposed, Get application status , KYC done , bifurcation -

---

## #87 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #88 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #89 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #90 — Repeat B2B2C
**Status:** Unknown | **Last edited:** Unknown

# Repeat B2B2C MFD Activation Journey Field Update & Lead Schema Integration ### **Purpose:** To define and manage the set of fields that must be updated post-MFD activation journey completion and ensure these updates are shared with the lead schema for downstream processing by the Repeat team. ### **Scope:** - Capturing required data fields. - Defining when and how these fields are updated. - Updating the lead schema with the captured data. - Triggering opportunity closure upon journey completion. **The following fields need to be replicated in the lead schema:"** 1. MFD Name 2. MFD Phone Number 3. MFD Employee Name 4. MFD AUM 5. MFD ARN 6. MFD Email 7. MFD Activation Date 8. MFD Origin 9. MFD Partner Referral Link 10. MFD Customer Referral Link 11. Referred By 12. Referrer Name 13. Referrer Phone 14. Partner Account ID Additionally, include the list of customers referred so far. 1. All the customer-referred activity must be populated in the lead once activated. **In conclusion, the repeat team can work completely on the lead level, and the MFD activation team can work on the opportunity level** The activities that must be polluted in the lead fields are as follows: 1. Daily partner details update 2. Customer referred 3. Customer loan created

---

## #91 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #92 — Analytics Requirement Name verification (TCL)
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Name verification (TCL) Query 1: (errors consolidation, distributed by providor) Total applications initiated (unique) Total Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #93 — PhonePe UPI Autopay Evaluation
**Status:** Unknown | **Last edited:** Unknown

# PhonePe UPI Autopay Evaluation API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization) **List of APIs** 1. Authorization API 1. This API is used to generate the auth token to access the rest of the APIs. 2. The auth token is valid for 1 hour. 3. If the auth token is re-generated within 1 hour, the old token will not expire. - Request ```json curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'client_id=' \ --data-urlencode 'client_version=1' \ --data-urlencode 'client_secret=' \ --data-urlencode 'grant_type=' ``` - Response ```json { "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "expires_in": 3600, "issued_at": 1738669002, "expires_at": 1738672602, "session_expires_at": 1738672602, "token_type": "O-Bearer" } ``` 1. Validate VPA API 1. This API is used to validate the user's VPA. 2. Returns, valid & name of the user. 3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts. - Request ```json { "type": "VPA", "vpa": "nihaltest1@ybl" } ``` - Response ```json { "valid": true, "name": "<Name of User>" } ``` 1. Intent 1. This API is used to create the intent link for autopay. 2. amount - this parameter defines the amount to be deducted at the time of registration. 3. maxAmount - this amount defines the maximum amount the mandate is registering for. 4. Android - Generic intent URI will be provided. 5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app. - Request ```json { "merchantOrderId": "MOTEST5", "amount": 300, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST5", "authWorkflowType": "TRANSACTION", "amountType": "FIXED", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_INTENT", "targetApp": "com.phonepe.app" } }, "deviceContext" : { "deviceOS" : "ANDROID" } } ``` - Response ```json { "orderId": "OMO2502041725138147510236", "state": "PENDING", "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738" } ``` 1. Collect 1. This API is used to send the collect request for mandate setup. 2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported. - Request Body ```json { "merchantOrderId": "MOTEST6", "amount": 200, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST6", "authWorkflowType": "TRANSACTION", "amountType": "VARIABLE", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_COLLECT", "details": { "type": "VPA", "vpa": "nihaltest1@ybl" } } } } ``` - Response ```json { "orderId": "OMO2502041727154877510267", "state": "PENDING" } ``` 1.

---

## #94 — Bajaj signature was not generating and user was ke
**Status:** In progress | **Last edited:** Unknown

# Bajaj signature was not generating and user was kept in a waiting state Classification: Bajaj agreement link generation Notes: Bajaj callback API for agreement link PRD/Solution mapping: In Progress Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13058 Status: In progress

---

## #95 — NBFC B2B LSP API List
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : API List - Pledge API on DSP - pending - Fetch API on DSP - pending - Submit opportunity - create account - Mobile & Email update - no verification - Add verification timestamp for mobile & email - KFS & Agreement: we might have to decouple and make KFS pass the response in parameters - Offer API on DSP - LSP passes back the confirmation to DSP - PAN verification - LSP not required to integrate -

---

## #96 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #97 — NBFC LSP Stack GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC LSP Stack : GTM Below are the GTM phases of the LSP stack. | Phase | Objective | Partner/s | Number of applications | Timeframe | | --- | --- | --- | --- | --- | | Phase 1 | To augment the existing DSP capabilities into APIs to validate the stack a small scale | 1-2 | 100/day | 30 days | | Phase 2 | To build fall-back capabilities for each part of the journey to handle scale | 3-4 | 500/day | Ongoing | | Phase 3 | To build term loan capabilities over and above the current offerings for newer partners | | | TBD | | | | | | |

---

## #98 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are