# Current State: Mandate

> Auto-generated from 143 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — SDK for b2b2c SAAS partners
**Status:** Not started | **Last edited:** September 30, 2024 6:06 PM

# SDK for b2b2c SAAS partners ### **Interest Details Management Table** | **Attribute** | **Description** | | --- | --- | | View Interest and Charges | Access current month due interest and charges details with respective statuses. | | Filtering | Filter by mandate status, interest status, and lender name (TATA, BAJAJ). | | Search | Search the interest details table. | | Interest Calculator | Provide tools for calculating interest. | | Pre-defined Messaging | WhatsApp messages based on interest and mandate statuses. | | Pagination | Support pagination with 50 records per page. | ### **Shortfall Management Table** | **Attribute** | **Description** | | | --- | --- | --- | | View Shortfall Amounts | Access details of shortfall amounts and aging information. | | | Sorting and Filtering | Sort by due date and filter by aging and lender name. | | | Search | Search within the shortfall details table. | | | Educational Content | Provide information on what a shortfall means. | | | Pre-defined Messaging | WhatsApp messages for communicating shortfalls to customers. | | | Pagination | Support pagination with 50 records per page. | | ### **Loan Renewals Management Table** | **Attribute** | **Description** | | --- | --- | | View Loan Renewal Details | Access loan renewal information, including statuses and due dates. | | Sorting and Filtering | Filter by lender name and status; sort by customers nearest to renewal dates. | | Search | Search within the loan renewal details. | | Educational Content | Provide information about the benefits and consequences of non-renewal. | | Pre-defined Messaging | WhatsApp messages based on loan status (Active, Expired with/without amounts). | | Pagination | Support pagination with 50 records per page. | ### **General Features Table** | **Feature** | **Description** | | --- | --- | | Tab and Page Deep Linking | Allow access to functionalities via deep links on all platforms (web, Android). | | Dynamic Tab Visibility | Display or hide tabs based on customer counts (hide when count is zero). | | Consistent Data Display | Ensure uniform data presentation across SDK and internal dashboard. | ### **Detailed Customer Information Table** | **Attribute** | **Description** | | --- | --- | | Customer Name | Name of the customer. | | Phone Number | Contact number of the customer. | | Due

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

## #3 — Deferring email capture and verification during on
**Status:** Not started | **Last edited:** September 26, 2025 7:05 PM

**Problem:**
are we solving?**

Currently we are observing a drop-off of 15% on average across Volt Channels at Email verification step in 30 day window (Apr ‘25). As email is asked from the user during initial part of onboarding process, the drop-offs are higher and needs to be reduced to <10% across Volt channels.

![image.png](Deferring%20email%20capture%20and%20verification%20during%20on/image.png)

---

**Solution:**
?**

- We are proposing to defer the email verification step to later stage in the funnel i.e. pre-agreement creation in order to reduce user drop-off at the initial stage.
- The idea for deferring the email verification to post pledge and pre-agreement is based on the intent of the user which would be high during the later stage of the funnel compared to asking for email verification at initial stage where the intent is usually low leading to higher drop-offs here.

---

## #4 — Additional documents upload for Bajaj for AS ES DI
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

## #5 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #6 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #7 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #8 — Multi Drawdown Term Loan LMS Requirements
**Status:** In progress | **Last edited:** October 30, 2025 2:56 PM

**Problem:**
are we solving?**

The existing OD-based Loan Against Mutual Funds (LAMF) product does not align with the repayment expectations and financial behavior of a large segment of customers. These users are more familiar with **structured EMI-based repayment formats**, as seen in personal loans, home loans, and auto loans. As a result, product comprehension, drawdown confidence, and repayment discipline are negatively impacted when only an OD line is offered.

This gap is particularly visible in:

- Low drawdown rates from sanctioned limits
- Confusion around usage-based interest calculation
- Hesit

**Solution:**
?

Product Overview

We propose a **term-loan-style wrapper** on top of the facility construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown.
- **Enabling multiple drawdowns** from the same facility, with flexibility in amount and tenure.
- **Allowing re-borrowing** once limits are replenished through repayment.
- **Positioning the product clearly as “term loans with flexibility”**

This hybrid approach is designed to increase adoption, improve credit utilization, and grow customer LTV.

**Product Technical Construct**

A **line-backed, multi-drawdown term loan**, where:

- **Both loan and tranche constructs are exposed to the LSP**.
- DSP manages the **loan** as the credit container; **

---

## #9 — Master collections PRD (NBFC)
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

## #10 — Integrated Sales tool
**Status:** In progress | **Last edited:** October 14, 2024 2:04 PM

**Problem:**
are we solving?**

Support systems face significant challenges in managing multi-channel customer queries across B2C, B2B2C, and partner channels. These issues include fragmented communication, difficulty handling diverse customer types, inadequate issue categorization, lack of centralized ticketing, ineffective SLA tracking, absence of real-time performance dashboards, fragmented reporting, delayed follow-ups, communication errors, and no customer feedback mechanisms. These problems lead to decreased customer satisfaction, poor service levels, and reduced operational efficiency.

- We don’t h

**Solution:**
? (potential)**

Implement a centralized, multi-channel support system that unifies all customer interaction channels (email, chat, phone, WhatsApp) into a single platform. This system should support segmentation for B2C, B2B2C, and partner customers, incorporate automated ticketing and routing based on issue complexity and customer type, enforce SLA tracking, provide real-time performance dashboards, and include integrated feedback mechanisms.

- INBOUND
    - Calls
        - Call are routed or provided by Exotell
        - Received calls
            
            
            | Type | Instance | percentage |
            | --- | --- | --- |
            | Incoming | 1595 | 26.14% |
            | Outgoing | 1407 | 23.06% |
            | Missed | 2950 | 48.35% |
            | Rejected | 132 |

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

