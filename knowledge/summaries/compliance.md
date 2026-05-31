# Current State: Compliance

> Auto-generated from 140 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — NBFC Bureau Reporting
**Status:** Not started | **Last edited:** September 6, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #2 — PRD - Mandate conversion optimisation via swap in
**Status:** Not started | **Last edited:** September 3, 2025 2:24 PM

**Problem:**
are we solving?**

Currently, the user journey follows **Bank Account Verification → Mandate Setup → Pledge**.

- Users feel hesitant about setting up a **bank mandate before pledging assets**.
- This results in drop-offs at the mandate step, as the user hasn’t yet committed to taking a loan.
- Additionally, mandates are sometimes created for users who **never pledge**, leading to wasted effort, operational overhead, and potential regulatory friction.

We want to reverse the sequence to **Pledge → Bank Verification → Mandate**, so the mandate is only triggered once the user has committed by pl

**Solution:**
?**

Reorder the loan journey flow as follows:

1. **Pledge** (user commits MF units as collateral).
2. **Bank Verification** (fetch & confirm repayment account with penny drop).
3. **Mandate Setup** (NACH/e-mandate/UPI Autopay).

This ensures only committed users proceed to mandate, improving mandate conversion and reducing unused mandates.

---

## #3 — PRD - Handling MF Central CAS Summary API fields r
**Status:** Not started | **Last edited:** September 29, 2025 12:15 PM

**Problem:**
are we solving?**

MF Central (MFC) is deprecating certain user attributes in its CAS Summary API response, the major ones are namely-

- Available units
- Email
- Bank Account Details
- DoB
- Age

Currently, Volt Money relies on some of these fields like Bank account details for showing total portfolio value in check eligibility and pre-filling user details during loan journeys. If these fields are no longer available:

- Our loan application funnel will face friction due to lack of prefilled data.
- Users may need to manually enter information they previously didn’t, leading to drop-offs.
- 

**Solution:**
?**

---

## #4 — TATA compliance requirement - 30th August 2024
**Status:** In progress | **Last edited:** September 19, 2024 4:06 PM

**Problem:**
are we solving?**

Compliance issue for TATA

---

**Solution:**
?**

---

## #5 — BAJAJ Dedupe API
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

## #6 — DSP Website
**Status:** In progress | **Last edited:** October 8, 2024 7:17 PM

**Problem:**
are we solving?**

As a regulated entity, DSP needs to have a website in its name with basic details. This is required from a regulatory  perspective to disclose key policies, procedures, etc.

In addition, certain borrowers also research the lender they have taken a loan from and would want to reach out for any concern or query.

---

**Solution:**
?**

---

## #7 — Master collections PRD (NBFC)
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

## #8 — TATA KFS and Agreement Phase 2
**Status:** In progress | **Last edited:** October 24, 2024 10:46 AM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge.

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

## #10 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

**Solution:**
?**

---

## #11 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #12 — Lodgement decoupling from enhancement
**Status:** Ready for Tech | **Last edited:** November 6, 2024 10:33 AM

**Problem:**
are we solving?**

Users when performing line enhancement journeys often complete pledging of their securities but do not complete the application by signing the agreement.

Current flow lodges the securities post agreement completion for the user which leaves the securities in dangling state (pledged but not lodged) for the lender. RBI regulation dictates the REs to unpledge all unlinked/unlodged securities after 30 days of pledging if they are not lodged.

This problem increases operational overload for our ops team and lender and impacts customer experience since they now have to wait for t

**Solution:**
?**

Decoupling lodgement from agreement signature in case of line enhancement. 

Margin pledge:

Case where agreement signature is not required due to low amount of pledging not enough for increase in SL:

Lodge securities post pledging as is

Line enhancement:

Cases where SL needs to be updated to increase the limit for the user against the pledged securities:

Lodge securities post pledging, and generate agreement with the updated SL. Save updated SL post agreement signature. 

- Customer will not see updated SL even if their securities are lodged but SL is not updated:
Same as current flow, user should see the updated available limit till the agreement is signed against the application.

- Customer will keep on seeing the old agreement and will not be able to raise another enhancement

---

## #13 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #14 — Father’s name validation removal
**Status:** Not started | **Last edited:** November 30, 2025 12:18 PM

**Problem:**
are we solving?**

LSPs are currently seeing high rejection rates at the **Submit Opportunity** stage due to mismatches between the user-entered *father’s name* and the value returned from KYC.

Since the RBI’s KYC Master Directions do **not** mandate verification of the father’s name—and it is required only for CKYC reporting—strict validation is unnecessary. Most regulated entities rely on customer-provided details with minimal checks, which aligns with our revised approach.

---

**Solution:**
?**

---

## #15 — TCL Credit Referral Automations & optimisations
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

## #16 — TATA Dedupe API with updated BRE
**Status:** Pending Review | **Last edited:** November 21, 2024 12:42 PM

**Problem:**
are we solving?**

- For users whose lender is assigned as TATA, either via BRE logic or hardcoding, an existing loan account with TATA is only detected after the user has completed the application process.
- This leads to a poor user experience, as the user is required to un-pledge their funds and restart the application process from scratch with a different lender.

---

**Solution:**
?**

We will hit the TATA dedupe APIs that will return if a customer holds an active LAS/LAMF relationship with TATA. 

1. The customer is checked for the partner from whom the application is being received
2. We check the DB if there are any specific lender assigned to the partner (eg. Jupiter and some MFDs)
3. If the customer has only TATA assigned as the lender OR any lender, the rest of the process follows.
4. At the step of lender assigning through BRE - dedupe check will be done using PAN number of the user for both TATA and BFL
5. Whenever there is a lender change from BAJAJ to TATA through admin panel  
6. Posidex check to be done if the customer is dedupe negative (customer has no relationship with TATA)
7. Dedupe will be the first check in the BRE and basis the outcome, the rest 

---

## #17 — New Posidex report template
**Status:** In progress | **Last edited:** November 20, 2024 4:54 PM

**Problem:**
are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

**Solution:**
?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

---

## #18 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #19 — External reporting requirements
**Status:** Done | **Last edited:** November 15, 2024 3:03 PM

**Solution:**
?**

**CKYC update and upload**

We will be integrating with CKYC provider which will help us automate the [process of SFTP upload](CKYC%20Upload%20for%20DSP%201433e0160911411981171e2d7d788b91.md)  for the NBFC. 

**CIC**

We will get Finflux to create a pre-built report for us, which can be converted into TUDF format and directly uploaded to different SFTPs and ST clients of CICs for batch processing

**NeSL:**

We will get Finflux to create a custom report for us, which can be uploaded to NeSL’s website on a weekly and a monthly frequency

