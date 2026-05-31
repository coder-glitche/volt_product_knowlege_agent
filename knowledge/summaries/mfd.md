# Current State: Mfd

> Auto-generated from 87 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Update MFC limit in application - from API and lan
**Status:** Not started | **Last edited:** September 3, 2024 4:07 PM

**Problem:**
are we solving?**

Currently for B2B partners where we allow MFC fetch and RTA pledge:  Once customers checks MFC limit on their platform and logins into the SDK, the limit is not refreshed upon refreshing the limit on partner platfomrs. 

---

**Solution:**
?**

---

## #2 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #3 — MFD Partner Servicing revamp
**Status:** Not started | **Last edited:** October 29, 2024 12:05 PM

**Problem:**
are we solving?**

- Currently we have are missing 30% of the calls from MFD
- MFD primary complain is regarding servicing
- We can track and highlight missing SLAs
- No categorisations of the inbound issues

[Current Volt setup ](MFD%20Partner%20Servicing%20revamp/Current%20Volt%20setup%2012ee8d3af13a8039826df2f291258f48.md)

---

**Solution:**
?**

---

## #4 — MFD Payouts
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

## #5 — DSP MFD Flows
**Status:** Not started | **Last edited:** November 9, 2024 5:28 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #6 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #7 — MFC Summary API calculations update
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

## #8 — MFD Tier & Performance Data Activity Passing in LS
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

## #9 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #10 — Enhancement to MFD partner Signup page
**Status:** Pending Review | **Last edited:** May 8, 2025 4:19 PM

# Enhancement to MFD partner Signup page **Product Updates** ## **1. Enhanced Partner Login Experience:** - **Feature:** Mobile Number Pre-fill & Browser Autofill Support. - **Problem:** Returning partners re-enter mobile numbers, causing friction. - **Goal:** Faster, more convenient login. - **Solution:** - **Custom Pre-fill:** Store last successfully used/OTP-requested mobile number in browser local storage for automatic pre-population. (Editable by partner). - **Browser Autofill Hint:** Add autocomplete="tel" to the mobile number field to allow browsers (like Chrome) to suggest saved phone numbers. - **Benefit:** Quicker login, reduced errors, improved partner experience. ## **2. Improved Partner Empanelment Form:** - **Feature:** Browser Autofill for Empanelment Details. - **Problem:** Manual entry of common details (name, email, city, company) is time-consuming. - **Goal:** Faster and more accurate empanelment. - **Solution:** Implement standard HTML autocomplete attributes (e.g., name, email, address-level2, organization) on relevant input fields. - **Benefit:** Quicker form completion, fewer typing errors, smoother empanelment. ## **3. Branding & Content Updates:** - **Logo Update:** Replaced Bajaj Finserv logo with DSP logo in "Our trusted partners" section. - **Partner Count Update:** Updated "2000+ Partners have joined Volt Money" to "3000+ Partners have joined Volt Money". - **Benefit:** Reflects current partnerships and growth accurately.

---

## #11 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #12 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #13 — MFC Pledge error handling - V1 (1)
**Status:** In progress | **Last edited:** May 4, 2026 5:20 PM

**Problem:**
are we solving?**

- Currently, as we have made MFC Pledge live for B2B2C and B2C channels and plan to dial up for other channels as primary mode for pledging, we need to address and handle the top errors that have occurred until now.
- Currently, these errors are not handled: users see generic failure messages and raise tickets with customer support.
- This creates friction in the journey, increases TAT for resolution, and causes user drop-offs.

**Goal:** Show clear, actionable error messages for the most frequent pledge errors in frontend so users can self-resolve or know what to do next, r

**Solution:**
?**

---

## #14 — Bulk Upload mapping of RM and MFDs
**Status:** Not started | **Last edited:** May 28, 2025 2:57 PM

# Bulk Upload mapping of RM and MFDs To enable a one-time bulk update of the mapping between Relationship Managers (RMs) and MFDs, and ensure that the updated mappings are reflected in the Volt Partner Dashboard. - Develop a script to bulk update the RM to MFD mapping. - Save and document the script for future reference. - Ensure that the updated RM to MFD mappings are reflected in the Volt Partner Dashboard. > Summary > > - Update outdated RM (Relationship Manager) mappings in MFD dashboards to show correct RM information.- > https://docs.google.com/spreadsheets/d/1aX1thTESwja-n1J-LL1rgCydee2pp6aKZ5igGUTLGgU/edit?gid=0#gid=0 > > - MFD dashboards are showing incorrect RM numbers due to an LSQ bulk upload. Need to sync with current RM assignments using existing API endpoints. > - Update RM-MFD mapping table with current data > - Verify all dashboards show correct RM numbers > - Confirm data consistency between LSQ and MFD dashboard

---

## #15 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #16 — PRD – Volt MFD Payouts Process
**Status:** In progress | **Last edited:** May 27, 2025 2:52 PM

# PRD – Volt MFD Payouts Process # **PRD – Volt MFD Payouts Process** ## **1. What Problem Are We Solving?** ### **Key Issues Identified** 1. Business continuity risk as we are too dependent on one analyst for the calculations 2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~ 3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries. 4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts. 5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed. 6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS). 7. **Support Visibility:** No centralized tracking for payout-related support issues. 8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files. 9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails. 10. **GSTN Verification:** No automated verification of correct GST numbers. --- ## **2. Changes needed for Payout automation (Current vs. Proposed)** | Database | Current | Proposed | | --- | --- | --- | | Application Data | DB | No change | | Transaction Data | DB | No change | | Principle Outstanding | Google Sheets | DB | | Partner Commercials | Google Sheets | DB | | Payout Ledger Table | Google Sheets | DB | | Account Payable (AP) | Not tracked | DB | | Base Payout Calculations | Google Sheets | DB | | GST & TDS Calculations | Google Sheets | DB | | Payout & GST Invoice | Google Sheets | DB | | GST Tax & TDS Filing | Google Sheets | DB | | Bank Account Data | Manual Check | DB | | Payout File to Bank | Excel | API | | Payout Payment Status | Statement | API | | Reconciliation & UTR Backfill | Google Sheets | DB | --- ## **3. User Needs** ### **MFD / Partner** - Expect accurate, on-time payments. - Need clear payout breakdowns, including GST invoices. - Require an easy way to highlight and resolve discrepancies. - Want Volt to handle tax filings accurately. - Prefer a payout experience similar to top AMCs. ### **Business Team** - Aims to improve MFD service by resolving payout issues efficiently.

---

## #17 — Migrating MFD Partners to the LSQ Accounts
**Status:** Ready for Tech | **Last edited:** May 27, 2025 2:25 PM