## #12 — Mandate Set up optimisation - Error Messaging + Ne
**Status:** Ready for Tech | **Last edited:** November 8, 2024 12:55 PM

**Problem:**
are we solving?**

Setting a mandate is an important step in our loan application process. However only 30-40% of our users are able to set up a mandate successfully in their first attempt.

Other users end up either dropping or relying on our RMs to assist them with the journeys. RMs do not have clarity on the kind of errors the users are facing and what is the optimal way to help the user in completing the process.

We currently use Digio for setting up e-mandates for the loan application journey of BFL and Tata’s own e-mandate flow for Tata’s application journey.

Currently we solve this pr

**Solution:**
?**

We intend to solve this issue with a three pronged approach:

- Communicating and enabling users to identify and solve issues by themselves by providing contextual messaging and CTAs
- Sharing exact issues on Retool against mandate set up step for ops team to assist the user better and not rely on tech team for RCA

---

## #13 — Father’s name validation removal
**Status:** Not started | **Last edited:** November 30, 2025 12:18 PM

**Problem:**
are we solving?**

LSPs are currently seeing high rejection rates at the **Submit Opportunity** stage due to mismatches between the user-entered *father’s name* and the value returned from KYC.

Since the RBI’s KYC Master Directions do **not** mandate verification of the father’s name—and it is required only for CKYC reporting—strict validation is unnecessary. Most regulated entities rely on customer-provided details with minimal checks, which aligns with our revised approach.

---

**Solution:**
?**

---

## #14 — NBFC Virtual Accounts for Repayments (Alignment)
**Status:** In progress | **Last edited:** November 27, 2024 4:59 PM

**Problem:**
are we solving?**

Currently, we are accepting repayments from customers through payment gateway for adhoc repayments and NACH for interest repayments. While this will cater to customers who are on app/website, there are multiple scenarios where a customer might want to repayment directly to DSP’s account.

The problems can be further distilled into.

- We don’t want to expose our underlying account to customers to minimize operational overheads as well as risk of account getting impacted
- We want to handle large ticket repayments from customers more seamless, especially for MFD channels wher

**Solution:**
?**

---

## #15 — NLP-736 Timestamp value is not captured with hh mm
**Status:** Not started | **Last edited:** November 19, 2024 7:41 AM

# NLP-736: Timestamp value is not captured with hh:mm:ss due to which the default value 05:30:00 is shown in the UI Command centre search result pages: Client creation date (client search) Expiry date (loan search) Bureau pull date (client details risk section) AML pull date (client details risk section) Mandate expiry date (loan details section) Expiry date (is in small case) KYC expiry date is comming as invalid date Completed on (repayment detail is coming as invalid detail)

---

## #16 — Foreclosure handling for DSP
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

## #17 — External reporting requirements
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

## #18 — White-labelled Redirection Journey for B2B Partner
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

## #19 — MFD Tier & Performance Data Activity Passing in LS
**Status:** Pending Review | **Last edited:** November 10, 2025 6:43 PM

**Problem:**
are we solving?**

RMs lack a unified and actionable view of Mutual Fund Distributor (MFD) engagement, performance, and calling priorities within LSQ.

Current lead-level visibility doesn’t help RMs prioritise their outreach or track monthly conversion performance efficiently.

We are solving for:

- Fragmented data visibility (AUM, tier, last engagement, conversion, pipeline, MFD referred)
- Manual tracking of RM disposition and calling data via google sheets
- Lack of month-on-month visibility into MFD productivity and performance
- No structured, real-time reporting for RM calling effective

---

## #20 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #21 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #22 — [Platform] Callbacks for LSP APIs for core servici
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

## #23 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #24 — Phase 0 LTV Tenure Update_LOS
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

## #25 — Handling LOS Application Rejections
**Status:** Not started | **Last edited:** May 25, 2026 12:22 PM

**Problem:**
are we solving?**

Currently in LOS , several business-critical validation checks are performed — such as client deduplication, MNRL checks, and AML/PEP screenings. 

However when any of these checks fail, the system surfaces a generic ‘declined’  error message (”Something went wrong”) to the user. The root cause is that the backend does not propagate the specific error code or reason to the frontend, so the frontend cannot render contextual, actionable error screens.

---

**Solution:**
?**

---

## #26 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #27 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #28 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #29 — Term Loan LOS requirements
**Status:** In progress | **Last edited:** May 14, 2026 10:50 AM

**Problem:**
are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Poor use of the product as a one-time loan:** Even when users opt in, they typically draw down only once and never return, leading to poor utilization of the approved credit limit.
- **Lack of lifecycle borrowing behavior:** Users do not engage in multiple drawdowns or reborrowing after repayment, resulting in limited customer lifetime value (LTV).
- **Ineffective product positioning:** The existing product f

**Solution:**
?**

Product Overview

We propose a **term-loan-style wrapper** on top of the line construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown.
- **Enabling multiple drawdowns** from the same line, with flexibility in amount and tenure.
- **Allowing re-borrowing** once limits are replenished through repayment.
- **Positioning the product clearly as “term loans with flexibility”**

This hybrid approach is designed to increase adoption, improve credit line utilization, and grow customer LTV.

**Product Technical Construct**

A **line-backed, multi-drawdown term loan**, where:

- **Both loan and tranche constructs are exposed to the LSP**.
- DSP manages the **loan** as the credit container; **e

---

## #30 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #31 — DSP PhonePe PG Integration for PhonePe
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

## #32 — Mandate limit change
**Status:** Not started | **Last edited:** March 5, 2025 3:41 PM

