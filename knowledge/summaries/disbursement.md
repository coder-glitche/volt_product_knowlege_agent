# Current State: Disbursement

> Auto-generated from 133 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Bank Account Verification for Disbursement in TATA
**Status:** In progress | **Last edited:** September 6, 2024 7:57 PM

**Problem:**
are we solving?**

- For users whose loans are processed with TATA and who have multiple bank accounts stored with the lender, the Volt’s system picks the first bank account for sending disbursement request to the lender.
- Discrepancies occurs between the lender's records and Volt's database regarding a customer's bank account information due to lack of verification process during the account updation using admin tool.

---

**Solution:**
?**

- We will match the bank account number and IFSC code of a customer's bank account stored in Volt's database with the bank account details stored at TATA's end before disbursal.
- This process ensures synchronisation between the two systems, allowing us to accurately identify the correct bank account for disbursement, even when TATA has multiple bank accounts stored for a user, while Volt only retains one.

Below is the request and response of **getDisbursementInfo API** and **SaveDisbursement API**:

**GetDisbursementInfo API**

**REQUEST:-**

INFO NonStaticHttpUtility RRId= RId=6476af48-8ffd-4e4f-bc3b-dabb5f40bf93, CreditId=8a806612907de1bb01907de459bc0005, UId= - Creating post request for uri [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/GetDisburseme

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

## #3 — Manage Limit Error messaging handling
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

## #4 — PhonePe Landing page requirement - 15th April
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

## #5 — Optimizing disbursement metrics
**Status:** In progress | **Last edited:** September 12, 2024 4:44 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

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

## #10 — [Lending stack] Welcome mail
**Status:** Not started | **Last edited:** October 21, 2024 6:19 PM

**Problem:**
are we solving?**

Have to send a welcome email to customer who take loan from DSP Fin Pvt Ltd. The email will contain the loan kit that contains documents like MITC, GTC, KFS and other documents. 

The email should serve the following purposes:

**Functional objectives:**

- **Loan Approval Confirmation**: Clearly inform the customer that their loan application has been successfully approved.
- **Share loan kit**: Provide essential loan details through the MITC, GTC, KFS, and the sanction letter.
- **Next Steps:** Guide the customer on the next steps, such as how can he place disbursement fro

**Solution:**
?**

---

## #11 — MFD Payouts
**Status:** In progress | **Last edited:** October 18, 2024 5:50 PM

**Problem:**
are we solving?**

Current challenges

- Programs line Self-line, has no indication to the payout team causing them to miss the cases.
- GST payouts and Editing of the Payout  reports are manual which will create issues for schedule of payout for reports with edits
- MFDs get the report alongside the payouts, they can not keep track of payout date, and resolution the query they have raised
- We don’t create different reports for MFDs with GSTN, requiring manual work for the GSTN MFDs

Notes 

- Incorrect communication is occasionally provided to MFDs regarding their payouts.
    - data on the 

**Solution:**
?**

- We will build a table with date and report for MFD on the MFD dashboard >earnings
- MFD will have new report every month, we will mention due date
- MFD can download the payout report in a access controlled way(Email to main Email)
- We will provide a Option to add the GSTN number to MFD (optional for MFDs) and we will process there full payout + GST together.
- MFD can accept or raise issues from the dashboard, Reducing the support bandwidth
- MFD can then see status of there issues on the same dashboard.
- MFD will get steps to receive payouts like adding bank account

Current payout journey 

- Invoice details
    - **Select PAN type**
        - Resident Individual (Self)
        - Resident Individual (Other)
        - Private Limited Company
        - Limited Liability Partnersh

---

## #12 — Withdrawal Optimisations
**Status:** In progress | **Last edited:** October 17, 2024 4:45 PM

**Problem:**
are we solving?**

In a 15-day period, 2.84% of the 5130 disbursal requests were rejected, with 1.98% attributed to tech gaps within Volt app. The key problems to address are : 

- Customers see a higher limit on the app and request a bigger amount resulting in failures
- We use a higher limit in our DB which results in withdrawals getting rejected at lender’s end
- Customer raise support tickets and give poor reviews impacting our CSAT and retention
- We face challenges in acquiring new customers due to poor ratings on app
- We are checking the customer’s holding statement which creates issue

**Solution:**
?**

---

## #13 — Integrated Sales tool
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

## #14 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

**Solution:**
?**

---

## #15 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #16 — Excess amount handling
**Status:** On Hold | **Last edited:** November 8, 2024 1:55 PM

**Problem:**
are we solving?**

1. Users are not able to withdraw or utilise their complete limit in case their line goes in excess. 
2. Handling of storing of the excess amount data in our DB is not proper. 

---

**Solution:**
?**

- **Current handling :**
    - When user has excess amount in their line -
        - We show the available cash as excess amount itself
        - The DP gets reduced to excess amount amount itself. We also have a limitation of 1000 as minimum amount of withdrawal. In most cases excess is less than 1000 and hence the user is not able to make withdrawal & gets blocked.

![Untitled](Excess%20amount%20handling/Untitled.png)

- **Optimised handling :**
    - **1st approach**
        - We can show an alert to the user that shows the excess amount on the home screen itself.
        - Alert will say: “You have excess amount present in your loan account, click here to withdraw the excess amount”.
        - We will process the excess amounts which are greater than Rs 1 and less than Rs 1000
   

---

## #17 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #18 — TCL getDisbursementAPI logic updation
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

## #19 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #20 — Sell-off Repayment Reconciliation — Maker Automati
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

## #21 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #22 — PRD – Volt MFD Payouts Process
**Status:** In progress | **Last edited:** May 27, 2025 2:52 PM

# PRD – Volt MFD Payouts Process # **PRD – Volt MFD Payouts Process** ## **1. What Problem Are We Solving?** ### **Key Issues Identified** 1. Business continuity risk as we are too dependent on one analyst for the calculations 2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~ 3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries. 4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts. 5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed. 6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS). 7. **Support Visibility:** No centralized tracking for payout-related support issues. 8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files. 9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails. 10. **GSTN Verification:** No automated verification of correct GST numbers. --- ## **2. Changes needed for Payout automation (Current vs. Proposed)** | Database | Current | Proposed | | --- | --- | --- | | Application Data | DB | No change | | Transaction Data | DB | No change | | Principle Outstanding | Google Sheets | DB | | Partner Commercials | Google Sheets | DB | | Payout Ledger Table | Google Sheets | DB | | Account Payable (AP) | Not tracked | DB | | Base Payout Calculations | Google Sheets | DB | | GST & TDS Calculations | Google Sheets | DB | | Payout & GST Invoice | Google Sheets | DB | | GST Tax & TDS Filing | Google Sheets | DB | | Bank Account Data | Manual Check | DB | | Payout File to Bank | Excel | API | | Payout Payment Status | Statement | API | | Reconciliation & UTR Backfill | Google Sheets | DB | --- ## **3. User Needs** ### **MFD / Partner** - Expect accurate, on-time payments. - Need clear payout breakdowns, including GST invoices. - Require an easy way to highlight and resolve discrepancies. - Want Volt to handle tax filings accurately. - Prefer a payout experience similar to top AMCs. ### **Business Team** - Aims to improve MFD service by resolving payout issues efficiently.

---

## #23 — PRD MFD Performance Metrics & Earnings Display
**Status:** Not started | **Last edited:** May 21, 2025 12:46 PM

# PRD: MFD Performance Metrics & Earnings Display ## **1. Introduction** This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show: - Their sourced **MF Loan AUM** - Applicable **trail income rate** - **Trail income earned** - **Account opening bonuses** The goal is to make it simple for MFDs to understand how their efforts are driving their earnings. --- ## **2. Goals & Objectives** ### **Primary Goal** To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives. ### **MFD User Objectives** - Understand how MF Loan AUM translates into income or Increase visibility to the MFDs - Track progress toward higher income tiers - See a breakdown of earnings and new account bonuses - View historical trends and performance ### **Business Objectives** - Encourage MFDs to grow MF Loan AUM - Boost Volt Money customer acquisition - Reduce support queries about commissions ## **Success Metrics** - MFD Monthly visits to partner portal - MFD Repeat rate - MFD Avg number of applicaitons per month - upward move in MFD LAMF AUM Buckets --- ## **3. User Stories** - *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier. - I want to know my current trail income rate based on slabs. - I want to see how close I am to the next earning tier. - I want to track monthly/quarterly/yearly trail income. - I want to verify bonuses for each new LAMF line opened. - I want a full summary of earnings: trail income + bonuses. - I want to view historical performance trends. - I want to quickly reference the trail income slab table. --- ## **4. Feature Breakdown & UI/UX** ### **4.1 Main Dashboard: Volt Money Performance Overview** **Key Metrics:** | Metric | Example | Tooltip | | --- | --- | --- | | **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money | | **Trail Rate** | 0.55% | Based on current AUM slab | | **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. | | **New Accounts (MTD)** | 5 | From Onboarding CRM | | **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts | | **Total Earnings (MTD)** | ₹58,291 |

---

## #24 — Term Loan LOS requirements
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

## #25 — Product Note LTV update to 70
**Status:** Not started | **Last edited:** May 12, 2026 10:39 AM

# Product Note : LTV update to 70 --- # **1. Problem Statement** --- ## **2. Objective** --- ## **3. Scope** --- - LTV update task - Finflux - Multiple approved script management - Validations - Any sort of handling - Fenix - Multiple approved scripts handling - Risk and RMS validations required - Impact of all collateral transactions - Collateral addition - Collateral removal - Collateral invocation - Shortfall handling - Communications and statements - ROI auditing - Current offer visibility for NBFC and LSPs - Volt - Journey - Enhancement (Fetch/Pledge/Offer/Agreement) - Nudges - B2B2C & B2C - PF/ROI changes - Journey - Admin actions (PF increase to work out of the box) - Payout - Scope reduction - Loan offer - PF/ROI - Contract level - Volt UI --- - Nudge - Current limit - Updated Limit - Current ROI - New ROI - LTV update charges - KFS/Agreement - Task name - Service request approval - Left panel - Request details - Request ID - Service request type : Limit enhancement - Requested on - Current collateral limit - Additional collateral limit - Updated collateral limit - Limit enhancement charges - AMC charges - Substatus - Maker name - Maker remark - Maker created on - Collateral details - ISIN - Asset type - Collateral sub type - Folio - Value - Existing limit - New limit - Right panel - Client details - Loan details - With loan contract - Transactions - Collaterals - Collaterals with details (LTV) - Loan kit - KFS - Agreement - Generate offer what happens? - Request - FXLAN (with collateral details) - Response - Funds with higher LTV - Limit enhancement charge ranges - AMC charge ranges - ROI ranges - Accept offer - Request - Fund with LTV, charges & ROI details - Response - Offer ID - Service request and collateral addition in parallel, what validations to happen

---

## #26 — MFD Payout Process Revamp
**Status:** In progress | **Last edited:** March 7, 2025 1:51 PM

**Problem:**
are we solving?**

[**VOLT MFD Payout Process Overview**](MFD%20Payout%20Process%20Revamp/VOLT%20MFD%20Payout%20Process%20Overview%20129e8d3af13a80f0a322dd388f71d70c.md)

[Payout Working File](MFD%20Payout%20Process%20Revamp/Payout%20Working%20File%20129e8d3af13a80c8ba52c870cda414ea.md)

[PRD - GST Invoice and Payout statement creation and approval ](MFD%20Payout%20Process%20Revamp/PRD%20-%20GST%20Invoice%20and%20Payout%20statement%20creation%20an%2012ee8d3af13a80189662fc13cfe7d2a1.md) 

[Process note Payouts ](MFD%20Payout%20Process%20Revamp/Process%20note%20Payouts%2013be8d3af13a80d58fbaf763

**Solution:**
?**

---

## #27 — [IronGrid] Email trigger for ops in case of disbur
**Status:** Not started | **Last edited:** March 31, 2026 8:24 AM

**Solution:**
?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

---

## #28 — [Platform] Foreclosure handling and enhancement
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

## #29 — PN Storing Commercial Data at Credit Level
**Status:** Pending Review | **Last edited:** March 3, 2025 12:37 PM

# PN: Storing Commercial Data at Credit Level ## Problem Statement Currently, we do not store Platform-level commercial data directly at the Credit level. Instead, this data is maintained in external Excel sheets, which creates inefficiencies in the payout calculation process. The data team must manually add these commercial details when creating payout files, resulting in: - Increased processing time - Higher risk of manual errors - Difficulty in data reconciliation - Lack of data integrity between systems ## Proposed Solution Implement a dedicated commercial data object at the Credit application level that will store all relevant commercial parameters at the time of application processing. ## Key Data Points to Store The Credit level commercial data object should include: - **Lender**: The financial institution providing the loan - **Base ROI**: Original interest rate from lender pricing grid - **Base PF**: Original processing fee from lender pricing grid - **PF Split**: Processing fee revenue distribution between platform and partners - **ROI Split**: Interest revenue distribution between platform and partners - **Payout Amount PF**: Calculated processing fee payout amount - **Payout ROI**: Calculated interest-based payout amount ## Implementation Benefits 1. **Data Integrity**: Single source of truth for commercial terms at the application level 2. **Audit Trail**: Historical record of commercial terms applied to each application 3. **Streamlined Reporting**: Direct data access for reporting without manual intervention 4. **Efficient Payout Processing**: Automated payout file generation based on stored values 5. **Reduced Manual Effort**: Elimination of manual data enrichment processes ## Considerations - Create a new data structure to store commercial data as part of the credit application object - Implement data validation to ensure complete commercial information - Add timestamp and user attribution for commercial data changes ## Example data table | **S_No** | **Platform** | **Type** | **Tata Interest base rate** | **Bajaj Interest base rate** | **DSP Interest base rate** | **Tata PF base rate** | **Bajaj PF base rate** | **DSP PF base rate** | **PF Sharing** | **Trail Sharing** | **PF Sharing %** | **Trail Sharing %** | **Comments** | Signoff | Actionable | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 | Advisorkhoj | Partner | | | | | | | | 0.5 | | | | | | |

---

## #30 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #31 — Withdrawal issues enhancement
**Status:** Not started | **Last edited:** March 23, 2025 6:43 PM

**Problem:**
are we solving?**

- **Users are not able to track and are not notified on failed withdrawal requests**
- Users are not clear that amount disbursed in their account is after deducting the processing fee or other outstanding charges against their line
- Users are not able to track other charges deducted from their withdrawal amount
- Users are sent triggers of processing of withdrawals at incorrect triggers (State management)
- Users are not shown accurate ETAs of their withdrawal requests

For the scope of this PRD we will be covering failed withdrawal handling for the users

- Future scope
  

**Solution:**
?**

---

## #32 — [B2B2C] GST payouts and reconciliation optimisatio
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

## #33 — [B2B2C] Modification for financial terms functiona
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

## #34 — Product note Co-lending foreclosure - Deprecated -
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

## #35 — Increase Credit Utilization via Whatsapp Drips
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

## #36 — Disbursement workflow optimisations
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

## #37 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #38 — Tata Video KYC Integration V0
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

## #39 — Product note LMS integration with Tally
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

## #40 — [NBFC] DSP Finance Website (Aug25)
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

## #41 — Delaying getDisbursementInfo API hit after savePle
**Status:** Pending Review | **Last edited:** January 6, 2025 3:50 PM

**Problem:**
are we solving?**

- For the first getDisbursementInfo API call post credit creation we are getting “No data Found” in the response of the getDisbursementInfo API
- Since we run a scheduler of 1 hour of getDisbursementInfo thus it takes another hour to get a valid response from getDisbursementInfo API response (after getting No Data Found in the response first time)

---

**Solution:**
?**

---

## #42 — [Platform] Mandate collection BRE optimisation
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

## #43 — B2B Platform Dashboard v1
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

## #44 — CKYC Upload for DSP
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

## #45 — [Platform LSP] All transactions requirements
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

## #46 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #47 — [Final] End use capture of transactions
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

## #48 — [Platform] Handling of below 1 Rs transactions for
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

## #49 — PAN type update on partner dashboard
**Status:** Pending Review | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

- Add new PAN type for payout details on partner dashboard
- Update existing PAN type
- PAN and GST validation

---

**Solution:**
?**

---

## #50 — Penny drop on partner dashboard
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- Verify partner bank account for smooth payout

---

**Solution:**
?**

---

## #51 — Foreclosure repayment - Handle PenalInterestAccrue
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

## #52 — Handle settlement of charges against withdrawal
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

When a user initiates their first withdrawal [after new application or line enhancement], we call the adhoc charges API to post the processing charges. However, the posting of charges takes time, this results in.

- Charges not being deducted from the withdrawal amount.
- Charges remain outstanding after the first withdrawal.

---

**Solution:**
?**

---

## #53 — Loan servicing - LAS VOLT
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Stocks collateral management at Volt end:

In scope

1. Remove collateral 
2. Remove collateral status tracking
3. Lien removal communications

Out of scope:

1. Add collateral

---

**Solution:**
?**

---

## #54 — Partial lodgement handling - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

There is a recurring issue with **pledged mutual funds not being lodged** by DSP when the **pledge status remains in "Pending" or “HOLD”** (DSP check pledge status through get lien status **API before initiating the lodgement**). This results in customer confusion, manual intervention from DSP Ops, and lack of visibility for Volt Ops/Support.

---

**Solution:**
?**

To address the visibility gaps, manual operations, and poor customer experience caused by undisbursed pledged funds, the following solutions are proposed:

---

---

## #55 — Partner MFD Dashboard PRD (LAS Servicing)
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt currently provides a **LAMF Servicing Dashboard** for partners (MFDs) to view and manage completed loan applications.

With the launch of **LAS (Loan Against Shares)**, we need to **extend the Partner Dashboard** to:

- Support **LAS servicing & monitoring**
- Provide **cross-product visibility** (LAMF + LAS)
- Maintain consistency, data integrity, and usability across both products

**Solution:**
?**

Volt will **extend its existing Partner (MFD) Dashboard** to support **LAS (Loan Against Shares)** servicing with:

- **Full cross-product visibility** across **LAMF and LAS**
- Ability for partners to **manage LAS loan accounts on behalf of customers**
- Enable **servicing communication** for LAS

This extension ensures that MFDs can seamlessly service both **LAMF and LAS portfolios** through a **single, unified platform**, driving operational efficiency, improved customer experience, and higher LAS adoption.

---

## #56 — TCL Dynamic repayment schedule
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

## #57 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #58 — DSP website revamp
**Status:** Not started | **Last edited:** February 12, 2025 4:29 PM

# DSP website revamp # Problems to solve 1. “Make the website a public website” 1. Make it accessible on Google and other search engines (already visible through Bing) 2. Brand impression: currently looks like a placeholder website 3. Improve “About DSP” section 1. More prominently referencing to the DSP group - Review other DSP children websites 4. Product offerings 1. Structured lending 2. LAMF - understand what’s missing 3. LAS - show coming soon? 5. Regulatory 1. Link RBI’s sachet portal 2. Prominently display name, email, contact number of grievance redressal officer on website 3. Prominently display details of COO - Principal Nodal officer on website 6. Minor fixes 1. Update address - 11th floor instead of 10th floor 2. Update CIN 3. Operating timings: customer care 4. Update partners list 5. Benefits → “RBI registered” needs to come with a disclaimer - refer to flexiloans footer 7. Logo finalisation ![image.png](DSP%20website%20revamp/image.png) # Solution space - [ ] Understand scope - [ ] Talk to priya - What is “headers” - Pankaj notes - [ ] Get feedback shared by Pankaj Thapar (policy consultant) - [ ] New website mood board - how much brand referencing is needed? | Problem | Proposed solution | | --- | --- | | 1.a | - Submit site on Google Search Console - Make sitemap.xml - Make robots.txt | | | | WEBSITE LAYOUT ### Header - Partners - Products - About ### Hero - Title - “Loans against securities” - “digital first approach” - CTA ### About Organisation stats - Money disbursed, Loans given, no. of partner tie ups - Since 160+ years ![image.png](DSP%20website%20revamp/image%201.png) ### Our products - LAMF - LAS - Structured lending ### LAMF features ### How it works ### Footer ## Additions - FAQs - About us → our team

---

## #59 — Attribution for Volt applications
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

## #60 — Un-pledge optimisations
**Status:** In progress | **Last edited:** December 3, 2024 3:13 PM

**Problem:**
are we solving?**

For BFL users, who make a withdrawal request of complete available amount while an un-pledge request is in-progress then the withdrawal requests gets processed first and un-pledge request gets rejected due to update in the value of net-payable due to the withdrawal processing  

---

**Solution:**
?**

When user is making a withdrawal is making a withdrawal while an un-pledge request is in “In progress” we will give a heads-up to the user that the withdrawal request might interfere with the un-pledge request if the outstanding is not zero. [This change only needs to be done for BFL]

---

## #61 — Show accrued interest on UI
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

## #62 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #63 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #64 — Single drawdown Term Loan LMS Requirements
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

## #65 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #66 — PRD Disbursement Method Selection Logic (BRE Optim
**Status:** Not started | **Last edited:** April 7, 2026 11:53 AM

# PRD: Disbursement Method Selection Logic (BRE Optimization) --- # **1. Problem Statement** Currently, payout method selection (IMPS / NEFT / RTGS) is not dynamically optimized based on: - Disbursement sequence (1st vs subsequent) - Loan type (co-lending vs non co-lending) - Ticket size - Sourcing channel (e.g., CRED) This leads to: - Suboptimal payout routing - Higher costs and delays - Lack of configurability at product / contract / channel level --- ## **2. Objective** Enable a rule-based engine (BRE) to dynamically select payout method based on: - Disbursement sequence - Loan type - Amount slab - Sourcing channel --- ## **3. Scope** ### **Dimensions for Rule Evaluation** 1. **Contract type** - Co-lending - Non co-lending 2. **Sourcing Channel** - Volt - CRED (override rules) 3. **Nth Disbursement** - 1st - Subsequent 4. **Amount Slabs** - < 2 lakhs - 2–5 lakhs - 5 lakhs --- ## **4. Business Rules** ### **4.1 Co-lending Loans** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | NEFT | NEFT | RTGS | | **Subsequent** | NEFT | RTGS | RTGS | --- ### **4.2 Non Co-lending Loans** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | IMPS | IMPS | RTGS | | **Subsequent** | NEFT | RTGS | RTGS | --- ### **4.3 Sourcing Channel: CRED** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | IMPS | IMPS | RTGS | | **Subsequent** | IMPS | RTGS | RTGS | **Note:** - These rules override both co-lending and non co-lending logic when sourcing channel = CRED --- ## **5. Rule Priority Logic** Order of evaluation: 1. **Sourcing Channel Override (Highest Priority)** 2. **Contract Type (Co-lending / Non co-lending)** 3. **Nth Disbursement** 4. **Amount Slab** --- ## **6. Configurability Requirements** - Rules should be configurable at: - Product level (for future requirements) - Contract level - Sourcing channel level - Ability to: - Add/edit slabs - Change payout method mapping - Introduce new channels without code changes --- ## **8. Success Metrics** - Reduction in payout failures - Reduction in payout cost per transaction - Improvement in disbursement TAT - % of transactions routed via optimal rail ---

---

## #67 — Enhancements in Fenix disbursements BRE
**Status:** Pending Review | **Last edited:** April 7, 2026 11:50 AM

**Problem:**
are we solving?**

---

- The overall SR for payouts is 99.2% and payment method wise the SR is the
    - IMPS : 99.59%
    - NEFT : 83.81 % (lower SR because these are retry attempts after IMPS failures - usually an issue at bene bank)
    - RTGS : 97. 66%
- As confirmed with Cashfree and YES Bank the SR of disbursements through NEFT is significantly higher than IMPS (Cashfree to share exact data points for this).
- Bifurcation of 0.8% disbursement failures in Apr-May
    
    
    | Reason | Count | Percentage |
    | --- | --- | --- |
    | Beneficiary bank side decline | 138 | 46.78% |
   

**Solution:**
?**

**Experiment 1 - Pilot NEFT as a primary payout method** 

- Objective -
    - Understand if Success Rate (SR) will increase by using NEFT
    - Settlement Time (TAT) of NEFT across business hour and non business hours
- Introduce NEFT as an alternate disbursement method to improve success rates as NEFT has a higher success rate than IMPS (as confirmed with Cashfree)
- 1st disbursement will continue to be IMPS upto 5L and RTGS >5L
- Logic for subsequent disbursements.
    - Every disbursement less the amount of ₹5 lakhs (except the first disbursement) will be routed via NEFT, since amounts above ₹5 lakhs are already handled through RTGS
- Implement a configurable flag to enable or disable NEFT routing instantly in case of any issues during the pilot.

**Results of experiment 1 -** 

-

---

## #68 — Product Note – DRPS (Final Version – Unified Forma
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

## #69 — Untitled
**Status:** Not started | **Last edited:** April 17, 2025 11:42 AM

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #70 — B2B2C call incoming reduction
**Status:** In progress | **Last edited:** April 17, 2025 11:41 AM

# B2B2C call incoming reduction [Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md) [](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md) # Detailed Breakdown of Customer Call Issues ## Loan Application Issues - **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval. - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times. - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."* - The withdrawal interface appears to lack clear instructions for first-time users. - **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process. - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."* - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs. - **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations. - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."* - The fee structure appears to be disclosed incompletely during the application process. - **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements. - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."* - The eligibility criteria seem inconsistently communicated across different channels. - **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process. - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."* - These timeouts appear to occur most frequently during document upload or verification steps. Payment Processing Issues - **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments. - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."* - These delays severely

---

## #71 — Unpledge and Disbursement Enhancement
**Status:** In progress | **Last edited:** April 14, 2025 8:21 PM

**Problem:**
are we solving?**

Currently, customers with pending unlien (unpledge) requests see a general disclaimer: "Unlien request in progress, withdrawals may affect the approval of your on-going unpledge request." This creates uncertainty as customers cannot determine their exact available limit until their unlien request reaches a terminal status.

---

**Solution:**
?**

I. During Unliening in process:

1. Display Precise Information 
    - Show a specific message: "Unlien request in progress, withdrawals over ₹X,XXX will affect the approval of your on-going unpledge request"
    - The ₹X,XXX represents the calculated "recommended disbursement amount" that won't interfere with the pending unlien request
2. Calculation Method for Recommended Amount
    - Calculate the active loan amount of the pending unlien funds
    - Subtract this value from the customer's current available limit
    - Present this as the safe withdrawal threshold
3. User Experience Benefits
    - Guides customers to select realistic withdrawal amounts
    - Reduces confusion and prevents unexpected withdrawal rejections
    - Provides transparent information about current account l

---

## #72 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #73 — MFD Processes
**Status:** Unknown | **Last edited:** Unknown

# MFD Processes # Activation Process To connect with Ashik, # Application Process MFD portal flow - RMs to explain. LSQ + sales flow like Exotel. # Servicing Process Whatsapp groups process like Periskope - Sowmya, # Payout Process

---

## #74 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #75 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #76 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #77 — MFD Payout dashboard
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout dashboard We have a commercial relationship with MFD , where we pay them as per the business they bring Commercials | trail income | 0.5% of AUM | | --- | --- | | account opeing | 200rs | | Selfline | Processing fees waived | | Cashback | | | Content | | | referral | | - MFD payout is calculated based on commercials agreed on with them - MFD payout is different if the MFD is registed for GST - MFD with Gst number has to be paid 18% extra as GST - we collect 5 % TDS for any payout >15000rs - we payout on 10th on month to volt MFDs - we payout on 15th to SAAS partner platform MFDs - we payout on 18 th to MFD GST payout - we clear all pending and charges till 25th - MFD may not want to share the PAYOUT amount to there employees - MFD need to see the payout status - GST issues - Payout starts at 1 of the money - Time preiod is month to month - And 10 to 15 th of month payout disbursement happen - 10 MFD get paid - 15 Platform , - 18 MFD GST payout - 25 th anything pending - Puneet compute the payout MFD , 0.5% of AUM yearly trail income/ 12 200 rs per account opening , creditline open MFD selfline - we refund the family of MFDs , RMs fill a sheet Cashback for MFD’s end customers , - we gave 10.49 % customer we have given 0.5 % cashback as we advertised on 9.99% Contest , referrals price, activated MFD referral rs 1000 Platform , :- payout Affiliate - payout - MFD - - partner - - Platform - Affilaetes - Bharat sign off, Labdhi comms - Total amount August Pain points - GST filling , we have to 18% as a TDS of the total payout of the month. - we collect 5% TDS ,

---

## #78 — One Pagers
**Status:** Unknown | **Last edited:** Unknown

# One Pagers [OP - Selloff and Withdrawal request mismatch](One%20Pagers/OP%20-%20Selloff%20and%20Withdrawal%20request%20mismatch%20106e8d3af13a808cbebffae82d466652.md) [**Handling Discrepancies Between Assumed and Actual Limits**](One%20Pagers/Handling%20Discrepancies%20Between%20Assumed%20and%20Actual%20%20106e8d3af13a80748d1cd01661d83138.md) [Missed calls from customers aren't being called back or addressed](One%20Pagers/Missed%20calls%20from%20customers%20aren't%20being%20called%20ba%207dfeec301f004c0586694a51de935466.md) [Sales team is calling customers who complete the journey on their own](One%20Pagers/Sales%20team%20is%20calling%20customers%20who%20complete%20the%20j%2010ae8d3af13a80e4ba2af4aee3ad9ee8.md) [LaMF funnel ](One%20Pagers/LaMF%20funnel%2010ae8d3af13a80ef8b19ccc25e547569.md) [LSQ: Leedsquared](One%20Pagers/LSQ%20Leedsquared%20119e8d3af13a80a0b441ed3d3b464180.md) [MFD Payout dashboard ](One%20Pagers/MFD%20Payout%20dashboard%20120e8d3af13a80f5980de9438ff2e277.md) [Periskope](One%20Pagers/Periskope%20120e8d3af13a80b9ad82c524050ef3a2.md)

---

## #79 — Analytics requirement for amortisation of PF
**Status:** Pending review | **Last edited:** Unknown

# Analytics requirement for amortisation of PF Last Edited: April 24, 2026 8:59 AM PRD ETA: April 24, 2026 PRD Owner: Vaibhav Arora # **1. Objective** Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module. The design must be extensible to accommodate other fee/cost types in future iterations without structural rework. # **2. Scope & Exclusions** ## **2.1 In Scope** - Product lines: LAMF, LAS, Term Loan (TL) - Charge type: Processing Fee (PF) - Accounting entries: Income recognition at monthly amortisation level - Amortisation method: Straight Line Method (SLM) - Report period: M-N (N>0) (previous calendar months only) - Waiver handling: Partial and complete waivers with corresponding reverse entries - Loan closure handling: Remaining balance acceleration on closure date ## **2.2 Explicitly Out of Scope** - GST component of processing fee excluded from amortisation entries - Current month entries - report is strictly retrospective - Real-time or intra-month amortisation schedules # **3. Source Data & Key Fields** All data will be sourced from the accounting report. The following fields are required at a schedule/charge level: | **Field** | **Source / Table** | **Notes** | | --- | --- | --- | | FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier | | Client External ID | LMS – Loan Master | FXCID reference | | Product Type | LMS – Loan Master | LAMF / LAS / TL | | Charge Application Date | LMS – Fee Schedule | Date PF was applied | | PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only | | Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference | | Loan Status | LMS – Loan Master | Active / Closed | | Closure Date | LMS – Loan Master | Populated only if loan is closed | | Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator | | Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee | | Waiver Date | LMS – Waiver Log | Date waiver was applied | | Waiver Type | LMS – Waiver Log | Partial /

---

## #80 — Charge reversal enhancement
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

## #81 — Colending Disbursement and Charge knock off
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

## #82 — Corporate action - Data feed
**Status:** Completed | **Last edited:** Unknown

# Corporate action - Data feed Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # Corporate Actions Data Feed ## Overview To support monitoring of securities pledged as collateral, we have reviewed a **Corporate Actions data feed sourced from BSE end-of-day bulletins**. This feed provides information on **events and disclosures that may impact the value, structure, or tradability of securities**. The data is consumed daily and can be used by the Risk team to monitor portfolio changes and identify events that may require action. The data covers the following broad categories: - Corporate action events - Company structural changes - Market disclosures - Large market transactions - Insider activity - Liquidity indicators --- # 1. Corporate Action Events This dataset contains information about **corporate actions declared by listed companies** that may affect the number of shares, price, or entitlement of shareholders. Typical corporate actions include: - Dividends - Stock splits - Bonus issues - Rights issues - Buybacks - Capital restructuring events For each event, the feed provides key reference dates such as: - **Record Date** – Date used to determine shareholder eligibility - **Ex-Date** – Date after which the security trades without the entitlement - **Cum Date** – Date before which investors must hold shares to be eligible - **Effective Dates** – Time period during which the action is applicable In addition, where applicable, the feed also provides: - Dividend amount or payout value - Share conversion ratios (e.g., split or bonus ratios) - Share quantity adjustments - Offer price or premium for rights issues These events are critical for adjusting **collateral valuation and share quantities** in pledged portfolios. --- # 2. Corporate Action Classification A separate master dataset provides the **mapping of corporate action identifiers to the specific event type** (e.g., dividend, split, bonus). This allows systems to interpret the corporate action feed and determine the **nature of the event impacting a security.** ---

---

## #83 — Credit note PRD
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

## #84 — Disbursement simulation - LMS
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
- Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula.
- Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen.
- Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum a

# Disbursement simulation - LMS Last Edited: May 22, 2026 3:49 PM PRD ETA: May 5, 2026 PRD Owner: Vaibhav Arora ## Background and Context - **Who is affected** - Borrowers using Volt (DSP Finance's LSP) who initiate withdrawal requests from their Loan Against Mutual Fund (LAMF) accounts. - All LSP partners integrated with DSP Finance's disbursement infrastructure. - DSP Finance's Risk Operations team, who are exposed to collateral shortfall risk when disbursements breach the safe limit. - **What is broken today** - The current Available Limit calculation — `AL = min(DP, SL) - POS + EM` does not account for accrued interest, charges, or scenarios where non-principal exposure grows to exceed the margin held against collateral. Two specific scenarios expose DSP Finance to risk: - **Case 1 — Collateral Removal:** After a borrower repays principal and requests maximum collateral removal, the remaining collateral may only cover the Drawing Power. Any subsequent withdrawal creates a situation where accrued interest (once booked as Interest Due) pushes total exposure above collateral value. - **Case 2 — Voluntary Sell-off:** After a sell-off settles principal, the sell-off proceeds inflate Excess Money, which inflates the Available Limit. A borrower can withdraw this excess, creating a POS that, combined with accrued interest becoming due, exceeds the remaining collateral value. - Today, the Loan Detail API value is trusted by all downstream systems (Fenix, Volt, and LSP partners) as the authoritative available limit. There is no pre-disbursement validation layer that applies the updated risk-safe AL formula before funds are transferred. - **Why it matters** - Collateral shortfall represents direct credit risk for DSP Finance — in cases of default, outstanding dues cannot be fully recovered. - The gap grows over time as accrued interest compounds, making early intervention critical. - LSP partners rely on the available limit shown to borrowers; without a simulation gate, disbursements that breach exposure limits will be processed without any check. --- ## 1. Problem Scope ### In scope - Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula. - Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen. - Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum allowed amount and enabling re-entry. - API design contract documentation to be shared with

---

## #85 — FD Fixerra
**Status:** Unknown | **Last edited:** Unknown

# FD: Fixerra Last Edited: December 1, 2025 2:13 PM ### Product Alignment Note – Fixerra FD Offering via Partner Dashboard *(DSP Finance × Volt Platform)* --- ### **Problem statement** Volt x DSP have a strong distribution via IFAs, we want to experiment distribution of different products via this channel, because of DSP Finance (NBFC) is looking to expand its retail investment footprint beyond LAMF (Loan Against Mutual Funds) by introducing a Fixed Deposit (FD) product. On the Volt platform today, distributors (primarily MFDs) only have LAMF as the monetizable product. While LAMF has strong unit economics, it is not a top-of-funnel product for retail customers. Fixerra provides the underlying FD product and infrastructure. The hypothesis is: - We already have arms-reach access to a large base of customers with mutual fund holdings. - These customers have a natural affinity for low-risk investment instruments. - FDs can act as a trust-building, widely accepted entry product, opening the funnel for both direct revenue (FD) and future LAMF conversions. This note outlines the scope for v1 of FD origination and servicing through the Volt Partner Dashboard, and is intended to align stakeholders across DSP Finance, Volt, and Fixerra. --- ### 2. Problem statement ### 2.1 Current state - MFDs on Volt can only offer LAMF. - Monetization is limited to one product with a relatively narrow target audience. - No simple “safe” product exists to attract or engage a wider customer base. - Distributors lack tools to deepen customer relationships beyond MF transactions. ### 2.2 Opportunity Introducing FDs: - Expands the product portfolio for MFDs. - Helps create a trust-led entry point (“mouth of the funnel”), improving conversions into higher-ticket products like LAMF. - Offers DSP Finance a scalable retail deposit base. - Allows Fixerra to distribute its FD product through MFD networks. --- ### 3. Product hypothesis **FDs can become a high-trust, low-friction product that increases distributor engagement and revenue, while simultaneously opening the pipeline for LAMF upsell.** Supporting hypotheses: 1. Customers with MF holdings are more likely to evaluate FD products with high confidence. 2. MFDs will be able to deepen their relationship and improve overall earnings by offering a broader product suite. 3. The NBFC can explore differentiated FD structuring based on distribution performance (for example, special rates, bulk programs). --- ### 4. High-level GTM - **Channel:** Volt Partner Dashboard - **Actors:** Mutual Fund Distributors on Volt - **v1

---

## #86 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #87 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #88 — Tally ERP Integration
**Status:** Completed | **Last edited:** Unknown

# Tally ERP Integration Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # **Tally Journal Voucher API Contract (Sample Document)** This document outlines the proposed API contract for pushing journal voucher entries from the LMS/ERP system to Tally. Each journal voucher corresponds to a single **transaction event**, containing one or more **ledger-level debit/credit lines** with consolidated amounts. --- ## **1. API Overview** ### **Endpoint** (To be shared by the vendor) ### **Purpose** Push a complete journal voucher entry at a transaction type level to Tally for accounting purposes. --- ## **2. Request Structure (Batch Journal Posting)** The API will support **batch posting** of journal vouchers. Each request will contain an **array of transactions**, where each object represents one complete journal voucher. ### **2.1 Journal Voucher Batch Payload** ```json [ { "transaction_type": "string", "narration": "string", "voucher_date": "YYYY-MM-DD", "tally_txn_id": "1234564534432", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" } ] }, { "transaction_type": "string", "narration": "string", "tally_txn_id": "1234564534433", "voucher_date": "YYYY-MM-DD", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" }, { "ledger_name": "Sample3", "debit": "number", "credit": "number" } ] } ] ``` --- ### **Field Description** | Field | Type | Description | | --- | --- | --- | | transaction_type | string | Preconfigured transaction type (ex: PAYIN, PAYOUT) | | tally_txn_id | string | Unique transaction identifier used as **dedupe key** | | voucher_date | date | Voucher posting date | | narration | string | Narration mapped to transaction type | | ledger_entries | array | List of debit/credit ledger lines | --- ### **Ledger Entry Object** | Field | Type | Description | | --- | --- | --- | | ledger_name | string | Name of the ledger in Tally | | debit | number | Amount debited (zero if not applicable) | | credit | number | Amount credited (zero if not applicable) | --- ## **3. Transaction Type Samples** Below are examples for each transaction type based on provided data. --- ## **3.1 ADD_FEE** **Narration:** Being fee income recognition ```json { "tally_txn_id": "<unique-id>", "transaction_type": "ADD_FEE", "voucher_date": "2025-01-01", "narration": "Application of fee on loan account", "ledger_entries": [ {"ledger_name": "Fees receivable", "debit": 7109825, "credit": 0}, {"ledger_name": "Income from Fees", "debit": 0, "credit": 6025269}, {"ledger_name": "CGST Payable", "debit": 0, "credit": 90382}, {"ledger_name": "SGST Payable", "debit": 0, "credit":

---

## #89 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #90 — [Platform] Disbursement optimisation to handle cro
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?**

As an NBFC one of the core aspects is to handle disbursements. Disbursement as a request as primarily two main components:

- Payout from the source bank account to the beneficiary bank account
- Posting of the transaction in the loan account of the user

While it seems pretty straightforward, there are multiple aspects that affect this workflow:

- Charge posting and knock off from disbursement requests
- Disbursement reversals

More about payouts:

Now payouts primarily have two cycles, debit cycle where the money is debited from the source bank account (NBFC bank account)

**Solution:**
?**

When a payout for a disbursement request placed in the previous billing cycle with a successful SOA posting in the previous billing cycle fails in the next billing cycle.

Change 1: Instead of reversing the payout as well as the corresponding knock off entry, we will be doing a partial return of the SOA posting.

Change 2: When a user places a withdrawal request, as a part of the workflow, we first knock off the charges, and then initiate the payout (sometimes it takes time for us to get confirmation on the payout cycle and the debit cycle in itself can fail) can cause similar instances as described in the problem statement where we are unable to reverse the charge knock off transaction post billing cycle

Scenario 1:

Processing fees applied on 31st March 2025 for account opening of 

---

## #91 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #92 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #93 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #94 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #95 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #96 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #97 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #98 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #99 — Notes Bharat
**Status:** Unknown | **Last edited:** Unknown

# Notes <>Bharat Negotiations table - we will close self-line until we can ensure 1 self-line per partner account. - Rate change, and PF - In tata we can’t change the Rate , so cashback is the option for the Tata. TDS Accounts payable Payment ops Commercials data on the entity - there are three entities applications partner platform that dictate commcials there is a base rate as per the lender that will be assigned by the BRE now once the ROI and PF are assigned to the user then the commencial terms should be added to the application as well on a applciations level we have We have different commercial terms with the on three entity levels application Partner Platfrom the commercials are the the param used to calculate the payout made for the user the Base rate is assigned as per the lender pricing grid of the time of application creation There is default commercials rate that get assigned to Partners and platform by default there are admin actions which assign for a application differenct ROI and PF and the split between the Volt and partner s we are currently not storing the commercials data on the entities level instead its a excel sheet , which casuses issues when calciualting the Solution possible to add object to the right entity that stores he commercials data Application level - ROI - PF - ROI split - PF slip - Base ROI - Base PF Partner level - offer applicable ? - Offer code - ROI - PF - ROI split - PF slip the ROI , PF and splits can be added to the application or to the partner, if added to the partner all the application created by the partner will be assigned the new commercials. Offer code is applied if the applicable. offer can be set of rules like >5 application in the month x = 5000 rs in the payouts Offer has a applicable to and from date the platfrom Platfroms have the similar - ROI - PF - SLITs - Slab based rules the data flow will be 1. application is created 2. assign base ROI and PF from the Lender pricing Grid 3. assign the Application level negotiated Rates collected from Admin actions 4. Assign the MFD commercials as default , then change if changed by the admin action 5. the Platform commercials will

---

## #100 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #101 — Cost estimates
**Status:** Unknown | **Last edited:** Unknown

# Cost estimates # AWS Infrastructure Cost Projections (2024-2026) ## Constants & Assumptions | Parameter | Value | Notes | | --- | --- | --- | | Growth Rate | 2x yearly | Partner base doubles each year | | Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) | | Retention Period | 84 months | 7 years for regulatory compliance | | Emails per Partner | 3/month | Registration, payout, GST notifications | | API Calls per Partner | 20/month | Includes all interactions | | Lambda Executions per Partner | 10/month | All automated processes | ## Growth & Cost Projections | Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | | --- | --- | --- | --- | | Active Partners | 2,500 | 5,000 | 10,000 | | Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB | | Cumulative Storage | 93 GB | 279 GB | 558 GB | | Monthly Emails | 7,500 | 15,000 | 30,000 | | Monthly API Calls | 50,000 | 100,000 | 200,000 | ## Monthly Cost Breakdown (USD) | Service | Year 1 | Year 2 | Year 3 | Scaling Factor | | --- | --- | --- | --- | --- | | S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation | | RDS | $45 | $65 | $110 | Step Function* | | Lambda | $3 | $6 | $12 | Linear | | SES (Email) | $0.75 | $1.50 | $3 | Linear | | API Gateway | $5 | $10 | $20 | Linear | | CloudWatch | $15 | $25 | $45 | Step Function* | | Route 53 | $0.50 | $0.50 | $0.50 | Fixed | | Step Functions | $2 | $4 | $8 | Linear | | **Total Monthly** | **$73.39** | **$118.42** | **$211.33** | | | **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** | |

---

## #102 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #103 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #104 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #105 — Payout Working File
**Status:** Unknown | **Last edited:** Unknown

# Payout Working File Errors earliar - We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured - We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally - We receive GST issues as Customer raise wrong invoices, This is because we don’t provide GST tax invoice to the partners - We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering uploads the data once a month - We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data. - We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date - We need to streamline GST and TDS filing - We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~ list , journey , use case ## Meeting notes - customer - cashback- - previously - partner - platform customer cashback Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49 march 2022. —>23—>24 <may 1st 9.99 9.99 -ROI base rate - 10.49%. 0.5 % cashback on may 1 we changed the base rate for the customer to 10.49% cusotmer cashback , partner to partner Selfline partner payout - MFD - Volt empaneeled MFD - MFD direct - through Software, redvisison or invest well, assest plus , zfunds , - MFD software - affiliates, - Ytbers , - Partner payout - apps like phonepe , jupiter, niyo, part+ - Money is calculated on the Principal outstanding , monthly average daily average, payout is calculated customer wise average POS, eod, for debit-credit sharing percentage with partners - 1. customer —> loan —> 1. credit to borrower 2. Credit to partner 3. Credit to platform 2. partner - volt- 3. upfront - one time payment, rs 200 for opening a account 4. trail income - 0.5 % into POS 5. category —> upfront and

---

## #106 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #107 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #108 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #109 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #110 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #111 — Term Loan Apportionment Logic
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Apportionment Logic - Apportionment is the distribution of a paid sum of money across multiple components of a loan/tranche in order to knock off/settle these components. - Apportionment logic will be based in the order of IPC. - In case of a single tranche apportionment the order will be: Interest Overdue>Principal Overdue>Interest Due>Principal Due>Charge. In case there are multiple EMIs of the Tranche which are overdue then apportionment will start from the oldest EMI overdue. - In case of multiple tranches apportionment the order will be: Oldest EMI overdue(Interest>Principal)>Oldest EMI due(Interest>Principal)>Charges. In case of EMIs overdue across multiple tranches the oldest EMI across tranches will be apportioned first then the apportioning will be done for the next oldest EMI across the tranches and so on so forth. In case all the overdue EMIs are cleared/apportioned the next apportioning will be done for the oldest due EMI and once the oldest due EMI is apportioned then apportioning of the next oldest due EMI will be done and so on so forth. Once all the overdue and due EMIs are apportioned across tranches, apportionment of charges will start and it will also be done based in the order of the oldest charge getting apportioned first i.e. in the chronological order. - If after the apportionment of all the components there is an excess which remains then we will ask the user to select the tranche wherein the excess will be adjusted. The excess adjustment will happen in a way that either the Tenure of the Tranche is reduced or the EMI of the Tranche is reduced based on the user’s selection. Default option(in case user does not select) will always be to reduce the tenure keeping the EMI same for the oldest Tranche.

---

## #112 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #113 — Term Loan Communications
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

## #114 — Term Loan Customer Statements
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

## #115 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #116 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #117 — Term Loan Excess Handling and Refund
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

## #118 — Term Loan Foreclosure
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

## #119 — Term Loan Mandate Repayments
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

## #120 — Term Loan Manual Repayments(PG)
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

## #121 — Term Loan Manual Repayments(VA)
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

## #122 — Term Loan Prepayments and Excess Handling
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

## #123 — Term Loan Sell off
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

## #124 — Term Loan Unpledge Eligibility API(Post loan creat
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, LSPs do not have visibility into how much of a customer’s pledged portfolio is eligible for unpledging at any given point in time.

When users initiate an unpledge request through the LSP interface, they may encounter errors or rejections if:

- The requested unpledge amount exceeds the eligible limit (based on outstanding loan value, haircut, or margin requirements)

This leads to:

- Poor user experience — users get rejected after attempting unpledge.
- Increased operational load — repeated support queries and failed attempts.
- Inefficient system calls — LSPs m

**Solution:**
?**

We will provide an Eligibility API for Unpledging that LSPs can call before initiating an unpledge request. The API will return aggregate eligibility (amount-wise) for the LSP to inform to their customers on their app. The eligible amount based on which the user will be able to unpledge their funds will be calculated as detailed below:

$Maximum Unpledge Eligible Amount = Drawing Power - Principal Dues - Interest Dues - Outstanding Loan Principal(Not due) -  Outstanding Interest for Upcoming EMI across all Tranches(Not Due) + Total Excess$

The API we need to provide will include the following mandatory parameter:

loanAccountId

The response we need to provide based on the API call will include the following mandatory parameters:

loanAccountId
maxUnpledgeEligibleAmount

The Maximum 

---

## #125 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #126 — MFD Payout Calculation Automation
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout Calculation Automation **Introduction** Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency. 1. we need to handle changing factors like - Monthly Transactions table - Marketing Offers /Referral bonuses - New Platforms additions - Changes in commercials with existing platforms /partners - Changes in base rates / Format - Negotiations with MFDs 2. We need to be able to audit how an amount was generated 3. we need to be able to accrue the credits to an account based on the activity 4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback Problem statements Before base payout calculations - Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing. - We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable. - Attribution of customer to correct Platfrom and partner require manual intervention. - We don’t store the PF and ROI paid by the customer in Credits table. - Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts After the Base payout calculation - TDS rules change and have to accommodate - GST payout are tracked manually Payout process - Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC - For Platform Payouts we need to provide a statement and how the Payout amount is calculated. - Partners have a hard time understanding statements. Potential solutions - Get TATA to improve the API data provided to get the updated transactions - Better fall-back handling on our side Activity activity triggers a

---

## #127 — MFD payouts payment reconciliation
**Status:** Unknown | **Last edited:** Unknown

# MFD payouts payment reconciliation Problem statements - It takes 3-4 days to reconcile payouts to MFDs - It takes 2 day to make bulk payments and get the status back from the HSFC. - We have to wait 2 days and try to make payment again to MFDs for whom the Payment have failed , this takes another 2 days to reconcile -

---

## #128 — rough
**Status:** Unknown | **Last edited:** Unknown

# rough notes - Tat on a chat , - ticket resolution and creation - check whatsapp api changes Ideal flow MFD is had a request or a issue they communicate the issue with us we mark it as issue and solve it MFD —> Issues —> communications —> Tickets—> solution - IF a MFD or there employees have issues they can reachout to volt and we want to solve the issues promtly - MFD can communicate with us through WhatsApp chat - Now we need to Identify the issues , create a ticket and resolve the ticket Current problems - We don’t have the ticketing system in place - Current tools we are using are not optimal for creating and tracking Tickets Raw notes - The MFD facing challenges in getting timely response - All the onboarded MFD are added to periscope group - MFD’s uses WATI when they interact through Dashboard chat - MFD’s has to use two separate chat channel if they open up a Whatsapp channel through Wati - MFD’s ask , servicing , payout topic of communications are of general nature. our challenges - We have limited ( can’t) tracking of the incoming chats and there resolution - This is a Periskope limitation. we don’t get Open , resolved , WIP status of a Chat - we are unable to check “How many chats groups are active “ , “were active last week “ - We can’t identify if chats are Sales or service related - we get ~100 chats a day - There is no Bulk download chat option in Periscope - we can’t see TAT for a response and resolution - - agents loose track of the ongoing chats , as it chats are pushed to the bottom of the que and it become a issue to differentiate between the chat groups - 2 people work on the periscope - No way of closing the chats and mark that issue was solved - Analytics- daily number of message counts, Flagged messages - no explanation of what these terms are - How to raise tickets is not clear to the team - we use Periscope to reach out to MFDs , If a MFD reach-out and RM are unavailable then we assign another agent to Periscope - group is already connected with Periscope , all all the MFD are added to periscope they are

---

## #129 — Repayment_Schedule_3900 (4)
**Status:** Unknown | **Last edited:** Unknown

# Repayment_Schedule_3900 (4) ![](Repayment_Schedule_3900%20(4)/image1.png) --- Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) --- RANJAN SINGH S/O: Dinesh Singh,shivalya bhawan,Sector, 03,nandgawn,Singrauli,Singrauli,Madhya, Pradesh,486887 Singrauli- 486887,Madhya Pradesh 7980565882 ranjan.singh@voltmoney.in --- Branch Name DELHI - RAJENDRA PLACE Product Type LAS Customer Name RANJAN SINGH Currency INR Loan Account No. 3900 Frequency Monthly Rate of Interest per annum [%] 10.19 Loan Status Active Loan Amount [Rs.] 315.00 Total Installment [Rs.] Total Tenure (in month) 12 Balance Installment [Rs.] Loan Sanctioned Amount [Rs.] 50,500.00 Charges Outstanding 0.00 Loan maturity date 07-Oct-2026 [Rs.] Available Amount for 49,998.00 Interest Rate type Floating Disbursement [Rs.] ![](Repayment_Schedule_3900%20(4)/image2.png) --- | | | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | Installment no . /TypeDue Date / Transaction DateOpening Balance [Rs.]Installment Amount [Rs.]Principal [Rs.]Interest [Rs.]Closing Balance [Rs.]Efftect Rate(%)Transaction TypeF07-Oct-2025407.000.000.000.00407.0010.19Facility DateD13-Oct-2025407.000.000.000.0010,407.0010.19DisbursementD17-Oct-202510,407.000.000.000.0030,407.0010.19DisbursementD20-Oct-202530,407.000.000.000.0045,407.0010.19DisbursementD27-Oct-202545,407.000.000.000.0049,907.0010.19Disbursement131-Oct-202549,907.00196.840.00196.8449,907.0010.19P17-Nov-202549,907.000.000.000.0049,906.0010.19Part Payment230-Nov-202549,906.00417.900.00417.9049,906.0010.19P02-Dec-202549,906.000.000.000.0030,326.0010.19Part PaymentD08-Dec-202530,326.000.000.000.0031,326.0010.19DisbursementP09-Dec-202531,326.000.000.000.0030,325.0010.19Part PaymentP29-Dec-202530,325.000.000.000.0030,315.0010.19Part Payment331-Dec-202530,315.00268.280.00268.2830,315.0010.19P02-Jan-202630,315.000.000.000.00315.0010.19Part Payment431-Jan-2026315.0011.160.0011.16315.0010.19528-Feb-2026315.002.520.002.52315.0010.19631-Mar-2026315.002.790.002.79315.0010.19 | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | | | | | | | | | | | | | | | | Terms and Condition: The dynamic repayment details provided above are for reference only. Please refer to the Statement of Account (SOA) for actual payments, receipts, and dues. The repayment schedule is drawn from the latest facility date. Interest dues will be basis actual utilisation during the month. The “Available loan amount for disbursement” will be restricted to the net of sanctioned amount and loan amount. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #130 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #131 — User Persona Research
**Status:** ** Married with family responsibilities | **Last edited:** Unknown

# User Persona Research [V0.1 for User Research](User%20Persona%20Research/V0%201%20for%20User%20Research%206d63c60255e247f1a2d7a8b49d5a3bbd.md) [User Research Framework](User%20Persona%20Research/User%20Research%20Framework%20adba50e539a84bf8be27f3377b94ba29.md) ## Why do we need user personas - Empathise our user while designing products - Help target their goals, needs, aspirations and pain points - Make user centric product decisions ## Hypothesis ### Established Investor # Meet Rajesh Gupta - The Established Business Owner ## Demographics - **Age:** 44 years old - **Location:** Tier 1 city (Mumbai/Delhi/Bangalore) - **Profession:** Business Owner - **Income Level:** Upper middle class to affluent - **Family Status:** Married with family responsibilities ## Financial Profile - **Loan Requirements:** ₹7.35L (average for business customers) - **Primary Loan Purpose:** Working capital for business - **Investment Portfolio:** Active mutual fund investor - **Existing Loans:** Has a car loan and possibly a home loan - **Financial Behavior:** Financially aware but prefers quick solutions ## Digital Behavior - **Social Media Usage:** Moderate user of Facebook and Linkedin - **Content Consumption:** Actively watches financial/business content (56%) - **Preferred Platforms:** Newsletters (31%), Facebook (28%), YouTube (21%) - **Financial Influencers:** Follows personalities like Rachna Ranade, Akshat Srivastava ## Pain Points & Needs - **Time Sensitivity:** Needs immediate access to funds (74% unplanned loans) - **Process Friction:** Avoids traditional banks due to lengthy processes (69% don't approach banks first) - **Alternative Consideration:** Considers personal loans (41%) or borrowing (23%) before LAMF - **Social Constraints:** Hesitant to borrow from personal network despite considering it ## Decision Making Behavior - **Planning:** Generally makes quick, unplanned financial decisions for business needs - **Research:** Limited research into alternatives due to urgency - **Priority:** Views liquidating mutual funds as last resort but values speed and convenience - **Motivation:** Driven by immediate business requirements rather than personal expenses ## Product Expectations - **Core Needs:** Quick disbursement, minimal documentation - **User Experience:** Expects digital-first, seamless experience - **Post-Service:** Wants clear visibility of loan status, EMIs, and interest calculations - **Communication:** Prefers digital updates but appreciates timely reminders for payments ## Quote "Quick process, bethe bethe kaam ho gaya" (The work was done while sitting in one place) ### New Investors # Meet Aditya Shah - The Tech-Savvy Growth Seeker ## Demographics - **Age:** 28 years old - **Location:** Tier 1 city (Bangalore/Mumbai) - **Profession:** Senior Software Engineer at a tech startup - **Income:** ₹18-25 LPA - **Living Situation:** Single, lives independently in a rented apartment ## Financial Profile - **Investment Portfolio:** - Started investing 3-4 years ago - 60% equity mutual

---

## #132 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #133 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can