# Migrating MFD Partners to the LSQ Accounts [**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md) - Accounts are now enabled for org: volt - Reading LSQ documentation to understand and create a transition plan - MFD is currently treated as lead and should be moved to accounts - RMs will be assigned accounts and will be responsible for its success - All the customer of a MFD will be under their account - **1. Purpose & Goal:** - **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data. - **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads. - **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership). **3. Procedure:** **Phase 1: Configure the Accounts Module for MFDs** Setting up the Accounts entity for MFDs - **3.1 Identify Required MFD Fields:** - Review the current Lead fields list - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples: - PAN - ARN No - Referral Code / Partner Code - Partner Referral Link - Partner Type - Platform / Platform Id - Empanelment Date - Company (if used for MFD firm name) - Key contact details (Email, Mobile Number, Address, City, State, Zip Code) - Ownership (Owner) - Any other relevant custom fields. - **3.2 Create Custom Account Fields:** - Adding all the Lead files to account - For every required MFD field *not* present by default in Accounts, create a custom field: - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions - Click **Add**. - Define: - **Display Name:** - **Schema Name:** format cf_display_name. custom field for easy reference - **Field Type:** Match - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/) - 3.3 Add Drop-downs in fields like stage, etc. **Phase 2: Migrate MFD Data from Leads to Accounts** - **3.4 Extract MFD Leads:** - Manage leads - Use **Advanced Search** Lead Type != MFD - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**. - **Export:** Select Actions -> Export Leads -> Export as CSV. - **3.5 Prepare the Import File

---

## #18 — MFC Summary API integration
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

## #19 — PRD MFD Performance Metrics & Earnings Display
**Status:** Not started | **Last edited:** May 21, 2025 12:46 PM

# PRD: MFD Performance Metrics & Earnings Display ## **1. Introduction** This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show: - Their sourced **MF Loan AUM** - Applicable **trail income rate** - **Trail income earned** - **Account opening bonuses** The goal is to make it simple for MFDs to understand how their efforts are driving their earnings. --- ## **2. Goals & Objectives** ### **Primary Goal** To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives. ### **MFD User Objectives** - Understand how MF Loan AUM translates into income or Increase visibility to the MFDs - Track progress toward higher income tiers - See a breakdown of earnings and new account bonuses - View historical trends and performance ### **Business Objectives** - Encourage MFDs to grow MF Loan AUM - Boost Volt Money customer acquisition - Reduce support queries about commissions ## **Success Metrics** - MFD Monthly visits to partner portal - MFD Repeat rate - MFD Avg number of applicaitons per month - upward move in MFD LAMF AUM Buckets --- ## **3. User Stories** - *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier. - I want to know my current trail income rate based on slabs. - I want to see how close I am to the next earning tier. - I want to track monthly/quarterly/yearly trail income. - I want to verify bonuses for each new LAMF line opened. - I want a full summary of earnings: trail income + bonuses. - I want to view historical performance trends. - I want to quickly reference the trail income slab table. --- ## **4. Feature Breakdown & UI/UX** ### **4.1 Main Dashboard: Volt Money Performance Overview** **Key Metrics:** | Metric | Example | Tooltip | | --- | --- | --- | | **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money | | **Trail Rate** | 0.55% | Based on current AUM slab | | **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. | | **New Accounts (MTD)** | 5 | From Onboarding CRM | | **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts | | **Total Earnings (MTD)** | ₹58,291 |

---

## #20 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #21 — MFD Payout Process Revamp
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

## #22 — Selfie Link - MFD Prudent PRD
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

## #23 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #24 — MFD Activation Flow in LSQ
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

## #25 — MFC Pledge (revocation & invocation)
**Status:** Pending Review | **Last edited:** July 4, 2025 7:04 PM

**Problem:**
are we solving?**

---

- **Multiple OTP Friction**: Users currently need to enter two separate OTPs when pledging mutual fund units - one for CAMS RTA and another for KFIN RTA if their portfolio spans across both RTAs. The dual OTP process creates friction in the loan origination journey, potentially leading to higher drop-off rates during pledge process
- **Complex Integration Overhead**: LSPs must maintain separate API integrations with both CAMS and KFIN RTAs, leading to:
    - Duplicate development effort
    - Multiple credential management
    - Inconsistent error handling across RTAs
 

**Solution:**
?**

---

## #26 — [Platform +Volt ] MFC Pledge wrapper APIs + Volt J
**Status:** In progress | **Last edited:** July 30, 2025 3:55 PM

**Problem:**
are we solving?**

Currently LSPs pledge funds through RTA wrapper APIs. This means that for end customer to pledge mutual funds, customer requires to provide 2 separate OTPs one for each RTA. 

This can be solved by providing LSPs an option to pledge mutual funds via MFC with single OTP.

Pledging through two RTA also has a cost implication, pledging via MFC will reduce the pledging cost to half of the current cost. 

---

**Solution:**
?**

---

## #27 — MFD Account View in LSQ
**Status:** In progress | **Last edited:** July 3, 2025 12:49 AM

**Problem:**
are we solving?**

Volt Money’s CRM (LeadSquared) is currently optimized for B2C workflows. However, the B2B2C sales channel relies on MFDs (Mutual Fund Distributors) to bring in retail loan customers. Since RMs (Relationship Managers) interact only with MFDs and not directly with end customers, the lead-level view is insufficient.

Key gaps include:

- No account (MFD)-level visibility
- Lack of pipeline tracking across referred leads
- No structure to capture relationship intelligence
- Inability to assess MFD performance, intent, or conversion potential
- Performance of Agents are affected 

**Solution:**
?**

Create a dual-layer CRM structure in LeadSquared (LSQ) that allows RM teams to operate with both:

- **Account-level visibility** (for MFDs)
- **Lead-level granularity** (for referred end-customers)

---

## #28 — [Volt LSP] MFC pledge
**Status:** Not started | **Last edited:** July 21, 2025 3:33 PM

**Problem:**
are we solving?**

Current pledging requires customers to submit upto two OTPs, one for CAMS and another from KFin. This add to the friction in our loan application journey. 
MFC pledging APIs solve this by requiring 

---

**Solution:**
?**

---

## #29 — MFD partner dashbaord Onboarding Rewamp
**Status:** Not started | **Last edited:** January 8, 2025 1:39 PM

# MFD partner dashbaord Onboarding Rewamp ## Current problems -

---

## #30 — MFC in-app journey
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

## #31 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #32 — Transactions for MFD API
**Status:** In progress | **Last edited:** January 16, 2025 7:45 PM