# Mandate limit change # Credit Limit Increase Analysis (Excluding <10K Initial Credit Limit) Based on the analysis of 10,467 valid records with initial credit limits of 10K or greater, here's the comprehensive breakdown: ## Applications by Initial Credit Limit Range and Percentage Increase | Initial Credit Limit | 0-400% | 400%-600% | 600%-800% | 800%-1000% | 1000%+ | Total | | --- | --- | --- | --- | --- | --- | --- | | 10K-25K | 119 | 13 | 8 | 2 | 16 | 158 | | 25K-1L | 2,361 | 78 | 24 | 25 | 84 | 2,572 | | 1L-5L | 4,393 | 81 | 51 | 27 | 41 | 4,593 | | 5L-25L | 2,432 | 42 | 17 | 8 | 18 | 2,517 | | 25L+ | 620 | 6 | 1 | 0 | 0 | 627 | | **Total** | 9,925 | 220 | 101 | 62 | 159 | 10,467 | ## Percentage Increase Distribution | Range | Count | Percentage | | --- | --- | --- | | 0-100% | 7,858 | 75.07% | | 100%-200% | 1,383 | 13.21% | | 200%-300% | 471 | 4.50% | | 300%-400% | 213 | 2.03% | | 400%-500% | 133 | 1.27% | | 500%-600% | 87 | 0.83% | | 600%-700% | 57 | 0.54% | | 700%-800% | 44 | 0.42% | | 800%-900% | 29 | 0.28% | | 900%-1000% | 33 | 0.32% | | 1000%-1500% | 58 | 0.55% | | 1500%-2000% | 28 | 0.27% | | 2000%+ | 73 | 0.70% | ## Applications with 400%+ Credit Limit Increase by Range | Initial Credit Limit | Count | % of Range | | --- | --- | --- | | 10K-25K | 39 | 24.68% | | 25K-1L | 211 | 8.20% | | 1L-5L | 200 | 4.35% | | 5L-25L | 85 | 3.38% | | 25L+ | 7 | 1.12% | | **Total** | 542 | 5.18% | ## Cumulative Distribution | Up to | Count | Percentage | | --- | --- | --- | | 100% | 7,858 | 75.07% | | 200% | 9,241 | 88.29% | | 300% | 9,712 | 92.79% | | 400% | 9,925 | 94.82% | | 500% | 10,058 | 96.09% | | 600% |

---

## #33 — [Platform] Foreclosure handling and enhancement
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

## #34 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** March 24, 2026 11:57 AM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

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

## #36 — [Volt LOS] KYC optimisations
**Status:** Not started | **Last edited:** March 19, 2025 12:54 PM

**Problem:**
are we solving?**

Currently for customers to complete KYC on Volt Money, across lenders we only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL P

**Solution:**
?**

TL;DR 

- Introduce multiple methods of KYC for DSP Fin customers.
- Build an orchestration among these KYC methods for the customer. In case customer is unable to complete KYC through one method because of user issues or downtime, they should be redirected to the fallback method(s) of KYC.

What counts as KYC for our customer?

- Compliance (CDD) requirements
    
    Obtain the following - 
    
    1. Aadhaar number 
        1. Proof of possession of Aadhaar(current), OVD, or equivalent e-document. Will have to do Digital KYC in this case. 
        2. the KYC Identifier with an explicit consent to download records from CKYCR
    2. the Permanent Account Number or the equivalent e-document thereof. This needs to be verified from the issuing authority. 
- POI/POA requirements
    - P

---

## #37 — Improving Mandate Conversions
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

## #39 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #40 — DSP UPI Autopay Integration for NBFC
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

## #41 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #42 — Tata Video KYC Integration V0
**Status:** In progress | **Last edited:** July 3, 2025 10:08 AM

**Problem:**
are we solving?**

Tata Capital mandated the VKYC process to be completed for each new customer from 1st April 2025. With larger vision and deeper potential partnerships in the horizon, restarting the business with Tata Capital is required.

To do so, we need to implement Tata  Capital’s VKYC in our journey flow.

---

**Solution:**
?**

Implementation of VKYC will cause significant rise in the drop-offs. With alignment from Tata, we can open the account without the customer completing the VKYC but it is mandatory for the customer to complete VKYC before raising a disbursement request.

For the initial launch (and till we observe stabilized funnels) we would be involving our Support team to help customers before and after (in cases of rejection/incomplete VKYC) with clear instructions and hand holding.

This is for the V0 launch only.

 

Note:

Tata’s Business Hour: 9AM - 6pm

[Activation: LSQ Task Creation](Tata%20Video%20KYC%20Integration%20V0/Activation%20LSQ%20Task%20Creation%20224e8d3af13a80c982dacebab3d9b6b0.md)

---

## #43 — [DSP] Mandate enhancements Handling of charge coll
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

## #44 — Implementing UTR dedupe for repayment postings
**Status:** Pending Review | **Last edited:** July 14, 2025 3:52 PM

**Problem:**
are we solving?**

---

- We currently do not perform a deduplication (dedupe) check on incoming repayment requests from Lending Service Providers (LSPs), which poses a risk of **duplicate repayment postings**. This issue becomes critical as we scale with more LSPs like PayTM and PhonePe initiating repayments through their own Payment Gateways (PGs).
- Additional complexity arises because **UTR (Unique Transaction Reference) numbers are only unique at the bank level**, not globally. Hence, simply using UTR for deduplication is not sufficient and can lead to false positives or missed duplicates

**Solution:**
?**

---

## #45 — Axis bank e-collect API integration for virtual ac
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

## #46 — [Platform] Mandate collection BRE optimisation
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

## #47 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #48 — [Volt LSP] DSP QC rejection handling
**Status:** In progress | **Last edited:** January 3, 2025 4:44 PM

