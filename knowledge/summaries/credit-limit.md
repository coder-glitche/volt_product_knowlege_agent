# Current State: Credit Limit

> Auto-generated from 93 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — SDK for b2b2c SAAS partners
**Status:** Not started | **Last edited:** September 30, 2024 6:06 PM

# SDK for b2b2c SAAS partners ### **Interest Details Management Table** | **Attribute** | **Description** | | --- | --- | | View Interest and Charges | Access current month due interest and charges details with respective statuses. | | Filtering | Filter by mandate status, interest status, and lender name (TATA, BAJAJ). | | Search | Search the interest details table. | | Interest Calculator | Provide tools for calculating interest. | | Pre-defined Messaging | WhatsApp messages based on interest and mandate statuses. | | Pagination | Support pagination with 50 records per page. | ### **Shortfall Management Table** | **Attribute** | **Description** | | | --- | --- | --- | | View Shortfall Amounts | Access details of shortfall amounts and aging information. | | | Sorting and Filtering | Sort by due date and filter by aging and lender name. | | | Search | Search within the shortfall details table. | | | Educational Content | Provide information on what a shortfall means. | | | Pre-defined Messaging | WhatsApp messages for communicating shortfalls to customers. | | | Pagination | Support pagination with 50 records per page. | | ### **Loan Renewals Management Table** | **Attribute** | **Description** | | --- | --- | | View Loan Renewal Details | Access loan renewal information, including statuses and due dates. | | Sorting and Filtering | Filter by lender name and status; sort by customers nearest to renewal dates. | | Search | Search within the loan renewal details. | | Educational Content | Provide information about the benefits and consequences of non-renewal. | | Pre-defined Messaging | WhatsApp messages based on loan status (Active, Expired with/without amounts). | | Pagination | Support pagination with 50 records per page. | ### **General Features Table** | **Feature** | **Description** | | --- | --- | | Tab and Page Deep Linking | Allow access to functionalities via deep links on all platforms (web, Android). | | Dynamic Tab Visibility | Display or hide tabs based on customer counts (hide when count is zero). | | Consistent Data Display | Ensure uniform data presentation across SDK and internal dashboard. | ### **Detailed Customer Information Table** | **Attribute** | **Description** | | --- | --- | | Customer Name | Name of the customer. | | Phone Number | Contact number of the customer. | | Due

---

## #2 — Update MFC limit in application - from API and lan
**Status:** Not started | **Last edited:** September 3, 2024 4:07 PM

**Problem:**
are we solving?**

Currently for B2B partners where we allow MFC fetch and RTA pledge:  Once customers checks MFC limit on their platform and logins into the SDK, the limit is not refreshed upon refreshing the limit on partner platfomrs. 

---

**Solution:**
?**

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

## #5 — Loan Offer Optimisation experiment for CheQ
**Status:** In progress | **Last edited:** September 2, 2025 5:55 AM

**Problem:**
are we solving?**

Currently we are observing low conversion rate at loan offer page selection for CheQ compared to other B2B partners for (June and Aug month) ~ 7pp lower.

**For ≥10K eligible limit (CheQ):**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 19% | 29% | 18% |

**For ≥10K eligible limit (Other B2B partners ex CheQ and PP)**

| **Step** | **Aug** | **Jul** | **Jun** |
| --- | --- | --- | --- |
| **Loan Offer selection %** | 25% | 30% | 31% |

For **July** month overview of drop-offs at each stage in the funnel from eligible cre

**Solution:**
?**

---

## #6 — BRE Proposal for cases above 1 Cr
**Status:** Done | **Last edited:** September 12, 2024 4:44 PM

**Problem:**
are we solving?**