# Transactions for MFD API # PRD: Partner-Level Transaction API ## Overview New API endpoint to provide aggregated transaction data at partner level for all customers under a specific partner to address transaction duplication issues. ## Business Context - Need to provide accurate transactions to partner MFDs - Currently experiencing transaction duplication issues - Need consolidated partner-level view instead of customer-level only - Support platforms with multiple partners and customers We recreate our transaction Db with different txn ID every day. Redvision does not have a sophisticated dedupe check , causing transactions to get duplicated multiple time ~avg 2.7 time , highest 28+ count. https://voltmoney.atlassian.net/browse/VSSB-398 This is a major escalations from the redvision, as the daily transaction sync with the with redvision will be unfeasible they requested partner level API to full from our DB. ## API Specification ### Endpoint `GET /v1/partner/platform/transactions` ### Headers | Header | Description | Required | Example | | --- | --- | --- | --- | | X-AppPlatform | Platform identifier | Yes | FUNDS_INDIA | | requestReferenceId | Unique request ID | Yes | b2595c8c-a163-4072 | | Content-Type | Content type | Yes | application/json | ### Request Parameters | Field | Type | Required | Description | Example | | --- | --- | --- | --- | --- | | fromDate | String | Yes | Start date | "2024-01-01" | | toDate | String | Yes | End date | "2024-01-31" | | volt_Partner_id | String | Yes | Partner identifier | "PARTNER123" | | format | String | No | Response format | "JSON" | ### Response Structure | Field | Type | Required | Description | | --- | --- | --- | --- | | status | String | Yes | Response status (SUCCESS/ERROR) | | partnerDetails.partnerId | String | Yes | Unique partner identifier | | partnerDetails.partnerName | String | Yes | Partner name | | partnerDetails.totalCustomers | Number | Yes | Total customers count | | transactions[].transactionId | String | Yes | Unique transaction ID | | transactions[].voltcustomerCode | String | Yes | Customer identifier | | transactions[].description | String | Yes | Transaction description | | transactions[].amount | Number | Yes | Transaction amount | | transactions[].transactionStatus | String | Yes | SETTLED/PENDING_SETTLEMENT | | transactions[].transactionType | String | Yes | CREDIT/DEBIT | | transactions[].settledOn | Number | Yes | Settlement timestamp | |

---

## #33 — MFD Partner Portal Access
**Status:** Not started | **Last edited:** February 21, 2025 1:31 PM

# MFD Partner Portal Access Problem statements 1. Some MFDs forget which number they have used to create the account. 2. The MFD employees struggle to find the Portal, the number to log in, and OTP from their MFD 3. MFDs don’t set up passwords as the process to set up a password is deep in the portal. Solutions 1. We can send the Link with Phone number / Account ID and password over email to MFD 2. Generally, MFD employees too have access to the E-mail, they can search Volt money Email

---

## #34 — MFC fetch in Volt Journey
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

## #35 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #36 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #37 — Post loan Status APIs for MFD SaaS Partner Platfor
**Status:** Done | **Last edited:** February 14, 2025 12:59 PM

# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal # Product Requirements Document (PRD) [API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md) ## **Project Title:** **Development of External APIs for MFD Dashboard Integration** --- ## **1. Introduction** This document outlines the requirements for developing a set of External APIs intended for MFD platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners --- ## **2. Objective** To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base. --- ## **3. Target Audience** - **Primary Users:** - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards. - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data. - **Stakeholders:** - **Product Management Team** - **Development Team** - QA - **MFD SAAS Partners** --- ## **4. Scope** ### **In-Scope:** - Development of four External APIs: 1. **Get Active Customers** 2. **Get Shortfall Details** 3. **Get Interest Due Details** 4. **Get Renewal Details** - Documentation and specifications for each API. - Implementation of business logic within each API. - Security measures for data protection. ### **Out-of-Scope:** - Development of UI components for MFD dashboards. - Integration of common headers and authentication mechanisms (handled separately). --- ## **5. API Specifications** ### **5.1. Get Active Customers** ### **Endpoint:** ``` GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber} ``` ### **Description:** Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively. ### **Parameters:** - **Path Parameters:** - `partnerAccountId` (string, **required**): Unique identifier for the partner account. - **Query Parameters:** - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve. ### **Response Payload:** ```json { "activeCustomerDetails": [ { "mobileNumber": "+919876501234", "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "email": "dummy@voltmoney.in", "pan": "AUWPA7175L", "dob": "30-03-1988", "creditDetails": { "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "creditType": "OVERDRAFT", "lenderCreditId": "9911725722", "lenderName": "Bajaj", "totalCreditAmount": 332300, "availableCreditAmount": 282300, "principalOutStandingAmount": 50000, "currentApplicableInterestRate": 9.95, "pledgedPortfolioAmount": 738723, "overUtilizationAmount": 0, "chargesDueAmount":

---

## #38 — MFC Pledge error handling - V1
**Status:** Not started | **Last edited:** December 8, 2025 10:53 AM

**Problem:**
are we solving?**

- Currently, as we have made MFC Pledge live for B2B2C and B2C channels and plan to dial up for other channels as primary mode for pledging, we need to address and handle the top errors that have occurred until now.
- Currently, these errors are not handled: users see generic failure messages and raise tickets with customer support.
- This creates friction in the journey, increases TAT for resolution, and causes user drop-offs.

**Goal:** Show clear, actionable error messages for the most frequent pledge errors in frontend so users can self-resolve or know what to do next, r

**Solution:**
?**

---

## #39 — [Volt LSP] Pre fill bank account number from MFC d
**Status:** In progress | **Last edited:** December 27, 2024 10:40 AM

**Problem:**
are we solving?**

Customers on the bank verification step are currently required to enter their complete Bank account number and IFSC code to verify their bank account this is a pain for customers. 

[https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99](https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99)

---

**Solution:**
?**

---

## #40 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #41 — MFD Communications for MFDs and Customers
**Status:** Not started | **Last edited:** December 24, 2024 2:11 PM

**Problem:**
are we solving?**

- unclear and mistimed comms leads to lot of escalations.
- we are sending comms with wrong informations
- Some of the comms are not compliant
- 

---

**Solution:**
?**

---

## #42 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #43 — MFD Servicing
**Status:** Not started | **Last edited:** December 17, 2024 1:46 PM