**Problem:**
are we solving?**

Post an application is submitted by the LSP, DSP checks data and policy adherence sanity of the customer application on the QC (Quality check) step. 

For applications rejected in QC the current SOP for the customer requires customer to be manually moved back to the needed step in the application. This is non ideal because of the-

1. High effort for tech ops to move back the customer. 
2. High TAT for the customer to get unblocked. 

---

**Solution:**
?**

---

## #49 — CKYC Upload for DSP
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

## #50 — [Platform LSP] All transactions requirements
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

## #51 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #52 — Yes bank e-collect API integration for virtual acc
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

## #53 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #54 — Repayment next step
**Status:** Not started | **Last edited:** January 17, 2025 12:25 PM

# Repayment next step # Loan Repayment System Redesign ### Current Hypotheses 1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected. 2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. ## JTBD problem list ### Job Story 1: Clear Shortfall "When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall." **Current Problems:** - The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest - Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront - Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts ### Job Story 2: Pay Interest "When I need to pay my interest, I want to understand why I need to pay any additional charges" **Current Problems:** - In TATA, users see interest amounts increase in months with additional charges - The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained - Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments - These charges and interest come under monthly dues as a concept ### Job Story 3: Make Principal Repayment "When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision." **Current Problems:** - For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate. - The principal repayment screen doesn't explain that the payment will first go towards interest and charges - Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users. - Users are not aware that principal is being repaid early and isn’t due for 3 years. ### Job Story 4: Understand Payment Structure "When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system." **Current Problems:** - The home

---

## #55 — [Email Template] Decoupling of Lodgement and Agree
**Status:** Not started | **Last edited:** January 15, 2025 4:44 PM

**Problem:**
are we solving?**

—> In case of Line Enhancement, the flow is as follows: KYC—>Bank —> pledge —> Agreement

- Two separate communications through email is sent to BAJAJ through email, one after the pledge step and the other after Agreement step.
- Email format sent after the Pledge step(no change in Email format):

<aside>
💡

Hi,

Customer has pledged additional securities. Please refer to the attached file for the lodgement of the MF pledged.

LAN No. : V402ALAS00171774

Expecting confirmation with IVR file (PDF)

MF_Pledged_Portfolio.csv

</aside>

- New Email format sent after the Agreemen

**Solution:**
?**

---

## #56 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #57 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #58 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #59 — Interest, shortfall, renewal table on partner dash
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

## #60 — Admin action to update mandate status & interest
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

## #61 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #62 — DSP Bank Account Update and Mandate Re-Registratio
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

## #63 — Handle physical mandate cases for BAJAJ
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

## #64 — Interest feature handling for TCL
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

## #65 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #66 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #67 — Mandate registration post loan
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We need to allow user to update the mandate post loan application completion

Below are the reason due to which we need to ask or allow user to add new mandate or update mandate details

TCL:

- Registration unsuccessful after confirmation
- User cancelled mandate
- Bank account blocked/frozen
- Mandate registered with wrong details like mandate limit amount
- User want to change Bank and mandate

BFL:

- Everything in TCL
- User opted for physical and mandate registration rejection/unsuccessful

DSP: 

- Everything in TCL and BFL
- User skipped the mandate step

Mandate pre

**Solution:**
?**

---

## #68 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #69 — Volt Mandate re-registration Post loan
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

## #70 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #71 — [Platform] Enabling alternate mandate registration
**Status:** Done | **Last edited:** February 1, 2025 7:49 PM

**Problem:**
are we solving?**

As a part of the application flow, users have to register a mandate. While it is not mandatory, it is convenient for both the lender as well as the user to do so.

- **Convenient EMI Payments**: A mandate ensures automatic deduction of EMIs from the borrower's account, reducing the risk of missed payments.
- **Assurance for the Lender**: It provides the lender a reliable mechanism for repayment.

The mandate registration process requires the user to authenticate the registration on their bank account, NPCI allows the user to do so via three methods:

1. E-NACH 
    1. Debit 

**Solution:**
?**

We will be utilising Digio’s flow to initiate mandate registration flow for the user/LSP. LSP will be able to control which registration method is to be used in the mandate registration request.

LSP be able to pass the preferred method of mandate set up to the request post which the request will go through a whitelist. 

Each LSP will have the methods of mandate registration whitelisted for them (If they can use E-NACH/ Aadhaar E-sign/ Physical NACH) for the user mapping with source code.

Fenix will also share a bank whitelist with the LSPs for them to able to gauge which bank account is activated and available for the corresponding registration method.

Basis the selection, Fenix will invoke the specfic flow for the LSP by modifying a request parameter for Digio

<aside>
💡

Importa

---

## #72 — Update user details (for TCL, BFL, DSP)
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

## #73 — [Platform] Mandate presentation request optimisati
**Status:** Done | **Last edited:** December 31, 2024 11:49 AM

**Problem:**
are we solving?**

We are solving three problems via this enhancement:

- Mandate presentation UTR entries for the destination bank (User) are very general. Since the amount is deducted automatically from the user’s bank account, it often gets difficult to track why the amount was deducted (across services and products) while analysing bank account statements.
- Currently reconciliation for mandate presentations is built on top of item ids (shared by Digio) to us in response and also passed as a parameter in the report.

---

**Solution:**
?**

P1:

- We will be passing custom narrations in the user’s bank account statement
DSP Finance NACH debit for LAN: FXLAN534324

and UTR in the user’s loan account statement:
Loan repayment received against sale of security: IN9876543210 for account number: FXLAN6789012 with Ref ID:

P2:
We will be passing enrichment values in the presentation request for Digio to assist reconciliation with operations team

---

