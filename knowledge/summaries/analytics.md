# Current State: Analytics

> Auto-generated from 464 PRD(s). Most recently edited shown first.


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

## #3 — Update MFC limit in application - from API and lan
**Status:** Not started | **Last edited:** September 3, 2024 4:07 PM

**Problem:**
are we solving?**

Currently for B2B partners where we allow MFC fetch and RTA pledge:  Once customers checks MFC limit on their platform and logins into the SDK, the limit is not refreshed upon refreshing the limit on partner platfomrs. 

---

**Solution:**
?**

---

## #4 — PRD - Handling MF Central CAS Summary API fields r
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

## #5 — Manage Limit Error messaging handling
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

## #6 — [Lending stack] KFS
**Status:** Not started | **Last edited:** September 22, 2024 8:38 PM

**Problem:**
are we solving?**

Scope of the problem:

1. Content of the KFS should be user friendly and make the user understand key terms and construct of the product.
2. How will RE share the values which will enable LSP to render the KFS
3. How will LSP render the KFS (design)
4. How will LSP capture consent from the customer?
5. How will LSP share consent with the RE?
6. How will RE store this consent?

---

**Solution:**
?**

---

## #7 — Loan Offer Optimisation experiment for CheQ
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

## #8 — BAJAJ GetMilesAccountDetails
**Status:** On Hold | **Last edited:** September 2, 2024 11:37 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #9 — Bajaj PAN verification API
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

## #10 — TATA compliance requirement - 30th August 2024
**Status:** In progress | **Last edited:** September 19, 2024 4:06 PM

**Problem:**
are we solving?**

Compliance issue for TATA

---

**Solution:**
?**

---

## #11 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #12 — MF Pledge optimizations
**Status:** In progress | **Last edited:** September 16, 2024 8:23 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #13 — DSP - Integrated KFS & Agreement Flow
**Status:** Not started | **Last edited:** September 16, 2024 11:47 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #14 — [Lending stack] Agreement customer signing - Leega
**Status:** Not started | **Last edited:** September 12, 2024 9:30 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #15 — Optimizing disbursement metrics
**Status:** In progress | **Last edited:** September 12, 2024 4:44 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #16 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** September 11, 2024 8:14 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #17 — Product Brainstorming & Research Process
**Status:** In progress | **Last edited:** September 11, 2024 7:49 PM

**Problem:**
are we solving?**

PMs currently are maintaining all the workflows outside Jira or any tool on Notion and sheets. This is creating a massive challenge in tracking of activities, features, etc resulting in multiple sync calls/meetings, etc. at multiple stages like pre-sprint as well as at the time of sprint planning.

In addition, a lot of the pre-development activities like stakeholder sign-off, problem review, solution review, etc are maintained offline or on sheets. This results in sub-optimal outcomes for the Product team as well as stakeholders.

---

**Solution:**
?**

---

## #18 — Streamlining Support Communication by Segregating
**Status:** In progress | **Last edited:** September 11, 2024 4:31 PM

**Problem:**
are we solving?**

- The support inbox(support@voltmoney.in) is comprising customer issues and automated system notifications regarding pledge configuration, SFDC creation, Pledge failure and Pledge confirmation
- This clutter makes it difficult to efficiently manage and prioritise genuine customer queries.
- As a result, our ability to respond quickly and effectively to customer issues is compromised.

---

**Solution:**
?**

---

## #19 — User getting stuck at KYC verification step in cas
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

## #20 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #21 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #22 — LSQ Revamp Solution Doc
**Status:** Not started | **Last edited:** October 6, 2025 12:50 PM

**Problem:**
are we solving?**

Currently, both the **MFD activation journey** and the **customer LAMF journey** run through a **single combined flow**, which is leading to multiple challenges:

- Difficult to manage MFDs handling multiple applications/customers
- Limited ability to manage multiple products at the customer level
- Workflow and opportunity overlaps and causing confusion
- Lack of clarity on which opportunity belongs to which journey
- Inadequate visibility into MFD vs. customer progress tracking
- **Phone number as the primary identifier creates a constraint** — if an MFD and a customer sha

**Solution:**
?**

---

## #23 — MFD Partner Servicing revamp
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

## #24 — TATA KFS and Agreement Phase 2
**Status:** In progress | **Last edited:** October 24, 2024 10:46 AM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge.

---

**Solution:**
?**

---

## #25 — [Lending stack] Welcome mail
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

## #26 — DSP communication email template
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

## #27 — MFD Payouts
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

## #28 — [Lending stack] DSP lender assignment logics
**Status:** Not started | **Last edited:** October 18, 2024 11:01 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #29 — Change in audit trail flow for PAN Validation API
**Status:** Pending Review | **Last edited:** October 17, 2024 8:05 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details (POV=null), the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

---

## #30 — Withdrawal Optimisations
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

## #31 — Data and Metrics for NBFC Stack
**Status:** Not started | **Last edited:** October 16, 2024 5:59 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #32 — LOS and LMS admin actions (LSP with DSP as lender)
**Status:** In progress | **Last edited:** October 16, 2024 2:25 PM

**Problem:**
are we solving?**

We have developed multiple admin actions (ops controlled actions) that help in servicing our customers in the onboarding as well as the servicing journey. 

This requirement covers utilising the admin actions (where needed) to cover use cases currently served by LSP (for customers) with DSP as a lender.

---

**Solution:**
?**

---

## #33 — Bulk email automation
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

## #34 — Integrated Sales tool
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

## #35 — Simplify B2B Partner Redirection Journey
**Status:** In progress | **Last edited:** October 11, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #36 — API and Transaction Logging
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

## #37 — Name storing from different sources
**Status:** Not started | **Last edited:** October 11, 2024 11:26 AM

**Problem:**
are we solving?**

Currently, we don’t store user names from different sources (PAN, Aadhar, Bank) in a structured, queryable format. This leads to inefficiencies during analysis and debugging, as names must be individually retrieved from writing query for each source through Amazon CloudWatch, resulting in increased latency.

---

**Solution:**
?**

---

## #38 — DSP MFD Flows
**Status:** Not started | **Last edited:** November 9, 2024 5:28 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #39 — Excess amount handling
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

## #40 — Mandate Set up optimisation - Error Messaging + Ne
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

## #41 — Lien removal SLA tracking report
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

## #42 — Repayments Error Handling and Changes
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

## #43 — Lodgement decoupling from enhancement
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

## #44 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #45 — Father’s name validation removal
**Status:** Not started | **Last edited:** November 30, 2025 12:18 PM

**Problem:**
are we solving?**

LSPs are currently seeing high rejection rates at the **Submit Opportunity** stage due to mismatches between the user-entered *father’s name* and the value returned from KYC.

Since the RBI’s KYC Master Directions do **not** mandate verification of the father’s name—and it is required only for CKYC reporting—strict validation is unnecessary. Most regulated entities rely on customer-provided details with minimal checks, which aligns with our revised approach.

---

**Solution:**
?**

---

## #46 — Periskope
**Status:** In progress | **Last edited:** November 29, 2024 1:55 PM

# Periskope [Periskope to wati plan ](Periskope/Periskope%20to%20wati%20plan%2014ce8d3af13a80849cf2d1d5e048585e.md) ### Current Challenges: 1. **Limited Tracking**: We cannot effectively track incoming chats or their resolutions due to limitations in Periscope. 2. **Chat Status Visibility**: There is no visibility into chat statuses (e.g., open, resolved, work-in-progress). 3. **Active Chat Monitoring**: We cannot determine how many chat groups are currently active or were active in the last week. 4. **Categorization Issues**: There's no way to identify whether chats are related to sales or service. 5. **Chat Volume**: We receive around 100 chats daily. This a 6. **Lack of Bulk Chat Download**: Periscope does not offer a bulk download feature for chat records. 7. **Response Time (TAT)**: We are unable to track response times or resolution times for chats. 8. **Agent Tracking Issues**: Agents lose track of ongoing chats as new chats push older conversations to the bottom of the queue, making it difficult to manage multiple conversations. 9. **Limited Team Capacity**: Only two people manage Periscope at a time, which limits our ability to handle high chat volumes effectively. 10. **No Chat Closure Mechanism**: There is no way to close chats or mark them as resolved. 11. **Unclear Analytics**: Terms such as "daily message counts" and "flagged messages" lack clear definitions and explanations. 12. **Ticketing Process**: The process for raising tickets is unclear to the team. 13. **Unavailability of RM (Relationship Managers)**: If an MFD reaches out and the assigned RM is unavailable, another agent is assigned to Periscope to manage the chat. 14. **Periscope and WATI Integration**: While all MFDs are connected to Periscope, they are not added to WATI, leading to inconsistencies in communication channels. 15. **Missed Chats**: Missed chats often go unnoticed until they escalate, as there is no way to flag or track missed communications in real time. ## Visibility There are three visibility that we need. - Visibility on Chat messages - Visibility on the issue resolution - Visibility on the Impact of the Providing support Table 1: Visibility on Interactions with MFD Partners | Metric | Description | Current | Wati (option 1 ) | Suggested | | --- | --- | --- | --- | --- | | Total Interactions | Number of interactions with MFD partners | Tracked in Periskope | | | | Call Volume | Number of calls between RMs and MFDs | exotell | | | | Chat Volume | Number of chat conversations

---

## #47 — LSQ misattribution b2c of B2b2c data
**Status:** Ready for Tech | **Last edited:** November 27, 2024 11:25 AM

# LSQ misattribution b2c of B2b2c data # B2C to B2B2C Lead Update Specification ## Background When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues: 1. Lead tracking inefficiencies 2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams) 3. MFD partner dissatisfaction with direct customer contact ## Objective Reduce misattributed leads - Reduce Creation of the new Misattributed leads. - Update LSQ with admin action (tech pickup) - Backfill data to correct misattribution Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database. ## Technical Implementation ### API Details - **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate) - **Identifier**: Mobile Number (unique in LSQ) ### Required Field Updates ```json { "LeadDetails": [ {"Attribute": "mx_Channel", "Value": "B2B2C"}, {"Attribute": "Source", "Value": "MFD Referral"}, {"Attribute": "mx_Referred_By", "Value": "MFD"}, {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"}, {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"}, {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"}, {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"}, {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"}, {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"}, {"Attribute": "SearchBy", "Value": "Phone"} ] } ``` ## Data Migration Plan ### Initial Data Reconciliation - Tech team to provide excel export of leads updated via admin actions - Data to be shared with LSQ team for backfill - Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count) ### Scope Limitations - Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ - Focus on forward data synchronization and provided historical data only ### MFD Status Handling - Automated daily updates for partially-activated MFD status ## Requirements ### Technical Requirements 1. Admin action implementation for borrower-partner relationship updates 2. API integration with error handling 3. Comprehensive update logging for audit purposes ### Acceptance Criteria 1. Successful lead type transition (B2C to B2B2C) 2. Accurate referrer information mapping 3. Proper API response handling 4. Complete audit logging 5. Visual verification in LSQ dashboard ## Important Notes - Mobile Number serves as the unique identifier in LSQ - Lead merges occur when same email is used with different phone numbers - Implementation must include robust error handling for API failures - API failures should be notified to the team.

---

## #48 — TCL Credit Referral Automations & optimisations
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

## #49 — Volt B2B Redirection Enhancement - Park+
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

## #50 — QC rejection flow handling for DSP - Volt LOS
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

## #51 — New Posidex report template
**Status:** In progress | **Last edited:** November 20, 2024 4:54 PM

**Problem:**
are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

**Solution:**
?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

---

## #52 — TCL getDisbursementAPI logic updation
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

## #53 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #54 — NBFC LSP APIs
**Status:** Not started | **Last edited:** November 15, 2024 6:47 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #55 — External reporting requirements
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

## #56 — White-labelled Redirection Journey for B2B Partner
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

## #57 — Enhancement optimization
**Status:** In progress | **Last edited:** November 14, 2024 7:21 PM

**Problem:**
are we solving?**

- For the customers whose DP is significantly less than sanction limit when try to enhance (pledge more funds) such that there sanction limit does not get updated then user are not given information

---

**Solution:**
?**

---

## #58 — KYC Risk Status (NBFC Platform)
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

## #59 — MFC Summary API calculations update
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

## #60 — Repayment failure handling
**Status:** In progress | **Last edited:** November 12, 2024 1:14 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

---

## #61 — MFD Tier & Performance Data Activity Passing in LS
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

## #62 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #63 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #64 — PhonePe Contact support changes - 12th April 2024
**Status:** Not started | **Last edited:** May 6, 2024 9:14 AM

**Problem:**
are we solving?**

1. PhonePe has sent a requirement to stop lead leakage due to Volt support number available on the landing page. 
2. Number of junk inbound calls has increase 4x

---

**Solution:**
?**

---

## #65 — DSP KFS & Agreement for LSPs
**Status:** In progress | **Last edited:** May 5, 2025 5:36 PM

**Problem:**
are we solving?**

Currently, a lot of the LSPs don’t want to showcase DSP 

---

**Solution:**
?**

---

## #66 — PhonePe press release - 30th May 2024
**Status:** Not started | **Last edited:** May 30, 2024 10:11 AM

**Problem:**
are we solving?**

Creating a static landing page for PhonePe press release due to release on 30th May. 

---

**Solution:**
?**

---

## #67 — Custom Comms based for Ad-hoc situations v2
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

## #68 — Sell-off Repayment Reconciliation — Maker Automati
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

## #69 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #70 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #71 — [DSP] Additional customer comms (compliance)
**Status:** In progress | **Last edited:** May 28, 2025 12:27 PM

**Problem:**
are we solving?**

Sending additional comms to users to comply with DLG and internal compliance requirements. 

---

**Solution:**
?**

---

## #72 — PRD - B2C Referral [Phase-1 1]
**Status:** In progress | **Last edited:** May 27, 2026 4:29 PM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new us

**Solution:**
?**

---

## #73 — STP validation for Sell-off Repayment Reconciliati
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

## #74 — PRD – Volt MFD Payouts Process
**Status:** In progress | **Last edited:** May 27, 2025 2:52 PM

# PRD – Volt MFD Payouts Process # **PRD – Volt MFD Payouts Process** ## **1. What Problem Are We Solving?** ### **Key Issues Identified** 1. Business continuity risk as we are too dependent on one analyst for the calculations 2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~ 3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries. 4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts. 5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed. 6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS). 7. **Support Visibility:** No centralized tracking for payout-related support issues. 8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files. 9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails. 10. **GSTN Verification:** No automated verification of correct GST numbers. --- ## **2. Changes needed for Payout automation (Current vs. Proposed)** | Database | Current | Proposed | | --- | --- | --- | | Application Data | DB | No change | | Transaction Data | DB | No change | | Principle Outstanding | Google Sheets | DB | | Partner Commercials | Google Sheets | DB | | Payout Ledger Table | Google Sheets | DB | | Account Payable (AP) | Not tracked | DB | | Base Payout Calculations | Google Sheets | DB | | GST & TDS Calculations | Google Sheets | DB | | Payout & GST Invoice | Google Sheets | DB | | GST Tax & TDS Filing | Google Sheets | DB | | Bank Account Data | Manual Check | DB | | Payout File to Bank | Excel | API | | Payout Payment Status | Statement | API | | Reconciliation & UTR Backfill | Google Sheets | DB | --- ## **3. User Needs** ### **MFD / Partner** - Expect accurate, on-time payments. - Need clear payout breakdowns, including GST invoices. - Require an easy way to highlight and resolve discrepancies. - Want Volt to handle tax filings accurately. - Prefer a payout experience similar to top AMCs. ### **Business Team** - Aims to improve MFD service by resolving payout issues efficiently.

---

## #75 — Migrating MFD Partners to the LSQ Accounts
**Status:** Ready for Tech | **Last edited:** May 27, 2025 2:25 PM

# Migrating MFD Partners to the LSQ Accounts [**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md) - Accounts are now enabled for org: volt - Reading LSQ documentation to understand and create a transition plan - MFD is currently treated as lead and should be moved to accounts - RMs will be assigned accounts and will be responsible for its success - All the customer of a MFD will be under their account - **1. Purpose & Goal:** - **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data. - **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads. - **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership). **3. Procedure:** **Phase 1: Configure the Accounts Module for MFDs** Setting up the Accounts entity for MFDs - **3.1 Identify Required MFD Fields:** - Review the current Lead fields list - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples: - PAN - ARN No - Referral Code / Partner Code - Partner Referral Link - Partner Type - Platform / Platform Id - Empanelment Date - Company (if used for MFD firm name) - Key contact details (Email, Mobile Number, Address, City, State, Zip Code) - Ownership (Owner) - Any other relevant custom fields. - **3.2 Create Custom Account Fields:** - Adding all the Lead files to account - For every required MFD field *not* present by default in Accounts, create a custom field: - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions - Click **Add**. - Define: - **Display Name:** - **Schema Name:** format cf_display_name. custom field for easy reference - **Field Type:** Match - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/) - 3.3 Add Drop-downs in fields like stage, etc. **Phase 2: Migrate MFD Data from Leads to Accounts** - **3.4 Extract MFD Leads:** - Manage leads - Use **Advanced Search** Lead Type != MFD - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**. - **Export:** Select Actions -> Export Leads -> Export as CSV. - **3.5 Prepare the Import File

---

## #76 — CAMS min_unit Validation for LAMF Lien Transaction
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

## #77 — Handling LOS Application Rejections
**Status:** Not started | **Last edited:** May 25, 2026 12:22 PM

**Problem:**
are we solving?**

Currently in LOS , several business-critical validation checks are performed — such as client deduplication, MNRL checks, and AML/PEP screenings. 

However when any of these checks fail, the system surfaces a generic ‘declined’  error message (”Something went wrong”) to the user. The root cause is that the backend does not propagate the specific error code or reason to the frontend, so the frontend cannot render contextual, actionable error screens.

---

**Solution:**
?**

---

## #78 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** May 24, 2026 11:40 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #79 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #80 — LSQ Chat workflow - Phase 1
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

## #81 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #82 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #83 — PRD MFD Performance Metrics & Earnings Display
**Status:** Not started | **Last edited:** May 21, 2025 12:46 PM

# PRD: MFD Performance Metrics & Earnings Display ## **1. Introduction** This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show: - Their sourced **MF Loan AUM** - Applicable **trail income rate** - **Trail income earned** - **Account opening bonuses** The goal is to make it simple for MFDs to understand how their efforts are driving their earnings. --- ## **2. Goals & Objectives** ### **Primary Goal** To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives. ### **MFD User Objectives** - Understand how MF Loan AUM translates into income or Increase visibility to the MFDs - Track progress toward higher income tiers - See a breakdown of earnings and new account bonuses - View historical trends and performance ### **Business Objectives** - Encourage MFDs to grow MF Loan AUM - Boost Volt Money customer acquisition - Reduce support queries about commissions ## **Success Metrics** - MFD Monthly visits to partner portal - MFD Repeat rate - MFD Avg number of applicaitons per month - upward move in MFD LAMF AUM Buckets --- ## **3. User Stories** - *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier. - I want to know my current trail income rate based on slabs. - I want to see how close I am to the next earning tier. - I want to track monthly/quarterly/yearly trail income. - I want to verify bonuses for each new LAMF line opened. - I want a full summary of earnings: trail income + bonuses. - I want to view historical performance trends. - I want to quickly reference the trail income slab table. --- ## **4. Feature Breakdown & UI/UX** ### **4.1 Main Dashboard: Volt Money Performance Overview** **Key Metrics:** | Metric | Example | Tooltip | | --- | --- | --- | | **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money | | **Trail Rate** | 0.55% | Based on current AUM slab | | **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. | | **New Accounts (MTD)** | 5 | From Onboarding CRM | | **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts | | **Total Earnings (MTD)** | ₹58,291 |

---

## #84 — Enhancement Of STP NSTP validations for Bulk sell
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

## #85 — Lodgement STP optimisations
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

## #86 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #87 — Consent Architecture FE requirements
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

## #88 — Phase 0 LTV update to 70 (servicing)
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

## #89 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #90 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #91 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #92 — Enhanced Customer Registration & Deduplication for
**Status:** Done | **Last edited:** May 12, 2025 12:46 PM

# Enhanced Customer Registration & Deduplication for MFDs **Enhanced Customer Registration & Deduplication for MFDs** ### **Problem** 1. MFDs often hit blockers or need RM support when trying to register customers who already exist in Volt’s system (e.g., as B2C users, under another B2B partner, or with active loans). 2. The current error message—“Failed to register customer”—is vague and doesn’t guide the MFD on what to do next based on the type of duplicate. 3. There were 1,200 such error on MFD portal. ~50% of the registered TOFU. and 185 admin actions to Map partners ### **Goal** - Simplify the customer registration journey for MFDs, especially in common duplicate scenarios. - Reduce RM dependency, particularly for B2C linking. - Provide clear, actionable feedback to MFDs when a duplicate is found. ### **Proposed Solution: Automat** When an MFD submits “Register Customer” with Name, Mobile, and: ### 1. **Backend Deduplication Check** - Use Mobile and to detect existing customer records. ### 2. **Modal-Based Responses Based on Scenario** - **A. New Customer (No Prior Account)** - **Action:** Add customer —> OTP - **UI:** No modal or interruption. - **B. Customer Exists as B2C (Registered directly on Volt)** - **Modal Title:** *Customer Found in Volt* - **Message:** “This customer is already registered directly with Volt. To add them to your portfolio, OTP verification is required.” - **CTAs:** - “Send OTP & Add Customer” (launches OTP flow) - “Cancel” - **C. Customer Linked to Another Partner or Has Active Application** - **Modal Title:** *Customer Already Registered* - **Message:** “This customer ([Name or Masked ID]) is already registered with Volt and may be linked to another partner or have an active application/loan. Please contact your RM for support.” - **CTA:** “Okay” (returns MFD to form) - **D. Typo/Error in Initial Input (Pre-dedupe)** - If the MFD catches a mistake before dedupe runs (e.g., wrong PAN), allow them to use the existing “Edit details” button. - Once dedupe identifies a match, scenario-specific modals override the generic error message. ### **Key Requirements** - Backend API for robust deduplication using PAN/Mobile. - API must return customer status: - Not found - Existing B2C - Linked to another partner - Active loan/application - Dynamic modals based on API response. - OTP flow for linking B2C customers to MFDs. - Clear attribution/commission logic for B2C linking. ### **Benefits** - Fewer MFD drop-offs and RM escalations. - Seamless onboarding for B2C customers

---

## #93 — Term loan CC enhancements
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

## #94 — DSP PhonePe PG Integration for PhonePe
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

## #95 — MFD Payout Process Revamp
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

## #96 — LSQ KT
**Status:** In progress | **Last edited:** March 7, 2025 11:34 AM

# LSQ KT LSQ is used to enable sales to efficiently increase conversion rate The goal is to provide agents with a Customised view for them to take actions - Customer - Platforms —> Mobile number + otp —> registered - Fetch —> Limit if limit is > 10k Eligible ,we send them to LSQ - In LSQ we create Leads and Opportunity

---

## #97 — [Volt LSP] Supporting multiple products for same c
**Status:** Not started | **Last edited:** March 5, 2025 6:06 PM

**Problem:**
are we solving?**

Immediate problem: 
BFL has stopped new applications (Including enhancement) with Volt. Current customers who want to enhance their credit line are not able to do so. To solve their need of enhancing their credit limit we are thinking of a dual credit line solution where the customer will open a new credit line with DSP and the existing credit line from BFL/Tata will remain active. 

---

**Solution:**
?**

---

## #98 — [IronGrid] Email trigger for ops in case of disbur
**Status:** Not started | **Last edited:** March 31, 2026 8:24 AM

**Solution:**
?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

---

## #99 — [Volt LSP] CAS summary and detailed POC
**Status:** Not started | **Last edited:** March 31, 2025 6:14 PM

**Problem:**
are we solving?**

- MFC CAS summary API, required for

---

**Solution:**
?**

---

## #100 — [Volt LSP] Volt LOS Journey 2 0
**Status:** Not started | **Last edited:** March 31, 2025 5:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #101 — [Volt LSP] Biometric cases
**Status:** Not started | **Last edited:** March 3, 2025 5:55 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #102 — [Volt LSP] Integrating DSP KYC
**Status:** Not started | **Last edited:** March 3, 2025 2:38 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #103 — [Platform] Foreclosure handling and enhancement
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

## #104 — PN Storing Commercial Data at Credit Level
**Status:** Pending Review | **Last edited:** March 3, 2025 12:37 PM

# PN: Storing Commercial Data at Credit Level ## Problem Statement Currently, we do not store Platform-level commercial data directly at the Credit level. Instead, this data is maintained in external Excel sheets, which creates inefficiencies in the payout calculation process. The data team must manually add these commercial details when creating payout files, resulting in: - Increased processing time - Higher risk of manual errors - Difficulty in data reconciliation - Lack of data integrity between systems ## Proposed Solution Implement a dedicated commercial data object at the Credit application level that will store all relevant commercial parameters at the time of application processing. ## Key Data Points to Store The Credit level commercial data object should include: - **Lender**: The financial institution providing the loan - **Base ROI**: Original interest rate from lender pricing grid - **Base PF**: Original processing fee from lender pricing grid - **PF Split**: Processing fee revenue distribution between platform and partners - **ROI Split**: Interest revenue distribution between platform and partners - **Payout Amount PF**: Calculated processing fee payout amount - **Payout ROI**: Calculated interest-based payout amount ## Implementation Benefits 1. **Data Integrity**: Single source of truth for commercial terms at the application level 2. **Audit Trail**: Historical record of commercial terms applied to each application 3. **Streamlined Reporting**: Direct data access for reporting without manual intervention 4. **Efficient Payout Processing**: Automated payout file generation based on stored values 5. **Reduced Manual Effort**: Elimination of manual data enrichment processes ## Considerations - Create a new data structure to store commercial data as part of the credit application object - Implement data validation to ensure complete commercial information - Add timestamp and user attribution for commercial data changes ## Example data table | **S_No** | **Platform** | **Type** | **Tata Interest base rate** | **Bajaj Interest base rate** | **DSP Interest base rate** | **Tata PF base rate** | **Bajaj PF base rate** | **DSP PF base rate** | **PF Sharing** | **Trail Sharing** | **PF Sharing %** | **Trail Sharing %** | **Comments** | Signoff | Actionable | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 1 | Advisorkhoj | Partner | | | | | | | | 0.5 | | | | | | |

---

## #105 — BharatPe changes
**Status:** In progress | **Last edited:** March 28, 2024 7:26 PM

**Problem:**
are we solving?**

For our B2B partner BharatPe we are making a few changes to make the post loan application journey for the user as smooth as possible.

---

**Solution:**
?**

---

## #106 — Custom Comms based for Ad-hoc situations
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

## #107 — Revocation Status API
**Status:** In progress | **Last edited:** March 24, 2025 6:08 PM

**Problem:**
are we solving?**

- Un-pledging requests are processed by polling the holding statement to check if the lender has released the funds. However, if the Drawing Power (DP) isn't updated within 4 days, the status remains "In-progress" rather than automatically resolving.
- Ops teams have to manually update the un-pledging status by referring to the Lien report when the DP isn't updated, adding manual effort.
- Dependence on the Lien report is inefficient since it is often delayed by the lender, causing further delays in updating the un-pledge status.
- The current method of indirectly tracking u

**Solution:**
?**

- Implement a direct integration with the GetReleaseStatus API to retrieve the un-pledging status without relying on the get holding statement or Lien report

[Release Status.docx](Revocation%20Status%20API/Release_Status.docx)

[RevocationRequestStatusAPI.docx](Revocation%20Status%20API/RevocationRequestStatusAPI.docx)

---

## #108 — Lien status lifecycle tracking
**Status:** In progress | **Last edited:** March 23, 2025 9:16 PM

**Problem:**
are we solving?**

- Users keep seeing the notification on dashboard till it is not removed via admin action.
    - Once a request was raised manually to the lenders, and the selected folio is unlodged from the account, there is little to no visibility to volt on the status of unpledging.
    - Since this is shown to the user when they login, it creates an urgency in the user’s mind regarding their pending request.
- Users are not communicated the steps and the involved stakeholders to complete their unpledge request.
    - This makes the user think that Volt is responsible for the end to end 

**Solution:**
?**

<aside>
⚠️ Users keep seeing the notification on dashboard till it is not removed via admin action.

</aside>

We will change the discovery of pending unpledge request from dashboard to pledged portfolio discussion to make it less apparent and more contextual for the user.

- Only users who want to track their pledged portfolio would discover the notification and can act on it accordingly.
- User will be able to close their unpledge request once all necessary steps are made and communicated to the user.

<aside>
⚠️ Users are not communicated the steps and the involved stakeholders to complete their unpledge request.

</aside>

We will communicate the involved steps and stakeholders in the unpledge journey and show active states of the user’s request in the track pledge request screen 

---

## #109 — Withdrawal issues enhancement
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

## #110 — Foreclosure lifecycle tracking + Tata EOD report
**Status:** Done | **Last edited:** March 23, 2025 6:31 PM

**Problem:**
are we solving?**

- Users currently are not able to track the exact status of their request.
- Users do not get information and respective ETAs for the different steps involved in the process of their foreclosure request.
- Due to lack of clarity and involvement of 3P flows in the process, users feel that it is Volt that is causing delay in their application causing misinformation and instilling distrust in the minds of the user.

![User raises support ticket due to lack of clarity on status - tonality suggests that they feel that Volt is not doing anything to solve their issue](Foreclosure%2

**Solution:**
?**

We are solving this problem for the user by the following ways:

- Post making the foreclosure request, clearly describe the steps in the process to the user with accurate ETAs for each step.
- Descriptive UI screen describing the status along with steppers describing the journey of a foreclosure requests of the user
- Actively sharing the status of the request made by the user (foreclosure success/ foreclosure processed) on UI and via WhatsApp and Email to the user.
- Tata excess interest case handling - Foreclosure requests where we pay excess interest but it is not posted in the settlement account.
- Alerts
    - Flagging cases to Ops where requests are not automatically settled, so that they can be raised to BFL and Tata for settlement

---

## #111 — [B2B2C] GST payouts and reconciliation optimisatio
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

## #112 — Credit Bureau Reporting Comms
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

## #113 — [Volt LOS] KYC optimisations
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

## #114 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #115 — Calling Support Workflow – Exotel + LeadSquared In
**Status:** Not started | **Last edited:** March 17, 2026 7:00 PM

# Calling Support Workflow – Exotel + LeadSquared Integration ```mermaid flowchart TD A[Customer calls support number] --> B[Exotel receives call] B --> C[Exotel triggers API to LeadSquared] C --> D[Fetch customer details using phone number] D --> E[Open Customer 360] E --> F[Show call popup in Marvin] F --> G{Agent available?} G -- Yes --> H[Connect call to agent] H --> I[Agent discusses issue] I --> J{Existing ticket?} J -- Yes --> K[Associate call with existing ticket] J -- No --> L{Closed ticket exists?} L -- Yes --> M[Reopen ticket] L -- No --> N{Issue resolved?} N -- Yes --> O[Capture disposition] N -- No --> P[Create new ticket] K --> Q[Capture call disposition] M --> Q O --> Q P --> Q Q --> R[Exotel collects CSAT] R --> S[Send CSAT to LeadSquared] S --> T[Call process completed] %% MISSED CALL FLOW G -- No --> U[Call not connected] U --> V[Create missed call ticket] V --> W[Assign ticket via round robin] W --> X[Agent opens ticket] X --> Y[Click to Call] Y --> H ```

---

## #116 — [B2B2C] Modification for financial terms functiona
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

## #117 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #118 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #119 — Product note Co-lending foreclosure - Deprecated -
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

## #120 — Capital gains tax calculator
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

## #121 — [Platform] Withdrawal reversal post billing cycle
**Status:** Not started | **Last edited:** March 11, 2025 6:50 AM

**Problem:**
are we solving?**

As an NBFC it is very important for us to ensure that all transactions are posted as soon as 

---

**Solution:**
?**

---

## #122 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #123 — [DSP] Facility value limit
**Status:** Not started | **Last edited:** June 6, 2025 1:34 PM

**Problem:**
are we solving?**

Current the way we are defining the Facility Value limit in our agreements in not very understandable for the user;

Following is the fin

---

**Solution:**
?**

---

## #124 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #125 — Bajaj KYC Coborrower enhancement and renewal
**Status:** Not started | **Last edited:** June 5, 2024 1:29 PM

**Problem:**
are we solving?**

1. Currently users with joint holdings can not do KYC.
2. Customer with Bajaj lender will not be able to enhance or renew their line. 

---

**Solution:**
?**

---

## #126 — MFD Activation Flow in LSQ
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

## #127 — Increase Credit Utilization via Whatsapp Drips
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

## #128 — Unlock credit limit revamp
**Status:** Not started | **Last edited:** June 24, 2024 10:53 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #129 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** June 21, 2024 11:32 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #130 — DSP UPI Autopay Integration for PhonePe
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

## #131 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #132 — Addition of City-State to CKYC Request in Decentro
**Status:** In progress | **Last edited:** June 18, 2025 6:10 PM

**Problem:**
are we solving?**

The Central Registry of Securitisation Asset Reconstruction and Security Interest (CERSAI) manages the centralized CKYC database. 

CKYCRR (CKYC Registry) maintains a master pincode list that works differently from the standard India Post directory. Here's how:

Source and Updates

- CKYCRR sources its pincode data from India Post (.csv file)
- Updates occur every 6 months
- Requires 3 weeks notice to Reporting Entities for implementation

Note: city and district are used through out the PRD inter-changeably. 

How the Master List Works

The CKYC Master List follows a specif

**Solution:**
?**

The solution has been presented in the notice provided by CERSAI published on 31st Jan 2025:
[**Notice by CERSAI](https://www.ckycindia.in/ckyc/assets/doc/4838-Rejection_in_upload_of_KYC_records_due_to_mismatch_of_PIN.pdf)**
The notice recognised the problem and gave the solution of passing the state and the city (which have been part of the request body but was not added before as they were optional). CERSAI will accept the city-state pair and process the documents if the pincode is missing.

This ensures no rejection from CERSAI’s  as well as 3rd Party Service Provider’s side due to the pincode missing with the CKYC Master Pincode List.

---

## #133 — DSP UPI Autopay Integration for NBFC
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

## #134 — [DSP] NSDL PAN Verification alignment
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

## #135 — PhonePe KFS & Agreement
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

## #136 — B2B Zype integration FE and SDK callbacks
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

## #137 — Disbursement workflow optimisations
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

## #138 — End use capture of transactions
**Status:** Pending Review | **Last edited:** June 10, 2025 4:04 PM

**Problem:**
are we solving?**

- As per RBI guidelines, lenders are required to record the end use of loan disbursements to prevent misuse or diversion of funds and to enable traceability of customer transactions if necessary. Currently, our system does not ask users to specify the purpose of withdrawals, which is a compliance gap.
- Additionally, capturing end use helps improve internal reporting and risk management.

---

**Solution:**
?**

---

## #139 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #140 — MFC Pledge (revocation & invocation)
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

## #141 — [Jupiter] Unlock credit limit page changes
**Status:** Not started | **Last edited:** July 31, 2024 5:41 PM

**Problem:**
are we solving?**

Change copies on the verify interest and charges page for partners with MFC fetch. 

---

**Solution:**
?**

---

## #142 — MFD Account View in LSQ
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

## #143 — Tata Video KYC Integration V0
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

## #144 — Razorpay PG SDK integration DSP (1)
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

## #145 — Razorpay PG SDK integration DSP
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

## #146 — Repayment Lifecycle Tracking
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

## #147 — [Volt LSP] MFC pledge
**Status:** Not started | **Last edited:** July 21, 2025 3:33 PM

**Problem:**
are we solving?**

Current pledging requires customers to submit upto two OTPs, one for CAMS and another from KFin. This add to the friction in our loan application journey. 
MFC pledging APIs solve this by requiring 

---

**Solution:**
?**

---

## #148 — Implementing UTR dedupe for repayment postings
**Status:** Pending Review | **Last edited:** July 14, 2025 3:52 PM

**Problem:**
are we solving?**

---

- We currently do not perform a deduplication (dedupe) check on incoming repayment requests from Lending Service Providers (LSPs), which poses a risk of **duplicate repayment postings**. This issue becomes critical as we scale with more LSPs like PayTM and PhonePe initiating repayments through their own Payment Gateways (PGs).
- Additional complexity arises because **UTR (Unique Transaction Reference) numbers are only unique at the bank level**, not globally. Hence, simply using UTR for deduplication is not sufficient and can lead to false positives or missed duplicates

**Solution:**
?**

---

## #149 — NBFC Capturing Additional details post KYC
**Status:** Ready for Tech | **Last edited:** July 11, 2025 12:42 PM

**Problem:**
are we solving?**

Few LSPs integrating with our stack do not capture all the necessary ‘Additional Details’ or ‘declarations’ required by DSP to process the loan. In such cases, LSPs expect the DSP to collect these details directly from the customer.

---

**Solution:**
?**

---

## #150 — Untitled
**Status:** Not started | **Last edited:** July 11, 2025 10:33 AM

**Problem:**
are we solving?**

For DSP lender, finalising the values of additional details and decalarations that we need to take from the customer. 

---

**Solution:**
?**

---

## #151 — [Platform] BRE configurations for approval tasks
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

## #152 — Product note LMS integration with Tally
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

## #153 — Front loading the MF Fetch step in application
**Status:** Not started | **Last edited:** January 8, 2025 9:00 PM

**Problem:**
are we solving?**

Our current application conversion stand at ~14%, while the industry standard for conversion is closure to 70%. We have a lot of ground to cover in our conversion percentage. 

---

**Solution:**
?**

---

## #154 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #155 — Reduce Phonepe Drop-offs
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

## #156 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #157 — Delaying getDisbursementInfo API hit after savePle
**Status:** Pending Review | **Last edited:** January 6, 2025 3:50 PM

**Problem:**
are we solving?**

- For the first getDisbursementInfo API call post credit creation we are getting “No data Found” in the response of the getDisbursementInfo API
- Since we run a scheduler of 1 hour of getDisbursementInfo thus it takes another hour to get a valid response from getDisbursementInfo API response (after getting No Data Found in the response first time)

---

**Solution:**
?**

---

## #158 — MFC in-app journey
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

## #159 — Axis bank e-collect API integration for virtual ac
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

## #160 — [Platform] Mandate collection BRE optimisation
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

## #161 — [Volt LSP] DSP QC rejection handling
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

## #162 — B2B Platform Dashboard v1
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

## #163 — CKYC Upload for DSP
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

## #164 — [Platform LSP] All transactions requirements
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

## #165 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #166 — [Platform] Photo verification and liveliness check
**Status:** Done | **Last edited:** January 21, 2025 7:21 AM

**Problem:**
are we solving?**

It is important to ensure that the user who is going through the application journey submits there own verification documents and details (POA, POI and bank account). 

There are multiple checks in place currently in the system that ensure that:

- Customer Aadhaar PAN seeding check
- Selfie/Photo verification (not liveliness check) with their Aadhaar
- Name verification with bank account (Aadhaar/PAN)

Despite these checks, we have seen cases in the past when operating as an LSP where users were able to bypass this check by clicking a screenshot/someone else’s photograph in

**Solution:**
?**

We will be integrating with Hyperverge’s photo verification and liveliness check stack where the photo will be first matched and then will be checked by a model which verifies if it was a live photograph or a picture of a picture

---

## #167 — [Platform] QC rejection handling
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

## #168 — Yes bank e-collect API integration for virtual acc
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

## #169 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #170 — Volt website revamp
**Status:** In progress | **Last edited:** January 2, 2025 3:15 PM

# Volt website revamp # Why - Poor impression created (customers, hiring, partners) -- gives a stock website + app impression - Absence of adequate trust markers: - Generic trust markers - not impactful - No social proofing - Lender credibility not used to build trust in TOFU - No testament of scale - App ratings (maybe not right now) - Scope to improve education about the product and benefits - Structure content to make it easy to consume - Set up proper website analytics to get insights: GA4, Hotjar - Brand & UI - Typography used: Poppins + Inter since widely used - doesn’t give a unique personality to the brand - Stock images used on the website doesn’t help build trust - gives an impression that the product is not modern, tech savvy, old - Improve targeting user pain points - no clear understanding of the user personas we’re targeting - Very minimal understanding of users motivations, fears, pain points - Increase engagement on the website - interest calculators, motion - Solve for organic SEO ranking - Careers page, values - B2B, B2B2C pages # How do we define success: - Website is able to clear most customer queries and reduce the need to reach out to sales for conversion - Able to convincingly convey benefits, help understand process, address concerns/fears - Able to convey the scale of Volt to visitors and build trust - Build strong credibility about the brand, product and offerings - Confidently use website for external conversations - Increase top of the funnel conversions # Data to get 1. User personas: Who comes to the website and to do what? - Hypothesis to validate - Impact of showing interest rate conversion on the website - [User Persona Research](Volt%20website%20revamp/User%20Persona%20Research%209b08e7ebacfc4da59413f602c8868aa3.md) - User research - Sales team insights - Personas using the website 2. Brand positioning data from founders [Understanding brand (WIP)](Volt%20website%20revamp/Understanding%20brand%20(WIP)%209517bbbaf78d4ff28d86c3db1b31c6bf.md) 3. Market research / Competitor analysis 1. Competitor website stats: similarweb.com 4. Website metrics 1. Depth 1. Scroll depth on key pages (need to setup hotjar) - Set up “scroll_vertical” on GA4 2. Page depth (how many pages users visit) 2. Exit pages/sections - from where do users drop-off from 3. Time spent on different pages/sections 4. Click patterns / heat maps (if available) 5. FAQ’s opened 6. Help button clicked :: queries asked 5. Search queries in loans/LAMF space 6. Interest calculator engagement 7.

---

## #171 — External APIs for Holdings Statement and Statement
**Status:** In progress | **Last edited:** January 16, 2025 7:53 PM

# External APIs for Holdings Statement and Statement of Accounts (SOA) External APIs for Holdings Statement and Statement of Accounts (SOA) --- ## 1. Introduction This document outlines the requirements for developing external APIs that will provide Holding Statements and Statement of Accounts (SOA) to MFD partners. These APIs will enable partners to access comprehensive financial statements and holdings data for their customers, enhancing transparency and operational efficiency. ## 2. Objective To develop robust external APIs that provide detailed holdings statements and transaction histories, allowing MFD partners to: - Access real-time holdings data - Retrieve historical transaction statements - Generate comprehensive financial reports - Support customer portfolio management ## 3. Target Audience ### Primary Users - MFD Platform Developers - MFD Operations Teams - MFDs ## 4. Scope ### In-Scope - Development of two primary APIs: 1. Get Holdings Statement API 2. Get Statement of Accounts (SOA) API - Documentation and specifications - Data validation and error handling - Integration with existing systems like Invest well dashboard ### ## 5. API Specifications ### 5.1. Get Holdings Statement API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/holdings?date={date} ``` ### Description Retrieves a comprehensive holdings statement for a specific date, showing all active mutual fund investments and their current values. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `date` (string, optional, format: YYYY-MM-DD): Date for which holdings are requested. Defaults to current date ### Response Payload ```json { "holdingsStatement": { "statementDate": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "holdings": [ { "folioNumber": "1041038180", "schemeName": "Aditya Birla Sun Life Flexi Cap Fund", "isinCode": "INF209K01AJ8", "units": 22.7620, "navValue": 1670.00, "currentValue": 38021.64, "lienMarked": true, "lienQuantity": 22.7620, "lienMarkingDate": "2024-09-14" } ], "summaryMetrics": { "totalPortfolioValue": 2454930.52, "totalLienMarkedValue": 801000.00, "availableValue": 1653930.52 } } } ``` ### 5.2. Get Statement of Accounts (SOA) API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/soa?startDate={startDate}&endDate={endDate} ``` ### Description Retrieves a detailed statement of accounts showing all transactions within the specified date range. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `startDate` (string, required, format: YYYY-MM-DD): Start date for the statement period - `endDate` (string, required, format: YYYY-MM-DD): End date for the statement period ### Response Payload ```json { "statementOfAccounts": { "periodStart": "2024-07-01", "periodEnd": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "transactions": [ { "date": "2024-07-02", "transactionType": "DEBIT", "description":

---

## #172 — [Final] End use capture of transactions
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

## #173 — [Email Template] Decoupling of Lodgement and Agree
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

## #174 — PRD - B2C Referral [Phase-2]
**Status:** In progress | **Last edited:** January 14, 2026 5:28 PM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new us

**Solution:**
?**

---

## #175 — [CC] Lodgement Enhancement
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

## #176 — [CC] Showcase the reason for freezing on CC
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

## #177 — [LSP] Document upload support for maker
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

## #178 — [Platform] Handling of below 1 Rs transactions for
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

## #179 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #180 — Measuring Customer Support Events and 5XX errors
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

## #181 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** February 26, 2024 1:22 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #182 — Product note - DRPS
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

## #183 — [Volt] Photo and Bank Deviations enhancement
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

## #184 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #185 — Shortfall communication enhancement Ignoring accou
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

## #186 — Check eligibility overhaul
**Status:** Not started | **Last edited:** February 22, 2024 8:34 AM

**Problem:**
are we solving?**

In context of Check limit page we are solving the following problems

1. UI/UX Problems: 
    1. CTA copy signifies that this is an eligibility test which means not everyone is eligible for loan. 
    2. The main headline occupies too much space. Pushes the form down and deviates user attention from the form. The current headline conveys very little. 
    3. Too much space on the main scroll is left unused. Nothing except the form and headline is visible in the first fold. Pushes trust markers and education content down. 
    4. CTAs that are of now use to user at this stage

**Solution:**
?**

---

## #187 — Product Note Separating Portfolio Pledge and Asset
**Status:** Not started | **Last edited:** February 21, 2025 3:29 PM

# Product Note: Separating Portfolio Pledge and Asset Pledge Steps in LSQ # Product Note: Separating Portfolio Pledge and Asset Pledge Steps ## Current Behavior Currently, the system combines two distinct steps - MF Portfolio Pledge (offer page) and Asset Pledge - into a single step labeled as `ASSET_PLEDGE_STEP` in the CRM event mapping. This creates ambiguity in tracking and managing these separate processes. ## Problem Statement The current implementation: 1. Does not distinguish between portfolio pledge (offer page) and actual asset pledge steps 2. Sales agents have hard time understanding is the application is on offer or pledge for calling 3. Creates confusion in the application flow tracking 4. Reduces granularity in analytics and monitoring ## Proposed Solution Separate the current combined step into two distinct steps: 1. **Portfolio Pledge** (`PORTFOLIO_PLEDGE_STEP`) - Represents the offer page where customers view their eligible portfolio - Maps to `MF_PLEDGE_PORTFOLIO` in application flow 2. **Asset Pledge** (`ASSET_PLEDGE_STEP`) - Represents the actual asset pledging process - Maps to `ASSET_PLEDGE` in application flow ## Implementation Changes Required 1. Update CRM event mapping in `getCRMEvenTypeForStepStart`: ```java case MF_PLEDGE_PORTFOLIO -> CRMEventType.PORTFOLIO_PLEDGE_STEP; case ASSET_PLEDGE -> CRMEventType.ASSET_PLEDGE_STEP; ``` 1. Update DB schema to reflect new step definitions: - Add `PORTFOLIO_PLEDGE` as a distinct step after `MF_FETCH_PORTFOLIO` - Keep `ASSET_PLEDGE` in its current position in the flow ## Expected Benefits 1. Improved tracking and analytics 2. Better user journey mapping 3. Better lead prioritisation in outbound ## Migration Plan 1. Understand current Lead stage update activity send to LSQ 2. Create new step definitions in DB 3. Verify the changes in LSQ 4. (Backfill) ## Next Steps 1. PN :- Tech Review

---

## #188 — Verify interest and charges revamp
**Status:** Not started | **Last edited:** February 21, 2025 12:28 PM

**Problem:**
are we solving?**

1. One day conversion rate of Verify interest and charges page is ~46%
2. Most users are dropping off this screen because of the following problems:
    1. Users think that this is the last page of the application.
        1. “Mutual fund lock ho jayega”
        2. “Loan ho jayega agar aagay jayegay”
    2. Benefits are not properly communicated. key benefits such as
        1. One time processing fee
        2. OD
        3. Interest only EMI
        4. Unlimited withdrawals and repayments are not shown to the user
    3. User thinks that the “Pledge Funds” value is too hig

**Solution:**
?**

---

## #189 — CKYC (Decentro) API integration
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

## #190 — Periscope
**Status:** Not started | **Last edited:** February 20, 2024 7:01 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #191 — Pre-fetch flow Optimisation Consolidating PAN flow
**Status:** Done | **Last edited:** February 19, 2026 9:43 AM

**Problem:**
are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

**Solution:**
?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

---

## #192 — Custom commercial for Cambridge wealth
**Status:** In progress | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

- Custom ROI and lender configuration for Cambridge wealth

---

**Solution:**
?**

---

## #193 — Line enhancement Loan renewal BRE
**Status:** Not started | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

1. Line enhancement and loan renewal fees BRE changes
2. Fee and charges verification for fresh application, line enhancement and loan renewal for both lender

**Solution:**
?**

---

## #194 — PAN type update on partner dashboard
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

## #195 — Attribution for Jupiter
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to create a BRE which will allow Jupiter platform to create customer even if customer account exist.

---

**Solution:**
?**

---

## #196 — Bajaj PG
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

## #197 — LSQ data sync
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

## #198 — Penny drop on partner dashboard
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- Verify partner bank account for smooth payout

---

**Solution:**
?**

---

## #199 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #200 — Pledge error handling
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

**Solution:**
?**

---

## #201 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #202 — Admin action to update mandate status & interest
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

## #203 — Centralised issue reporting process
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

## #204 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #205 — DSP Bank Account Update and Mandate Re-Registratio
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

## #206 — Downtime handling [Post loan]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #207 — FAQ Management System
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# FAQ Management System # FAQ Management System PRD ## 1. Problem Statement We need a flexible FAQ management system that allows: - Dynamic content updates without code deployment - Categorized display of FAQs - Multi-language support - Easy maintenance by non-technical teams ## 2. Goals & Success Metrics ### Primary Goals - Reduce customer support tickets volume by 30% ### Success Metrics - FAQ usage analytics - Improve FAQ content quality through user feedback - Identify gaps in documentation/support - Increase user satisfaction - Track FAQ effectiveness - Reduction in support tickets ## 3. Technical Requirements ### 3.1 Content Management ```sql Table: faq_content - id (PK) - category_id (FK) - question - answer - language_code - status (ACTIVE/INACTIVE) - created_at - updated_at - last_updated_by ``` ### 3.2 Category Management ```sql Table: faq_categories - id (PK) - name - description - display_order - status - parent_category_id (for sub-categories) ``` ### 3.3 Language Support ```sql Table: supported_languages - language_code (PK) - language_name - status - rtl_support ``` ## 4. Feature Requirements ### 4.1 Admin Panel Features 1. Content Management - CRUD operations for FAQs - Version history 2. Category Management - Create/edit categories: should be able to create the new FAQ category - Reorder categories : Should be able to set the order of category and will be shown on UI in same order - Category status toggle: Show hide on UI 3. Language Management - Add new languages - Translation management - Default language setting ### 4.2 User Interface Features 1. FAQ Display - Categorized view - Search functionality - Language selector 2. Navigation - Category filters - Breadcrumb navigation - Back to top button 3. Content Features - Rich text support - Image/video embedding - Link handling ## 5. API Structure ### 5.1 Content APIs ```json GET /api/v1/faqs { "category": "withdrawal", "language": "hi", "search": "optional_search_term" } Response: { "category": { "id": "withdrawal", "name": "Withdrawal", "faqs": [ { "id": "w1", "question": "When will I receive funds?", "answer": "During banking hours...", "last_updated": "timestamp", "last_updated_by": "Ranjan kumar singh" } ] } } ``` ### 5.2 Admin APIs ```json POST /api/v1/admin/faqs { "question": { "en": "English question", "hi": "Hindi question" }, "answer": { "en": "English answer", "hi": "Hindi answer" }, "category_id": "withdrawal", "status": "ACTIVE" } ``` ## 6. Content Update Workflow 1. Content Creation ```mermaid graph TD A[Create Content] --> B[Add Translations] B --> C[Preview] C --> D[Publish] ``` 2. Content Update ```mermaid

---

## #208 — Handle excess amount in foreclosure request [TCL]
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

## #209 — Handle physical mandate cases for BAJAJ
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

## #210 — Handle settlement of charges against withdrawal
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

## #211 — In app user review [Play store]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We currently do not collect user experience feedback directly at key moments in the app journey, which has led to the following challenges. 

- **Missed Pain Points:** Without timely feedback, we risk missing critical pain points during specific stages of the app journey, such as loan applications, payments, or withdrawals. These missed insights can result in unresolved issues, leading to decreased user satisfaction.
- **Lost Improvement Opportunities:** Journey-based feedback offers real-time insights into what’s working and what needs improvement. Without this feedback, we

**Solution:**
?**

---

## #212 — Interest feature handling for TCL
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

## #213 — Loan servicing - LAS VOLT
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

## #214 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #215 — Mandate registration post loan
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

## #216 — Partial lodgement handling - DSP
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

## #217 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #218 — Push application id and type in LSQ
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Currently we do not push loan application ID against the opportunity and because of this data team are not able to perform recon of LSQ data with Volt DB

---

**Solution:**
?**

---

## #219 — Repayment flow optimisation
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

## #220 — Revocation MIS - TCL customer
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

## #221 — Rounding of Accrued Interest before Posting bill a
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

## #222 — SYNC shortfall status with Principal & shortfall r
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our current shortfall management process is manual and inefficient:

1. We rely on lender-provided spreadsheets for shortfall data
2. Updates are made only once daily through the admin tool by the ops team
3. The app continues showing shortfall notifications even after customers have repaid, leading to:
    - Poor user experience
    - Increased customer complaints
    - Unnecessary escalations

---

**Solution:**
?**

---

## #223 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #224 — Setup new and fix existing MIS for lender BFL and
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Setup new and fix existing MIS for lender BFL and TCL

---

**Solution:**
?**

---

## #225 — Shortfall experience optimisation
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

## #226 — Show interest virtual bank account to BFL customer
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

## #227 — Supporting shares as a collateral - LMS (Volt)
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Scope:

- Un-pledging
- Collateral tracking
- Collateral transactions

---

**Solution:**
?**

---

## #228 — TATA loan renewal
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #229 — Ticketing Tool Evaluation Document
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# Ticketing Tool Evaluation Document ## 1. Introduction ### Purpose of Evaluation The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation. ### Scope and Objectives This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include: - Analyzing feature sets and usability - Evaluating system performance and reliability - Reviewing security and compliance standards - Assessing cost-effectiveness and support options DATA sharing over WA and 1:1 WA chat with MFD - PI Data and any other data ## 2. Current Challenges ## Agent Challenges/process gap | # | Challenge | Impact | Priority | | --- | --- | --- | --- | | 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 | | 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 | | 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 | | 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 | | 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 | | 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 | | 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 | | 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 | | 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 | | 10 | No visibility into **TAT of internal ticket and resolution TAT from the 3P** | Inability to provide ETAs to customers | P0 | | 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 | |

---

## #230 — Volt Apps & Web Multiple Loan Handling - Launching
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

## #231 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #232 — Ticketing system for Volt
**Status:** In progress | **Last edited:** February 19, 2025 3:20 PM

# Ticketing system for Volt # **Problem Statement:** Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. Applications successful = With + without assist = Count * Cost Current Support team are facing following challenges Borrower - Long wait times for the agents to get back - Chat support - visibility - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product. - RMs and agents have to provide context in sending the client Between RMs or on Leave - We would have a data on the issues raised by a particular customer or to maintain history of support - If the support request is not OPS or Tech realted then taking followup - High Inbound Traffic :- Agents are move from call to call and saving - Lack of a single source of truth for customer issues. - Inconsistent tracking across calls, WhatsApp, and emails. - Unrecorded issues, especially from phone calls. - No SLA tracking or identification of common problems. **Key Requirements:** - **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket. - **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes. - **Workflow Needs**: - Easy ticket creation and search by phone number. - Visibility into all tickets per customer/issue. - Strong APIs and customizable workflows. - **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database. **Goals:** - Achieve 100% ticketing for all interactions. - Track and measure issue resolution times (SLAs). - Identify bottlenecks and common problems. - Prevent any customer issue from being overlooked. The Workflows that need to be enabled - Grouping of users - Page-nation for the pending and completed application The Filter for the lead stage to be added Add filters in the pending application User stories - Customer will call us - customer is routed to a agent - How is this routing setup? - Agent takes notes on the call - Dispostion

---

## #233 — Track inbound calls
**Status:** Not started | **Last edited:** February 19, 2024 5:26 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #234 — DSP Handling Sell-Off Dependencies
**Status:** Not started | **Last edited:** February 18, 2025 2:22 PM

**Problem:**
are we solving?**

The user can request to initiate a voluntary sell-off of his collateral to pay their interest or total outstanding or principle amounts. 

---

**Solution:**
?**

---

## #235 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** February 16, 2024 7:07 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #236 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #237 — DSP website revamp
**Status:** Not started | **Last edited:** February 12, 2025 4:29 PM

# DSP website revamp # Problems to solve 1. “Make the website a public website” 1. Make it accessible on Google and other search engines (already visible through Bing) 2. Brand impression: currently looks like a placeholder website 3. Improve “About DSP” section 1. More prominently referencing to the DSP group - Review other DSP children websites 4. Product offerings 1. Structured lending 2. LAMF - understand what’s missing 3. LAS - show coming soon? 5. Regulatory 1. Link RBI’s sachet portal 2. Prominently display name, email, contact number of grievance redressal officer on website 3. Prominently display details of COO - Principal Nodal officer on website 6. Minor fixes 1. Update address - 11th floor instead of 10th floor 2. Update CIN 3. Operating timings: customer care 4. Update partners list 5. Benefits → “RBI registered” needs to come with a disclaimer - refer to flexiloans footer 7. Logo finalisation ![image.png](DSP%20website%20revamp/image.png) # Solution space - [ ] Understand scope - [ ] Talk to priya - What is “headers” - Pankaj notes - [ ] Get feedback shared by Pankaj Thapar (policy consultant) - [ ] New website mood board - how much brand referencing is needed? | Problem | Proposed solution | | --- | --- | | 1.a | - Submit site on Google Search Console - Make sitemap.xml - Make robots.txt | | | | WEBSITE LAYOUT ### Header - Partners - Products - About ### Hero - Title - “Loans against securities” - “digital first approach” - CTA ### About Organisation stats - Money disbursed, Loans given, no. of partner tie ups - Since 160+ years ![image.png](DSP%20website%20revamp/image%201.png) ### Our products - LAMF - LAS - Structured lending ### LAMF features ### How it works ### Footer ## Additions - FAQs - About us → our team

---

## #238 — Callback Management System – Inbound Call Optimisa
**Status:** In progress | **Last edited:** February 10, 2026 3:13 PM

**In scope:**
(Phase 1)

- Inbound calls on pre-loan & post-loan Exophones
- Auto-creation of callback tickets in LSQ
- SLA-driven agent callbacks
- Retry logic (RNR 1–3)
- Operational & performance reporting

# Callback Management System – Inbound Call Optimisation ## 1. Document Overview --- **Product Name:** Callback Management System **Owner:** Product **Stakeholders:** Debesh, Tushar, Vivek **Systems Involved:** Exotel, LSQ Service Desk (Marvin)\ Reference BRD: [https://docs.google.com/document/d/144kWIA_KxfnZIej1Jp-F6_YInsMxaK2KR3hufMTqrIE/edit?tab=t.0](https://docs.google.com/document/d/144kWIA_KxfnZIej1Jp-F6_YInsMxaK2KR3hufMTqrIE/edit?tab=t.0) ## 2. Problem Statement A significant percentage of inbound support calls (pre-loan and post-loan) are currently missed due to: - Peak-hour call spikes - Round-robin routing limitations - Static agent capacity Missed calls negatively impact: - Customer experience and CSAT - Repeat call volume - Conversion and servicing efficiency Adding headcount is **not cost-effective** due to uneven call distribution across the month. ## 3. Objective & Success Criteria ### Primary Objective Eliminate inbound missed calls by converting **every inbound attempt** into a **guaranteed callback**, with defined SLAs and retry logic. ### Success Metrics - Reduce missed call rate from ~36% → **<5% within 7 days** - Peak-hour missed calls → **near zero** - Callback connection rate > **80%** - SLA adherence > **95%** ## 4. Scope Definition ### In Scope (Phase 1) - Inbound calls on pre-loan & post-loan Exophones - Auto-creation of callback tickets in LSQ - SLA-driven agent callbacks - Retry logic (RNR 1–3) - Operational & performance reporting ### Out of Scope (Phase 1) - Customer-selected callback slots - Outbound campaign integration - Direct re- routing to the Sales agent ## 5. Key Assumptions - All inbound calls are treated as callback requests - Agents will only call customers via system-tracked outbound calls - LSQ Service Desk is the source of truth for SLA and status - Exotel IVR and webhooks are available for integration ## 6. Core Entities & Data Model ### Callback Ticket (LSQ Service Desk) | Field | Description | Comments | | --- | --- | --- | | Phone Number | Primary identifier | | | Journey Type | Pre-Loan / Post-Loan | | | Ticket Status | Open | | | Total Missed Calls | 2 | To confirm with lsq | | Callback Attempt Count | Outbound attempts made | | | Assigned Agent | Auto-assigned | Round robin | | Queue | Inbound Callback Queue | | | SLA Deadline | Dynamic based on attempt | SLA | | Disposition | Final outcome | To be defined | | Sub Disposition | | To be defined | ## 7. Detailed End-to-End Process Flow ```mermaid flowchart TD %% ===================== %% CALL INTAKE %% ===================== A["📞 Customer

---

## #239 — AppSmith Enhancement
**Status:** Pending Review | **Last edited:** February 10, 2025 11:43 AM

**Problem:**
are we solving?**

- Currently sales and ops team face information insufficiency while dealing with customers

---

**Solution:**
?**

---

## #240 — [Platform] Enabling alternate mandate registration
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

## #241 — Attribution for Volt applications
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

## #242 — MFC Pledge error handling - V1
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

## #243 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** December 6, 2024 2:49 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #244 — Volt LOS journey optimisations
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

## #245 — Update user details (for TCL, BFL, DSP)
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

## #246 — [Platform] Mandate presentation request optimisati
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

## #247 — one page application for Partners RMs
**Status:** Not started | **Last edited:** December 30, 2024 4:36 PM

**Problem:**
are we solving?**

- the Customer oriented LAMF journey is not suited for the Partner triung to complete the appliocations for the customer
    - The customer persona is to not know what the steps are or are need, but to follow the guide and complete it , while this process works for the MFD as well the Need for login and OTP etc can be simplified
- The current step don’t provide application visiblity on the steps and status clearly enpough
- MFD can’t select the Funds easily

---

**Solution:**
?**

---

## #248 — Un-pledge optimisations
**Status:** In progress | **Last edited:** December 3, 2024 3:13 PM

**Problem:**
are we solving?**

For BFL users, who make a withdrawal request of complete available amount while an un-pledge request is in-progress then the withdrawal requests gets processed first and un-pledge request gets rejected due to update in the value of net-payable due to the withdrawal processing  

---

**Solution:**
?**

When user is making a withdrawal is making a withdrawal while an un-pledge request is in “In progress” we will give a heads-up to the user that the withdrawal request might interfere with the un-pledge request if the outstanding is not zero. [This change only needs to be done for BFL]

---

## #249 — [B2B2C] Improving lead quality in partner journey
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

## #250 — [Volt LSP] Pre fill bank account number from MFC d
**Status:** In progress | **Last edited:** December 27, 2024 10:40 AM

**Problem:**
are we solving?**

Customers on the bank verification step are currently required to enter their complete Bank account number and IFSC code to verify their bank account this is a pain for customers. 

[https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99](https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99)

---

**Solution:**
?**

---

## #251 — Mobile email dedupe check in case on in-progress m
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

## #252 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #253 — LSQ Service Desk
**Status:** Not started | **Last edited:** December 24, 2025 11:59 AM

# LSQ Service Desk ## **1. Overview** **Objective:** Phase 1 focuses on building an LSQ-based internal Service Desk that enables structured internal ticketing, SLA management, and Jira integration. **Scope Includes:** - Jira Integration with LSQ - Internal Ticket Management (Sales, Support, Ops) - Ticket Creation & Assignment Logic - Volt Operations Team Workflow - Email Integration (Phase-ready foundation) ## [Jira Integration on LSQ Service desk](LSQ%20Service%20Desk/Jira%20Integration%20on%20LSQ%20Service%20desk%202aee8d3af13a80e8a5f7c0b8e990256a.md) [Support Requirement](LSQ%20Service%20Desk/Support%20Requirement%202aee8d3af13a80e3ae45c08bfa32a8bf.md) [Volt Ops Requirements The child ticket will be created and assigned to Volt Ops.](LSQ%20Service%20Desk/Volt%20Ops%20Requirements%20The%20child%20ticket%20will%20be%20cre%202afe8d3af13a80b9be04e4c2eb5d9880.md) # **3. Internal Ticketing Framework:** This section defines the **complete ticket lifecycle** for the LSQ Service Desk used by Support, Sales, and Operations teams. It covers how a ticket is created, assigned, triaged, escalated (Volt Ops, Product, Lender), and resolved, including SLA behaviour, parent–child ticket logic, and exception handling. # **Actively Involved** - **Customer / MFD** - **Agent (Chat / Email / Calling)** - **System (LSQ Automations & Integrations)** - **Volt Ops Team** - **Product / Tech (via Jira)** - **Lender Partners** # **Ticket Lifecycle Overview** A ticket progresses through the following high-level stages: 1. **Intake & Ticket Creation** 2. **Classification** 3. **Work / Investigation** 4. **Child Ticket Creation (Volt Ops / Product / Tech / Lender)** 5. **Resolution & Customer Validation** 6. **Closure & CSAT** 7. **Reopen, RCA** # **Detailed Step-by-Step Ticket Flow** ## **In Take & Ticket Creation** 1. **Customer initiates contact** via Chat, Call, Email 2. **System identifies the customer** - If contact exists → attach to contact. - If new → create new contact with basic details. Use cases where a ticket will be created and a ticket will not be created: | Channel | Scenario | Condition | Ticket? | Notes | | --- | --- | --- | --- | --- | | Call | Registered number call | Lead exists | YES | Auto-link ticket to lead; capture disposition. | | Call | Unregistered number call | Lead not found | YES | Capture disposiiton and Create new ticket. | | Call | Telemarketing calls | | NO | Mark as Spam | | Call | Missed call from registered number | Customer dropped | YES | New Ticket with status open with associated lead | | Call | Missed call from non registered number | Customer dropped | YES | New Ticket with status open | | Email | Any email sent to support@ | Incoming email | YES | LSQ

---

## #254 — MFD Communications for MFDs and Customers
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

## #255 — [Volt LSP] Liveliness check
**Status:** Not started | **Last edited:** December 23, 2024 8:08 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #256 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #257 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #258 — [Platform] Agent session management
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

## #259 — GET Transaction API - Volt
**Status:** Not started | **Last edited:** December 21, 2024 12:36 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #260 — [Platform] Risk report
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

## #261 — Figma file organisation
**Status:** Not started | **Last edited:** December 2, 2024 3:59 PM

**Problem:**
are we solving?**

- Searching for updated files of features and different stages of the journey
- Get visibility on how each stage is handled for different lender
- Easy visibility on version history, compliance updates etc. done in the past - need to view in one place
- Allow storing secondary flows like: error handling, drop-off flows etc

---

## #262 — [Platform] Mobile verification method
**Status:** Not started | **Last edited:** December 17, 2024 7:42 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #263 — Design process + requirements
**Status:** Not started | **Last edited:** December 17, 2024 7:00 PM

# Design process + requirements # Why - Enable leveraging design for problem solving during PRD discovery state. - Avoid using up design bandwidth on unclear requirements only to have to redo designs or get deprioritised - Streamline design process: set expectations for requirements. - To provide clear, documented requirements (stakeholders aligned) before design starts work. - Design bandwidth getting used up in ad-hoc tasks without clear understanding of the problem statement. - Can’t allocate time to work on planned design projects. # How ### 10-50-90 feedback process 💡 The 10-50-90 feedback process creates structured checkpoints for feedback that align with different stages of design maturity, helping prevent costly late-stage revisions. - **10%** - Reviewing initial concepts and direction To ensure we’re solving the right problem and heading in a promising direction before investing too much time - **50%** Core design elements are taking shape but there's still flexibility to make meaningful changes. - **90%** The design is nearly finished. This final review focuses on refinements and polish rather than major changes. It's about catching small issues and ensuring everything meets quality standards before finalising the design. ### Why? - Sets clear expectations on what kind of feedback is valuable at each stage - Reduces wasted effort by catching misalignments early. [How To Use the "10/50/99" Approach to Give Feedback | HackerNoon](https://hackernoon.com/how-to-use-the-105099-approach-to-give-feedback-1y8433l0) # Design process for major projects | Stage | Steps | Notes | | --- | --- | --- | | | Review problem statement | In this stage Product <> Design will: - Understand problem statement : Get a detailed understanding on scope, expectations, ETA - Supporting data: Who are we building for, what do they need to do, why this problem statement - Impact : How many users are facing this problem - Data points : Information required to be displayed or used in screens, PDFs, or any other mediums we are designing for | | | Make user flow | What all tasks need to accomplished by the user | | | Make wireframes | Identify all edge cases, drop-off flows, error states, happy flows | | | | | | 10% | Walkthrough PRD + approach | Tech + product + design alignment on screen/flow - Aligned on routes, data availability, limitations Clear alignment necessary to avoid having to rework high fidelity UI | | | Work on feedback | | | | Work

---

## #264 — MFD Servicing
**Status:** Not started | **Last edited:** December 17, 2024 1:46 PM

# MFD Servicing # MFD servicing We need to provide assistance to the MFDs in completing the application process on behalf of there customers and provide servicing. These issues need to be identified and to be solved for reduced effort on the MFD and Volt side. We want to provide quick resolution to any issues our MFD might be facing , Goal of the document is to describe the process and current challenges faced by us Ideal process 1. MFD communicates the issues with us using WhatsApp. 2. RM understands the issues from the Communications and raise a ticket 3. Agent then communicates the resolution and mark the tickets as resolved 4. We track the WhatsApp chat and Ticket analytics to understand and improve our servicing ## Current issues ### Communications - **Issue communication:** We use WhatsApp based tools for the MFD to communicate with us (preferred mode of communication by the MFDs). We have the two tools that we currently use - **Periskope: U**sed for providing Group chats to the MFD. - Periskope is based on Whatsapp app. It does not provide good tracking for the chats and expect us to create tickets to track issues - Pros - If MFD has a employees then they can be served by a whatsapp group better to have a one channel for updates *~ 300 groups currently with >1 MFD member.* - If MFD has a escalation then escalation can be handled on group ~ *this really has a bandwidth issues for Kapil or Bharat. We should have a separate channel for the grievance.* - If the RM is on leave and we have a group to solve then someone else can take the handover and solve the problem ~ *Currently only RM has the context on the issues of the MFD and rest of the people in group can’t takeover. The new RM has to gain context from the chat history or notes on the tickets.* - Convert WhatsApp messages into tickets or tasks - Connect with CRM systems, ticketing platforms, and other tools via APIs and web-hooks. - Cons - The platform is no longer supported by the Company - The API integration need to developed by Volt - We are not provided with most Chat level tracking like First time response, Time spend on a chat, How long the message hasn’t been responded to. - Tickets has to

---

## #265 — Product Note
**Status:** Not started | **Last edited:** December 16, 2025 2:19 PM

# Product Note # **Background and Context:** - Broader context - User/Business/Department context of the problem they are facing - What is the challenge they are facing - What is getting impacted - problem impact - What is broken or missing today? - Why are we solving this now? (Trigger for prioritisation, define urgency, dependency) - When are we planning to solve it? (High level timelines / Key milestones) --- ## **1. What is the scope of the problem?** - **What is the scope of the problem?** - Clear, concise scope of the problem. - Who are we solving it for? (Primary and secondary user segments) - What is out of scope? - Why is this out of scope? Key decisions/alignments/stakeholders - Will this be picked later? If yes, when? If no? why not? - Who is explicitly out of scope --- ## 2. Success Criteria **How will we know the problem is solved?** - Clear, measurable outcomes - User, business, or system-level metrics (2-3 Key metrics) - What “good” looks like post-launch - What should not get impacted (Check/Guardrail metrics) --- ## 3. **What is the scope of the solution?** **How are we planning to solve it?** - Summary of the solution approach - Use cases being covered in the solution scope **Explicitly out of scope** - What use cases are out of scope? - Why is they out of scope? Key decisions/alignments/stakeholders - Will this be picked later? If yes, when? If no? why not? **FAQ:** | **Question** | What is in scope? | | --- | --- | | Will this change existing processes? | | | Who and how will they get impacted? | | | | | --- ## 4. Key flows - How will it look like? What are the steps in the journey ---

---

## #266 — MF Fetch optimizations
**Status:** Ready for Tech | **Last edited:** December 15, 2025 4:53 PM

**Problem:**
are we solving?**

The aim is to improve MF fetch flow, to solve for this we will solve the following problems:

1. Show users contextual errors that convey what exactly went wrong for the user in fetch.
    
    Users should have better understanding of the fetch errors, the construct of LAMF, what investments can be used for LAMF, and actionable to rectify errors (for errors that can be rectified).
    
    For users downloading our app from app stores without understanding that this is not a traditional unsecured loan, these errors should handle their disappointment with grace and make them

**Solution:**
?**

---

## #267 — Volt LSP PAN verification
**Status:** Not started | **Last edited:** December 13, 2024 3:02 PM

**Problem:**
are we solving?**

A high number of customers are currently facing issues with Decentro PAN verification step on the LSP, this need to be solved.

---

**Solution:**
?**

---

## #268 — User engagement on the LSQ
**Status:** Not started | **Last edited:** December 12, 2024 5:55 PM

# User engagement on the LSQ Currently issues # Ticketing System Requirements & Workflow Chief Product Officer Document | December 2024 ## Executive Summary Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency. ## Current Pain Points Analysis 1. Issue Resolution Tracking - No unified system to track resolution progress - Limited visibility into resolution time frames - Inability to measure team performance effectively 2. Organizational Context - Disconnected systems leading to fragmented customer context - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos - Limited cross-functional visibility 3. Support Coverage - Backup handling inefficiencies - Lack of structured handover processes - No clear escalation matrices 4. Performance Metrics - Missing TAT (Turn Around Time) tracking at issue level - No trend analysis capabilities - Unable to identify recurring issues and root causes ## Core Requirements ### Ticket Creation & Management 1. Mandatory Ticket Creation - 100% ticket creation for all customer interactions - Channels: Phone calls, WhatsApp, Email - Required fields: Partner ID, Issue Category, Description - Clear resolution confirmation before ticket closure 2. Channel-Specific Workflows - MFD Channel specific routing rules - Direct customer support workflow - B2B partner interface requirements 3. SLA Management - Channel-specific SLA definitions - Real-time SLA tracking - Escalation workflows - Performance dashboards ### User Management & Access Control 1. Internal Users - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support) - Support Channel Team (10 agents) - Sales Team (7 members) - Ops and Tech on-call teams - Admin users 2. External Users - Direct MFDs - Platform MFDs - B2C customers - B2B platform partners ### Integration Requirements 1. Communication Systems - Exotel for call routing - RUNO for call visibility - Periskope and WATI for WhatsApp - Email integration 2. Internal Systems - Retool for DB state visibility - LSQ CRM - Slack for internal communications ## Key Features 1. Unified Dashboard - Single view of customer interactions - Real-time status tracking - SLA monitoring - Team performance metrics 2. Analytics & Reporting - Issue frequency analysis - Resolution time tracking - Team performance metrics - Channel-wise analysis - Custom report generation 3. Workflow Automation - Automatic

---

## #269 — Un-pledging bug fixes & UI optimisation
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

## #270 — PRD - B2C Referral [Phase-1]
**Status:** In progress | **Last edited:** December 10, 2025 8:08 AM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt does not have any mechanism to leverage its existing loan users base who has experienced the value of Volt Money LAMF product for new user acquisitions.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new users to borrow LAMF from Volt as a trusted brand and limited period reward offers will assist i

**Solution:**
?**

---

## #271 — Volt Partners - Request Demo Revamping
**Status:** Done | **Last edited:** December 10, 2024 4:55 PM

**Problem:**
are we solving?**

1. **Lack of Clarity for Business Teams**:
    - Business teams do not have visibility into which companies or platforms are interested in the Volt Partners Program.
2. **Inefficient Communication Process**:
    - Teams are spending excessive time and bandwidth reaching out to individual users to identify their company details.
3. **Difficulty in Lead Prioritization**:
    - Without knowing the company names, the business team cannot effectively prioritize leads, resulting in inefficient allocation of resources.

---

**Solution:**
?**

1. **Add New Fields to the Form:**
    - **Company Name**: Add a mandatory textbox to capture the user's company name.
    - **Company Website**: Add an optional textbox to collect the company's website link.
2. **Implement Validations:**
    - **Phone(Re-name “Phone” to “Mobile Number”**: Ensure the input does not accept alphabets or special characters. Implement a phone number regex for validation.
    - **Name**: Enforce a minimum of 3 characters for the name field.
    - **Company Website**: Validate the input using a website URL regex to ensure proper format.

![image.png](Volt%20Partners%20-%20Request%20Demo%20Revamping/image.png)

---

---

## #272 — [Tata Neu] Bottom sheet to nudge user to withdraw
**Status:** Not started | **Last edited:** August 6, 2024 5:19 PM

**Problem:**
are we solving?**

Post completion of application, users currently land on the dashboard page. The user now has multiple actions that they can perform which can distract them from the primary use case of customers withdrawing from their credit limit. 

Problem statement is to nudge user to place a withdrawal request as soon as the customer lands on the dashboard page.

---

**Solution:**
?**

---

## #273 — Cashfree PG integration
**Status:** Pending Review | **Last edited:** August 5, 2025 3:56 PM

**Problem:**
are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

**Solution:**
?**

---

## #274 — PRD - Capturing UTM-Based parameters for acquisiti
**Status:** Not started | **Last edited:** August 29, 2025 4:46 PM

**Problem:**
are we solving?**

We need a **robust end-to-end attribution system** that:

1. **Capture & persist** both first-touch and last-touch UTMs from initial visit to post-registration lifecycle across sessions/ devices for every MFD
2. Stores them in the **MFD master record (MFD table)** for permanent reference.
3. ~~Sends UTM data to LSQ during lead creation.~~
4. Retains them for use in **activation attribution** (linking post-onboarding milestones/ activation events back to acquisition source for full funnel attribution).

---

**Solution:**
?**

---

## #275 — [Lending stack] Command centre - QC
**Status:** Not started | **Last edited:** August 29, 2024 11:56 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #276 — LSQ Requirements for UTM Attribution
**Status:** Not started | **Last edited:** August 28, 2025 11:55 AM

# LSQ Requirements for UTM Attribution ## Objective Enable LSQ (LeadSquared) to **store, track, and act upon attribution data** for each MFD by capturing both **initial UTM** and **last UTM**. Ensure every UTM update creates **activities and follow-up tasks** for better engagement tracking. ## Data Flow 1. **Event Logging** - Each time an MFD clicks on a campaign link or engages with a communication containing UTMs, the event is logged with: - MFD phone number (identifier) - UTM parameters (`campaign_id`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) - Timestamp of event - Activity context (page visited, registration, activation milestone, etc.) 2. **MFD Matching** - The backend matches the UTM event to the MFD via phone number. - If no MFD record exists, UTM data is stored and linked upon registration. 3. **Stack Ranking of UTM Events** - UTM events are ranked by **timestamp**. - Two attribution markers are defined: - **Initial UTM** = first UTM triggered (never overwritten). - **Last UTM** = most recent UTM triggered (always updated). ## Data Storage in LSQ 1. **Custom Fields (Lead Record)** - Store **Initial UTM** and **Last UTM** parameters in dedicated custom fields (see earlier table). 2. **Activity Logging (Mandatory)** - For every **Initial UTM capture** → create an **Activity** in LSQ: - Activity Name: *“Initial UTM Recorded”* - Fields: UTM parameters, timestamp, campaign type. - For every **Last UTM update** → create an **Activity** in LSQ: - Activity Name: *“Last UTM Updated”* - Fields: UTM parameters, timestamp, campaign type. 3. **Follow-Up Task Creation (Linked to Last UTM)** - Each time a **Last UTM** is updated: - A **Follow-up Task** must be automatically created for the assigned RM/Owner. - Task Type: *“Follow-Up on Campaign Lead”* - Due Date: Based on **Last UTM Activity timestamp** (e.g., +24 hours). - Linked to the same MFD Lead. - This ensures **freshest campaign interaction → RM engagement**. 4. **Last Activity Field Update** - Each **Last UTM Activity** must also update the **system’s Last Activity Date field** in LSQ. - This allows LSQ’s native filters/reports to stay accurate. ## Rules & Logic 1. **Initial UTM** - Captured once on first campaign click. - Not overwritten. - Activity logged → *“Initial UTM Recorded”*. 2. **Last UTM** - Updated on every new campaign click. - Always overwrites previous Last UTM fields. - Activity logged → *“Last UTM Updated”*. - Follow-up Task created → *“Follow-Up on Campaign Lead”*. - Last Activity Date updated.

---

## #277 — Payment gateway integration
**Status:** Not started | **Last edited:** August 28, 2024 3:44 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #278 — SL updation & additional limit calculation optimis
**Status:** On Hold | **Last edited:** August 27, 2024 5:20 PM

**Problem:**
are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

**Solution:**
?**

---

## #279 — [Platform] RTA portfolio API integration
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

## #280 — [DSP] Dues collection comms
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

## #281 — LSQ Revamp
**Status:** In progress | **Last edited:** August 20, 2025 3:15 PM

**Problem:**
are we solving?**

Currently, we have a **single flow** that combines both the **MFD activation journey** and the **customer LAMF journey**. This setup is causing several issues:

- Manage MFDs who have multiple applications/customers under them is a challenge
- Managing multiple products at a customer level is a challenge
- Confusion in workflow management
- Low visibility into which opportunity belongs to which journey
- Difficulty in segregating and tracking MFD vs customer-related progress
- **Since the phone number is used as the primary identifier, we cannot create separate applications 

**Solution:**
?**

We will proceed with using **Leads and Opportunities**, rather than shifting to the **Lead and Account** view.

The key reasons for not adopting the Account view are:

1. **Task limitations** – Tasks cannot be created or managed in Accounts the same way they can be in Leads.
2. **View-only structure** – The Account view primarily serves as a dashboard to display associated leads, with limited operational functionality.
    - This same visibility can be replicated within the Lead view using additional connectors such as the **Custom Tabs Builder**, allowing us to achieve similar outcomes without shifting to the Account model.
3. **No follow-up workflows** – Accounts do not support activity logging or follow-up creation, which are essential for our engagement and tracking needs.

Given 

---

## #282 — Amplitude Audit and Additions
**Status:** Not started | **Last edited:** August 20, 2025 12:02 PM

**Problem:**
are we solving?**

Auditing the existing amplitude implementation and listing out all the events to add.

---

**Solution:**
?**

---

## #283 — MFC Journey - Fetch
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #284 — MFC implementations
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #285 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** August 16, 2024 5:19 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #286 — [DSP] KYC v2 (including CKYC)
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

## #287 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #288 — B2B Zype integration webhook
**Status:** Not started | **Last edited:** August 12, 2024 8:25 PM

**Problem:**
are we solving?**

In addition to current webhooks, create another webhook for partner platforms to get an understanding of when was withdrawal initiated by a user on their platform. 

**Note:** While this requirement was raised by zype this webhook will be created for the complete SDK, any partner can choose to consume it. 

---

**Solution:**
?**

---

## #289 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #290 — Bank account Mandate update
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

## #291 — Amplitude issues
**Status:** Not started | **Last edited:** April 4, 2024 2:09 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #292 — Bajaj KYC Pod Requirements
**Status:** Not started | **Last edited:** April 4, 2024 1:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #293 — E2E Sell-off Productisation 34ae8d3af13a80928d80d8
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

## #294 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #295 — MNRL Compliance Validation Integration
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

## #296 — Account opening STP optimisations
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

## #297 — VKYC Integration PRD
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

## #298 — CKYC Comms for Regulatory Compliance
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

## #299 — Untitled
**Status:** Not started | **Last edited:** April 17, 2025 11:42 AM

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #300 — B2B2C call incoming reduction
**Status:** In progress | **Last edited:** April 17, 2025 11:41 AM

# B2B2C call incoming reduction [Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md) [](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md) # Detailed Breakdown of Customer Call Issues ## Loan Application Issues - **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval. - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times. - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."* - The withdrawal interface appears to lack clear instructions for first-time users. - **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process. - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."* - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs. - **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations. - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."* - The fee structure appears to be disclosed incompletely during the application process. - **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements. - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."* - The eligibility criteria seem inconsistently communicated across different channels. - **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process. - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."* - These timeouts appear to occur most frequently during document upload or verification steps. Payment Processing Issues - **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments. - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."* - These delays severely

---

## #301 — KYC & Mandate Workflow PRD
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

## #302 — CKYC Internal Report
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

## #303 — Analytics setup for MFD channel
**Status:** In progress | **Last edited:** April 10, 2025 11:11 AM

# Analytics setup for MFD channel **Problem Statements:** 1. **Source Identification:** - We currently lack detailed data to distinguish the source platform/interface for applications. Examples include: - Partner Portal Web vs. Partner App - Customer App vs. specific SDKs 2. **SDK Tracking:** - We cannot accurately identify which SDK version or type was used by a partner platform for an application. 3. **TAT Calculation:** - Relying on the audit table for TAT is not ideal for analyzing detailed stage performance. --- ### **Proposed Solutions:** 1. **Source Markers:** - Add unique markers/attributes to application records to identify the origin: - Volt Partner Portal (Desktop) - Volt Partner Portal (Mobile Web) - Volt Customer Web - Volt Customer Mobile App (iOS/Android) - Volt Partner Mobile App (iOS/Android) - SDK (Identify SDK Type/Partner) - Device Type (where applicable) - Application step level - Source (e.g., in the MFD channel where both Partner and Customer may complete steps) 2. **Dedicated TAT Metrics:** - Implement fields/timestamps to capture: - Add Created add of the step , to capture the the First time stage change - **Overall TAT:** From Lead Creation/Customer Registration to Loan Complete status. - **Stage-Level TAT:** Track start times for each key state to calculate the duration spent in each stage (e.g., Start of State A → Start of State B). 3. **Logging for FE UI related bugs:** - Tracking sluggishness on the website - If the Elements fail to load or are stuck

---

## #304 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #305 — PhonePe requirements
**Status:** Done | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #306 — UPI Autopay
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

## #307 — Check eligibility overhaul
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

In context of Check limit page we are solving the following problems

1. UI/UX Problems: 
    1. CTA copy signifies that this is an eligibility test which means not everyone is eligible for loan. 
    2. The main headline occupies too much space. Pushes the form down and deviates user attention from the form. The current headline conveys very little. 
    3. Too much space on the main scroll is left unused. Nothing except the form and headline is visible in the first fold. Pushes trust markers and education content down. 
    4. CTAs that are of now use to user at this stage

**Solution:**
?**

---

## #308 — Measuring Customer Support Events
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

Throughout the journey our users often take support from our RMs who then assist them in completing their application. However we are not able to understand the key milestones or statuses at which customers face problems.

We would be building events on Amplitude throughout the journey where 

To be able to make completely self serve-able journeys, we need to understand these milestones along with the underlying problems/errors/inefficient communications and solve them with product initiatives.

---

**Solution:**
?**

---

## #309 — Template (Duplicate this for new PRDs) - PN
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #310 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #311 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #312 — Ai optimisation in current design workflow
**Status:** Unknown | **Last edited:** Unknown

# Ai optimisation in current design workflow - Prompt SO right now the design process at volt **AI is used by UX pros as a thought partner and reviewer** - Resources https://www.userinterviews.com/ai-in-ux-research-report There is around following major steps when it comes to designing - Problem identification - Prioritisation - Benchmarking - Building a user flow - Working on wireframes - Final design Methodologies for problem identification - User Interviews - Surveys - Synthesis of data - Requirements/Insights from the data Benchmarking - Exploration with competitors - Exploration of layout, components, illustrations Building user flow - User journey map - Information architecture - Technical capabilities - Information per screen and hierarchy - Scoping based on the existing designs Working on wireframes - Visual hierarchy - Communication clarity - Navigation - Need to evaluate screens based on :Navigation Ease, Information Clarity, Error Recovery Final designs - Emotional Triggers, Actionability, Consistency, - Illustration design - Interaction with motion --- ## Problem Identification ### User Research - **Automated data analysis** : Transcription, analysis, and synthesis of user research data. - **Sentiment analysis** to identify pain points from user feedback - **Pattern recognition** to spot recurring issues that humans might miss - **Natural language processing** to extract insights from unstructured user comments ### Desk Research - Scanning research papers on psychology eg. Indians’ behaviour in 2020, market trends Eg. How genZ interacts with money, etc, Understanding fintech domain Eg. Understanding how NACH and UPI Autopay works oversimplified. - Tools https://www.perplexity.ai/ https://consensus.app/ https://elicit.com/ ### Process - Designer/PM will take user interviews with the ‣ using ai to generate questionnaire based on the problem statement at hand. - Ai will help to synthesise the data analysis based on the user interview. # Current design workflow [https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system) # Optimized AI workflow 1. Qualitative data collection - Questionnaire for Surveys and User interviews - Desk research - Tools: Perplexity - Dashboard for CS Tickets - How to build this. ### **1. Centralize All Ticket Data** Export data from Zendesk, WhatsApp, etc. into a single table or sheet. Include fields like user message, date, channel, and status for context. --- ### **2. Analyze with AI (GPT or ML Tools)** Use GPT to extract pain points, tag themes, and identify patterns. Alternatively, use BERTopic or clustering models to detect recurring issues. --- ### **3. Summarize & Visualize Insights** Group findings by theme, volume, and sentiment in a dashboard or table. Highlight

---

## #313 — B2B Theme issues
**Status:** Not started | **Last edited:** Unknown

# B2B Theme issues Charter: Design Initiatives ![image.png](B2B%20Theme%20issues/image.png) ![image.png](B2B%20Theme%20issues/image%201.png) ![image.png](B2B%20Theme%20issues/image%202.png) ![image.png](B2B%20Theme%20issues/image%203.png) Screen recording link: https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1184224081308?sessionReplayId=128b9366-93bd-4630-9872-8f471fdcc59a/1749276669544&sessionStartTime=1749276669543 1. NEED HELP button is not themed properly, Primary Back ground surface color is not looking good. 2. Home icon is blue when it should be in primary color. 3. Profile icon color is also blue? 4. Updating benefits for you section icons 5. Can we check the redendering of font in SDKs Why is Popping in serif? 6. Primary button color changes when user comes to increase limit screen.

---

## #314 — Biometrics addition of 2 screens
**Status:** Developed | **Last edited:** Unknown

# Biometrics addition of 2 screens Charter: LOS Pod # Context We need to add permissions and error pop up for biometrics # Process benchmark design # Figma [https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3591-8894&t=kzwBhN3rHeElEoxX-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3591-8894&t=kzwBhN3rHeElEoxX-11&embed-host=notion&footer=false&theme=system)

---

## #315 — UX Writing for Indian Fintech Users (Volt) – Resea
**Status:** Unknown | **Last edited:** Unknown

# UX Writing for Indian Fintech Users (Volt) – Research & Guidelines # Introduction Designing a UX writing system requires a deep understanding of **local users**, **financial regulations**, and **effective copy practices**. Every label, message, and CTA must inspire confidence and clarity, since <aside> 💡 > *Fintech content design and UX writing is all about building user trust, and it couldn’t matter more when we’re dealing with people’s money.* https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=Fintech%20content%20design%20and%20UX,we%E2%80%99re%20dealing%20with%20people%E2%80%99s%20money > </aside> ## Understanding the Indian Fintech User ### **Trust is paramount** Indian users, especially first-time investors and borrowers, tend to be cautious with new financial services. <aside> 💡 A McKinsey report found that *trust is the primary factor influencing customer adoption and engagement with fintech services* [thence.co](https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=User%20confidence%20is%20the%20degree,and%20engagement%20with%20fintech%20services) </aside> Users need to feel their money and data are safe. UX copy should therefore reassure at every step (e.g. using phrases like “securely powered by XYZ bank” or highlighting RBI oversight) to strengthen this trust foundation. ### **Broad, diverse audience** Volt’s target users include salaried professionals investing in mutual funds, stocks, insurance, bonds, etc. Many are financially savvy to an extent, but there’s a **wide range of literacy** Some may be first-time investors from Tier-2 cities (as seen with apps like Groww), while others are seasoned market participants. Copy must hit a sweet spot where **both novices and experts can understand it easily** <aside> 💡 As one UX guide advises, F*intech UX should prioritize clear, simple language that can be easily understood by both newbies and experts alike* https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=Problem%3A%20The%20financial%20language%20can,to%20understand%20for%20many%20users </aside> This means avoiding heavy jargon and explaining necessary terms in plain language. For example, instead of “lien marking your mutual fund units,” Volt’s app explains it as *“mark your mutual funds as a security with a trusted lender”* immediately clarifying the action. ### Friendly, guiding tone A friendly tone humanizes complex financial tasks – it’s like having a helpful friend explain things rather than a formal banker. However, the tone should also reflect **professionalism** to build credibility; a balance of *professional yet approachable* works well, as Razorpay’s content team describes: their fintech UX writing maintains a *“consistent tone – professional yet approachable”* to serve users dealing with high-stakes transactions ### Attention span and mobile behaviour Remember that Indian users predominantly access fintech services on mobile (Volt is **mobile-first**, as noted). Mobile users skim and scan due to small screens and on-the-go usage. Studies show people read only ~20–28% of text on

---

## #316 — Frontend UI fixes [small]
**Status:** In progress | **Last edited:** Unknown

# Frontend UI fixes [small] Charter: Design Initiatives # Context While watching screen recording i have been noticing small UI frontend fixes that need to be done. List is added below with screenshots. Session recording ID and User ID # Issues ### Mobile number icon **Issue**: There is an unecessary fill on the mobile icon **Fix** remove the fill. **Account id**: 27028d22-2807-428c-9ffa-73e584decd09 **Session recording id:** https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1320386903165?sessionReplayId=34b38273-eb63-45d7-955e-25cbe0d1e8ca/1756790681555&sessionStartTime=1756790681555 ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image.png) ### Surface page color on B2B theme looks very off for many partners - Can we change the surface page to Fill primary? ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%201.png) ### Wrong logo I have seen we are using the wrong logo for DSP Finance in many of our communications. ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%202.png) ### Avg time on Anchor page is - 10s ### Time take to get OTP is 8-9s for MFC fetch # Figma

---

## #317 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #318 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #319 — Loan Offer page
**Status:** In progress | **Last edited:** Unknown

# Loan Offer page Assign: Karuna Sankolli Charter: Design Initiatives Priority: P0 # Context [Product Note : Post limit fetch optimisation](Loan%20Offer%20page/Product%20Note%20Post%20limit%20fetch%20optimisation%20268e8d3af13a8008a6b5c4b85b092305.md) [📄 Loan Offer Funnel Optimisation Document](Loan%20Offer%20page/%F0%9F%93%84%20Loan%20Offer%20Funnel%20Optimisation%20Document%2027ce8d3af13a808c9d5efd10821ccf2e.md) # Process # Figma

---

## #320 — Loan foreclosure reasons
**Status:** Developed | **Last edited:** Unknown

# Loan foreclosure reasons Assign: Karuna Sankolli Charter: LMS Pod # Context - [x] Get list of reasons from Ranjan - [x] Make a table with what we will sell for every reason selected. - [x] Redesign FAQs page - [ ] Work with Ranjan for the FAQs page - [ ] Foreclosure landing page 3 options - [ ] Reasons for foreclosure 3 options - [ ] Reconsider page 3 options - [ ] Status of payment page 3 component 3 options - [ ] Last tracking foreclosure page options - [ ] Ability to cancel foreclosure --- [Capture foreclosure reasons from customer](../PRDs/PRDs/Capture%20foreclosure%20reasons%20from%20customer%20170e8d3af13a80ec8d7bff6a6e988d1f.md) ‣ # Figma [https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system)

---

## #321 — MFD UI screen exploration
**Status:** Deprioritised | **Last edited:** Unknown

# MFD UI screen exploration Charter: MFD Pod # Context Post fetch, offer screen. HMW optimise for faster TAT. Not club and make is a non linear journey. https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6090-1797&t=MmlJYS7TFHPgzhgQ-11 https://whimsical.com/mfd-board-SQzR6Ph8GAR7cMj6RtBVfL # Process - [ ] Benchmarking - [ ] Explorations # Figma

---

## #322 — Pre fetch optimisation
**Status:** Ready for kickoff | **Last edited:** Unknown

# Pre fetch optimisation Charter: LOS Pod Priority: P0 Task type: Sprint # Context - Need replace DOB input with mobile number before MFC fetch since it is unnecessary and has drop offs - [Pre-fetch flow Optimisation: Consolidating PAN flow](../PRDs/PRDs/Pre-fetch%20flow%20Optimisation%20Consolidating%20PAN%20flow%20207e8d3af13a80e2b744f8bd135a6319.md) # Process # Figma

---

## #323 — Events
**Status:** Unknown | **Last edited:** Unknown

# Events Below is an event strategy document for Volt Money, based on the flow and details you provided. The table format includes event name, priority, expected values, and comments on the event's current status. This document is structured to track events from user interactions to backend processes. --- ### Event Strategy Document for Volt Money Certainly! Below is a comprehensive table that outlines the various user flows, actions, corresponding event names, detailed descriptions, and the user journeys they belong to. This should help in tracking and understanding user interactions within your application. | **User Flow** | **User Action** | **Event Name** | **Description** | **User Journey** | | --- | --- | --- | --- | --- | | **Onboarding** | User views onboarding page | ONBOARDING_PAGE_VIEWED | The user has viewed the onboarding page. | Onboarding | | **Onboarding** | First time the app is loaded | LAUNCH_PAGE_VIEWED | The user has launched the app for the first time and viewed the splash screen. | Onboarding | | **Signup** | User Signup on Volt Android | SIGNUP_PAGE_VIEWED | The user has viewed the signup page on the Volt Android app. | Signup | | **Signup** | When user lands on enter OTP page from signup page | SIGNUP_OTP_PAGE_VIEWED | The user has navigated to the OTP entry page from the signup page. | Signup | | **Signup** | When user clicks on T&C, Privacy Policy on signup screen | SIGNUP_T&C_BUTTON_CLICKED | The user has clicked on the Terms & Conditions or Privacy Policy buttons on the signup screen. | Signup | | **Signup** | When user clicks on edit button on enter OTP screen | EDIT_PHONE_BUTTON_CLICKED | The user has clicked the edit button on the OTP entry screen to modify their phone number. | Signup | | **Signup** | When user clicks on resend OTP button on OTP screen, capturing resend attempts | RESEND_OTP_BUTTON_CLICKED | The user has clicked the resend OTP button on the OTP entry screen. | Signup | | **Signup** | When user enters invalid OTP | INVALID_OTP_ENTERED | The user has entered an invalid OTP during signup. | Signup | | **Signup** | When new user is created | SIGNUP_COMPLETED | The user has successfully completed the signup process and a new user account has been created. | Signup | | **Signup** | When user lands on page to select email for signup

---

## #324 — Selfie capture journey
**Status:** Unknown | **Last edited:** Unknown

# Selfie capture journey In the Tata journey, we have a step to capture a selfie, but this is not included in the Bajaj journey. While the selfie feature is part of the Bajaj Figma design, it is neither implemented in production nor required. **User Flow for Selfie Capture (Bajaj Journey):** 1. The user sees a "Click Selfie" button, which activates the front camera after obtaining permission. 2. If an MFD creates the application, they can share a link with the customer. 3. The customer flow is as follows: - MFD shares the link with the customer. - Customer receives the link and opens it. - Customer logs in by verifying their phone number and entering the OTP. - The customer continues the application, completes KYC, and provides camera permissions. - Customer clicks the "Click Selfie" button, captures, and uploads the selfie. - Once the selfie is verified, the customer proceeds to the next steps.

---

## #325 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #326 — LSQ Leedsquared
**Status:** Unknown | **Last edited:** Unknown

# LSQ: Leedsquared @Naman Agarwal ### **Overview** LeadSquared (LSQ) is a comprehensive Customer Relationship Management (CRM) tool primarily used by Volt Money to manage lead generation, customer interactions, and the loan application process. LSQ enables sales teams and Relationship Managers (RMs) to track customer journeys, from lead acquisition to loan approval, providing a centralized view of lead data, customer details, and application stages. --- ### **Framework: Business Impact of LSQ** ### 1. **Purpose/Objective** LSQ’s core objective is to **streamline lead management** and **enhance customer support** by providing sales teams with real-time access to lead information and loan application statuses. By organizing customer interactions and loan data in one place, LSQ improves the efficiency and transparency of the sales process, enabling better decision-making and quicker responses to customer needs. ### 2. **Key Features & Functions** | **Feature** | **Description** | | --- | --- | | **Lead Management** | LSQ tracks customer leads from acquisition to conversion, providing visibility into lead status, ownership, and data. | | **Loan Application Tracking** | Displays the current stage of loan applications (e.g., CIBIL check, KYC, approval), helping RMs manage their pipeline. | | **Customer Data Storage** | Stores critical customer details such as name, email, phone number, and loan amounts, enabling personalized outreach. | | **Sales Performance Insights** | Generates reports on lead outreach, conversion, and sales performance, helping teams optimize their strategies. | ### 3. **Business Benefits** - **Improved Lead Conversion**: LSQ helps RMs track the progress of leads efficiently, ensuring no customer falls through the cracks and allowing for timely follow-ups. - **Increased Transparency**: By providing a clear view of each lead’s stage in the loan application process, LSQ reduces ambiguity and improves decision-making. - **Enhanced Customer Support**: Real-time access to customer details and loan data allows RMs to provide more informed and tailored support during customer interactions. ### 4. **Challenges/Current Gaps** - **Lead Stage Sync Issues**: Discrepancies between the stages in LSQ and Volt Money's backend systems can lead to confusion and mismanagement of leads. - **Missing Loan Details**: Critical loan information like Processing Fees (PF), Rate of Interest (ROI), and Sanction Limits are not always available in LSQ, affecting RMs' ability to assist customers. - **Manual Data Updates**: Admin actions (e.g., changes to customer data) are not automatically reflected in LSQ, which can lead to outdated records and inefficiencies. ### 5. **Opportunities for Improvement** - Lead prioritisation - **Automating Data

---

## #327 — LaMF funnel
**Status:** Unknown | **Last edited:** Unknown

# LaMF funnel To document a funnel from a product manager's perspective, especially for opening a credit line with multiple third-party APIs involved, you can follow these steps: ### 1. **Define the Funnel Stages** - **Map the key stages** of the funnel from a user’s perspective. Each stage should represent a meaningful user action: 1. ### 2. **Identify Touchpoints & Third-Party API Dependencies** - **For each stage**, document which third-party API is involved and what data is exchanged. - **E.g.,** ### 3. **Track Conversion & Drop-off Metrics** - At each stage, define **conversion rate** (users who successfully pass to the next stage). - **Identify drop-offs**: Calculate how many users fail or exit the flow at each stage and investigate why. - **E.g., Eligibility Check** → 75% conversion, 25% drop-off due to API failure or ineligible users. ### 4. **Diagnose Breakpoints & Flow Bottlenecks** - **API Response Failures**: Track the rate of success and failure for API calls (e.g., timeout, invalid responses, high failure rate in the KYC stage). - **User Frustration Points**: Analyze user sessions to find out if there are UI/UX challenges (e.g., users leave due to complex form submissions or unclear messaging). - **Incomplete User Inputs**: Check if the flow is breaking due to missing or invalid user input (e.g., incorrect document uploads or failed validation). ### 5. **Attribution of Drop-offs** - **Tag each drop-off** with an attribution reason: 1. **Technical** (API failure, timeout, or 500 error). 2. **User Behavior** (abandonment, confusion with next steps). 3. **Eligibility** (e.g., failed credit check or ineligibility). ### 6. **Major Pain Points** - **Highlight user pain points** by reviewing feedback, support tickets, and analytics. - **E.g., KYC Step**: Users frequently abandon due to the complexity of document uploads. - Use qualitative feedback (e.g., user interviews, support chats) alongside quantitative data (e.g., Google Analytics, session recordings). ### 7. **Set Up Conversion Tracking** - Use **attribution tools** to track how users are progressing through the funnel, and set up **event tracking** in Google Analytics or similar. - **For each stage**, track key metrics like: 1. Average time spent. 2. Bounce rates. 3. API success/failure rates. ### 8. **Monitor Real-Time Data** - Implement **dashboards** that allow you to monitor API response times, error rates, and user journeys in real-time. - Example tools: **DataDog** for API monitoring, **Hotjar** for session recording, **Google Analytics** for user tracking. ### Example Documentation Flow: ``` 1. Stage 1: User Signup

---

## #328 — Missed calls from customers aren't being called ba
**Status:** Unknown | **Last edited:** Unknown

# Missed calls from customers aren't being called back or addressed # Missed Calls and Customer Support Optimization Missed calls from customers are a significant issue, as many are not being addressed. Customers reach out to us for help during various stages, such as onboarding, opening credit lines, post-account opening support, or product inquiries. To effectively manage these requests and reduce missed calls, we need a strategy that not only addresses customer needs but also balances the cost of support channels. ## Understanding the Support Categories: We can categorize customer interactions into three key areas: 1. **Awareness**: Customers seek to understand the product better. 2. **Sales**: Customers eligible for the service but who have not yet opened an account. 3. **Support**: Customers who already have accounts and need assistance with specific issues. ## Support Channel Options: There are several ways we can provide support, each with its own cost and effectiveness: - **Online Documentation**: Free but less accessible for most users. - **Product Journey (In-App Help)**: Accessible but costly in terms of development time. - **Chat Support**: Affordable and accessible for general queries. - **Call Support**: Highly impactful but also the most expensive to maintain. ### Optimizing Customer Support: Our goal is to provide the right support channel for each category of customer, depending on their needs, to maximize effectiveness while minimizing costs. This means segmenting customers into "buckets" based on their status and needs and directing them to the appropriate support channel: | **Bucket** | **Identifier** | **Channel to Retarget** | | --- | --- | --- | | **Awareness** | No record of the number in the system, ineligible | Chat or WhatsApp | | **Sales** | Eligible number, account not yet opened | Call Support | | **Support** | Customer with an open account | Chatbot with common services | ### Proposed Changes: To reduce call support costs, we should remove the call option for ineligible customers and instead provide them with WhatsApp support. This will help to ensure that calls are only directed to customers who are further along the funnel, and likely to require higher-touch support. ### Key Objectives: - **Address customer needs** through the appropriate support channels. - **Reduce support costs** by minimizing unnecessary call support. - **Reduce missed calls and errors** by routing customers more effectively. ### Data Requirements: To implement this strategy, we need to collect and analyze the following data: -

---

## #329 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #330 — Sales team is calling customers who complete the j
**Status:** Unknown | **Last edited:** Unknown

# Sales team is calling customers who complete the journey on their own To maximize the efficiency of our sales team and ensure that our limited resources are used effectively, we aim to distinguish between customers who genuinely need assistance and those who can self-serve. By enabling our sales team to focus on "struck" customers—those facing difficulties in the application or onboarding process—we can optimize our support efforts, increase customer satisfaction, and drive higher conversion rates. ## Strategy: We are building a **customer classifier** that will automatically detect whether a customer is "stuck" in the journey or can self-serve. This will allow our CRM to prioritize customers based on their likelihood to convert or their need for human assistance. By focusing on high-priority leads, we can drive better performance with the same resources. ### Key Steps: 1. **Develop a Classifier**: - Build a mechanism that identifies "struck" customers based on their interaction with the platform. This classifier will be able to distinguish between users who are struggling and those who can proceed independently. 2. **Highlight in CRM**: - Integrate the classifier with our CRM system to ensure that sales representatives are notified in real-time when a customer is identified as "stuck." The CRM should highlight these customers, offering the sales team clear, actionable insights. 3. **Update Sales Incentives**: - Modify the incentive structure for sales executives to align with the new system, rewarding them for focusing on and resolving cases where their intervention is truly needed. ## Identifying "Struck" Applicants: To accurately identify struck customers, we will deploy the following tactics: - **Telemetry on Errors**: - Implement error tracking throughout the customer journey. If a customer encounters a technical problem (e.g., form submission fails, API error), they will be flagged as "struck." - **Abandoned Journey**: - Monitor customer activity in real-time. If a user abandons a critical stage of the application process (e.g., KYC, loan application) for more than 30 minutes, they will be marked as "stuck." - **Custom Rules**: - We will determine additional logic based on further data analysis and customer feedback to enhance the classifier. ### Classifier Logic: The classifier's logic will be based on a combination of: - **User behavior telemetry** (e.g., error reports, time spent on a task). - **Abandonment tracking** (e.g., inactivity beyond a defined threshold). - **Data-driven insights** (e.g., patterns in customers’ prior journeys that lead to successful or failed conversions). ### CRM

---

## #331 — One Pagers
**Status:** Unknown | **Last edited:** Unknown

# One Pagers [OP - Selloff and Withdrawal request mismatch](One%20Pagers/OP%20-%20Selloff%20and%20Withdrawal%20request%20mismatch%20106e8d3af13a808cbebffae82d466652.md) [**Handling Discrepancies Between Assumed and Actual Limits**](One%20Pagers/Handling%20Discrepancies%20Between%20Assumed%20and%20Actual%20%20106e8d3af13a80748d1cd01661d83138.md) [Missed calls from customers aren't being called back or addressed](One%20Pagers/Missed%20calls%20from%20customers%20aren't%20being%20called%20ba%207dfeec301f004c0586694a51de935466.md) [Sales team is calling customers who complete the journey on their own](One%20Pagers/Sales%20team%20is%20calling%20customers%20who%20complete%20the%20j%2010ae8d3af13a80e4ba2af4aee3ad9ee8.md) [LaMF funnel ](One%20Pagers/LaMF%20funnel%2010ae8d3af13a80ef8b19ccc25e547569.md) [LSQ: Leedsquared](One%20Pagers/LSQ%20Leedsquared%20119e8d3af13a80a0b441ed3d3b464180.md) [MFD Payout dashboard ](One%20Pagers/MFD%20Payout%20dashboard%20120e8d3af13a80f5980de9438ff2e277.md) [Periskope](One%20Pagers/Periskope%20120e8d3af13a80b9ad82c524050ef3a2.md)

---

## #332 — E2E Sell-off Productisation V1
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

## #333 — Additional details enhancement
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

## #334 — Analytics requirement for amortisation of PF
**Status:** Pending review | **Last edited:** Unknown

# Analytics requirement for amortisation of PF Last Edited: April 24, 2026 8:59 AM PRD ETA: April 24, 2026 PRD Owner: Vaibhav Arora # **1. Objective** Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module. The design must be extensible to accommodate other fee/cost types in future iterations without structural rework. # **2. Scope & Exclusions** ## **2.1 In Scope** - Product lines: LAMF, LAS, Term Loan (TL) - Charge type: Processing Fee (PF) - Accounting entries: Income recognition at monthly amortisation level - Amortisation method: Straight Line Method (SLM) - Report period: M-N (N>0) (previous calendar months only) - Waiver handling: Partial and complete waivers with corresponding reverse entries - Loan closure handling: Remaining balance acceleration on closure date ## **2.2 Explicitly Out of Scope** - GST component of processing fee excluded from amortisation entries - Current month entries - report is strictly retrospective - Real-time or intra-month amortisation schedules # **3. Source Data & Key Fields** All data will be sourced from the accounting report. The following fields are required at a schedule/charge level: | **Field** | **Source / Table** | **Notes** | | --- | --- | --- | | FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier | | Client External ID | LMS – Loan Master | FXCID reference | | Product Type | LMS – Loan Master | LAMF / LAS / TL | | Charge Application Date | LMS – Fee Schedule | Date PF was applied | | PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only | | Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference | | Loan Status | LMS – Loan Master | Active / Closed | | Closure Date | LMS – Loan Master | Populated only if loan is closed | | Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator | | Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee | | Waiver Date | LMS – Waiver Log | Date waiver was applied | | Waiver Type | LMS – Waiver Log | Partial /

---

## #335 — BRD Enhancements to Schedule & Derived Details Pro
**Status:** Completed | **Last edited:** Unknown

# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds) Last Edited: December 11, 2025 2:41 PM PRD Owner: Vaibhav Arora ## **1. Problem Statement** Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for: - Accurate repayment allocation - DPD computation - Interest/charge tracking - Reconciliation, reporting (internal and external) Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations. We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur. --- ## **2. Context: How It Should Work (High Level)** - Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule. - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule - When a transaction settles that obligation, the schedule and derived details should reflect: - obligation met - amount accounted - linkage to the transaction identifier - timestamps for audit - For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.). Finflux already follows this pattern for regular repayments. The gaps occur only for specific transaction types listed below. --- ## **3. Issues & Required Enhancements** --- ## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details*** ### **Current Behaviour** - During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line: - Accrued-but-not-yet-due interest is first made due. - Finflux then settles this newly created due using excess funds when the clear dues API is hit - However: - The **schedule table is not updated** to reflect the new temporary obligation. - The **obligation is not marked as met**. - **Derived details** are not populated with the settlement transaction. ### **Impact** - Reporting discrepancies (interest recognised vs. interest settled). - Incorrect DPD because obligations appear “unmet”. ### **Required Behaviour** Finflux should: 1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge). 2. **Immediately settle the obligation** and mark: - obligation_met = true - obligation_met_on = timestamp 3. **Populate derived details** with: - linkage to the

---

## #336 — Banking partner finalization
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #337 — Charge details on Command centre
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

## #338 — Colending Disbursement and Charge knock off
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

## #339 — Collateral release enhancement
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #340 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #341 — Dishonour charge enhancement
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

## #342 — Enhancing Collections Efficiency Through Mid-Month
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #343 — FD Fixerra
**Status:** Unknown | **Last edited:** Unknown

# FD: Fixerra Last Edited: December 1, 2025 2:13 PM ### Product Alignment Note – Fixerra FD Offering via Partner Dashboard *(DSP Finance × Volt Platform)* --- ### **Problem statement** Volt x DSP have a strong distribution via IFAs, we want to experiment distribution of different products via this channel, because of DSP Finance (NBFC) is looking to expand its retail investment footprint beyond LAMF (Loan Against Mutual Funds) by introducing a Fixed Deposit (FD) product. On the Volt platform today, distributors (primarily MFDs) only have LAMF as the monetizable product. While LAMF has strong unit economics, it is not a top-of-funnel product for retail customers. Fixerra provides the underlying FD product and infrastructure. The hypothesis is: - We already have arms-reach access to a large base of customers with mutual fund holdings. - These customers have a natural affinity for low-risk investment instruments. - FDs can act as a trust-building, widely accepted entry product, opening the funnel for both direct revenue (FD) and future LAMF conversions. This note outlines the scope for v1 of FD origination and servicing through the Volt Partner Dashboard, and is intended to align stakeholders across DSP Finance, Volt, and Fixerra. --- ### 2. Problem statement ### 2.1 Current state - MFDs on Volt can only offer LAMF. - Monetization is limited to one product with a relatively narrow target audience. - No simple “safe” product exists to attract or engage a wider customer base. - Distributors lack tools to deepen customer relationships beyond MF transactions. ### 2.2 Opportunity Introducing FDs: - Expands the product portfolio for MFDs. - Helps create a trust-led entry point (“mouth of the funnel”), improving conversions into higher-ticket products like LAMF. - Offers DSP Finance a scalable retail deposit base. - Allows Fixerra to distribute its FD product through MFD networks. --- ### 3. Product hypothesis **FDs can become a high-trust, low-friction product that increases distributor engagement and revenue, while simultaneously opening the pipeline for LAMF upsell.** Supporting hypotheses: 1. Customers with MF holdings are more likely to evaluate FD products with high confidence. 2. MFDs will be able to deepen their relationship and improve overall earnings by offering a broader product suite. 3. The NBFC can explore differentiated FD structuring based on distribution performance (for example, special rates, bulk programs). --- ### 4. High-level GTM - **Channel:** Volt Partner Dashboard - **Actors:** Mutual Fund Distributors on Volt - **v1

---

## #344 — Finflux Product Setup for Co-Lending
**Status:** Completed | **Last edited:** Unknown

# Finflux Product Setup for Co-Lending Last Edited: March 19, 2026 9:44 PM PRD ETA: January 27, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context As part of the co-lending setup, loans are economically split between: - **10% exposure (CLA portion)** - **90% exposure (TCL)** - **100% loan representation** required for operational and accounting purposes Current state: - Finflux is running on a **single instance** supporting **OD and TL products** - All reporting, accounting, SMA/NPA tagging, and operational workflows are currently **instance-scoped** - Finflux manages collateral and exposure deduplication The setup needs to support: - Fast go-live - Clean accounting - Correct delinquency signaling to TCL - Minimal disruption to existing production flows --- ## 2. Problem Statement The co-lending structure introduces multiple complexities: - **Collateral deduplication risk** if multiple loans referencing the same securities exist in the same instance - **Client-level SMA/NPA contagion**, where delinquency in a small CLA exposure may impact unrelated production loans - **Accounting segregation** required across different exposure types - **Operational overhead** introduced by multiple Finflux instances - **Reporting and reconciliation complexity** across LMS, Finflux, and TCL --- ## 3. Design Options Considered ### Option A: Single Finflux Instance with Multiple Products - All co-lending loans (10% and 100%) reside in the same instance - Separation handled purely via product-level configurations **Challenges** - High risk of collateral dedupe conflicts - Client-level NPA impact across all loans - Heavy reliance on product-level filters across reporting and accounting - Higher regression risk for existing OD and TL products --- ### Option B: Multiple Finflux Instances for All Co-Lending Loans - Separate instances for 10% and 100% loans **Challenges** - Higher setup and maintenance effort - Configuration and version-sync risks - Increased reporting and reconciliation overhead - Multiple operational points of failure at launch --- ## 4. Final Recommendation (Chosen Approach) **Recommended Setup** - **10% co-lending loan (CLA exposure)** → Booked in the **existing Finflux instance** - **100% loan** → Booked in a **separate Finflux instance** - **90% exposure** → Booked in **TCL** This approach optimizes for **lower effort, faster go-live, and controlled risk**, while keeping core production flows isolated. --- ## 5. Rationale for the Recommendation ### 5.1 Faster Go-Live with Minimal Change Surface - Existing Finflux instance already supports: - Live products - Accounting - Reporting - Monitoring - Adding a **single CLA product (10%)** is significantly lower effort than: - Standing up and

---

## #345 — IFSC addition Account opening enhancement
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?’**

Every day, over 200 customers apply for a loan. For 1–3 of these customers, the IFSC is missing in Finflux, our core lending platform. Currently, adding a missing IFSC requires raising a support ticket to the Finflux team, which takes 3–4 working hours.

This manual dependency directly delays account opening, increases operational overhead, and negatively affects the customer experience and turnaround time (TAT).

---

**Solution:**
?**

We will be integrating with the Finflux add IFSC insert API, whenever a client creation is stuck due to a missing pin code exception, we will get details from Digio’s IFSC detail API to update into the LMS

---

## #346 — LAS CMS Confiscation and sale of securities
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

## #347 — LAS CMS Lodgement
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

## #348 — LAS CMS Unlodgement
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

## #349 — PMR consumption SHCIL
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

## #350 — LAS Collateral management system
**Status:** Completed | **Last edited:** Unknown

# LAS: Collateral management system Last Edited: July 28, 2025 8:43 PM PRD ETA: June 27, 2025 PRD Owner: Vaibhav Arora # **What is CMS?** The Collateral Management System (CMS) will act as the central infrastructure for managing pledged shares for a Loan Against Shares (LAS) product. It will interface with the Loan Origination System (LOS), Loan Management System (LMS), and Depository Participant (DP) — SHCIL — to manage the full lifecycle of collateral from validation to lien marking, valuation, revocation, and reconciliation. It will also include risk management via real-time LTV monitoring, handling of corporate actions, and tools for operations teams. [CMS system architecture](https://claude.ai/public/artifacts/b5a68c3c-4705-4c9d-b34b-52a1d6bb8ec4) --- # Why do we need a CMS? A **Collateral Management System (CMS)** is essential for a **Loan Against Shares (LAS)** product because collateral (in the form of pledged shares) is **the core security** backing the loan. Without an automated, secure, and integrated system to manage this collateral, the business is exposed to **operational risk, financial risk, and regulatory gaps**. 1. Centralised tracking and management of collaterals: Currently all collaterals are managed by the LMS which makes it very risk prone: A CMS ensures each step is trackable, audit-logged, and consistent with external systems (DP/SHCIL) and internal ones (LMS/LOS). 2. CMS constantly monitors Loan-to-Value (LTV) ratios. If share prices fall, LTV breaches can be automatically flagged (exposure tracking), triggering margin calls or partial lien revocation. 3. Logic separation from LMS: CMS has a lot of collateral management intelligence which should be LMS agnostic, this will make our LMS very modular and easily replaceable since majority of the complexity of collateral management will be handled via CMS. --- # **How are others solving this problem?** The approach to collateral management for Loan Against Shares (LAS) varies widely across the lending ecosystem, largely depending on a company’s scale, tech maturity, and risk appetite. Broadly, solutions fall into two categories: ### 1. **Tightly Coupled CMS-LMS Systems (Usually Vendor-Provided)** Some lenders use **end-to-end lending platforms** where the CMS is embedded within the LMS — often provided by a third-party vendor. These platforms offer: - Pre-integrated lien workflows - Basic LTV tracking - Unified borrower and collateral view ### 2. **No CMS — Operations-Led Collateral Tracking** Most early-stage or mid-sized lenders operate without a dedicated CMS. Instead, they rely on: - Manual **ops processes** to initiate and track lien/revocation files - **Excel sheets or shared dashboards** to monitor pledged ISINs

---

## #351 — LSP Presentation enhancement for externally regist
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

## #352 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #353 — NBFC PG Evaluation
**Status:** Unknown | **Last edited:** Unknown

# NBFC PG Evaluation Last Edited: April 8, 2025 1:06 PM PRD Owner: Surya Ganesh # Evaluation Criteria ## Business Criteria | Parameter | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | | Same day Settlements | No | No | No | No | | UPI Commercials | | | | | | Netbanking Commercials | | | | | | VISA Commercials | | | | | | Mastercard Commercials | | | | | | | | | | | ## Product Criteria | Parameter | Priority | RazorPay | PhonePe | PayU + HDFC | Easebuzz | | --- | --- | --- | --- | --- | --- | | No user login (OTP) | High | No | Available (Standard checkout flow doesn't require user login) | | | | Transaction level control on payment methods | High | | Available (Can specify payment instruments in the payment initiation request) | | | | Transaction level control on card networks | High | | Available (Can filter specific card networks in payment instruments) | | | | Customer name at transaction level | High | | | | | | Backend callback post transaction level | High | | Available (Via callbackUrl parameter in payment request) | | | | Ability to whitelist multiple URLs | High | | Available (Can configure multiple callback and redirect URLs) | | | | White-labelling of checkout | High | | Limited (PhonePe branded checkout but some customization options) | | | | Error codes and reasons at transaction level | High | | Available (Detailed error codes in status responses) | | | | Settlement webhook | Medium | | Available (Supports settlement notifications) | | | | TPV check for UPI transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for DC transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for Netbanking transactions | High | | Available (Transaction status API provides verification) | | | ## Operations Criteria | Parameter | Priority | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | --- | | Settlement timeline | High |

---

## #354 — NESL report
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #355 — PMR consumption
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?

Today, Pledge Master Reports (PMRs) are received over email at [collaterals@dspfin.com](mailto:collaterals@dspfin.com). The ops team shares these with engineering, who manually hit an API to consume the report - creating an operational bottleneck that directly impacts loan account opening timelines for the Loan Against Shares (LAS) program.

We need to eliminate this manual handoff by automating PMR ingestion the moment the email arrives, while preserving a checker workflow for validation and audit.

In a Loan Against Securities (LAS) setup, collateral positions are dynamic se

**Solution:**
?

---

## #356 — Pincode addition Account opening enhancement
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?’**

Every day, over 200 customers apply for a loan. For 4–5 of these customers, the pincode is missing in Finflux, our core lending platform. Currently, adding a missing pincode requires raising a support ticket to the Finflux team, which takes 3–4 working hours.

This manual dependency directly delays account opening, increases operational overhead, and negatively affects the customer experience and turnaround time (TAT).

Why do we need to store pin codes in Finflux?
User’s state is important as a context in the LMS (Accounting module) to ensure that the GST that is applied o

**Solution:**
?**

We will be integrating with the Finflux add Pincode API, whenever a client creation is stuck due to a missing pin code exception, we will get details from the user’s KYC details (KYC utility) to push into the LMS and retry account opening

---

## #357 — Product Note Interest Refund via Credit Note
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**What specific problems are we solving?**

1. **Slow Resolution Time:**
    - Interest refund requests take 2-3 days to resolve from initiation to completion
    - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times
    - Delays compound when requests require back-and-forth clarifications between operations, e

# Product Note: Interest Refund via Credit Note Last Edited: January 23, 2026 8:15 PM PRD ETA: July 22, 2025 PRD Owner: Vaibhav Arora ## Background and Context **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged or goodwill interest waivers - Operations team processing interest refunds/waivers - Finance team managing manual accounting entries for interest reversals - Tech ops/Product handling backend interventions for interest adjustments **What is the challenge that they are facing? What is broken today?** - Interest refunds and waivers currently require manual engineering intervention through backend APIs or direct Finflux access - Process is operationally intensive with dependency on Jira ticket workflows - No standardized maker-checker workflow for interest refunds similar to charge refunds - Manual JV posting for interest reversals creates additional overhead for Finance team - Lengthy resolution time (2-3 days) impacting customer experience - No automated validation mechanism to prevent duplicate interest waivers or refunds for the same period - Lack of visibility and tracking for interest refund requests across the loan lifecycle **Why is it important? What is getting impacted?** - Customer satisfaction is negatively impacted due to delayed resolution of legitimate interest refund requests - Operational inefficiency with high manual effort required for each interest refund case - Risk of errors and duplicate processing without systematic validations - Finance team bandwidth consumed by repetitive manual JV entries - Lack of audit trail and reconciliation capabilities for interest reversals - Inconsistent treatment of interest refunds compared to the now-standardised charge refund process --- ## 1. Problem Scope ### In scope **What specific problems are we solving?** 1. **Slow Resolution Time:** - Interest refund requests take 2-3 days to resolve from initiation to completion - Customers awaiting legitimate refunds (due to calculation errors, goodwill adjustments, or service recovery) experience extended wait times - Delays compound when requests require back-and-forth clarifications between operations, engineering, and product 2. **Operational Bottleneck and Dependency:** - Operations teams cannot independently process interest refunds or waivers - Every interest adjustment requires raising a Jira ticket and waiting for engineering/product team intervention - Backend access and API calls are needed for what should be a routine operational task - Process creates unnecessary dependencies across multiple teams for resolution 3. **Risk of Duplicate Processing:** - No systematic validation exists to check if interest for a specific period has already been waived or refunded - Product team rely

---

## #358 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #359 — Product note Credit note for TL
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

We are solving:

# Product note: Credit note for TL Last Edited: April 28, 2026 4:45 PM PRD ETA: April 17, 2026 PRD Owner: Vaibhav Arora # **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)** --- ## **Background and Context** **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged interest - Operations team handling refund/waiver requests - Finance team managing manual income reversals and reconciliation - Product/Tech teams currently intervening via backend/API --- **What is the challenge today?** - Interest refunds require **manual intervention via engineering or Finflux access** - No standardized **maker-checker workflow** - **Not supported for Term loans, currently productised and implemented only for OD** - Manual JV posting required for income reversal - No **system-driven dedupe or validation** - No **tranche-level visibility or audit tracking** - Turnaround time is **2–3 days**, impacting CX --- **Why is it important?** - Poor customer experience due to delays - High operational dependency and inefficiency - Risk of duplicate or incorrect refunds - Manual accounting overhead for finance - Lack of audit trail and reconciliation visibility --- ## **1. Problem Scope** ### **In Scope** We are solving: ### **1. Operational Independence** - Enable Ops to process **interest refunds without engineering dependency for Term loans** - Introduce **maker-checker workflow** --- ### **2. Standardized Accounting** - Eliminate manual JV posting - Introduce **credit note + automated income reversal** --- ### **3. Tranche-Level Refund Handling** - Refunds applied at **tranche level (not line level)** - Excess created is: - Initially **tranche-tagged** - **Not usable across tranches while tranche is active** - Becomes **line-level usable only after tranche closure** --- ### **4. Validation & Dedupe** - Prevent duplicate refunds via: - Schedule validation - Credit note existence checks --- ### **5. Audit & Traceability** - Full linkage: - Interest → Credit Note → JV - Tranche-level enrichment and reporting --- ### **Out of Scope** - Principal refunds - Bulk refund processing - Automated eligibility rules - Reversal of incorrect refunds (no reversal flow) --- ## **2. Success Criteria** ### **Outcomes** - Maker → Checker → Accounting completion within **1 hour** - **>90% reduction** in Jira dependency - Capability to refund interest for Term Loan - **Zero duplicate refunds** at tranche-month level --- ### **Post-launch Good State** - All refunds processed via maker-checker - Credit notes posted correctly at tranche level - Automated JV posted for income reversal - Finance can reconcile via

---

## #360 — Product note Foreclosure (Colending)
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure (Colending) Last Edited: May 19, 2026 2:47 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**. ### Who is impacted - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting ### What is broken today Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations: 1. **Incorrect foreclosure simulation** Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances. 2. **Pending transaction inconsistencies** Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations. 3. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring that: - Loan 90 and Loan 10 are closed - All charges and interest are posted - Excess settlement is completed 4. **Penalty and applicable charge dependency** Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment. 5. **Incorrect collateral release timing** Securities may be released before confirming that **both loan legs are closed**, which introduces risk. ### Why this is important Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to: - Incorrect payoff amounts shared with borrowers - Operational rework due to partial closures - Accounting mismatches across loan legs - Risk of releasing collateral before loan closure creating financial exposure for the NBFC This PRD defines a **colending foreclosure workflow** that ensures: - Correct payoff simulation - Transaction sequencing across loan legs - Controlled collateral release - Accurate excess settlement. --- # **1. Problem Scope** ## **In Scope** ### **Colending foreclosure simulation** Foreclosure simulation will incorporate balances from: - Loan

---

## #361 — Product note Foreclosure V2 for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure V2 for Colending Last Edited: April 24, 2026 7:43 AM PRD ETA: April 7, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across Loan 90 and Loan 10 in the Colending Loan Management System (CLMS). --- ### **Who is impacted** - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting --- ### **What is broken today** 1. **Incorrect foreclosure simulation** Foreclosure amounts are often computed using Loan 100 without fully reconciling Loan 90 and Loan 10 balances. 1. **Pending transaction inconsistencies** Foreclosure may be initiated even when pending transactions exist in CLMS, leading to incorrect payoff calculations. 1. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring: - Loan 10 and Loan 90 are closed - All dues and interest are settled - Excess is correctly handled 1. **Penalty and applicable charge dependency** Charges (such as penal charges) may be posted after repayment due to system jobs, leading to foreclosure failures. 1. **Incorrect collateral release timing** Collateral may be released before confirming closure of underlying loan legs. 1. **Excess handling gap in colending** - Excess is parked in Loan 100 - Excess does not auto-settle dues or accrued interest - There is no native way to use excess during foreclosure This leads to: - Incorrect net payable shown to users - Failed foreclosure despite sufficient excess - Manual intervention for settlement - Reconciliation gaps --- ### **Why this is important** Foreclosure is a **high-intent and customer-sensitive journey**. Incorrect handling leads to: - Poor customer experience - Increased operational workload - Financial and accounting mismatches - Risk of incorrect collateral release This PRD ensures: - Accurate payoff computation - Deterministic transaction sequencing - Proper utilization of excess - Correct closure and refund handling --- # **1. Problem Scope** ## **In Scope** ### **1. Colending foreclosure simulation** Foreclosure simulation will compute payoff using: -

---

## #362 — Product note Interest rate change handling
**Status:** Pending review | **Last edited:** Unknown

# Product note: Interest rate change handling Last Edited: March 19, 2026 9:51 PM PRD ETA: March 19, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** In the current co-lending construct between DSP (NBFC) and TCL (co-lender), loans are originated and managed across multiple representations within the LMS: - **Loan 90 (TCL Book):** Represents TCL’s capital contribution and is controlled externally by TCL, including interest rate decisions. - **Loan 10 (DSP Book):** Represents DSP’s capital contribution and follows DSP’s internal benchmark and pricing logic. - **Loan 100 (Customer-facing Loan):** A composite loan created in the LMS, reflecting the borrower’s obligation and used for repayment schedules, accruals, and customer communication. The effective interest rate for the borrower is derived as a **weighted average of the underlying lender rates based on capital contribution**: - 90% → TCL (Loan 90) - 10% → DSP (Loan 10) However, from a system and implementation perspective: - The LMS treats **Loan 100 as an independent loan** with its own benchmark and ROI. - Interest rates are currently configured using **benchmark + spread constructs defined at an organizational level**. - There is **no native support for dynamic weighted rate computation** across multiple lender loans within the LMS. --- ### **Problem Statement** As part of ongoing co-lending operations: 1. **Independent Rate Changes by Lenders** - TCL may revise its interest rates (benchmark or spread) independently. - DSP may also revise its own benchmark rates. - These changes directly impact the **effective blended ROI** applicable to the borrower. 2. **Lack of Native Synchronization** - Since Loan 90, Loan 10, and Loan 100 are maintained separately: - Rate changes in Loan 90 (TCL) do not automatically reflect in Loan 100. - Loan 100 must be **manually or systematically updated** to maintain parity with the blended rate. 3. **Risk of Misalignment** - If Loan 90 and Loan 100 are not updated in sync: - Incorrect borrower interest may be charged. - Accruals and repayment splits between lenders may become inconsistent. - Downstream systems (accounting, reconciliation, reporting) may break. 4. **Operational Complexity** - Current benchmark configuration is **organization-wide**, not contract-specific. - With multiple co-lending partners, each having: - Different benchmarks - Different spreads - Different rate change cycles → A single benchmark approach does not scale. --- ### **Constraints** - Loan 100 **must exist as a physical loan in the LMS** and cannot be treated as a derived construct. - LMS

---

## #363 — Product note Razorpay PG integration Colending
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

## #364 — Product note Virtual account handling for Colendin
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

## #365 — Razorpay SDK enhancement for Colending
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

## #366 — Risk management system LAS
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

## #367 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #368 — Suspension framework
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?

Currently, suspensions or blacklisting actions (triggered by screening alerts, loan irregularities, or risk assessments) are handled inconsistently across different systems and entities within the NBFC. This fragmented approach creates several critical issues:

1. **Inconsistent Enforcement**: Different systems apply suspension logic differently, leading to gaps where suspended entities can still transact through certain channels
2. **`Missing Hierarchy Propagation**: When a customer is flagged at PAN level, the suspension doesn't automatically cascade to their existing leads,

**Solution:**
?

---

## #369 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #370 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #371 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #372 — Trackwizz continuos monitoring enhancement
**Status:** Unknown | **Last edited:** Unknown

# Trackwizz continuos monitoring enhancement Last Edited: November 13, 2025 12:39 PM PRD Owner: Vaibhav Arora # Contract Changes Required for Stopping Continuous Monitoring - AS504 API ## Executive Summary Based on the AS504 API documentation, the following contract modifications are necessary to effectively discontinue continuous monitoring (Purpose 04) for customers while managing ongoing screening operations. --- ## 1. API Purpose Codes & Termination Logic ### Current Purpose Definitions - **Purpose 01**: Initial Screening with API Response and No Storage - **Purpose 03**: Initial Screening with API Response and TW Workflow - **Purpose 04**: Continuous Screening with TW Workflow ### Key Finding To stop continuous monitoring, contracts must clarify the mechanisms for Purpose 04 discontinuation, as there is no explicit "Purpose 05" for stopping monitoring in the current API specification. --- ## 2. Required Contract Amendments ### 2.1 Data Retention & Deactivation Terms **Required Changes:** ### 2.1.1 Customer Status Field Modification - **Field**: `status` (Customer Status Enum) - **Current Values**: Active, Closed, Dormant, Inactive, Suspended - **Contract Change**: Add explicit condition: `When a customer record's purpose changes from "04" (Continuous Screening) to either "01" or "03" (Initial Screening only), the system must: 1. Cease real-time continuous screening operations 2. Maintain historical screening records for audit/compliance purposes 3. Update effectiveDate to reflect when continuous monitoring ended 4. Mark continuous monitoring as "Terminated" in internal tracking` **Effective Date Requirements:** - Must be provided in "DD-MMM-YYYY" format - Should reflect the exact date when continuous monitoring ceases - Cannot be a future date (must be current or past) --- ### 2.2 Purpose Code Combination Restrictions **Contract Required Clause:** The API currently allows: - Purpose 01 & Purpose 04 (combination allowed) - Purpose 03 & Purpose 04 (combination allowed) **To Stop Continuous Monitoring**, the contract must specify: `Transition Rules for Discontinuing Continuous Monitoring: 1. If Purpose 04 is removed from a request while Purpose 01 or 03 remains: - Continuous monitoring CEASES immediately - Initial screening continues as specified - Customer record remains in TrackWizz but without ongoing monitoring 2. If ONLY Purpose 04 is passed in a new request: - Continuous monitoring CONTINUES unchanged 3. If NEITHER Purpose 01, 03, nor 04 is passed: - Request is REJECTED per validation MRV12` --- ### 2.3 Mandatory Fields for Terminating Continuous Monitoring **Contract Clause - Purpose 04 Discontinuation:** When removing Purpose 04, the following fields become mandatory: ``` FieldRequirementFormatPurposesourceSystemCustomerCodeMandatoryString (Max 100)Identifies record to stop monitoringsourceSystemNameMandatoryEnum

---

## #373 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #374 — Unpledge - Stocks selection logic
**Status:** Completed | **Last edited:** Unknown

**Solution:**
?**

---

## #375 — [Platform] Disbursement optimisation to handle cro
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

## #376 — tech issues
**Status:** Unknown | **Last edited:** Unknown

# tech issues ## ### KYC & Authentication Issues 1. **KYC verification process fails with no clear error messaging** - Example (VTS-9511): "AKGPV3060R - Not able to move forward in kyc step" - Customer was stuck during verification with no indication of what went wrong or how to proceed. - Example (VTS-9981): "Stuck in kyc summary" - Process halted after completing verification with no error details provided to the customer. 2. **Digilocker integration failures during KYC verification** - Example (VTS-9770): "9415307644 - VIKAS KUMAR - KYC issue with digilocker's end" - API connection to Digilocker failing, preventing document verification. - Example (VTS-9964): "Discrepancies in CKYC record associated with the KYC Identifier: 50072772797161" - Records in Digilocker not matching with application data. 3. **Unusual KYC errors without diagnostic information** - Example (VTS-9711): "Unusual KYC Error" - Generic error message without actionable details for troubleshooting. - Example (VTS-10138): "CFCPS2351M - Facing error on KYC Page" - Customer encountered undefined error with no clear next steps. ### Pledging Process Failures 1. **KFin OTP delivery system failures** - Example (VTS-10085): "8928846293 - ATUL TIWARI - not getting otp at pledging for kfintech" - Customer attempted multiple times from web and app but never received OTP. - Example (VTS-10227): "8884052766 - DINESH KUMAR INALA - Kfintech pledging OTP issue" - System-wide failure in OTP delivery when pledging through KFin. 2. **Pledging failure despite eligibility** - Example (VTS-9396): "EQSPK8350P - KFin Pledging error" - "Fund is in approved list of TATA and is also visible when we did 15sec eligibility check" but still failing. - Example (VTS-9358): "DIWPP4809P - Unable to pledge Kfin funds" - Eligible funds appearing in portfolio but pledge transaction failing. 3. **Funds pledged but not lodged in system** - Example (VTS-9884): "Lodgment issue -ANNPS4596F" - "One of the pledged funds of the above client is not lodged in the system yet". - Example (VTS-10044): "BEPPB3956Q, Units pledged but lodgment not done" - Pledge transaction completed but credit not applied to account. ### API Integration Failures 1. **Timeouts in partner integrations** - Example (VTS-9597): "Frequent API Timeout Issues" - FundsIndia experiencing frequent API timeouts, preventing operations completion. - Example (VTS-9529): "Assistance Required: User Facing PAN Mobile Number Error in SDK" - API timeout causing user verification failures. 2. **Document API failures** - Example (VTS-9346): "Volt - Documents are Missing" - "I checked the webtops and I am unbale to find. Requesting you to

---

## #377 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #378 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #379 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #380 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #381 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #382 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #383 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #384 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # Technical Design Document: Call Recording Processing System ## 1. System Overview The Call Recording Processing System is designed to ingest, store, transcribe, and analyze call recordings at scale. The system follows a microservices architecture to ensure modularity, scalability, and maintainability. ## 2. Detailed Service Architecture ### 2.1 Ingestion Service ### Components 1. **Upload Controller** - Handles HTTP uploads of call recordings - Validates input files and metadata - Initiates storage and processing workflow 2. **S3 Integration Module** - Manages direct integrations with S3 storage - Handles signed URLs for direct uploads - Processes S3 event notifications 3. **Bulk Download Manager** - Schedules and manages batch download jobs - Handles large volume transfers efficiently - Provides download job status tracking 4. **Ingestion Repository** - Stores recording metadata - Tracks ingestion status - Provides query capabilities for monitoring 5. Dedupe Manager - Checks the upload file name for the existing files names - Send callback with error “File already exist” ### Data Models ``` Recording { id: UUID externalId: String (client reference) filename: String mimeType: String fileSize: Long duration: Integer (seconds) source: String (enum: UPLOAD, BULK, S3) status: String (enum: UPLOADED, PROCESSING, COMPLETE, ERROR) storageLocation: String createdAt: Timestamp updatedAt: Timestamp metadata: JSON } ``` ### APIs 1. **Upload API** - `POST /recordings` - Multipart form upload for recording file - JSON metadata - Returns recording ID and status - Return Error is File name exists 2. **Bulk Operations API** - `POST /recordings/bulk` - Batch job creation - Configuration options (source, filters) - Returns job ID - Return Error is File name exists in batch handling allow others 3. **Status API** - `GET /recordings/{id}` - Recording metadata - Processing status - Links to associated resources ### 3.2 Storage Service ### Components 1. **Object Storage Manager** - Abstracts object storage operations - Implements retention policies - Handles object lifecycle management 2. **Database Service** - Manages PostgreSQL connections - Implements connection pooling - Provides transaction management 3. **Cache Service** - Redis-based caching - Frequently accessed metadata - Cache invalidation patterns ### Data Models ``` StorageMetadata { objectKey: String bucket: String region: String (if applicable) contentType: String contentLength: Long eTag: String createdAt: Timestamp lastAccessed: Timestamp } ``` ### APIs 1. **Object API** - `GET /storage/objects/{key}` - Object metadata - Presigned download URLs - `DELETE /storage/objects/{key}` - Mark for deletion or immediate removal 2. **Bucket Operations API** - `GET /storage/buckets/{name}/stats` - Storage statistics -

---

## #385 — Capital gains statements UI requirements for Yusuf
**Status:** Unknown | **Last edited:** Unknown

# Capital gains statements UI requirements for Yusuf Requirements: - User flow: User visits the CGS landing page → User enters PAN → User enters mobile number → User enters OTP → User sees the summary data for the current financial year by default, user can change the FY from a dropdown → User sees fund level data and all transactions → User downloads/shares excel, PDF of the report - Use cases to solve for: - User when comes to the website should be able to navigate to the calculator. It should attract attention but not away from check eligibility. - User should understand that is only for mutual funds and not for stocks or other assets. - User should understand that this not a calculator but a report. - User should know the benefits of fetching CGS from Volt. - Completely free! - One stop solution. Not broker specific. - Fast and accurate! - Detailed folio/transaction level understanding - In partnership with/powered by MF central - User should be able to select for which financial year do they want to check. This will be done along with date ranges - User should see a summary of Capital gains tax - User should see a detailed scheme wise view of the CG - Use should understand what terms like grandfathered unit etc mean. - User should have information on how the CG is calculated on mutual funds. - User should have a basic understanding on how to use the Volt CGS report. - Design requirement: - Changes in top nav on the website to include a new section for resources. This will house blogs and calculators. - Landing page for calculator [https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/ae4a091b4](https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/ae4a091b4) - Main calculator input fields. This will be in the interface where user interacts with our calculator. - 3 USP of volt CGS calculator. This will be outside the calculator/report interface. - FAQ section. This will be outside the calculator/report interface. - Summary page [https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/a38739487](https://app.moqups.com/2Tyojb88rrZlICqSEKVsKIt6PNiNaeVQ/edit/page/a38739487) - Scheme level page - Transaction level page - Report PDF design?

---

## #386 — FAQs on CGS landing page
**Status:** Unknown | **Last edited:** Unknown

# FAQs on CGS landing page - What is capital gain statement? How is it generated? **Capital gain statement** is a document that summarizes your redemption activities and the resulting capital gains or losses on your mutual fund holdings. It provides crucial information for filing your income tax return accurately. Volt is partnering up with MFCentral to generate a detailed mutual fund capital gain statement for you. - What is MFCentral? MFCentral is a unified platform launched in September 2021 to simplify mutual fund investments for individuals in India. It is a collaborative effort between the two leading Transfer Agents (RTAs) in the Indian mutual fund industry, CAMS and KFintech. It is also a close partner of Volt Money in facilitating effortless LAMF eligibility check and capital gain report generation. - What are the different classes of Mutual Funds with respect to taxation? Currently there are mainly three types of mutual funds based on their equity or debt instrument allocation: Equity, Debt and Hybrid. Taxation of a mutual fund depends on their domestic equity allocation percentage. - What are Equity Mutual Funds? How are they taxed? Equity Mutual Funds allocate a minimum of 65% of their investable assets to Equity-oriented instruments like domestic Equity shares. From a tax perspective, Equity Mutual Funds are subject to the same treatment as domestic Equity shares. Short-term capital gains (STCG) at a rate of 15% are applicable to profits from Equity Mutual Fund units held for 12 months or less. If the holding period exceeds 12 months, capital gains from Equity Mutual Funds are considered Long-term Capital Gains (LTCG). In such cases, the LTCG rate is 10% on cumulative capital gains exceeding Rs. 1 lakh in a financial year. Popular equity mutual funds include: [] - What are Debt Mutual Funds? How are they taxed? Debt Mutual Funds must allocate a minimum of 65% of their assets to Debt instruments, including bonds, T-bills, Certificates of Deposits, and similar securities. The tax rates and holding periods applicable to Debt Funds differ significantly from those of Equity Mutual Funds. From a tax perspective, for investments made before April 1, 2023: STCG is taxed as per your applicable Income Tax slab rate. However, long-term capital gains are taxed at 20% with indexation benefits. For investments made after April 1, 2023: LTCG and STCG earned on the debt mutual funds are taxable as per your income tax slab.

---

## #387 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #388 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #389 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled - routing to multpe RM , elimates COntext - Call duration average, conversion per RM, overall call per day - inbound patterns - rm have indirect insentive to help customer - list of issues, solution - rm motiwation, rm doesn’t know who to call - call are long, mfd says please hild while i create a case - t90 call - create dashboard for user information - transition mfd to auto serve Wati - templates and analytics - - Expired chats >24 hrs after user message

---

## #390 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #391 — LSQ Swach
**Status:** Unknown | **Last edited:** Unknown

# LSQ Swach **Title:** LSQ Opportunity Management – Solution Document **Date:** 18/07/2025 **Version:** v1.0 --- ## 🔷 Section 1: Customer Journey Solutioning ### 🔹 Objective To transition from a lead-centric to an opportunity-centric model in LSQ, enabling granular tracking across different types of customer interactions and ensuring all workflows are governed through opportunity objects. --- ### ✅ Key Requirements ### 1. Opportunity Types Configuration for Customers Set up the following distinct opportunity types in LSQ: - **Main Application (LAMF)** - **Enhancement** - **Foreclosure** - **LAS** (To be configured at a later stage) - **Renewal** Each opportunity type must be independently configurable, with distinct stages, activities, and associated automations. --- ### 2. Opportunity Attribute Support - All relevant **lead fields** (except name, email, and phone) will be replicated in the opportunity object. - A one-time schema sync between the LSQ backend and opportunity fields will be done to maintain consistency. - The Opportunity object will act as the **source of truth** for all downstream processes and reporting. --- ### 3. Lead to Opportunity Migration - All existing leads (excluding core identifiers: name, email, phone) will be migrated into new opportunities. - Migration logic will ensure backwards compatibility and data integrity. - **The migration from lead to opportunity will be interdependent, as all current flows are tightly integrated. Changes must be deployed simultaneously—partial implementation without complete migration is not feasible.** --- ### 4. Activity Management - Activities will be recorded and managed at the opportunity level, based on opportunity type. - Post-activity workflows will be executed based on opportunity state transitions. --- ### 5. Field Directionality - **One-way sync** from Opportunity → Lead for core fields (name, email, phone). - No data will flow from Lead → Opportunity to avoid overwrites. --- ### 6. Lead Automation Deprecation - Legacy lead-level automations (routing, field updates) will be **disabled**. - All process automations will now be driven by opportunity logic and configuration. --- ## 🔷 Section 2: Partner Journey Solutioning ### 🔹 Objective To establish a dedicated flow for managing the lifecycle of Partner (MFD) leads and activities using a structured, opportunity-driven model. --- ### ✅ Key Requirements ### 1. New Partner Lead Table - Introduce a **dedicated database table** for Partner (MFD) leads. - This will sync with LSQ and create a new partner lead distinct from the customer lead table. --- ### 2. New Opportunity Type: **MFD Activation** - Dedicated opportunity type

---

## #392 — Elevate Cases in LSQ- LAMF
**Status:** Open | **Last edited:** Unknown

# Elevate Cases in LSQ- LAMF: ### 1. **Purpose** To define the business and system requirements for handling **Elevate Cases** in LeadSquared (LSQ). Elevate Cases allow creation of a **new LAMF opportunity** for a borrower even if they already have an won LAMF opportunity with a different lender, enabling **parallel opportunities** under the same borrower account while keeping the opportunity name consistent. ### 2. **Background** Currently, LSQ enforces a “one-active-opportunity-per-lender” rule for each customer, identified by phone number. In *Elevate* scenarios, a borrower who has availed or is availing a LAMF loan from **Tata** or **Bajaj** may now seek a **new LAMF loan from DSP**. The Elevate mechanism ensures: - The **existing opportunity remains untouched**, and - A **new parallel LAMF opportunity** is created for DSP, maintaining full visibility and independent tracking without renaming opportunities. ### 3. **Scope** **In Scope** - Creation of a **new LAMF opportunity** when an existing LAMF opportunity belongs to another lender. - Detection and handling of duplicate opportunities via lender-based exception logic. - Full journey and disposition tracking for both opportunities. - Tagging and reporting visibility for all opportunities per borrower. **Out of Scope** - Changes to standard LAMF journey flow for non-elevate cases. - Changes to lender onboarding or scoring logic. - Non-LAMF product types. ### 4. **Trigger Condition for Elevate Case Creation** An **Elevate Case** is triggered when **all** of the following are true: 1. **Existing Opportunity Check** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = TATA or BAJAJ - Phone Number matches existing record (primary identifier) - Status = WON 2. **New Opportunity Request** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = DSP - Phone Number matches existing opportunity’s phone number 3. **Borrower Account ID Check** - Borrower Account ID ≠ Existing opportunity’s Borrower Account ID If all conditions above are true → **flag as Elevate case** and create a new opportunity with the same name. ### 5. **Functional Requirements** | **#** | **Requirement** | **Description** | | | --- | --- | --- | --- | | 1 | Elevate Case Detection | System should detect when a new opportunity matches Elevate trigger conditions. | | | 2 | Parallel Opportunity Creation | Allow creation of a new LAMF opportunity for a different lender without overwriting existing opportunities. |

---

## #393 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #394 — Jira Integration on LSQ Service desk
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

## #395 — Support Requirement
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

## #396 — LSQ BRD For MFD Activations
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

## #397 — Periskope handling
**Status:** Unknown | **Last edited:** Unknown

# Periskope handling Problem ? - we have too many tools in servicing - As we have Wati and periskope for whatsapp we want to move to one platform - we are having difficulty in managing and reviewing the service SLA. we are missing out on the parter comms and not responding in many hours , this leads to lower MFD retention Goal ? - Increase MFD engagement and retention. - Do we have to add new number to Wati, or one number would suffice ? - If One number then how the handling between agents? - if Two then how will we handle the Display on the MFD , MFD based Number on dashboard ? Current Wati number for mFD? Current agent assigned to Wati? List of 500 MFD to move ? can we add the number and chat to Wati? We will be moving from Periskope to Wati List of the MFD to move ➖ Identify the MFDs to move communicate the Change to MFD Surge planning for the WATI Periskope to Wati Transition plan - Identify the MFDs to move :- https://docs.google.com/spreadsheets/d/1ONAVTJh3wK8kxfcf9j_GvWPis71DKvNbr78d7c342Lk/edit?usp=sharing - Communicate the change to MFD - Message template Dear <name>, We are updating our support communication channel to enhance our service quality. Please note the following: Effective immediately, all support interactions will be conducted through our new channel. Please use the WhatsApp number mentioned below for any Support request. CTA—> Link to Wati Number for message - Surge planning Day 0 - Create a bulk message template - Train and prepare agents Day 1 - We move the Single and inactive MFDs. By sending the message. We will not reply to Periskope after the message (Exception - If Wati is not working ) - Wati will be Serviced by → <Agent name>. Making sure that we have a dedicated resource and they have tools needed to help MFDs - Observe the Volume , allocate the Bandwidth from Periskope to Wati → <name of the agent > - We should expect some Comms from inactive MFDs due to confusion /curiosity. - Day 2 - Review the channel from yesterday - We move rest of the Single MFDs , Barring the top ~100 - We move Inactive 2 MFDs today as well - Same process of handling the Chat support - Day 3 - We move all the MFDs apart from the Top MFDs identified Analytics

---

## #398 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #399 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #400 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #401 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #402 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #403 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #404 — Payout Working File
**Status:** Unknown | **Last edited:** Unknown

# Payout Working File Errors earliar - We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured - We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally - We receive GST issues as Customer raise wrong invoices, This is because we don’t provide GST tax invoice to the partners - We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering uploads the data once a month - We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data. - We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date - We need to streamline GST and TDS filing - We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~ list , journey , use case ## Meeting notes - customer - cashback- - previously - partner - platform customer cashback Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49 march 2022. —>23—>24 <may 1st 9.99 9.99 -ROI base rate - 10.49%. 0.5 % cashback on may 1 we changed the base rate for the customer to 10.49% cusotmer cashback , partner to partner Selfline partner payout - MFD - Volt empaneeled MFD - MFD direct - through Software, redvisison or invest well, assest plus , zfunds , - MFD software - affiliates, - Ytbers , - Partner payout - apps like phonepe , jupiter, niyo, part+ - Money is calculated on the Principal outstanding , monthly average daily average, payout is calculated customer wise average POS, eod, for debit-credit sharing percentage with partners - 1. customer —> loan —> 1. credit to borrower 2. Credit to partner 3. Credit to platform 2. partner - volt- 3. upfront - one time payment, rs 200 for opening a account 4. trail income - 0.5 % into POS 5. category —> upfront and

---

## #405 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #406 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #407 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #408 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #409 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #410 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #411 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #412 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #413 — ARN mandatory for new Registrations
**Status:** Unknown | **Last edited:** Unknown

# ARN mandatory for new Registrations ### **Problem Statement:** - Currently, the partner registration flow allows users to sign up with or without providing an ARN. This has led to a high volume of registrations from individuals who are not certified Mutual Fund Distributors (MFDs). - Approximately 70% of current partner registrations fall into this category. This influx of non-MFD sign-ups places a significant strain on the onboarding team, requiring manual filtering and follow-up, reducing overall efficiency. ### **Proposed Solution:** Modify the partner registration process to require a valid AMFI Registration Number (ARN) for successful sign-up. This will ensure that only verified MFDs can register as partners on the platform. ### **Implementation Requirements:** - **Target Page:** https://staging.voltmoney.in/partner/signup/ (and subsequently production) - Only applicable on New registrations , not existing MFDs - **UI Changes:** - Remove the option/checkbox/link currently allowing users to proceed without an ARN (e.g., "I don't have an ARN number"). - Modify the ARN input field to be mandatory. - **Field Validation:** - The ARN field must not be empty upon form submission. - ~~The entered ARN must consist of exactly **6 digits**.~~ - *(Note: For this initial implementation phase, no external validation against the AMFI database is required.)* - **Error Handling:** - If the user attempts to submit the form without entering an ARN, display a clear inline error message (e.g., "ARN is required."). - ~~If the user enters an ARN that is not exactly 6 digits, display a clear inline error message (e.g., "ARN must be exactly 6 digits.").~~ - **Informational Text:** - Add clear text near the ARN field to inform users about the requirement and guide non-MFDs. Use the following text: > Enter your AMFI Registration Number (ARN)* > > > *Only registered Mutual Fund Distributors (MFDs) can sign up as partners. If you are an investor looking to use Volt Money, please go to our [**Customer registration**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.voltmoney.in%2F%3Fstartnew%3Dtrue).* > **Expected Outcomes & Benefits:** - **Reduced Non-MFD Registrations:** Significantly decrease (estimated 70% reduction) the number of sign-ups from users without a valid ARN. - **Improved Onboarding Efficiency:** Allow the onboarding team to focus solely on qualified MFD partners, streamlining the verification and activation process. - The Existing MFD has no impact / change **Potential Risks & Considerations:** - **Lower Overall Registration Volume:** Expect an initial decrease in the *total* number of registration submissions. However, the number of *qualified* registrations should remain stable or increase relative

---

## #414 — Analytics Requirement Mandate issues
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Mandate issues Query 1: (errors consolidation, distributed by providor) ```jsx select 'tata' as providor,emandate_error_message as error_message,count(distinct(application_id)) as unique_cases from (select application_id, created_date_time, bank_account_number, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) >= date_add('day', -6, current_date) and mandate_status not in ('In Progress','Finished')) t group by emandate_error_message union all select 'digio' as providor,npci_error as error_message,count(distinct(application_id)) as unique_cases from (select application_id, bank_account_number, created_date_time, SUBSTRING(bank_ifsc_code FROM 1 FOR 4) AS bank, umrn, case when CAST(JSON_Extract(digio_mandate_response, '$.npci_auth_failed_error') AS VARCHAR) != 'null' then JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') else JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') end as npci_error , CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) >= date_add('day', -6, current_date) and umrn is null and digio_mandate_status!='EXPIRED' and CAST(JSON_Extract(digio_mandate_response, '$.state') AS VARCHAR) != 'expired') t group by npci_error order by 3 desc ``` Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #415 — Analytics Requirement Name verification (TCL)
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Name verification (TCL) Query 1: (errors consolidation, distributed by providor) Total applications initiated (unique) Total Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #416 — Digio Volt Exploring mandate authorisation flows
**Status:** Unknown | **Last edited:** Unknown

# Digio <> Volt: Exploring mandate authorisation flows What are the different ways via which we can authorise mandates? Debit Card Net Banking Aadhaar OTP Bank OTP - Bank level integrations Some users dont have net banking and aadhaar card, how can we create digital journeys for them for easy mandate set ups? Does digio support direct bank otp based mandate set ups? is it for all banks or specific banks? if yes can we get a list of the supported banks? Check internally bank level requests, how many of our requests can be eased via direct integrations? If not how does one do that? does She have context

---

## #417 — Term Loan Apportionment Logic
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Apportionment Logic - Apportionment is the distribution of a paid sum of money across multiple components of a loan/tranche in order to knock off/settle these components. - Apportionment logic will be based in the order of IPC. - In case of a single tranche apportionment the order will be: Interest Overdue>Principal Overdue>Interest Due>Principal Due>Charge. In case there are multiple EMIs of the Tranche which are overdue then apportionment will start from the oldest EMI overdue. - In case of multiple tranches apportionment the order will be: Oldest EMI overdue(Interest>Principal)>Oldest EMI due(Interest>Principal)>Charges. In case of EMIs overdue across multiple tranches the oldest EMI across tranches will be apportioned first then the apportioning will be done for the next oldest EMI across the tranches and so on so forth. In case all the overdue EMIs are cleared/apportioned the next apportioning will be done for the oldest due EMI and once the oldest due EMI is apportioned then apportioning of the next oldest due EMI will be done and so on so forth. Once all the overdue and due EMIs are apportioned across tranches, apportionment of charges will start and it will also be done based in the order of the oldest charge getting apportioned first i.e. in the chronological order. - If after the apportionment of all the components there is an excess which remains then we will ask the user to select the tranche wherein the excess will be adjusted. The excess adjustment will happen in a way that either the Tenure of the Tranche is reduced or the EMI of the Tranche is reduced based on the user’s selection. Default option(in case user does not select) will always be to reduce the tenure keeping the EMI same for the oldest Tranche.

---

## #418 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #419 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #420 — Term Loan Excess Handling and Refund
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

## #421 — Term Loan Mandate Repayments
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

## #422 — Term Loan Manual Repayments(PG)
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

## #423 — Term Loan Prepayments and Excess Handling
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

## #424 — Term Loan Sell off
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

## #425 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #426 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #427 — MFD Payout Calculation Automation
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout Calculation Automation **Introduction** Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency. 1. we need to handle changing factors like - Monthly Transactions table - Marketing Offers /Referral bonuses - New Platforms additions - Changes in commercials with existing platforms /partners - Changes in base rates / Format - Negotiations with MFDs 2. We need to be able to audit how an amount was generated 3. we need to be able to accrue the credits to an account based on the activity 4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback Problem statements Before base payout calculations - Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing. - We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable. - Attribution of customer to correct Platfrom and partner require manual intervention. - We don’t store the PF and ROI paid by the customer in Credits table. - Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts After the Base payout calculation - TDS rules change and have to accommodate - GST payout are tracked manually Payout process - Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC - For Platform Payouts we need to provide a statement and how the Payout amount is calculated. - Partners have a hard time understanding statements. Potential solutions - Get TATA to improve the API data provided to get the updated transactions - Better fall-back handling on our side Activity activity triggers a

---

## #428 — Periskope to wati plan
**Status:** Unknown | **Last edited:** Unknown

# Periskope to wati plan # Periscope to Wati Migration Plan ## 1. Current Periscope Issues - No effective tracking of incoming chats or resolutions - Lack of chat status visibility (open/resolved/WIP) - Unable to monitor active chat groups - No categorization between sales and service chats - Missing bulk chat download capability - No response time (TAT) tracking - Agents losing track of ongoing conversations - Limited team capacity (2 people per shift) - No chat closure mechanism - Unclear analytics definitions - Missed chats going unnoticed - Integration issues with WATI ## 2. Metrics Comparison ### Current Periscope Metrics - Total interactions count - Unopened messages - Basic chat volume - Group activity status ### Available Wati Metrics - Open/Pending/Solved tickets - First Response Time - Resolution Time - Bot vs. Operator solutions - Expired conversations - Missed chats - Operator performance - Message delivery status - Conversation types - Tag distribution ## 3. Migration Goals 1. Improved Tracking - Real-time chat status - Response time monitoring - Issue categorization 2. Better Resource Management - Automated workflows - Clear agent allocation 3. Enhanced Analytics - Detailed performance metrics - Customer satisfaction tracking 4. Streamlined Operations - Automated responses - Efficient ticket management ## 4. Migration Plan with Checkpoints ### Phase 1: Setup (Day 0) - [ ] Configure Wati dashboard - [ ] Set up automated responses - [ ] Create tags and categories - [ ] Test message templates - [ ] Train agents **Checkpoint Metrics:** - System functionality - Template delivery success - Agent readiness scores ### Phase 2: Initial Migration (Day 1) - [ ] Migrate single and inactive MFDs - [ ] Monitor initial responses - [ ] Track conversion rate - [ ] Handle exceptions **Checkpoint Metrics:** - Message delivery rate - Response times - System stability ### Phase 3: Main Migration (Day 2-3) - [ ] Migrate remaining MFDs excluding top 250 - [ ] Monitor scalability - [ ] Adjust resources as needed **Checkpoint Metrics:** - Chat volume handling - Resolution rates - Customer feedback ## 5. Communication Templates ### Periscope Exit Message ``` Dear [MFD Name], To enhance your support experience, we're upgrading our communication channel. From [Date], we'll be transitioning to a new WhatsApp support system. Key Points: - Last day on current system: [Date] - New support number: [Number] - Transition period: [Duration] For any questions, please contact

---

## #429 — rough
**Status:** Unknown | **Last edited:** Unknown

# rough notes - Tat on a chat , - ticket resolution and creation - check whatsapp api changes Ideal flow MFD is had a request or a issue they communicate the issue with us we mark it as issue and solve it MFD —> Issues —> communications —> Tickets—> solution - IF a MFD or there employees have issues they can reachout to volt and we want to solve the issues promtly - MFD can communicate with us through WhatsApp chat - Now we need to Identify the issues , create a ticket and resolve the ticket Current problems - We don’t have the ticketing system in place - Current tools we are using are not optimal for creating and tracking Tickets Raw notes - The MFD facing challenges in getting timely response - All the onboarded MFD are added to periscope group - MFD’s uses WATI when they interact through Dashboard chat - MFD’s has to use two separate chat channel if they open up a Whatsapp channel through Wati - MFD’s ask , servicing , payout topic of communications are of general nature. our challenges - We have limited ( can’t) tracking of the incoming chats and there resolution - This is a Periskope limitation. we don’t get Open , resolved , WIP status of a Chat - we are unable to check “How many chats groups are active “ , “were active last week “ - We can’t identify if chats are Sales or service related - we get ~100 chats a day - There is no Bulk download chat option in Periscope - we can’t see TAT for a response and resolution - - agents loose track of the ongoing chats , as it chats are pushed to the bottom of the que and it become a issue to differentiate between the chat groups - 2 people work on the periscope - No way of closing the chats and mark that issue was solved - Analytics- daily number of message counts, Flagged messages - no explanation of what these terms are - How to raise tickets is not clear to the team - we use Periscope to reach out to MFDs , If a MFD reach-out and RM are unavailable then we assign another agent to Periscope - group is already connected with Periscope , all all the MFD are added to periscope they are

---

## #430 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #431 — Analytics requirement Repayment
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Repayment | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of repayments | (count of total repayments made today) | | | | | | | | | | Number of transactions automatically settled | (count of repayments made and settled today) | yesterday | | | | | | | | | Number of transactions pending settlement | (Count of repayments made today but pending settlement) | | | | | | | | | | Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours | | | | | | | | | | % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) | | | | | | | | | | | | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.collections ### Field: Collections: created_on - When payment was created Collections: settled_on - When payment was settled automatically Payment_status (If equals to settled - payment was settled either using admin action or automatically) ### Table: admin_action_audit (Credits) admin action name: UPDATE_COLLECTION_STATUS To identify which collections were settled manually Format: Email with CSV attached Sample query: ```sql SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*) FROM collections LEFT JOIN credits ON collections.credit_id = credits.credit_id WHERE lending_partner_id = 'Bajaj' AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY AND collection_status not in ('REQUESTED','CANCELLED','FAILED') group by collection_status,CAST(collections.created_on AS DATE) order by 1,2 ``` Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #432 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #433 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #434 — Transactions Key Mapping
**Status:** Unknown | **Last edited:** Unknown

# Transactions Key Mapping: We shorten Bajaj transaction strings to make them more legible and to format it better in the SOA: | **Bajaj Key** | **Volt derived value** | | --- | --- | | Loan amount disbursed | Withdrawal | | LAS PROCESSING FEES | Processing fee | | Processing fees collected | Processing fee | | Repayment received | Principal repayment | | Cancellation of Disbursement for LAS | Withdrawal failed | | Reversal of Principal amount | Withdrawal failed | | Interest Posting | Interest repayment | | Interest received | Interest repayment | | Charges Posting for LAS Recurring Amount adjusted against Disbursement | Adjustment - Disbursement | | Interest for the period | Interest Repayment | | Round off | Round off | | LAS NACH BOUNCE CHARGES | Bounce Charges | | Processing fees | Processing Fee | | Penal Interest | Penal Interest | | Loan receipt Manual Posting of Interest | Interest Repayment | | Amount received towards Sale of Shares | Sell-Off | | PF Rebook | Processing Fee | | PF Reversal | Processing Fee | | Advance Interest | Interest Repayment |

---

## #435 — KT discussion 19th Feb
**Status:** Unknown | **Last edited:** Unknown

# KT discussion 19th Feb ## Flows - MFDs number - Customer number MFD flow - Pre-empanelment - Outbound → Labdhi - Inbound → OE team - Post empanelment - Outbound → OE team - Inbound → OE team (lead owner) - RM - RM **Leadsquared tracking** - **Inbound call picked** - **Inbound call task with disposition** - **Backup lead owner** - Check team / attribute - Backup assignee should have lead access - Missed call task - Outside business hours - No Assignee available - Assigned but not picked - Inbound call activity / duration / activity **Other questions** - If lead doesn’t exist? **Notes:** - whats will happen if we change role/team name on LSQ, how switch case will work - Discuss in exotel - Need to check if we are saving owner details of all lead on volt DB - Need to check with ENOSH - If no lead found on LSQ then what will happen in case of exotel inbound, create lead and assign to team based on lead origin - Exotel inbound call - lead info modal should open on LSQ dashboard - If outside of business hours, create missed call task - If unanswered, create task for lead owner - Labdi teams call should assign to Volt Onboarding team - Ask Exotel to share BRD and take sign-off from Volt - What will be ETA on Exotel to implement solutions

---

## #436 — Webhook Handling Flow
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

## #437 — While uploading documents in SDFC KFS got missed
**Status:** Solutioning pending | **Last edited:** Unknown

# While uploading documents in SDFC KFS got missed Classification: Bajaj SFDC document upload Notes: Understand why this happened? How can this be fixed? Can we check status of document upload before moving the customer forward PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13055 Status: Solutioning pending

---

## #438 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #439 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #440 — Name
**Status:** Unknown | **Last edited:** Unknown

# Name Column 1: Does it check if the permissions are given? Column 2: Switch On Permission automatically/guide the customer? Column 3: Is Scheduling Available? Column 4: Configure communications for scheduled customers? Column 5: Is Digi Locker Integrated? Column 6: Is Pan Required? Column 7: Does Dashboard have Analytics Available?

---

## #441 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #442 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements ![Untitled](Design%20requirements/Untitled.png) ![Untitled](Design%20requirements/Untitled%201.png) 35% users drop off from the loan summary(Verify interest and charges page) Problems we have identified: 1. Users think that this is the last page of the application. 2. Benefits are not properly communicated. 3. User thinks that the PF is too high. Things that we want to communicate with this page: 1. Highlight selected credit limit, remove selected mutual funds: This might be reminding the users that they are pledging alot of MFs for the limit that they are getting. 2. Show maximum credit limit (maybe). 3. Unlimited withdrawals, repay anytime: Communicate benefits. 4. Pay interest only on the amount you use: Communicate benefits. 5. Monthly interest only EMIs, we can show this for 1,00,00 withdrawal and user can change it to see the IOEMI change: This will quantify the interest that they have to pay 1. 10.49% might feel high but IOEMI will be low for default sum of 1,00,000 2. This will communicate that they only have to pay interest on the sum withdrawn 6. Provided by our trusted lender Tata Capital: User trust 7. Highlight zero hidden charges before showing the charges: User should know that we are transparent with our charges. 8. Other details to be in bottom 25% of the screen: [Content ](Design%20requirements/Content%20aa1bb6ecad904d00b07393fa73ff756a.md)

---

## #443 — Brand Positioning Doc
**Status:** Unknown | **Last edited:** Unknown

# Brand Positioning Doc Volt Money embodies the characteristics of an approachable, efficient, and empowering financial partner for all India. Our brand speaks directly to our customers presenting itself as a fast, transparent, and trustworthy ally in their financial journey. **Tone of Voice**: - Friendly and supportive - Clear and easy-to-understand - Empowering and optimistic - Proactive **Voice Keywords**: Decisive, Warm, Real, Optimistic, Dependable **Core Brand Traits**: 1. **Supportive**: Always there to provide timely assistance in financial needs. 2. **Reliable**: Trustworthy and transparent, ensuring users feel secure and informed. 3. **Empowering**: Motivates users to achieve their financial goals and take charge of their future. 4. **Effortless**: Makes financial processes efficient and stress-free. ### **Core Principles** 1. **Customer-First Approach**: - Always prioritise user needs and design solutions that simplify their financial challenges. 2. **Transparency**: - Build trust by clearly communicating terms, processes, and expectations without hidden fees or jargon. 3. **Empathy**: - Understand the unique challenges of their life and provide support that genuinely makes a difference. 4. **Speed and Efficiency**: - Deliver quick, hassle-free loan disbursals and ensure easy fund management with no unnecessary delays. 5. **Growth-Oriented**: - Enable users to grow their financial potential while meeting immediate needs, offering tools to secure their future. **Key Differentiators**: - **Ease of Use**: Intuitive, simple processes designed for everyone. - **Speed**: Rapid approval and disbursal of loans, ensuring help when it’s needed most. - **Trust and Transparency**: No hidden fees, clear terms, and a commitment to user success. - **Dual Purpose**: Simultaneously solves immediate needs and facilitates long-term financial growth. ## Design Principles for Volt Money's App and Website ### **1. Simplicity First** **Key Concept**: Make every interaction effortless and intuitive. ### **2. Transparency** **Key Concept**: Build confidence through clarity and consistency. ### **4. Speed** **Key Concept**: Reflect the brand’s fast and seamless functionality in the user experience. ### **5. Accessibility for All** **Key Concept**: Ensure inclusivity for all users, regardless of technological or physical barriers. ### 6. Helpful **Key concept:** At every issue, corner or hurdle, the design needs to help users make decisions. ### 7. Thematic **Key concept:** We aim to be the leading technological partner to multiple brands. So making sure your designs provide thematic capabilities we need to use colour, design elements and illustrations consciously

---

## #444 — Market research
**Status:** Unknown | **Last edited:** Unknown

# Market research Benchmarking for Brand, UX, UI, Component usage ### Brand - Understand market standards and common practices - Handling of Trust, Education, Effortless, Supportive - Gaps in competitor offerings ### Component, UI/UX - Use of components - Screen layout - Information architecture - Application of color palette + typography - Icons, illustrations: Use, emphasis - How they deal with complex data visualisation ## Competitors to benchmark 1. Lending apps (LAS, P2P, unsecured, banks, airtel types etc) - Yenmo - Navi - Smallcase - Airtel Finance 1. Credit card apps - Slice - One card - Lazypay - Jupiter - Amex 1. Investment/trading apps Simplicity - Zerodha - Groww - Smallcase Delight - Stable money - Dezerv 1. Modern - design first - Cred - Kiwi --- 1. Audit - Identify inconsistencies | Component | Problem | Action | | --- | --- | --- | | Topbar | - no defined bars for L1, L2, L3 screens - Inconsistent font style, size used | Standardise component types and define use case for each topbar. | | Buttons | - Signup buttons sizing bad - Inconsistent button sizing across screens, modals, journey - Link button component missing - low emphasis buttons missing. | Standardise component types and define use case for each buttons. - Add link button component - Add more low emphasis button components | | Input fields | - Placeholder missing | - Allow placeholder + label - Character count | | Form | - Disabled button: bad ux | - Better validation, error handling | | | | | | Layout | Screen level standardised layouts not defined - inconsistent UI | Define layouts for repetitive scre | 1. Competitor - Color palette used - Type - Layout - Spacing - Shadow, animation, icons - Components (buttons, inputs, modals, cards, etc.) - Visual hierarchy 2. Update palette 3. Update typography 4. Standardize spacing system 5. Redesign components - Buttons - Input fields, Forms - Headers, navigation -

---

## #445 — Scope
**Status:** Unknown | **Last edited:** Unknown

# Scope V1 scope gotten made from claude [Detailed scope](Scope/Detailed%20scope%2094076bd5bcd54381979f8bc87a54b252.md) ## 1. Foundation ```jsx A. Design Tokens ├─ Colors ├─ Typography ├─ Spacing ├─ Border ├─ Shadows ├─ Motion └─ Grid/Layout B. Brand Assets ├─ Logo usage ├─ Icons ├─ Illustrations └─ Photography guidelines ``` ## 2. Components ```jsx A. Base Components (Atoms) ├─ Buttons ├─ Inputs ├─ Typography elements └─ Icons B. Composite Components (Molecules) ├─ Input groups ├─ Form fields ├─ Search bars └─ Navigation items C. Patterns (Organisms) ├─ Forms ├─ Navigation bars ├─ Cards └─ Tables ``` ## 3. Behaviours & interactions ```jsx A. Component States ├─ Hover ├─ Focus ├─ Active ├─ Disabled ├─ Loading └─ Error B. Motion & Animation ├─ Transitions ├─ Micro-interactions ├─ Page transitions └─ Loading states C. Interactive Patterns ├─ Form validation ├─ Error handling ├─ Loading sequences ├─ Data refresh patterns └─ Infinite scroll behaviors ``` ## 4. Usage guidelines ```jsx A. Implementation Rules ├─ Component composition ├─ Spacing rules ├─ Layout guidelines └─ Responsive behaviors B. Accessibility Guidelines ├─ Color contrast ├─ Keyboard navigation ├─ Screen reader support └─ Focus management C. Content Guidelines ├─ Voice & tone ├─ Writing style ├─ Error messages └─ Empty states ``` ## 5. Dev tools & documentation ```jsx A. Technical Documentation ├─ API documentation ├─ Props documentation ├─ Event handling └─ State management B. Code Examples ├─ Usage examples ├─ Integration guides ├─ Common patterns └─ Best practices C. Tools & Resources ├─ Design tokens export ├─ Component library ├─ Storybook documentation └─ Figma libraries ``` ## 6. Logic & business rules ```jsx A. Form Logic ├─ Validation rules ├─ Error handling ├─ Data formatting └─ Submission flows B. Data Display Logic ├─ Sorting ├─ Filtering ├─ Pagination └─ Data refresh rules C. State Management ├─ Loading states ├─ Error states ├─ Empty states └─ Success states ``` ## 7. Platform specific guidelines ```jsx A. Web ├─ Browser support ├─ Responsive breakpoints └─ Performance guidelines B. Mobile ├─ Touch targets ├─ Gesture support └─ Native patterns C. Cross-platform ├─ Consistency guidelines ├─ Platform adaptations └─ Feature parity ```

---

## #446 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: AUM, Short of this trail, Weekly reports, Impact of AUM on their customers, interactive way Kevin (Servicing): the number needs changed, choose funds, for tenure, lender change, MFD customers, 2 time sefie enchancement process Mahesh: Short videos, Error. Govt app, Graphs to explain shortfall Names: Dashboard feedback

---

## #447 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Process kaise hoga, loan disbursal process, their commission, Referral program Kevin (Servicing): 10% buffer for Bajaj Mahesh: Repayment queries, How is my interest calculated, Stop growing, ownership changed, low ticket sizes, Dont need the loan right now, they want to check limit. Names: Common questions Naveen: - Processing fee channel - Transparency KYC - Fetch and Setting during this time we dont see the interestv or fees

---

## #448 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: interest rate, stocks, physical presence, commission | Convinience, One platform, Easy, Visibility, RM, Groups, iN HOUSE TECH, Mahesh: Reducing rate of interest, 10 hours Customer care, Balloon repayment. Names: USPs Naveen: 70-80% are cross checking Interest rate, PF reduce, dedicated product

---

## #449 — User Research Framework
**Status:** Unknown | **Last edited:** Unknown

# User Research Framework ### User research guide ## **Step 1 : Defining Purpose & Objectives** Define the goals of the research to ensure alignment across stakeholders. The research objective should answer - What decision do you need to make for which you need data through user research? - What assumptions are you trying to validate - What would success of this user research look like ## **Step 2 : Target the right and varied User Segments** To ensure comprehensive insights, target varied user groups based on relevant characteristics. Use the following parameters to define your user cohorts: 1. **By User Personas:** - Leverage pre-defined personas representing key demographics, behaviors, or motivations. - Example: - **Persona A**: New users exploring the product. - **Persona B**: Long-term users engaging with advanced features. 2. **By Task-Based Segmentation:** - Categorize users based on their interactions with specific features or tasks: - **Completion:** Users who successfully completed the task. - **Abandonment:** Users who started the task but dropped off. - **Non-Starters:** Users who never attempted the task. ## Step 3 : Selecting the right Research Method Select methods tailored to your objectives and audience. | **Stage** | **Method** | **Purpose** | Examples | Focus on | | --- | --- | --- | --- | --- | | **Exploration** | User Interviews | Discovering Needs and Pain Points | Amazon or Airbnb uses exploratory research when entering new markets or identifying adjacent user needs | Understand attitudes, motivations, and unmet needs. | | | Surveys | | | Gather quantitative preferences at scale. | | **Validation** | Usability Testing | Testing Solutions for Effectiveness | Google routinely conducts rapid validation for its features using A/B testing | Test ease of use for loan application processes. | | | Surveys | | | Assess clarity of repayment terms and options. | | **Tracking** | Behavioral Analytics | Monitoring User Interactions | Facebook employs tracking through behavioral analytics to refine its News Feed algorithm, using live user data rather than pre-launch tests | Identify friction points in user flows (e.g., drop-off rates). | ### Good articles on user research [Defining the Objectives of User Research](https://www.interaction-design.org/literature/article/defining-the-objectives-of-user-research) [How to conduct user research: A step-by-step guide](https://designstrategy.guide/ux/ux-research-guide/) [The Key Factors Driving Silicon Valley Companies' Success - Attorney Aaron Hall](https://aaronhall.com/the-key-factors-driving-silicon-valley-companies-success/) ## Parameters for types of research **Exploration Type:** Discovering Needs and Pain Points - Motivations - Aspirations - Influences - Context

---

## #450 — User Persona Research
**Status:** ** Married with family responsibilities | **Last edited:** Unknown

# User Persona Research [V0.1 for User Research](User%20Persona%20Research/V0%201%20for%20User%20Research%206d63c60255e247f1a2d7a8b49d5a3bbd.md) [User Research Framework](User%20Persona%20Research/User%20Research%20Framework%20adba50e539a84bf8be27f3377b94ba29.md) ## Why do we need user personas - Empathise our user while designing products - Help target their goals, needs, aspirations and pain points - Make user centric product decisions ## Hypothesis ### Established Investor # Meet Rajesh Gupta - The Established Business Owner ## Demographics - **Age:** 44 years old - **Location:** Tier 1 city (Mumbai/Delhi/Bangalore) - **Profession:** Business Owner - **Income Level:** Upper middle class to affluent - **Family Status:** Married with family responsibilities ## Financial Profile - **Loan Requirements:** ₹7.35L (average for business customers) - **Primary Loan Purpose:** Working capital for business - **Investment Portfolio:** Active mutual fund investor - **Existing Loans:** Has a car loan and possibly a home loan - **Financial Behavior:** Financially aware but prefers quick solutions ## Digital Behavior - **Social Media Usage:** Moderate user of Facebook and Linkedin - **Content Consumption:** Actively watches financial/business content (56%) - **Preferred Platforms:** Newsletters (31%), Facebook (28%), YouTube (21%) - **Financial Influencers:** Follows personalities like Rachna Ranade, Akshat Srivastava ## Pain Points & Needs - **Time Sensitivity:** Needs immediate access to funds (74% unplanned loans) - **Process Friction:** Avoids traditional banks due to lengthy processes (69% don't approach banks first) - **Alternative Consideration:** Considers personal loans (41%) or borrowing (23%) before LAMF - **Social Constraints:** Hesitant to borrow from personal network despite considering it ## Decision Making Behavior - **Planning:** Generally makes quick, unplanned financial decisions for business needs - **Research:** Limited research into alternatives due to urgency - **Priority:** Views liquidating mutual funds as last resort but values speed and convenience - **Motivation:** Driven by immediate business requirements rather than personal expenses ## Product Expectations - **Core Needs:** Quick disbursement, minimal documentation - **User Experience:** Expects digital-first, seamless experience - **Post-Service:** Wants clear visibility of loan status, EMIs, and interest calculations - **Communication:** Prefers digital updates but appreciates timely reminders for payments ## Quote "Quick process, bethe bethe kaam ho gaya" (The work was done while sitting in one place) ### New Investors # Meet Aditya Shah - The Tech-Savvy Growth Seeker ## Demographics - **Age:** 28 years old - **Location:** Tier 1 city (Bangalore/Mumbai) - **Profession:** Senior Software Engineer at a tech startup - **Income:** ₹18-25 LPA - **Living Situation:** Single, lives independently in a rented apartment ## Financial Profile - **Investment Portfolio:** - Started investing 3-4 years ago - 60% equity mutual

---

## #451 — DSP Fin Website About Us Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin Website: About Us Page **Objective**: To communicate about the values of the company to audience. DSP Finance is a Non-Banking Financial Company (NBFC) backed by the 160+ year legacy of the DSP Group — one of India’s most respected names in financial services. Rooted in trust, innovation, and discipline, we provide customized credit solutions designed to help individuals and businesses unlock value and achieve their financial goals. We are a NBFC with a strong focus on growth through operational excellence and solving problems through technology. **Mission**: To combine deep market expertise with customer-first innovation, ensuring **reliable, transparent, and efficient access to credit** by leveraging technology and robust operational excellence. **Vision**: To be India’s most trusted partner for financial collateral-backed credit, enabling individuals and businesses to unlock value from their investments for exponential financial growth. DSP Finance’s Values. - Customers first - Utmost transparency - People focus - Continuous innovation Key Highlights of DSP finance to be mentioned - AUM of ~2000CR - ~70K customers - 8+ leading partners - AAA rated DSP Finance’s focus is on capital markets led product offerings in the below business lines. - Loan against securities: enabling individuals to leverage their financial assets to get easy access to credit. This page will redirect to the LAS page. - Financial solutions group: providing corporates access to credit by leveraging their assets to get quick access to funds. This page will redirect to the FSG page. DSP Finance works on the below principles. - **Legacy of Trust** – Backed by the DSP Group’s long-standing credibility in Indian finance ecosystem. - **Customer-First Approach** – Transparent processes, no hidden charges, and clear communication. - **Digital-First Experience** – End-to-end paperless solutions with seamless pledge and disbursal. - **Prudent Risk Management** – Strong governance and compliance in line with RBI regulations. - **Expertise & Innovation** – Blend of deep financial knowledge and modern technology to drive deep innovation. DSP has partnered with leading partners to enable customers to leverage their assets. - PhonePe - PayTm - Indmoney - Groww - ETMoney - CRED

---

## #452 — DSP Finance Website Summary
**Status:** Unknown | **Last edited:** Unknown

# DSP Finance Website: Summary # Positioning We, at DSP Finance, want to be positioned as the ***Most innovative and cutting-edge lender with deep expertise in capital markets.*** - We want to stand out from the crowd as a new-age and customer-friendly lender - We want to stand out from traditional lenders (BFL, TCL) - We want to standout as a specialist lender in the capital markets # Branding We at DSP finance will continue to maintain the DSP brand themes (Colors). That said, we also want to have an independent identity. - Branding to reflect our identity as a new-age lender - Common color schemes as DSP group - Different iconography compared to DSP group # Layout Below are the pages for the new website. - Homepage **Objective**: This page will talk about DSP Finance at a high level to instill confidence in the visitor. **Hero Section –** Innovation at core**.** - **Headline:** *“India’s most innovative lender in the securities space.”* - **Sub-headline:** “A seamless bouquet of credit offerings built on a deep understanding of customers, enabled through cutting-edge technology” - Our partners: Band of existing LSP partners we have. - CTA: *“Explore Partnership”* | *“Request a Call Back”* **Overview section** - India’s leading LAFA player. - DSP Finance helps individuals & businesses unlock the value of their securities seamlessly. - DSP Finance, which is part of the DSP Group is the fastest growing digital lender in the space. - AUM - Rating - Customers **Offerings section** - Our product suite - **LAFA**: Liquidity at the finger-tips against financial securities spanning mutual funds and securities. Redirects to the product page. - **FSG**: Tailored solutions for businesses looking to unlock their business potential by leveraging their financial assets. Redirects to the product page. **DSP Advantage** - Our USP. - **Industry Expertise**: DSP Finance brings to the table, unparalleled expertise and business understanding of capital markets & Securities space. - **Technology First**: DSP Finance offers customers and partners the ease of leveraging technology for superior experience. - **Product Suite**: DSP Finance has the entire suite of products in the financial securities space to suit the needs of individuals and businesses. - **Transparency & Trust**: DSP Finance has very clear and easy to understand fees and charges, backed by the legacy of DSP Group. **FAQs -** Answering questions. **Testimonials** - Building trust in customers. - About Us **Mission & Vision -** Context

---

## #453 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #454 — NBFC B2B LSP Stack
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP Stack # Press Release DSP Finance, a non-banking lender licensed by RBI and part of the DSP group has recently gone live with its retail lending portfolio of Loan against Mutual funds. DSP Finance has been in the news recently for acquiring a majority stake in Volt Money, one of India’s pioneers in the LAMF space as well as the one of the biggest in the market. DSP Finance intends to leverage Volt’s product, distribution as well as technology platform to roll out a suite of products across retail and corporate lending which aims to help individuals and businesses leverage their financial assets better for a better financial profile. DSP Finance has recently been onboarded on Volt Money as one of its lending partners for the Credit line facility offered to individuals. As the business volumes ramps us in this segment, DSP Finance intends to work with other leading online and offline platforms in the country to offer LAMF products. In addition to the current offering of the on-demand loan, DSP Finance intends to offer term loans through its platform where its LSP partners can offer multiple credit products within their app. DSP Finance’s latest offering ‘DSP Flash’ aims to help platforms embed credit offerings into their ecosystem through plug n play APIs and SDKs. These capabilities span the entire credit offerings spanning credit line and term loans against mutual funds as well as securities. DSP finance’s offering not just focusses on customer journey but post servicing as well as operational reconciliation, thus providing an entire suite of offerings compared to most players who offer application related capabilities and rely on offline processes for customer experience. DSP Finance’s capabilities allow platforms to help retain their customers better and at the same time, monetize their base. DSP Finance’s offerings in the credit space comes at a highly flexible yet affordable pricing structure compared to the traditional unsecured loan offerings as well as EMIs against credit cards. This win-win strategy allows platforms to build their own customer experience and ensure trust while DSP Finance focusses on the core activities spanning risk assessment, CDD, compliance and operations as per RBI’s DLG guidelines. --- # FAQs ## External FAQs ## Internal FAQs - **Who will be our target segment for the Flash offering?** Our Target segment for the Flash offering will largely be large online and offline platforms who are

---

## #455 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #456 — Bug Fix Process
**Status:** Unknown | **Last edited:** Unknown

# Bug Fix Process # Challenges Currently, Volt’s platform is being constantly modified to suit the requirements of new initiatives and business scenarios. As we grow rapidly, we need to streamline our bug-fix process to drive higher quality across the board. - Increased man-hours spent on fixing issues - Customers escalating about functional or technical issues - Partners escalating about functional or technical issues - Increased number of bugs being reported - Lack of a feedback loop or learning from each bug The above challenges arise due to the below elements. - Bugs and fixes are being rolled without product sign-off - Bugs and fixes are being rolled without design sign-off - Bugs aren’t religiously analyzed for RCAs - Product team isn’t involved or doesn’t drive bug fixes - Stakeholders ask oncall for enhancements or even new features # Proposed Solution Below are the interventions proposed to solve these challenges. - Streamline the reporting process from multiple sources (TBD). - Oncall dev unblocks the customer quickly where feasible. - Oncall dev identifies the RCA. - All reported issues are categorized into features, enhancements or bugs. - Bugs are prioritized and addressed as per impact and routed through release process. - Features and enhancements are prioritized and addressed as per impact and routed through sprint process. Link to [Product Release Process](Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md). # Proposed Process Below is the proposed process to address these challenges. - Oncall dev receives the ticket from any one of the sources of reporting. - Oncall dev unblocks the customer through a quick-fix or moving the application forward where possible. - Oncall dev classifies the ask into one of the buckets on Jira and tags the program manager after conducting a detailed RCA after the quick fix. - **New feature**: this could be anywhere from a large feature to a small feature but is a capability that doesn’t exist in the system and needs product intervention. - **Enhancement**: this could be a tweak in the logic or minor scenario handling for an existing feature and needs product intervention. - **Bug fix**: this could be an issue at Volt’s end due to a technical or functional issue and impacts users. - All new features and enhancements are tagged to the respective PM on Jira. - PM evaluates the ask and prioritizes it as part of the backlog. - PM informs the stakeholder about the timelines when picked up by

---

## #457 — Problem Discovery & Tracking
**Status:** Unknown | **Last edited:** Unknown

# Problem Discovery & Tracking # Challenges Currently, Volt’s Product team is solving problems across the board at different stages. In addition, the team gets requirements from stakeholders spanning business, operations, partners, etc. This results in multiple challenges. - Lack of a consolidated view of all items - Lack of visibility of multiple things on the PM’s plate - Man-hours spent in tracking items across business, product and tech - Lack of clear communication/ updates to stakeholders - Lack of visibility of sprint plan and the aligned features. A lot of this is happening due to the below reasons. - PMs are using Notion to document basic PRDs. However, all detailed requirements and its tracking is happening on Jira. - PMs use google sheets to maintain trackers for each features which becomes a challenge as there’s no one-stop visibility - Design team doesn’t have complete visibility and a lot of misses happen post a feature being picked up for development or at PRD review stage. - Calling out blockers and tracking various open items across multiple items becomes a challenge due to lack of holistic visibility. - Sprint goals and plans are maintained on excel which isn’t fully linked to Jira which becomes tough to visualize end-to-end. # Proposed Solution Below is the proposed solution. - Use Google sheets for stakeholder alignment - Use Jira (PSB board) for all problem discovery items - Use Notion for PRDs and detailing out requirements - Use Jira for writing detailed requirements (user stories) The rationale for using Jira is that helps track items under development as well as items that don’t need tech intervention. In addition, Jira has all the required capabilities to track complex items like project tracker, creating list of items, etc # Proposed Process Below is the proposed process. - Stakeholder discusses a problem statement OR the PM/PD finds a problem - PM/PD documents the item on Jira on the PSB board as one of the items. - **Epic**: a large project that requires multiple items for completion - **Story**: a story level item that requires only task level items - **Task**: a single task like sign-off from stakeholders, bug, etc. - PM/PD can add multiple items and keep adding comments as well as move tasks to different statuses - PM/PD should aim to segregate problems into 2 buckets. - Problem discovery, identification, sign-off and prioritization - Solution discovery, identification,

---

## #458 — Product Release Process
**Status:** Unknown | **Last edited:** Unknown

# Product Release Process # Challenges Below are the key challenges in the current release process. - Bugs on production environment impacting customers & users - Features being rolled out having bugs/issues leading to quality concerns - Stakeholders have concerns on lack of feature understanding or change - Customers are impacted or have a poor experience on production due to mismatch in requirements vs. development. - Number of man-hours spent on bugfixes increase due to functional clarity lacking. The above challenges arise due to the below elements. - Features are being rolled out with or without QA sign-off but no product sign-off - Bugs and fixes are being rolled without product sign-off - Fixes and changes are being done without any training for stakeholders - There’s no design sign-off before deploying UI capabilities on production - No formal release note is being sent to stakeholders # Proposed Solution Below are the interventions proposed to solve these challenges. - All features would go through a product sign-off is there’s any impact on any existing or new functionality. - All features would go through a design sign-off if there’s any UI/UX impact on any functionalities. - All bugs or fixes including logic changes that impact any functionality will go through a product sign-off. - All bugs or fixes including logic changes that impact any functionality will go through a design sign-off for UI/UX features. - Any feature that won’t meet the product and/or design sign-off criteria will not be allowed to deployed to production. - All new features, including enhancements and bug-fixes that change flow or logic will require a formal release note and training session. While the above items are undertaken, the PM should also setup the required monitoring capabilities by setting up reports or dashboard through Analytics on their own. # Proposed Process ## Sprint Features Below is the broad process for sprint features. - Once the requirements are closed for the sprint, program team informs the PM team of the timelines for QA sign-off. - Product team keeps the test scenarios handy which is shared upfront as part of requirements with tech. - Program team informs the PM and Designer about the timeline for QA sign-off. PM and designer will review the test scenarios on QA or staging environment. - PM and/or designer informs the program team if a feature is signed-off and good to go on Jira. If

---

## #459 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #460 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #461 — Referral Product Note
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and program

---

## #462 — Referral Product Note [Claim approaches]
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note [Claim approaches] ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility

---

## #463 — User Story template
**Status:** Unknown | **Last edited:** Unknown

# User Story template # Guidelines **How should user stories be written?** - Each user story should be atomic — focus on one activity or action. - One feature needs to have multiple user stories for each activity. - For the UPI mandate registration feature, this will be: - Context page. - Mandate registration page. - UPI registration (TPAP). - Post-registration confirmation. - Retry or fallback, if required. - Each user story should be written from a user/customer perspective. - Users can be internal users like sales, support, or operations OR - User can be customer OR - User can be a partner (B2B or LSP) - User stories should document key scenarios and how they will be handled from a UI/UX perspective. - For the UPI mandate feature, this will be: - Mandate registration is pending due to user inactivity. - Mandate registration failure due to user error. - Mandate registration failure due to technical issues. - Mandate registration success. - Delayed confirmation handling. # Template Below is a template for User Stories. - **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc. - **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve. - **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement. # Example Below is a list of User Stories keeping UPI mandate registration as an example. - **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate. **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate). **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey. **Requirement**: Below are the requirements for this page. - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest. - This will be a common page that will cover both NACH and UPI mandate. - This page will describe that customer’s bank account will

---

## #464 — Product Processes
**Status:** Unknown | **Last edited:** Unknown

# Product Processes [Product Discovery Process](Product%20Processes/Product%20Discovery%20Process%20f37c9edce0b54be18a223d28b3c298f9.md) [Product Requirements Standards](Product%20Processes/Product%20Requirements%20Standards%2011de8d3af13a80eb95a2dd3932920a07.md) [Invoice & Payment Process](Product%20Processes/Invoice%20&%20Payment%20Process%20111e8d3af13a808c9c0bc626c723b28e.md) [Product Feedback Process](Product%20Processes/Product%20Feedback%20Process%2011ce8d3af13a8033be22f9de58e9b4b4.md) [Product Release Process](Product%20Processes/Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md) [Problem Discovery & Tracking](Product%20Processes/Problem%20Discovery%20&%20Tracking%2011de8d3af13a80268a83ebb07efd9e5f.md) [Product Impact Analysis](Product%20Processes/Product%20Impact%20Analysis%2011fe8d3af13a80a091feda5d39a5d9ad.md) [Bug Fix Process](Product%20Processes/Bug%20Fix%20Process%2011fe8d3af13a801eb2ede8072b602bc3.md) [Product Release Process (Draft)](Product%20Processes/Product%20Release%20Process%20(Draft)%20122e8d3af13a802cbfcacd425595c340.md) [Product Analytics Process](Product%20Processes/Product%20Analytics%20Process%2019ae8d3af13a80eebcb0c66556b20b46.md) [User Story template](Product%20Processes/User%20Story%20template%202d2e8d3af13a8026992dce13d3df6ec9.md) [Product note template (Duplicate this for use)](Product%20Processes/Product%20note%20template%20(Duplicate%20this%20for%20use)%202cde8d3af13a802a9af1eaea66c5f45c.md) [Referral Product Note](Product%20Processes/Referral%20Product%20Note%202cfe8d3af13a80b485fff3273928ebca.md) [Referral Product Note [Claim approaches]](Product%20Processes/Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) [Referral Product Note (1)](Product%20Processes/Referral%20Product%20Note%20(1)%202e7e8d3af13a804899c0cad099c6aa81.md) [Referral Product Note (1)](Product%20Processes/Referral%20Product%20Note%20(1)%202e7e8d3af13a807ab9a1fe10c4c8527d.md)