# MFD Servicing # MFD servicing We need to provide assistance to the MFDs in completing the application process on behalf of there customers and provide servicing. These issues need to be identified and to be solved for reduced effort on the MFD and Volt side. We want to provide quick resolution to any issues our MFD might be facing , Goal of the document is to describe the process and current challenges faced by us Ideal process 1. MFD communicates the issues with us using WhatsApp. 2. RM understands the issues from the Communications and raise a ticket 3. Agent then communicates the resolution and mark the tickets as resolved 4. We track the WhatsApp chat and Ticket analytics to understand and improve our servicing ## Current issues ### Communications - **Issue communication:** We use WhatsApp based tools for the MFD to communicate with us (preferred mode of communication by the MFDs). We have the two tools that we currently use - **Periskope: U**sed for providing Group chats to the MFD. - Periskope is based on Whatsapp app. It does not provide good tracking for the chats and expect us to create tickets to track issues - Pros - If MFD has a employees then they can be served by a whatsapp group better to have a one channel for updates *~ 300 groups currently with >1 MFD member.* - If MFD has a escalation then escalation can be handled on group ~ *this really has a bandwidth issues for Kapil or Bharat. We should have a separate channel for the grievance.* - If the RM is on leave and we have a group to solve then someone else can take the handover and solve the problem ~ *Currently only RM has the context on the issues of the MFD and rest of the people in group can’t takeover. The new RM has to gain context from the chat history or notes on the tickets.* - Convert WhatsApp messages into tickets or tasks - Connect with CRM systems, ticketing platforms, and other tools via APIs and web-hooks. - Cons - The platform is no longer supported by the Company - The API integration need to developed by Volt - We are not provided with most Chat level tracking like First time response, Time spend on a chat, How long the message hasn’t been responded to. - Tickets has to

---

## #44 — MFC Journey - Fetch
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #45 — MFC implementations
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #46 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #47 — MFD - Removing google SSO from PLJ
**Status:** Ready for Tech | **Last edited:** April 22, 2025 10:53 AM

# MFD - Removing google SSO from PLJ Problem statement 1. The **Email field is not Pre-filled** even when the MFD has already fetched the MFC for the client. 2. **Email verification via Google SSO** doesn’t work well for the MFD channel—Google pulls the MFD's email from the device instead of the client’s. ![Screenshot 2025-04-11 at 1.31.35 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.35_PM.png) - MFDs often manually enter their email in the **“Continue with other email”** option, leading to operational effort to remove the Email. ![Screenshot 2025-04-11 at 1.31.44 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.44_PM.png) ## **Proposed Solution:** **After customer registration (Name + Mobile Number + OTP):** 1. The MFD lands on the **Customer Registered** screen. 2. The screen gives two options: - Learn how to **create an application** on the Partner Portal, or - **Share a link** with the customer. 3. If the MFD chooses **“Continue creating customer application”**: - The flow will continue to the next application journey step skipping the App homepage as the intended action at this step is to complete the application. - The Data like Email ID and Fetched portfolio will be Pre-filled if the MFC has been previously fetched for the customer - If the MFD needs to access the App home page then they can go back on the application process using the top ← arrow on the top left. Text changes on the verify Email step ” The provided email will be used by lenders as the Client’s registered Email for all communications “ ### Key Changes from the Current Flow 1. **Skip the email selector page** — go directly to the “Add Email” screen. 2. **Show the client’s name** clearly to ensure the email being entered is for the right person. 3. **Include a note** saying the email will be used by lenders for important updates. 4. **Update the header** to: “Add client’s email.” 5. **Streamline the journey** by removing extra steps and taking MFDs directly to the email input screen.

---

## #48 — PRD MFC Revised Flow
**Status:** Not started | **Last edited:** April 14, 2026 1:03 PM

**In scope:**
- 
    - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including::
        - Partners who have directly integrated with MFC  fetch flow (eg-Paytm)
        - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter)
        - Partners who are using Volt fetch journey

# PRD: MFC Revised Flow ## **Background and Context** - - Since MFC is going to deprecate the MFC fetch apis and moving to SDK based flow for fetching (concerns from AMFI around fintech platforms accessing investor data freely w/o explicit customer consent.) - This change is expected to go live by 31st January - Since all Volt channel flows (B2B,B2C & B2B2C) as well as LSP flows will be impacted by this change, figuring out how to tackle this transition to esnure business continuity in the near and long terms is critical --- ## **1. Problem scope** ### In scope - - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including:: - Partners who have directly integrated with MFC fetch flow (eg-Paytm) - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter) - Partners who are using Volt fetch journey ### Out of scope - N~~ot covered as part of current scope:~~ - ~~Loan journey changes ‘post fetch’ for Volt channels~~ - ~~B2C website journey changes wrt MFC SD~~K - While the MFC SDK flow implementation is currently suboptimal from tech/ UX POV, improving it by working with the MFC team is not feasible given our tight deadline. --- ## **2. Success Criteria** - - Overall fund fetch SR & first time SR - Overall Fetch TAT - MFC SDK flow SR & TAT - MFC SDK & RTA flow stability /uptime ## **3. Solution Scope** ### [Detailed solution /Journey](https://whimsical.com/internal-mfc-fetch-updated-flow-copy-FDDhzqEJNzTbNnkUCW73b5) ### 1. Entry point (Volt/LSP channels) Volt B2C - Android/IOS app/Partner app: DSP SDK will be triggered on on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen ![Screenshot 2026-02-08 at 2.51.52 PM.png](PRD%20MFC%20Revised%20Flow/Screenshot_2026-02-08_at_2.51.52_PM.png) - ‘Sign in’ entry point on Website : DSP SDK will be triggered on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen in the web app - Check eligibility’ entry point on VoltWebsite: DSP SDK will be triggered on submitting ‘PAN & mob no’ screen & will open in an iframe Volt B2B2C/B2B partners - Partners fetching in own UI:The ‘DSP SDK’ flow is triggered from the partner UI - Partners using Volt UI for fetching: Flows will be same as that mentioned under ‘B2C’ section LSP - The ‘DSP SDK’ flow is triggered from the partner UI ### 2.User

---

## #49 — Analytics setup for MFD channel
**Status:** In progress | **Last edited:** April 10, 2025 11:11 AM

# Analytics setup for MFD channel **Problem Statements:** 1. **Source Identification:** - We currently lack detailed data to distinguish the source platform/interface for applications. Examples include: - Partner Portal Web vs. Partner App - Customer App vs. specific SDKs 2. **SDK Tracking:** - We cannot accurately identify which SDK version or type was used by a partner platform for an application. 3. **TAT Calculation:** - Relying on the audit table for TAT is not ideal for analyzing detailed stage performance. --- ### **Proposed Solutions:** 1. **Source Markers:** - Add unique markers/attributes to application records to identify the origin: - Volt Partner Portal (Desktop) - Volt Partner Portal (Mobile Web) - Volt Customer Web - Volt Customer Mobile App (iOS/Android) - Volt Partner Mobile App (iOS/Android) - SDK (Identify SDK Type/Partner) - Device Type (where applicable) - Application step level - Source (e.g., in the MFD channel where both Partner and Customer may complete steps) 2. **Dedicated TAT Metrics:** - Implement fields/timestamps to capture: - Add Created add of the step , to capture the the First time stage change - **Overall TAT:** From Lead Creation/Customer Registration to Loan Complete status. - **Stage-Level TAT:** Track start times for each key state to calculate the duration spent in each stage (e.g., Start of State A → Start of State B). 3. **Logging for FE UI related bugs:** - Tracking sluggishness on the website - If the Elements fail to load or are stuck