## #74 — [Platform] Risk report
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

## #75 — Figma file organisation
**Status:** Not started | **Last edited:** December 2, 2024 3:59 PM

**Problem:**
are we solving?**

- Searching for updated files of features and different stages of the journey
- Get visibility on how each stage is handled for different lender
- Easy visibility on version history, compliance updates etc. done in the past - need to view in one place
- Allow storing secondary flows like: error handling, drop-off flows etc

---

## #76 — Renewal applications in the LSQ
**Status:** Not started | **Last edited:** December 17, 2024 7:16 PM

# Renewal applications in the LSQ # Customer Lead Renewal Flow ## Customer lead and opportunity creation steps for Renewal - Create renewal opportunity using lead create and update API - Save renewal opportunity id - Post opportunity update - Post activity on opportunity ## Case Scenarios ### Case 1: Customer initiating renewal through MFC Landing page - Create renewal opportunity if existing loan is near maturity - When user clicks on "Renew loan" update opportunity stage to renewal_initiated - If renewal opportunity already exists, post activity for existing opportunity ### Case 2: Customer initiating renewal through Android/iOS app When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Post "Renewal initiated" activity - Update portfolio verification status ### Case 3: Customer initiating renewal through Web App When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Update portfolio verification status - Post activity for renewal journey progress ### Case 4: System-initiated renewal notification - System identifies loans approaching maturity (30 days before) - Create renewal opportunity if eligible - Send notification to customer - Track customer response through activities ## Renewal Lead/Opportunity Attributes | Lead field name | Data type | Lead Schema name | Opportunity Schema name | Comment | Status | | --- | --- | --- | --- | --- | --- | | Original Loan ID | Text | mx_Original_Loan_Id | mx_Custom_70 | Required | sending | | Renewal Type | Dropdown | mx_Renewal_Type | mx_Custom_71 | Standard/Enhanced | sending | | Original Maturity Date | Date | mx_Original_Maturity_Date | mx_Custom_72 | Required | sending | | Portfolio Re-verification | Boolean | mx_Portfolio_Verified | mx_Custom_73 | Required | sending | | Renewal Amount | Number | mx_Renewal_Amount | mx_Custom_74 | Required | sending | | Original Loan Amount | Number | mx_Original_Loan_Amount | mx_Custom_75 | Required | sending | | Days to Maturity | Number | mx_Days_To_Maturity | mx_Custom_76 | System Calculated | sending | | Renewal Eligibility | Boolean | mx_Renewal_Eligible | mx_Custom_77 | System Calculated | sending | ## Renewal Stage Progression ### Active Stages - Renewal_Eligible - Renewal_Initiated - Portfolio_Verification - Documentation_Update - Agreement_Signing - Mandate_Setup - Renewal_Processed - Renewal_Complete ## Custom Activities for Renewal |

---

## #77 — Lead stage handling on LSQ
**Status:** Not started | **Last edited:** December 13, 2024 11:58 AM

# Lead stage handling on LSQ Lead stages in LSQ Initial Registration Stages: 1. Unregistered 2. Registered Portfolio Stages: 3. Portfolio Fetch 4. Portfolio Fetch KFIN 5. Portfolio Fetch CAMS 6. Portfolio Pledge 7. Portfolio Pledge KFIN 8. Portfolio Pledge CAMS Application Processing Stages: 9. KYC Verification 10. Sign Agreement 11. Link bank account 12. Setup Mandate 13. Verify Photo 14. Application Submitted 15. Loan Created 16. Empaneled Final Status Stages: 17. Partially activated 18. Activated 19. Closed

---

## #78 — Single drawdown Term Loan LMS Requirements
**Status:** In progress | **Last edited:** August 9, 2025 11:23 AM

**Problem:**
are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Lack of lifecycle borrowing behaviour:** Users do not engage in re-borrowing after repayment, resulting in limited customer lifetime value (LTV).

---

**Solution:**
?**

Product Overview

We propose a vanilla **term-loan-style wrapper** on top of the line construct to match user expectations and drive better usage. The solution involves:

- **Offering a familiar term-loan onboarding flow** for the first drawdown
- **Allowing re-borrowing** once limits are replenished through repayment.

This hybrid approach is designed to increase adoption and grow customer LTV.

**Product Technical Construct**

A **line-backed, single-drawdown term loan**, where:

- DSP creates and manages the line & loan internally for eligibility and lifecycle logic.
- **Only the loan construct is exposed to the LSP**, appearing as a standard term loan.
- Only one single **active** loan drawdown is supported at a time in this construct ie loan = line at any pt in time
- Future draw

---

## #79 — [DSP] Dues collection comms
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

## #80 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #81 — [DSP] KYC v2 (including CKYC)
**Status:** Ready for Tech | **Last edited:** August 13, 2025 12:55 PM

**Problem:**
are we solving?**

Currently for customers to complete KYC on DSP, they only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL PIN to complete KYC o

**Solution:**
?**

---

## #82 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #83 — Bank account Mandate update
**Status:** Pending Review | **Last edited:** April 7, 2025 2:42 PM

**Problem:**
are we solving?**

- Our operations team has to spend a lot of bandwidth for co-ordinating with lender’s APIs to get users’ bank account updated.
- It’s a really bad experience for the users to get their bank account updated as they are required to share various documents, formal email request to Volt & Lender Ops team.
- Number of update requests analysis -
    
    
    | Update requests  | Number  |
    | --- | --- |
    | Bank account  | 30 |
    | Mandate re-registration | 8 |

---

**Solution:**
?**

---

## #84 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #85 — MNRL Compliance Validation Integration
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

## #86 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #87 — CKYC Comms for Regulatory Compliance
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

## #88 — KYC & Mandate Workflow PRD
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