(Note: We will create automated emails to Ops, with the reports so that they a respective ticket is created for them to complete the task for V1

We will automate the complete uploading of files to the external agencies in v2 (Post we have confidence i

---

## #20 — KYC Risk Status (NBFC Platform)
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

## #21 — Repayment flow for DSP
**Status:** Pending Review | **Last edited:** November 11, 2024 8:01 PM

**Problem:**
are we solving?**

We offer three payment methods for a user to be able to make a repayment towards their loan via Razorpay:

- UPI
- Debits cards (Rupay)
- Net banking

For net banking, Razorpay assists us with partnering with different banks so that they can offer net banking as a service with our sponsor bank (Yes bank). Currently we are only utilising Razorpay integration as an LSP (via Volt) and do not have a repayment flow on the DSP website. 

To enable large banks like SBI, HDFC, ICICI, IDFC bank, we need to have a repayment flow on the DSP website to meet compliance requirements.

---

**Solution:**
?**

We will build an intermediate repayment flow for users to be able to make a repayment on their loan account on the DSP landing page (to showcase to Banking partners)

---

## #22 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #23 — Custom Comms based for Ad-hoc situations v2
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

## #24 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #25 — [DSP] Additional customer comms (compliance)
**Status:** In progress | **Last edited:** May 28, 2025 12:27 PM

**Problem:**
are we solving?**

Sending additional comms to users to comply with DLG and internal compliance requirements. 

---

**Solution:**
?**

---

## #26 — Phase 0 LTV Tenure Update_LOS
**Status:** Not started | **Last edited:** May 25, 2026 4:26 PM

**Problem:**
are we solving?**

Problem 1: LTV at 45

DSP's LAMF product offers 45% LTV on equity and hybrid funds, compared to 70% LTV offered by banks — making it structurally uncompetitive. This gap limits DSP on three fronts:

- **Existing customers** are under-drawing against already-pledged assets, leaving loan book growth on the table
- **New customers** in lower-ticket segments have sufficient collateral at 70% LTV but fall below viable thresholds at 45%
- **Product parity** with banks cannot be achieved without closing this 25pp LTV gap

Problem 2: Tenure at 3 years

RBI has recently mandated that

**Solution:**
?**

**In scope:**
(Phase 0)

Product

- LTV increase from 45% → 70%
- 6-year tenure migration
- Partner-level LTV configuration
- Updated KFS/Agreement templates

Customer Scope

- New customers
- Existing users still within LOS flow

Platform Scope

- DSP (Fenix)
- LSP integrations
- Volt & its partners

---

## #27 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #28 — STP validation for Bulk Sell off
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

## #29 — Consent Architecture FE requirements
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

## #30 — Dues Comms Updation
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

## #31 — [Platform] Unpledging of unlinked funds bulk appro
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

## #32 — [Platform] Foreclosure handling and enhancement
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

## #33 — Custom Comms based for Ad-hoc situations
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

## #34 — [Platform] Wrapper APIs for RTAs
**Status:** Not started | **Last edited:** March 24, 2025 5:17 PM

**Problem:**
are we solving?**

AMCs are divided between two RTAs CAMS and KFIN, both CAMS and KFIN have a common initiative called MFC. All CAMS, KFIN and MFC have different APIs and corresponding features like:

- Session management
- Error handling
- Encryption/Decryption
- Authorisation

While KFIN has session management and credential based authorisation, CAMS has a signature along with encryption and decryption of requests and response packets.

MFC on the other hand, has session management (via JWT tokens), encryption and decryption along with signatures which makes it very hard for an LSP to integr

**Solution:**
?**

We will be building wrapper V2 APIs for the following workflows:

- Investor consent API (MFC) (OTP generation)
- Get CAS Document API - Summary (MFC)
- Lien status API (KFIN V2)
- Lien status API (CAMS)
- Lien marking API (KFIN V2)
- Lien marking API (CAMS)

We will also be simplifying multiple processes which are to be done to ensure that the integration is seamless for our LSPs:

- MFC token generation and management
- MFC signature generation
- MFC encryption and decryption (Sanitisation of LSP request to MFC encrypted format and response sanitisation in decrypted format to LSP)
- KFIN session management for lien marking and status
- CAMS signature generation for lien marking and status
- CAMS encryption and decryption for lien marking and status

There will be three wrapper APIs 

---

## #35 — Credit Bureau Reporting Comms
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

## #36 — Selfie Link - MFD Prudent PRD
**Status:** Done | **Last edited:** March 19, 2025 1:38 PM

**Problem:**
are we solving?**

- Approximately 2.6% of applications(irrespective of platforms) take more than 5 minutes to complete, while 1% of applicants take more than 30 minutes without even entering the deviation flow. This increases the time required for applicants to complete the loan application.
- For Mutual Fund Distributors (MFDs) or MFD software partners completing applications on behalf of users, the problem lies in the **selfie verification step**, where MFDs often either drop off or capture an image of the user displayed on a mobile screen, leading to potential errors or spoofed images.
- V

**Solution:**
?**

Provide a **shareable link** that MFDs or MFD software partners can use to enable users to complete only the selfie step directly. This ensures that the user is actively involved in the selfie capture, reducing errors and improving image authenticity.

---

## #37 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #38 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #39 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #40 — Product note Co-lending foreclosure - Deprecated -
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

## #41 — MFD Activation Flow in LSQ
**Status:** In progress | **Last edited:** June 30, 2025 11:39 AM

**Problem:**
are we solving?**

Currently, MFD leads entering through multiple channels lack a unified onboarding and activation process. This results in:

- Productivity Loss
    - Data inconsistencies
    - Delayed activation due to low follow up mechanism
    - Fragmented visibility across different channel of leads
- Activation Process currently is adhoc and dependent on the Google sheets for tracking
- Enhance Follow up mechanism

---

---

## #42 — Virtual Accounts for LSPs
**Status:** Pending Review | **Last edited:** June 20, 2025 11:32 AM

**Problem:**
are we solving?**

---

- Currently partner LSPs are looking for an alternate payments methods than the payment like because -
    - They have an existing UI flow ready to support VA accounts (SmallCase)
    - They want to provide a back-up repayment option in case payment link is down

**Solution:**
?**

- DSP will expose APIs that enable each partner LSP to retrieve a virtual account (VA) number uniquely mapped to a customer’s loan account. Instead of embedding the VA generation logic within each LSP’s system, this design centralizes the logic at DSP’s end. As a result, if DSP ever modifies the way VAs are generated—due to regulatory, operational, or technical changes—no updates are required on the LSP side.
- This decouples the VA logic from partner implementations and ensures long-term scalability, consistency, and ease of maintenance across all integrations.
- LSPs will get the status of VA repayment through the repayment order status update web hook

---

## #43 — Margin pledge charges
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

## #44 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #45 — [DSP] NSDL PAN Verification alignment
**Status:** Not started | **Last edited:** June 13, 2025 11:59 AM

**Problem:**
are we solving?**

As per RBI’s KYC guidelines, if as an RE we are obtaining PAN of the customer the same should be verified from the issuing authority (as per point 10(j) of Chapter III in the RBI KYC [Masterdirections](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566)). This means that PAN should be verified via the NSDL PAN verification API. 

![image.png](%5BDSP%5D%20NSDL%20PAN%20Verification%20alignment/image.png)

Currently we are not integrated with the NSDL PAN verification API, which makes us non-compliant. We need to plan and align on how to integrate NSDL PAN verifi

**Solution:**
?**

Understanding of the regulation - 

Where PAN is obtained, the same shall be verified from the verification facility of the issuing authority. 

“Verification facility of the issuing authority” makes it very clear that the PAN obtained should be verified by NDSL. 

We currently obtain PAN of the customer either from Digilocker or get it verified via PAN verification API provided by Signzy

- PAN document obtained from Digilocker is an e-document that NSDL (or UTIITSL) has already cryptographically signed and published. Does obtaining this document suffices the “verification facility of the issuing authority”? This is not clear.
    - Digio mentions that this suffices the compliance requirement.
    - Protean mentions that this does NOT suffice the compliance requirement.
    - Hyperve

---

## #46 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #47 — Making Mobile & Email Verification Log Optional LO
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

## #48 — Product note LMS integration with Tally
**Status:** Ready for Tech | **Last edited:** January 8, 2026 9:27 AM

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- **Manual ERP Posting Dependency**:
    
    Accounting entries are generated in Finflux (LMS) but are **manually transformed and uploaded into Tally**, creating operational dependency on the Finance team.
    
- **High Risk of Errors and Duplicates**:
    
    Manual handlin

# Product note: LMS integration with Tally ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? Most businesses record transactions across multiple ledgers to accurately classify income, expenses, assets, and liabilities arising from each business event such as product sales, and discounts. For us as an NBFC, core business transactions include interest posting, charge application, payouts against sanctioned limits, and customer repayments. Given the regulated nature of lending, NBFC accounting processes are subject to direct regulatory scrutiny by the RBI. It is therefore critical that accounting is accurate, automated, system-driven, and free from manual intervention. Currently, accounting entries are generated in the LMS and then manually transformed and posted into the ERP. This manual handoff introduces operational and control risks. This gap was highlighted as a key vulnerability in our statutory audit and must be addressed as a priority. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users - **Manual ERP Posting Dependency**: Accounting entries are generated in Finflux (LMS) but are **manually transformed and uploaded into Tally**, creating operational dependency on the Finance team. - **High Risk of Errors and Duplicates**: Manual handling increases the risk of: - Duplicate ledger postings - Incorrect ledger mapping - Debit / credit sign errors - Partial or missed uploads **Lack of Idempotency & Control**: There is currently: - No system enforced idempotency for ERP postings - No way to prevent re-posting of the same transaction - Limited ability to trace an LMS transaction to a Tally voucher **Delayed and Unpredictable TAT**: Posting timelines depend on: - Manual availability of the Finance team - Ad-hoc batch preparation and uploads This leads to **inconsistent turnaround times** **Access control**: Current workflows do not consistently enforce: - System-driven approvals - Clear separation between generation, validation, and posting of accounting entries. ### Out of scope - - Call out on items out of scope - Rationale for exclusion - Manual Reconciliation: Reconciliation between LMS (Finflux) and ERP (Tally) is currently manual and time-intensive, requiring cross-system data pulls and comparisons. This will be picked as an enhancement once the current release is stabilised. ETA to be confirmed - Delayed

---

## #49 — [NBFC] DSP Finance Website (Aug25)
**Status:** In progress | **Last edited:** January 7, 2026 6:34 PM

**Problem:**
are we solving?**

DSP Fin website currently meets the basic expectations in terms of content and regulatory requirements. That said, it still doesn’t measure upto competitor websites like BFL, TCL or NBFC websites like Navi, CRED, Piramal, etc. 

Now that we need to do a PR and work with external partners (Banks, rating agencies, etc), we need to polish up the website to ensure it conveys trust and confidence.

The new version would also have a basic customer servicing activities like ability to request for a SOA, disbursement or even do repayment.

---

**Solution:**
?**

---

## #50 — [Platform] Mandate collection BRE optimisation
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

## #51 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #52 — CKYC Upload for DSP
**Status:** In progress | **Last edited:** January 22, 2025 6:39 PM

**Problem:**
are we solving?**

- Manual effort in retrieving and matching data
    - CKYC is a manual process for a lot of banks where KYC records are manually updated and then converted into consumable format by Cersai.
- Prone to errors which might result in borrowers’ records getting updated incorrectly
    - Due to the manual nature of flows, the process is error prone and has an impact on user’s KYC data saved with Cersai (which may be used by other lenders) and may impact user experience
- Upload involves processing/accessing a lot of PII & KYC data of borrowers
    - A lot of PII information and KY

**Solution:**
?**

We will be building a file generator for ops team which will generate the CKYC reporting file (as per the guidelines of RBI) which can be uploaded directly to the SFTP portal by Cersai.

---

## #53 — Shortfall FAQ
**Status:** Not started | **Last edited:** January 21, 2025 8:23 PM

# Shortfall FAQ What is shortfall? Short fall is the when the DP of customer goes below the withdrawn amount. This happens due to Market downfall. LTV SEBI Regulatory LTV As per RBI the Guidelines are the LTV should be 50% DSP Configured LTV we generally keep the LTV 0.45 to keep buffer of 10% for the Market fall There is minimum limit of the Pledging of the 25k

---

## #54 — Repayment next step
**Status:** Not started | **Last edited:** January 17, 2025 12:25 PM

# Repayment next step # Loan Repayment System Redesign ### Current Hypotheses 1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected. 2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. ## JTBD problem list ### Job Story 1: Clear Shortfall "When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall." **Current Problems:** - The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest - Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront - Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts ### Job Story 2: Pay Interest "When I need to pay my interest, I want to understand why I need to pay any additional charges" **Current Problems:** - In TATA, users see interest amounts increase in months with additional charges - The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained - Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments - These charges and interest come under monthly dues as a concept ### Job Story 3: Make Principal Repayment "When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision." **Current Problems:** - For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate. - The principal repayment screen doesn't explain that the payment will first go towards interest and charges - Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users. - Users are not aware that principal is being repaid early and isn’t due for 3 years. ### Job Story 4: Understand Payment Structure "When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system." **Current Problems:** - The home

---

## #55 — [Final] End use capture of transactions
**Status:** Pending Review | **Last edited:** January 15, 2026 5:13 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

- **Capture end use during each withdrawal**
    - **Pros**: Enables granular tracking of the specific purpose behind each withdrawal, offering clear visibility into usage patterns.
    - **Cons**:
        - Complicates the mapping between repayments and disbursements, especially when multiple withdrawals have different declared purposes.
        - Involves higher development effort, as UI changes (e.g., dropdowns on withdrawal screens) would be required.
- **Incorporate tweaks in the end use declaration within the loan agreement [Prioritised]**
    - **Pros**: Minimal engineering effort, as no changes to withdrawal screens are needed.
    - **Cons**: Limits visibility into actual usage at a transaction level, which may reduce data fidelity for downstream analysis or compliance.

---

## #56 — DSP QC Reject Handling in LSQ
**Status:** In progress | **Last edited:** February 27, 2025 7:48 PM

# DSP QC Reject Handling in LSQ # Custom Activity Configuration: DSP QC Rejection ### Problem Statement Currently, when DSP operations team rejects an applicationBased on Risk/compliance reasons, they need customer to Re attempt some step. - That increases Risk of customer application Abandonment - Customer might not see the message based communication - Sales team don’t have the List of applications in QC reject to reach out to Customer over a call and get them to complete the applications ### Success Metrics 1. **Primary Metrics** - Reduction in application abandonment rate post-QC rejection - Decrease in time to resolution for QC issues - Sales team response time to QC rejections 2. **Secondary Metrics** - Increase in first-time-right applications by understanding the Common QC reject issues ## User Personas & Journey ### 1. DSP Ops Team - Reviews loan applications - Identifies risk/compliance issues - Rejects the application on CC - Provides detailed feedback on CC ### 2. Sales Team - Receives QC rejection notifications - Contacts customers for updates - Guides application completion - Updates activity status ### 3. Customer - borrower - Receives rejection notification - Needs to update application - Requires clear guidance - Expects minimal friction ## 1. Activity Setup in LeadSquared Using LeadSquared's Custom Activities & Scores section: ### 1 Basic Configuration - Activity Display Name: DSP_QC_Rejection - Activity Code: 268 - Score: 0 - Show in Activity List: Yes - Delete Activity: Yes ### 1.1 Activity Setup in LeadSquared ```json { "ActivityEventName": "DSP_QC_Rejection", "Code": "268", "Score": 0, "ShowInActivityList": true, "CanDeleteActivity": true } ``` ![Screenshot 2025-02-21 at 4.00.31 PM.png](DSP%20QC%20Reject%20Handling%20in%20LSQ/Screenshot_2025-02-21_at_4.00.31_PM.png) ### 1.2 Custom Fields 1. **Notes Field** - Display Name: Notes - Schema Name: ActivityEvent_Note - Type: String - Purpose: Capture rejection reasons 2. **Status Field** - Display Name: Status - Schema Name: Status - Type: Dropdown - Options: - Pending Review - Customer Contacted - Update Required - Update Received - Resolved 3. **Owner Field** - Display Name: Owner - Schema Name: Owner - Type: User - Purpose: Track responsibility ### 2.1 API Call for Creating Activity ```json POST https://{host}/v2/ProspectActivity.svc/Create { "RelatedProspectId": "[LEAD_ID]", "ActivityEvent": "268", "ActivityNote": "[QC_REJECTION_NOTES]", "Fields": [ { "SchemaName": "Status", "Value": "Pending" }, { "SchemaName": "Owner", "Value": "[ASSIGNED_SALES_REP]" } ] } ``` ### 2.2 Application Logic 1. When QC team rejects application: - Create activity with rejection details - Set initial status as "Pending" - Assign to original sales owner - Return customer

---

## #57 — Product note - DRPS
**Status:** In progress | **Last edited:** February 25, 2026 11:01 AM

**In scope:**
**

- Enable users to **download an updated repayment schedule(on 100% loan)** that reflects:
    - Disbursals
    - Part payments (principal / interest / charges)
    - Interest based on actual utilisation
    - Loan meta data [ROI, Credit limit, Sanction limit, Interest due, Charges due, Principal due, LAN]
    - Should reflect any change in ROI during loan tenure
- Ensure schedule is **regenera

# Product note - DRPS ## **Background and Context** - **Who is facing the problem** - End customers using LAMF with multiple/single disbursals and part repayments - Customer support & operations teams - NBFC has to provide DRPS to borrower due to regulatory requirement. - **What is the challenge today** - Repayment schedules are **static** and was generated at the time of Agreement sign - Any transaction post generation (disbursal, part payment, interest payment) makes the schedule **outdated** - Users rely on SOA or support teams to understand: - Updated interest dues - Final maturity amount - Remaining principal and cash flow expectations - **Why this is important** - LAMF is a **dynamic credit line**, not a fixed EMI loan - Mismatch between schedule vs actual dues creates: - User confusion understanding the EMI - A real-time repayment schedule improves **transparency, self-service, and confidence** - **It’s a regulatory requirement to provide dynamic schedule post disbursal and repayment to borrower.** <aside> 💡 **What is Dynamic repayment schedule (DRS/DRPS)** **Dynamic Repayment Schedule (DRS)** is a **continuously recalculated repayment plan** that reflects the **current and actual state of a loan**, instead of a fixed, one-time schedule. Unlike traditional EMI schedules, a DRPS is an **updated document that changes whenever the loan balance is impacted by a transaction**, ensuring alignment with actual utilisation and repayments. *In simple terms:* A Dynamic Repayment Schedule shows **what borrower owe, how it is calculated, and how it changes** — based on everything that has *actually happened* on **borrowers** loan till now. </aside> --- ## **1. Problem Scope** ### **In scope** - Enable users to **download an updated repayment schedule(on 100% loan)** that reflects: - Disbursals - Part payments (principal / interest / charges) - Interest based on actual utilisation - Loan meta data [ROI, Credit limit, Sanction limit, Interest due, Charges due, Principal due, LAN] - Should reflect any change in ROI during loan tenure - Ensure schedule is **regenerated dynamically** after every transaction - Provide a **single source of truth** aligned with system calculations - **Data type:** JSON and PDF - API to generate the DRP [Download feature to enable at LSP end] **Primary users** - LSPs → LAMF customers **Secondary users** - Customer support teams - Relationship managers / partners - Internal ops and reconciliation teams ### **Out of scope** - Real-time in-app visualisation (non-download view) *Rationale: Phase-1 focuses on downloadable schedule* - Manual override or

---

## #58 — Shortfall communication enhancement Ignoring accou
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

## #59 — CKYC (Decentro) API integration
**Status:** Done | **Last edited:** February 20, 2025 5:27 PM

**Problem:**
are we solving?**

- Manual effort in retrieving and matching data
    - CKYC is a manual process for a lot of banks where KYC records are manually updated and then converted into consumable format by Cersai.
- Prone to errors which might result in borrowers’ records getting updated incorrectly
    - Due to the manual nature of flows, the process is error prone and has an impact on user’s KYC data saved with Cersai (which may be used by other lenders) and may impact user experience
- Upload involves processing/accessing a lot of PII & KYC data of borrowers
    - A lot of PII information and KY

**Solution:**
?**

We will be integrating with Decentro’s upload API to push CKYC data to Cersai.

[Documentation](https://docs.decentro.tech/reference/kyc-and-onboarding-api-reference-identities-ckyc-services-upload-individuals)

API request sections:

| **Parameter** | **Type** | **Number of entries per API call** | **Mandatory** | **Definition** |
| --- | --- | --- | --- | --- |
| `name` | String | One | Yes. Hardcoded | The name of the employee who has done the KYC verification and is performing the CKYC upload.  |
| `designation` | String | One | Yes. | The designation of the employee who is performing the CKYC upload. |
| `kyc_declaration_place` | String | One | Yes. Hardcoded | The place of declaration or verification of the KYC documents. |
| `employee_code` | String | One | Yes. Hardcoded | The

---

## #60 — LSQ data sync
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- LSQ lead stage is not synced with the DB status, as we introduced new application step in loan application journey.
- Push PF, ROI, Platform and sanction limit on LSQ to enable RMs to assist customer on call.
- Update customer details on LSQ when customer details gets changed using admin action.
- Show LSQ lead owner details on the service dashboard.

---

**Solution:**
?**

---

## #61 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #62 — Admin action to update mandate status & interest
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Manual mandate status updates in our database require multiple handoffs between lenders, ops, and tech teams
- The process is inefficient, requiring file formatting and manual updates
- High dependency on technical team for routine database updates
- Time-consuming workflow with multiple touch points increases the risk of errors and delays

---

**Solution:**
?**

Enable operations team to directly manage mandate status updates and interest creation by:

- Creating a self-service portal for ops to upload status files
- Automating the validation and database update process
- Eliminating technical team dependency for routine updates
- Reducing turnaround time and potential errors

---

## #63 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #64 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #65 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #66 — Rounding of Accrued Interest before Posting bill a
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

## #67 — TCL Dynamic repayment schedule
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

## #68 — Ticketing Tool Evaluation Document
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# Ticketing Tool Evaluation Document ## 1. Introduction ### Purpose of Evaluation The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation. ### Scope and Objectives This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include: - Analyzing feature sets and usability - Evaluating system performance and reliability - Reviewing security and compliance standards - Assessing cost-effectiveness and support options DATA sharing over WA and 1:1 WA chat with MFD - PI Data and any other data ## 2. Current Challenges ## Agent Challenges/process gap | # | Challenge | Impact | Priority | | --- | --- | --- | --- | | 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 | | 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 | | 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 | | 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 | | 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 | | 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 | | 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 | | 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 | | 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 | | 10 | No visibility into **TAT of internal ticket and resolution TAT from the 3P** | Inability to provide ETAs to customers | P0 | | 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 | |

---

## #69 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #70 — DSP website revamp
**Status:** Not started | **Last edited:** February 12, 2025 4:29 PM

# DSP website revamp # Problems to solve 1. “Make the website a public website” 1. Make it accessible on Google and other search engines (already visible through Bing) 2. Brand impression: currently looks like a placeholder website 3. Improve “About DSP” section 1. More prominently referencing to the DSP group - Review other DSP children websites 4. Product offerings 1. Structured lending 2. LAMF - understand what’s missing 3. LAS - show coming soon? 5. Regulatory 1. Link RBI’s sachet portal 2. Prominently display name, email, contact number of grievance redressal officer on website 3. Prominently display details of COO - Principal Nodal officer on website 6. Minor fixes 1. Update address - 11th floor instead of 10th floor 2. Update CIN 3. Operating timings: customer care 4. Update partners list 5. Benefits → “RBI registered” needs to come with a disclaimer - refer to flexiloans footer 7. Logo finalisation ![image.png](DSP%20website%20revamp/image.png) # Solution space - [ ] Understand scope - [ ] Talk to priya - What is “headers” - Pankaj notes - [ ] Get feedback shared by Pankaj Thapar (policy consultant) - [ ] New website mood board - how much brand referencing is needed? | Problem | Proposed solution | | --- | --- | | 1.a | - Submit site on Google Search Console - Make sitemap.xml - Make robots.txt | | | | WEBSITE LAYOUT ### Header - Partners - Products - About ### Hero - Title - “Loans against securities” - “digital first approach” - CTA ### About Organisation stats - Money disbursed, Loans given, no. of partner tie ups - Since 160+ years ![image.png](DSP%20website%20revamp/image%201.png) ### Our products - LAMF - LAS - Structured lending ### LAMF features ### How it works ### Footer ## Additions - FAQs - About us → our team

---

## #71 — [Platform] Liveliness check
**Status:** In progress | **Last edited:** December 26, 2024 2:13 PM

**Problem:**
are we solving?**

Users can pledge their collateral using our platform and can get a loan within 5 minutes. The process is completely digital and can be done via just an application or website.

To ensure fair use of our product, there are certain checks that need to be in place to avoid frauds for un-willing / unaware users. 

The same is proposed by RBI in their guidelines:

<aside>
💡

The RE must ensure that the Live photograph of the customer is taken by the authorized officer and the same photograph is embedded in the Customer Application Form (CAF). Further, the system Application of th

**Solution:**
?**

We will be integrating with Digio’s passive liveliness check API which uses a base64 to identify the following checks:

- If there is a person in the image
- If the shared photograph is a live photo

What is a live photo?
When a customer clicks there photograph while actually being there in front of the lens - it is considered as a live photo. 

What is not a live photo?

- Photograph of a passport size picture
- Photograph of a screen (picture of person)
- Photograph of a person on a video call

---

## #72 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #73 — [Platform] Risk report
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

## #74 — Figma file organisation
**Status:** Not started | **Last edited:** December 2, 2024 3:59 PM

**Problem:**
are we solving?**

- Searching for updated files of features and different stages of the journey
- Get visibility on how each stage is handled for different lender
- Easy visibility on version history, compliance updates etc. done in the past - need to view in one place
- Allow storing secondary flows like: error handling, drop-off flows etc

---

## #75 — [Platform] RTA portfolio API integration
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

## #76 — [DSP] Dues collection comms
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

## #77 — VKYC for DSP and Co-Lending
**Status:** In progress | **Last edited:** August 19, 2025 7:01 PM

# VKYC for DSP and Co-Lending [LSP Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/LSP%20Focused%20VKYC%20Journey%20Alignment%20238e8d3af13a80cd80c6f64c76ab3aed.md) [Volt Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/Volt%20Focused%20VKYC%20Journey%20Alignment%20216e8d3af13a801bbba2eb686074c82b.csv) [VKYC: Vendor Evaluation](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Vendor%20Evaluation%20217e8d3af13a80dfb53bed7d04c1e7f3.md) [VKYC: Regulatory Understanding](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Regulatory%20Understanding%20217e8d3af13a809f88e9f173d73f3d5a.md) [Discussion with Rohan (Groww)](VKYC%20for%20DSP%20and%20Co-Lending/Discussion%20with%20Rohan%20(Groww)%20254e8d3af13a8085a070ce018cec0f02.md)

---

## #78 — Product note NSDL PAN Verification
**Status:** In progress | **Last edited:** April 7, 2026 3:21 PM

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- Ensuring all the various sources [Digilocker, LSP, CKYC, etc.] through which DSP is obtaining the PAN related details (PAN number, PAN Name, and PAN DoB) must be verified via NSDL as a part of compliance and KYC.
- Verification with Primary source for KYC being Digilocker.
-

# Product note: NSDL PAN Verification ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? As per RBI’s KYC guidelines, if as an RE we are obtaining PAN of the customer the same should be verified from the issuing authority (as per point 10(j) of Chapter III in the RBI KYC [Masterdirections](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566)). This means that PAN should be verified via the NSDL PAN verification API. ![image.png](%5BDSP%5D%20NSDL%20PAN%20Verification%20alignment/image.png) With the current sources for obtaining PAN that we use in the KYC journey 1. Digilocker PAN 2. If Digilocker PAN is not fetched, we use Signzy enrichment API for verification Currently we are not integrated with the NSDL PAN verification API for verifying PAN details, which makes us non-compliant. Also, even in cases where we are able to receive PAN document from Digilocker that also needs to be verified from NSDL which is the verification facility of the issuing authority as users can also directly update/ renew PAN with ITDB and records might not be synced with Digio. The interval/ frequency when digilocker updates the new PAN when a user renews it is also uncertain. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users - Ensuring all the various sources [Digilocker, LSP, CKYC, etc.] through which DSP is obtaining the PAN related details (PAN number, PAN Name, and PAN DoB) must be verified via NSDL as a part of compliance and KYC. - Verification with Primary source for KYC being Digilocker. - Fallback for Consuming Name from Decentro PAN API for Volt flows in order to use it for NSDL PAN Verification in the fallback flows (Volt) - ~~Downstream changes in th e agreement name and DoB.~~ ### Out of scope - - Call out on items out of scope - Rationale for exclusion - --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) - 100% compliance in terms of verifying Proof of identity in KYC

---

## #79 — [Platform] Validation to Stop Un-pledging, closure
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

## #80 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #81 — MNRL Compliance Validation Integration
**Status:** Not started | **Last edited:** April 29, 2026 5:11 PM

**Problem:**
are we solving?**

---

- Currently, our system does not have a standardized mechanism to validate mobile numbers against authoritative revocation and risk datasets.
- This creates a gap where deactivated or reassigned numbers can still be used within onboarding and auth flows, leading to potential exposure of sensitive information (like OTPs) to unintended users.
- Additionally, numbers flagged by Department of Telecommunications (DoT) and Law Enforcement Agencies (LEAs) for fraud or non-compliance may remain undetected, increasing the platform’s exposure to fraud risk and regulatory non-comp

**Solution:**
?**

---

- We propose implementing MNRL validation at two critical touchpoints in the user journey to ensure early risk detection and strict compliance at the point of loan creation.
- Currently, mobile numbers appear in the MNRL dataset for multiple reasons. As part of the implementation, users will be blocked from loan account creation only for specific high-risk categories, based on compliance requirements.

| disconnectionreason_id | disconnection_reason | Action |
| --- | --- | --- |
| 1 | Subscriber Verification Non-compliant Cases | Don’t Block |
| 2 | Disconnection due to Zero Usage or Non-payment | Don’t Block |
| 3 | LEAs Reported Cybercrime | Block |
| 4 | DoT Reported Fake or Forged Cases | Block |
| 5 | TSP Internal Analysis | Block |
| 6 | Others  | Don’t Block |

---

## #82 — NSDL PAN integration
**Status:** Not started | **Last edited:** April 29, 2026 5:11 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #83 — VKYC Integration PRD
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

## #84 — Product Note – DRPS (Final Version – Unified Forma
**Status:** Ready for Tech | **Last edited:** April 22, 2026 7:17 PM

**In scope:**
- Credit Line products only
- Monthly frequency
- Single unified schedule table
- JSON + PDF output

Term Loans are out of scope.

---

# Product Note – DRPS (Final Version – Unified Format) # 1. Background & Context ## Who is facing the problem - End customers using LAMF (Credit Line / LAS) - Customer support & operations teams - NBFC (regulatory requirement to provide updated repayment schedule) --- ## What is the challenge today - Static schedules become outdated after: - Disbursement - Part repayment - ROI change - Charge application - Users depend on SOA to understand updated dues. - No single structured month-wise forward view aligned with current POS. --- ## Why this is important LAMF is a **dynamic demand loan**, not a fixed EMI loan. A Dynamic Repayment Schedule must: - Reflect actual utilisation - Reflect historical interest accrual - Provide predictive view till closure - Be aligned with system ledger - Be audit-reconcilable --- # 2. Problem Definition DRPS must: 1. Reflect actual historical data till generation timestamp. 2. Reflect projected dues till closure date. 3. Be aligned to: - Current POS - Current ROI - Closure date (currentTermEndDate) 4. Include non-contingent charges prospectively. 5. Use a **single continuous table format**. --- # 3. Solution Scope ## In Scope - Credit Line products only - Monthly frequency - Single unified schedule table - JSON + PDF output Term Loans are out of scope. --- # 4. DRPS Structure There will be **one unified repayment schedule table**. Older rows = system-derived actuals. Future rows = system-computed projections. The format remains identical for all rows. --- # 5. Repayment Schedule Columns (Final – As Per New Requirement) | Column | Description | | --- | --- | | Repayment Date | Month-end date (7th of next month for due logic; last row = closure date if mid-month) | | Outstanding principal (Opening) | Principal outstanding at start of period | | Principal payable/Prepayment | Principal component (only non-zero in closure row unless repayment exists historically) | | Outstanding principal (Closing) | Opening − Principal (interest does not reduce principal) | | Instalment | Interest + Charges (Last instalment principal will be included in instalment) | | Interest payable/Paid | Interest for that period (actual for past, computed for future) Middle of the month accrued interest for interest until now + calculate future interest based on current ROI | | Charges payable/Paid | Retro charges for past; Non-contingent charges for future (AMC charge) | No instalment type column. --- # 6.

---

## #85 — CKYC Comms for Regulatory Compliance
**Status:** Done | **Last edited:** April 17, 2026 2:41 PM

**Problem:**
are we solving?

- Currently, DSP Finance (via Decentro) will search for an existing CKYC record in the CERSAI registry (using PAN) → if found, it downloads the data, compares it, and uploads any updates → if not found, it creates a new CKYC record.
- Regulatory compliance mandates that customers be notified when a CKYC record is created by DSP Finance.
- Currently, there is no automated mechanism to trigger an acknowledgement SMS to customers upon CKYC ID creation.
- Without this flow, DSP Finance risks non-compliance with RBI regulatory notification norms.

---

**Solution:**
?

**In scope:**
- Automated SMS trigger inline within the Decentro web-hook processing flow
- Per-record eligibility check (status == COMPLETED AND ckycReferenceId == null)
- Customer phone number resolution from internal system using fxcid_key
- Dynamo DB logging at per-record level for all outcomes (success, failure)
- Trigger Condition Logic
    - When Decentro’s bulk CKYC web-hook is received, the system insp

---

## #86 — KYC & Mandate Workflow PRD
**Status:** Done | **Last edited:** April 14, 2025 7:17 PM

**Problem:**
are we solving?**

1. LSPs currently need to integrate with third-party SDKs to complete the KYC and mandate steps. Integrating two separate SDKs is cumbersome, fails to establish a high standard for DSP, and raises compliance concerns when DSP credentials are shared with LSPs for SDK invocation.
2. Alternatively, LSPs can initiate the Digilocker/mandate step via a web URL, which opens in a web view belonging to a third-party provider. DSP has no control over the session, screens, or analytics on what step user dropped.
3. The go-live TAT for LSPs increases due to third-party SDK integrations,

**Solution:**
?**

We are introducing fully customizable, DSP-managed user screens to deliver a seamless, compliant, and consistent user experience. These screens will allow LSPs to customize themes and branding to align with their specific requirements.

This solution eliminates the reliance on third-party SDKs, reduces integration complexity, and accelerates the go-live process.

Additionally, LSPs can enable or disable specific modules, or manage them independently through backend APIs:

1. **KYC Module**:
    - Mandatory for all LSPs and cannot be skipped or disabled.
2. **Photo Verification**:
    - Optional module; LSPs can choose to disable it and handle verification via backend APIs.
3. **Additional Data Collection**:
    - Optional module; LSPs can disable it and manage the data collection proc

---

## #87 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #88 — Compliance changes in loan offer screen
**Status:** Ready for kickoff | **Last edited:** Unknown

# Compliance changes in loan offer screen Charter: LOS Pod Priority: P0 # Context Have to make the following changes on the loan offer page, this will be specific for DSP: 1. Remove (excl. GST) from One time charges. 2. Add another line item in the One time charges collapse menu. Add this below the "Processing fees" item; "GST at 18%" and show the value. 3. Have to include a disclaimer that "Account creation/withdrawals are subject to lender approval" # Process # Figma [https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system)

---

## #89 — UX Writing for Indian Fintech Users (Volt) – Resea
**Status:** Unknown | **Last edited:** Unknown

# UX Writing for Indian Fintech Users (Volt) – Research & Guidelines # Introduction Designing a UX writing system requires a deep understanding of **local users**, **financial regulations**, and **effective copy practices**. Every label, message, and CTA must inspire confidence and clarity, since <aside> 💡 > *Fintech content design and UX writing is all about building user trust, and it couldn’t matter more when we’re dealing with people’s money.* https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=Fintech%20content%20design%20and%20UX,we%E2%80%99re%20dealing%20with%20people%E2%80%99s%20money > </aside> ## Understanding the Indian Fintech User ### **Trust is paramount** Indian users, especially first-time investors and borrowers, tend to be cautious with new financial services. <aside> 💡 A McKinsey report found that *trust is the primary factor influencing customer adoption and engagement with fintech services* [thence.co](https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=User%20confidence%20is%20the%20degree,and%20engagement%20with%20fintech%20services) </aside> Users need to feel their money and data are safe. UX copy should therefore reassure at every step (e.g. using phrases like “securely powered by XYZ bank” or highlighting RBI oversight) to strengthen this trust foundation. ### **Broad, diverse audience** Volt’s target users include salaried professionals investing in mutual funds, stocks, insurance, bonds, etc. Many are financially savvy to an extent, but there’s a **wide range of literacy** Some may be first-time investors from Tier-2 cities (as seen with apps like Groww), while others are seasoned market participants. Copy must hit a sweet spot where **both novices and experts can understand it easily** <aside> 💡 As one UX guide advises, F*intech UX should prioritize clear, simple language that can be easily understood by both newbies and experts alike* https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=Problem%3A%20The%20financial%20language%20can,to%20understand%20for%20many%20users </aside> This means avoiding heavy jargon and explaining necessary terms in plain language. For example, instead of “lien marking your mutual fund units,” Volt’s app explains it as *“mark your mutual funds as a security with a trusted lender”* immediately clarifying the action. ### Friendly, guiding tone A friendly tone humanizes complex financial tasks – it’s like having a helpful friend explain things rather than a formal banker. However, the tone should also reflect **professionalism** to build credibility; a balance of *professional yet approachable* works well, as Razorpay’s content team describes: their fintech UX writing maintains a *“consistent tone – professional yet approachable”* to serve users dealing with high-stakes transactions ### Attention span and mobile behaviour Remember that Indian users predominantly access fintech services on mobile (Volt is **mobile-first**, as noted). Mobile users skim and scan due to small screens and on-the-go usage. Studies show people read only ~20–28% of text on

---

## #90 — Copy system for Volt
**Status:** In progress | **Last edited:** Unknown

# Copy system for Volt Charter: Design Initiatives # Context Aim to keep copy clear and build guidelines for people to jusde copy by. [UX Writing for Indian Fintech Users (Volt) – Research & Guidelines](Copy%20system%20for%20Volt/UX%20Writing%20for%20Indian%20Fintech%20Users%20(Volt)%20%E2%80%93%20Resea%20211e8d3af13a808785a4dc9775a26443.md) [Copy Plugin](Copy%20system%20for%20Volt/Copy%20Plugin%2021be8d3af13a8084af15c2492f81eebc.md) [Volt Plugin Knowledge Base](Copy%20system%20for%20Volt/Volt%20Plugin%20Knowledge%20Base%2025de8d3af13a802abbd7d4ab8d9b20d2.md) # Process - [x] Define Volt’s principles for copy based on best practices - [x] Understand compliance and legal requirements from Indian fintechs - [x] Make the prompt for copy json with tone, ux writing principles and Gemini API Key - [x] Build copy on cursor - [ ] Test & Improve # Research Volt’s Design Fundamental Pillars 1. Simplicity 2. Speed 3. Transparency 4. Helpful **Fundamentals of UX Writing (for fintech apps)** At its core, UX writing is about: ✅ **Guiding** users through tasks: What to do ✅ Making **complex information simple**: Information clarity ✅ **Building trust** and confidence: Reassurance ✅ Ensuring **accessibility**: Less jargon more simple words # Figma

---

## #91 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #92 — Loan account creation error handling
**Status:** Ready for kickoff | **Last edited:** Unknown

# Loan account creation error handling Charter: LOS Pod # Context MOM 1. Active loan + Cibil score reason 2. Redirect users to try with another PAN [tentative] 3. Handle in pop up if possible 4. Feedback after the pop up in the flow # Figma [https://embed.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/%5BOLD%5D-Loan-application-flow?node-id=11844-61349&t=r1DgLWQIr5SO6puF-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/%5BOLD%5D-Loan-application-flow?node-id=11844-61349&t=r1DgLWQIr5SO6puF-11&embed-host=notion&footer=false&theme=system) Loan profile did not meet out criteria for a loan account. Last checked eligibility on 12/02/24

---

## #93 — APIs
**Status:** ** Retrieves the status of the KYC verification. | **Last edited:** Unknown

# APIs **Explanation of the API Sequence in the Volt Money Application Flow** Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience. --- ### **Overview** The Volt Money application process involves several key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail. --- ### **1. Login** - **API Used:** *Custom Authentication API (Not listed in the provided APIs)* - **Functionality:** - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone. - **Notes:** - This step establishes a secure session for the user. - While not specified in the provided API list, we use a standard authentication service to handle this process. --- ### **2. PAN Verification** - **API Used:** - `POST /app/borrower/application/kyc/pan/panVerify` - **Partner:** Decentro (facilitates connection to NSDL) - **Functionality:** - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid. - **Data Retrieval:** Fetches the full name associated with the PAN. - **Notes:** - Essential for KYC compliance and identity verification. - Helps prevent fraudulent applications. --- ### **3. Fetch Folio** - **APIs Used:** - `POST /app/borrower/application/fetch/init/otp/v3` - `POST /app/borrower/application/fetch/authCAS/v2` - **Partners:** Cams, KFintech, MF Central - **Functionality:** - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio. - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details. - **Notes:** - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets. - This data is used later in the asset pledge and eligibility assessment. --- ### **4. Eligibility Assessment and Lender Assignment** - **API Used:** - `POST /app/borrower/application/credit/profile/evaluate` - **Partner:** Internal Business Rule Engine (BRE) - **Functionality:** - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria. - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based

---

## #94 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #95 — LSQ Leedsquared
**Status:** Unknown | **Last edited:** Unknown

# LSQ: Leedsquared @Naman Agarwal ### **Overview** LeadSquared (LSQ) is a comprehensive Customer Relationship Management (CRM) tool primarily used by Volt Money to manage lead generation, customer interactions, and the loan application process. LSQ enables sales teams and Relationship Managers (RMs) to track customer journeys, from lead acquisition to loan approval, providing a centralized view of lead data, customer details, and application stages. --- ### **Framework: Business Impact of LSQ** ### 1. **Purpose/Objective** LSQ’s core objective is to **streamline lead management** and **enhance customer support** by providing sales teams with real-time access to lead information and loan application statuses. By organizing customer interactions and loan data in one place, LSQ improves the efficiency and transparency of the sales process, enabling better decision-making and quicker responses to customer needs. ### 2. **Key Features & Functions** | **Feature** | **Description** | | --- | --- | | **Lead Management** | LSQ tracks customer leads from acquisition to conversion, providing visibility into lead status, ownership, and data. | | **Loan Application Tracking** | Displays the current stage of loan applications (e.g., CIBIL check, KYC, approval), helping RMs manage their pipeline. | | **Customer Data Storage** | Stores critical customer details such as name, email, phone number, and loan amounts, enabling personalized outreach. | | **Sales Performance Insights** | Generates reports on lead outreach, conversion, and sales performance, helping teams optimize their strategies. | ### 3. **Business Benefits** - **Improved Lead Conversion**: LSQ helps RMs track the progress of leads efficiently, ensuring no customer falls through the cracks and allowing for timely follow-ups. - **Increased Transparency**: By providing a clear view of each lead’s stage in the loan application process, LSQ reduces ambiguity and improves decision-making. - **Enhanced Customer Support**: Real-time access to customer details and loan data allows RMs to provide more informed and tailored support during customer interactions. ### 4. **Challenges/Current Gaps** - **Lead Stage Sync Issues**: Discrepancies between the stages in LSQ and Volt Money's backend systems can lead to confusion and mismanagement of leads. - **Missing Loan Details**: Critical loan information like Processing Fees (PF), Rate of Interest (ROI), and Sanction Limits are not always available in LSQ, affecting RMs' ability to assist customers. - **Manual Data Updates**: Admin actions (e.g., changes to customer data) are not automatically reflected in LSQ, which can lead to outdated records and inefficiencies. ### 5. **Opportunities for Improvement** - Lead prioritisation - **Automating Data

---

## #96 — API flow for KFS and Agreement
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

## #97 — Approved Scrips productisation
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
We are solving for:

- A governed, audited maker-checker flow for all approved scrip updates in Command Centre
- Support for the following scrip operations via this flow:
    - **Approve new ISIN** — add a new ISIN (Mutual fund or Share) to the approved scrip with all required parameters
    - **Stop new lodgements** — set min LTV to zero for an ISIN (blocks new pledges without impacting existing 

# Approved Scrips productisation Last Edited: May 8, 2026 12:03 PM PRD ETA: April 21, 2026 PRD Owner: Vaibhav Arora ## Background and Context The approved scrip list is the master reference that controls which ISINs can be pledged as collateral in the LMS, and at what LTV. It has two layers: - **Finflux approved scrip** — Global NBFC-level list managed in the LMS (Finflux). Stores min LTV and max LTV per ISIN and enforces that no lodged collateral exceeds max LTV. (Min LTV for default LTV value, Max LTV as a ceiling validation) - Finflux max LTV should be equal to Risk LTV and Finflux min LTV should be equal to Fenix min LTV - **Fenix approved scrip** — Internal list managed at a co-lender relationship (contract) level (colending vs non-colending) and product level (LAS and LAMF). Fenix carries three LTV values per ISIN: Regulatory LTV (= max LTV), Risk LTV (internal ceiling set by the risk team, ≤ Regulatory LTV), and Min LTV. Today, updates to both scrips require manually calling APIs in Fenix and Finflux separately. This is done by anyone with API access and without any audit trail, approval gate, or role-based control. **Who is affected:** - Risk ops team (makers) who need to update scrips frequently but have no safe, governed tool to do so - Risk managers (checkers) who have no visibility into what changed, when, and by whom - End users and LSPs who are indirectly impacted by incorrect LTV values (inflated or deflated offers, wrong shortfall calculations) **What is broken today:** - Fenix and Finflux scrips are updated separately and can fall out of sync — they should be updated atomically - Direct API updates are error-prone. A documented past incident set LTVs to 50 instead of 50% causing 100x limit inflation - No audit log exists for scrip changes — there is no way to trace who changed what and when - No role-based control — anyone with API access can make changes with immediate live impact on offer generation and shortfall computation **Why it matters now — three upcoming catalysts:** 1. **Colending expansion** — More colending relationships mean more contract-level approved scrip variants, increasing change frequency 2. **LTV increase to 70%** — Moving from 45% to 70% introduces higher risk volatility and requires more frequent scrip tuning by the risk team 3. **Loan against Shares launch** — Shares are more

---

## #98 — Colending Disbursement and Charge knock off
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

## #99 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #100 — FD Fixerra
**Status:** Unknown | **Last edited:** Unknown

# FD: Fixerra Last Edited: December 1, 2025 2:13 PM ### Product Alignment Note – Fixerra FD Offering via Partner Dashboard *(DSP Finance × Volt Platform)* --- ### **Problem statement** Volt x DSP have a strong distribution via IFAs, we want to experiment distribution of different products via this channel, because of DSP Finance (NBFC) is looking to expand its retail investment footprint beyond LAMF (Loan Against Mutual Funds) by introducing a Fixed Deposit (FD) product. On the Volt platform today, distributors (primarily MFDs) only have LAMF as the monetizable product. While LAMF has strong unit economics, it is not a top-of-funnel product for retail customers. Fixerra provides the underlying FD product and infrastructure. The hypothesis is: - We already have arms-reach access to a large base of customers with mutual fund holdings. - These customers have a natural affinity for low-risk investment instruments. - FDs can act as a trust-building, widely accepted entry product, opening the funnel for both direct revenue (FD) and future LAMF conversions. This note outlines the scope for v1 of FD origination and servicing through the Volt Partner Dashboard, and is intended to align stakeholders across DSP Finance, Volt, and Fixerra. --- ### 2. Problem statement ### 2.1 Current state - MFDs on Volt can only offer LAMF. - Monetization is limited to one product with a relatively narrow target audience. - No simple “safe” product exists to attract or engage a wider customer base. - Distributors lack tools to deepen customer relationships beyond MF transactions. ### 2.2 Opportunity Introducing FDs: - Expands the product portfolio for MFDs. - Helps create a trust-led entry point (“mouth of the funnel”), improving conversions into higher-ticket products like LAMF. - Offers DSP Finance a scalable retail deposit base. - Allows Fixerra to distribute its FD product through MFD networks. --- ### 3. Product hypothesis **FDs can become a high-trust, low-friction product that increases distributor engagement and revenue, while simultaneously opening the pipeline for LAMF upsell.** Supporting hypotheses: 1. Customers with MF holdings are more likely to evaluate FD products with high confidence. 2. MFDs will be able to deepen their relationship and improve overall earnings by offering a broader product suite. 3. The NBFC can explore differentiated FD structuring based on distribution performance (for example, special rates, bulk programs). --- ### 4. High-level GTM - **Channel:** Volt Partner Dashboard - **Actors:** Mutual Fund Distributors on Volt - **v1

---

## #101 — LAS CMS Confiscation and sale of securities
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

## #102 — LAS Collateral management system
**Status:** Completed | **Last edited:** Unknown

# LAS: Collateral management system Last Edited: July 28, 2025 8:43 PM PRD ETA: June 27, 2025 PRD Owner: Vaibhav Arora # **What is CMS?** The Collateral Management System (CMS) will act as the central infrastructure for managing pledged shares for a Loan Against Shares (LAS) product. It will interface with the Loan Origination System (LOS), Loan Management System (LMS), and Depository Participant (DP) — SHCIL — to manage the full lifecycle of collateral from validation to lien marking, valuation, revocation, and reconciliation. It will also include risk management via real-time LTV monitoring, handling of corporate actions, and tools for operations teams. [CMS system architecture](https://claude.ai/public/artifacts/b5a68c3c-4705-4c9d-b34b-52a1d6bb8ec4) --- # Why do we need a CMS? A **Collateral Management System (CMS)** is essential for a **Loan Against Shares (LAS)** product because collateral (in the form of pledged shares) is **the core security** backing the loan. Without an automated, secure, and integrated system to manage this collateral, the business is exposed to **operational risk, financial risk, and regulatory gaps**. 1. Centralised tracking and management of collaterals: Currently all collaterals are managed by the LMS which makes it very risk prone: A CMS ensures each step is trackable, audit-logged, and consistent with external systems (DP/SHCIL) and internal ones (LMS/LOS). 2. CMS constantly monitors Loan-to-Value (LTV) ratios. If share prices fall, LTV breaches can be automatically flagged (exposure tracking), triggering margin calls or partial lien revocation. 3. Logic separation from LMS: CMS has a lot of collateral management intelligence which should be LMS agnostic, this will make our LMS very modular and easily replaceable since majority of the complexity of collateral management will be handled via CMS. --- # **How are others solving this problem?** The approach to collateral management for Loan Against Shares (LAS) varies widely across the lending ecosystem, largely depending on a company’s scale, tech maturity, and risk appetite. Broadly, solutions fall into two categories: ### 1. **Tightly Coupled CMS-LMS Systems (Usually Vendor-Provided)** Some lenders use **end-to-end lending platforms** where the CMS is embedded within the LMS — often provided by a third-party vendor. These platforms offer: - Pre-integrated lien workflows - Basic LTV tracking - Unified borrower and collateral view ### 2. **No CMS — Operations-Led Collateral Tracking** Most early-stage or mid-sized lenders operate without a dedicated CMS. Instead, they rely on: - Manual **ops processes** to initiate and track lien/revocation files - **Excel sheets or shared dashboards** to monitor pledged ISINs

---

## #103 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #104 — Product Note LAS Customer Consent Capture
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

## #105 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #106 — Product note Excess refund Colending
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

## #107 — Product note Foreclosure (Colending)
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure (Colending) Last Edited: May 19, 2026 2:47 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**. ### Who is impacted - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting ### What is broken today Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations: 1. **Incorrect foreclosure simulation** Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances. 2. **Pending transaction inconsistencies** Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations. 3. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring that: - Loan 90 and Loan 10 are closed - All charges and interest are posted - Excess settlement is completed 4. **Penalty and applicable charge dependency** Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment. 5. **Incorrect collateral release timing** Securities may be released before confirming that **both loan legs are closed**, which introduces risk. ### Why this is important Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to: - Incorrect payoff amounts shared with borrowers - Operational rework due to partial closures - Accounting mismatches across loan legs - Risk of releasing collateral before loan closure creating financial exposure for the NBFC This PRD defines a **colending foreclosure workflow** that ensures: - Correct payoff simulation - Transaction sequencing across loan legs - Controlled collateral release - Accurate excess settlement. --- # **1. Problem Scope** ## **In Scope** ### **Colending foreclosure simulation** Foreclosure simulation will incorporate balances from: - Loan

---

## #108 — Product note Razorpay PG integration Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Enable **dynamic MID selection** for PG repayments:
    - Colending loans → escrow-linked MID (at a contract level - Makes it extendable to multiple MIDs for multiple colending relationships)
    - Non-colending loans → DSP MID
- Store:
    - **MID at contract level**
- Fetch:
    - API credentials via **secret manager (not stored directly)**
- Ensure:
    - All Razorpay operations use the **sam

# Product note: Razorpay PG integration Colending Last Edited: April 7, 2026 3:38 PM PRD ETA: March 26, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** - **Who is facing the problem** - NBFC (DSP) – Product, Engineering, Finance - Co-lenders (e.g., TCL) - Payment partner (Razorpay) - LSPs (Volt) and end customers - **What is the challenge** - Current PG integration uses a **single MID (merchant account)** for all repayments - For **co-lended loans**, regulations require: - Funds to be collected directly into a **designated escrow account** - In Razorpay: - **MID determines settlement account** - Each MID has **separate API credentials** - System today: - Does not differentiate between **colending vs non-colending loans at MID level** - **Why is it important** - Regulatory requirement → escrow-based fund flow - Incorrect MID usage → funds settle to wrong account - Breaks reconciliation and lender settlement - Scaling issue → multiple co-lenders = multiple MIDs --- ## **1. Problem scope** ### In scope - Enable **dynamic MID selection** for PG repayments: - Colending loans → escrow-linked MID (at a contract level - Makes it extendable to multiple MIDs for multiple colending relationships) - Non-colending loans → DSP MID - Store: - **MID at contract level** - Fetch: - API credentials via **secret manager (not stored directly)** - Ensure: - All Razorpay operations use the **same MID context**: - Order creation - Payment fetch - Payment validation - Stakeholders: - Primary: Engineering, Finance - Secondary: Razorpay, LSPs --- ### Out of scope - Changes to: - Razorpay API contracts (no change) - SDK integration at frontend (Volt continues as-is) - Multi-MID fallback logic within a single contract - Changes to repayment lifecycle or LMS posting --- ## **2. Success Criteria** ### Key outcomes - **100% correct routing of PG funds** to escrow for colending loans - **Zero reconciliation issues** due to incorrect MID usage - Seamless experience for LSP and end user (no UX changes) ### Metrics - % of PG transactions using correct MID (target: 100%) - Payment success rate (no degradation post rollout) - Reconciliation mismatches due to MID errors (target: 0) ### Post-launch good state - MID selection is: - Fully automated - Invisible to end user - All Razorpay flows work unchanged ### Guardrails - No increase in: - Order creation failure rate - Payment verification failures - API latency --- ## **3. Solution Scope** ###

---

## #109 — Product note Virtual account handling for Colendin
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

## #110 — Product note template evaluation
**Status:** Completed | **Last edited:** Unknown

# Product note template evaluation Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ### Lifecycle of a feature (Why product note): ```json ┌────────────────────┐ │ │ │ (initial problem, │ │ scope, context) │ └─────────┬──────────┘ │ ▼ ┌──────────────── Grooming / Kickoff ───────────────┐ │ │ │ • Align on scope │ │ • Identify edge cases │ │ • Refine requirements │ └─────────┬───────────────────────────┬─────────────┘ │ │ ▼ ▼ ┌───────────────────┐ ┌────────────────────────┐ │ Design Handoff │ │ Cross-Functional │ │ (UX, flows, │ │ Sign-offs │ │ mocks, journeys) │ │ • Finance │ └─────────┬─────────┘ │ • Compliance │ │ │ • Business Ops │ ▼ └─────────┬──────────────┘ ┌───────────────┐ │ │ │ │ │ Product Note │◄─────────────────┘ └─────────┬─────┘ ▼ ┌───────────────────┐ │ PRD │ │ (final detailed │ │ specifications) │ └─────────┬─────────┘ ▼ ┌──────────────┐ │ Engineering │ │ (breakdown, │ │ estimation, │ │ sprinting) │ └────────────── ┘ ``` ### What is a product note? A product note is a succinct, structured document that brings all stakeholders onto the same page before execution begins. Execution here is function specific: - PRDs for PMs - Low fidelity mockups and high fidelity for Design - System design documents for Engineering team - Development of core product It distils the problem, the scope, the target audience, the desired outcomes, and the key decisions into a single source of truth. Its goal is alignment ensuring everyone understands what we’re solving, why it matters, what success looks like, and what the first version will include. ### Use cases of a product note: **1. What is the problem?** - Clear articulation of the problem statement. (What are we not solving) **2. Who are we solving it for?** - Target audience definition and roll-out strategy. (GTM should be separate from defining the target audience) / Phasing can be a part of the product note however GTM may not be a product note **3. How will we know the problem is solved?** - Success criteria and measurable outcomes. **4. How are we planning to solve it?** - Scope of the solution and key components of the approach. - Entry points (User flow diagram) / Use cases **5. Why does this problem matter now?** - Prioritisation rationale and business/user impact. (Merge with what is the problem?) **6. When will we solve it and who owns what?** - Timeline, milestones, and ownership across teams. (Can be a part of solution scope) **7. How does

---

## #111 — Razorpay SDK enhancement for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

- Unified Razorpay integration across:
    - DSP loans
    - Colended loans
- Support for:
    - SDK-based flow
    - Payment link flow
- Dynamic resolution of:
    - MID
    - Razorpay client_id
- Contract-level PG configuration
- Frontend enablement for SDK invocation

**Primary users**

- LSP engineering teams (Volt FE + BE)
- DSP LMS / PG systems

**Secondary users**

- End customers
- Ops

# Razorpay SDK enhancement for Colending Last Edited: April 22, 2026 6:29 PM PRD ETA: April 22, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Today, LSPs (e.g. Volt, CRED, PhonePe) can integrate with DSP for repayments via multiple payment gateway (PG) options: - DSP internal PG - Razorpay - Cashfree - Native PG managed by LSP (direct settlement) ### **Current Challenge** With **colending**, regulatory guidelines mandate: - Funds must flow into **escrow accounts** - This leads to **different MIDs**: - DSP loans → DSP current account MID - Colending loans → Escrow MID For Razorpay SDK: - `client_id` is tied to MID - SDK invocation becomes **MID dependent** ### **What is broken today** - LSPs need **loan-type aware logic** - Multiple client IDs → complex integration - Breaks abstraction: > DSP vs Colending loans should be indistinguishable > ### **Why this matters** - Colending is a key growth lever - Repayment friction directly impacts: - Conversion - Partner experience - Slows onboarding of new LSPs --- ## **1. Problem Scope** ### **In scope** - Unified Razorpay integration across: - DSP loans - Colended loans - Support for: - SDK-based flow - Payment link flow - Dynamic resolution of: - MID - Razorpay client_id - Contract-level PG configuration - Frontend enablement for SDK invocation **Primary users** - LSP engineering teams (Volt FE + BE) - DSP LMS / PG systems **Secondary users** - End customers - Ops / reconciliation teams --- ### **Out of scope** - Supporting multiple PGs for colending (Razorpay only) - Changes to settlement / reconciliation - Native LSP PG flows --- ## **2. Success Criteria** ### **Primary outcomes** - Single integration for all loan types - SDK invocation fully abstracted - No increase in payment failures ### **Post-launch good state** - 100% repayments via unified API - No loan-type branching at LSP - 99.9% uptime ### **Guardrails** - No reconciliation mismatch - No incorrect MID usage - No increase in disputes --- ## **3. Solution Scope** ### **Solution Overview** Introduce **contract-driven PG abstraction** where: - `create repayment order API` determines: - PG (Razorpay) - MID - client_id - LSP consumes a **single API** - SDK invocation is **agnostic to loan type** --- ### **Core Design** ### **1. API Enhancement** **Endpoint** ``` POST /repayment/order/v1 ``` **Enhancements** - Add: `paymentGateway` - Populate: `paymentGatewayOrderId` (for SDK) --- ### **2. Contract-Level Configuration** | Field | Description | | ---

---

## #112 — Risk management system LAS
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

## #113 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #114 — Suspension framework
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?

Currently, suspensions or blacklisting actions (triggered by screening alerts, loan irregularities, or risk assessments) are handled inconsistently across different systems and entities within the NBFC. This fragmented approach creates several critical issues:

1. **Inconsistent Enforcement**: Different systems apply suspension logic differently, leading to gaps where suspended entities can still transact through certain channels
2. **`Missing Hierarchy Propagation**: When a customer is flagged at PAN level, the suspension doesn't automatically cascade to their existing leads,

**Solution:**
?

---

## #115 — Trackwizz continuos monitoring enhancement
**Status:** Unknown | **Last edited:** Unknown

# Trackwizz continuos monitoring enhancement Last Edited: November 13, 2025 12:39 PM PRD Owner: Vaibhav Arora # Contract Changes Required for Stopping Continuous Monitoring - AS504 API ## Executive Summary Based on the AS504 API documentation, the following contract modifications are necessary to effectively discontinue continuous monitoring (Purpose 04) for customers while managing ongoing screening operations. --- ## 1. API Purpose Codes & Termination Logic ### Current Purpose Definitions - **Purpose 01**: Initial Screening with API Response and No Storage - **Purpose 03**: Initial Screening with API Response and TW Workflow - **Purpose 04**: Continuous Screening with TW Workflow ### Key Finding To stop continuous monitoring, contracts must clarify the mechanisms for Purpose 04 discontinuation, as there is no explicit "Purpose 05" for stopping monitoring in the current API specification. --- ## 2. Required Contract Amendments ### 2.1 Data Retention & Deactivation Terms **Required Changes:** ### 2.1.1 Customer Status Field Modification - **Field**: `status` (Customer Status Enum) - **Current Values**: Active, Closed, Dormant, Inactive, Suspended - **Contract Change**: Add explicit condition: `When a customer record's purpose changes from "04" (Continuous Screening) to either "01" or "03" (Initial Screening only), the system must: 1. Cease real-time continuous screening operations 2. Maintain historical screening records for audit/compliance purposes 3. Update effectiveDate to reflect when continuous monitoring ended 4. Mark continuous monitoring as "Terminated" in internal tracking` **Effective Date Requirements:** - Must be provided in "DD-MMM-YYYY" format - Should reflect the exact date when continuous monitoring ceases - Cannot be a future date (must be current or past) --- ### 2.2 Purpose Code Combination Restrictions **Contract Required Clause:** The API currently allows: - Purpose 01 & Purpose 04 (combination allowed) - Purpose 03 & Purpose 04 (combination allowed) **To Stop Continuous Monitoring**, the contract must specify: `Transition Rules for Discontinuing Continuous Monitoring: 1. If Purpose 04 is removed from a request while Purpose 01 or 03 remains: - Continuous monitoring CEASES immediately - Initial screening continues as specified - Customer record remains in TrackWizz but without ongoing monitoring 2. If ONLY Purpose 04 is passed in a new request: - Continuous monitoring CONTINUES unchanged 3. If NEITHER Purpose 01, 03, nor 04 is passed: - Request is REJECTED per validation MRV12` --- ### 2.3 Mandatory Fields for Terminating Continuous Monitoring **Contract Clause - Purpose 04 Discontinuation:** When removing Purpose 04, the following fields become mandatory: ``` FieldRequirementFormatPurposesourceSystemCustomerCodeMandatoryString (Max 100)Identifies record to stop monitoringsourceSystemNameMandatoryEnum

---

## #116 — Volt - Shortfall Communication Enhancement – Due D
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

## #117 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #118 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #119 — Jira Integration on LSQ Service desk
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
**

- Ticket creation from LSQ → Jira
- Bidirectional sync for:
    - Status
    - Comments
    - SLA metrics
    - Priority
- Jira issue visibility inside LSQ ticket view
- SLA compliance dashboards within LSQ

**Out of Scope**

- Jira → LSQ ticket creation
- Custom Jira workflow or automation changes
- Integration with other Atlassian tools (Confluence, Slack, etc.)

# Jira Integration on LSQ Service desk ## **Jira Integration with LeadSquared Service Desk** ### **Context** Volt is implementing a Service Desk in LeadSquared (LSQ) to manage all internal and external support requests. While LSQ will serve as the primary ticketing and workflow system for business and operations teams, Jira will continue to be the engineering and product team’s issue tracking system. ### **Objective** Build a **Jira Integration Layer** within LSQ to enable: - Direct **ticket creation in Jira from LSQ**. - **Bidirectional sync** for key fields — Status, Comments, SLA, and Priority. - **Embedded Jira ticket visibility** within LSQ UI. - Unified **SLA compliance tracking** in LSQ for Jira-linked issues. ### **Problem Statement** At present, there is no structured mechanism for Ops or Support teams to escalate issues from LSQ to Jira. Without integration: - Engineering escalations must be manually recreated in Jira. - Status tracking between LSQ and Jira is disconnected. - SLA compliance and visibility across tools is missing. - No unified audit trail exists across ticket lifecycles. **Challenges / Gaps Identified** The following key Jira–LSQ integration elements are **not currently visible or functional** within the LSQ Service Desk: - SLA metrics not visible in Service Desk. - Jira Owner (Assignee) and reassignment not visible in Service desk - Status changes visibility not visible in the Service desk ### **Existing Jira Integration (Zendesk Reference)** Currently, Volt’s Zendesk–Jira setup supports: - Ticket creation from Zendesk → Jira - Limited field sync (status, comments) - No SLA sync or audit visibility This integration will be **replicated and enhanced** in LSQ. ![image.png](Jira%20Integration%20on%20LSQ%20Service%20desk/image.png) ### **In Scope** - Ticket creation from LSQ → Jira - Bidirectional sync for: - Status - Comments - SLA metrics - Priority - Jira issue visibility inside LSQ ticket view - SLA compliance dashboards within LSQ **Out of Scope** - Jira → LSQ ticket creation - Custom Jira workflow or automation changes - Integration with other Atlassian tools (Confluence, Slack, etc.) ### **Functional Requirements** ### **1 Jira Ticket creation:** - Out of the box jira ticket creation fields: - Project - Issue Type - Ticket Owner - Priority - Summary - Description - Attachement - Additional Fields Required: - L1 Category - L2 Category - Requester - LSQ Agent creates ticket → fills L1, L2, Issue Type, Summary, Priority, Description. - LSQ → Jira API creates issue with above fields + Reporter + Lender - Jira ID

---

## #120 — Support Requirement
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
**

- Manual ticket creation by Chat/Calling teams
- Parent–child ticket architecture
- Assignment, ownership, and SLA logic
- Disposition capture on resolution
- Agent & Manager dashboards
- Jira integration for Tech escalations
- Ticket activity logs
- SLA breach alerts & escalation rules

# Support Requirement ## **Objective & Context** Phase 1 aims to establish a **structured Internal Service Desk** within LeadSquared (LSQ) for Chat, Calling, and Operations teams. This Service Desk enables internal teams to **log, assign, track, and resolve internal issues** with: - Standardised ticket lifecycle - SLA tracking & escalation - Ownership & accountability - Reporting & visibility - Optional Jira escalation for Tech teams This phase is **manual only (no external integrations)** and forms the foundation for future omnichannel Service Desk capabilities. ## **Problem Statement** Today, internal issues are logged through scattered channels like WhatsApp, email, and direct calls. This results in: - No centralised system for ticket creation and disposition capture - No SLA enforcement - Manual follow-ups and delays - No visibility into ticket ageing or owner performance - No audit trail of actions taken - No structured categorisation for root-cause insights A unified LSQ-based Internal Ticketing System will standardise **Ticket Creation → Ownership → Resolution → Closure**, ensuring **SLA adherence, accountability, transparency, and improved operational efficiency**. ## **Scope & Deliverables** Build a structured internal ticketing system within LSQ that supports manual ticket creation, lifecycle tracking, SLA management, parent–child tickets, dashboards, and Tech escalations via Jira. ### **Key Deliverables** 1. **Ticket Schema** - L1–L3 categories - Priority & SLA mapping - Dispositions & RCA fields 2. **Ticket Creation Form** - Mandatory fields & validations - Customer verification checks 3. **Ticket Activities & Logs** - Comments, attachments - Status change audits - Ownership logs 4. **Assignment & Ownership Rules** - Manual owner assignment - Owner assignment Automations 5. **SLA Engine** - SLA start/stop/pause - Breach alerts - Escalation alerts to manager/superviours 6. **Parent–Child Ticket Model** - Parent ticket by Support team - Child ticket for Operations team. - Independent SLA for child tickets 7. **System Notifications** - SLA breach alerts - Assignment alerts - Resolution alerts 8. **Agent & Manager Views** - Smart Views - Ticket ageing dashboards - SLA compliance dashboards 9. **Reopen Logic** - New SLA cycle on reopen - Mandatory reason ### **In Scope** - Manual ticket creation by Chat/Calling teams - Parent–child ticket architecture - Assignment, ownership, and SLA logic - Disposition capture on resolution - Agent & Manager dashboards - Jira integration for Tech escalations - Ticket activity logs - SLA breach alerts & escalation rules ### **Out of Scope** - Auto-ingestion via WhatsApp, Email, or Calls - CSAT or survey automation -

---

## #121 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #122 — Cost estimates
**Status:** Unknown | **Last edited:** Unknown

# Cost estimates # AWS Infrastructure Cost Projections (2024-2026) ## Constants & Assumptions | Parameter | Value | Notes | | --- | --- | --- | | Growth Rate | 2x yearly | Partner base doubles each year | | Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) | | Retention Period | 84 months | 7 years for regulatory compliance | | Emails per Partner | 3/month | Registration, payout, GST notifications | | API Calls per Partner | 20/month | Includes all interactions | | Lambda Executions per Partner | 10/month | All automated processes | ## Growth & Cost Projections | Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | | --- | --- | --- | --- | | Active Partners | 2,500 | 5,000 | 10,000 | | Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB | | Cumulative Storage | 93 GB | 279 GB | 558 GB | | Monthly Emails | 7,500 | 15,000 | 30,000 | | Monthly API Calls | 50,000 | 100,000 | 200,000 | ## Monthly Cost Breakdown (USD) | Service | Year 1 | Year 2 | Year 3 | Scaling Factor | | --- | --- | --- | --- | --- | | S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation | | RDS | $45 | $65 | $110 | Step Function* | | Lambda | $3 | $6 | $12 | Linear | | SES (Email) | $0.75 | $1.50 | $3 | Linear | | API Gateway | $5 | $10 | $20 | Linear | | CloudWatch | $15 | $25 | $45 | Step Function* | | Route 53 | $0.50 | $0.50 | $0.50 | Fixed | | Step Functions | $2 | $4 | $8 | Linear | | **Total Monthly** | **$73.39** | **$118.42** | **$211.33** | | | **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** | |

---

## #123 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #124 — Term Loan Communications
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

## #125 — Term Loan Customer Statements
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

## #126 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #127 — Term Loan Excess Handling and Refund
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

## #128 — Term Loan Mandate Repayments
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

## #129 — Term Loan Prepayments and Excess Handling
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

## #130 — Term Loan Sell off
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

## #131 — How banks and NBFCs manage rounding of interest an
**Status:** Unknown | **Last edited:** Unknown

# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases. ## **1. Regulatory & Industry Context** ### RBI Guidelines: RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in: - Customer charging - Auto-debit recovery - Tax invoicing - Reconciliation of ledgers So, banks and NBFCs need to: - Ensure **customers aren’t overcharged** - Match debits with invoices/statements - Maintain proper **audit trail** and **variance accounting** if rounding is applied --- ## 2. Rounding Methods Used by Banks & NBFCs | Type | Common Use Case | Real-world Examples | | --- | --- | --- | | **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs | | **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton | | **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs | | **Cumulative Rounding** | Long tenure loans | Used in housing finance | --- ## 3. Detailed Accounting Treatment by Banks/NBFCs ### **A. Exact Posting (No Rounding)** ### Use Case: - Processing fees + GST - Penal charges ### System Flow: 1. Fee computed: ₹100 2. GST @18% = ₹18 3. Total = ₹118.00 (posted and debited as-is) ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹118.00 | | | Processing Fee Income | | ₹100.00 | | GST Payable (Output) | | ₹18.00 | ✅ Matches invoice and is tax compliant --- ### **B. Round at Posting (Nearest Rupee)** ### Use Case: - Accrued interest - EMI interest - Installment schedules ### Example: - Accrued Interest: ₹199.48 → Rounded: ₹199 - Accrued Interest: ₹199.50 → Rounded: ₹200 ### System Flow: - Round value **at the point of debit** ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹200.00 | | | Interest Income | | ₹199.48 | | **Rounding Reserve GL (Internal)** | | ₹0.52 | > 🔸 If we round down, the 0.52 may be debited to an expense account. > ### Why Rounding Reserve GL? To track small deltas between system-calculated interest and posted amount. ✅ Fair

---

## #132 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #133 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #134 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #135 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Pledging will not affect the growth, Financial goal for which you started, long term plan gets hampered, no cibil requirement, Repay any time, Being in control, Reducing interest, Kevin (Servicing): unpledge request 10% buffer, shortfall, bad sell off experience, change in Sanction limit Mahesh: NBFC license, TATA and Bajaj, Names: Trust Naveen: - No brand val - GST india - NBFC license - Lenders

---

## #136 — DSP Fin Partner Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin: Partner Page # Context RBI requires REs to disclose LSP details in a standard template. While we do the elegant website change, we want to modify only the partners page to be compliant with regulatory requirements. # Requirements As per the RBI guidelines on DLG here, RBI requires REs to disclose the following details. 1. Details of all of its digital lending products and its DLAs; 2. Details of LSPs and the DLAs of the LSPs along with the details of the activities for which they have been engaged for; 3. Particulars of RE’s customer care and internal grievance redressal mechanism; 4. Link to RBI’s Complaint Management System (CMS) and Sachet Portal; 5. Privacy policies and other details as required under extant guidelines of the Reserve Bank. We will display the below details in the current partners page. - Name of LSP - Nature of Service Availed from LSP's - Description of the LSP - DLA of the LSP - Additional Information about the Lender Sample file is attached for reference. [DSPFin Website Disclosures of LSP DLA.odt](DSP%20Fin%20Partner%20Page/DSPFin_Website_Disclosures_of_LSP_DLA.odt) # Benchmarking A few other lenders who display the LSP details are listed below. - InCred: https://incred.com/partnership/ - Piramal : https://www.piramalfinance.com/about-us/lending-partners - BFL: https://www.bajajfinserv.in/bajaj-finserv-partners - ABFL: https://www.adityabirlacapital.com/loans/our-digital-lending-platform-partners

---

## #137 — DSP Fin Website About Us Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin Website: About Us Page **Objective**: To communicate about the values of the company to audience. DSP Finance is a Non-Banking Financial Company (NBFC) backed by the 160+ year legacy of the DSP Group — one of India’s most respected names in financial services. Rooted in trust, innovation, and discipline, we provide customized credit solutions designed to help individuals and businesses unlock value and achieve their financial goals. We are a NBFC with a strong focus on growth through operational excellence and solving problems through technology. **Mission**: To combine deep market expertise with customer-first innovation, ensuring **reliable, transparent, and efficient access to credit** by leveraging technology and robust operational excellence. **Vision**: To be India’s most trusted partner for financial collateral-backed credit, enabling individuals and businesses to unlock value from their investments for exponential financial growth. DSP Finance’s Values. - Customers first - Utmost transparency - People focus - Continuous innovation Key Highlights of DSP finance to be mentioned - AUM of ~2000CR - ~70K customers - 8+ leading partners - AAA rated DSP Finance’s focus is on capital markets led product offerings in the below business lines. - Loan against securities: enabling individuals to leverage their financial assets to get easy access to credit. This page will redirect to the LAS page. - Financial solutions group: providing corporates access to credit by leveraging their assets to get quick access to funds. This page will redirect to the FSG page. DSP Finance works on the below principles. - **Legacy of Trust** – Backed by the DSP Group’s long-standing credibility in Indian finance ecosystem. - **Customer-First Approach** – Transparent processes, no hidden charges, and clear communication. - **Digital-First Experience** – End-to-end paperless solutions with seamless pledge and disbursal. - **Prudent Risk Management** – Strong governance and compliance in line with RBI regulations. - **Expertise & Innovation** – Blend of deep financial knowledge and modern technology to drive deep innovation. DSP has partnered with leading partners to enable customers to leverage their assets. - PhonePe - PayTm - Indmoney - Groww - ETMoney - CRED

---

## #138 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #139 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are

---

## #140 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can