---

## #50 — MFD comms
**Status:** Unknown | **Last edited:** Unknown

# MFD comms Drive link [https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph](https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph) 1. **6 Day MFD activation plan** – Last modified on Oct 10, 2023, by Ranjan Kumar Singh. 2. **Comms content - MFD drop off during reg...** – Last modified on Aug 29, 2023, by Kapil Nagal. 3. **Comms content - MFD Referral** – Last modified on Jul 24, 2023, by Kapil Nagal. 4. **Comms content - Welcome email to MFD** – Last modified on Mar 18, 2023, by Kapil Nagal. 5. **Mastersheet Volt Money - MFD Comms** – Last modified on Jul 24, 2023, by Kapil Nagal. 6. **partner comms status** – Last modified on May 3, 2023, by Ranjan Kumar Singh. 7. **partnerComm[Signup]** – Last modified on May 1, 2023, by Ranjan Kumar Singh. 8. **Referral activation message** – Last modified on Aug 29, 2023, by Ranjan Kumar Singh. [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) Consumer comms :- [https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing)

---

## #51 — MFD UI screen exploration
**Status:** Deprioritised | **Last edited:** Unknown

# MFD UI screen exploration Charter: MFD Pod # Context Post fetch, offer screen. HMW optimise for faster TAT. Not club and make is a non linear journey. https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6090-1797&t=MmlJYS7TFHPgzhgQ-11 https://whimsical.com/mfd-board-SQzR6Ph8GAR7cMj6RtBVfL # Process - [ ] Benchmarking - [ ] Explorations # Figma

---

## #52 — MFD Processes
**Status:** Unknown | **Last edited:** Unknown

# MFD Processes # Activation Process To connect with Ashik, # Application Process MFD portal flow - RMs to explain. LSQ + sales flow like Exotel. # Servicing Process Whatsapp groups process like Periskope - Sowmya, # Payout Process

---

## #53 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #54 — Inbound call assignment
**Status:** Unknown | **Last edited:** Unknown

# Inbound call assignment Future requests - Moving to a RM and Central team structure - Having a auto dialler for the central team - For inbound and Outbound Dialler Plan - One central team for the MFD channel - One number to be used for inbound and outbound December 11, 2024 @Tushar Luthra - The MFD are assigned to RMs and the RMs number is given to the MFD - If the RMs are busy then the Backup RM teams - There are B2C sales calling team with X number of people Tushar has tried auto dialer for the outbound for the Sales team to call the priorised leads and not have team cherry pick the applications #

---

## #55 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #56 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #57 — MFD Payout dashboard
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout dashboard We have a commercial relationship with MFD , where we pay them as per the business they bring Commercials | trail income | 0.5% of AUM | | --- | --- | | account opeing | 200rs | | Selfline | Processing fees waived | | Cashback | | | Content | | | referral | | - MFD payout is calculated based on commercials agreed on with them - MFD payout is different if the MFD is registed for GST - MFD with Gst number has to be paid 18% extra as GST - we collect 5 % TDS for any payout >15000rs - we payout on 10th on month to volt MFDs - we payout on 15th to SAAS partner platform MFDs - we payout on 18 th to MFD GST payout - we clear all pending and charges till 25th - MFD may not want to share the PAYOUT amount to there employees - MFD need to see the payout status - GST issues - Payout starts at 1 of the money - Time preiod is month to month - And 10 to 15 th of month payout disbursement happen - 10 MFD get paid - 15 Platform , - 18 MFD GST payout - 25 th anything pending - Puneet compute the payout MFD , 0.5% of AUM yearly trail income/ 12 200 rs per account opening , creditline open MFD selfline - we refund the family of MFDs , RMs fill a sheet Cashback for MFD’s end customers , - we gave 10.49 % customer we have given 0.5 % cashback as we advertised on 9.99% Contest , referrals price, activated MFD referral rs 1000 Platform , :- payout Affiliate - payout - MFD - - partner - - Platform - Affilaetes - Bharat sign off, Labdhi comms - Total amount August Pain points - GST filling , we have to 18% as a TDS of the total payout of the month. - we collect 5% TDS ,

---

## #58 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #59 — LSQ BRD For MFD Activations
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Currently, MFD leads entering through multiple channels lack a unified onboarding and activation process. This results in:

- Productivity Loss
    - Data inconsistencies
    - Delayed activation due to a low follow-up mechanism
    - Fragmented visibility across different channels of leads
- The Activation Process is currently ad hoc and dependent on Google Sheets for tracking
- Enhance the follow-up mechanism

---

---

## #60 — Current Volt setup
**Status:** Unknown | **Last edited:** Unknown

# Current Volt setup We have around ~ 2500 MFDs Number of activated MFDs? Number of tickets chats on the Periskope /per day We have these tools - Periskope for group chat - Wati for Chat support - Exotel for call support - Zendesk for the internal ticketing - Retools for the Customer details -

---

## #61 — Periskope handling
**Status:** Unknown | **Last edited:** Unknown

# Periskope handling Problem ? - we have too many tools in servicing - As we have Wati and periskope for whatsapp we want to move to one platform - we are having difficulty in managing and reviewing the service SLA. we are missing out on the parter comms and not responding in many hours , this leads to lower MFD retention Goal ? - Increase MFD engagement and retention. - Do we have to add new number to Wati, or one number would suffice ? - If One number then how the handling between agents? - if Two then how will we handle the Display on the MFD , MFD based Number on dashboard ? Current Wati number for mFD? Current agent assigned to Wati? List of 500 MFD to move ? can we add the number and chat to Wati? We will be moving from Periskope to Wati List of the MFD to move ➖ Identify the MFDs to move communicate the Change to MFD Surge planning for the WATI Periskope to Wati Transition plan - Identify the MFDs to move :- https://docs.google.com/spreadsheets/d/1ONAVTJh3wK8kxfcf9j_GvWPis71DKvNbr78d7c342Lk/edit?usp=sharing - Communicate the change to MFD - Message template Dear <name>, We are updating our support communication channel to enhance our service quality. Please note the following: Effective immediately, all support interactions will be conducted through our new channel. Please use the WhatsApp number mentioned below for any Support request. CTA—> Link to Wati Number for message - Surge planning Day 0 - Create a bulk message template - Train and prepare agents Day 1 - We move the Single and inactive MFDs. By sending the message. We will not reply to Periskope after the message (Exception - If Wati is not working ) - Wati will be Serviced by → <Agent name>. Making sure that we have a dedicated resource and they have tools needed to help MFDs - Observe the Volume , allocate the Bandwidth from Periskope to Wati → <name of the agent > - We should expect some Comms from inactive MFDs due to confusion /curiosity. - Day 2 - Review the channel from yesterday - We move rest of the Single MFDs , Barring the top ~100 - We move Inactive 2 MFDs today as well - Same process of handling the Chat support - Day 3 - We move all the MFDs apart from the Top MFDs identified Analytics