## #89 — Admin tool migration to Appsmith
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

## #90 — UPI Autopay
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

## #91 — Ai optimisation in current design workflow
**Status:** Unknown | **Last edited:** Unknown

# Ai optimisation in current design workflow - Prompt SO right now the design process at volt **AI is used by UX pros as a thought partner and reviewer** - Resources https://www.userinterviews.com/ai-in-ux-research-report There is around following major steps when it comes to designing - Problem identification - Prioritisation - Benchmarking - Building a user flow - Working on wireframes - Final design Methodologies for problem identification - User Interviews - Surveys - Synthesis of data - Requirements/Insights from the data Benchmarking - Exploration with competitors - Exploration of layout, components, illustrations Building user flow - User journey map - Information architecture - Technical capabilities - Information per screen and hierarchy - Scoping based on the existing designs Working on wireframes - Visual hierarchy - Communication clarity - Navigation - Need to evaluate screens based on :Navigation Ease, Information Clarity, Error Recovery Final designs - Emotional Triggers, Actionability, Consistency, - Illustration design - Interaction with motion --- ## Problem Identification ### User Research - **Automated data analysis** : Transcription, analysis, and synthesis of user research data. - **Sentiment analysis** to identify pain points from user feedback - **Pattern recognition** to spot recurring issues that humans might miss - **Natural language processing** to extract insights from unstructured user comments ### Desk Research - Scanning research papers on psychology eg. Indians’ behaviour in 2020, market trends Eg. How genZ interacts with money, etc, Understanding fintech domain Eg. Understanding how NACH and UPI Autopay works oversimplified. - Tools https://www.perplexity.ai/ https://consensus.app/ https://elicit.com/ ### Process - Designer/PM will take user interviews with the ‣ using ai to generate questionnaire based on the problem statement at hand. - Ai will help to synthesise the data analysis based on the user interview. # Current design workflow [https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system) # Optimized AI workflow 1. Qualitative data collection - Questionnaire for Surveys and User interviews - Desk research - Tools: Perplexity - Dashboard for CS Tickets - How to build this. ### **1. Centralize All Ticket Data** Export data from Zendesk, WhatsApp, etc. into a single table or sheet. Include fields like user message, date, channel, and status for context. --- ### **2. Analyze with AI (GPT or ML Tools)** Use GPT to extract pain points, tag themes, and identify patterns. Alternatively, use BERTopic or clustering models to detect recurring issues. --- ### **3. Summarize & Visualize Insights** Group findings by theme, volume, and sentiment in a dashboard or table. Highlight

---

## #92 — Enhance limit Research
**Status:** Unknown | **Last edited:** Unknown

# Enhance limit Research ### Objective 1. **User Motivation:** Why do people enhance their limit? 2. **Mental Models** How do they currently think about credit lines? - Currently our users think about credit line like a personal loan, They only choose increase their credit limit if they are in need. - What we can work towards is building the mindset like a credit card where increased credit limit is something people go for even when they don’t feel the need for it. - Folks tried to 3. **Context of Use** When do they increase limit? - After a withdrawal (they see low balance) - Utilisation > 70% - If they see the value of their MF has increased. . . 4. **Flow Drop Offs** Why do users abandon this? - Users who dropped out usually didn’t get the limit they wanted - They also were ineligible for the loan since there is a 10K limit Unclear next steps. Lack of feedback Screen fatigue 5. **Purpose & Value** Why does this feature matter to users? > It’s a fast, low-effort way to access more cash without applying for a new loan. KYC, Mandate and Agreement not required (If new total limit is below SL) > --- ### Feedback from users - No one complained of any difficulty, lack of information for dropping off. - When asked “What’s one thing stopping you from increasing your limit right now?” - The answer always is they don’t have the need for it. - Minimum 10K being the reason for drop-off. --- ### Segments of Users and Questionnaire 1. **Repeat Users (Used Top-Up More Than Once- Ideal Users)** - Why did you “Enhance Limit”? - What made you come back and do it again? - How easy or difficult was it to find the increase limit option? - Was anything unclear or unexpected in your experience? - Hindi - Aapne pehli baar limit enhance kyun kiya tha? - Aapne phir se kyun kiya? - Pura process aapko kaisa laga — easy ya confusing? - Koi ek step jo aapko helpful ya clear laga? - Aapko paise milne mein kitna time laga tha? - Kya koi cheez aisi thi jo alag thi ya samajh nahi aayi? - Aapko is process pe trust kyun hua? - Aapne jo extra limit mili uska use kaha kiya? - Kya kuch aisa hai jo aur better banaya ja sakta hai?

---

## #93 — Mandate update for better conversion
**Status:** Not started | **Last edited:** Unknown

# Mandate update for better conversion Charter: NBFC Pod Priority: P1 # Context Need to work through mandate flows all three and improve conversion rates for the same. This is for the DSP DSK # Process - [x] Understand mandate processes and types - [ ] Benchmarking mandate flows from others - [ ] Numbers on current conversion rates --- - [ ] Understanding gaps in the current flows - [ ] Flow exploration and alignment - [ ] Wireframes - [ ] Design # Figma

---

## #94 — APIs
**Status:** ** Retrieves the status of the KYC verification. | **Last edited:** Unknown

