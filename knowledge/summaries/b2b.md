# Current State: B2B

> Auto-generated from 482 PRD(s). Most recently edited shown first.


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

## #2 — SDK for b2b2c SAAS partners
**Status:** Not started | **Last edited:** September 30, 2024 6:06 PM

# SDK for b2b2c SAAS partners ### **Interest Details Management Table** | **Attribute** | **Description** | | --- | --- | | View Interest and Charges | Access current month due interest and charges details with respective statuses. | | Filtering | Filter by mandate status, interest status, and lender name (TATA, BAJAJ). | | Search | Search the interest details table. | | Interest Calculator | Provide tools for calculating interest. | | Pre-defined Messaging | WhatsApp messages based on interest and mandate statuses. | | Pagination | Support pagination with 50 records per page. | ### **Shortfall Management Table** | **Attribute** | **Description** | | | --- | --- | --- | | View Shortfall Amounts | Access details of shortfall amounts and aging information. | | | Sorting and Filtering | Sort by due date and filter by aging and lender name. | | | Search | Search within the shortfall details table. | | | Educational Content | Provide information on what a shortfall means. | | | Pre-defined Messaging | WhatsApp messages for communicating shortfalls to customers. | | | Pagination | Support pagination with 50 records per page. | | ### **Loan Renewals Management Table** | **Attribute** | **Description** | | --- | --- | | View Loan Renewal Details | Access loan renewal information, including statuses and due dates. | | Sorting and Filtering | Filter by lender name and status; sort by customers nearest to renewal dates. | | Search | Search within the loan renewal details. | | Educational Content | Provide information about the benefits and consequences of non-renewal. | | Pre-defined Messaging | WhatsApp messages based on loan status (Active, Expired with/without amounts). | | Pagination | Support pagination with 50 records per page. | ### **General Features Table** | **Feature** | **Description** | | --- | --- | | Tab and Page Deep Linking | Allow access to functionalities via deep links on all platforms (web, Android). | | Dynamic Tab Visibility | Display or hide tabs based on customer counts (hide when count is zero). | | Consistent Data Display | Ensure uniform data presentation across SDK and internal dashboard. | ### **Detailed Customer Information Table** | **Attribute** | **Description** | | --- | --- | | Customer Name | Name of the customer. | | Phone Number | Contact number of the customer. | | Due

---

## #3 — PRD - Mandate conversion optimisation via swap in
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

## #4 — Update MFC limit in application - from API and lan
**Status:** Not started | **Last edited:** September 3, 2024 4:07 PM

**Problem:**
are we solving?**

Currently for B2B partners where we allow MFC fetch and RTA pledge:  Once customers checks MFC limit on their platform and logins into the SDK, the limit is not refreshed upon refreshing the limit on partner platfomrs. 

---

**Solution:**
?**

---

## #5 — Deferring email capture and verification during on
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

## #6 — Manage Limit Error messaging handling
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

## #7 — Additional documents upload for Bajaj for AS ES DI
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

## #8 — Loan Offer Optimisation experiment for CheQ
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

## #9 — BAJAJ GetMilesAccountDetails
**Status:** On Hold | **Last edited:** September 2, 2024 11:37 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #10 — Bajaj PAN verification API
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

## #11 — PhonePe Landing page requirement - 15th April
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

## #12 — DSP - Integrated KFS & Agreement Flow
**Status:** Not started | **Last edited:** September 16, 2024 11:47 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #13 — BAJAJ Dedupe API
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

## #14 — BRE Proposal for cases above 1 Cr
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

## #15 — DSP Website
**Status:** In progress | **Last edited:** October 8, 2024 7:17 PM

**Problem:**
are we solving?**

As a regulated entity, DSP needs to have a website in its name with basic details. This is required from a regulatory  perspective to disclose key policies, procedures, etc.

In addition, certain borrowers also research the lender they have taken a loan from and would want to reach out for any concern or query.

---

**Solution:**
?**

---

## #16 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #17 — BAJAJ New KFS+Agreement flow
**Status:** Done | **Last edited:** October 8, 2024 1:04 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload

---

**Solution:**
?**

---

## #18 — User getting stuck at KYC verification step in cas
**Status:** On Hold | **Last edited:** October 7, 2024 5:01 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details, the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

- User completes the KYC screen :
    - We get “POV=null” in the getkycdetails response.
    - Then we will not keep the user stuck at this step, and allow them to move to the next “bank account” step.
    - Then we will enable the user to add supporting documents in the documents section
- When the issue is of mis-match, we will enable the 1st applicant to the add additional documents screen, where we will make the user attach the :
    - PAN signed document