---

## #62 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #63 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #64 — Notes Bharat
**Status:** Unknown | **Last edited:** Unknown

# Notes <>Bharat Negotiations table - we will close self-line until we can ensure 1 self-line per partner account. - Rate change, and PF - In tata we can’t change the Rate , so cashback is the option for the Tata. TDS Accounts payable Payment ops Commercials data on the entity - there are three entities applications partner platform that dictate commcials there is a base rate as per the lender that will be assigned by the BRE now once the ROI and PF are assigned to the user then the commencial terms should be added to the application as well on a applciations level we have We have different commercial terms with the on three entity levels application Partner Platfrom the commercials are the the param used to calculate the payout made for the user the Base rate is assigned as per the lender pricing grid of the time of application creation There is default commercials rate that get assigned to Partners and platform by default there are admin actions which assign for a application differenct ROI and PF and the split between the Volt and partner s we are currently not storing the commercials data on the entities level instead its a excel sheet , which casuses issues when calciualting the Solution possible to add object to the right entity that stores he commercials data Application level - ROI - PF - ROI split - PF slip - Base ROI - Base PF Partner level - offer applicable ? - Offer code - ROI - PF - ROI split - PF slip the ROI , PF and splits can be added to the application or to the partner, if added to the partner all the application created by the partner will be assigned the new commercials. Offer code is applied if the applicable. offer can be set of rules like >5 application in the month x = 5000 rs in the payouts Offer has a applicable to and from date the platfrom Platfroms have the similar - ROI - PF - SLITs - Slab based rules the data flow will be 1. application is created 2. assign base ROI and PF from the Lender pricing Grid 3. assign the Application level negotiated Rates collected from Admin actions 4. Assign the MFD commercials as default , then change if changed by the admin action 5. the Platform commercials will

---

## #65 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #66 — Cost estimates
**Status:** Unknown | **Last edited:** Unknown

# Cost estimates # AWS Infrastructure Cost Projections (2024-2026) ## Constants & Assumptions | Parameter | Value | Notes | | --- | --- | --- | | Growth Rate | 2x yearly | Partner base doubles each year | | Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) | | Retention Period | 84 months | 7 years for regulatory compliance | | Emails per Partner | 3/month | Registration, payout, GST notifications | | API Calls per Partner | 20/month | Includes all interactions | | Lambda Executions per Partner | 10/month | All automated processes | ## Growth & Cost Projections | Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | | --- | --- | --- | --- | | Active Partners | 2,500 | 5,000 | 10,000 | | Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB | | Cumulative Storage | 93 GB | 279 GB | 558 GB | | Monthly Emails | 7,500 | 15,000 | 30,000 | | Monthly API Calls | 50,000 | 100,000 | 200,000 | ## Monthly Cost Breakdown (USD) | Service | Year 1 | Year 2 | Year 3 | Scaling Factor | | --- | --- | --- | --- | --- | | S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation | | RDS | $45 | $65 | $110 | Step Function* | | Lambda | $3 | $6 | $12 | Linear | | SES (Email) | $0.75 | $1.50 | $3 | Linear | | API Gateway | $5 | $10 | $20 | Linear | | CloudWatch | $15 | $25 | $45 | Step Function* | | Route 53 | $0.50 | $0.50 | $0.50 | Fixed | | Step Functions | $2 | $4 | $8 | Linear | | **Total Monthly** | **$73.39** | **$118.42** | **$211.33** | | | **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** | |

---

## #67 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #68 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #69 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #70 — Payout Working File
**Status:** Unknown | **Last edited:** Unknown

# Payout Working File Errors earliar - We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured - We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally - We receive GST issues as Customer raise wrong invoices, This is because we don’t provide GST tax invoice to the partners - We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering uploads the data once a month - We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data. - We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date - We need to streamline GST and TDS filing - We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~ list , journey , use case ## Meeting notes - customer - cashback- - previously - partner - platform customer cashback Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49 march 2022. —>23—>24 <may 1st 9.99 9.99 -ROI base rate - 10.49%. 0.5 % cashback on may 1 we changed the base rate for the customer to 10.49% cusotmer cashback , partner to partner Selfline partner payout - MFD - Volt empaneeled MFD - MFD direct - through Software, redvisison or invest well, assest plus , zfunds , - MFD software - affiliates, - Ytbers , - Partner payout - apps like phonepe , jupiter, niyo, part+ - Money is calculated on the Principal outstanding , monthly average daily average, payout is calculated customer wise average POS, eod, for debit-credit sharing percentage with partners - 1. customer —> loan —> 1. credit to borrower 2. Credit to partner 3. Credit to platform 2. partner - volt- 3. upfront - one time payment, rs 200 for opening a account 4. trail income - 0.5 % into POS 5. category —> upfront and

---

## #71 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #72 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #73 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #74 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #75 — Query for MFD tiering
**Status:** Unknown | **Last edited:** Unknown