# APIs **Explanation of the API Sequence in the Volt Money Application Flow** Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience. --- ### **Overview** The Volt Money application process involves several key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail. --- ### **1. Login** - **API Used:** *Custom Authentication API (Not listed in the provided APIs)* - **Functionality:** - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone. - **Notes:** - This step establishes a secure session for the user. - While not specified in the provided API list, we use a standard authentication service to handle this process. --- ### **2. PAN Verification** - **API Used:** - `POST /app/borrower/application/kyc/pan/panVerify` - **Partner:** Decentro (facilitates connection to NSDL) - **Functionality:** - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid. - **Data Retrieval:** Fetches the full name associated with the PAN. - **Notes:** - Essential for KYC compliance and identity verification. - Helps prevent fraudulent applications. --- ### **3. Fetch Folio** - **APIs Used:** - `POST /app/borrower/application/fetch/init/otp/v3` - `POST /app/borrower/application/fetch/authCAS/v2` - **Partners:** Cams, KFintech, MF Central - **Functionality:** - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio. - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details. - **Notes:** - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets. - This data is used later in the asset pledge and eligibility assessment. --- ### **4. Eligibility Assessment and Lender Assignment** - **API Used:** - `POST /app/borrower/application/credit/profile/evaluate` - **Partner:** Internal Business Rule Engine (BRE) - **Functionality:** - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria. - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based

---

## #95 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #96 — flows api
**Status:** Unknown | **Last edited:** Unknown

# flows api 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** 1. **Fetch Folio-** 2. **Eligibility Assessment and Lender Assignment** 3. **KYC Verification** 4. **Bank Account Verification** 5. **Mandate Setting** 6. **Asset Pledge** 7. **KFS and Documentation** 8. **Loan Agreement Execution**

---

## #97 — LaMF application journey
**Status:** Unknown | **Last edited:** Unknown

# LaMF application journey [APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md) [API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md) [flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md) [Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md) The journey to create a loan against mf is as follows - login - user logs in using mobile number and otp validation - PAN verification - user enter DOB and PAN to validate pan , API - decentro - Fetch folio - we ping Cams/KFin to get the folio for the user - We ping them manually - we have option of gettign both from MF central - One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists - Folio have ISIN , NAV etc details - We assign the customer basis BRE to either Bajaj ot TATA capital - KYC of the customer aadhar - API is diifetent for tata and bajaj - Bank account verification - Mandate setting - Logement - KFS and docuemnttation Support I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table. [Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv) | Step | improvements | Description | Partner/Service | API Name | | | --- | --- | --- | --- | --- | --- | | Login | | User logs in using mobile number and OTP validation | | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) | | | Verify OTP | | | | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/ | | | user details | | | | https://api.staging.voltmoney.in/app/borrower/user | | | Email verification | | | Google sso | https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com | | | | | | Email / manual | | | | | | | | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) | | | | | | | | | | PAN Verification | | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API | | | Fetch Folio | | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API | | | Run BRE and Calculate Eligible Limits | | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system | | | | Assign Lender | | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system | | | | KYC Verification | | KYC of the customer with different APIs for Bajaj and TATA Capital

---

## #98 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #99 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #100 — Dishonour charge enhancement
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

## #101 — Enhancing Collections Efficiency Through Mid-Month
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #102 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #103 — LSP Presentation enhancement for externally regist
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, all mandate registrations for DSP Finance are done internally through our TSP (Digio) integration. As we onboard LSP partners like Smallcase, there is a need for them to independently initiate mandate registration flows while still maintaining DSP Finance’s sponsor bank credentials.

This enhancement allows Smallcase to register mandates on behalf of DSP Finance, improving the customer experience by reducing redirects and enabling a native flow within the LSP app.

However, since mandates will be registered from the partner’s Digio account, DSP will not have direc

**Solution:**
?**

We will extend mandate registration capability to Smallcase via Digio by sharing DSP’s sponsor bank configuration. Smallcase will have restricted access — limited only to mandate registration (not cancellation or presentation).

Post successful registration, Smallcase will call submitMandateDetails API to push the mandate details to DSP for internal record-keeping and tagging.

During future mandate presentations, if the mandate is tagged as external, DSP will additionally pass bank_account and ifsc in the presentation request since these details are unavailable within DSP’s Digio account context.

---

## #104 — PPSL UPI mandate presentation
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

## #105 — Product note Excess refund Colending
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

## #106 — Product note Virtual account handling for Colendin
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

## #107 — Razorpay SDK enhancement for Colending
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

## #108 — [Platform] Decoupling of dishonour fees with manda
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

## #109 — [Platform] Foreclosure handling to support Volt fo
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

## #110 — [Platform] Mandate collection enhancement
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

## #111 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #112 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #113 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #114 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #115 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #116 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #117 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #118 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #119 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #120 — Analytics Requirement Mandate issues
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Mandate issues Query 1: (errors consolidation, distributed by providor) ```jsx select 'tata' as providor,emandate_error_message as error_message,count(distinct(application_id)) as unique_cases from (select application_id, created_date_time, bank_account_number, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) >= date_add('day', -6, current_date) and mandate_status not in ('In Progress','Finished')) t group by emandate_error_message union all select 'digio' as providor,npci_error as error_message,count(distinct(application_id)) as unique_cases from (select application_id, bank_account_number, created_date_time, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, umrn, case when CAST(JSON_Extract(digio_mandate_response, '$.npci_auth_failed_error') AS VARCHAR) != 'null' then JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') else JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') end as npci_error , CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) >= date_add('day', -6, current_date) and umrn is null and digio_mandate_status!='EXPIRED' and CAST(JSON_Extract(digio_mandate_response, '$.state') AS VARCHAR) != 'expired') t group by npci_error order by 3 desc ``` Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #121 — Analytics Requirement Name verification (TCL)
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Name verification (TCL) Query 1: (errors consolidation, distributed by providor) Total applications initiated (unique) Total Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #122 — Digio Volt Exploring mandate authorisation flows
**Status:** Unknown | **Last edited:** Unknown

# Digio <> Volt: Exploring mandate authorisation flows What are the different ways via which we can authorise mandates? Debit Card Net Banking Aadhaar OTP Bank OTP - Bank level integrations Some users dont have net banking and aadhaar card, how can we create digital journeys for them for easy mandate set ups? Does digio support direct bank otp based mandate set ups? is it for all banks or specific banks? if yes can we get a list of the supported banks? Check internally bank level requests, how many of our requests can be eased via direct integrations? If not how does one do that? does She have context

---

## #123 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

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

## #125 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #126 — Term Loan Excess Handling and Refund
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

## #127 — Term Loan Mandate Repayments
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

## #128 — Term Loan Manual Repayments(PG)
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

## #129 — Term Loan Manual Repayments(VA)
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

## #131 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #132 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #133 — Webhook Handling Flow
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?

Currently, during UPI mandate setup via Digio, we incorrectly treat Auth webhooks (Auth Success / Auth Failure) as the final mandate status. This causes:

- False positives (e.g., Auth Success but later Auto Debit(Rs 1) fails).
- Customers setting mandate on a different bank account, than the registered one, move ahead in the journey but mandate gets revoked later due to TPV failure.
- Inconsistent mandate states that require manual Ops intervention.

---

**Solution:**
?

---

## #134 — PhonePe UPI Autopay Evaluation
**Status:** Unknown | **Last edited:** Unknown

# PhonePe UPI Autopay Evaluation API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization) **List of APIs** 1. Authorization API 1. This API is used to generate the auth token to access the rest of the APIs. 2. The auth token is valid for 1 hour. 3. If the auth token is re-generated within 1 hour, the old token will not expire. - Request ```json curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'client_id=' \ --data-urlencode 'client_version=1' \ --data-urlencode 'client_secret=' \ --data-urlencode 'grant_type=' ``` - Response ```json { "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "expires_in": 3600, "issued_at": 1738669002, "expires_at": 1738672602, "session_expires_at": 1738672602, "token_type": "O-Bearer" } ``` 1. Validate VPA API 1. This API is used to validate the user's VPA. 2. Returns, valid & name of the user. 3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts. - Request ```json { "type": "VPA", "vpa": "nihaltest1@ybl" } ``` - Response ```json { "valid": true, "name": "<Name of User>" } ``` 1. Intent 1. This API is used to create the intent link for autopay. 2. amount - this parameter defines the amount to be deducted at the time of registration. 3. maxAmount - this amount defines the maximum amount the mandate is registering for. 4. Android - Generic intent URI will be provided. 5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app. - Request ```json { "merchantOrderId": "MOTEST5", "amount": 300, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST5", "authWorkflowType": "TRANSACTION", "amountType": "FIXED", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_INTENT", "targetApp": "com.phonepe.app" } }, "deviceContext" : { "deviceOS" : "ANDROID" } } ``` - Response ```json { "orderId": "OMO2502041725138147510236", "state": "PENDING", "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738" } ``` 1. Collect 1. This API is used to send the collect request for mandate setup. 2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported. - Request Body ```json { "merchantOrderId": "MOTEST6", "amount": 200, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST6", "authWorkflowType": "TRANSACTION", "amountType": "VARIABLE", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_COLLECT", "details": { "type": "VPA", "vpa": "nihaltest1@ybl" } } } } ``` - Response ```json { "orderId": "OMO2502041727154877510267", "state": "PENDING" } ``` 1.

---

## #135 — Ok, but 10 lac show why ”
**Status:** Pending development | **Last edited:** Unknown

# """Ok, but 10 lac show why?""” Classification: Mandate amount Notes: User was unsure as loan amount was different than mandate amount PRD/Solution mapping: PRD ready Platform: Wati Reference Link/ID: 919156743753 Status: Pending development

---

## #136 — User had to create 3 mandates in a span of 3 month
**Status:** Solutioning pending | **Last edited:** Unknown

# User had to create 3 mandates in a span of 3 months Classification: Mandate Reuse Notes: Re use mandate for users so that they dont have to recreate everytime. Consider manual mandate set ups and respective expiry to handle PRD/Solution mapping: PRD ready Platform: Zendesk Status: Solutioning pending

---

## #137 — Will i come to know the interest amt earlier for k
**Status:** Solutioning pending | **Last edited:** Unknown

# """Will i come to know the interest amt earlier for keeping balance""” Classification: UX issue Notes: User wanted to see accrued interest (currently we communicate a couple days before) so that they can maintain the required balance on their bank account and avoid mandate failures (bounce charge) PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 919821375595 Status: Solutioning pending

---

## #138 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #139 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #140 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #141 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #142 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #143 — User Story template
**Status:** Unknown | **Last edited:** Unknown

# User Story template # Guidelines **How should user stories be written?** - Each user story should be atomic — focus on one activity or action. - One feature needs to have multiple user stories for each activity. - For the UPI mandate registration feature, this will be: - Context page. - Mandate registration page. - UPI registration (TPAP). - Post-registration confirmation. - Retry or fallback, if required. - Each user story should be written from a user/customer perspective. - Users can be internal users like sales, support, or operations OR - User can be customer OR - User can be a partner (B2B or LSP) - User stories should document key scenarios and how they will be handled from a UI/UX perspective. - For the UPI mandate feature, this will be: - Mandate registration is pending due to user inactivity. - Mandate registration failure due to user error. - Mandate registration failure due to technical issues. - Mandate registration success. - Delayed confirmation handling. # Template Below is a template for User Stories. - **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc. - **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve. - **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement. # Example Below is a list of User Stories keeping UPI mandate registration as an example. - **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate. **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate). **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey. **Requirement**: Below are the requirements for this page. - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest. - This will be a common page that will cover both NACH and UPI mandate. - This page will describe that customer’s bank account will