- Once the user has uploaded the document, these documents will be sent in BAJAJ account creation mail, **(with remarks)**
    - **Remarks : “PAN for the customer was not fetched from Digilocker, hence attaching the self attested PAN of the user”**
    - Add Pratik, Sheetal & Parul in cc
        - Pratik :  [pratik.bagul@bajajfin

---

## #19 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #20 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #21 — Multi Drawdown Term Loan LMS Requirements
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

## #22 — Master collections PRD (NBFC)
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

## #23 — LSQ Audit QA
**Status:** Not started | **Last edited:** October 29, 2024 12:08 PM

# LSQ Audit QA MFD - connect with Ranjan DSP - talk to saksham

---

## #24 — DSP BRE for Beta
**Status:** Pending Review | **Last edited:** October 28, 2024 10:53 AM

**Problem:**
are we solving?**

Currently, customers can avail a loan from Volt app or web through DSP only through whitelisting or URL based parameters. This will not be possible to handle in the beta stage as we need to route applications real-time to DSP.

In addition, the segment where the credit limit offered by Volt is between 10K and 25K is ~12% of the total eligible applications which isn’t catered to by our other lenders, Bajaj and Tata. This opens up a new set of customers for us to acquire and eventual enhance from a limit perspective. 

---

**Solution:**
?**

---

## #25 — [IronGrid] Adding un-pledge validations in BE
**Status:** Not started | **Last edited:** October 25, 2024 1:20 PM

# [IronGrid] Adding un-pledge validations in BE ### Validations present in FE **FE Checks** - Manage limit - Remove pledge - Pledge more - Pledge history - At this page we have a starting check of buffer - User taps on Remove pledge and lands on the screen with list of funds - Buffer check applied again to calculate the number of units which can be selected by the user for un-pledging **Checks to be added** - Jay to share the tech solutioning doc of the customer - Folio level checks need to be added - Need to create validation in init API using this API : app/borrower/lms/credit/lender/manageLimitConfig

---

## #26 — TATA KFS and Agreement Phase 2
**Status:** In progress | **Last edited:** October 24, 2024 10:46 AM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge.

---

**Solution:**
?**

---

## #27 — Email Validation Approach PhonePe
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

## #28 — [Lending stack] Welcome mail
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

## #29 — DSP communication email template
**Status:** Done | **Last edited:** October 21, 2024 4:31 PM

**Problem:**
are we solving?**

NBFC will be sharing important communications to the user triggered by certain events that occur in the user’s loan account. The communication should follow a template (for ease of perusal and identification of content by the user)

List of comms:

https://docs.google.com/spreadsheets/d/1BrvoUyz4SbO_Odc4sTLvFumESJkDQwNS4ZahPu3n36o/edit?gid=0#gid=0

---

**Solution:**
?**

| Element | Consideration | Requirement description |
| --- | --- | --- |
| Header | Required | All email template should have a common header with the DSP finance logo. Date of communication and a description of the communication |
| Call-to-Action (CTA): | Required | Capabilities to place primary and secondary CTAs in the body of the text, the design should be able to support multiple CTAs for the user to click |
| Action-oriented text (e.g., "Apply Now", "View Statement") | Required | Design should support call to action statements, while there would be CTAs, specific text with weights would be required to draw user attention (outside of CTAs) |
| Contact information: | Required | Specific section which contains contact details of the NBFC (if the user wants to reach back the team)

---

## #30 — [Lending stack] DSP lender assignment logics
**Status:** Not started | **Last edited:** October 18, 2024 11:01 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #31 — Change in audit trail flow for PAN Validation API
**Status:** Pending Review | **Last edited:** October 17, 2024 8:05 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details (POV=null), the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

---

## #32 — SDKs
**Status:** Not started | **Last edited:** October 17, 2024 6:24 PM

# SDKs SDK requirement - business channels - Organic , volt app , web - IFA channel, MFD as a AUM protect , partner dashboard - B2b channel - they spend a lot on the CAC, - securing loans a low margin product - NIMs are 3 to 4 for unsecured loans - we are helping b2b partners cross-selling - we need 3 thing - Redirect - API level - SDK level - there must be a business usecase , integration effort vs reward - SDK - package of all the APIs, partner needs to call - complexities , different env in coded, - JS SDK , for any website integration - React native SDK, zype - Android SDK - koitlin - IOS SDK - swift - Flutter in works - - what is required to invoke a SDK - auth, cust code , sso token - primary secondry colour - step of the customer journey , - API Credit management for partner to poll the application status - version 1.2 m

---

## #33 — Withdrawal Optimisations
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

## #34 — LOS and LMS admin actions (LSP with DSP as lender)
**Status:** In progress | **Last edited:** October 16, 2024 2:25 PM

**Problem:**
are we solving?**

We have developed multiple admin actions (ops controlled actions) that help in servicing our customers in the onboarding as well as the servicing journey. 

This requirement covers utilising the admin actions (where needed) to cover use cases currently served by LSP (for customers) with DSP as a lender.

---

**Solution:**
?**

---

## #35 — Bulk email automation
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

## #36 — Integrated Sales tool
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

## #37 — Simplify B2B Partner Redirection Journey
**Status:** In progress | **Last edited:** October 11, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #38 — Lender selection logic for BRE for production
**Status:** Ready for Tech | **Last edited:** October 11, 2024 4:47 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

I’m not able to find the logic of TATA/BAJAJ based on fetch limit

---

## #39 — [Lending stack] KYC Flow
**Status:** Not started | **Last edited:** October 11, 2024 4:17 PM

**Problem:**
are we solving?**

Complete KYC of the customer for DSP lender. For completing a successful CDD, following are the requirements as per regulations.

1. Proof of possession of Aadhaar number.
2. Verified E-document of Aadhaar (to be used as proof of address)
3. PAN should be verified fro mt hte issuing authority. 
4. PAN details/document (to be used as proof of identity). 

---

**Solution:**
?**

---

## #40 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

**Solution:**
?**

---

## #41 — API and Transaction Logging
**Status:** In progress | **Last edited:** October 11, 2024 11:39 AM

**Problem:**
are we solving?**

Currently, we log all our API hits in our DB. However, this isn’t sufficient since this results in the below challenges.

- Lack of visibility at an API level
- Lack of visibility of API level HTTP codes
- Ease of access of API level error or status codes
- Ease of access of API level request and response timestamps
- Lack of storage of computation like name match, etc
- Considerable amount of bandwidth dedicated in extracting data
- Lack of visibility of product level metrics
- Lack of proactive/reactive alerting mechanisms

These challenges result in requiring product, ana

**Solution:**
?**

---

## #42 — DSP MFD Flows
**Status:** Not started | **Last edited:** November 9, 2024 5:28 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #43 — Process note Creating a new user on Command Centre
**Status:** Done | **Last edited:** November 8, 2024 9:36 AM

# Process note: Creating a new user on Command Centre # Process Note: Creating a User on Command Centre ## Overview This document outlines the step-by-step process for creating a new user account on the Command Centre system. ## Prerequisites - Admin access to the Command Centre system - New user's details (full name, email address, role, department) - Approval from Head of Operations (@Nishant Athmakoori) [Access level details](https://docs.google.com/spreadsheets/d/1VSPMYia-Kmwob9X3pH-T3nMTYNZxXpEC_Afpfq27e-o/edit?gid=0#gid=0) ## Steps 1. Request for access on Email from the business counterpart, in this case, all access will be shared by @Nishant Athmakoori 1. Details required in the email: 1. Name 2. Designation 3. Role (Admin / Approver / Read only) 4. Employee ID 5. Mobile number 6. Email address (DSP Email address) Any requests without the aforementioned details will get rejected 2. Forward the access with consent and approval to tech-ops@dspfinance.com 3. Access will be shared within 1 working day of request. 4. Once access is shared (User name and password), logon to the command centre using the following URL: https://cc.dspfin.com/login 5. Once logged on, users will be able to use the command centre for the following utilities: 1. Client search (all roles) 2. Loan search (all roles) 3. Review client details (all roles) 4. Review client KYC details (all roles) 5. Review client risk details (all roles) 6. Review loan details (all roles) 7. Review transactions (money and collateral) (all roles) 8. View servicing tasks (Approver and admin only) 9. View collateral tasks (Approver and admin only) 10. View application tasks (Approver and admin only) 11. View NBFC operations tasks (Approver and admin only) 12. Approve or reject tasks (Approver and admin only) ## Post-Creation Steps - Document the new user creation in your system log or user management spreadsheet ## Troubleshooting If you encounter any issues during this process, please contact the IT support team at tech-ops@dspfinance.com

---

## #44 — Excess amount handling
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

## #45 — Mandate Set up optimisation - Error Messaging + Ne
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

## #46 — Lien removal SLA tracking report
**Status:** Ready for Tech | **Last edited:** November 7, 2024 8:13 AM

**Problem:**
are we solving?**

Users raise lien removal requests via Volt app and web app which are raised directly with the lenders. 

Lien removal requests have broadly three steps:

1. Lien removal request validation
2. Unlodgement of funds
3. Unpledging of funds

The process for the first two steps is done digitally via API however unpledging is done operationally via letters send to the RTAs (CAMS and Kfintech).

Volt and lenders have an operational workflow set between the teams of the two organisations and they need a report to manage SLAs.

**Problem statements:**

1. Volt ops agents should be abl

**Solution:**
?**

Two reports (Revocation request level and ISIN level will be created which will be sent to the lender

**Report 1:**

Created_on

Loan account number - Lender loan account number (Credits)
Loan contract number - Lender credit ID (Credits)
Customer name - Borrower name (Borroweraccounts)
VOLT request ID - Revocation request ID (revocation requests)
Customer PAN - AccountholderPAN (Borroweraccounts)
Total outstanding amount - Netpayable (Credits) - 

Update (07-17) - At the time of making request (Needs to be stored while making the request)
DP before un-pledging - Assetlimitbeforepledging (Revocationrequests)

Update (07-17) - At the time of making request (Needs to be stored while making the request)
DP after un-pledging - Assetlimitbeforepledging (Update (07-17) - At the time of maki

---

## #47 — Repayments Error Handling and Changes
**Status:** In progress | **Last edited:** November 6, 2024 1:24 PM

**Problem:**
are we solving?**

Customers are facing issue in receiving repayment confirmation from TATA due to SOA not getting updated from TATA’s end. This results in the below challenges.

- Customer satisfaction (CSAT) impacted
- Reduced retention due to poor customer experience
- Number of customer support tickets increase

These issues arise due to failure to account a successful payment at the Payment Gateway (PG) level to the Statement of Account(SOA) of the user due to an error in the saveLoanReceipt API.

Total failure rate ~ 3%

- Current failure rates for successful transactions is 1.37%
- Fail

**Solution:**
?**

---

## #48 — [IronGrid] Un-lien related issues
**Status:** Not started | **Last edited:** November 5, 2024 12:48 PM

# [IronGrid] Un-lien related issues ## Fund level status of un-pledge request **Phase 1** - Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED. - We will keep polling the status of all the funds until we get the terminal statuses of each of the funds - We keep polling the API for 4 days every hour until we get the status of all the fund - Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached) - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request - We will store the individual status of all the funds under the un-pledge request - API Documentation : [Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx) **Phase 2** - We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user. ## Excess margin handling in un-pledge request **For BFL (only need to make this change for BAJAJ)** - While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge. - 3 fields which are present in Foreclosure details API : - net payable = Total due - Excess Margin - Total Due - Excess Margin - For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding. ### **User not able to request un-lien request if stocks present in their holding** - **Issue** - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error - **Solution** - We will only

---

## #49 — Father’s name validation removal
**Status:** Not started | **Last edited:** November 30, 2025 12:18 PM

**Problem:**
are we solving?**

LSPs are currently seeing high rejection rates at the **Submit Opportunity** stage due to mismatches between the user-entered *father’s name* and the value returned from KYC.

Since the RBI’s KYC Master Directions do **not** mandate verification of the father’s name—and it is required only for CKYC reporting—strict validation is unnecessary. Most regulated entities rely on customer-provided details with minimal checks, which aligns with our revised approach.

---

**Solution:**
?**

---

## #50 — Lodgement maker
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

## #51 — NBFC Virtual Accounts for Repayments (Alignment)
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

## #52 — LSQ misattribution b2c of B2b2c data
**Status:** Ready for Tech | **Last edited:** November 27, 2024 11:25 AM

# LSQ misattribution b2c of B2b2c data # B2C to B2B2C Lead Update Specification ## Background When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues: 1. Lead tracking inefficiencies 2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams) 3. MFD partner dissatisfaction with direct customer contact ## Objective Reduce misattributed leads - Reduce Creation of the new Misattributed leads. - Update LSQ with admin action (tech pickup) - Backfill data to correct misattribution Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database. ## Technical Implementation ### API Details - **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate) - **Identifier**: Mobile Number (unique in LSQ) ### Required Field Updates ```json { "LeadDetails": [ {"Attribute": "mx_Channel", "Value": "B2B2C"}, {"Attribute": "Source", "Value": "MFD Referral"}, {"Attribute": "mx_Referred_By", "Value": "MFD"}, {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"}, {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"}, {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"}, {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"}, {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"}, {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"}, {"Attribute": "SearchBy", "Value": "Phone"} ] } ``` ## Data Migration Plan ### Initial Data Reconciliation - Tech team to provide excel export of leads updated via admin actions - Data to be shared with LSQ team for backfill - Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count) ### Scope Limitations - Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ - Focus on forward data synchronization and provided historical data only ### MFD Status Handling - Automated daily updates for partially-activated MFD status ## Requirements ### Technical Requirements 1. Admin action implementation for borrower-partner relationship updates 2. API integration with error handling 3. Comprehensive update logging for audit purposes ### Acceptance Criteria 1. Successful lead type transition (B2C to B2B2C) 2. Accurate referrer information mapping 3. Proper API response handling 4. Complete audit logging 5. Visual verification in LSQ dashboard ## Important Notes - Mobile Number serves as the unique identifier in LSQ - Lead merges occur when same email is used with different phone numbers - Implementation must include robust error handling for API failures - API failures should be notified to the team.

---

## #53 — TCL Credit Referral Automations & optimisations
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

## #54 — Volt B2B Redirection Enhancement - Park+
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

## #55 — TATA Dedupe API with updated BRE
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

## #56 — QC rejection flow handling for DSP - Volt LOS
**Status:** Not started | **Last edited:** November 20, 2024 9:35 AM

**Problem:**
are we solving?**

When an LSP shares an application with DSP a QC task is generated which helps the operations team (DSP) to validate multiple parameters related to the loan application.

The operations team at DSP may find certain issues with the applications like:

- Name mismatch (Bank and Pan/Aadhaar)
- Age above threshold
- Issues in agreement

Which may lead them to reject the user’s application. When an application is rejected by the lender, a callback is shared (by the lender) to the LSP. 

However the same is not being consumed by Volt. This will lead to bad customer experience, as L

**Solution:**
?**

Callback by DSP will contain the following details:

- Opportunity ID
- Remarks (added by operations team at DSP)

Following needs to be consumed by the LSP. 

Current scope:

Post consuming the callback we will perform the following actions:

- Send a communication to the operations team
- Change the status of the application to blocked

Volt ops communications:

- Template ID: d-2c4e1d4b6d6a40c2a314b7c59a9c8ed0
- Variables:

```json
{
	"lender": "DSP",
	"contactEmail": "operations@voltmoney.in",
	"customerMobile": "+919611749097",
	"supportEmail": "support@voltmoney.in",
	"customerName": "Vaibhav Arora",
	"opportunityId": "234982390423",
	"rejectionRemarks": "Name mismatch"
}
```

---

## #57 — QA setup for Partners
**Status:** Not started | **Last edited:** November 20, 2024 2:05 PM

# QA setup for Partners ## Current Challenges 1. No test coverage for SDK implementations 2. Absence of platform logging 3. No standardized testing setup for partner journeys 4. Limited testing capabilities through playground environment ## Immediate Priority Areas ### 1. Test Coverage Implementation (Q1) - **SDK Testing Framework** - Implement unit testing for all SDK versions (JS, RN, Android, iOS) - Set up integration testing framework - Target initial coverage of 60% for critical paths - Required Resources: 2 QA Engineers, 1 DevOps Engineer - **Frontend Testing** - Implement E2E testing using Cypress/Playwright - Create component testing suite - Setup visual regression testing - Required Resources: 1 QA Engineer, 1 Frontend Developer ### 2. Logging & Monitoring System (Q1) - **Platform Logging** - Implement centralized logging system (ELK Stack/Splunk) - Set up real-time monitoring dashboards - Create alert mechanisms for critical failures - Required Resources: 1 DevOps Engineer, 1 Backend Developer ### 3. Partner Journey Testing Framework (Q2) - **Automated Testing Setup** - Create standardized test cases for each integration type - Redirection flows (PhonePe, Park+, etc.) - SDK implementations (Jupiter, Zype, etc.) - Implement automated testing pipeline - Setup test data management system - Required Resources: 2 QA Engineers ### 4. Testing Environment Enhancement (Q2) - **Enhanced Playground** - Develop comprehensive testing interface - Create partner-specific testing scenarios - Implement mock services for external dependencies - Required Resources: 1 Frontend Developer, 1 Backend Developer ## Resource Requirements Summary - 2 QA Engineers (Full-time) - 1 DevOps Engineer - 1 Frontend Developer - 1 Backend Developer - Testing Infrastructure Budget ## Implementation Timeline ### Phase 1 (Q1) 1. Week 1-2: Setup basic testing infrastructure 2. Week 3-6: Implement logging system 3. Week 7-10: Develop SDK testing framework 4. Week 11-12: Initial frontend testing implementation ### Phase 2 (Q2) 1. Week 1-4: Partner journey framework development 2. Week 5-8: Enhanced playground implementation 3. Week 9-12: Integration and system testing ## Success Metrics 1. Test Coverage: - 80% coverage for critical paths - 60% overall coverage 2. Platform Stability: - 99.9% uptime for integration services - <1% failed transactions due to technical issues 3. Partner Satisfaction: - <4 hours mean time to resolution for critical issues - Zero production deployments with partner-impacting bugs ## Budget Considerations 1. Infrastructure costs - Testing environments - Monitoring tools - CI/CD pipeline enhancements 2. Team costs - New hires - Training - Tools and licenses

---

## #58 — TCL getDisbursementAPI logic updation
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

## #59 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #60 — Foreclosure handling for DSP
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

## #61 — External reporting requirements
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

## #62 — White-labelled Redirection Journey for B2B Partner
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

## #63 — MFC Summary API calculations update
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

## #64 — Repayment flow for DSP
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

## #65 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #66 — Enhancement to MFD partner Signup page
**Status:** Pending Review | **Last edited:** May 8, 2025 4:19 PM

# Enhancement to MFD partner Signup page **Product Updates** ## **1. Enhanced Partner Login Experience:** - **Feature:** Mobile Number Pre-fill & Browser Autofill Support. - **Problem:** Returning partners re-enter mobile numbers, causing friction. - **Goal:** Faster, more convenient login. - **Solution:** - **Custom Pre-fill:** Store last successfully used/OTP-requested mobile number in browser local storage for automatic pre-population. (Editable by partner). - **Browser Autofill Hint:** Add autocomplete="tel" to the mobile number field to allow browsers (like Chrome) to suggest saved phone numbers. - **Benefit:** Quicker login, reduced errors, improved partner experience. ## **2. Improved Partner Empanelment Form:** - **Feature:** Browser Autofill for Empanelment Details. - **Problem:** Manual entry of common details (name, email, city, company) is time-consuming. - **Goal:** Faster and more accurate empanelment. - **Solution:** Implement standard HTML autocomplete attributes (e.g., name, email, address-level2, organization) on relevant input fields. - **Benefit:** Quicker form completion, fewer typing errors, smoother empanelment. ## **3. Branding & Content Updates:** - **Logo Update:** Replaced Bajaj Finserv logo with DSP logo in "Our trusted partners" section. - **Partner Count Update:** Updated "2000+ Partners have joined Volt Money" to "3000+ Partners have joined Volt Money". - **Benefit:** Reflects current partnerships and growth accurately.

---

## #67 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #68 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #69 — PhonePe Contact support changes - 12th April 2024
**Status:** Not started | **Last edited:** May 6, 2024 9:14 AM

**Problem:**
are we solving?**

1. PhonePe has sent a requirement to stop lead leakage due to Volt support number available on the landing page. 
2. Number of junk inbound calls has increase 4x

---

**Solution:**
?**

---

## #70 — DSP KFS & Agreement for LSPs
**Status:** In progress | **Last edited:** May 5, 2025 5:36 PM

**Problem:**
are we solving?**

Currently, a lot of the LSPs don’t want to showcase DSP 

---

**Solution:**
?**

---

## #71 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #72 — MFC Pledge error handling - V1 (1)
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

## #73 — PhonePe press release - 30th May 2024
**Status:** Not started | **Last edited:** May 30, 2024 10:11 AM

**Problem:**
are we solving?**

Creating a static landing page for PhonePe press release due to release on 30th May. 

---

**Solution:**
?**

---

## #74 — Phase 1 LTV Tenure Update_LOS
**Status:** Not started | **Last edited:** May 29, 2026 8:52 AM

**Problem:**
are we solving?**

DSP's LAMF product offers 45% LTV on equity and hybrid funds, compared to 70% LTV offered by banks — making it structurally uncompetitive. This gap limits DSP on three fronts:

- **Existing customers** are under-drawing against already-pledged assets, leaving loan book growth on the table
- **New customers** in lower-ticket segments have sufficient collateral at 70% LTV but fall below viable thresholds at 45%
- **Product parity** with banks cannot be achieved without closing this 25pp LTV gap

---

**Solution:**
?**

**In scope:**
Product

- Support for both LTV45 & 70 product offers
- Support for  6-year tenure migration
- Partner-specific product config (LTV 45/70) for recommended offer
- Providing offer visibility to Sales/CS

Customer Scope

- New customers
- In journey users

Platform Scope

- DSP (Fenix)
- LSP integrations
- Volt & its partners

Product scope

- Term Loan
- LAMF

---

## #75 — [Platform] Callbacks for LSP APIs for core servici
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

## #76 — PRD — Term Loan Repayment STP Threshold Update
**Status:** Not started | **Last edited:** May 29, 2026 5:51 PM

**Problem:**
are we solving?

- Current STP repayment thresholds are overly conservative, causing valid low-risk repayments to be unnecessarily routed to NSTP via `REPAYMENT_AMOUNT_LIMIT_EXCEEDED` (>₹15L) and `REPAYMENT_DAILY_COUNT_EXCEEDED` (>4 repayments/day per LAN).
- Jan–May 2026 production data shows minimal breach risk: only 3 of 1,952 customers (0.15%) made repayments above ₹15L (max observed: ₹20.1L), and no LAN exceeded 5 repayments in a day — indicating the limits can be safely relaxed.
- Unlike other LSPs (Razorpay for Volt, PhonePe dashboard for PhonePe), there is no Cred repayment dashboard a

---

## #77 — Custom Comms based for Ad-hoc situations v2
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

## #78 — Sell-off Repayment Reconciliation — Maker Automati
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

## #79 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #80 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #81 — [DSP] Additional customer comms (compliance)
**Status:** In progress | **Last edited:** May 28, 2025 12:27 PM

**Problem:**
are we solving?**

Sending additional comms to users to comply with DLG and internal compliance requirements. 

---

**Solution:**
?**

---

## #82 — PRD - B2C Referral [Phase-1 1]
**Status:** In progress | **Last edited:** May 27, 2026 4:29 PM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new us

**Solution:**
?**

---

## #83 — STP validation for Sell-off Repayment Reconciliati
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

## #84 — Migrating MFD Partners to the LSQ Accounts
**Status:** Ready for Tech | **Last edited:** May 27, 2025 2:25 PM

# Migrating MFD Partners to the LSQ Accounts [**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md) - Accounts are now enabled for org: volt - Reading LSQ documentation to understand and create a transition plan - MFD is currently treated as lead and should be moved to accounts - RMs will be assigned accounts and will be responsible for its success - All the customer of a MFD will be under their account - **1. Purpose & Goal:** - **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data. - **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads. - **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership). **3. Procedure:** **Phase 1: Configure the Accounts Module for MFDs** Setting up the Accounts entity for MFDs - **3.1 Identify Required MFD Fields:** - Review the current Lead fields list - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples: - PAN - ARN No - Referral Code / Partner Code - Partner Referral Link - Partner Type - Platform / Platform Id - Empanelment Date - Company (if used for MFD firm name) - Key contact details (Email, Mobile Number, Address, City, State, Zip Code) - Ownership (Owner) - Any other relevant custom fields. - **3.2 Create Custom Account Fields:** - Adding all the Lead files to account - For every required MFD field *not* present by default in Accounts, create a custom field: - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions - Click **Add**. - Define: - **Display Name:** - **Schema Name:** format cf_display_name. custom field for easy reference - **Field Type:** Match - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/) - 3.3 Add Drop-downs in fields like stage, etc. **Phase 2: Migrate MFD Data from Leads to Accounts** - **3.4 Extract MFD Leads:** - Manage leads - Use **Advanced Search** Lead Type != MFD - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**. - **Export:** Select Actions -> Export Leads -> Export as CSV. - **3.5 Prepare the Import File

---

## #85 — Phase 0 LTV Tenure Update_LOS
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

## #86 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #87 — MFC Summary API integration
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

## #88 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #89 — LSQ Chat workflow - Phase 1
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

## #90 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #91 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #92 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #93 — Lodgement STP optimisations
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

## #94 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #95 — Lead Follow-Up Mechanism — Old Leads
**Status:** Not started | **Last edited:** May 19, 2026 6:08 PM

# Lead Follow-Up Mechanism — Old Leads ## Objective Design a structured follow-up mechanism for old leads to: - Ensure periodic engagement - Maximize lead conversion - Control automation usage - Avoid excessive calling - Standardize disposition-driven follow-ups # 1. Lead Segmentation ## Lead Types ### 1. New Leads - Real-time lead assignment - Immediate engagement journey - Separate automation flow ### 2. Old Leads - Leads not converted - Re-engagement campaign - Monthly task-based follow-up mechanism # 2. Old Lead Follow-Up Workflow ## Monthly Trigger ### Automation 1 At the beginning of every month: - Create calling task for all eligible old leads ### Eligibility Conditions - Lead not converted - Lead not closed permanently - Lead not activated - Lead within retry policy # 3. Agent Calling Workflow ## Step 1 — Agent Filters Pending Tasks Agent opens: - Same-day pending tasks - Older pending tasks ## Step 2 — Open Task Agent initiates call. ## Step 3 — Add Disposition Agent marks call outcome. # 4. Disposition-Based Follow-Up Logic | Call Outcome | Sub-Disposition | Action | Next Follow-Up | | --- | --- | --- | --- | | Connected | Interested | Create Follow-Up Task | T+4 | | Connected | Follow-Up Required | Create Follow-Up Task | T+3 | | Connected | Not Interested | Close Task | No Retry | | Connected | MFD Activated | Close Task | No Retry | | Connected | Other Dispositions | Close Task | No Retry | | RNR | — | Create Retry Task | T+2 | | Asked to Call Back | — | Create Retry Task | T+1 | # 5. Calling Attempt Policy ## Monthly Attempt Limits | Criteria | Count | | --- | --- | | Minimum Calls per Lead | 4 | | Recommended Maximum | 8 | | Absolute Maximum | 10 | # 6. Retry Logic ## Retry Rules - Retry only if: - RNR - Callback Requested - Follow-Up Needed - Interested - Stop retries if: - Not Interested - Activated - Invalid - Duplicate - DND - Converted # 7. Automation Consumption Model ## A. Initial Monthly Task Creation | Activity | Automations | | --- | --- | | Monthly Task Creation | 1 | ## B. Per Call Attempt Each call consumes: | Automation Activity | Count | | --- | --- |

---

## #96 — Consent Architecture FE requirements
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

## #97 — Dues Comms Updation
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

## #98 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #99 — Term Loan LOS requirements
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

## #100 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #101 — Product Note LTV update to 70
**Status:** Not started | **Last edited:** May 12, 2026 10:39 AM

# Product Note : LTV update to 70 --- # **1. Problem Statement** --- ## **2. Objective** --- ## **3. Scope** --- - LTV update task - Finflux - Multiple approved script management - Validations - Any sort of handling - Fenix - Multiple approved scripts handling - Risk and RMS validations required - Impact of all collateral transactions - Collateral addition - Collateral removal - Collateral invocation - Shortfall handling - Communications and statements - ROI auditing - Current offer visibility for NBFC and LSPs - Volt - Journey - Enhancement (Fetch/Pledge/Offer/Agreement) - Nudges - B2B2C & B2C - PF/ROI changes - Journey - Admin actions (PF increase to work out of the box) - Payout - Scope reduction - Loan offer - PF/ROI - Contract level - Volt UI --- - Nudge - Current limit - Updated Limit - Current ROI - New ROI - LTV update charges - KFS/Agreement - Task name - Service request approval - Left panel - Request details - Request ID - Service request type : Limit enhancement - Requested on - Current collateral limit - Additional collateral limit - Updated collateral limit - Limit enhancement charges - AMC charges - Substatus - Maker name - Maker remark - Maker created on - Collateral details - ISIN - Asset type - Collateral sub type - Folio - Value - Existing limit - New limit - Right panel - Client details - Loan details - With loan contract - Transactions - Collaterals - Collaterals with details (LTV) - Loan kit - KFS - Agreement - Generate offer what happens? - Request - FXLAN (with collateral details) - Response - Funds with higher LTV - Limit enhancement charge ranges - AMC charge ranges - ROI ranges - Accept offer - Request - Fund with LTV, charges & ROI details - Response - Offer ID - Service request and collateral addition in parallel, what validations to happen

---

## #102 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #103 — Enhanced Customer Registration & Deduplication for
**Status:** Done | **Last edited:** May 12, 2025 12:46 PM

# Enhanced Customer Registration & Deduplication for MFDs **Enhanced Customer Registration & Deduplication for MFDs** ### **Problem** 1. MFDs often hit blockers or need RM support when trying to register customers who already exist in Volt’s system (e.g., as B2C users, under another B2B partner, or with active loans). 2. The current error message—“Failed to register customer”—is vague and doesn’t guide the MFD on what to do next based on the type of duplicate. 3. There were 1,200 such error on MFD portal. ~50% of the registered TOFU. and 185 admin actions to Map partners ### **Goal** - Simplify the customer registration journey for MFDs, especially in common duplicate scenarios. - Reduce RM dependency, particularly for B2C linking. - Provide clear, actionable feedback to MFDs when a duplicate is found. ### **Proposed Solution: Automat** When an MFD submits “Register Customer” with Name, Mobile, and: ### 1. **Backend Deduplication Check** - Use Mobile and to detect existing customer records. ### 2. **Modal-Based Responses Based on Scenario** - **A. New Customer (No Prior Account)** - **Action:** Add customer —> OTP - **UI:** No modal or interruption. - **B. Customer Exists as B2C (Registered directly on Volt)** - **Modal Title:** *Customer Found in Volt* - **Message:** “This customer is already registered directly with Volt. To add them to your portfolio, OTP verification is required.” - **CTAs:** - “Send OTP & Add Customer” (launches OTP flow) - “Cancel” - **C. Customer Linked to Another Partner or Has Active Application** - **Modal Title:** *Customer Already Registered* - **Message:** “This customer ([Name or Masked ID]) is already registered with Volt and may be linked to another partner or have an active application/loan. Please contact your RM for support.” - **CTA:** “Okay” (returns MFD to form) - **D. Typo/Error in Initial Input (Pre-dedupe)** - If the MFD catches a mistake before dedupe runs (e.g., wrong PAN), allow them to use the existing “Edit details” button. - Once dedupe identifies a match, scenario-specific modals override the generic error message. ### **Key Requirements** - Backend API for robust deduplication using PAN/Mobile. - API must return customer status: - Not found - Existing B2C - Linked to another partner - Active loan/application - Dynamic modals based on API response. - OTP flow for linking B2C customers to MFDs. - Clear attribution/commission logic for B2C linking. ### **Benefits** - Fewer MFD drop-offs and RM escalations. - Seamless onboarding for B2C customers

---

## #104 — DSP PhonePe PG Integration for PhonePe
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

## #105 — [Volt LSP] Supporting multiple products for same c
**Status:** Not started | **Last edited:** March 5, 2025 6:06 PM

**Problem:**
are we solving?**

Immediate problem: 
BFL has stopped new applications (Including enhancement) with Volt. Current customers who want to enhance their credit line are not able to do so. To solve their need of enhancing their credit limit we are thinking of a dual credit line solution where the customer will open a new credit line with DSP and the existing credit line from BFL/Tata will remain active. 

---

**Solution:**
?**

---

## #106 — Mandate limit change
**Status:** Not started | **Last edited:** March 5, 2025 3:41 PM

# Mandate limit change # Credit Limit Increase Analysis (Excluding <10K Initial Credit Limit) Based on the analysis of 10,467 valid records with initial credit limits of 10K or greater, here's the comprehensive breakdown: ## Applications by Initial Credit Limit Range and Percentage Increase | Initial Credit Limit | 0-400% | 400%-600% | 600%-800% | 800%-1000% | 1000%+ | Total | | --- | --- | --- | --- | --- | --- | --- | | 10K-25K | 119 | 13 | 8 | 2 | 16 | 158 | | 25K-1L | 2,361 | 78 | 24 | 25 | 84 | 2,572 | | 1L-5L | 4,393 | 81 | 51 | 27 | 41 | 4,593 | | 5L-25L | 2,432 | 42 | 17 | 8 | 18 | 2,517 | | 25L+ | 620 | 6 | 1 | 0 | 0 | 627 | | **Total** | 9,925 | 220 | 101 | 62 | 159 | 10,467 | ## Percentage Increase Distribution | Range | Count | Percentage | | --- | --- | --- | | 0-100% | 7,858 | 75.07% | | 100%-200% | 1,383 | 13.21% | | 200%-300% | 471 | 4.50% | | 300%-400% | 213 | 2.03% | | 400%-500% | 133 | 1.27% | | 500%-600% | 87 | 0.83% | | 600%-700% | 57 | 0.54% | | 700%-800% | 44 | 0.42% | | 800%-900% | 29 | 0.28% | | 900%-1000% | 33 | 0.32% | | 1000%-1500% | 58 | 0.55% | | 1500%-2000% | 28 | 0.27% | | 2000%+ | 73 | 0.70% | ## Applications with 400%+ Credit Limit Increase by Range | Initial Credit Limit | Count | % of Range | | --- | --- | --- | | 10K-25K | 39 | 24.68% | | 25K-1L | 211 | 8.20% | | 1L-5L | 200 | 4.35% | | 5L-25L | 85 | 3.38% | | 25L+ | 7 | 1.12% | | **Total** | 542 | 5.18% | ## Cumulative Distribution | Up to | Count | Percentage | | --- | --- | --- | | 100% | 7,858 | 75.07% | | 200% | 9,241 | 88.29% | | 300% | 9,712 | 92.79% | | 400% | 9,925 | 94.82% | | 500% | 10,058 | 96.09% | | 600% |

---

## #107 — [Platform] Unpledging of unlinked funds bulk appro
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

## #108 — [IronGrid] Email trigger for ops in case of disbur
**Status:** Not started | **Last edited:** March 31, 2026 8:24 AM

**Solution:**
?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

---

## #109 — [Volt LSP] Integrating DSP KYC
**Status:** Not started | **Last edited:** March 3, 2025 2:38 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #110 — [Platform] Foreclosure handling and enhancement
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

## #111 — PN Storing Commercial Data at Credit Level
**Status:** Pending Review | **Last edited:** March 3, 2025 12:37 PM

# PN: Storing Commercial Data at Credit Level ## Problem Statement Currently, we do not store Platform-level commercial data directly at the Credit level. Instead, this data is maintained in external Excel sheets, which creates inefficiencies in the payout calculation process. The data team must manually add these commercial details when creating payout files, resulting in: - Increased processing time - Higher risk of manual errors - Difficulty in data reconciliation - Lack of data integrity between systems ## Proposed Solution Implement a dedicated commercial data object at the Credit application level that will store all relevant commercial parameters at the time of application processing. ## Key Data Points to Store The Credit level commercial data object should include: - **Lender**: The financial institution providing the loan - **Base ROI**: Original interest rate from lender pricing grid - **Base PF**: Original processing fee from lender pricing grid - **PF Split**: Processing fee revenue distribution between platform and partners - **ROI Split**: Interest revenue distribution between platform and partners - **Payout Amount PF**: Calculated processing fee payout amount - **Payout ROI**: Calculated interest-based payout amount ## Implementation Benefits 1. **Data Integrity**: Single source of truth for commercial terms at the application level 2. **Audit Trail**: Historical record of commercial terms applied to each application 3. **Streamlined Reporting**: Direct data access for reporting without manual intervention 4. **Efficient Payout Processing**: Automated payout file generation based on stored values 5. **Reduced Manual Effort**: Elimination of manual data enrichment processes ## Considerations - Create a new data structure to store commercial data as part of the credit application object - Implement data validation to ensure complete commercial information - Add timestamp and user attribution for commercial data changes ## Example data table | **S_No** | **Platform** | **Type** | **Tata Interest base rate** | **Bajaj Interest base rate** | **DSP Interest base rate** | **Tata PF base rate** | **Bajaj PF base rate** | **DSP PF base rate** | **PF Sharing** | **Trail Sharing** | **PF Sharing %** | **Trail Sharing %** | **Comments** | Signoff | Actionable | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 | Advisorkhoj | Partner | | | | | | | | 0.5 | | | | | | |

---

## #112 — BharatPe changes
**Status:** In progress | **Last edited:** March 28, 2024 7:26 PM

**Problem:**
are we solving?**

For our B2B partner BharatPe we are making a few changes to make the post loan application journey for the user as smooth as possible.

---

**Solution:**
?**

---

## #113 — Custom Comms based for Ad-hoc situations
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

## #114 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** March 24, 2026 11:57 AM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #115 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #116 — [Platform] Wrapper APIs for RTAs
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

## #117 — Withdrawal issues enhancement
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

## #118 — [B2B2C] GST payouts and reconciliation optimisatio
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

## #119 — Credit Bureau Reporting Comms
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

## #120 — [Volt LOS] KYC optimisations
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

## #121 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #122 — [B2B2C] Modification for financial terms functiona
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

## #123 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #124 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #125 — Product note Co-lending foreclosure - Deprecated -
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

## #126 — Capital gains tax calculator
**Status:** In progress | **Last edited:** March 15, 2024 6:49 PM

**Problem:**
are we solving?**

1. Users currently don’t have a resource readily available that helps them calculate and create a consolidated MF capital gains/losses report from all their brokers. 
2. Users also don’t know how much tax they will have to pay on these gains due to complex categorisations of these gains. 
3. MFD users similarly don’t have a resource readily available where they can create a consolidated capital gains statement for their clients.  

---

**Solution:**
?**

1. Create a report/statement generator that enables users to download a report that gives them a consolidated understanding of their MF capital gains. 
2. We will also build a summary in UI that gives them approximate understanding of how much tax they will have to pay in different categories of capital gain/losses.

---

## #127 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #128 — [DSP] Facility value limit
**Status:** Not started | **Last edited:** June 6, 2025 1:34 PM

**Problem:**
are we solving?**

Current the way we are defining the Facility Value limit in our agreements in not very understandable for the user;

Following is the fin

---

**Solution:**
?**

---

## #129 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #130 — Margin pledge charges
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

## #131 — Bajaj KYC Coborrower enhancement and renewal
**Status:** Not started | **Last edited:** June 5, 2024 1:29 PM

**Problem:**
are we solving?**

1. Currently users with joint holdings can not do KYC.
2. Customer with Bajaj lender will not be able to enhance or renew their line. 

---

**Solution:**
?**

---

## #132 — Increase Credit Utilization via Whatsapp Drips
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

## #133 — 1400 160 Series Outbound Implementation
**Status:** Not started | **Last edited:** June 25, 2025 1:15 PM

# 1400/160 Series Outbound Implementation Check list: 1. Internal Approval- sent heads-up mail 2. Commercial alignment 3. Exotel-implementation - for DSP → Phone number acquisition for Volt → Outbound implementation Step 1: DLT registration We need DLT registration with Tata. Understand the automations made and how the change might affect these automations. Step 2: Confirm and Acquire the number.

---

## #134 — Unlock credit limit revamp
**Status:** Not started | **Last edited:** June 24, 2024 10:53 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #135 — Virtual Accounts for LSPs
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

## #136 — DSP UPI Autopay Integration for PhonePe
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

## #137 — Margin pledge charges
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

## #138 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #139 — DSP UPI Autopay Integration for NBFC
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

## #140 — [DSP] NSDL PAN Verification alignment
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

## #141 — PhonePe KFS & Agreement
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

## #142 — B2B Zype integration FE and SDK callbacks
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

## #143 — Disbursement workflow optimisations
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

## #144 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #145 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #146 — MFC Pledge (revocation & invocation)
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

## #147 — [Jupiter] Unlock credit limit page changes
**Status:** Not started | **Last edited:** July 31, 2024 5:41 PM

**Problem:**
are we solving?**

Change copies on the verify interest and charges page for partners with MFC fetch. 

---

**Solution:**
?**

---

## #148 — [Platform +Volt ] MFC Pledge wrapper APIs + Volt J
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

## #149 — MFD Account View in LSQ
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

## #150 — Tata Video KYC Integration V0
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

## #151 — Razorpay PG SDK integration DSP (1)
**Status:** Ready for Tech | **Last edited:** July 29, 2025 2:16 PM

**Problem:**
are we solving?**

As an LSP we have integrated with lender repayments flow via web integrations where the repayment pages are loaded as screens (web-view) and open the URLs in the web-view (Android and iOS) or as tabs replacing Volt’s URL (Web). 

In parallel, we rely on backend for the status of the user sessions via deep checks. This process is not optimal and often causes the following issues:

1. Blank screen opens (link comes from backend via lenders) 
2. Delayed status (backend is dependent on lender for status, client application gets status from backend)
3. Web hook drops - Amount get

**Solution:**
?**

We will be integrating React Native SDK for Android and iOS to improve user experience while they make repayments as a client side integration with Volt.

**Documentation:**

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/) (Android)

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/) (iOS)

---

## #152 — Razorpay PG SDK integration DSP
**Status:** Ready for Tech | **Last edited:** July 29, 2025 2:15 PM

**Problem:**
are we solving?**

As an LSP we have integrated with lender repayments flow via web integrations where the repayment pages are loaded as screens (web-view) and open the URLs in the web-view (Android and iOS) or as tabs replacing Volt’s URL (Web). 

In parallel, we rely on backend for the status of the user sessions via deep checks. This process is not optimal and often causes the following issues:

1. Blank screen opens (link comes from backend via lenders) 
2. Delayed status (backend is dependent on lender for status, client application gets status from backend)
3. Web hook drops - Amount get

**Solution:**
?**

We will be integrating React Native SDK for Android and iOS to improve user experience while they make repayments as a client side integration with Volt.

**Documentation:**

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-android/) (Android)