# Query for MFD tiering: WITH partnet_cte AS ( SELECT vdl_audit_partneraccounts.accountid AS partner_account_id, max(NULLIF(partnername,'nan')) as partner_name, MAX(NULLIF(accountholderphonenumber,'nan')) AS partner_phone_number, MAX( COALESCE(NULLIF(accountholderphonenumber, 'nan'),NULLIF(pa_sub.pa_alt_phonenumber, 'nan'))) AS partner_phone_number, max(case when address = 'nan' then null else json_extract_scalar(REPLACE(address, '''', '"'), '$.city') end) as partner_city, MAX(partnercode) AS partnercode, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') END) AS partner_arn, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') END) AS companyName, MAX(NULLIF(accountholderemail,'nan')) AS partner_email, MIN(CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END) + INTERVAL '330' MINUTE AS registered_date, MIN( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END )+ INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" left join (select accountid,coalesce(accountholderphonenumber,json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) as pa_alt_phonenumber from "volt-data-lake"."vdl_partneraccounts") pa_sub on pa_sub.accountid = vdl_audit_partneraccounts.accountid GROUP BY vdl_audit_partneraccounts.accountid UNION - - PART 2: From Partner Table not present in Audit SELECT partner.accountid AS partner_account_id, NULLIF(partnername, 'nan') AS partner_name, COALESCE(NULLIF(accountholderphonenumber, 'nan'), json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) AS partner_phone_number, json_extract_scalar(REPLACE(address, '''', '"'), '$.city') as partner_city, partnercode, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') AS partner_arn, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') AS companyName, NULLIF(accountholderemail, 'nan') AS partner_email, ( CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END ) + INTERVAL '330' MINUTE AS registered_date, ( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END ) + INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-data-lake"."vdl_partneraccounts" partner LEFT JOIN ( SELECT DISTINCT accountid FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" ) audit_check ON partner.accountid = audit_check.accountid WHERE audit_check.accountid IS NULL ), customer_cte AS ( select partner_account_id,date(first_created_on) as partner_active_date_application_first_created_on,partner_partially_active_date,partner_active_date,dhanda_activity_date from ( SELECT partner_account_id, first_created_on, MIN(date(first_created_on)) OVER (PARTITION BY partner_account_id) AS partner_partially_active_date, MIN(date(completed_on)) OVER (PARTITION BY partner_account_id) AS partner_active_date, MAX(date(completed_on)) OVER (PARTITION BY partner_account_id) AS dhanda_activity_date, ROW_NUMBER() OVER (PARTITION BY partner_account_id ORDER BY completed_on ASC) AS rn FROM "volt-analytics"."primary_application_full_info" -- WHERE partner_account_id = '072f9922-abe0-4c79-9883-1b26044767b8' ) sub where rn=1 ), partner_customer_detail_cte as ( select count(distinct application_id) as total_no_of_completed_applications,sum(app_pledged_credit_limit) as toal_pledged_credit_limit,partner_account_id,max(business_channel) as business_channel ,max(operating_channel) as operating_channel,max(platform_name) as platform_name from "volt-analytics"."primary_application_full_info" where current_step_id='COMPLETED' group by partner_account_id ), final_cte as ( select p.*, c.partner_active_date_application_first_created_on, c.partner_partially_active_date, c.partner_active_date, c.dhanda_activity_date, pc.total_no_of_completed_applications, pc.toal_pledged_credit_limit, pc.business_channel, pc.operating_channel, pc.platform_name from partnet_cte p left join customer_cte c on p.partner_account_id=c.partner_account_id left join partner_customer_detail_cte pc on p.partner_account_id=pc.partner_account_id ), volt_cte as ( select *,CASE WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10 THEN 'Super Gold' WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <=

---

## #76 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #77 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #78 — MFD Login data
**Status:** Unknown | **Last edited:** Unknown

# MFD Login data "total_partner_users": 77588, "never_logged_in": 12310, "first_login_mobile": 4978, "first_login_web": 31789, "first_login_other": 28511, "total_mobile_users": 24608, "total_web_users": 37813, "used_both_platforms": 21165, "used_only_other_platforms": 24028, "never_logged_in_percent": 15.87, "mobile_adoption_percent": 31.72, "web_adoption_percent": 48.74, "both_platforms_percent": 27.28 query ```jsx WITH first_logins AS ( SELECT user_id, MIN(created_date_time) as first_login_date, -- Get the platform of their first login platform as first_platform FROM user_login_audits WHERE created_date_time = ( SELECT MIN(created_date_time) FROM user_login_audits ua2 WHERE ua2.user_id = user_login_audits.user_id ) GROUP BY user_id, platform ), platform_usage AS ( SELECT DISTINCT rutpm.user_id, fl.first_login_date, fl.first_platform, CASE WHEN EXISTS (SELECT 1 FROM user_login_audits ua WHERE ua.user_id = rutpm.user_id AND ua.platform = 'VOLT_MOBILE_APP') THEN 1 ELSE 0 END as has_used_mobile, CASE WHEN EXISTS (SELECT 1 FROM user_login_audits ua WHERE ua.user_id = rutpm.user_id AND ua.platform = 'VOLT_WEB_APP') THEN 1 ELSE 0 END as has_used_web FROM relationship_user_to_partner_main rutpm LEFT JOIN first_logins fl ON rutpm.user_id = fl.user_id ) SELECT -- Total Users with Partners COUNT(*) as total_partner_users, -- Users who have never logged in COUNT(CASE WHEN first_login_date IS NULL THEN 1 END) as never_logged_in, -- First Platform Distribution COUNT(CASE WHEN first_platform = 'VOLT_MOBILE_APP' THEN 1 END) as first_login_mobile, COUNT(CASE WHEN first_platform = 'VOLT_WEB_APP' THEN 1 END) as first_login_web, COUNT(CASE WHEN first_platform NOT IN ('VOLT_MOBILE_APP', 'VOLT_WEB_APP') AND first_platform IS NOT NULL THEN 1 END) as first_login_other, -- Platform Usage Distribution COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END) as total_mobile_users, COUNT(CASE WHEN has_used_web = 1 THEN 1 END) as total_web_users, COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END) as used_both_platforms, COUNT(CASE WHEN has_used_mobile = 0 AND has_used_web = 0 AND first_login_date IS NOT NULL THEN 1 END) as used_only_other_platforms, -- Calculate percentages ROUND(100.0 * COUNT(CASE WHEN first_login_date IS NULL THEN 1 END)::numeric / COUNT(*), 2) as never_logged_in_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END)::numeric / COUNT(*), 2) as mobile_adoption_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as web_adoption_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as both_platforms_percent FROM platform_usage; ``` --- **Subject:** Empanelment Funnel & Landing Page Data (/partner) Hi Shivansh, Here’s the data for the initial landing page views of **/partner** and the subsequent steps in the empanelment journey. **Limitations:** - This data is for the **first two weeks of April** only. - Note: `/signup` and `/signup/` both refer to the empanelment flow. --- **Page Views (Apr 1–14, from Google Analytics)** | Page URL | Unique

---

## #79 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #80 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #81 — Kapture CX
**Status:** Unknown | **Last edited:** Unknown

# Kapture CX - they are connect with incred , phone pe (to be ) ![Screenshot 2024-12-23 at 4.16.58 PM.png](Kapture%20CX/Screenshot_2024-12-23_at_4.16.58_PM.png) - connectors with exotell and other functions - they have customer 360 with all the data that we can send , history , details , txns, - auto QA, for the call summary and interaction quality scoring - 13 years of experience. - Auto translate - Ticket history and summary - solutioning team , —> commercials —> timelines —>

---

## #82 — ARN mandatory for new Registrations
**Status:** Unknown | **Last edited:** Unknown