For the users with eligible limit > 1 Cr when they complete the application with BAJAJ as lender then - 
a. SPDC (BAJAJ's Form need to be filled & signed)
b. Cancel cheque (Signed blank cheque)
c. These 2 documents need to be done by user & couriered to BAJAJ office by the user [Very high effort]
d. It takes about 3-4 days for the lodgement to be done by after the user has couriered the documents

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

## #8 — DSP BRE for Beta
**Status:** Pending Review | **Last edited:** October 28, 2024 10:53 AM

**Problem:**
are we solving?**

Currently, customers can avail a loan from Volt app or web through DSP only through whitelisting or URL based parameters. This will not be possible to handle in the beta stage as we need to route applications real-time to DSP.

In addition, the segment where the credit limit offered by Volt is between 10K and 25K is ~12% of the total eligible applications which isn’t catered to by our other lenders, Bajaj and Tata. This opens up a new set of customers for us to acquire and eventual enhance from a limit perspective. 

---

**Solution:**
?**

---

## #9 — [Lending stack] Welcome mail
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

## #10 — [Lending stack] DSP lender assignment logics
**Status:** Not started | **Last edited:** October 18, 2024 11:01 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #11 — Excess amount handling
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

## #12 — TATA Dedupe API with updated BRE
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

## #13 — MFC Summary API calculations update
**Status:** Not started | **Last edited:** November 12, 2024 3:32 PM

**Problem:**
are we solving?**

Until now due to lienEligibleUnits data discrepancy from KFin’s end, while using MFC summary API to fetch customer’s mutual funds we were making few approximations and removing all KFin ELSS funds from eligible limit. 

- This lead to lower limits shown to the users, multiple issues of eligible limit discrepancies were reported.
- Pledge errors occurred due discrepancy in available and locked units data

---

**Solution:**
?**

---

## #14 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #15 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #16 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #17 — Phase 0 LTV Tenure Update_LOS
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

## #18 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #19 — MFC Summary API integration
**Status:** In progress | **Last edited:** May 23, 2024 4:59 PM

**Problem:**
are we solving?**

Currently for the Check eligibility in 15s landing page we use the MFC CAS detailed API, this has the following problems:

1. Detailed API takes longer to give CAS response.
2. Detailed API in alot of cases gives locked units as available units.

Shifting to CAS summary API will solve both of these problems. 

---

**Solution:**
?**

---

## #20 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #21 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #22 — Term Loan LOS requirements
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

## #23 — [Volt LSP] Supporting multiple products for same c
**Status:** Not started | **Last edited:** March 5, 2025 6:06 PM

**Problem:**
are we solving?**

Immediate problem: 
BFL has stopped new applications (Including enhancement) with Volt. Current customers who want to enhance their credit line are not able to do so. To solve their need of enhancing their credit limit we are thinking of a dual credit line solution where the customer will open a new credit line with DSP and the existing credit line from BFL/Tata will remain active. 

---

**Solution:**
?**

---

## #24 — Mandate limit change
**Status:** Not started | **Last edited:** March 5, 2025 3:41 PM

# Mandate limit change # Credit Limit Increase Analysis (Excluding <10K Initial Credit Limit) Based on the analysis of 10,467 valid records with initial credit limits of 10K or greater, here's the comprehensive breakdown: ## Applications by Initial Credit Limit Range and Percentage Increase | Initial Credit Limit | 0-400% | 400%-600% | 600%-800% | 800%-1000% | 1000%+ | Total | | --- | --- | --- | --- | --- | --- | --- | | 10K-25K | 119 | 13 | 8 | 2 | 16 | 158 | | 25K-1L | 2,361 | 78 | 24 | 25 | 84 | 2,572 | | 1L-5L | 4,393 | 81 | 51 | 27 | 41 | 4,593 | | 5L-25L | 2,432 | 42 | 17 | 8 | 18 | 2,517 | | 25L+ | 620 | 6 | 1 | 0 | 0 | 627 | | **Total** | 9,925 | 220 | 101 | 62 | 159 | 10,467 | ## Percentage Increase Distribution | Range | Count | Percentage | | --- | --- | --- | | 0-100% | 7,858 | 75.07% | | 100%-200% | 1,383 | 13.21% | | 200%-300% | 471 | 4.50% | | 300%-400% | 213 | 2.03% | | 400%-500% | 133 | 1.27% | | 500%-600% | 87 | 0.83% | | 600%-700% | 57 | 0.54% | | 700%-800% | 44 | 0.42% | | 800%-900% | 29 | 0.28% | | 900%-1000% | 33 | 0.32% | | 1000%-1500% | 58 | 0.55% | | 1500%-2000% | 28 | 0.27% | | 2000%+ | 73 | 0.70% | ## Applications with 400%+ Credit Limit Increase by Range | Initial Credit Limit | Count | % of Range | | --- | --- | --- | | 10K-25K | 39 | 24.68% | | 25K-1L | 211 | 8.20% | | 1L-5L | 200 | 4.35% | | 5L-25L | 85 | 3.38% | | 25L+ | 7 | 1.12% | | **Total** | 542 | 5.18% | ## Cumulative Distribution | Up to | Count | Percentage | | --- | --- | --- | | 100% | 7,858 | 75.07% | | 200% | 9,241 | 88.29% | | 300% | 9,712 | 92.79% | | 400% | 9,925 | 94.82% | | 500% | 10,058 | 96.09% | | 600% |

---

## #25 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #26 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #27 — Margin pledge charges
**Status:** Pending Review | **Last edited:** June 5, 2025 7:19 PM

**Problem:**
are we solving?**

- Currently, DSP Finance offers a maximum sanction limit of ₹2,00,00,000, allowing users to pledge collaterals post-account opening up to this limit (calculated as NAV × LTV × Units) to access credit.
- However, this leads to cost implications such as lien marking charges, ongoing tech maintenance, and operational overheads, which are not being recovered from users today. To address this and improve monetisation, we plan to introduce pledge invocation charges, applicable when users pledge additional securities to increase their credit limit.
- As of April 30, DSP Finance has

**Solution:**
?**

We will be applying margin pledge charges (Additional pledge charges) on the user’s loan account. Margin pledge charges will be applied. The same will be added in the product construct.

---

## #28 — Increase Credit Utilization via Whatsapp Drips
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

## #29 — Unlock credit limit revamp
**Status:** Not started | **Last edited:** June 24, 2024 10:53 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #30 — Margin pledge charges
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

## #31 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #32 — [Jupiter] Unlock credit limit page changes
**Status:** Not started | **Last edited:** July 31, 2024 5:41 PM

**Problem:**
are we solving?**

Change copies on the verify interest and charges page for partners with MFC fetch. 

---

**Solution:**
?**

---

## #33 — Repayment Lifecycle Tracking
**Status:** Not started | **Last edited:** July 22, 2024 10:29 AM

**Problem:**
are we solving?

- Users currently are not able to see the status of their transactions once a repayment is done till it is settled by the lender in their statement of accounts.
    - Users are not able to see the updated credit limit and the transaction and want to know the status of the transaction.
        - Payment takes 1-2 days to get updated in the loan account (Then it gets visible to the user)
    - This makes them follow up with our Ops/Support teams via support channels to confirm if their payment was received by us.
    - This consumes a lot of time for the support team and is crea

**Solution:**
?

We are solving this problem for the user by the following ways:

- Add a pending transaction in transactions section with status in progress till the time it is settled by the lender (transactions section - ledger)
    - [**Transaction status management**](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- On payment success screen in the flexi pay screen, communicate to the user the steps and timeline for the settlement with the lender.
    - [UI and cases that need to be handled](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
    - [Accounting and Settlement](Repayment%20Lifecycle%20Tracking%2078fa41d1303d42618155771cd05196bf.md)
- Actively sharing the status of the transaction made by the user (Transaction Success/ Transaction settled) 

---

## #34 — [Platform] BRE configurations for approval tasks
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

## #35 — MFC in-app journey
**Status:** In progress | **Last edited:** January 5, 2025 4:07 PM

**Problem:**
are we solving?**

Currently for Volt in-app journeys customers are required to fetch from CAMS and KFin separately. This results in increased customer drop-off because of the following reasons:

- User comprehension: The initial limit fetched from CAMS is roughly 60% of the total limit of the customer, customers don’t clearly understand that they need to fetch from KFin to get their complete eligible limit.

The same is reflected in the funnel numbers below: 

- High friction: Two OTPs required for complete fetch.

[https://app.amplitude.com/analytics/volt-hq/chart/new/za7my7iy](https://app.a

**Solution:**
?**

---

## #36 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #37 — [Fenix] Lodgement maker bulk approval
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

## #38 — [Final] End use capture of transactions
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

## #39 — [CC] Lodgement Enhancement
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

## #40 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #41 — Measuring Customer Support Events and 5XX errors
**Status:** Ready for Tech | **Last edited:** February 28, 2024 12:08 PM

**Problem:**
are we solving?**

- To accurately identify and measure user support issues in the loan application journey on a step by step level.
- To identify internal API errors and flow breakages in our flows and to be able to map them with respective flows to understand product and tech level issues
- Track assisted and non assisted journeys
- Identifying UX and copy issues

**Context:**

A lot of our users contact support (WA/Call/Email) while applying for a credit line and need assistance to complete the application. In most cases, our RMs end up assisting the customer in completing the application.


**Solution:**
?**

---

## #42 — Product note - DRPS
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

## #43 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #44 — Shortfall communication enhancement Ignoring accou
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

## #45 — Pre-fetch flow Optimisation Consolidating PAN flow
**Status:** Done | **Last edited:** February 19, 2026 9:43 AM

**Problem:**
are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

**Solution:**
?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

---

## #46 — Interest, shortfall, renewal table on partner dash
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

## #47 — LSQ data sync
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

## #48 — Annual Maintenance Charges (AMC)
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**DSP offers a credit line facility to users for a tenure of 3 years.** Maintaining this credit line involves ongoing costs including customer servicing, technology infrastructure, portfolio monitoring, and operational overheads.

To ensure the long-term sustainability of the offering and continue delivering high-quality service, **we propose introducing an Annual Maintenance Charge (AMC)**. This will serve as a recurring revenue stream to offset the costs associated with account maintenance and user support throughout the lifecycle of the credit line.

---

**Solution:**
?**

We will be applying AMC on the user’s loan account. AMC will be applied at the end of every year(should be calculated based on account opening date). The same will be added in the product construct.

AMC is Non-contingent charge: will be charged unconditionally whether there is 100%  utilization also.

---

## #49 — Capture foreclosure reasons from customer
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

## #50 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #51 — MFC fetch in Volt Journey
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Allow users to fetch their folio using the MFC API to calculate the eligible credit limit during loan applications, limit increases, and loan renewals.
    - Streamline the process by requiring users to enter only one OTP to fetch the entire folio.
    - This reduces cognitive load, as they currently need to enter two OTPs when fetching or refreshing folios from both CAMS and KFIN.
    - Allow user to continue loan application journey without requiring to fetch again with CAMS and KFIN if user has already fetched folio with MFC on other platform like Volt landing page, par

**Solution:**
?**

---

## #52 — Project Elevate - LMS
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

## #53 — TCL Dynamic repayment schedule
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

## #54 — Untitled
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Untitled ```mermaid flowchart TD A[User Login] --> B{Account Status Check} B --> C[Only LAS Account] B --> D[Only LAMF Account] B --> E[Both Accounts] B --> F[No Accounts] %% Only LAS Flow C --> C1[LAS Dashboard] C1 --> C2{User Action} C2 --> C3[View Account Details] C2 --> C4[Make Repayment] C2 --> C5[Top Up Collateral] C2 --> C6[Apply for LAMF] C2 --> C7[View Statements] C6 --> G[LAMF Application Flow] G --> G1[Document Upload] G1 --> G2[Verification] G2 --> G3[Approval/Rejection] G3 --> |Approved| H[Dual Account User] G3 --> |Rejected| C1 %% Only LAMF Flow D --> D1[LAMF Dashboard] D1 --> D2{User Action} D2 --> D3[View Account Details] D2 --> D4[Make EMI Payment] D2 --> D5[Top Up Collateral] D2 --> D6[Apply for LAS] D2 --> D7[View Statements] D6 --> I[LAS Application Flow] I --> I1[Collateral Setup] I1 --> I2[Verification] I2 --> I3[Approval/Rejection] I3 --> |Approved| H I3 --> |Rejected| D1 %% Both Accounts Flow E --> H[Unified Dashboard] H --> H1{Account Selection} H1 --> H2[LAS View] H1 --> H3[LAMF View] H1 --> H4[Combined View] H2 --> H5{LAS Actions} H5 --> H6[LAS Account Details] H5 --> H7[LAS Repayment] H5 --> H8[LAS Top Up] H5 --> H9[Switch to LAMF] H3 --> H10{LAMF Actions} H10 --> H11[LAMF Account Details] H10 --> H12[LAMF EMI Payment] H10 --> H13[LAMF Top Up] H10 --> H14[Switch to LAS] H4 --> H15{Combined Actions} H15 --> H16[Cross-Account Summary] H15 --> H17[Unified Repayment] H15 --> H18[Portfolio Analysis] H15 --> H19[Recommendations] %% No Accounts Flow F --> F1[Welcome Screen] F1 --> F2{Product Selection} F2 --> F3[Apply for LAS] F2 --> F4[Apply for LAMF] F2 --> F5[Learn More] F3 --> J[LAS Onboarding] F4 --> K[LAMF Onboarding] %% Common Flows C4 --> L[Repayment Flow] D4 --> L H7 --> L H12 --> L H17 --> M[Multi-Account Repayment] L --> L1[Select Amount] L1 --> L2[Choose Payment Method] L2 --> L3[Confirm Payment] L3 --> L4[Payment Processing] L4 --> L5{Payment Result} L5 --> |Success| L6[Success Screen] L5 --> |Failed| L7[Error Handling] M --> M1[Allocate Amount] M1 --> M2[Choose Payment Method] M2 --> M3[Confirm Split Payment] M3 --> L4 C5 --> N[Top Up Flow] D5 --> N H8 --> N H13 --> N N --> N1[Select Collateral Type] N1 --> N2[Enter Amount/Quantity] N2 --> N3[Verify Collateral] N3 --> N4[Confirm Top Up] N4 --> N5[Processing] N5 --> N6{Result} N6 --> |Success| N7[Success Screen] N6 --> |Failed| N8[Error Handling] %% Support & Help C1 --> O[Help Center] D1 --> O H

---

## #55 — Volt Apps & Web Multiple Loan Handling - Launching
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

DSP Finance is launching **LAS (Loan Against Shares) for B2B2C customers**. 

To enable customers to seamlessly manage their LAS loan accounts, we need to build a **scalable, modular, and user-friendly loan servicing experience** within the Volt platform.

The servicing module must support:

1. **LAS loan management** — for customers availing loan against shares
2. **LAMF loan management** — for existing customers availing loan against mutual funds
3. **Unified product** — for users holding **both LAS and LAMF**, offering an intuitive, consistent experience across products 


**Solution:**
?**

Volt will provide a **modular loan account management system** that supports:

1. **LAS-only servicing**
2. **LAMF-only servicing**
3. **Hybrid servicing (both LAS + LAMF[Multi-lender])**
    1. Support of multiple loan type(OD, TL) under the umbrella of different product type (LAMF, LAS)
4. **Cohesive communication and notification design for both products**
    1. **Messages are clearly distinguished yet work seamlessly together, preventing confusion for users managing multiple loan products⁠**

---

## #56 — Reducing Limit on DSP from 25K
**Status:** In progress | **Last edited:** December 6, 2024 3:39 PM

**Problem:**
are we solving?**

Currently, a lot of customers, especially in the B2B channels are dropping off due to the limit fetched being < 25,000. 

- ~5000 customers/month across channels (B2B, B2C) aren’t being serviced for having a limit b/w 10K and 25K
- ~4000 customers/month across channels (B2B, B2C) aren’t being serviced for having a limit b/w 5K and 10K
- Loss of customers to competitors like Fibe and Abhiloans who are servicing customers with limits of 15K and 7.5K respective
- Loss of revenue from PF and interest fee due to customers not taking a loan from DSP

These customers aren’t service

**Solution:**
?//.**

---

## #57 — [Platform] Risk report
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

## #58 — Single drawdown Term Loan LMS Requirements
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

## #59 — [Tata Neu] Bottom sheet to nudge user to withdraw
**Status:** Not started | **Last edited:** August 6, 2024 5:19 PM

**Problem:**
are we solving?**

Post completion of application, users currently land on the dashboard page. The user now has multiple actions that they can perform which can distract them from the primary use case of customers withdrawing from their credit limit. 

Problem statement is to nudge user to place a withdrawal request as soon as the customer lands on the dashboard page.

---

**Solution:**
?**

---

## #60 — SL updation & additional limit calculation optimis
**Status:** On Hold | **Last edited:** August 27, 2024 5:20 PM

**Problem:**
are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

**Solution:**
?**

---

## #61 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #62 — Product Note – DRPS (Final Version – Unified Forma
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

## #63 — PRD MFC Revised Flow
**Status:** Not started | **Last edited:** April 14, 2026 1:03 PM

**In scope:**
- 
    - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including::
        - Partners who have directly integrated with MFC  fetch flow (eg-Paytm)
        - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter)
        - Partners who are using Volt fetch journey

# PRD: MFC Revised Flow ## **Background and Context** - - Since MFC is going to deprecate the MFC fetch apis and moving to SDK based flow for fetching (concerns from AMFI around fintech platforms accessing investor data freely w/o explicit customer consent.) - This change is expected to go live by 31st January - Since all Volt channel flows (B2B,B2C & B2B2C) as well as LSP flows will be impacted by this change, figuring out how to tackle this transition to esnure business continuity in the near and long terms is critical --- ## **1. Problem scope** ### In scope - - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including:: - Partners who have directly integrated with MFC fetch flow (eg-Paytm) - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter) - Partners who are using Volt fetch journey ### Out of scope - N~~ot covered as part of current scope:~~ - ~~Loan journey changes ‘post fetch’ for Volt channels~~ - ~~B2C website journey changes wrt MFC SD~~K - While the MFC SDK flow implementation is currently suboptimal from tech/ UX POV, improving it by working with the MFC team is not feasible given our tight deadline. --- ## **2. Success Criteria** - - Overall fund fetch SR & first time SR - Overall Fetch TAT - MFC SDK flow SR & TAT - MFC SDK & RTA flow stability /uptime ## **3. Solution Scope** ### [Detailed solution /Journey](https://whimsical.com/internal-mfc-fetch-updated-flow-copy-FDDhzqEJNzTbNnkUCW73b5) ### 1. Entry point (Volt/LSP channels) Volt B2C - Android/IOS app/Partner app: DSP SDK will be triggered on on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen ![Screenshot 2026-02-08 at 2.51.52 PM.png](PRD%20MFC%20Revised%20Flow/Screenshot_2026-02-08_at_2.51.52_PM.png) - ‘Sign in’ entry point on Website : DSP SDK will be triggered on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen in the web app - Check eligibility’ entry point on VoltWebsite: DSP SDK will be triggered on submitting ‘PAN & mob no’ screen & will open in an iframe Volt B2B2C/B2B partners - Partners fetching in own UI:The ‘DSP SDK’ flow is triggered from the partner UI - Partners using Volt UI for fetching: Flows will be same as that mentioned under ‘B2C’ section LSP - The ‘DSP SDK’ flow is triggered from the partner UI ### 2.User

---

## #64 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #65 — Enhance limit Research
**Status:** Unknown | **Last edited:** Unknown

# Enhance limit Research ### Objective 1. **User Motivation:** Why do people enhance their limit? 2. **Mental Models** How do they currently think about credit lines? - Currently our users think about credit line like a personal loan, They only choose increase their credit limit if they are in need. - What we can work towards is building the mindset like a credit card where increased credit limit is something people go for even when they don’t feel the need for it. - Folks tried to 3. **Context of Use** When do they increase limit? - After a withdrawal (they see low balance) - Utilisation > 70% - If they see the value of their MF has increased. . . 4. **Flow Drop Offs** Why do users abandon this? - Users who dropped out usually didn’t get the limit they wanted - They also were ineligible for the loan since there is a 10K limit Unclear next steps. Lack of feedback Screen fatigue 5. **Purpose & Value** Why does this feature matter to users? > It’s a fast, low-effort way to access more cash without applying for a new loan. KYC, Mandate and Agreement not required (If new total limit is below SL) > --- ### Feedback from users - No one complained of any difficulty, lack of information for dropping off. - When asked “What’s one thing stopping you from increasing your limit right now?” - The answer always is they don’t have the need for it. - Minimum 10K being the reason for drop-off. --- ### Segments of Users and Questionnaire 1. **Repeat Users (Used Top-Up More Than Once- Ideal Users)** - Why did you “Enhance Limit”? - What made you come back and do it again? - How easy or difficult was it to find the increase limit option? - Was anything unclear or unexpected in your experience? - Hindi - Aapne pehli baar limit enhance kyun kiya tha? - Aapne phir se kyun kiya? - Pura process aapko kaisa laga — easy ya confusing? - Koi ek step jo aapko helpful ya clear laga? - Aapko paise milne mein kitna time laga tha? - Kya koi cheez aisi thi jo alag thi ya samajh nahi aayi? - Aapko is process pe trust kyun hua? - Aapne jo extra limit mili uska use kaha kiya? - Kya kuch aisa hai jo aur better banaya ja sakta hai?

---

## #66 — Line enhancement nudge
**Status:** Ready for kickoff | **Last edited:** Unknown

# Line enhancement nudge Charter: LMS Pod Priority: P0 # Context [Increase Top-up TOFU & conversion [TCL & DSP]](../PRDs/PRDs/Increase%20Top-up%20TOFU%20&%20conversion%20%5BTCL%20&%20DSP%5D%20203e8d3af13a80ba82aeef50d440f823.md) # Process - [x] Understand scope [Enhance limit Research](Line%20enhancement%20nudge/Enhance%20limit%20Research%2020ae8d3af13a8010a645c3a79ab76e8e.md) - [ ] Benchmarking - [ ] Messaging - [ ] Illustration - [ ] Concept - [ ] Touchpoints - [ ] Messaging - [ ] Design # Figma

---

## #67 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #68 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #69 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #70 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #71 — LaMF funnel
**Status:** Unknown | **Last edited:** Unknown

# LaMF funnel To document a funnel from a product manager's perspective, especially for opening a credit line with multiple third-party APIs involved, you can follow these steps: ### 1. **Define the Funnel Stages** - **Map the key stages** of the funnel from a user’s perspective. Each stage should represent a meaningful user action: 1. ### 2. **Identify Touchpoints & Third-Party API Dependencies** - **For each stage**, document which third-party API is involved and what data is exchanged. - **E.g.,** ### 3. **Track Conversion & Drop-off Metrics** - At each stage, define **conversion rate** (users who successfully pass to the next stage). - **Identify drop-offs**: Calculate how many users fail or exit the flow at each stage and investigate why. - **E.g., Eligibility Check** → 75% conversion, 25% drop-off due to API failure or ineligible users. ### 4. **Diagnose Breakpoints & Flow Bottlenecks** - **API Response Failures**: Track the rate of success and failure for API calls (e.g., timeout, invalid responses, high failure rate in the KYC stage). - **User Frustration Points**: Analyze user sessions to find out if there are UI/UX challenges (e.g., users leave due to complex form submissions or unclear messaging). - **Incomplete User Inputs**: Check if the flow is breaking due to missing or invalid user input (e.g., incorrect document uploads or failed validation). ### 5. **Attribution of Drop-offs** - **Tag each drop-off** with an attribution reason: 1. **Technical** (API failure, timeout, or 500 error). 2. **User Behavior** (abandonment, confusion with next steps). 3. **Eligibility** (e.g., failed credit check or ineligibility). ### 6. **Major Pain Points** - **Highlight user pain points** by reviewing feedback, support tickets, and analytics. - **E.g., KYC Step**: Users frequently abandon due to the complexity of document uploads. - Use qualitative feedback (e.g., user interviews, support chats) alongside quantitative data (e.g., Google Analytics, session recordings). ### 7. **Set Up Conversion Tracking** - Use **attribution tools** to track how users are progressing through the funnel, and set up **event tracking** in Google Analytics or similar. - **For each stage**, track key metrics like: 1. Average time spent. 2. Bounce rates. 3. API success/failure rates. ### 8. **Monitor Real-Time Data** - Implement **dashboards** that allow you to monitor API response times, error rates, and user journeys in real-time. - Example tools: **DataDog** for API monitoring, **Hotjar** for session recording, **Google Analytics** for user tracking. ### Example Documentation Flow: ``` 1. Stage 1: User Signup

---

## #72 — Missed calls from customers aren't being called ba
**Status:** Unknown | **Last edited:** Unknown

# Missed calls from customers aren't being called back or addressed # Missed Calls and Customer Support Optimization Missed calls from customers are a significant issue, as many are not being addressed. Customers reach out to us for help during various stages, such as onboarding, opening credit lines, post-account opening support, or product inquiries. To effectively manage these requests and reduce missed calls, we need a strategy that not only addresses customer needs but also balances the cost of support channels. ## Understanding the Support Categories: We can categorize customer interactions into three key areas: 1. **Awareness**: Customers seek to understand the product better. 2. **Sales**: Customers eligible for the service but who have not yet opened an account. 3. **Support**: Customers who already have accounts and need assistance with specific issues. ## Support Channel Options: There are several ways we can provide support, each with its own cost and effectiveness: - **Online Documentation**: Free but less accessible for most users. - **Product Journey (In-App Help)**: Accessible but costly in terms of development time. - **Chat Support**: Affordable and accessible for general queries. - **Call Support**: Highly impactful but also the most expensive to maintain. ### Optimizing Customer Support: Our goal is to provide the right support channel for each category of customer, depending on their needs, to maximize effectiveness while minimizing costs. This means segmenting customers into "buckets" based on their status and needs and directing them to the appropriate support channel: | **Bucket** | **Identifier** | **Channel to Retarget** | | --- | --- | --- | | **Awareness** | No record of the number in the system, ineligible | Chat or WhatsApp | | **Sales** | Eligible number, account not yet opened | Call Support | | **Support** | Customer with an open account | Chatbot with common services | ### Proposed Changes: To reduce call support costs, we should remove the call option for ineligible customers and instead provide them with WhatsApp support. This will help to ensure that calls are only directed to customers who are further along the funnel, and likely to require higher-touch support. ### Key Objectives: - **Address customer needs** through the appropriate support channels. - **Reduce support costs** by minimizing unnecessary call support. - **Reduce missed calls and errors** by routing customers more effectively. ### Data Requirements: To implement this strategy, we need to collect and analyze the following data: -

---

## #73 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #74 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #75 — Risk management system LAS
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

## #76 — Tally ERP Integration
**Status:** Completed | **Last edited:** Unknown

# Tally ERP Integration Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # **Tally Journal Voucher API Contract (Sample Document)** This document outlines the proposed API contract for pushing journal voucher entries from the LMS/ERP system to Tally. Each journal voucher corresponds to a single **transaction event**, containing one or more **ledger-level debit/credit lines** with consolidated amounts. --- ## **1. API Overview** ### **Endpoint** (To be shared by the vendor) ### **Purpose** Push a complete journal voucher entry at a transaction type level to Tally for accounting purposes. --- ## **2. Request Structure (Batch Journal Posting)** The API will support **batch posting** of journal vouchers. Each request will contain an **array of transactions**, where each object represents one complete journal voucher. ### **2.1 Journal Voucher Batch Payload** ```json [ { "transaction_type": "string", "narration": "string", "voucher_date": "YYYY-MM-DD", "tally_txn_id": "1234564534432", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" } ] }, { "transaction_type": "string", "narration": "string", "tally_txn_id": "1234564534433", "voucher_date": "YYYY-MM-DD", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" }, { "ledger_name": "Sample3", "debit": "number", "credit": "number" } ] } ] ``` --- ### **Field Description** | Field | Type | Description | | --- | --- | --- | | transaction_type | string | Preconfigured transaction type (ex: PAYIN, PAYOUT) | | tally_txn_id | string | Unique transaction identifier used as **dedupe key** | | voucher_date | date | Voucher posting date | | narration | string | Narration mapped to transaction type | | ledger_entries | array | List of debit/credit ledger lines | --- ### **Ledger Entry Object** | Field | Type | Description | | --- | --- | --- | | ledger_name | string | Name of the ledger in Tally | | debit | number | Amount debited (zero if not applicable) | | credit | number | Amount credited (zero if not applicable) | --- ## **3. Transaction Type Samples** Below are examples for each transaction type based on provided data. --- ## **3.1 ADD_FEE** **Narration:** Being fee income recognition ```json { "tally_txn_id": "<unique-id>", "transaction_type": "ADD_FEE", "voucher_date": "2025-01-01", "narration": "Application of fee on loan account", "ledger_entries": [ {"ledger_name": "Fees receivable", "debit": 7109825, "credit": 0}, {"ledger_name": "Income from Fees", "debit": 0, "credit": 6025269}, {"ledger_name": "CGST Payable", "debit": 0, "credit": 90382}, {"ledger_name": "SGST Payable", "debit": 0, "credit":

---

## #77 — Unpledge - Stocks selection logic
**Status:** Completed | **Last edited:** Unknown

**Solution:**
?**

---

## #78 — Volt - Shortfall Communication Enhancement – Due D
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

## #79 — [Platform] Mandate collection enhancement
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

## #80 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #81 — SEO Text
**Status:** Unknown | **Last edited:** Unknown

# SEO Text A Loan against mutual funds (LAMF) allows you to borrow money by using your mutual fund units as collateral. Volt Money’s loan against mutual funds calculator can help you estimate the interest costs associated with this financing option. **What is a loan against mutual funds (LAMF)?** A loan against mutual funds (LAMF) is a secured loan where you pledge your mutual fund units as security to borrow money. The lender will determine the maximum loan amount you can qualify for based on a Loan-to-Value (LTV) ratio. This ratio represents the percentage of your mutual fund's market value that the lender is willing to lend against. You are then issued a credit limit which functions like a bank overdraft facility, where you are charged interest only on the amount you withdraw from this credit limit. **How to get a loan against mutual funds?** With Volt Money, you can get loan against mutual funds in 4 simple steps: 1. Check credit limit: We’ll evaluate your mutual fund portfolio & confirm credit limit. Check your credit limit from here. 2. Instant KYC: Complete digital KYC process. No paperwork required! 3. Pledge your assets: Mark your mutual funds as a security with a trusted lender. 4. Withdraw money: Withdraw & repay as per you requirement. No hidden charges. **How interest is calculated on loan against mutual funds?** Loan against mutual fund works like a bank overdraft limit, where you are only charged interest on the amount you withdraw. Interest is calculated daily and is deducted on a particular date every month. Interest calculation works on the following formula: Daily interest = P*(R/365) Monthly interest = Daily interest*N P = Principal outstanding on the day R = Annual rate of interest N = Number of days in a month Example: Suppose you withdraw ₹50,000 from Volt Money credit line at an interest of 10.49%. The daily interest rate would be calculated as (10.49% / 365) = 0.0287% per day. If the limit is utilized for 30 days, the interest accrued would be: *Interest = ₹50,000 × 0.0287% × 30 = ₹43.05* You can also make part payments to reduce your principal outstanding and thus reducing your interest payable. **Why Volt money’s overdraft like credit limit is better than a loan?** 1. Flexibility: With Volt money’s credit limit, you only pay interest on the amount you actually use, and you can repay it

---

## #82 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #83 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #84 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #85 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #86 — Term Loan Foreclosure
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

## #87 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #88 — Thanks a lot for the explanation Can you also link
**Status:** Solutioning pending | **Last edited:** Unknown

# "Thanks a lot for the explanation. Can you also link to the documentation for this as I couldn't find it directly mentioned in the site, although LLA referenced it. My other query is : The processing fee of 999+GST will be applicable each time I make a withdrawal, or only during the creation of the credit line?" Classification: Processing Fee Notes: User asked if processing fees will be charged every time they make withdrawal, how to ensure this communication is straightforward PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 917005467390 Status: Solutioning pending

---

## #89 — User was given a higher sanction amount than their
**Status:** Solutioning pending | **Last edited:** Unknown

# User was given a higher sanction amount than their credit limit, was able to place a withdrawal request before lodgement was done Classification: Sanction Amount and credit limit handling Notes: Sanction amount instead of credit line amount is shown to the customer before lodgement, ideally withdrawal should be blocked or better communicated, there should be a failed state for all transactions PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13404 Status: Solutioning pending

---

## #90 — Content
**Status:** Unknown | **Last edited:** Unknown

# Content 1. Title: Loan offer 2. Hero details: 1. Selected loan amount. 2. Credit limit available. 3. Benefits: 1. Trusted lender Tata capital 2. Unlimited withdrawals 3. Repay principal anytime 4. Pay interest only on what you withdraw 5. Monthly Interest only EMI of only ₹862 for ₹1,00,000 withdrawal at 10.49% interest (Interest should be communicated upfront) 4. Charges: 1. Interest rates: 10.49% p.a. 2. Early repayment/ foreclosure: Free 3. Withdrawals: within 4 hours 4. One time processing fee (excl. GST): ₹840 1. Processing fee is charged once in the whole term 5. Stamp duty (as per registration state): ₹260 6. Term: 36 months (Renewal available) 5. CTA: 1. Withdraw in 4 steps

---

## #91 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements ![Untitled](Design%20requirements/Untitled.png) ![Untitled](Design%20requirements/Untitled%201.png) 35% users drop off from the loan summary(Verify interest and charges page) Problems we have identified: 1. Users think that this is the last page of the application. 2. Benefits are not properly communicated. 3. User thinks that the PF is too high. Things that we want to communicate with this page: 1. Highlight selected credit limit, remove selected mutual funds: This might be reminding the users that they are pledging alot of MFs for the limit that they are getting. 2. Show maximum credit limit (maybe). 3. Unlimited withdrawals, repay anytime: Communicate benefits. 4. Pay interest only on the amount you use: Communicate benefits. 5. Monthly interest only EMIs, we can show this for 1,00,00 withdrawal and user can change it to see the IOEMI change: This will quantify the interest that they have to pay 1. 10.49% might feel high but IOEMI will be low for default sum of 1,00,000 2. This will communicate that they only have to pay interest on the sum withdrawn 6. Provided by our trusted lender Tata Capital: User trust 7. Highlight zero hidden charges before showing the charges: User should know that we are transparent with our charges. 8. Other details to be in bottom 25% of the screen: [Content ](Design%20requirements/Content%20aa1bb6ecad904d00b07393fa73ff756a.md)

---

## #92 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: rate of interest, foreclousure, processing fees, lein removal, repayment, additional top up, stocks, Kevin (Servicing): Instant disbursals, Delays, Unpledging and Forclosure. ELSS funds are possible for TATA, Schedule the loan disbursal time, Mahesh: Interest, How it works, Repayment. phone pe traffic is greater than influencers, Reconstruct their houses. Names: Main areas of concerns Naveen: Portfolio value, Location. I dont feel like I am doing the Pledging step Requirement : Urgency. Pay somebody, reinvest, NFO Bugs on app vs web

---

## #93 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are