[https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/](https://razorpay.com/docs/payments/payment-gateway/react-native-integration/standard/build-integration-ios/) (iOS)

---

## #153 — [DSP] Mandate enhancements Handling of charge coll
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

## #154 — Repayment Lifecycle Tracking
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

## #155 — [DSP] Borrower agreement execution flow change
**Status:** Ready for Tech | **Last edited:** July 21, 2025 2:52 PM

**Problem:**
are we solving?**

Making sure the agreement execution happens in the newly aligned order

---

**Solution:**
?**

---

## #156 — Making Mobile & Email Verification Log Optional LO
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

## #157 — Implementing UTR dedupe for repayment postings
**Status:** Pending Review | **Last edited:** July 14, 2025 3:52 PM

**Problem:**
are we solving?**

---

- We currently do not perform a deduplication (dedupe) check on incoming repayment requests from Lending Service Providers (LSPs), which poses a risk of **duplicate repayment postings**. This issue becomes critical as we scale with more LSPs like PayTM and PhonePe initiating repayments through their own Payment Gateways (PGs).
- Additional complexity arises because **UTR (Unique Transaction Reference) numbers are only unique at the bank level**, not globally. Hence, simply using UTR for deduplication is not sufficient and can lead to false positives or missed duplicates

**Solution:**
?**

---

## #158 — NBFC Capturing Additional details post KYC
**Status:** Ready for Tech | **Last edited:** July 11, 2025 12:42 PM

**Problem:**
are we solving?**

Few LSPs integrating with our stack do not capture all the necessary ‘Additional Details’ or ‘declarations’ required by DSP to process the loan. In such cases, LSPs expect the DSP to collect these details directly from the customer.

---

**Solution:**
?**

---

## #159 — Untitled
**Status:** Not started | **Last edited:** July 11, 2025 10:33 AM

**Problem:**
are we solving?**

For DSP lender, finalising the values of additional details and decalarations that we need to take from the customer. 

---

**Solution:**
?**

---

## #160 — [Platform] BRE configurations for approval tasks
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

## #161 — Product note LMS integration with Tally
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

## #162 — [B2B2C] Fixed deposits via partner dashboard
**Status:** Pending Review | **Last edited:** January 8, 2026 4:23 PM

**Problem:**
are we solving?**

---

- Volt is looking to improve partner engagement by helping partners monetise their existing clients better and sell multiple financial products through one platform. Adding Fixed Deposits (FDs) as a product offering allows partners to offer a popular, high-value product along with loans.
- The objective of this initiative is to integrate FD booking and servicing into the existing Volt Partner Dashboard, leveraging Fixxera for the booking journey while providing partners with a unified interface to initiate, track, and manage FD applications.

**Solution:**
?**

---

## #163 — Front loading the MF Fetch step in application
**Status:** Not started | **Last edited:** January 8, 2025 9:00 PM

**Problem:**
are we solving?**

Our current application conversion stand at ~14%, while the industry standard for conversion is closure to 70%. We have a lot of ground to cover in our conversion percentage. 

---

**Solution:**
?**

---

## #164 — [NBFC] DSP Finance Website (Aug25)
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

## #165 — Reduce Phonepe Drop-offs
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

## #166 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #167 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #168 — Delaying getDisbursementInfo API hit after savePle
**Status:** Pending Review | **Last edited:** January 6, 2025 3:50 PM

**Problem:**
are we solving?**

- For the first getDisbursementInfo API call post credit creation we are getting “No data Found” in the response of the getDisbursementInfo API
- Since we run a scheduler of 1 hour of getDisbursementInfo thus it takes another hour to get a valid response from getDisbursementInfo API response (after getting No Data Found in the response first time)

---

**Solution:**
?**

---

## #169 — MFC in-app journey
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

## #170 — Axis bank e-collect API integration for virtual ac
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

## #171 — [Platform] Mandate collection BRE optimisation
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

## #172 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #173 — [Volt LSP] DSP QC rejection handling
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

## #174 — B2B Platform Dashboard v1
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

## #175 — CKYC Upload for DSP
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

## #176 — [Platform LSP] All transactions requirements
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

## #177 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #178 — Shortfall FAQ
**Status:** Not started | **Last edited:** January 21, 2025 8:23 PM

# Shortfall FAQ What is shortfall? Short fall is the when the DP of customer goes below the withdrawn amount. This happens due to Market downfall. LTV SEBI Regulatory LTV As per RBI the Guidelines are the LTV should be 50% DSP Configured LTV we generally keep the LTV 0.45 to keep buffer of 10% for the Market fall There is minimum limit of the Pledging of the 25k

---

## #179 — [LSP] Total outstanding amount correction and over
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

## #180 — [Platform] QC rejection handling
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

## #181 — Yes bank e-collect API integration for virtual acc
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

## #182 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #183 — Volt website revamp
**Status:** In progress | **Last edited:** January 2, 2025 3:15 PM

# Volt website revamp # Why - Poor impression created (customers, hiring, partners) -- gives a stock website + app impression - Absence of adequate trust markers: - Generic trust markers - not impactful - No social proofing - Lender credibility not used to build trust in TOFU - No testament of scale - App ratings (maybe not right now) - Scope to improve education about the product and benefits - Structure content to make it easy to consume - Set up proper website analytics to get insights: GA4, Hotjar - Brand & UI - Typography used: Poppins + Inter since widely used - doesn’t give a unique personality to the brand - Stock images used on the website doesn’t help build trust - gives an impression that the product is not modern, tech savvy, old - Improve targeting user pain points - no clear understanding of the user personas we’re targeting - Very minimal understanding of users motivations, fears, pain points - Increase engagement on the website - interest calculators, motion - Solve for organic SEO ranking - Careers page, values - B2B, B2B2C pages # How do we define success: - Website is able to clear most customer queries and reduce the need to reach out to sales for conversion - Able to convincingly convey benefits, help understand process, address concerns/fears - Able to convey the scale of Volt to visitors and build trust - Build strong credibility about the brand, product and offerings - Confidently use website for external conversations - Increase top of the funnel conversions # Data to get 1. User personas: Who comes to the website and to do what? - Hypothesis to validate - Impact of showing interest rate conversion on the website - [User Persona Research](Volt%20website%20revamp/User%20Persona%20Research%209b08e7ebacfc4da59413f602c8868aa3.md) - User research - Sales team insights - Personas using the website 2. Brand positioning data from founders [Understanding brand (WIP)](Volt%20website%20revamp/Understanding%20brand%20(WIP)%209517bbbaf78d4ff28d86c3db1b31c6bf.md) 3. Market research / Competitor analysis 1. Competitor website stats: similarweb.com 4. Website metrics 1. Depth 1. Scroll depth on key pages (need to setup hotjar) - Set up “scroll_vertical” on GA4 2. Page depth (how many pages users visit) 2. Exit pages/sections - from where do users drop-off from 3. Time spent on different pages/sections 4. Click patterns / heat maps (if available) 5. FAQ’s opened 6. Help button clicked :: queries asked 5. Search queries in loans/LAMF space 6. Interest calculator engagement 7.

---

## #184 — Repayment next step
**Status:** Not started | **Last edited:** January 17, 2025 12:25 PM

# Repayment next step # Loan Repayment System Redesign ### Current Hypotheses 1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected. 2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. ## JTBD problem list ### Job Story 1: Clear Shortfall "When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall." **Current Problems:** - The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest - Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront - Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts ### Job Story 2: Pay Interest "When I need to pay my interest, I want to understand why I need to pay any additional charges" **Current Problems:** - In TATA, users see interest amounts increase in months with additional charges - The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained - Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments - These charges and interest come under monthly dues as a concept ### Job Story 3: Make Principal Repayment "When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision." **Current Problems:** - For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate. - The principal repayment screen doesn't explain that the payment will first go towards interest and charges - Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users. - Users are not aware that principal is being repaid early and isn’t due for 3 years. ### Job Story 4: Understand Payment Structure "When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system." **Current Problems:** - The home

---

## #185 — [Fenix] Lodgement maker bulk approval
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

## #186 — Transactions for MFD API
**Status:** In progress | **Last edited:** January 16, 2025 7:45 PM

# Transactions for MFD API # PRD: Partner-Level Transaction API ## Overview New API endpoint to provide aggregated transaction data at partner level for all customers under a specific partner to address transaction duplication issues. ## Business Context - Need to provide accurate transactions to partner MFDs - Currently experiencing transaction duplication issues - Need consolidated partner-level view instead of customer-level only - Support platforms with multiple partners and customers We recreate our transaction Db with different txn ID every day. Redvision does not have a sophisticated dedupe check , causing transactions to get duplicated multiple time ~avg 2.7 time , highest 28+ count. https://voltmoney.atlassian.net/browse/VSSB-398 This is a major escalations from the redvision, as the daily transaction sync with the with redvision will be unfeasible they requested partner level API to full from our DB. ## API Specification ### Endpoint `GET /v1/partner/platform/transactions` ### Headers | Header | Description | Required | Example | | --- | --- | --- | --- | | X-AppPlatform | Platform identifier | Yes | FUNDS_INDIA | | requestReferenceId | Unique request ID | Yes | b2595c8c-a163-4072 | | Content-Type | Content type | Yes | application/json | ### Request Parameters | Field | Type | Required | Description | Example | | --- | --- | --- | --- | --- | | fromDate | String | Yes | Start date | "2024-01-01" | | toDate | String | Yes | End date | "2024-01-31" | | volt_Partner_id | String | Yes | Partner identifier | "PARTNER123" | | format | String | No | Response format | "JSON" | ### Response Structure | Field | Type | Required | Description | | --- | --- | --- | --- | | status | String | Yes | Response status (SUCCESS/ERROR) | | partnerDetails.partnerId | String | Yes | Unique partner identifier | | partnerDetails.partnerName | String | Yes | Partner name | | partnerDetails.totalCustomers | Number | Yes | Total customers count | | transactions[].transactionId | String | Yes | Unique transaction ID | | transactions[].voltcustomerCode | String | Yes | Customer identifier | | transactions[].description | String | Yes | Transaction description | | transactions[].amount | Number | Yes | Transaction amount | | transactions[].transactionStatus | String | Yes | SETTLED/PENDING_SETTLEMENT | | transactions[].transactionType | String | Yes | CREDIT/DEBIT | | transactions[].settledOn | Number | Yes | Settlement timestamp | |

---

## #187 — [Final] End use capture of transactions
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

## #188 — [Email Template] Decoupling of Lodgement and Agree
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

## #189 — PRD - B2C Referral [Phase-2]
**Status:** In progress | **Last edited:** January 14, 2026 5:28 PM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new us

**Solution:**
?**

---

## #190 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #191 — [CC] Lodgement Enhancement
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

## #192 — [CC] Showcase the reason for freezing on CC
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

## #193 — TCL EOD Status Check Integration
**Status:** In progress | **Last edited:** February 4, 2025 2:21 PM

# TCL EOD Status Check Integration ## 1. Overview Integration of TCL's EOD status check API to prevent transaction processing during EOD window and avoid backdated transactions posting. Sample Adhoc charge posting API and request: ```json https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/adhocCharges with body [ { "Amount": "200", "ChargesSID": "5", "Date": "2025-01-28", "LoanAccountName": "Avinash Goutam", "LoanContractNo": "41211", "Narration": "Stamping Charges", "Type": "charges", "UniqueRecordID": "1881575495221406782", "UserName": "adminiaf" } , { "Amount": "799", "ChargesSID": "3", "Date": "2025-01-28", "LoanAccountName": "Avinash Goutam", "LoanContractNo": "41211", "Narration": "Processing Fee", "Type": "charges", "UniqueRecordID": "2630159110274265629", "UserName": "adminiaf" } ] ``` ## 2. API Details [https://docs.google.com/spreadsheets/d/18RGjvVKQBvT9UHgKA_Vagjy_1b14LA9f8b3dBwAK5Uk/edit?usp=sharing](https://docs.google.com/spreadsheets/d/18RGjvVKQBvT9UHgKA_Vagjy_1b14LA9f8b3dBwAK5Uk/edit?usp=sharing) ### 2.1 Base Information - **API Purpose**: Check EOD process status in TCL LMS - **Endpoint**: `/miles/EodStatus` - **Base URL**: `https://miles-uat-apicast.apps.tclprdservices.tatacapital.com:443/rest/v1.0` - **Method**: POST ### 2.2 Request Parameters ```json { "SOURCE_NAME": "Miles" // Mandatory, String(10) } ``` ### 2.3 Response States 1. EOD Not Started ```json { "retStatus": "SUCCESS", "response": [], "sysErrorMessage": "", "errorMessage": "", "sysErrorCode": "" } ``` 1. EOD In Progress ```json { "retStatus": "SUCCESS", "response": [{ "EODDate": "2024-10-19 00:00:00", "Remarks": "EOD is in Progress" }] } ``` ## 3. Business Rules ### 3.1 API Execution Rules - Start checking EOD status after 7:00 PM daily - Implement polling mechanism with intervals: - Every 15 min till 11:00 PM ### 3.2 Status-based Actions | Status | System Behavior | Next Action | Impact | | --- | --- | --- | --- | | Null/Not Started | Continue normal operations | Use current system date | No impact | | In Progress | Pause charge posting API calls and queue the request | Poll status at defined intervals | Credit opening TAT | | Completed | Resume all operations | Use current date + 1 when posting adhoc charge | No impact | | 400/500 or any other error | Pause charge posting API calls and queue the request | Queue the request and process when we get completed status and if we do not get completed status till 11 PM, then process queued request after 12 AM with current date | Credit opening TAT | ### 3.3 State Machine ```mermaid stateDiagram-v2 [*] --> CheckEOD: After 7 PM CheckEOD --> NotStarted: Status Null CheckEOD --> InProgress: Status In Progress CheckEOD --> Completed: Status Completed NotStarted --> NormalOps: Continue Current Date InProgress --> PauseOps: Queue charge posting APIs PauseOps --> PollingState: Wait 15 min PollingState --> CheckEOD Completed --> NextDayOps: Use Current Date + 1 ``` ##

---

## #194 — [Platform] Handling of below 1 Rs transactions for
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

## #195 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #196 — PhonePe PG Implementation
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

## #197 — Measuring Customer Support Events and 5XX errors
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

## #198 — DSP QC Reject Handling in LSQ
**Status:** In progress | **Last edited:** February 27, 2025 7:48 PM

# DSP QC Reject Handling in LSQ # Custom Activity Configuration: DSP QC Rejection ### Problem Statement Currently, when DSP operations team rejects an applicationBased on Risk/compliance reasons, they need customer to Re attempt some step. - That increases Risk of customer application Abandonment - Customer might not see the message based communication - Sales team don’t have the List of applications in QC reject to reach out to Customer over a call and get them to complete the applications ### Success Metrics 1. **Primary Metrics** - Reduction in application abandonment rate post-QC rejection - Decrease in time to resolution for QC issues - Sales team response time to QC rejections 2. **Secondary Metrics** - Increase in first-time-right applications by understanding the Common QC reject issues ## User Personas & Journey ### 1. DSP Ops Team - Reviews loan applications - Identifies risk/compliance issues - Rejects the application on CC - Provides detailed feedback on CC ### 2. Sales Team - Receives QC rejection notifications - Contacts customers for updates - Guides application completion - Updates activity status ### 3. Customer - borrower - Receives rejection notification - Needs to update application - Requires clear guidance - Expects minimal friction ## 1. Activity Setup in LeadSquared Using LeadSquared's Custom Activities & Scores section: ### 1 Basic Configuration - Activity Display Name: DSP_QC_Rejection - Activity Code: 268 - Score: 0 - Show in Activity List: Yes - Delete Activity: Yes ### 1.1 Activity Setup in LeadSquared ```json { "ActivityEventName": "DSP_QC_Rejection", "Code": "268", "Score": 0, "ShowInActivityList": true, "CanDeleteActivity": true } ``` ![Screenshot 2025-02-21 at 4.00.31 PM.png](DSP%20QC%20Reject%20Handling%20in%20LSQ/Screenshot_2025-02-21_at_4.00.31_PM.png) ### 1.2 Custom Fields 1. **Notes Field** - Display Name: Notes - Schema Name: ActivityEvent_Note - Type: String - Purpose: Capture rejection reasons 2. **Status Field** - Display Name: Status - Schema Name: Status - Type: Dropdown - Options: - Pending Review - Customer Contacted - Update Required - Update Received - Resolved 3. **Owner Field** - Display Name: Owner - Schema Name: Owner - Type: User - Purpose: Track responsibility ### 2.1 API Call for Creating Activity ```json POST https://{host}/v2/ProspectActivity.svc/Create { "RelatedProspectId": "[LEAD_ID]", "ActivityEvent": "268", "ActivityNote": "[QC_REJECTION_NOTES]", "Fields": [ { "SchemaName": "Status", "Value": "Pending" }, { "SchemaName": "Owner", "Value": "[ASSIGNED_SALES_REP]" } ] } ``` ### 2.2 Application Logic 1. When QC team rejects application: - Create activity with rejection details - Set initial status as "Pending" - Assign to original sales owner - Return customer

---

## #199 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #200 — Active customer in LSQ
**Status:** In progress | **Last edited:** February 27, 2025 3:11 PM

# Active customer in LSQ ### **Problem Statement** 1. There is a significant delay in conversion between lead creation and the customer's decision to take a loan. Data shows that **40% of PhonePe customers complete their application more than 30 days after lead creation**. - The current LSQ setup is optimized for leads ready to take a loan immediately after account creation, but not for delayed conversions. 2. We lack a robust mechanism to identify customers returning after an extended period (e.g., 30+ days) to re-fetch data and reconsider taking a loan, which means that sales team is not calling the Leads with eligible limits that registered few weeks ago. 3. The Sales and RM teams often reach out to customers at inconvenient times, such as when they are not actively engaged with their applications or are preoccupied with other tasks. This increases conversion time and creates user frustration. We want to have a sales process similar to that of Policy bazaar, as the customer is visiting the platform they are get sales call. ## Metrics - Sales call to active customers - Conversion rate of active customers vs In-active customers - Cohort long term conversion rate ### **Expected Impact** - Improved loan application conversion rates. - Enhanced efficiency in Sales and RM team outreach. - Reduced user frustration by aligning engagement efforts with customer activity. ### **Proposed Solutions** - Implement a parameter to identify and track customer engagement on the platform. - **Criteria for Active_lead Users**: - A user is considered "Active_lead" if: - They are browsing any section of the Volt platform (Web/App) - They have a session duration exceeding **30 seconds**. - Updates to LSQ on user activity will be triggered: - When a new session starts and is on for more than 30 sec - No more than three **times per day per user due to the API constraints**. - If the User is eligible for LAMF and do not have loan created - **Integration with LSQ** - Send the user activity parameter as a **Customer Platform_Active Timestamp** to LSQ. - LSQ will prioritise and manage leads based on this timestamp, enabling: - Focused outreach to active users. - Support for users stalled at critical stages like Fetch. - Agents will see the Last active time as lead detail and have a view with Last active time as a Column ### **Additional Requirements** - Estimate the

---

## #201 — Product note - DRPS
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

## #202 — B2B2C RM Flows
**Status:** In progress | **Last edited:** February 25, 2025 5:07 PM

# B2B2C RM Flows Problem statements - Agents have no context on the Incoming calls as they only see the Mobile number - There is no place to Use this mobile number to see the details of the MFD calling and past context - If the MFD has a chat with other RM then i can’t see there messages - Disposition forms in the RUNO and Zendesk are not MECE for the need of RMs - Tech Tickets status don’t get auto updated - RM have to remember to follow up with MFDs, they don’t have a workflow requiring it - [tech issues ](B2B2C%20RM%20Flows/tech%20issues%201a5e8d3af13a8016b001f22540049447.md)

---

## #203 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #204 — Shortfall communication enhancement Ignoring accou
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

## #205 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #206 — Pre-fetch flow Optimisation Consolidating PAN flow
**Status:** Done | **Last edited:** February 19, 2026 9:43 AM

**Problem:**
are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

**Solution:**
?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

---

## #207 — Line enhancement Loan renewal BRE
**Status:** Not started | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

1. Line enhancement and loan renewal fees BRE changes
2. Fee and charges verification for fresh application, line enhancement and loan renewal for both lender

**Solution:**
?**

---

## #208 — PAN type update on partner dashboard
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

## #209 — Attribution for Jupiter
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to create a BRE which will allow Jupiter platform to create customer even if customer account exist.

---

**Solution:**
?**

---

## #210 — Bajaj PG
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

## #211 — Foreclosure payment handling (EOD) repayment in fo
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

## #212 — Interest, shortfall, renewal table on partner dash
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

## #213 — LSQ data sync
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

## #214 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #215 — AA integrations - Fetch journey
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

DSP needs a compliant, automated way to fetch users’ demat **stock holdings** via AA for LAS underwriting, without handling other asset classes.

---

**Solution:**
?**

Introduce an **AA Consent & Data module** backed by Finarkein Nerv “dynamic multi‑consent” APIs.

The module will orchestrate: journey creation, consent state management, data fetch, webhook processing, and normalized holdings storage for LAS underwriting.

---

## #216 — Annual Maintenance Charges (AMC)
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

## #217 — Capture foreclosure reasons from customer
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

## #218 — Centralised issue reporting process
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We have multiple source of ticket creation
    - WATI + Phone calls : Issue reported by customer or MFDs to inbound team
    - Email: User reports issue on email, internal team send mail to product or tech team to raise the issue/feature enhancement/new requirement.
    - B2B platform: Issue raised by B2B partners on behalf or their customer
    - Product team: Issues identified by the product team
    - Tech team: Issues identified by the tech team
    - Sales/OPS: Issues reported by customer or MFD at time of sales call or while doing the journey
    - Business/Customer 

**Solution:**
?**

---

## #219 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #220 — Comms config
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Comms config Customer loan renewals ```json { "LOAN_RENEWAL_REMINDER_1ST": { "eventInFiltering": { "customerChannel": [ "B2C", "B2B", "B2B2C" ], "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "loan_renewal_1st_day_of_month_v1", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "loan_renewal_1st_day_of_month_v1" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "loan_renewal_1st_day_of_month_v1" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "contactnumber" ] }, "MAIL": { "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_2ND": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "15th_day_of_loan_expiry_v1", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "15th_day_of_loan_expiry_v1" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "15th_day_of_loan_expiry_v1" }, ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "contactnumber" ] }, "MAIL": { "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_LAST_WEEK_DUE": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "20days_to_last_day_amount_due", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "20days_to_last_day_amount_due" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "20days_to_last_day_amount_due" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "outstanding_amount", "contactnumber" ] }, "MAIL": { "templateId": "d-78f7acdde85248798dfda7f480312e31", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP",

---

## #221 — DSP - Charges Deduction Identification Wrapper API
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

Lending Service Providers (LSPs) receive charges data(in loan summary API) but cannot easily identify which charges will be deducted from the loan disbursal amount (net disbursal) and which will not. The existing API lacks explicit categorisation or clear indication, leading to confusion and incorrect communication to customers about the deduction of charges.

**Solution:**
?

Create a **wrapper API** that:

- Use FinFlux Charges API “Get Account Charge Api”.
    - UAT URL: [https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000000049/charges](https://uat-voltmoney.finfluxtrial.io/fineract-provider/api/v1/revolving-credit-lines/000000049/charges)
- Uses a **configurable mapping** of `chargeIdentifier` and/or `chargeId` to determine if a charge is deducted from disbursal.
- Returns two clean, separate lists:
    - **deductedFromDisbursal**
    - **notDeductedFromDisbursal**
- Provides a clear, consistent API response optimized for LSP consumption.
- Supports easy updates to the mapping without any changes at FinFlux end.

---

## #222 — DSP Bank Account Update and Mandate Re-Registratio
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

## #223 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #224 — Foreclosure repayment - Handle PenalInterestAccrue
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

## #225 — Handle excess amount in foreclosure request [TCL]
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

## #226 — Handle physical mandate cases for BAJAJ
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

## #227 — In app user review [Play store]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We currently do not collect user experience feedback directly at key moments in the app journey, which has led to the following challenges. 

- **Missed Pain Points:** Without timely feedback, we risk missing critical pain points during specific stages of the app journey, such as loan applications, payments, or withdrawals. These missed insights can result in unresolved issues, leading to decreased user satisfaction.
- **Lost Improvement Opportunities:** Journey-based feedback offers real-time insights into what’s working and what needs improvement. Without this feedback, we

**Solution:**
?**

---

## #228 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #229 — Interest feature handling for TCL
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

## #230 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #231 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #232 — MFC fetch in Volt Journey
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

## #233 — Mandate registration post loan
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

## #234 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #235 — Partial lodgement handling - DSP
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

## #236 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #237 — Project Elevate - LMS
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

## #238 — Repayment flow optimisation
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

## #239 — Revocation MIS - TCL customer
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

## #240 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #241 — Setup new and fix existing MIS for lender BFL and
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Setup new and fix existing MIS for lender BFL and TCL

---

**Solution:**
?**

---

## #242 — Shortfall experience optimisation
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

## #243 — TCL Dynamic repayment schedule
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

## #244 — TCL foreclosure API integration
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

## #245 — Volt Apps & Web Multiple Loan Handling - Launching
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

## #246 — Volt Mandate re-registration Post loan
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

## #247 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #248 — Ticketing system for Volt
**Status:** In progress | **Last edited:** February 19, 2025 3:20 PM

# Ticketing system for Volt # **Problem Statement:** Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. Applications successful = With + without assist = Count * Cost Current Support team are facing following challenges Borrower - Long wait times for the agents to get back - Chat support - visibility - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product. - RMs and agents have to provide context in sending the client Between RMs or on Leave - We would have a data on the issues raised by a particular customer or to maintain history of support - If the support request is not OPS or Tech realted then taking followup - High Inbound Traffic :- Agents are move from call to call and saving - Lack of a single source of truth for customer issues. - Inconsistent tracking across calls, WhatsApp, and emails. - Unrecorded issues, especially from phone calls. - No SLA tracking or identification of common problems. **Key Requirements:** - **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket. - **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes. - **Workflow Needs**: - Easy ticket creation and search by phone number. - Visibility into all tickets per customer/issue. - Strong APIs and customizable workflows. - **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database. **Goals:** - Achieve 100% ticketing for all interactions. - Track and measure issue resolution times (SLAs). - Identify bottlenecks and common problems. - Prevent any customer issue from being overlooked. The Workflows that need to be enabled - Grouping of users - Page-nation for the pending and completed application The Filter for the lead stage to be added Add filters in the pending application User stories - Customer will call us - customer is routed to a agent - How is this routing setup? - Agent takes notes on the call - Dispostion

---

## #249 — DSP Handling Sell-Off Dependencies
**Status:** Not started | **Last edited:** February 18, 2025 2:22 PM

**Problem:**
are we solving?**

The user can request to initiate a voluntary sell-off of his collateral to pay their interest or total outstanding or principle amounts. 

---

**Solution:**
?**

---

## #250 — B2B2C DSP ops handling
**Status:** Not started | **Last edited:** February 17, 2025 12:47 PM

# B2B2C DSP ops handling Problems 1. Sales team raise a ticket to Volt ops , Volt ops send the cases to DSP over E-Mail. 2. Sales team do select the lender 3. What is the FRT form the DSP ops 4. What is the TAT end to end. 5. Volt ops use Zendesk and DSP ops use ZOHO 6.

---

## #251 — Post loan Status APIs for MFD SaaS Partner Platfor
**Status:** Done | **Last edited:** February 14, 2025 12:59 PM

# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal # Product Requirements Document (PRD) [API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md) ## **Project Title:** **Development of External APIs for MFD Dashboard Integration** --- ## **1. Introduction** This document outlines the requirements for developing a set of External APIs intended for MFD platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners --- ## **2. Objective** To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base. --- ## **3. Target Audience** - **Primary Users:** - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards. - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data. - **Stakeholders:** - **Product Management Team** - **Development Team** - QA - **MFD SAAS Partners** --- ## **4. Scope** ### **In-Scope:** - Development of four External APIs: 1. **Get Active Customers** 2. **Get Shortfall Details** 3. **Get Interest Due Details** 4. **Get Renewal Details** - Documentation and specifications for each API. - Implementation of business logic within each API. - Security measures for data protection. ### **Out-of-Scope:** - Development of UI components for MFD dashboards. - Integration of common headers and authentication mechanisms (handled separately). --- ## **5. API Specifications** ### **5.1. Get Active Customers** ### **Endpoint:** ``` GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber} ``` ### **Description:** Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively. ### **Parameters:** - **Path Parameters:** - `partnerAccountId` (string, **required**): Unique identifier for the partner account. - **Query Parameters:** - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve. ### **Response Payload:** ```json { "activeCustomerDetails": [ { "mobileNumber": "+919876501234", "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "email": "dummy@voltmoney.in", "pan": "AUWPA7175L", "dob": "30-03-1988", "creditDetails": { "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "creditType": "OVERDRAFT", "lenderCreditId": "9911725722", "lenderName": "Bajaj", "totalCreditAmount": 332300, "availableCreditAmount": 282300, "principalOutStandingAmount": 50000, "currentApplicableInterestRate": 9.95, "pledgedPortfolioAmount": 738723, "overUtilizationAmount": 0, "chargesDueAmount":

---

## #252 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #253 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #254 — DSP website revamp
**Status:** Not started | **Last edited:** February 12, 2025 4:29 PM

# DSP website revamp # Problems to solve 1. “Make the website a public website” 1. Make it accessible on Google and other search engines (already visible through Bing) 2. Brand impression: currently looks like a placeholder website 3. Improve “About DSP” section 1. More prominently referencing to the DSP group - Review other DSP children websites 4. Product offerings 1. Structured lending 2. LAMF - understand what’s missing 3. LAS - show coming soon? 5. Regulatory 1. Link RBI’s sachet portal 2. Prominently display name, email, contact number of grievance redressal officer on website 3. Prominently display details of COO - Principal Nodal officer on website 6. Minor fixes 1. Update address - 11th floor instead of 10th floor 2. Update CIN 3. Operating timings: customer care 4. Update partners list 5. Benefits → “RBI registered” needs to come with a disclaimer - refer to flexiloans footer 7. Logo finalisation ![image.png](DSP%20website%20revamp/image.png) # Solution space - [ ] Understand scope - [ ] Talk to priya - What is “headers” - Pankaj notes - [ ] Get feedback shared by Pankaj Thapar (policy consultant) - [ ] New website mood board - how much brand referencing is needed? | Problem | Proposed solution | | --- | --- | | 1.a | - Submit site on Google Search Console - Make sitemap.xml - Make robots.txt | | | | WEBSITE LAYOUT ### Header - Partners - Products - About ### Hero - Title - “Loans against securities” - “digital first approach” - CTA ### About Organisation stats - Money disbursed, Loans given, no. of partner tie ups - Since 160+ years ![image.png](DSP%20website%20revamp/image%201.png) ### Our products - LAMF - LAS - Structured lending ### LAMF features ### How it works ### Footer ## Additions - FAQs - About us → our team

---

## #255 — [Platform] Enabling alternate mandate registration
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

## #256 — TATA PG dulplicate refNo validations
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

## #257 — Attribution for Volt applications
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

## #258 — MFC Pledge error handling - V1
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

## #259 — Reducing Limit on DSP from 25K
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

## #260 — Volt LOS journey optimisations
**Status:** In progress | **Last edited:** December 5, 2024 10:50 AM

**Problem:**
are we solving?**

1. Journey completion %
2. Reduce customer support queries
3. Reduce 
4. Reduce loan application journey time
    1. Reduce number of stages
    2. Reduce time spent per screen/stage of journey, 
5. Clear and easy to understand screens: info, warnings, hierarchy.
6. Maintain high user psych till journey completion
    1. Easy education.
    2. High motivation.
    3. Trust and comfort.
    4. Delight.
7. User has to drop-off and come back to refresh portfolio - bad UX, 0 education

**Solution:**
?**

---

## #261 — Update user details (for TCL, BFL, DSP)
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

## #262 — [Platform] Mandate presentation request optimisati
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

## #263 — [B2B2C] Improving lead quality in partner journey
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

## #264 — Skip Email verification
**Status:** Not started | **Last edited:** December 29, 2025 11:59 AM

**Problem:**
are we solving?**

Email verification is currently mandatory for loan application creation. However, we’re seeing around 15% **user drop-off** at this step. To reduce friction, we propose letting users **choose their preferred primary communication channel — SMS or Email** — and **skip email verification** for those who select SMS. This allows users who rely on SMS to continue without being blocked by email OTP verification.

---

**Solution:**
?**

---

## #265 — [Volt LSP] Pre fill bank account number from MFC d
**Status:** In progress | **Last edited:** December 27, 2024 10:40 AM

**Problem:**
are we solving?**

Customers on the bank verification step are currently required to enter their complete Bank account number and IFSC code to verify their bank account this is a pain for customers. 

[https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99](https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99)

---

**Solution:**
?**

---

## #266 — Show accrued interest on UI
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

## #267 — [Platform] Liveliness check
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

## #268 — Mobile email dedupe check in case on in-progress m
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

## #269 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #270 — [Volt LSP] Liveliness check
**Status:** Not started | **Last edited:** December 23, 2024 8:08 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #271 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #272 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #273 — LAS LOS
**Status:** Not started | **Last edited:** December 21, 2025 12:48 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #274 — [Platform] Risk report
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

## #275 — [LSP] DSP VA
**Status:** Not started | **Last edited:** December 2, 2024 8:10 PM

# [LSP] DSP VA - What amount to show? - If we are showing only that then how are we expecting user to make the repayment of interest/prinicpal - Can be done like TCL? - Can we get the outstanding amount changed as total outstanding - BFL - DSP - TCL - Can we show the breakdown - Apportionment logic should be shown if we showing only one amount & only one bank account? - Will have to show break down? - Pull up numbers for bank transfer and importance of showing it expanded

---

## #276 — Figma file organisation
**Status:** Not started | **Last edited:** December 2, 2024 3:59 PM

**Problem:**
are we solving?**

- Searching for updated files of features and different stages of the journey
- Get visibility on how each stage is handled for different lender
- Easy visibility on version history, compliance updates etc. done in the past - need to view in one place
- Allow storing secondary flows like: error handling, drop-off flows etc

---

## #277 — User engagement on the LSQ
**Status:** Not started | **Last edited:** December 12, 2024 5:55 PM

# User engagement on the LSQ Currently issues # Ticketing System Requirements & Workflow Chief Product Officer Document | December 2024 ## Executive Summary Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency. ## Current Pain Points Analysis 1. Issue Resolution Tracking - No unified system to track resolution progress - Limited visibility into resolution time frames - Inability to measure team performance effectively 2. Organizational Context - Disconnected systems leading to fragmented customer context - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos - Limited cross-functional visibility 3. Support Coverage - Backup handling inefficiencies - Lack of structured handover processes - No clear escalation matrices 4. Performance Metrics - Missing TAT (Turn Around Time) tracking at issue level - No trend analysis capabilities - Unable to identify recurring issues and root causes ## Core Requirements ### Ticket Creation & Management 1. Mandatory Ticket Creation - 100% ticket creation for all customer interactions - Channels: Phone calls, WhatsApp, Email - Required fields: Partner ID, Issue Category, Description - Clear resolution confirmation before ticket closure 2. Channel-Specific Workflows - MFD Channel specific routing rules - Direct customer support workflow - B2B partner interface requirements 3. SLA Management - Channel-specific SLA definitions - Real-time SLA tracking - Escalation workflows - Performance dashboards ### User Management & Access Control 1. Internal Users - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support) - Support Channel Team (10 agents) - Sales Team (7 members) - Ops and Tech on-call teams - Admin users 2. External Users - Direct MFDs - Platform MFDs - B2C customers - B2B platform partners ### Integration Requirements 1. Communication Systems - Exotel for call routing - RUNO for call visibility - Periskope and WATI for WhatsApp - Email integration 2. Internal Systems - Retool for DB state visibility - LSQ CRM - Slack for internal communications ## Key Features 1. Unified Dashboard - Single view of customer interactions - Real-time status tracking - SLA monitoring - Team performance metrics 2. Analytics & Reporting - Issue frequency analysis - Resolution time tracking - Team performance metrics - Channel-wise analysis - Custom report generation 3. Workflow Automation - Automatic

---

## #278 — Volt DLS 2 0
**Status:** In progress | **Last edited:** December 12, 2024 1:59 PM

# Volt DLS 2.0 # Why —————————————————— - Reduce front end effort to create new features and products - Reduce effort of maintaining multiple DLS - Faster design + dev time: Faster decision making and alignment on design - Significantly higher consistency - Easier onboarding for new joinees <aside> 🎯 **Goal:** To create a singular org level DLS that helps build all our products: Core, web, dashboards, command center, etc. </aside> # What —————————————————— ### Process 1. Brand positioning doc - : *in progress* [Brand Positioning Doc](Volt%20DLS%202%200/Brand%20Positioning%20Doc%207b616b64989b4dd68419a624c15997eb.md) 2. User research: *in progress* 3. Market research/Competitor analysis - benchmarking [Market research](Volt%20DLS%202%200/Market%20research%20856a208a18e54d899487aa1703345e80.md) 4. Heuristic evaluation of current design 5. Finalise tokens 1. Keyword mapping 2. Options 1. UI language 2. Typography scale + tokens 3. Color scale + tokens 4. Components In-depth implementation [WIP]: [https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing) ## Scope [Scope](Volt%20DLS%202%200/Scope%20ad8083b8d6fd44fa8e0d2d347d7c5fe0.md) **Tokenization representation** - L3: Mapped - L2: Alias - L1: Primitives [https://thedesignsystem.guide/design-tokens](https://thedesignsystem.guide/design-tokens) [https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676) ![image.png](Volt%20DLS%202%200/image.png) ## ⛳️ Typography scale - Ability to update Heading font style separately than Body - Allow having capitalisation in subheaders, tags etc - Allow using singular token for a style which auto switches between mobile (14px), web, MFD, DSP (16px), command center (12px) ### **How →** - Primitives: xs, sm, md, lg… ,etc. - Alias (Text styles) - Tokens: H1, H2, H3, H4… B1, B2, B3, B4… - Theme: Core-mobile, Core-web, DSP-mobile, DSP-web ## ⛳️ Color scale - Allow switching themes for light and dark mode - Allow switching primary, secondary, success, etc colors for different products/brands/SDKs - Allow modifying individual component level colors. Eg: borders, CTAs, headings, secondary text, disabled, etc ### **How (WIP) →** - Primitives: blue (50, 100, 200…900), turquoise (50, 100, 200… 900)… red (50, 100… 900) - Alias - Primary (50, 100… 900), Secondary (50, 100… 900), Success (50, 100… 900) - Theme: Core, DSP - Mapped - Types: - Text (primary, secondary, action, disabled, success, warning…) - Surface (background, primary, secondary, info, action…) - Border (primary, secondary, warning, error…) - Icon (primary, action, error…) - Theme: Light, Dark ## ⛳️ Component level - Allow switching component styles (corner radius, padding, color…etc.) for different use-cases: Core, DSP, dashboards, command center etc. ### Priority components: 1. Top header bars 2. Buttons 3. Bottom sheet 4. Input fields 5. Form logic + behaviour 6. Bottom nav bars 7. Toasts, notification 8. Tabs - Refer to small case filter screen + chips + tabs inside MF selection 9.

---

## #279 — Un-pledging bug fixes & UI optimisation
**Status:** In progress | **Last edited:** December 11, 2024 6:31 PM

**Problem:**
are we solving?**

1. For the users who are making an un-pledging request in our app, when there is auto-adjust of limit according to credit allowance, 
    - Then users are just shown the limit of the fund un-pledged, because of which it is not clear to the user that only partial funds are selected for un-pledging
    - The message “We have accommodated the last fund as per credit allowance” which we show in this case might not be very clear for the user who is un-pledging funds for the first time. They may have questions like -
        - What does credit allowance exactly mean?
        - How

**Solution:**
?**

---

## #280 — PRD - B2C Referral [Phase-1]
**Status:** In progress | **Last edited:** December 10, 2025 8:08 AM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt does not have any mechanism to leverage its existing loan users base who has experienced the value of Volt Money LAMF product for new user acquisitions.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new users to borrow LAMF from Volt as a trusted brand and limited period reward offers will assist i

**Solution:**
?**

---

## #281 — Single drawdown Term Loan LMS Requirements
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

## #282 — [Tata Neu] Bottom sheet to nudge user to withdraw
**Status:** Not started | **Last edited:** August 6, 2024 5:19 PM

**Problem:**
are we solving?**

Post completion of application, users currently land on the dashboard page. The user now has multiple actions that they can perform which can distract them from the primary use case of customers withdrawing from their credit limit. 

Problem statement is to nudge user to place a withdrawal request as soon as the customer lands on the dashboard page.

---

**Solution:**
?**

---

## #283 — Cashfree PG integration
**Status:** Pending Review | **Last edited:** August 5, 2025 3:56 PM

**Problem:**
are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

**Solution:**
?**

---

## #284 — SL updation & additional limit calculation optimis
**Status:** On Hold | **Last edited:** August 27, 2024 5:20 PM

**Problem:**
are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

**Solution:**
?**

---

## #285 — [Platform] RTA portfolio API integration
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

## #286 — [DSP] Dues collection comms
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

## #287 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #288 — VKYC for DSP and Co-Lending
**Status:** In progress | **Last edited:** August 19, 2025 7:01 PM

# VKYC for DSP and Co-Lending [LSP Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/LSP%20Focused%20VKYC%20Journey%20Alignment%20238e8d3af13a80cd80c6f64c76ab3aed.md) [Volt Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/Volt%20Focused%20VKYC%20Journey%20Alignment%20216e8d3af13a801bbba2eb686074c82b.csv) [VKYC: Vendor Evaluation](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Vendor%20Evaluation%20217e8d3af13a80dfb53bed7d04c1e7f3.md) [VKYC: Regulatory Understanding](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Regulatory%20Understanding%20217e8d3af13a809f88e9f173d73f3d5a.md) [Discussion with Rohan (Groww)](VKYC%20for%20DSP%20and%20Co-Lending/Discussion%20with%20Rohan%20(Groww)%20254e8d3af13a8085a070ce018cec0f02.md)

---

## #289 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #290 — [DSP] KYC v2 (including CKYC)
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

## #291 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #292 — B2B Zype integration webhook
**Status:** Not started | **Last edited:** August 12, 2024 8:25 PM

**Problem:**
are we solving?**

In addition to current webhooks, create another webhook for partner platforms to get an understanding of when was withdrawal initiated by a user on their platform. 

**Note:** While this requirement was raised by zype this webhook will be created for the complete SDK, any partner can choose to consume it. 

---

**Solution:**
?**

---

## #293 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #294 — Lien removal buffer enhancement (Note)
**Status:** Not started | **Last edited:** August 10, 2024 3:51 PM

# Lien removal buffer enhancement (Note) [Bajaj buffer handling for lien removal](https://app.notion.com/p/Bajaj-buffer-handling-for-lien-removal-90fa191a67ec4f38b2bff1cfe6d99a98?pvs=21) For Bajaj, we had placed a buffer of 5% on total outstanding when users raise collateral removal requests to handle NAV changes. Collateral removal requests take 1-2 working days to be processed by the lender and hence to ensure requests are not cancelled this buffer is maintained. Due to high volatility in markets our requests are still getting rejected despite the 5% buffer. We need to solve for the cancellations. One proposed method by the business team is to increase the buffer to 10% however that impacts customer experience. Need solutioning for the same.

---

## #295 — Product note NSDL PAN Verification
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

## #296 — PRD Disbursement Method Selection Logic (BRE Optim
**Status:** Not started | **Last edited:** April 7, 2026 11:53 AM

# PRD: Disbursement Method Selection Logic (BRE Optimization) --- # **1. Problem Statement** Currently, payout method selection (IMPS / NEFT / RTGS) is not dynamically optimized based on: - Disbursement sequence (1st vs subsequent) - Loan type (co-lending vs non co-lending) - Ticket size - Sourcing channel (e.g., CRED) This leads to: - Suboptimal payout routing - Higher costs and delays - Lack of configurability at product / contract / channel level --- ## **2. Objective** Enable a rule-based engine (BRE) to dynamically select payout method based on: - Disbursement sequence - Loan type - Amount slab - Sourcing channel --- ## **3. Scope** ### **Dimensions for Rule Evaluation** 1. **Contract type** - Co-lending - Non co-lending 2. **Sourcing Channel** - Volt - CRED (override rules) 3. **Nth Disbursement** - 1st - Subsequent 4. **Amount Slabs** - < 2 lakhs - 2–5 lakhs - 5 lakhs --- ## **4. Business Rules** ### **4.1 Co-lending Loans** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | NEFT | NEFT | RTGS | | **Subsequent** | NEFT | RTGS | RTGS | --- ### **4.2 Non Co-lending Loans** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | IMPS | IMPS | RTGS | | **Subsequent** | NEFT | RTGS | RTGS | --- ### **4.3 Sourcing Channel: CRED** | Disbursement | < 2L | 2L–5L | > 5L | | --- | --- | --- | --- | | **1st** | IMPS | IMPS | RTGS | | **Subsequent** | IMPS | RTGS | RTGS | **Note:** - These rules override both co-lending and non co-lending logic when sourcing channel = CRED --- ## **5. Rule Priority Logic** Order of evaluation: 1. **Sourcing Channel Override (Highest Priority)** 2. **Contract Type (Co-lending / Non co-lending)** 3. **Nth Disbursement** 4. **Amount Slab** --- ## **6. Configurability Requirements** - Rules should be configurable at: - Product level (for future requirements) - Contract level - Sourcing channel level - Ability to: - Add/edit slabs - Change payout method mapping - Introduce new channels without code changes --- ## **8. Success Metrics** - Reduction in payout failures - Reduction in payout cost per transaction - Improvement in disbursement TAT - % of transactions routed via optimal rail ---

---

## #297 — [Platform] Validation to Stop Un-pledging, closure
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

## #298 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #299 — Amplitude issues
**Status:** Not started | **Last edited:** April 4, 2024 2:09 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #300 — Bajaj KYC Pod Requirements
**Status:** Not started | **Last edited:** April 4, 2024 1:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #301 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #302 — NSDL PAN integration
**Status:** Not started | **Last edited:** April 29, 2026 5:11 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #303 — Account opening STP optimisations
**Status:** Pending Review | **Last edited:** April 28, 2025 3:57 PM

**Problem:**
are we solving?**

- Approximately 17% of account opening journeys are currently diverted to non-STP paths, resulting in increased operational load on DSP Ops and keeping the customer blocked
- The primary driver of non-STP cases is a failure in the father’s name validation check, which comprises two sub-checks:
    - The match score between the father's name (captured from additional customer details) and the father’s name from Digio_KYC must exceed 80%.
    - The match score between the father's name and the customer's own name must remain below 90%.

---

**Solution:**
?**

---

## #304 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #305 — VKYC Integration PRD
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

## #306 — Product Note – DRPS (Final Version – Unified Forma
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

## #307 — CKYC Comms for Regulatory Compliance
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

## #308 — B2B2C call incoming reduction
**Status:** In progress | **Last edited:** April 17, 2025 11:41 AM

# B2B2C call incoming reduction [Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md) [](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md) # Detailed Breakdown of Customer Call Issues ## Loan Application Issues - **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval. - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times. - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."* - The withdrawal interface appears to lack clear instructions for first-time users. - **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process. - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."* - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs. - **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations. - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."* - The fee structure appears to be disclosed incompletely during the application process. - **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements. - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."* - The eligibility criteria seem inconsistently communicated across different channels. - **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process. - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."* - These timeouts appear to occur most frequently during document upload or verification steps. Payment Processing Issues - **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments. - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."* - These delays severely

---

## #309 — PRD MFC Revised Flow
**Status:** Not started | **Last edited:** April 14, 2026 1:03 PM

**In scope:**
- 
    - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including::
        - Partners who have directly integrated with MFC  fetch flow (eg-Paytm)
        - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter)
        - Partners who are using Volt fetch journey

# PRD: MFC Revised Flow ## **Background and Context** - - Since MFC is going to deprecate the MFC fetch apis and moving to SDK based flow for fetching (concerns from AMFI around fintech platforms accessing investor data freely w/o explicit customer consent.) - This change is expected to go live by 31st January - Since all Volt channel flows (B2B,B2C & B2B2C) as well as LSP flows will be impacted by this change, figuring out how to tackle this transition to esnure business continuity in the near and long terms is critical --- ## **1. Problem scope** ### In scope - - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including:: - Partners who have directly integrated with MFC fetch flow (eg-Paytm) - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter) - Partners who are using Volt fetch journey ### Out of scope - N~~ot covered as part of current scope:~~ - ~~Loan journey changes ‘post fetch’ for Volt channels~~ - ~~B2C website journey changes wrt MFC SD~~K - While the MFC SDK flow implementation is currently suboptimal from tech/ UX POV, improving it by working with the MFC team is not feasible given our tight deadline. --- ## **2. Success Criteria** - - Overall fund fetch SR & first time SR - Overall Fetch TAT - MFC SDK flow SR & TAT - MFC SDK & RTA flow stability /uptime ## **3. Solution Scope** ### [Detailed solution /Journey](https://whimsical.com/internal-mfc-fetch-updated-flow-copy-FDDhzqEJNzTbNnkUCW73b5) ### 1. Entry point (Volt/LSP channels) Volt B2C - Android/IOS app/Partner app: DSP SDK will be triggered on on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen ![Screenshot 2026-02-08 at 2.51.52 PM.png](PRD%20MFC%20Revised%20Flow/Screenshot_2026-02-08_at_2.51.52_PM.png) - ‘Sign in’ entry point on Website : DSP SDK will be triggered on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen in the web app - Check eligibility’ entry point on VoltWebsite: DSP SDK will be triggered on submitting ‘PAN & mob no’ screen & will open in an iframe Volt B2B2C/B2B partners - Partners fetching in own UI:The ‘DSP SDK’ flow is triggered from the partner UI - Partners using Volt UI for fetching: Flows will be same as that mentioned under ‘B2C’ section LSP - The ‘DSP SDK’ flow is triggered from the partner UI ### 2.User

---

## #310 — KYC & Mandate Workflow PRD
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

## #311 — Admin tool migration to Appsmith
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

## #312 — CKYC Internal Report
**Status:** Not started | **Last edited:** April 10, 2025 2:50 PM

**Problem:**
are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database for customer KYC verification. Currently, our team lacks visibility into the performance metrics of CKYC application submissions, including success rates, failure reasons, and backlog status.

There is a need for comprehensive monitoring and reporting on CKYC applications to:

1. Track submission success rates
2. Identify common failure reasons
3. Monitor backlogs
4. Analyze trends in application processing
5. Provide actionable insights for proces

**Solution:**
?**

The solution is to develop comprehensive dashboards that provide visibility into CKYC application metrics. These dashboards will track submissions, success rates, failure reasons, and backlogs.

---

## #313 — VA Repayment Handling [Volt LMS]
**Status:** Not started | **Last edited:** April 10, 2025 10:50 AM

**Problem:**
are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

**Solution:**
?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

---

## #314 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #315 — PhonePe requirements
**Status:** Done | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #316 — UPI Autopay
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

## #317 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #318 — B2B Theme issues
**Status:** Not started | **Last edited:** Unknown

# B2B Theme issues Charter: Design Initiatives ![image.png](B2B%20Theme%20issues/image.png) ![image.png](B2B%20Theme%20issues/image%201.png) ![image.png](B2B%20Theme%20issues/image%202.png) ![image.png](B2B%20Theme%20issues/image%203.png) Screen recording link: https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1184224081308?sessionReplayId=128b9366-93bd-4630-9872-8f471fdcc59a/1749276669544&sessionStartTime=1749276669543 1. NEED HELP button is not themed properly, Primary Back ground surface color is not looking good. 2. Home icon is blue when it should be in primary color. 3. Profile icon color is also blue? 4. Updating benefits for you section icons 5. Can we check the redendering of font in SDKs Why is Popping in serif? 6. Primary button color changes when user comes to increase limit screen.

---

## #319 — Compliance changes in loan offer screen
**Status:** Ready for kickoff | **Last edited:** Unknown

# Compliance changes in loan offer screen Charter: LOS Pod Priority: P0 # Context Have to make the following changes on the loan offer page, this will be specific for DSP: 1. Remove (excl. GST) from One time charges. 2. Add another line item in the One time charges collapse menu. Add this below the "Processing fees" item; "GST at 18%" and show the value. 3. Have to include a disclaimer that "Account creation/withdrawals are subject to lender approval" # Process # Figma [https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system)

---

## #320 — UX Writing for Indian Fintech Users (Volt) – Resea
**Status:** Unknown | **Last edited:** Unknown

# UX Writing for Indian Fintech Users (Volt) – Research & Guidelines # Introduction Designing a UX writing system requires a deep understanding of **local users**, **financial regulations**, and **effective copy practices**. Every label, message, and CTA must inspire confidence and clarity, since <aside> 💡 > *Fintech content design and UX writing is all about building user trust, and it couldn’t matter more when we’re dealing with people’s money.* https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=Fintech%20content%20design%20and%20UX,we%E2%80%99re%20dealing%20with%20people%E2%80%99s%20money > </aside> ## Understanding the Indian Fintech User ### **Trust is paramount** Indian users, especially first-time investors and borrowers, tend to be cautious with new financial services. <aside> 💡 A McKinsey report found that *trust is the primary factor influencing customer adoption and engagement with fintech services* [thence.co](https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=User%20confidence%20is%20the%20degree,and%20engagement%20with%20fintech%20services) </aside> Users need to feel their money and data are safe. UX copy should therefore reassure at every step (e.g. using phrases like “securely powered by XYZ bank” or highlighting RBI oversight) to strengthen this trust foundation. ### **Broad, diverse audience** Volt’s target users include salaried professionals investing in mutual funds, stocks, insurance, bonds, etc. Many are financially savvy to an extent, but there’s a **wide range of literacy** Some may be first-time investors from Tier-2 cities (as seen with apps like Groww), while others are seasoned market participants. Copy must hit a sweet spot where **both novices and experts can understand it easily** <aside> 💡 As one UX guide advises, F*intech UX should prioritize clear, simple language that can be easily understood by both newbies and experts alike* https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=Problem%3A%20The%20financial%20language%20can,to%20understand%20for%20many%20users </aside> This means avoiding heavy jargon and explaining necessary terms in plain language. For example, instead of “lien marking your mutual fund units,” Volt’s app explains it as *“mark your mutual funds as a security with a trusted lender”* immediately clarifying the action. ### Friendly, guiding tone A friendly tone humanizes complex financial tasks – it’s like having a helpful friend explain things rather than a formal banker. However, the tone should also reflect **professionalism** to build credibility; a balance of *professional yet approachable* works well, as Razorpay’s content team describes: their fintech UX writing maintains a *“consistent tone – professional yet approachable”* to serve users dealing with high-stakes transactions ### Attention span and mobile behaviour Remember that Indian users predominantly access fintech services on mobile (Volt is **mobile-first**, as noted). Mobile users skim and scan due to small screens and on-the-go usage. Studies show people read only ~20–28% of text on

---

## #321 — Frontend UI fixes [small]
**Status:** In progress | **Last edited:** Unknown

# Frontend UI fixes [small] Charter: Design Initiatives # Context While watching screen recording i have been noticing small UI frontend fixes that need to be done. List is added below with screenshots. Session recording ID and User ID # Issues ### Mobile number icon **Issue**: There is an unecessary fill on the mobile icon **Fix** remove the fill. **Account id**: 27028d22-2807-428c-9ffa-73e584decd09 **Session recording id:** https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1320386903165?sessionReplayId=34b38273-eb63-45d7-955e-25cbe0d1e8ca/1756790681555&sessionStartTime=1756790681555 ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image.png) ### Surface page color on B2B theme looks very off for many partners - Can we change the surface page to Fill primary? ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%201.png) ### Wrong logo I have seen we are using the wrong logo for DSP Finance in many of our communications. ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%202.png) ### Avg time on Anchor page is - 10s ### Time take to get OTP is 8-9s for MFC fetch # Figma

---

## #322 — Enhance limit Research
**Status:** Unknown | **Last edited:** Unknown

# Enhance limit Research ### Objective 1. **User Motivation:** Why do people enhance their limit? 2. **Mental Models** How do they currently think about credit lines? - Currently our users think about credit line like a personal loan, They only choose increase their credit limit if they are in need. - What we can work towards is building the mindset like a credit card where increased credit limit is something people go for even when they don’t feel the need for it. - Folks tried to 3. **Context of Use** When do they increase limit? - After a withdrawal (they see low balance) - Utilisation > 70% - If they see the value of their MF has increased. . . 4. **Flow Drop Offs** Why do users abandon this? - Users who dropped out usually didn’t get the limit they wanted - They also were ineligible for the loan since there is a 10K limit Unclear next steps. Lack of feedback Screen fatigue 5. **Purpose & Value** Why does this feature matter to users? > It’s a fast, low-effort way to access more cash without applying for a new loan. KYC, Mandate and Agreement not required (If new total limit is below SL) > --- ### Feedback from users - No one complained of any difficulty, lack of information for dropping off. - When asked “What’s one thing stopping you from increasing your limit right now?” - The answer always is they don’t have the need for it. - Minimum 10K being the reason for drop-off. --- ### Segments of Users and Questionnaire 1. **Repeat Users (Used Top-Up More Than Once- Ideal Users)** - Why did you “Enhance Limit”? - What made you come back and do it again? - How easy or difficult was it to find the increase limit option? - Was anything unclear or unexpected in your experience? - Hindi - Aapne pehli baar limit enhance kyun kiya tha? - Aapne phir se kyun kiya? - Pura process aapko kaisa laga — easy ya confusing? - Koi ek step jo aapko helpful ya clear laga? - Aapko paise milne mein kitna time laga tha? - Kya koi cheez aisi thi jo alag thi ya samajh nahi aayi? - Aapko is process pe trust kyun hua? - Aapne jo extra limit mili uska use kaha kiya? - Kya kuch aisa hai jo aur better banaya ja sakta hai?

---

## #323 — Line enhancement nudge
**Status:** Ready for kickoff | **Last edited:** Unknown

# Line enhancement nudge Charter: LMS Pod Priority: P0 # Context [Increase Top-up TOFU & conversion [TCL & DSP]](../PRDs/PRDs/Increase%20Top-up%20TOFU%20&%20conversion%20%5BTCL%20&%20DSP%5D%20203e8d3af13a80ba82aeef50d440f823.md) # Process - [x] Understand scope [Enhance limit Research](Line%20enhancement%20nudge/Enhance%20limit%20Research%2020ae8d3af13a8010a645c3a79ab76e8e.md) - [ ] Benchmarking - [ ] Messaging - [ ] Illustration - [ ] Concept - [ ] Touchpoints - [ ] Messaging - [ ] Design # Figma

---

## #324 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #325 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #326 — Mandate update for better conversion
**Status:** Not started | **Last edited:** Unknown

# Mandate update for better conversion Charter: NBFC Pod Priority: P1 # Context Need to work through mandate flows all three and improve conversion rates for the same. This is for the DSP DSK # Process - [x] Understand mandate processes and types - [ ] Benchmarking mandate flows from others - [ ] Numbers on current conversion rates --- - [ ] Understanding gaps in the current flows - [ ] Flow exploration and alignment - [ ] Wireframes - [ ] Design # Figma

---

## #327 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #328 — Flow charts
**Status:** Unknown | **Last edited:** Unknown

# Flow charts Certainly! Below is the visualization of the user journey map provided, represented in PlantUML diagrams. Due to the complexity and length of the entire journey, I've divided the visualization into sections corresponding to each main phase of the user journey. Each section includes the PlantUML code for the activity diagram, which you can use to generate the diagrams. --- ## **1. User Acquisition and Onboarding** ### **1.1. Launching the App and User Signup** ``` @startuml start partition "User (FE)" { :Launch App; :View Signup Page; if (Click T&C or Privacy Policy?) then (Yes) :Click T&C or Privacy Policy; :View T&C or Privacy Policy; endif :Edit Phone Number; :Navigate to OTP Page; } partition "Backend (BE)" { :Trigger OTP; } partition "User (FE)" { repeat :Enter OTP; :Submit OTP; partition "Backend (BE)" { :Verify OTP; if (OTP Valid?) then (No) :OTP Invalid; endif } if (OTP Valid?) then (No) :Display Error Message; :Resend OTP?; if (Resend OTP?) then (Yes) partition "Backend (BE)" { :Trigger OTP; } endif endif repeat while (OTP Invalid) :Complete Signup; :View Verify Email Page; if (Verify Email with Google?) then (Yes) :Verify Email with Google; else :Verify Email with Other Method; :View Enter Email Page; :Enter Email Address; endif :Email Verification Result; } partition "Backend (BE)" { :Create User Context; :Update User Email; } stop @enduml ``` --- ## **2. Eligibility and Limit Check** ### **2.1. PAN Verification and Eligibility Check** ``` @startuml start partition "User (FE)" { :Enter PAN; :Verify PAN; :PAN Verification Result; if (PAN Verification Successful?) then (Yes) :Confirm PAN Details; else :Edit PAN Details; :Resubmit PAN; endif } partition "Backend (BE)" { :Initiate PAN Verification; :Complete PAN Verification; if (PAN Verification Failed?) then (Yes) :PAN Verification Failed; endif } partition "User (FE)" { :Trigger Eligibility Check; :Eligibility Check Result; if (Eligible?) then (Yes) :Proceed to Next Step; else :Application Under Review or Rejected; stop endif } partition "Backend (BE)" { :Create Credit Application; :Receive Credit Approval Request; :LAN Generation Successful?; if (LAN Generation Failed?) then (Yes) :LAN Generation Failed; stop endif } stop @enduml ``` --- ## **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** ``` @startuml start partition "User (FE)" { :View Check Limit Page; :Edit Details if Necessary; :Update Portfolio Source; :Request MF Portfolio Details; :Choose CAMS or KFIN?; } partition "User (FE)" #LightBlue { if (CAMS Selected?) then (Yes) :Request OTP for CAMS MF Fetch;

---

## #329 — API grouping
**Status:** Unknown | **Last edited:** Unknown

# API grouping Sure! Below is a comprehensive list of all the APIs you've provided, organized into logical steps involved in the credit application process. I've included their descriptions and organized them into a table format that can be easily transferred to an Excel sheet. The total count of APIs is **112**. ### Step 1: Application Retrieval and Management | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 1 | `/app/borrower/application/{applicationId}` | GET | Retrieves application data using the application ID. | | 1 | `/app/borrower/application/change/state/progress/{applicationId}/{currentStepId}` | GET | Updates the step state to 'in progress' for the given application. | | 1 | `/app/borrower/application/override` | POST | Overrides application rules for exceptional cases. | | 1 | `/app/borrower/application/stepper` | POST | Retrieves stepper data for the given application. | ### Step 2: KYC Additional Details | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 2 | `/app/borrower/application/additionalDetails/{applicationId}` | GET | Retrieves the list of additional KYC details present in the system. | | 2 | `/app/borrower/application/additionalDetails/{applicationId}` | POST | Adds additional KYC details to the application. | ### Step 3: Agreement Processing | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 3 | `/app/borrower/application/agreement/link/{applicationId}` | GET | Retrieves the e-agreement setup link. | | 3 | `/app/borrower/application/agreement/status/{applicationId}` | GET | Retrieves the agreement acceptance status. | | 3 | `/app/borrower/application/agreement/stepper/{applicationId}` | GET | Retrieves agreement stepper information. | | 3 | `/app/borrower/application/doc/digio/init/{applicationId}` | GET | Initiates a Digio e-sign request for the agreement. | | 3 | `/app/borrower/application/doc/digio/status/{applicationId}` | GET | Checks the status of the Digio e-sign request. | | 3 | `/app/borrower/application/doc/digio/status/deep/{applicationId}` | GET | Performs a deep status check of the Digio e-sign request. | | 3 | `/app/borrower/application/signdesk/esign/init/{applicationId}` | GET | Initiates e-sign via SignDesk. | | 3 | `/app/borrower/application/signdesk/esign/status/deep/{applicationId}` | GET | Checks SignDesk e-sign status in depth. | | 3 | `/app/borrower/application/signdesk/esign/validate` | POST | Validates the SignDesk token. | ### Step 4: Loan Approval and Eligibility | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 4 | `/app/borrower/application/approval/check/{applicationId}` | GET | Retrieves loan approval status. | | 4 | `/app/borrower/application/check/shallow/creditApproval/{applicationId}` | GET | Checks credit approval status for

---

## #330 — APIs
**Status:** ** Retrieves the status of the KYC verification. | **Last edited:** Unknown

# APIs **Explanation of the API Sequence in the Volt Money Application Flow** Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience. --- ### **Overview** The Volt Money application process involves several key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail. --- ### **1. Login** - **API Used:** *Custom Authentication API (Not listed in the provided APIs)* - **Functionality:** - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone. - **Notes:** - This step establishes a secure session for the user. - While not specified in the provided API list, we use a standard authentication service to handle this process. --- ### **2. PAN Verification** - **API Used:** - `POST /app/borrower/application/kyc/pan/panVerify` - **Partner:** Decentro (facilitates connection to NSDL) - **Functionality:** - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid. - **Data Retrieval:** Fetches the full name associated with the PAN. - **Notes:** - Essential for KYC compliance and identity verification. - Helps prevent fraudulent applications. --- ### **3. Fetch Folio** - **APIs Used:** - `POST /app/borrower/application/fetch/init/otp/v3` - `POST /app/borrower/application/fetch/authCAS/v2` - **Partners:** Cams, KFintech, MF Central - **Functionality:** - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio. - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details. - **Notes:** - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets. - This data is used later in the asset pledge and eligibility assessment. --- ### **4. Eligibility Assessment and Lender Assignment** - **API Used:** - `POST /app/borrower/application/credit/profile/evaluate` - **Partner:** Internal Business Rule Engine (BRE) - **Functionality:** - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria. - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based

---

## #331 — LaMF application journey
**Status:** Unknown | **Last edited:** Unknown

# LaMF application journey [APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md) [API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md) [flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md) [Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md) The journey to create a loan against mf is as follows - login - user logs in using mobile number and otp validation - PAN verification - user enter DOB and PAN to validate pan , API - decentro - Fetch folio - we ping Cams/KFin to get the folio for the user - We ping them manually - we have option of gettign both from MF central - One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists - Folio have ISIN , NAV etc details - We assign the customer basis BRE to either Bajaj ot TATA capital - KYC of the customer aadhar - API is diifetent for tata and bajaj - Bank account verification - Mandate setting - Logement - KFS and docuemnttation Support I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table. [Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv) | Step | improvements | Description | Partner/Service | API Name | | | --- | --- | --- | --- | --- | --- | | Login | | User logs in using mobile number and OTP validation | | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) | | | Verify OTP | | | | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/ | | | user details | | | | https://api.staging.voltmoney.in/app/borrower/user | | | Email verification | | | Google sso | https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com | | | | | | Email / manual | | | | | | | | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) | | | | | | | | | | PAN Verification | | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API | | | Fetch Folio | | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API | | | Run BRE and Calculate Eligible Limits | | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system | | | | Assign Lender | | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system | | | | KYC Verification | | KYC of the customer with different APIs for Bajaj and TATA Capital

---

## #332 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #333 — Selfie capture journey
**Status:** Unknown | **Last edited:** Unknown

# Selfie capture journey In the Tata journey, we have a step to capture a selfie, but this is not included in the Bajaj journey. While the selfie feature is part of the Bajaj Figma design, it is neither implemented in production nor required. **User Flow for Selfie Capture (Bajaj Journey):** 1. The user sees a "Click Selfie" button, which activates the front camera after obtaining permission. 2. If an MFD creates the application, they can share a link with the customer. 3. The customer flow is as follows: - MFD shares the link with the customer. - Customer receives the link and opens it. - Customer logs in by verifying their phone number and entering the OTP. - The customer continues the application, completes KYC, and provides camera permissions. - Customer clicks the "Click Selfie" button, captures, and uploads the selfie. - Once the selfie is verified, the customer proceeds to the next steps.

---

## #334 — flow
**Status:** Unknown | **Last edited:** Unknown

# flow **User Journey Map for a Loan Against Mutual Funds Application** This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer). --- ### **1. User Acquisition and Onboarding** ### **1.1. Launching the App** - **FE Snippet:** - *Splash Screen > Launch App* ### **1.2. User Signup** - **FE Snippets:** - *Signup > View Signup Page* - *Signup > Click T&C or Privacy Policy* - *Signup > Edit Phone Number* - *Signup > Navigate to OTP Page* - *Signup > Resend OTP* - *Signup > Enter Invalid OTP* - *Signup > Complete Signup* - *Signup > View Verify Email Page* - *Signup > Verify Email with Google* - *Signup > Verify Email with Other Method* - *Signup > View Enter Email Page* - *Signup > Email Verification Result* - **BE Events:** - *Backend Events > OTP > Trigger OTP* - *Backend Events > OTP > Verify OTP* - *Backend Events > User Management > Create user context* - *Backend Events > User Management > Update user email* --- ### **2. Eligibility and Limit Check** ### **2.1. PAN Verification** - **FE Snippets:** - *Cash Limit > Enter PAN* - *Cash Limit > Verify PAN* - *Cash Limit > PAN Verification* - *Cash Limit > Edit PAN Details* - *Cash Limit > Confirm PAN Details* - **BE Events:** - *PAN Verification > Initiate PAN verification* - *PAN Verification > Complete PAN verification* - *PAN Verification > PAN verification failed* ### **2.2. Eligibility Check** - **FE Snippets:** - *Cash Limit > Trigger Eligibility Check* - *Cash Limit > Eligibility Check Result* - *Cash Limit > Application Under Review* - *Cash Limit > Application Rejected* - **BE Events:** - *Credit Application > Create credit application* - *Credit Approval Request > Receive credit approval request* - *Credit Approval Request > FAS creates the request* - *Credit Approval Request > LAN generation successful* - *Credit Approval Request > LAN generation failed* --- ### **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** - **FE Snippets:** - *Cash Limit > View Check Limit Page* - *Cash Limit > Edit Details on Check Limit Sheet* - *Cash Limit > Update Portfolio Source* - *Cash

---

## #335 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #336 — Notes
**Status:** Unknown | **Last edited:** Unknown

# Notes Redivision DSP - Prakhar to test the DSP flow - OTP for the Fetch taking too much time - The Email Enter earlier was of the Workemail and was not registered - Second time the OTP took too long to Confirm

---

## #337 — LaMF funnel
**Status:** Unknown | **Last edited:** Unknown

# LaMF funnel To document a funnel from a product manager's perspective, especially for opening a credit line with multiple third-party APIs involved, you can follow these steps: ### 1. **Define the Funnel Stages** - **Map the key stages** of the funnel from a user’s perspective. Each stage should represent a meaningful user action: 1. ### 2. **Identify Touchpoints & Third-Party API Dependencies** - **For each stage**, document which third-party API is involved and what data is exchanged. - **E.g.,** ### 3. **Track Conversion & Drop-off Metrics** - At each stage, define **conversion rate** (users who successfully pass to the next stage). - **Identify drop-offs**: Calculate how many users fail or exit the flow at each stage and investigate why. - **E.g., Eligibility Check** → 75% conversion, 25% drop-off due to API failure or ineligible users. ### 4. **Diagnose Breakpoints & Flow Bottlenecks** - **API Response Failures**: Track the rate of success and failure for API calls (e.g., timeout, invalid responses, high failure rate in the KYC stage). - **User Frustration Points**: Analyze user sessions to find out if there are UI/UX challenges (e.g., users leave due to complex form submissions or unclear messaging). - **Incomplete User Inputs**: Check if the flow is breaking due to missing or invalid user input (e.g., incorrect document uploads or failed validation). ### 5. **Attribution of Drop-offs** - **Tag each drop-off** with an attribution reason: 1. **Technical** (API failure, timeout, or 500 error). 2. **User Behavior** (abandonment, confusion with next steps). 3. **Eligibility** (e.g., failed credit check or ineligibility). ### 6. **Major Pain Points** - **Highlight user pain points** by reviewing feedback, support tickets, and analytics. - **E.g., KYC Step**: Users frequently abandon due to the complexity of document uploads. - Use qualitative feedback (e.g., user interviews, support chats) alongside quantitative data (e.g., Google Analytics, session recordings). ### 7. **Set Up Conversion Tracking** - Use **attribution tools** to track how users are progressing through the funnel, and set up **event tracking** in Google Analytics or similar. - **For each stage**, track key metrics like: 1. Average time spent. 2. Bounce rates. 3. API success/failure rates. ### 8. **Monitor Real-Time Data** - Implement **dashboards** that allow you to monitor API response times, error rates, and user journeys in real-time. - Example tools: **DataDog** for API monitoring, **Hotjar** for session recording, **Google Analytics** for user tracking. ### Example Documentation Flow: ``` 1. Stage 1: User Signup

---

## #338 — MFD Payout dashboard
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout dashboard We have a commercial relationship with MFD , where we pay them as per the business they bring Commercials | trail income | 0.5% of AUM | | --- | --- | | account opeing | 200rs | | Selfline | Processing fees waived | | Cashback | | | Content | | | referral | | - MFD payout is calculated based on commercials agreed on with them - MFD payout is different if the MFD is registed for GST - MFD with Gst number has to be paid 18% extra as GST - we collect 5 % TDS for any payout >15000rs - we payout on 10th on month to volt MFDs - we payout on 15th to SAAS partner platform MFDs - we payout on 18 th to MFD GST payout - we clear all pending and charges till 25th - MFD may not want to share the PAYOUT amount to there employees - MFD need to see the payout status - GST issues - Payout starts at 1 of the money - Time preiod is month to month - And 10 to 15 th of month payout disbursement happen - 10 MFD get paid - 15 Platform , - 18 MFD GST payout - 25 th anything pending - Puneet compute the payout MFD , 0.5% of AUM yearly trail income/ 12 200 rs per account opening , creditline open MFD selfline - we refund the family of MFDs , RMs fill a sheet Cashback for MFD’s end customers , - we gave 10.49 % customer we have given 0.5 % cashback as we advertised on 9.99% Contest , referrals price, activated MFD referral rs 1000 Platform , :- payout Affiliate - payout - MFD - - partner - - Platform - Affilaetes - Bharat sign off, Labdhi comms - Total amount August Pain points - GST filling , we have to 18% as a TDS of the total payout of the month. - we collect 5% TDS ,

---

## #339 — Missed calls from customers aren't being called ba
**Status:** Unknown | **Last edited:** Unknown

# Missed calls from customers aren't being called back or addressed # Missed Calls and Customer Support Optimization Missed calls from customers are a significant issue, as many are not being addressed. Customers reach out to us for help during various stages, such as onboarding, opening credit lines, post-account opening support, or product inquiries. To effectively manage these requests and reduce missed calls, we need a strategy that not only addresses customer needs but also balances the cost of support channels. ## Understanding the Support Categories: We can categorize customer interactions into three key areas: 1. **Awareness**: Customers seek to understand the product better. 2. **Sales**: Customers eligible for the service but who have not yet opened an account. 3. **Support**: Customers who already have accounts and need assistance with specific issues. ## Support Channel Options: There are several ways we can provide support, each with its own cost and effectiveness: - **Online Documentation**: Free but less accessible for most users. - **Product Journey (In-App Help)**: Accessible but costly in terms of development time. - **Chat Support**: Affordable and accessible for general queries. - **Call Support**: Highly impactful but also the most expensive to maintain. ### Optimizing Customer Support: Our goal is to provide the right support channel for each category of customer, depending on their needs, to maximize effectiveness while minimizing costs. This means segmenting customers into "buckets" based on their status and needs and directing them to the appropriate support channel: | **Bucket** | **Identifier** | **Channel to Retarget** | | --- | --- | --- | | **Awareness** | No record of the number in the system, ineligible | Chat or WhatsApp | | **Sales** | Eligible number, account not yet opened | Call Support | | **Support** | Customer with an open account | Chatbot with common services | ### Proposed Changes: To reduce call support costs, we should remove the call option for ineligible customers and instead provide them with WhatsApp support. This will help to ensure that calls are only directed to customers who are further along the funnel, and likely to require higher-touch support. ### Key Objectives: - **Address customer needs** through the appropriate support channels. - **Reduce support costs** by minimizing unnecessary call support. - **Reduce missed calls and errors** by routing customers more effectively. ### Data Requirements: To implement this strategy, we need to collect and analyze the following data: -

---

## #340 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #341 — API flow for KFS and Agreement
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

## #342 — Additional details enhancement
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

## #343 — Analytics requirement for amortisation of PF
**Status:** Pending review | **Last edited:** Unknown

# Analytics requirement for amortisation of PF Last Edited: April 24, 2026 8:59 AM PRD ETA: April 24, 2026 PRD Owner: Vaibhav Arora # **1. Objective** Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module. The design must be extensible to accommodate other fee/cost types in future iterations without structural rework. # **2. Scope & Exclusions** ## **2.1 In Scope** - Product lines: LAMF, LAS, Term Loan (TL) - Charge type: Processing Fee (PF) - Accounting entries: Income recognition at monthly amortisation level - Amortisation method: Straight Line Method (SLM) - Report period: M-N (N>0) (previous calendar months only) - Waiver handling: Partial and complete waivers with corresponding reverse entries - Loan closure handling: Remaining balance acceleration on closure date ## **2.2 Explicitly Out of Scope** - GST component of processing fee excluded from amortisation entries - Current month entries - report is strictly retrospective - Real-time or intra-month amortisation schedules # **3. Source Data & Key Fields** All data will be sourced from the accounting report. The following fields are required at a schedule/charge level: | **Field** | **Source / Table** | **Notes** | | --- | --- | --- | | FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier | | Client External ID | LMS – Loan Master | FXCID reference | | Product Type | LMS – Loan Master | LAMF / LAS / TL | | Charge Application Date | LMS – Fee Schedule | Date PF was applied | | PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only | | Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference | | Loan Status | LMS – Loan Master | Active / Closed | | Closure Date | LMS – Loan Master | Populated only if loan is closed | | Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator | | Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee | | Waiver Date | LMS – Waiver Log | Date waiver was applied | | Waiver Type | LMS – Waiver Log | Partial /

---

## #344 — BRD Interest Refund via Credit Note - OD - V2
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Refund of interest already posted and/or collected
- Refund processed only via Credit Note (Interest type)
- Support for partial and full interest refunds
- Integrated accounting and LMS impact
- Duplicate refund control with necessary dedupe validations

# BRD: Interest Refund via Credit Note - OD - V2 Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ## 1. Background & Objective Interest is periodically accrued, posted, and collected from users as part of the OD loan lifecycle and recognized as interest income in the accounting system. In certain business scenarios (pricing corrections, excess collection, grievance redressal, operational errors, etc.), a portion of already posted and/or collected interest may need to be refunded to the user. The objective of this document is to define a **system-driven, auditable mechanism** to process interest refunds via Credit Note with correct accounting treatment. The solution must ensure: - Accurate reversal of interest income in P&L - Correct user-level balance adjustment - Elimination of manual accounting interventions - Full audit traceability --- ## 2. Scope ### In Scope - Refund of interest already posted and/or collected - Refund processed only via Credit Note (Interest type) - Support for partial and full interest refunds - Integrated accounting and LMS impact - Duplicate refund control with necessary dedupe validations ### Out of Scope - Interest waiver before posting --- ## 3. Key Definitions | Term | Definition | | --- | --- | | Interest Refund | Reversal of interest already posted and/or collected | | Credit Note (Interest) | LMS transaction representing interest refund | | Interest Income Reversal A/c | Contra-income GL used to reverse recognised interest revenue | --- ## 4. Accounting Principles Interest refunds will follow a **single-step integrated accounting construct**. At the time of Credit Note processing: - User balance adjustment and income reversal will occur simultaneously - No intermediate liability or clearing account will be created - P&L impact will be immediate This ensures: - LMS reflects user truth - Accounting reflects financial truth - Reduced reconciliation complexity - No deferred clearing entries --- ## 5. Accounting Treatment ### 5.1 Interest Refund – Credit Note Issued At the time of processing Credit Note (Interest Refund): | Account | Debit | Credit | Account Type | | --- | --- | --- | --- | | Interest Income Reversal A/c | Refund Amount | | Contra Income | | User Interest / Excess / Principal (as applicable) | | Refund Amount | Asset / Liability | --- ### Impact - User outstanding reduces (or excess ledger adjusted) - Interest income reversed immediately in P&L - No clearing

---

## #345 — BRD Interest Refund via Credit Note - OD
**Status:** Completed | **Last edited:** Unknown

**In scope:**
- Refund of interest already posted and/or collected
- Refund processed only via **Credit Note**
- Accounting treatment for:
    - Interest income reversal
    
- Support for partial and full interest refunds

# BRD: Interest Refund via Credit Note - OD Last Edited: March 19, 2026 9:44 PM --- ## 1. Background & Objective Interest is periodically accrued, posted, and collected from users as part of the loan lifecycle and recognized as **interest income** in the accounting system. In specific business scenarios, a portion of **already posted and/or collected interest** may need to be reversed and refunded to the user. Currently, interest refunds are handled manually or via ad-hoc adjustments, which introduces: - Accounting inconsistencies - Limited audit traceability - Operational risk at scale ### Objective Define a **system-driven, auditable** mechanism to refund interest via **Credit Note**, ensuring: - Correct P&L reversal of interest income - Correct user balance adjustment - Alignment with existing Credit Note & Waiver accounting patterns --- ## 2. Scope ### In Scope - Refund of interest already posted and/or collected - Refund processed only via **Credit Note** - Accounting treatment for: - Interest income reversal - Support for partial and full interest refunds ### Out of Scope - Interest waiver before posting --- ## 3. Key Definitions | Term | Definition | | --- | --- | | Interest Refund | Reversal of interest already posted and/or collected | | Credit Note (Interest) | LMS transaction representing interest refund | | Intermittent Liability A/c | Temporary clearing account for refund settlement | | Interest Income Reversal A/c | Contra-income account to reverse interest revenue | --- ## 4. Accounting Principles The interest refund follows the **same two-step accounting construct** used for charge refunds: 1. User-level adjustment via **Credit Note** 2. Income reversal via **accounting journal** This ensures: - LMS reflects user truth - Accounting reflects financial truth - Refund execution remains decoupled from income correction --- ## 5. Accounting Scenarios ### 5.1 Interest Refund – Interest Collected (Credit Note Issued) ### Step 1: LMS Transaction – Credit Note (Interest) Creates a refund obligation without impacting income directly. | Account | Debit | Credit | Account Type | | --- | --- | --- | --- | | Intermittent Liability A/c | Interest Amount | | Liability | | As per apportionment of the credit note (independent of charge/interest waiver | | Principal/interest/Charge/Excess | Asset / Liability | **Impact** - User balance reduced - No P&L impact at this stage - Refund liability created --- ### Step 2: Accounting Journal – Interest Income & GST Reversal | Account

---

## #346 — Charge reversal enhancement
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

## #347 — Charge reversal enhancement V2
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

## #348 — Colending Disbursement and Charge knock off
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

## #349 — Credit note PRD
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

## #350 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #351 — Disbursement simulation - LMS
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
- Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula.
- Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen.
- Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum a

# Disbursement simulation - LMS Last Edited: May 22, 2026 3:49 PM PRD ETA: May 5, 2026 PRD Owner: Vaibhav Arora ## Background and Context - **Who is affected** - Borrowers using Volt (DSP Finance's LSP) who initiate withdrawal requests from their Loan Against Mutual Fund (LAMF) accounts. - All LSP partners integrated with DSP Finance's disbursement infrastructure. - DSP Finance's Risk Operations team, who are exposed to collateral shortfall risk when disbursements breach the safe limit. - **What is broken today** - The current Available Limit calculation — `AL = min(DP, SL) - POS + EM` does not account for accrued interest, charges, or scenarios where non-principal exposure grows to exceed the margin held against collateral. Two specific scenarios expose DSP Finance to risk: - **Case 1 — Collateral Removal:** After a borrower repays principal and requests maximum collateral removal, the remaining collateral may only cover the Drawing Power. Any subsequent withdrawal creates a situation where accrued interest (once booked as Interest Due) pushes total exposure above collateral value. - **Case 2 — Voluntary Sell-off:** After a sell-off settles principal, the sell-off proceeds inflate Excess Money, which inflates the Available Limit. A borrower can withdraw this excess, creating a POS that, combined with accrued interest becoming due, exceeds the remaining collateral value. - Today, the Loan Detail API value is trusted by all downstream systems (Fenix, Volt, and LSP partners) as the authoritative available limit. There is no pre-disbursement validation layer that applies the updated risk-safe AL formula before funds are transferred. - **Why it matters** - Collateral shortfall represents direct credit risk for DSP Finance — in cases of default, outstanding dues cannot be fully recovered. - The gap grows over time as accrued interest compounds, making early intervention critical. - LSP partners rely on the available limit shown to borrowers; without a simulation gate, disbursements that breach exposure limits will be processed without any check. --- ## 1. Problem Scope ### In scope - Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula. - Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen. - Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum allowed amount and enabling re-entry. - API design contract documentation to be shared with

---

## #352 — Dishonour charge enhancement
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

## #353 — FD Fixerra
**Status:** Unknown | **Last edited:** Unknown

# FD: Fixerra Last Edited: December 1, 2025 2:13 PM ### Product Alignment Note – Fixerra FD Offering via Partner Dashboard *(DSP Finance × Volt Platform)* --- ### **Problem statement** Volt x DSP have a strong distribution via IFAs, we want to experiment distribution of different products via this channel, because of DSP Finance (NBFC) is looking to expand its retail investment footprint beyond LAMF (Loan Against Mutual Funds) by introducing a Fixed Deposit (FD) product. On the Volt platform today, distributors (primarily MFDs) only have LAMF as the monetizable product. While LAMF has strong unit economics, it is not a top-of-funnel product for retail customers. Fixerra provides the underlying FD product and infrastructure. The hypothesis is: - We already have arms-reach access to a large base of customers with mutual fund holdings. - These customers have a natural affinity for low-risk investment instruments. - FDs can act as a trust-building, widely accepted entry product, opening the funnel for both direct revenue (FD) and future LAMF conversions. This note outlines the scope for v1 of FD origination and servicing through the Volt Partner Dashboard, and is intended to align stakeholders across DSP Finance, Volt, and Fixerra. --- ### 2. Problem statement ### 2.1 Current state - MFDs on Volt can only offer LAMF. - Monetization is limited to one product with a relatively narrow target audience. - No simple “safe” product exists to attract or engage a wider customer base. - Distributors lack tools to deepen customer relationships beyond MF transactions. ### 2.2 Opportunity Introducing FDs: - Expands the product portfolio for MFDs. - Helps create a trust-led entry point (“mouth of the funnel”), improving conversions into higher-ticket products like LAMF. - Offers DSP Finance a scalable retail deposit base. - Allows Fixerra to distribute its FD product through MFD networks. --- ### 3. Product hypothesis **FDs can become a high-trust, low-friction product that increases distributor engagement and revenue, while simultaneously opening the pipeline for LAMF upsell.** Supporting hypotheses: 1. Customers with MF holdings are more likely to evaluate FD products with high confidence. 2. MFDs will be able to deepen their relationship and improve overall earnings by offering a broader product suite. 3. The NBFC can explore differentiated FD structuring based on distribution performance (for example, special rates, bulk programs). --- ### 4. High-level GTM - **Channel:** Volt Partner Dashboard - **Actors:** Mutual Fund Distributors on Volt - **v1

---

## #354 — Finflux Product Setup for Co-Lending
**Status:** Completed | **Last edited:** Unknown

# Finflux Product Setup for Co-Lending Last Edited: March 19, 2026 9:44 PM PRD ETA: January 27, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context As part of the co-lending setup, loans are economically split between: - **10% exposure (CLA portion)** - **90% exposure (TCL)** - **100% loan representation** required for operational and accounting purposes Current state: - Finflux is running on a **single instance** supporting **OD and TL products** - All reporting, accounting, SMA/NPA tagging, and operational workflows are currently **instance-scoped** - Finflux manages collateral and exposure deduplication The setup needs to support: - Fast go-live - Clean accounting - Correct delinquency signaling to TCL - Minimal disruption to existing production flows --- ## 2. Problem Statement The co-lending structure introduces multiple complexities: - **Collateral deduplication risk** if multiple loans referencing the same securities exist in the same instance - **Client-level SMA/NPA contagion**, where delinquency in a small CLA exposure may impact unrelated production loans - **Accounting segregation** required across different exposure types - **Operational overhead** introduced by multiple Finflux instances - **Reporting and reconciliation complexity** across LMS, Finflux, and TCL --- ## 3. Design Options Considered ### Option A: Single Finflux Instance with Multiple Products - All co-lending loans (10% and 100%) reside in the same instance - Separation handled purely via product-level configurations **Challenges** - High risk of collateral dedupe conflicts - Client-level NPA impact across all loans - Heavy reliance on product-level filters across reporting and accounting - Higher regression risk for existing OD and TL products --- ### Option B: Multiple Finflux Instances for All Co-Lending Loans - Separate instances for 10% and 100% loans **Challenges** - Higher setup and maintenance effort - Configuration and version-sync risks - Increased reporting and reconciliation overhead - Multiple operational points of failure at launch --- ## 4. Final Recommendation (Chosen Approach) **Recommended Setup** - **10% co-lending loan (CLA exposure)** → Booked in the **existing Finflux instance** - **100% loan** → Booked in a **separate Finflux instance** - **90% exposure** → Booked in **TCL** This approach optimizes for **lower effort, faster go-live, and controlled risk**, while keeping core production flows isolated. --- ## 5. Rationale for the Recommendation ### 5.1 Faster Go-Live with Minimal Change Surface - Existing Finflux instance already supports: - Live products - Accounting - Reporting - Monitoring - Adding a **single CLA product (10%)** is significantly lower effort than: - Standing up and

---

## #355 — LAS CMS Confiscation and sale of securities
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

## #356 — LAS CMS Lodgement
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

## #357 — LAS CMS Unlodgement
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

## #358 — PMR consumption SHCIL
**Status:** Done | **Last edited:** Unknown

**Problem:**
are we solving?**

In a Loan Against Securities (LAS) setup, collateral positions are dynamic — securities can be lien marked, revoked, confiscated, or impacted by corporate actions at any time. For the NBFC, accurate and timely tracking of these changes is critical to:

- **Maintain exposure** by ensuring only lien-marked securities are considered as collateral.
- **Protect against credit and operational risk** by reconciling collateral transactions with actual depository data.

Why is it important?

- **Detection of lien mismatches** (e.g., securities released or confiscated without a reques

**Solution:**
?**

We will integrate **Pledge Master Report (PMR) consumption** into the Collateral Management System (CMS) to create a single, authoritative repository of all securities lien-marked in favour of the NBFC.

The PMR, received periodically from the depository, will be ingested into CMS and transformed into a structured collateral database. This will allow:

- **Automated lien verification** against depository records.
- **Accurate reconciliation** of pledged holdings between NBFC and depository data.
- **End-to-end collateral transaction lifecycle management** — tracking lien marking, revocation, substitution, and invocation.
- **NBFC-specific pledged collateral tracking** to maintain exposure accuracy.
- **Unlinked collateral identification and resolution** for pending customer applicatio

---

## #359 — Sample PMR transactions
**Status:** Done | **Last edited:** Unknown

# Sample PMR transactions ## CDSL (Lien marking): Pledge marking | Date | BO ID | ISIN | ISIN Description | Pledged Quantity | Pledgee Name | Status | Pledge Type | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Confirmed | Margin | Pledge created successfully | ## CDSL (Lien revocation): Pledge closure | Date | BO ID | ISIN | ISIN Description | Closed Quantity | Pledgee Name | Status | Closure Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Released | 05-Jul-2025 | Pledge closed successfully | ### CDSL: (Lien invocation) | Date | BO ID | ISIN | ISIN Description | Invoked Quantity | Pledgee Name | Status | Invocation Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 07-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 50 | DSP Finance Pvt Ltd | Invoked | 07-Jul-2025 | Partial invocation triggered | ### NSDL (Lien marking): Pledge marking | Execution Date | Client ID | ISIN | ISIN Description | Pledged Quantity | Pledgee | Pledge Type | Margin Pledge | Status | Agreement No. | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Margin | Yes | Confirmed | AGMT-56789 | ### NSDL (Lien revocation) Pledge closure | Closure Date | Client ID | ISIN | ISIN Description | Closed Quantity | Pledgee | Status | Lock-In Reason | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Released | NA | Closure on user request | ### NSDL (Lien invocation) | Execution Date | Client ID | ISIN | ISIN Description | Invoked Quantity | Pledgee | Status | Remarks | | ---

---

## #360 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #361 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #362 — LSP Presentation enhancement for externally regist
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

## #363 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #364 — NBFC PG Evaluation
**Status:** Unknown | **Last edited:** Unknown

# NBFC PG Evaluation Last Edited: April 8, 2025 1:06 PM PRD Owner: Surya Ganesh # Evaluation Criteria ## Business Criteria | Parameter | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | | Same day Settlements | No | No | No | No | | UPI Commercials | | | | | | Netbanking Commercials | | | | | | VISA Commercials | | | | | | Mastercard Commercials | | | | | | | | | | | ## Product Criteria | Parameter | Priority | RazorPay | PhonePe | PayU + HDFC | Easebuzz | | --- | --- | --- | --- | --- | --- | | No user login (OTP) | High | No | Available (Standard checkout flow doesn't require user login) | | | | Transaction level control on payment methods | High | | Available (Can specify payment instruments in the payment initiation request) | | | | Transaction level control on card networks | High | | Available (Can filter specific card networks in payment instruments) | | | | Customer name at transaction level | High | | | | | | Backend callback post transaction level | High | | Available (Via callbackUrl parameter in payment request) | | | | Ability to whitelist multiple URLs | High | | Available (Can configure multiple callback and redirect URLs) | | | | White-labelling of checkout | High | | Limited (PhonePe branded checkout but some customization options) | | | | Error codes and reasons at transaction level | High | | Available (Detailed error codes in status responses) | | | | Settlement webhook | Medium | | Available (Supports settlement notifications) | | | | TPV check for UPI transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for DC transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for Netbanking transactions | High | | Available (Transaction status API provides verification) | | | ## Operations Criteria | Parameter | Priority | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | --- | | Settlement timeline | High |

---

## #365 — PMR consumption
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?

Today, Pledge Master Reports (PMRs) are received over email at [collaterals@dspfin.com](mailto:collaterals@dspfin.com). The ops team shares these with engineering, who manually hit an API to consume the report - creating an operational bottleneck that directly impacts loan account opening timelines for the Loan Against Shares (LAS) program.

We need to eliminate this manual handoff by automating PMR ingestion the moment the email arrives, while preserving a checker workflow for validation and audit.

In a Loan Against Securities (LAS) setup, collateral positions are dynamic se

**Solution:**
?

---

## #366 — PPSL UPI mandate presentation
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

## #367 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #368 — Product Note Interest Refund via Credit Note
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, e

# Product Note: Interest Refund via Credit Note Last Edited: January 23, 2026 8:15 PM PRD ETA: July 22, 2025 PRD Owner: Vaibhav Arora ## Background and Context **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged or goodwill interest waivers - Operations team processing interest refunds/waivers - Finance team managing manual accounting entries for interest reversals - Tech ops/Product handling backend interventions for interest adjustments **What is the challenge that they are facing? What is broken today?** - Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access - Process is operationally intensive with dependency on Jira ticket workflows - No standardized maker-checker workflow for interest refunds similar to charge refunds - Manual JV posting for interest reversals creates additional overhead for Finance team - Lengthy resolution time (2-3 days) impacting customer experience - No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period - Lack of visibility and tracking for interest refund requests across the loan lifecycle **Why is it important? What is getting impacted?** - Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests - Operational inefficiency with high manual effort required for each interest refund case - Risk of errors and duplicate processing without systematic validations - Finance team bandwidth consumed by repetitive manual JV entries - Lack of audit trail and reconciliation capabilities for interest reversals - Inconsistent treatment of interest refunds compared to the now-standardised charge refund process --- ## 1. Problem Scope ### In scope **What specific problems are we solving?** 1. **Slow Resolution Time:** - Interest refund requests take 2-3 days to resolve from initiation to completion - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product 2. **Operational Bottleneck and Dependency:** - Operations teams cannot independently process interest refunds or waivers - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention - Backend access and API calls are needed for what should be a routine operational task - Process creates unnecessary dependencies across multiple teams for resolution 3. **Risk of Duplicate Processing:** - No systematic validation exists to check if interest for a specific period has already been waived or refunded - Product team rely

---

## #369 — Product Note LAS Customer Consent Capture
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

## #370 — Product note Credit note for TL
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

We are solving:

# Product note: Credit note for TL Last Edited: April 28, 2026 4:45 PM PRD ETA: April 17, 2026 PRD Owner: Vaibhav Arora # **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)** --- ## **Background and Context** **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged interest - Operations team handling refund/waiver requests - Finance team managing manual income reversals and reconciliation - Product/Tech teams currently intervening via backend/API --- **What is the challenge today?** - Interest refunds require **manual intervention via engineering or Finflux access** - No standardized **maker-checker workflow** - **Not supported for Term loans, currently productised and implemented only for OD** - Manual JV posting required for income reversal - No **system-driven dedupe or validation** - No **tranche-level visibility or audit tracking** - Turnaround time is **2–3 days**, impacting CX --- **Why is it important?** - Poor customer experience due to delays - High operational dependency and inefficiency - Risk of duplicate or incorrect refunds - Manual accounting overhead for finance - Lack of audit trail and reconciliation visibility --- ## **1. Problem Scope** ### **In Scope** We are solving: ### **1. Operational Independence** - Enable Ops to process **interest refunds without engineering dependency for Term loans** - Introduce **maker-checker workflow** --- ### **2. Standardized Accounting** - Eliminate manual JV posting - Introduce **credit note + automated income reversal** --- ### **3. Tranche-Level Refund Handling** - Refunds applied at **tranche level (not line level)** - Excess created is: - Initially **tranche-tagged** - **Not usable across tranches while tranche is active** - Becomes **line-level usable only after tranche closure** --- ### **4. Validation & Dedupe** - Prevent duplicate refunds via: - Schedule validation - Credit note existence checks --- ### **5. Audit & Traceability** - Full linkage: - Interest → Credit Note → JV - Tranche-level enrichment and reporting --- ### **Out of Scope** - Principal refunds - Bulk refund processing - Automated eligibility rules - Reversal of incorrect refunds (no reversal flow) --- ## **2. Success Criteria** ### **Outcomes** - Maker → Checker → Accounting completion within **1 hour** - **>90% reduction** in Jira dependency - Capability to refund interest for Term Loan - **Zero duplicate refunds** at tranche-month level --- ### **Post-launch Good State** - All refunds processed via maker-checker - Credit notes posted correctly at tranche level - Automated JV posted for income reversal - Finance can reconcile via

---

## #371 — Product note Excess refund Colending
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

## #372 — Product note Interest rate change handling
**Status:** Pending review | **Last edited:** Unknown

# Product note: Interest rate change handling Last Edited: March 19, 2026 9:51 PM PRD ETA: March 19, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** In the current co-lending construct between DSP (NBFC) and TCL (co-lender), loans are originated and managed across multiple representations within the LMS: - **Loan 90 (TCL Book):** Represents TCL’s capital contribution and is controlled externally by TCL, including interest rate decisions. - **Loan 10 (DSP Book):** Represents DSP’s capital contribution and follows DSP’s internal benchmark and pricing logic. - **Loan 100 (Customer-facing Loan):** A composite loan created in the LMS, reflecting the borrower’s obligation and used for repayment schedules, accruals, and customer communication. The effective interest rate for the borrower is derived as a **weighted average of the underlying lender rates based on capital contribution**: - 90% → TCL (Loan 90) - 10% → DSP (Loan 10) However, from a system and implementation perspective: - The LMS treats **Loan 100 as an independent loan** with its own benchmark and ROI. - Interest rates are currently configured using **benchmark + spread constructs defined at an organizational level**. - There is **no native support for dynamic weighted rate computation** across multiple lender loans within the LMS. --- ### **Problem Statement** As part of ongoing co-lending operations: 1. **Independent Rate Changes by Lenders** - TCL may revise its interest rates (benchmark or spread) independently. - DSP may also revise its own benchmark rates. - These changes directly impact the **effective blended ROI** applicable to the borrower. 2. **Lack of Native Synchronization** - Since Loan 90, Loan 10, and Loan 100 are maintained separately: - Rate changes in Loan 90 (TCL) do not automatically reflect in Loan 100. - Loan 100 must be **manually or systematically updated** to maintain parity with the blended rate. 3. **Risk of Misalignment** - If Loan 90 and Loan 100 are not updated in sync: - Incorrect borrower interest may be charged. - Accruals and repayment splits between lenders may become inconsistent. - Downstream systems (accounting, reconciliation, reporting) may break. 4. **Operational Complexity** - Current benchmark configuration is **organization-wide**, not contract-specific. - With multiple co-lending partners, each having: - Different benchmarks - Different spreads - Different rate change cycles → A single benchmark approach does not scale. --- ### **Constraints** - Loan 100 **must exist as a physical loan in the LMS** and cannot be treated as a derived construct. - LMS

---

## #373 — Product note Razorpay PG integration Colending
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

## #374 — Product note Virtual account handling for Colendin
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

## #375 — Razorpay SDK enhancement for Colending
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

## #376 — Risk management system LAS
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

## #377 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #378 — Tally ERP Integration
**Status:** Completed | **Last edited:** Unknown

# Tally ERP Integration Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # **Tally Journal Voucher API Contract (Sample Document)** This document outlines the proposed API contract for pushing journal voucher entries from the LMS/ERP system to Tally. Each journal voucher corresponds to a single **transaction event**, containing one or more **ledger-level debit/credit lines** with consolidated amounts. --- ## **1. API Overview** ### **Endpoint** (To be shared by the vendor) ### **Purpose** Push a complete journal voucher entry at a transaction type level to Tally for accounting purposes. --- ## **2. Request Structure (Batch Journal Posting)** The API will support **batch posting** of journal vouchers. Each request will contain an **array of transactions**, where each object represents one complete journal voucher. ### **2.1 Journal Voucher Batch Payload** ```json [ { "transaction_type": "string", "narration": "string", "voucher_date": "YYYY-MM-DD", "tally_txn_id": "1234564534432", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" } ] }, { "transaction_type": "string", "narration": "string", "tally_txn_id": "1234564534433", "voucher_date": "YYYY-MM-DD", "ledger_entries": [ { "ledger_name": "Sample1", "debit": "number", "credit": "number" }, { "ledger_name": "Sample2", "debit": "number", "credit": "number" }, { "ledger_name": "Sample3", "debit": "number", "credit": "number" } ] } ] ``` --- ### **Field Description** | Field | Type | Description | | --- | --- | --- | | transaction_type | string | Preconfigured transaction type (ex: PAYIN, PAYOUT) | | tally_txn_id | string | Unique transaction identifier used as **dedupe key** | | voucher_date | date | Voucher posting date | | narration | string | Narration mapped to transaction type | | ledger_entries | array | List of debit/credit ledger lines | --- ### **Ledger Entry Object** | Field | Type | Description | | --- | --- | --- | | ledger_name | string | Name of the ledger in Tally | | debit | number | Amount debited (zero if not applicable) | | credit | number | Amount credited (zero if not applicable) | --- ## **3. Transaction Type Samples** Below are examples for each transaction type based on provided data. --- ## **3.1 ADD_FEE** **Narration:** Being fee income recognition ```json { "tally_txn_id": "<unique-id>", "transaction_type": "ADD_FEE", "voucher_date": "2025-01-01", "narration": "Application of fee on loan account", "ledger_entries": [ {"ledger_name": "Fees receivable", "debit": 7109825, "credit": 0}, {"ledger_name": "Income from Fees", "debit": 0, "credit": 6025269}, {"ledger_name": "CGST Payable", "debit": 0, "credit": 90382}, {"ledger_name": "SGST Payable", "debit": 0, "credit":

---

## #379 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #380 — Unpledge - Stocks selection logic
**Status:** Completed | **Last edited:** Unknown

**Solution:**
?**

---

## #381 — Volt - Overdue Communication Enhancement
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

## #382 — Volt - Shortfall Communication Enhancement – Due D
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

## #383 — [Platform] Decoupling of dishonour fees with manda
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

## #384 — [Platform] Disbursement optimisation to handle cro
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

## #385 — [Platform] Mandate collection enhancement
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

## #386 — tech issues
**Status:** Unknown | **Last edited:** Unknown

# tech issues ## ### KYC & Authentication Issues 1. **KYC verification process fails with no clear error messaging** - Example (VTS-9511): "AKGPV3060R - Not able to move forward in kyc step" - Customer was stuck during verification with no indication of what went wrong or how to proceed. - Example (VTS-9981): "Stuck in kyc summary" - Process halted after completing verification with no error details provided to the customer. 2. **Digilocker integration failures during KYC verification** - Example (VTS-9770): "9415307644 - VIKAS KUMAR - KYC issue with digilocker's end" - API connection to Digilocker failing, preventing document verification. - Example (VTS-9964): "Discrepancies in CKYC record associated with the KYC Identifier: 50072772797161" - Records in Digilocker not matching with application data. 3. **Unusual KYC errors without diagnostic information** - Example (VTS-9711): "Unusual KYC Error" - Generic error message without actionable details for troubleshooting. - Example (VTS-10138): "CFCPS2351M - Facing error on KYC Page" - Customer encountered undefined error with no clear next steps. ### Pledging Process Failures 1. **KFin OTP delivery system failures** - Example (VTS-10085): "8928846293 - ATUL TIWARI - not getting otp at pledging for kfintech" - Customer attempted multiple times from web and app but never received OTP. - Example (VTS-10227): "8884052766 - DINESH KUMAR INALA - Kfintech pledging OTP issue" - System-wide failure in OTP delivery when pledging through KFin. 2. **Pledging failure despite eligibility** - Example (VTS-9396): "EQSPK8350P - KFin Pledging error" - "Fund is in approved list of TATA and is also visible when we did 15sec eligibility check" but still failing. - Example (VTS-9358): "DIWPP4809P - Unable to pledge Kfin funds" - Eligible funds appearing in portfolio but pledge transaction failing. 3. **Funds pledged but not lodged in system** - Example (VTS-9884): "Lodgment issue -ANNPS4596F" - "One of the pledged funds of the above client is not lodged in the system yet". - Example (VTS-10044): "BEPPB3956Q, Units pledged but lodgment not done" - Pledge transaction completed but credit not applied to account. ### API Integration Failures 1. **Timeouts in partner integrations** - Example (VTS-9597): "Frequent API Timeout Issues" - FundsIndia experiencing frequent API timeouts, preventing operations completion. - Example (VTS-9529): "Assistance Required: User Facing PAN Mobile Number Error in SDK" - API timeout causing user verification failures. 2. **Document API failures** - Example (VTS-9346): "Volt - Documents are Missing" - "I checked the webtops and I am unbale to find. Requesting you to

---

## #387 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #388 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #389 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #390 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #391 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #392 — SDK
**Status:** Unknown | **Last edited:** Unknown

# SDK - JS sdk - IOS sdk - Android SDK - RN sdk - partner mobile APP, web , PLJ - Iframe - webhook for partner , v-kyc done or not to partners - API exposed, Get application status , KYC done , bifurcation -

---

## #393 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #394 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #395 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #396 — UI benchmarking for CGS
**Status:** Unknown | **Last edited:** Unknown

# UI benchmarking for CGS ## Calculator tabs on websites 1. Smallcase ![Untitled](UI%20benchmarking%20for%20CGS/Untitled.png) 1. ETMoney ![Untitled](UI%20benchmarking%20for%20CGS/Untitled%201.png) 1. Jupiter ![Untitled](UI%20benchmarking%20for%20CGS/Untitled%202.png) 1. Fi ![Screenshot 2024-02-27 at 4.06.30 PM.png](UI%20benchmarking%20for%20CGS/Screenshot_2024-02-27_at_4.06.30_PM.png) 1. Groww ![Screenshot 2024-02-27 at 4.09.58 PM.png](UI%20benchmarking%20for%20CGS/Screenshot_2024-02-27_at_4.09.58_PM.png) ![Screenshot 2024-02-27 at 4.08.05 PM.png](UI%20benchmarking%20for%20CGS/Screenshot_2024-02-27_at_4.08.05_PM.png) ![Screenshot 2024-02-27 at 4.08.18 PM.png](UI%20benchmarking%20for%20CGS/Screenshot_2024-02-27_at_4.08.18_PM.png) 1. Zerodha ![Untitled](UI%20benchmarking%20for%20CGS/Untitled%203.png) 1. Cred ![Screenshot 2024-02-27 at 4.17.07 PM.png](UI%20benchmarking%20for%20CGS/Screenshot_2024-02-27_at_4.17.07_PM.png) ## Calculators input and output No direct comparison, all calculators either calculate STCG or LTCG. Economics time ![Untitled](UI%20benchmarking%20for%20CGS/Untitled%204.png) [https://www.etmoney.com/tools-and-calculators/income-tax-calculator](https://www.etmoney.com/tools-and-calculators/income-tax-calculator): Great minimalist structure, the structure of UI presentation is great.

---

## #397 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #398 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #399 — SEO Text
**Status:** Unknown | **Last edited:** Unknown

# SEO Text A Loan against mutual funds (LAMF) allows you to borrow money by using your mutual fund units as collateral. Volt Money’s loan against mutual funds calculator can help you estimate the interest costs associated with this financing option. **What is a loan against mutual funds (LAMF)?** A loan against mutual funds (LAMF) is a secured loan where you pledge your mutual fund units as security to borrow money. The lender will determine the maximum loan amount you can qualify for based on a Loan-to-Value (LTV) ratio. This ratio represents the percentage of your mutual fund's market value that the lender is willing to lend against. You are then issued a credit limit which functions like a bank overdraft facility, where you are charged interest only on the amount you withdraw from this credit limit. **How to get a loan against mutual funds?** With Volt Money, you can get loan against mutual funds in 4 simple steps: 1. Check credit limit: We’ll evaluate your mutual fund portfolio & confirm credit limit. Check your credit limit from here. 2. Instant KYC: Complete digital KYC process. No paperwork required! 3. Pledge your assets: Mark your mutual funds as a security with a trusted lender. 4. Withdraw money: Withdraw & repay as per you requirement. No hidden charges. **How interest is calculated on loan against mutual funds?** Loan against mutual fund works like a bank overdraft limit, where you are only charged interest on the amount you withdraw. Interest is calculated daily and is deducted on a particular date every month. Interest calculation works on the following formula: Daily interest = P*(R/365) Monthly interest = Daily interest*N P = Principal outstanding on the day R = Annual rate of interest N = Number of days in a month Example: Suppose you withdraw ₹50,000 from Volt Money credit line at an interest of 10.49%. The daily interest rate would be calculated as (10.49% / 365) = 0.0287% per day. If the limit is utilized for 30 days, the interest accrued would be: *Interest = ₹50,000 × 0.0287% × 30 = ₹43.05* You can also make part payments to reduce your principal outstanding and thus reducing your interest payable. **Why Volt money’s overdraft like credit limit is better than a loan?** 1. Flexibility: With Volt money’s credit limit, you only pay interest on the amount you actually use, and you can repay it

---

## #400 — Elevate Cases in LSQ- LAMF
**Status:** Open | **Last edited:** Unknown

# Elevate Cases in LSQ- LAMF: ### 1. **Purpose** To define the business and system requirements for handling **Elevate Cases** in LeadSquared (LSQ). Elevate Cases allow creation of a **new LAMF opportunity** for a borrower even if they already have an won LAMF opportunity with a different lender, enabling **parallel opportunities** under the same borrower account while keeping the opportunity name consistent. ### 2. **Background** Currently, LSQ enforces a “one-active-opportunity-per-lender” rule for each customer, identified by phone number. In *Elevate* scenarios, a borrower who has availed or is availing a LAMF loan from **Tata** or **Bajaj** may now seek a **new LAMF loan from DSP**. The Elevate mechanism ensures: - The **existing opportunity remains untouched**, and - A **new parallel LAMF opportunity** is created for DSP, maintaining full visibility and independent tracking without renaming opportunities. ### 3. **Scope** **In Scope** - Creation of a **new LAMF opportunity** when an existing LAMF opportunity belongs to another lender. - Detection and handling of duplicate opportunities via lender-based exception logic. - Full journey and disposition tracking for both opportunities. - Tagging and reporting visibility for all opportunities per borrower. **Out of Scope** - Changes to standard LAMF journey flow for non-elevate cases. - Changes to lender onboarding or scoring logic. - Non-LAMF product types. ### 4. **Trigger Condition for Elevate Case Creation** An **Elevate Case** is triggered when **all** of the following are true: 1. **Existing Opportunity Check** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = TATA or BAJAJ - Phone Number matches existing record (primary identifier) - Status = WON 2. **New Opportunity Request** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = DSP - Phone Number matches existing opportunity’s phone number 3. **Borrower Account ID Check** - Borrower Account ID ≠ Existing opportunity’s Borrower Account ID If all conditions above are true → **flag as Elevate case** and create a new opportunity with the same name. ### 5. **Functional Requirements** | **#** | **Requirement** | **Description** | | | --- | --- | --- | --- | | 1 | Elevate Case Detection | System should detect when a new opportunity matches Elevate trigger conditions. | | | 2 | Parallel Opportunity Creation | Allow creation of a new LAMF opportunity for a different lender without overwriting existing opportunities. |

---

## #401 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #402 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #403 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #404 — Repeat B2B2C
**Status:** Unknown | **Last edited:** Unknown

# Repeat B2B2C MFD Activation Journey Field Update & Lead Schema Integration ### **Purpose:** To define and manage the set of fields that must be updated post-MFD activation journey completion and ensure these updates are shared with the lead schema for downstream processing by the Repeat team. ### **Scope:** - Capturing required data fields. - Defining when and how these fields are updated. - Updating the lead schema with the captured data. - Triggering opportunity closure upon journey completion. **The following fields need to be replicated in the lead schema:"** 1. MFD Name 2. MFD Phone Number 3. MFD Employee Name 4. MFD AUM 5. MFD ARN 6. MFD Email 7. MFD Activation Date 8. MFD Origin 9. MFD Partner Referral Link 10. MFD Customer Referral Link 11. Referred By 12. Referrer Name 13. Referrer Phone 14. Partner Account ID Additionally, include the list of customers referred so far. 1. All the customer-referred activity must be populated in the lead once activated. **In conclusion, the repeat team can work completely on the lead level, and the MFD activation team can work on the opportunity level** The activities that must be polluted in the lead fields are as follows: 1. Daily partner details update 2. Customer referred 3. Customer loan created

---

## #405 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #406 — Notes Bharat
**Status:** Unknown | **Last edited:** Unknown

# Notes <>Bharat Negotiations table - we will close self-line until we can ensure 1 self-line per partner account. - Rate change, and PF - In tata we can’t change the Rate , so cashback is the option for the Tata. TDS Accounts payable Payment ops Commercials data on the entity - there are three entities applications partner platform that dictate commcials there is a base rate as per the lender that will be assigned by the BRE now once the ROI and PF are assigned to the user then the commencial terms should be added to the application as well on a applciations level we have We have different commercial terms with the on three entity levels application Partner Platfrom the commercials are the the param used to calculate the payout made for the user the Base rate is assigned as per the lender pricing grid of the time of application creation There is default commercials rate that get assigned to Partners and platform by default there are admin actions which assign for a application differenct ROI and PF and the split between the Volt and partner s we are currently not storing the commercials data on the entities level instead its a excel sheet , which casuses issues when calciualting the Solution possible to add object to the right entity that stores he commercials data Application level - ROI - PF - ROI split - PF slip - Base ROI - Base PF Partner level - offer applicable ? - Offer code - ROI - PF - ROI split - PF slip the ROI , PF and splits can be added to the application or to the partner, if added to the partner all the application created by the partner will be assigned the new commercials. Offer code is applied if the applicable. offer can be set of rules like >5 application in the month x = 5000 rs in the payouts Offer has a applicable to and from date the platfrom Platfroms have the similar - ROI - PF - SLITs - Slab based rules the data flow will be 1. application is created 2. assign base ROI and PF from the Lender pricing Grid 3. assign the Application level negotiated Rates collected from Admin actions 4. Assign the MFD commercials as default , then change if changed by the admin action 5. the Platform commercials will

---

## #407 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #408 — Payout Working File
**Status:** Unknown | **Last edited:** Unknown

# Payout Working File Errors earliar - We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured - We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally - We receive GST issues as Customer raise wrong invoices, This is because we don’t provide GST tax invoice to the partners - We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering uploads the data once a month - We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data. - We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date - We need to streamline GST and TDS filing - We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~ list , journey , use case ## Meeting notes - customer - cashback- - previously - partner - platform customer cashback Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49 march 2022. —>23—>24 <may 1st 9.99 9.99 -ROI base rate - 10.49%. 0.5 % cashback on may 1 we changed the base rate for the customer to 10.49% cusotmer cashback , partner to partner Selfline partner payout - MFD - Volt empaneeled MFD - MFD direct - through Software, redvisison or invest well, assest plus , zfunds , - MFD software - affiliates, - Ytbers , - Partner payout - apps like phonepe , jupiter, niyo, part+ - Money is calculated on the Principal outstanding , monthly average daily average, payout is calculated customer wise average POS, eod, for debit-credit sharing percentage with partners - 1. customer —> loan —> 1. credit to borrower 2. Credit to partner 3. Credit to platform 2. partner - volt- 3. upfront - one time payment, rs 200 for opening a account 4. trail income - 0.5 % into POS 5. category —> upfront and

---

## #409 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #410 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #411 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #412 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #413 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #414 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #415 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #416 — Kapture CX
**Status:** Unknown | **Last edited:** Unknown

# Kapture CX - they are connect with incred , phone pe (to be ) ![Screenshot 2024-12-23 at 4.16.58 PM.png](Kapture%20CX/Screenshot_2024-12-23_at_4.16.58_PM.png) - connectors with exotell and other functions - they have customer 360 with all the data that we can send , history , details , txns, - auto QA, for the call summary and interaction quality scoring - 13 years of experience. - Auto translate - Ticket history and summary - solutioning team , —> commercials —> timelines —>

---

## #417 — Analytics Requirement Mandate issues
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Mandate issues Query 1: (errors consolidation, distributed by providor) ```jsx select 'tata' as providor,emandate_error_message as error_message,count(distinct(application_id)) as unique_cases from (select application_id, created_date_time, bank_account_number, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) >= date_add('day', -6, current_date) and mandate_status not in ('In Progress','Finished')) t group by emandate_error_message union all select 'digio' as providor,npci_error as error_message,count(distinct(application_id)) as unique_cases from (select application_id, bank_account_number, created_date_time, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, umrn, case when CAST(JSON_Extract(digio_mandate_response, '$.npci_auth_failed_error') AS VARCHAR) != 'null' then JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') else JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') end as npci_error , CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) >= date_add('day', -6, current_date) and umrn is null and digio_mandate_status!='EXPIRED' and CAST(JSON_Extract(digio_mandate_response, '$.state') AS VARCHAR) != 'expired') t group by npci_error order by 3 desc ``` Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #418 — Analytics Requirement Name verification (TCL)
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Name verification (TCL) Query 1: (errors consolidation, distributed by providor) Total applications initiated (unique) Total Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #419 — API Integration Changes for MFD Migration to LSQ A
**Status:** Unknown | **Last edited:** Unknown

# API Integration Changes for MFD Migration to LSQ Accounts **Document: API Integration Changes for MFD Migration to LeadSquared Accounts** ## **1. Introduction & Goal** This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module. The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner. ## **2. Current API Usage Summary (Pre-Migration)** - **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD). - **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record. - **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*. - **Activity Logging:** - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*. - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*. ## **3. Required API Changes (Post-Migration)** The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked. **3.1 MFD Creation** - **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API. - **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate - **Changes Required:** - Replace API calls creating MFD Leads with calls to the Account creation endpoints. - **Payload Construction:** - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first. - CompanyProperties: Provide an array of Attribute/Value pairs. - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name] - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup). - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" } - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" } - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" } - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field,

---

## #420 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #421 — Term Loan Customer Statements
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

## #422 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #423 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #424 — Term Loan Foreclosure
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

## #425 — Term Loan Manual Repayments(PG)
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

## #426 — Term Loan Manual Repayments(VA)
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

## #427 — Term Loan Prepayments and Excess Handling
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

## #428 — Term Loan Sell off
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

## #429 — Term Loan Unpledge Eligibility API(Post loan creat
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

## #430 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #431 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #432 — MFD Payout Calculation Automation
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout Calculation Automation **Introduction** Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency. 1. we need to handle changing factors like - Monthly Transactions table - Marketing Offers /Referral bonuses - New Platforms additions - Changes in commercials with existing platforms /partners - Changes in base rates / Format - Negotiations with MFDs 2. We need to be able to audit how an amount was generated 3. we need to be able to accrue the credits to an account based on the activity 4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback Problem statements Before base payout calculations - Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing. - We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable. - Attribution of customer to correct Platfrom and partner require manual intervention. - We don’t store the PF and ROI paid by the customer in Credits table. - Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts After the Base payout calculation - TDS rules change and have to accommodate - GST payout are tracked manually Payout process - Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC - For Platform Payouts we need to provide a statement and how the Payout amount is calculated. - Partners have a hard time understanding statements. Potential solutions - Get TATA to improve the API data provided to get the updated transactions - Better fall-back handling on our side Activity activity triggers a

---

## #433 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs

---

## #434 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #435 — Analytics requirement Repayment
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Repayment | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of repayments | (count of total repayments made today) | | | | | | | | | | Number of transactions automatically settled | (count of repayments made and settled today) | yesterday | | | | | | | | | Number of transactions pending settlement | (Count of repayments made today but pending settlement) | | | | | | | | | | Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours | | | | | | | | | | % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) | | | | | | | | | | | | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.collections ### Field: Collections: created_on - When payment was created Collections: settled_on - When payment was settled automatically Payment_status (If equals to settled - payment was settled either using admin action or automatically) ### Table: admin_action_audit (Credits) admin action name: UPDATE_COLLECTION_STATUS To identify which collections were settled manually Format: Email with CSV attached Sample query: ```sql SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*) FROM collections LEFT JOIN credits ON collections.credit_id = credits.credit_id WHERE lending_partner_id = 'Bajaj' AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY AND collection_status not in ('REQUESTED','CANCELLED','FAILED') group by collection_status,CAST(collections.created_on AS DATE) order by 1,2 ``` Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #436 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #437 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #438 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #439 — How banks and NBFCs manage rounding of interest an
**Status:** Unknown | **Last edited:** Unknown

# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases. ## **1. Regulatory & Industry Context** ### RBI Guidelines: RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in: - Customer charging - Auto-debit recovery - Tax invoicing - Reconciliation of ledgers So, banks and NBFCs need to: - Ensure **customers aren’t overcharged** - Match debits with invoices/statements - Maintain proper **audit trail** and **variance accounting** if rounding is applied --- ## 2. Rounding Methods Used by Banks & NBFCs | Type | Common Use Case | Real-world Examples | | --- | --- | --- | | **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs | | **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton | | **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs | | **Cumulative Rounding** | Long tenure loans | Used in housing finance | --- ## 3. Detailed Accounting Treatment by Banks/NBFCs ### **A. Exact Posting (No Rounding)** ### Use Case: - Processing fees + GST - Penal charges ### System Flow: 1. Fee computed: ₹100 2. GST @18% = ₹18 3. Total = ₹118.00 (posted and debited as-is) ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹118.00 | | | Processing Fee Income | | ₹100.00 | | GST Payable (Output) | | ₹18.00 | ✅ Matches invoice and is tax compliant --- ### **B. Round at Posting (Nearest Rupee)** ### Use Case: - Accrued interest - EMI interest - Installment schedules ### Example: - Accrued Interest: ₹199.48 → Rounded: ₹199 - Accrued Interest: ₹199.50 → Rounded: ₹200 ### System Flow: - Round value **at the point of debit** ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹200.00 | | | Interest Income | | ₹199.48 | | **Rounding Reserve GL (Internal)** | | ₹0.52 | > 🔸 If we round down, the 0.52 may be debited to an expense account. > ### Why Rounding Reserve GL? To track small deltas between system-calculated interest and posted amount. ✅ Fair

---

## #440 — Webhook Handling Flow
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

## #441 — PhonePe UPI Autopay Evaluation
**Status:** Unknown | **Last edited:** Unknown

# PhonePe UPI Autopay Evaluation API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization) **List of APIs** 1. Authorization API 1. This API is used to generate the auth token to access the rest of the APIs. 2. The auth token is valid for 1 hour. 3. If the auth token is re-generated within 1 hour, the old token will not expire. - Request ```json curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'client_id=' \ --data-urlencode 'client_version=1' \ --data-urlencode 'client_secret=' \ --data-urlencode 'grant_type=' ``` - Response ```json { "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "expires_in": 3600, "issued_at": 1738669002, "expires_at": 1738672602, "session_expires_at": 1738672602, "token_type": "O-Bearer" } ``` 1. Validate VPA API 1. This API is used to validate the user's VPA. 2. Returns, valid & name of the user. 3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts. - Request ```json { "type": "VPA", "vpa": "nihaltest1@ybl" } ``` - Response ```json { "valid": true, "name": "<Name of User>" } ``` 1. Intent 1. This API is used to create the intent link for autopay. 2. amount - this parameter defines the amount to be deducted at the time of registration. 3. maxAmount - this amount defines the maximum amount the mandate is registering for. 4. Android - Generic intent URI will be provided. 5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app. - Request ```json { "merchantOrderId": "MOTEST5", "amount": 300, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST5", "authWorkflowType": "TRANSACTION", "amountType": "FIXED", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_INTENT", "targetApp": "com.phonepe.app" } }, "deviceContext" : { "deviceOS" : "ANDROID" } } ``` - Response ```json { "orderId": "OMO2502041725138147510236", "state": "PENDING", "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738" } ``` 1. Collect 1. This API is used to send the collect request for mandate setup. 2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported. - Request Body ```json { "merchantOrderId": "MOTEST6", "amount": 200, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST6", "authWorkflowType": "TRANSACTION", "amountType": "VARIABLE", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_COLLECT", "details": { "type": "VPA", "vpa": "nihaltest1@ybl" } } } } ``` - Response ```json { "orderId": "OMO2502041727154877510267", "state": "PENDING" } ``` 1.

---

## #442 — Agreement link not generating for the user
**Status:** Solutioning pending | **Last edited:** Unknown

# Agreement link not generating for the user Classification: Bajaj Agreement Link Notes: Bajaj delay in agreeement, understand why this happened PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13886 Status: Solutioning pending

---

## #443 — Agreement link not generating for the user
**Status:** Solutioning pending | **Last edited:** Unknown

# Agreement link not generating for the user Classification: Bajaj Agreement Link Notes: Bajaj delay in agreeement, understand why this happened PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13888 Status: Solutioning pending

---

## #444 — Bajaj signature was not generating and user was ke
**Status:** In progress | **Last edited:** Unknown

# Bajaj signature was not generating and user was kept in a waiting state Classification: Bajaj agreement link generation Notes: Bajaj callback API for agreement link PRD/Solution mapping: In Progress Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13058 Status: In progress

---

## #445 — Thanks a lot for the explanation Can you also link
**Status:** Solutioning pending | **Last edited:** Unknown

# "Thanks a lot for the explanation. Can you also link to the documentation for this as I couldn't find it directly mentioned in the site, although LLA referenced it. My other query is : The processing fee of 999+GST will be applicable each time I make a withdrawal, or only during the creation of the credit line?" Classification: Processing Fee Notes: User asked if processing fees will be charged every time they make withdrawal, how to ensure this communication is straightforward PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 917005467390 Status: Solutioning pending

---

## #446 — User was given a higher sanction amount than their
**Status:** Solutioning pending | **Last edited:** Unknown

# User was given a higher sanction amount than their credit limit, was able to place a withdrawal request before lodgement was done Classification: Sanction Amount and credit limit handling Notes: Sanction amount instead of credit line amount is shown to the customer before lodgement, ideally withdrawal should be blocked or better communicated, there should be a failed state for all transactions PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13404 Status: Solutioning pending

---

## #447 — User’s pledging failed for Karvy and when they ret
**Status:** Solutioning pending | **Last edited:** Unknown

# User’s pledging failed for Karvy and when they retried, we charged the user processing fee twice without withdrawal - Tata Classification: Karvy pledging issue Notes: Check with Karvy why pledging failed, we should have updated our creditapplication data automatically on pledge failure PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13013 Status: Solutioning pending

---

## #448 — While uploading documents in SDFC KFS got missed
**Status:** Solutioning pending | **Last edited:** Unknown

# While uploading documents in SDFC KFS got missed Classification: Bajaj SFDC document upload Notes: Understand why this happened? How can this be fixed? Can we check status of document upload before moving the customer forward PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13055 Status: Solutioning pending

---

## #449 — Discussion with Rohan (Groww)
**Status:** Unknown | **Last edited:** Unknown

# Discussion with Rohan (Groww) 1. Building in-house after 1 year of operations is recommendable instead of building it in-house from the start 2. VideoSDK has good solution for the video session. 3. Groww built all the in-house cause they were aiming for 4. Hyperverge gives a high amount of false negatives 5. Initially: Success rate → 80% and VKYC completion rate → 70% 6. After spending 2 quarters improving on the Vkyc stack, Success rate → 95% and VKYC completion rate → 80% 7. It is important to store the data correctly and in a reproducible manner. 8. IDfy and Digio are recommended VKYC solution providers 9. Digio uses VideoSDK for their video stack - confirmed 10.

---

## #450 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #451 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #452 — Name
**Status:** Unknown | **Last edited:** Unknown

# Name Column 1: Does it check if the permissions are given? Column 2: Switch On Permission automatically/guide the customer? Column 3: Is Scheduling Available? Column 4: Configure communications for scheduled customers? Column 5: Is Digi Locker Integrated? Column 6: Is Pan Required? Column 7: Does Dashboard have Analytics Available?

---

## #453 — VKYC Vendor Evaluation
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Vendor Evaluation # Evaluation Criteria # Vendor List List of vendors. - Hyperverge - Demo completed (SDK) - IDFy - Perfios - Signzy - Demo Complete (API driven) - Digio - Demo Completed - AuthBridge - Demo Completed - Pixl - Demo not Completed - KYC Hub - Demo Completed # Evaluation ## Summary [Untitled](VKYC%20Vendor%20Evaluation/Untitled%20216e8d3af13a80248558f522cbf900a8.csv) ## Hyperverge ## IDFy ## Perfios

---

## #454 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #455 — Content
**Status:** Unknown | **Last edited:** Unknown

# Content 1. Title: Loan offer 2. Hero details: 1. Selected loan amount. 2. Credit limit available. 3. Benefits: 1. Trusted lender Tata capital 2. Unlimited withdrawals 3. Repay principal anytime 4. Pay interest only on what you withdraw 5. Monthly Interest only EMI of only ₹862 for ₹1,00,000 withdrawal at 10.49% interest (Interest should be communicated upfront) 4. Charges: 1. Interest rates: 10.49% p.a. 2. Early repayment/ foreclosure: Free 3. Withdrawals: within 4 hours 4. One time processing fee (excl. GST): ₹840 1. Processing fee is charged once in the whole term 5. Stamp duty (as per registration state): ₹260 6. Term: 36 months (Renewal available) 5. CTA: 1. Withdraw in 4 steps

---

## #456 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements ![Untitled](Design%20requirements/Untitled.png) ![Untitled](Design%20requirements/Untitled%201.png) 35% users drop off from the loan summary(Verify interest and charges page) Problems we have identified: 1. Users think that this is the last page of the application. 2. Benefits are not properly communicated. 3. User thinks that the PF is too high. Things that we want to communicate with this page: 1. Highlight selected credit limit, remove selected mutual funds: This might be reminding the users that they are pledging alot of MFs for the limit that they are getting. 2. Show maximum credit limit (maybe). 3. Unlimited withdrawals, repay anytime: Communicate benefits. 4. Pay interest only on the amount you use: Communicate benefits. 5. Monthly interest only EMIs, we can show this for 1,00,00 withdrawal and user can change it to see the IOEMI change: This will quantify the interest that they have to pay 1. 10.49% might feel high but IOEMI will be low for default sum of 1,00,000 2. This will communicate that they only have to pay interest on the sum withdrawn 6. Provided by our trusted lender Tata Capital: User trust 7. Highlight zero hidden charges before showing the charges: User should know that we are transparent with our charges. 8. Other details to be in bottom 25% of the screen: [Content ](Design%20requirements/Content%20aa1bb6ecad904d00b07393fa73ff756a.md)

---

## #457 — Market research
**Status:** Unknown | **Last edited:** Unknown

# Market research Benchmarking for Brand, UX, UI, Component usage ### Brand - Understand market standards and common practices - Handling of Trust, Education, Effortless, Supportive - Gaps in competitor offerings ### Component, UI/UX - Use of components - Screen layout - Information architecture - Application of color palette + typography - Icons, illustrations: Use, emphasis - How they deal with complex data visualisation ## Competitors to benchmark 1. Lending apps (LAS, P2P, unsecured, banks, airtel types etc) - Yenmo - Navi - Smallcase - Airtel Finance 1. Credit card apps - Slice - One card - Lazypay - Jupiter - Amex 1. Investment/trading apps Simplicity - Zerodha - Groww - Smallcase Delight - Stable money - Dezerv 1. Modern - design first - Cred - Kiwi --- 1. Audit - Identify inconsistencies | Component | Problem | Action | | --- | --- | --- | | Topbar | - no defined bars for L1, L2, L3 screens - Inconsistent font style, size used | Standardise component types and define use case for each topbar. | | Buttons | - Signup buttons sizing bad - Inconsistent button sizing across screens, modals, journey - Link button component missing - low emphasis buttons missing. | Standardise component types and define use case for each buttons. - Add link button component - Add more low emphasis button components | | Input fields | - Placeholder missing | - Allow placeholder + label - Character count | | Form | - Disabled button: bad ux | - Better validation, error handling | | | | | | Layout | Screen level standardised layouts not defined - inconsistent UI | Define layouts for repetitive scre | 1. Competitor - Color palette used - Type - Layout - Spacing - Shadow, animation, icons - Components (buttons, inputs, modals, cards, etc.) - Visual hierarchy 2. Update palette 3. Update typography 4. Standardize spacing system 5. Redesign components - Buttons - Input fields, Forms - Headers, navigation -

---

## #458 — Detailed scope
**Status:** Unknown | **Last edited:** Unknown

# Detailed scope # Design Language System Documentation A comprehensive guide for Volt Money and DSP Finance ## Table of Contents - [1. Foundation](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#1-foundation) - [2. Components](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#2-components) - [3. Behaviors & Interactions](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#3-behaviors--interactions) - [4. Usage Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#4-usage-guidelines) - [5. Developer Tools](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#5-developer-tools) - [6. Logic & Business Rules](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#6-logic--business-rules) - [7. Platform-Specific Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#7-platform-specific-guidelines) ## 1. Foundation ### A. Design Tokens ### Colors - Primary palette - Secondary palette - Neutral colors - Semantic colors - Success - Error - Warning - Info ### Typography - Font families - Font weights - Size scales - Line heights - Letter spacing - Semantic styles - Headings (h1-h6) - Body text - Labels - Display text ### Spacing - Scale system - Layout spacing - Component spacing - Margin and padding rules ### Borders - Width scales - Radius scales - Styles - Color tokens ### Shadows - Elevation levels - Usage guidelines - Color and opacity ### Motion - Duration tokens - Easing functions - Animation patterns ### Grid/Layout - Grid system - Breakpoints - Container widths - Column configurations ### B. Brand Assets ### Logo - Primary logo - Secondary variations - Clear space rules - Minimum size - Usage guidelines ### Icons - Icon system - Size guidelines - Style guidelines - Usage rules - Icon library ### Illustrations - Style guide - Usage scenarios - Color application - Size guidelines ### Photography - Style guide - Composition rules - Color treatment - Usage scenarios ## 2. Components ### A. Base Components (Atoms) ### Buttons - Primary - Secondary - Tertiary - Icon buttons - States: - Default - Hover - Active - Disabled - Loading ### Inputs - Text input - Number input - Select - Checkbox - Radio - Toggle - States and validation ### Typography Elements - Headings - Paragraphs - Links - Lists - Inline elements ### Icons - Usage - Sizes - Colors - Alignment ### B. Composite Components (Molecules) ### Input Groups - Label + Input - Input + Button - Input + Icon - Validation messages ### Form Fields - Layout - Label placement - Helper text - Error states - Required fields ### Search Bars - Simple search - Advanced search - Filters - Results display ### Navigation Items - Menu items - Breadcrumbs - Tabs - Pills ### C. Patterns (Organisms) ### Forms - Layout patterns - Validation patterns - Submission patterns - Error

---

## #459 — Attribute to question marking
**Status:** Unknown | **Last edited:** Unknown

# Attribute to question marking # Question-Objective Coverage Analysis ## 1. Basic Details & Financial Profile | Questions | Key Insights | | --- | --- | | When and how did you start investing in Mutual Funds? | Investment experience level | | How often do you plan your finances? | Financial management sophistication | | Which banks do you currently have relationships with? | Banking relationships, satisfaction levels | | What tool do you use to track finances? | Financial management approach | ## 2. Behavioral Attributes | Questions | Key Insights | | --- | --- | | Walk me through how you chose that particular fund? | Decision-making style, research habits | | What other investment options did you consider? | Risk tolerance, analysis approach | | How often do you plan your finances? | Planning behavior | | Tell me about the last unexpected expense? | Crisis management style | | What financial apps do you like the most and why? | Technology comfort level | ## 3. Motivations & Goals | Questions | Key Insights | | --- | --- | | What's the next big purchase or investment you're planning? | Financial goals | | What are the various needs or reasons you take loan/credit for? | Loan motivations | | How fast did you need the loan? | Timeline needs | | How long were you willing to take the loan for? | Loan duration preferences | | What's a goal or dream you've been working toward? | Long-term objectives | | Do you hold any preference between asset backed loans and unsecured loans? | Loan type preferences | ## 4. Pain Points & Fears | Questions | Key Insights | | --- | --- | | What part of the process felt most stressful or frustrating? | Process pain points | | What's your biggest concern when considering a loan? | General loan concerns | | Have you ever felt let down by a financial institution? | Trust issues | | What's your biggest concern when considering a secured loan? | Secured loan specific concerns | ## 5. Information Needs | Questions | Key Insights | | --- | --- | | What sources do you rely on for financial research? | Information sources | | Are there any friends, family members, or experts whose financial advice you trust? | Trust

---

## #460 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Pledging will not affect the growth, Financial goal for which you started, long term plan gets hampered, no cibil requirement, Repay any time, Being in control, Reducing interest, Kevin (Servicing): unpledge request 10% buffer, shortfall, bad sell off experience, change in Sanction limit Mahesh: NBFC license, TATA and Bajaj, Names: Trust Naveen: - No brand val - GST india - NBFC license - Lenders

---

## #461 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Process kaise hoga, loan disbursal process, their commission, Referral program Kevin (Servicing): 10% buffer for Bajaj Mahesh: Repayment queries, How is my interest calculated, Stop growing, ownership changed, low ticket sizes, Dont need the loan right now, they want to check limit. Names: Common questions Naveen: - Processing fee channel - Transparency KYC - Fetch and Setting during this time we dont see the interestv or fees

---

## #462 — Hindi Questionnaire
**Status:** Unknown | **Last edited:** Unknown

# Hindi Questionnaire ### Warm-Up Questions 1. Aapne Volt Money ke baare mein kaise suna? 2. Volt ka use karte hue aapka anubhav kaisa raha? 3. Aap kya karte hain? Din lamba raha hoga? 4. Aapne Mutual Fund mein invest karna kab aur kaise shuru kiya? --- ### **Exploring Financial Interests and Habits** 1. Aapne Mutual Fund mein invest karna kab aur kaise shuru kiya? - "Aapne wo particular fund kaise choose kiya?" - "Us samay aapne aur kaunse investment options consider kiye?" 2. Aap apni finances ki planning kitni baar karte hain? - Kya aap ye yearly, monthly, ya daily karte hain? - Iske liye aap kaunsa tool use karte hain? 3. Pichhle kabhi unexpected expense ya financial emergency ke baare mein bataye. - "Aapne isse handle karne ke liye kya kiya?" - "Aapne kaunse options consider kiye?" - "Aapne kaunsa option choose karne ka decision liya aur kyun?" 4. Aakhri baar aapne kisi asset (jaise gold, FD, shares) ka use kab kiya tha? Jaise FD todna, shares bechna, ya Mutual Fund se paisa nikalna? 5. Aap abhi kin banks ke saath jude hain, aur unke saath apna experience kaise rate karte hain? - Aapne XYZ bank ko baaki banks se zyada rate kyun kiya? --- ### Identifying Influences 1. Kya koi kahani, anubhav, ya salah hai jisne aapke loans lene ya financial planning ka tarika badla ho? - Kya koi friend, family member, ya expert hai jinki financial advice par aap pura bharosa karte hain? Kyun? 2. Apne investments, liquidity, aur overall planning ke liye aap kin sources par rely karte hain? 3. Aapko kaunse financial apps sabse zyada pasand hain aur kyun? --- ### Uncovering Motivations and Goals - Maal lijiye ki aapke paas do alag-alag lenders hain. Kaun-si cheezein aapko ek ko dusre se better lagne ka ehsaas karati hain? - Aapka agla bada kharidaari ya investment kya hai? - Aap loan ya credit lene ke liye kin reasons ki wajah se zarurat mahsoos karte hain? - Aapko loan kitni jaldi chahiye hota hai? - Loan kitne samay ke liye lena aapko theek lagta hai? - Koi aisa goal ya sapna jo aap kaafi samay se achieve karne ki koshish kar rahe hain? Yeh aapke liye kitna important hai? - (Kya aisa koi sapna hai jiske liye aap paise jama kar rahe hain?) - Kya aap asset-backed loans aur unsecured loans ke beech koi preference rakhte

---

## #463 — CKYC OTP verify error cases
**Status:** Unknown | **Last edited:** Unknown

# CKYC OTP verify error cases | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | Customer enters wrong OTP | | | | | Resend tried by customer before 90 secs | | | | | Exceeded OTP verify attempts | | | | | | | | |

---

## #464 — CKYC S&D error handling
**Status:** Unknown | **Last edited:** Unknown

# CKYC S&D error handling | **Case description** | CKYC terminal status | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | PAN or Mobile number do not match with the records in Cersai. | | | | | Mobile number doesn’t match | | | | | Mobile number doesn’t exist | | | | | Customer doesn’t exist in CKYCRR | | | |

---

## #465 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements - Complete journey in DSP theme - Do we need a new anchor page on the Volt side? - What will happen in case customer drops off and starts the KYC journey again? - What will happen if the user faces an error in KYC? - Include an optional “Secondary logo”. This will be configured for each LSP - How can we make sure customers enter PAN details as per PAN only? - Add digilocker screens as well in the flow, this will be added in case CKYC fetch is failed - Do we need the KYC successful bottom sheet **Wed 19th March, 2025** - [x] Two sections one for Volt and another for DSP - [x] DSP will have a header as well, LSPs can pass a parameter to show or hide the header - [x] Primary, secondary, tertiary colour change option @Karuna Sankolli - [x] Retry KYC screen, this will be from Volt Side @Karuna Sankolli - [x] Secondary logo pendikng @Karuna Sankolli - [x] Rethink retake selfie flow @Karuna Sankolli - [ ] What will Volt header show when the DSP KYC is in progress @Saksham Srivastava - [ ] Deviation flow will be there or not? @Saksham Srivastava - [x] Jupiter colors @Saksham Srivastava

---

## #466 — NSDL error messaging
**Status:** Unknown | **Last edited:** Unknown

# NSDL error messaging | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | NSDL returns name not matching | | | | | NSDL returns DOB not matching | | | | | NSDL returns | | | |

---

## #467 — DSP Fin Partner Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin: Partner Page # Context RBI requires REs to disclose LSP details in a standard template. While we do the elegant website change, we want to modify only the partners page to be compliant with regulatory requirements. # Requirements As per the RBI guidelines on DLG here, RBI requires REs to disclose the following details. 1. Details of all of its digital lending products and its DLAs; 2. Details of LSPs and the DLAs of the LSPs along with the details of the activities for which they have been engaged for; 3. Particulars of RE’s customer care and internal grievance redressal mechanism; 4. Link to RBI’s Complaint Management System (CMS) and Sachet Portal; 5. Privacy policies and other details as required under extant guidelines of the Reserve Bank. We will display the below details in the current partners page. - Name of LSP - Nature of Service Availed from LSP's - Description of the LSP - DLA of the LSP - Additional Information about the Lender Sample file is attached for reference. [DSPFin Website Disclosures of LSP DLA.odt](DSP%20Fin%20Partner%20Page/DSPFin_Website_Disclosures_of_LSP_DLA.odt) # Benchmarking A few other lenders who display the LSP details are listed below. - InCred: https://incred.com/partnership/ - Piramal : https://www.piramalfinance.com/about-us/lending-partners - BFL: https://www.bajajfinserv.in/bajaj-finserv-partners - ABFL: https://www.adityabirlacapital.com/loans/our-digital-lending-platform-partners

---

## #468 — DSP Fin Website About Us Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin Website: About Us Page **Objective**: To communicate about the values of the company to audience. DSP Finance is a Non-Banking Financial Company (NBFC) backed by the 160+ year legacy of the DSP Group — one of India’s most respected names in financial services. Rooted in trust, innovation, and discipline, we provide customized credit solutions designed to help individuals and businesses unlock value and achieve their financial goals. We are a NBFC with a strong focus on growth through operational excellence and solving problems through technology. **Mission**: To combine deep market expertise with customer-first innovation, ensuring **reliable, transparent, and efficient access to credit** by leveraging technology and robust operational excellence. **Vision**: To be India’s most trusted partner for financial collateral-backed credit, enabling individuals and businesses to unlock value from their investments for exponential financial growth. DSP Finance’s Values. - Customers first - Utmost transparency - People focus - Continuous innovation Key Highlights of DSP finance to be mentioned - AUM of ~2000CR - ~70K customers - 8+ leading partners - AAA rated DSP Finance’s focus is on capital markets led product offerings in the below business lines. - Loan against securities: enabling individuals to leverage their financial assets to get easy access to credit. This page will redirect to the LAS page. - Financial solutions group: providing corporates access to credit by leveraging their assets to get quick access to funds. This page will redirect to the FSG page. DSP Finance works on the below principles. - **Legacy of Trust** – Backed by the DSP Group’s long-standing credibility in Indian finance ecosystem. - **Customer-First Approach** – Transparent processes, no hidden charges, and clear communication. - **Digital-First Experience** – End-to-end paperless solutions with seamless pledge and disbursal. - **Prudent Risk Management** – Strong governance and compliance in line with RBI regulations. - **Expertise & Innovation** – Blend of deep financial knowledge and modern technology to drive deep innovation. DSP has partnered with leading partners to enable customers to leverage their assets. - PhonePe - PayTm - Indmoney - Groww - ETMoney - CRED

---

## #469 — DSP Finance Website About DSP Group
**Status:** Unknown | **Last edited:** Unknown

# DSP Finance Website: About DSP Group DSP finance is part of the broader DSP Group, a leading financial services conglomerate in the capital markets space. DSP Asset Managers Pvt. Ltd. (commonly known as **DSP Mutual Fund**) is one of India’s most trusted asset management companies, managing investments across equity, debt, and hybrid categories. With a strong legacy of over 160 years through the DSP Group, the AMC focuses on long-term wealth creation, prudent risk management, and investor-centric solutions. - The **DSP Group** traces its roots back to the 19th century and has a rich history in Indian capital markets. - In the 1990s, DSP partnered with Merrill Lynch to launch DSP Merrill Lynch Asset Management, which later became DSP BlackRock. - In 2018, the DSP Group bought back BlackRock’s stake, and the AMC was rebranded as **DSP Mutual Fund**. - Today, DSP AMC continues to operate as a 100% Indian-owned asset manager, combining **global best practices** with deep understanding of Indian markets. DSP AMC serves lakhs of investors across the country, offering a diversified suite of mutual fund products to help individuals and institutions achieve their financial goals. Key items to talk about. - AUM of 1.5L CR - Investor base of 50L - Distributor base of 80K+ - 28+ years of investment experience More about DSP AMC can be found at https://www.dspim.com/about-us.

---

## #470 — DSP Finance Website Summary
**Status:** Unknown | **Last edited:** Unknown

# DSP Finance Website: Summary # Positioning We, at DSP Finance, want to be positioned as the ***Most innovative and cutting-edge lender with deep expertise in capital markets.*** - We want to stand out from the crowd as a new-age and customer-friendly lender - We want to stand out from traditional lenders (BFL, TCL) - We want to standout as a specialist lender in the capital markets # Branding We at DSP finance will continue to maintain the DSP brand themes (Colors). That said, we also want to have an independent identity. - Branding to reflect our identity as a new-age lender - Common color schemes as DSP group - Different iconography compared to DSP group # Layout Below are the pages for the new website. - Homepage **Objective**: This page will talk about DSP Finance at a high level to instill confidence in the visitor. **Hero Section –** Innovation at core**.** - **Headline:** *“India’s most innovative lender in the securities space.”* - **Sub-headline:** “A seamless bouquet of credit offerings built on a deep understanding of customers, enabled through cutting-edge technology” - Our partners: Band of existing LSP partners we have. - CTA: *“Explore Partnership”* | *“Request a Call Back”* **Overview section** - India’s leading LAFA player. - DSP Finance helps individuals & businesses unlock the value of their securities seamlessly. - DSP Finance, which is part of the DSP Group is the fastest growing digital lender in the space. - AUM - Rating - Customers **Offerings section** - Our product suite - **LAFA**: Liquidity at the finger-tips against financial securities spanning mutual funds and securities. Redirects to the product page. - **FSG**: Tailored solutions for businesses looking to unlock their business potential by leveraging their financial assets. Redirects to the product page. **DSP Advantage** - Our USP. - **Industry Expertise**: DSP Finance brings to the table, unparalleled expertise and business understanding of capital markets & Securities space. - **Technology First**: DSP Finance offers customers and partners the ease of leveraging technology for superior experience. - **Product Suite**: DSP Finance has the entire suite of products in the financial securities space to suit the needs of individuals and businesses. - **Transparency & Trust**: DSP Finance has very clear and easy to understand fees and charges, backed by the legacy of DSP Group. **FAQs -** Answering questions. **Testimonials** - Building trust in customers. - About Us **Mission & Vision -** Context

---

## #471 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #472 — NBFC B2B LSP API List
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : API List - Pledge API on DSP - pending - Fetch API on DSP - pending - Submit opportunity - create account - Mobile & Email update - no verification - Add verification timestamp for mobile & email - KFS & Agreement: we might have to decouple and make KFS pass the response in parameters - Offer API on DSP - LSP passes back the confirmation to DSP - PAN verification - LSP not required to integrate -

---

## #473 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #474 — NBFC LSP Stack GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC LSP Stack : GTM Below are the GTM phases of the LSP stack. | Phase | Objective | Partner/s | Number of applications | Timeframe | | --- | --- | --- | --- | --- | | Phase 1 | To augment the existing DSP capabilities into APIs to validate the stack a small scale | 1-2 | 100/day | 30 days | | Phase 2 | To build fall-back capabilities for each part of the journey to handle scale | 3-4 | 500/day | Ongoing | | Phase 3 | To build term loan capabilities over and above the current offerings for newer partners | | | TBD | | | | | | |

---

## #475 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are

---

## #476 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #477 — Invoice & Payment Process
**Status:** Unknown | **Last edited:** Unknown

# Invoice & Payment Process # Challenges Currently, Volt and its NBFC partner, DSP works with multiple partners spanning SaaS and bank partners for multiple tech related services. Most of these vendors work on postpaid model where they invoice us on a monthly level. This results in multiple challenges. - Dependencies on key people (Lalit, Ankit) to approve each invoice - Delay in processing payment resulting in bad experience for vendors - Possibility of not paying the right amount due to lack of reconciliation - Poor support from partners due to delayed payment processing The primary reason for the same is a lack of a documented process. # Solution

---

## #478 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #479 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #480 — Referral Product Note
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and program

---

## #481 — Referral Product Note [Claim approaches]
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note [Claim approaches] ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility

---

## #482 — User Story template
**Status:** Unknown | **Last edited:** Unknown

# User Story template # Guidelines **How should user stories be written?** - Each user story should be atomic — focus on one activity or action. - One feature needs to have multiple user stories for each activity. - For the UPI mandate registration feature, this will be: - Context page. - Mandate registration page. - UPI registration (TPAP). - Post-registration confirmation. - Retry or fallback, if required. - Each user story should be written from a user/customer perspective. - Users can be internal users like sales, support, or operations OR - User can be customer OR - User can be a partner (B2B or LSP) - User stories should document key scenarios and how they will be handled from a UI/UX perspective. - For the UPI mandate feature, this will be: - Mandate registration is pending due to user inactivity. - Mandate registration failure due to user error. - Mandate registration failure due to technical issues. - Mandate registration success. - Delayed confirmation handling. # Template Below is a template for User Stories. - **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc. - **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve. - **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement. # Example Below is a list of User Stories keeping UPI mandate registration as an example. - **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate. **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate). **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey. **Requirement**: Below are the requirements for this page. - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest. - This will be a common page that will cover both NACH and UPI mandate. - This page will describe that customer’s bank account will