# ARN mandatory for new Registrations ### **Problem Statement:** - Currently, the partner registration flow allows users to sign up with or without providing an ARN. This has led to a high volume of registrations from individuals who are not certified Mutual Fund Distributors (MFDs). - Approximately 70% of current partner registrations fall into this category. This influx of non-MFD sign-ups places a significant strain on the onboarding team, requiring manual filtering and follow-up, reducing overall efficiency. ### **Proposed Solution:** Modify the partner registration process to require a valid AMFI Registration Number (ARN) for successful sign-up. This will ensure that only verified MFDs can register as partners on the platform. ### **Implementation Requirements:** - **Target Page:** https://staging.voltmoney.in/partner/signup/ (and subsequently production) - Only applicable on New registrations , not existing MFDs - **UI Changes:** - Remove the option/checkbox/link currently allowing users to proceed without an ARN (e.g., "I don't have an ARN number"). - Modify the ARN input field to be mandatory. - **Field Validation:** - The ARN field must not be empty upon form submission. - ~~The entered ARN must consist of exactly **6 digits**.~~ - *(Note: For this initial implementation phase, no external validation against the AMFI database is required.)* - **Error Handling:** - If the user attempts to submit the form without entering an ARN, display a clear inline error message (e.g., "ARN is required."). - ~~If the user enters an ARN that is not exactly 6 digits, display a clear inline error message (e.g., "ARN must be exactly 6 digits.").~~ - **Informational Text:** - Add clear text near the ARN field to inform users about the requirement and guide non-MFDs. Use the following text: > Enter your AMFI Registration Number (ARN)* > > > *Only registered Mutual Fund Distributors (MFDs) can sign up as partners. If you are an investor looking to use Volt Money, please go to our [**Customer registration**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.voltmoney.in%2F%3Fstartnew%3Dtrue).* > **Expected Outcomes & Benefits:** - **Reduced Non-MFD Registrations:** Significantly decrease (estimated 70% reduction) the number of sign-ups from users without a valid ARN. - **Improved Onboarding Efficiency:** Allow the onboarding team to focus solely on qualified MFD partners, streamlining the verification and activation process. - The Existing MFD has no impact / change **Potential Risks & Considerations:** - **Lower Overall Registration Volume:** Expect an initial decrease in the *total* number of registration submissions. However, the number of *qualified* registrations should remain stable or increase relative

---

## #83 — API Integration Changes for MFD Migration to LSQ A
**Status:** Unknown | **Last edited:** Unknown

# API Integration Changes for MFD Migration to LSQ Accounts **Document: API Integration Changes for MFD Migration to LeadSquared Accounts** ## **1. Introduction & Goal** This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module. The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner. ## **2. Current API Usage Summary (Pre-Migration)** - **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD). - **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record. - **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*. - **Activity Logging:** - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*. - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*. ## **3. Required API Changes (Post-Migration)** The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked. **3.1 MFD Creation** - **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API. - **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate - **Changes Required:** - Replace API calls creating MFD Leads with calls to the Account creation endpoints. - **Payload Construction:** - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first. - CompanyProperties: Provide an array of Attribute/Value pairs. - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name] - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup). - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" } - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" } - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" } - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field,

---

## #84 — MFCentral CAS API Response Structure Analysis
**Status:** Unknown | **Last edited:** Unknown

# MFCentral CAS API Response Structure Analysis ## Top-Level Structure ```json { "reqId": "string", // Request identifier "pan": "string", // PAN number of the investor "pekrn": "string", // PEKRN (optional identifier) "mobile": "string", // Mobile number with country code "email": "string", // Email address (optional) "data": [ // Array of fund house holdings { "summary": [...], // Summary data for this fund house "schemes": [...] // Array of schemes under this fund house }, // Additional fund houses... ], "portfolio": [ // Overall portfolio summary { // Non-demat holdings summary }, { // Demat holdings summary } ], "investorDetails": { // Investor information // Address and contact details }, "statementHoldingFilter": "string" // Filter applied (e.g., "NON-ZERO") } ``` ## Fund House Data Structure Each element in the `data` array represents holdings from a single AMC: ```json { "summary": [ { "amc": "string", // AMC code "amcName": "string", // AMC full name "isDemat": "string", // "Y" or "N" for demat status "currentMktValue": "number", // Current market value "costValue": "number", // Total investment amount "gainLoss": "number", // Profit/loss amount "gainLossPercentage": "number" // Profit/loss percentage } ], "schemes": [ { // Detailed information for each scheme } // Additional schemes... ] } ``` ## Scheme-Level Structure Each scheme contains detailed investment information: ```json { "amc": "string", // AMC code "amcName": "string", // AMC full name "folio": "string", // Folio number "investorName": "string", // Investor name "age": number, // Investor age "mobile": "string", // Registered mobile "email": "string", // Registered email "taxStatus": "string", // Tax status code "modeOfHolding": "string", // Single, Joint, etc. "transactionSource": "string", // Source of transaction (BSE, etc.) "schemeCode": "string", // Unique scheme identifier "schemeName": "string", // Complete scheme name "idcwChangeAllowed": "string", // Income Distribution Change allowed flag "schemeOption": "string", // Growth, IDCW, etc. "assetType": "string", // EQUITY, DEBT, etc. "schemeType": "string", // Classification "nav": "number/string", // Current NAV "navDate": "string", // NAV as of date "closingBalance": "number/string", // Total units held "availableUnits": "number/string", // Redeemable units "availableAmount": "number/string", // Value of available units "currentMktValue": "number/string", // Total current value "costValue": "number/string", // Total investment amount "gainLoss": "number/string", // Profit/loss amount "gainLossPercentage": "number/string", // Profit/loss percentage "isDemat": "string", // "Y" or "N" "lienUnitsFlag": "string", // "Y" or "N" "decimalUnits": number, // Decimal places for units "decimalAmount": number, // Decimal places for amounts "decimalNav": number, // Decimal places for NAV "brokerCode": "string", // Distributor ARN code "brokerName": "string", // Distributor name "isin":

---

## #85 — MFD Payout Calculation Automation
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout Calculation Automation **Introduction** Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency. 1. we need to handle changing factors like - Monthly Transactions table - Marketing Offers /Referral bonuses - New Platforms additions - Changes in commercials with existing platforms /partners - Changes in base rates / Format - Negotiations with MFDs 2. We need to be able to audit how an amount was generated 3. we need to be able to accrue the credits to an account based on the activity 4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback Problem statements Before base payout calculations - Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing. - We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable. - Attribution of customer to correct Platfrom and partner require manual intervention. - We don’t store the PF and ROI paid by the customer in Credits table. - Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts After the Base payout calculation - TDS rules change and have to accommodate - GST payout are tracked manually Payout process - Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC - For Platform Payouts we need to provide a statement and how the Payout amount is calculated. - Partners have a hard time understanding statements. Potential solutions - Get TATA to improve the API data provided to get the updated transactions - Better fall-back handling on our side Activity activity triggers a

---

## #86 — MFD payouts payment reconciliation
**Status:** Unknown | **Last edited:** Unknown

# MFD payouts payment reconciliation Problem statements - It takes 3-4 days to reconcile payouts to MFDs - It takes 2 day to make bulk payments and get the status back from the HSFC. - We have to wait 2 days and try to make payment again to MFDs for whom the Payment have failed , this takes another 2 days to reconcile -

---

## #87 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs