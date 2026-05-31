# Current State: Mfd

> Auto-generated from 257 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — NBFC Bureau Reporting
**Status:** Not started | **Last edited:** September 6, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

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

## #4 — Deferring email capture and verification during on
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

## #6 — BAJAJ GetMilesAccountDetails
**Status:** On Hold | **Last edited:** September 2, 2024 11:37 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #7 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #8 — PhonePe Landing page requirement - 15th April
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

## #9 — [Lending stack] Agreement customer signing - Leega
**Status:** Not started | **Last edited:** September 12, 2024 9:30 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #10 — BAJAJ Dedupe API
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

## #11 — Optimizing disbursement metrics
**Status:** In progress | **Last edited:** September 12, 2024 4:44 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #12 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** September 11, 2024 8:14 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #13 — Interest calculator - landing page
**Status:** In progress | **Last edited:** October 9, 2024 8:22 PM

**Problem:**
are we solving?**

1. Before applying for Volt LAMF or withdrawals users want an estimate of what is the interest that they will pay.
2. Since alot of user consider Volt LAMF as term loan, they want to get an understanding of how to close the loan in X duration with equal monthly payments. MFDs are asked this query alot as well. 

---

**Solution:**
?**

---

## #14 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #15 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #16 — LSQ Revamp Solution Doc
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

## #17 — LSQ Audit QA
**Status:** Not started | **Last edited:** October 29, 2024 12:08 PM

# LSQ Audit QA MFD - connect with Ranjan DSP - talk to saksham

---

## #18 — MFD Partner Servicing revamp
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

## #19 — DSP BRE for Beta
**Status:** Pending Review | **Last edited:** October 28, 2024 10:53 AM

**Problem:**
are we solving?**

Currently, customers can avail a loan from Volt app or web through DSP only through whitelisting or URL based parameters. This will not be possible to handle in the beta stage as we need to route applications real-time to DSP.

In addition, the segment where the credit limit offered by Volt is between 10K and 25K is ~12% of the total eligible applications which isn’t catered to by our other lenders, Bajaj and Tata. This opens up a new set of customers for us to acquire and eventual enhance from a limit perspective. 

---

**Solution:**
?**

---

## #20 — MFD Payouts
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

## #21 — SDKs
**Status:** Not started | **Last edited:** October 17, 2024 6:24 PM

# SDKs SDK requirement - business channels - Organic , volt app , web - IFA channel, MFD as a AUM protect , partner dashboard - B2b channel - they spend a lot on the CAC, - securing loans a low margin product - NIMs are 3 to 4 for unsecured loans - we are helping b2b partners cross-selling - we need 3 thing - Redirect - API level - SDK level - there must be a business usecase , integration effort vs reward - SDK - package of all the APIs, partner needs to call - complexities , different env in coded, - JS SDK , for any website integration - React native SDK, zype - Android SDK - koitlin - IOS SDK - swift - Flutter in works - - what is required to invoke a SDK - auth, cust code , sso token - primary secondry colour - step of the customer journey , - API Credit management for partner to poll the application status - version 1.2 m

---

## #22 — Data and Metrics for NBFC Stack
**Status:** Not started | **Last edited:** October 16, 2024 5:59 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #23 — Integrated Sales tool
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

## #24 — Simplify B2B Partner Redirection Journey
**Status:** In progress | **Last edited:** October 11, 2024 6:37 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #25 — [Lending stack] KYC Flow
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

## #26 — Pledge error handling v1
**Status:** Not started | **Last edited:** October 1, 2025 9:19 AM

**Problem:**
are we solving?**

- In the last 3 months, majority of user escalations to support are related to pledge failures from **CAMS and KFin RTAs**. (For instance 41 tickets in last 2 weeks of Aug)
- Currently, these errors are not handled: users see generic failure messages and raise tickets with customer support.
- This creates friction in the journey, increases TAT for resolution, and causes user drop-offs.

**Goal:** Show clear, actionable error messages for the most frequent pledge errors in frontend so users can self-resolve or know what to do next, reducing support load.

---

**Solution:**
?**

---

## #27 — DSP MFD Flows
**Status:** Not started | **Last edited:** November 9, 2024 5:28 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #28 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #29 — Periskope
**Status:** In progress | **Last edited:** November 29, 2024 1:55 PM

# Periskope [Periskope to wati plan ](Periskope/Periskope%20to%20wati%20plan%2014ce8d3af13a80849cf2d1d5e048585e.md) ### Current Challenges: 1. **Limited Tracking**: We cannot effectively track incoming chats or their resolutions due to limitations in Periscope. 2. **Chat Status Visibility**: There is no visibility into chat statuses (e.g., open, resolved, work-in-progress). 3. **Active Chat Monitoring**: We cannot determine how many chat groups are currently active or were active in the last week. 4. **Categorization Issues**: There's no way to identify whether chats are related to sales or service. 5. **Chat Volume**: We receive around 100 chats daily. This a 6. **Lack of Bulk Chat Download**: Periscope does not offer a bulk download feature for chat records. 7. **Response Time (TAT)**: We are unable to track response times or resolution times for chats. 8. **Agent Tracking Issues**: Agents lose track of ongoing chats as new chats push older conversations to the bottom of the queue, making it difficult to manage multiple conversations. 9. **Limited Team Capacity**: Only two people manage Periscope at a time, which limits our ability to handle high chat volumes effectively. 10. **No Chat Closure Mechanism**: There is no way to close chats or mark them as resolved. 11. **Unclear Analytics**: Terms such as "daily message counts" and "flagged messages" lack clear definitions and explanations. 12. **Ticketing Process**: The process for raising tickets is unclear to the team. 13. **Unavailability of RM (Relationship Managers)**: If an MFD reaches out and the assigned RM is unavailable, another agent is assigned to Periscope to manage the chat. 14. **Periscope and WATI Integration**: While all MFDs are connected to Periscope, they are not added to WATI, leading to inconsistencies in communication channels. 15. **Missed Chats**: Missed chats often go unnoticed until they escalate, as there is no way to flag or track missed communications in real time. ## Visibility There are three visibility that we need. - Visibility on Chat messages - Visibility on the issue resolution - Visibility on the Impact of the Providing support Table 1: Visibility on Interactions with MFD Partners | Metric | Description | Current | Wati (option 1 ) | Suggested | | --- | --- | --- | --- | --- | | Total Interactions | Number of interactions with MFD partners | Tracked in Periskope | | | | Call Volume | Number of calls between RMs and MFDs | exotell | | | | Chat Volume | Number of chat conversations

---

## #30 — NBFC Virtual Accounts for Repayments (Alignment)
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

## #31 — LSQ misattribution b2c of B2b2c data
**Status:** Ready for Tech | **Last edited:** November 27, 2024 11:25 AM

# LSQ misattribution b2c of B2b2c data # B2C to B2B2C Lead Update Specification ## Background When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues: 1. Lead tracking inefficiencies 2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams) 3. MFD partner dissatisfaction with direct customer contact ## Objective Reduce misattributed leads - Reduce Creation of the new Misattributed leads. - Update LSQ with admin action (tech pickup) - Backfill data to correct misattribution Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database. ## Technical Implementation ### API Details - **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate) - **Identifier**: Mobile Number (unique in LSQ) ### Required Field Updates ```json { "LeadDetails": [ {"Attribute": "mx_Channel", "Value": "B2B2C"}, {"Attribute": "Source", "Value": "MFD Referral"}, {"Attribute": "mx_Referred_By", "Value": "MFD"}, {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"}, {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"}, {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"}, {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"}, {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"}, {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"}, {"Attribute": "SearchBy", "Value": "Phone"} ] } ``` ## Data Migration Plan ### Initial Data Reconciliation - Tech team to provide excel export of leads updated via admin actions - Data to be shared with LSQ team for backfill - Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count) ### Scope Limitations - Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ - Focus on forward data synchronization and provided historical data only ### MFD Status Handling - Automated daily updates for partially-activated MFD status ## Requirements ### Technical Requirements 1. Admin action implementation for borrower-partner relationship updates 2. API integration with error handling 3. Comprehensive update logging for audit purposes ### Acceptance Criteria 1. Successful lead type transition (B2C to B2B2C) 2. Accurate referrer information mapping 3. Proper API response handling 4. Complete audit logging 5. Visual verification in LSQ dashboard ## Important Notes - Mobile Number serves as the unique identifier in LSQ - Lead merges occur when same email is used with different phone numbers - Implementation must include robust error handling for API failures - API failures should be notified to the team.

---

## #32 — TATA Dedupe API with updated BRE
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

## #33 — NBFC LSP APIs
**Status:** Not started | **Last edited:** November 15, 2024 6:47 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #34 — White-labelled Redirection Journey for B2B Partner
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

## #35 — MFC Summary API calculations update
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

## #36 — Repayment failure handling
**Status:** In progress | **Last edited:** November 12, 2024 1:14 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

---

## #37 — MFD Tier & Performance Data Activity Passing in LS
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

## #38 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #39 — Enhancement to MFD partner Signup page
**Status:** Pending Review | **Last edited:** May 8, 2025 4:19 PM

# Enhancement to MFD partner Signup page **Product Updates** ## **1. Enhanced Partner Login Experience:** - **Feature:** Mobile Number Pre-fill & Browser Autofill Support. - **Problem:** Returning partners re-enter mobile numbers, causing friction. - **Goal:** Faster, more convenient login. - **Solution:** - **Custom Pre-fill:** Store last successfully used/OTP-requested mobile number in browser local storage for automatic pre-population. (Editable by partner). - **Browser Autofill Hint:** Add autocomplete="tel" to the mobile number field to allow browsers (like Chrome) to suggest saved phone numbers. - **Benefit:** Quicker login, reduced errors, improved partner experience. ## **2. Improved Partner Empanelment Form:** - **Feature:** Browser Autofill for Empanelment Details. - **Problem:** Manual entry of common details (name, email, city, company) is time-consuming. - **Goal:** Faster and more accurate empanelment. - **Solution:** Implement standard HTML autocomplete attributes (e.g., name, email, address-level2, organization) on relevant input fields. - **Benefit:** Quicker form completion, fewer typing errors, smoother empanelment. ## **3. Branding & Content Updates:** - **Logo Update:** Replaced Bajaj Finserv logo with DSP logo in "Our trusted partners" section. - **Partner Count Update:** Updated "2000+ Partners have joined Volt Money" to "3000+ Partners have joined Volt Money". - **Benefit:** Reflects current partnerships and growth accurately.

---

## #40 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #41 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #42 — DSP KFS & Agreement for LSPs
**Status:** In progress | **Last edited:** May 5, 2025 5:36 PM

**Problem:**
are we solving?**

Currently, a lot of the LSPs don’t want to showcase DSP 

---

**Solution:**
?**

---

## #43 — MFC Pledge error handling - V1 (1)
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

## #44 — Sell-off Repayment Reconciliation — Maker Automati
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

## #45 — Bulk Upload mapping of RM and MFDs
**Status:** Not started | **Last edited:** May 28, 2025 2:57 PM

# Bulk Upload mapping of RM and MFDs To enable a one-time bulk update of the mapping between Relationship Managers (RMs) and MFDs, and ensure that the updated mappings are reflected in the Volt Partner Dashboard. - Develop a script to bulk update the RM to MFD mapping. - Save and document the script for future reference. - Ensure that the updated RM to MFD mappings are reflected in the Volt Partner Dashboard. > Summary > > - Update outdated RM (Relationship Manager) mappings in MFD dashboards to show correct RM information.- > https://docs.google.com/spreadsheets/d/1aX1thTESwja-n1J-LL1rgCydee2pp6aKZ5igGUTLGgU/edit?gid=0#gid=0 > > - MFD dashboards are showing incorrect RM numbers due to an LSQ bulk upload. Need to sync with current RM assignments using existing API endpoints. > - Update RM-MFD mapping table with current data > - Verify all dashboards show correct RM numbers > - Confirm data consistency between LSQ and MFD dashboard

---

## #46 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #47 — PRD - B2C Referral [Phase-1 1]
**Status:** In progress | **Last edited:** May 27, 2026 4:29 PM

**Problem:**
are we solving?**

Volt Money's Loan Against Mutual Funds (LAMF OD) product has strong unit economics and high borrower quality.

Currently, Volt has no mechanism to leverage its existing user base (borrowers who have experienced the value of Volt Money's LAMF product or users who know about the platform), for new user acquisition through word-of-mouth in an organized and trackable manner.

We need a **trust-first, low-CAC acquisition method** built on the credibility of existing borrowers by activating them to refer new users to Volt LAMF OD product. This would also build trust amongst new us

**Solution:**
?**

---

## #48 — PRD – Volt MFD Payouts Process
**Status:** In progress | **Last edited:** May 27, 2025 2:52 PM

# PRD – Volt MFD Payouts Process # **PRD – Volt MFD Payouts Process** ## **1. What Problem Are We Solving?** ### **Key Issues Identified** 1. Business continuity risk as we are too dependent on one analyst for the calculations 2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~ 3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries. 4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts. 5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed. 6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS). 7. **Support Visibility:** No centralized tracking for payout-related support issues. 8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files. 9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails. 10. **GSTN Verification:** No automated verification of correct GST numbers. --- ## **2. Changes needed for Payout automation (Current vs. Proposed)** | Database | Current | Proposed | | --- | --- | --- | | Application Data | DB | No change | | Transaction Data | DB | No change | | Principle Outstanding | Google Sheets | DB | | Partner Commercials | Google Sheets | DB | | Payout Ledger Table | Google Sheets | DB | | Account Payable (AP) | Not tracked | DB | | Base Payout Calculations | Google Sheets | DB | | GST & TDS Calculations | Google Sheets | DB | | Payout & GST Invoice | Google Sheets | DB | | GST Tax & TDS Filing | Google Sheets | DB | | Bank Account Data | Manual Check | DB | | Payout File to Bank | Excel | API | | Payout Payment Status | Statement | API | | Reconciliation & UTR Backfill | Google Sheets | DB | --- ## **3. User Needs** ### **MFD / Partner** - Expect accurate, on-time payments. - Need clear payout breakdowns, including GST invoices. - Require an easy way to highlight and resolve discrepancies. - Want Volt to handle tax filings accurately. - Prefer a payout experience similar to top AMCs. ### **Business Team** - Aims to improve MFD service by resolving payout issues efficiently.

---

## #49 — Migrating MFD Partners to the LSQ Accounts
**Status:** Ready for Tech | **Last edited:** May 27, 2025 2:25 PM

# Migrating MFD Partners to the LSQ Accounts [**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md) - Accounts are now enabled for org: volt - Reading LSQ documentation to understand and create a transition plan - MFD is currently treated as lead and should be moved to accounts - RMs will be assigned accounts and will be responsible for its success - All the customer of a MFD will be under their account - **1. Purpose & Goal:** - **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data. - **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads. - **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership). **3. Procedure:** **Phase 1: Configure the Accounts Module for MFDs** Setting up the Accounts entity for MFDs - **3.1 Identify Required MFD Fields:** - Review the current Lead fields list - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples: - PAN - ARN No - Referral Code / Partner Code - Partner Referral Link - Partner Type - Platform / Platform Id - Empanelment Date - Company (if used for MFD firm name) - Key contact details (Email, Mobile Number, Address, City, State, Zip Code) - Ownership (Owner) - Any other relevant custom fields. - **3.2 Create Custom Account Fields:** - Adding all the Lead files to account - For every required MFD field *not* present by default in Accounts, create a custom field: - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions - Click **Add**. - Define: - **Display Name:** - **Schema Name:** format cf_display_name. custom field for easy reference - **Field Type:** Match - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/) - 3.3 Add Drop-downs in fields like stage, etc. **Phase 2: Migrate MFD Data from Leads to Accounts** - **3.4 Extract MFD Leads:** - Manage leads - Use **Advanced Search** Lead Type != MFD - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**. - **Export:** Select Actions -> Export Leads -> Export as CSV. - **3.5 Prepare the Import File

---

## #50 — CAMS min_unit Validation for LAMF Lien Transaction
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

## #51 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** May 24, 2026 11:40 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #52 — MFC Summary API integration
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

## #53 — LSQ Chat workflow - Phase 1
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

## #54 — PRD MFD Performance Metrics & Earnings Display
**Status:** Not started | **Last edited:** May 21, 2025 12:46 PM

# PRD: MFD Performance Metrics & Earnings Display ## **1. Introduction** This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show: - Their sourced **MF Loan AUM** - Applicable **trail income rate** - **Trail income earned** - **Account opening bonuses** The goal is to make it simple for MFDs to understand how their efforts are driving their earnings. --- ## **2. Goals & Objectives** ### **Primary Goal** To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives. ### **MFD User Objectives** - Understand how MF Loan AUM translates into income or Increase visibility to the MFDs - Track progress toward higher income tiers - See a breakdown of earnings and new account bonuses - View historical trends and performance ### **Business Objectives** - Encourage MFDs to grow MF Loan AUM - Boost Volt Money customer acquisition - Reduce support queries about commissions ## **Success Metrics** - MFD Monthly visits to partner portal - MFD Repeat rate - MFD Avg number of applicaitons per month - upward move in MFD LAMF AUM Buckets --- ## **3. User Stories** - *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier. - I want to know my current trail income rate based on slabs. - I want to see how close I am to the next earning tier. - I want to track monthly/quarterly/yearly trail income. - I want to verify bonuses for each new LAMF line opened. - I want a full summary of earnings: trail income + bonuses. - I want to view historical performance trends. - I want to quickly reference the trail income slab table. --- ## **4. Feature Breakdown & UI/UX** ### **4.1 Main Dashboard: Volt Money Performance Overview** **Key Metrics:** | Metric | Example | Tooltip | | --- | --- | --- | | **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money | | **Trail Rate** | 0.55% | Based on current AUM slab | | **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. | | **New Accounts (MTD)** | 5 | From Onboarding CRM | | **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts | | **Total Earnings (MTD)** | ₹58,291 |

---

## #55 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #56 — Lead Follow-Up Mechanism — Old Leads
**Status:** Not started | **Last edited:** May 19, 2026 6:08 PM

# Lead Follow-Up Mechanism — Old Leads ## Objective Design a structured follow-up mechanism for old leads to: - Ensure periodic engagement - Maximize lead conversion - Control automation usage - Avoid excessive calling - Standardize disposition-driven follow-ups # 1. Lead Segmentation ## Lead Types ### 1. New Leads - Real-time lead assignment - Immediate engagement journey - Separate automation flow ### 2. Old Leads - Leads not converted - Re-engagement campaign - Monthly task-based follow-up mechanism # 2. Old Lead Follow-Up Workflow ## Monthly Trigger ### Automation 1 At the beginning of every month: - Create calling task for all eligible old leads ### Eligibility Conditions - Lead not converted - Lead not closed permanently - Lead not activated - Lead within retry policy # 3. Agent Calling Workflow ## Step 1 — Agent Filters Pending Tasks Agent opens: - Same-day pending tasks - Older pending tasks ## Step 2 — Open Task Agent initiates call. ## Step 3 — Add Disposition Agent marks call outcome. # 4. Disposition-Based Follow-Up Logic | Call Outcome | Sub-Disposition | Action | Next Follow-Up | | --- | --- | --- | --- | | Connected | Interested | Create Follow-Up Task | T+4 | | Connected | Follow-Up Required | Create Follow-Up Task | T+3 | | Connected | Not Interested | Close Task | No Retry | | Connected | MFD Activated | Close Task | No Retry | | Connected | Other Dispositions | Close Task | No Retry | | RNR | — | Create Retry Task | T+2 | | Asked to Call Back | — | Create Retry Task | T+1 | # 5. Calling Attempt Policy ## Monthly Attempt Limits | Criteria | Count | | --- | --- | | Minimum Calls per Lead | 4 | | Recommended Maximum | 8 | | Absolute Maximum | 10 | # 6. Retry Logic ## Retry Rules - Retry only if: - RNR - Callback Requested - Follow-Up Needed - Interested - Stop retries if: - Not Interested - Activated - Invalid - Duplicate - DND - Converted # 7. Automation Consumption Model ## A. Initial Monthly Task Creation | Activity | Automations | | --- | --- | | Monthly Task Creation | 1 | ## B. Per Call Attempt Each call consumes: | Automation Activity | Count | | --- | --- |

---

## #57 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #58 — Term Loan LOS requirements
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

## #59 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #60 — Enhanced Customer Registration & Deduplication for
**Status:** Done | **Last edited:** May 12, 2025 12:46 PM

# Enhanced Customer Registration & Deduplication for MFDs **Enhanced Customer Registration & Deduplication for MFDs** ### **Problem** 1. MFDs often hit blockers or need RM support when trying to register customers who already exist in Volt’s system (e.g., as B2C users, under another B2B partner, or with active loans). 2. The current error message—“Failed to register customer”—is vague and doesn’t guide the MFD on what to do next based on the type of duplicate. 3. There were 1,200 such error on MFD portal. ~50% of the registered TOFU. and 185 admin actions to Map partners ### **Goal** - Simplify the customer registration journey for MFDs, especially in common duplicate scenarios. - Reduce RM dependency, particularly for B2C linking. - Provide clear, actionable feedback to MFDs when a duplicate is found. ### **Proposed Solution: Automat** When an MFD submits “Register Customer” with Name, Mobile, and: ### 1. **Backend Deduplication Check** - Use Mobile and to detect existing customer records. ### 2. **Modal-Based Responses Based on Scenario** - **A. New Customer (No Prior Account)** - **Action:** Add customer —> OTP - **UI:** No modal or interruption. - **B. Customer Exists as B2C (Registered directly on Volt)** - **Modal Title:** *Customer Found in Volt* - **Message:** “This customer is already registered directly with Volt. To add them to your portfolio, OTP verification is required.” - **CTAs:** - “Send OTP & Add Customer” (launches OTP flow) - “Cancel” - **C. Customer Linked to Another Partner or Has Active Application** - **Modal Title:** *Customer Already Registered* - **Message:** “This customer ([Name or Masked ID]) is already registered with Volt and may be linked to another partner or have an active application/loan. Please contact your RM for support.” - **CTA:** “Okay” (returns MFD to form) - **D. Typo/Error in Initial Input (Pre-dedupe)** - If the MFD catches a mistake before dedupe runs (e.g., wrong PAN), allow them to use the existing “Edit details” button. - Once dedupe identifies a match, scenario-specific modals override the generic error message. ### **Key Requirements** - Backend API for robust deduplication using PAN/Mobile. - API must return customer status: - Not found - Existing B2C - Linked to another partner - Active loan/application - Dynamic modals based on API response. - OTP flow for linking B2C customers to MFDs. - Clear attribution/commission logic for B2C linking. ### **Benefits** - Fewer MFD drop-offs and RM escalations. - Seamless onboarding for B2C customers

---

## #61 — MFD Payout Process Revamp
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

## #62 — [Volt LSP] CAS summary and detailed POC
**Status:** Not started | **Last edited:** March 31, 2025 6:14 PM

**Problem:**
are we solving?**

- MFC CAS summary API, required for

---

**Solution:**
?**

---

## #63 — [Volt LSP] Volt LOS Journey 2 0
**Status:** Not started | **Last edited:** March 31, 2025 5:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #64 — [Platform] Wrapper APIs for RTAs
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

## #65 — [B2B2C] GST payouts and reconciliation optimisatio
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

## #66 — Selfie Link - MFD Prudent PRD
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

## #67 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #68 — [B2B2C] Modification for financial terms functiona
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

## #69 — Capital gains tax calculator
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

## #70 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #71 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #72 — MFD Activation Flow in LSQ
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

## #73 — Aadhaar QR scan
**Status:** Not started | **Last edited:** June 26, 2025 11:33 AM

# Aadhaar QR scan 1. Perfios Walk-through completed: SDK includes: 1. Scan QR (scanner) 2. Upload QR 3. Fetches and displays the data 4. To verify the email and phone, the customer has to enter email and phone Steps: 1. Scan QR/ Upload QR 2. Perfios de-codes the data on the QR 3. Fetches the data from UIDAI 4. Verify the email and phone Downside of SDK: Cannot be used for web-app (MFD portal) Perfios gave a walk through for the OCR KYC Plus: 1. Upload the Aadhaar 2. Scans the QR itself 3. Gives the address as the outputD 1. Bureau ID gave the following demo: 1. Upload the Aadhaar QR of the customer 2. It provides: 1. Adhaar last 4 digits 2. careOf 3. District 4. DOB 5. gender 6. location 7. landmark 8. mobile number registered? 9. email registered? 10. name of the customer 11. signature base64 12. state 13. street 14. sub district But when I gave it my black and white aadhaar and another coloured aadhaar card photo, they could not process it. They provide an API based solution thus it can be used across for web-app and mobile-app usage.

---

## #74 — Unlock credit limit revamp
**Status:** Not started | **Last edited:** June 24, 2024 10:53 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #75 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** June 21, 2024 11:32 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #76 — Addition of City-State to CKYC Request in Decentro
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

## #77 — DSP UPI Autopay Integration for NBFC
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

## #78 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #79 — MFC Pledge (revocation & invocation)
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

## #80 — [Jupiter] Unlock credit limit page changes
**Status:** Not started | **Last edited:** July 31, 2024 5:41 PM

**Problem:**
are we solving?**

Change copies on the verify interest and charges page for partners with MFC fetch. 

---

**Solution:**
?**

---

## #81 — [Platform +Volt ] MFC Pledge wrapper APIs + Volt J
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

## #82 — MFD Account View in LSQ
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

## #83 — Tata Video KYC Integration V0
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

## #84 — [Volt LSP] MFC pledge
**Status:** Not started | **Last edited:** July 21, 2025 3:33 PM

**Problem:**
are we solving?**

Current pledging requires customers to submit upto two OTPs, one for CAMS and another from KFin. This add to the friction in our loan application journey. 
MFC pledging APIs solve this by requiring 

---

**Solution:**
?**

---

## #85 — [B2B2C] Fixed deposits via partner dashboard
**Status:** Pending Review | **Last edited:** January 8, 2026 4:23 PM

**Problem:**
are we solving?**

---

- Volt is looking to improve partner engagement by helping partners monetise their existing clients better and sell multiple financial products through one platform. Adding Fixed Deposits (FDs) as a product offering allows partners to offer a popular, high-value product along with loans.
- The objective of this initiative is to integrate FD booking and servicing into the existing Volt Partner Dashboard, leveraging Fixxera for the booking journey while providing partners with a unified interface to initiate, track, and manage FD applications.

**Solution:**
?**

---

## #86 — MFD partner dashbaord Onboarding Rewamp
**Status:** Not started | **Last edited:** January 8, 2025 1:39 PM

# MFD partner dashbaord Onboarding Rewamp ## Current problems -

---

## #87 — Reduce Phonepe Drop-offs
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

## #88 — MFC in-app journey
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

## #89 — Axis bank e-collect API integration for virtual ac
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

## #90 — B2B Platform Dashboard v1
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

## #91 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #92 — Yes bank e-collect API integration for virtual acc
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

## #93 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #94 — Repayment next step
**Status:** Not started | **Last edited:** January 17, 2025 12:25 PM

# Repayment next step # Loan Repayment System Redesign ### Current Hypotheses 1. **Hypothesis 1 :** Users expect repayments (interest, shortfall, principal) to be separate since our home screen and other places don’t communicate how they are interconnected. 2. **Hypothesis 2 :** Most of users are familiar with credit card statement model. ## JTBD problem list ### Job Story 1: Clear Shortfall "When I am in shortfall, I want to know exactly how much I need to pay so that I can clear my dues easily and get out of shortfall." **Current Problems:** - The shortfall card only shows the shortfall amount, hiding the fact that users need to pay shortfall + charges + interest - Both TATA & DSP use CIP/ICP apportionment logic which requires clearing all dues, but this isn't communicated upfront - Users encounter unexpected higher payment amounts at the final step, leading to frustration and payment abandonment or doubts ### Job Story 2: Pay Interest "When I need to pay my interest, I want to understand why I need to pay any additional charges" **Current Problems:** - In TATA, users see interest amounts increase in months with additional charges - The system requires users to clear charges before interest due to apportionment logic, but this requirement isn't explained - Users are unable to pay just interest when charges are due, contradicting their mental model of separate payments - These charges and interest come under monthly dues as a concept ### Job Story 3: Make Principal Repayment "When I want to repay my principal amount, I want to know how my payment will be applied so I can make an informed decision." **Current Problems:** - For both TATA & DSP, users with mandates try to repay principal but discover they must first clear out the interest and charges which are scheduled to be cut through mandate. - The principal repayment screen doesn't explain that the payment will first go towards interest and charges - Users learn about payment apportionment only after attempting the transaction, leading to canceled payments and frustrated users. - Users are not aware that principal is being repaid early and isn’t due for 3 years. ### Job Story 4: Understand Payment Structure "When I look at my home screen, I understand the payments are separate since they show up as separate components, But its in reality an interconnected system." **Current Problems:** - The home

---

## #95 — External APIs for Holdings Statement and Statement
**Status:** In progress | **Last edited:** January 16, 2025 7:53 PM

# External APIs for Holdings Statement and Statement of Accounts (SOA) External APIs for Holdings Statement and Statement of Accounts (SOA) --- ## 1. Introduction This document outlines the requirements for developing external APIs that will provide Holding Statements and Statement of Accounts (SOA) to MFD partners. These APIs will enable partners to access comprehensive financial statements and holdings data for their customers, enhancing transparency and operational efficiency. ## 2. Objective To develop robust external APIs that provide detailed holdings statements and transaction histories, allowing MFD partners to: - Access real-time holdings data - Retrieve historical transaction statements - Generate comprehensive financial reports - Support customer portfolio management ## 3. Target Audience ### Primary Users - MFD Platform Developers - MFD Operations Teams - MFDs ## 4. Scope ### In-Scope - Development of two primary APIs: 1. Get Holdings Statement API 2. Get Statement of Accounts (SOA) API - Documentation and specifications - Data validation and error handling - Integration with existing systems like Invest well dashboard ### ## 5. API Specifications ### 5.1. Get Holdings Statement API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/holdings?date={date} ``` ### Description Retrieves a comprehensive holdings statement for a specific date, showing all active mutual fund investments and their current values. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `date` (string, optional, format: YYYY-MM-DD): Date for which holdings are requested. Defaults to current date ### Response Payload ```json { "holdingsStatement": { "statementDate": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "holdings": [ { "folioNumber": "1041038180", "schemeName": "Aditya Birla Sun Life Flexi Cap Fund", "isinCode": "INF209K01AJ8", "units": 22.7620, "navValue": 1670.00, "currentValue": 38021.64, "lienMarked": true, "lienQuantity": 22.7620, "lienMarkingDate": "2024-09-14" } ], "summaryMetrics": { "totalPortfolioValue": 2454930.52, "totalLienMarkedValue": 801000.00, "availableValue": 1653930.52 } } } ``` ### 5.2. Get Statement of Accounts (SOA) API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/soa?startDate={startDate}&endDate={endDate} ``` ### Description Retrieves a detailed statement of accounts showing all transactions within the specified date range. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `startDate` (string, required, format: YYYY-MM-DD): Start date for the statement period - `endDate` (string, required, format: YYYY-MM-DD): End date for the statement period ### Response Payload ```json { "statementOfAccounts": { "periodStart": "2024-07-01", "periodEnd": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "transactions": [ { "date": "2024-07-02", "transactionType": "DEBIT", "description":

---

## #96 — Transactions for MFD API
**Status:** In progress | **Last edited:** January 16, 2025 7:45 PM

# Transactions for MFD API # PRD: Partner-Level Transaction API ## Overview New API endpoint to provide aggregated transaction data at partner level for all customers under a specific partner to address transaction duplication issues. ## Business Context - Need to provide accurate transactions to partner MFDs - Currently experiencing transaction duplication issues - Need consolidated partner-level view instead of customer-level only - Support platforms with multiple partners and customers We recreate our transaction Db with different txn ID every day. Redvision does not have a sophisticated dedupe check , causing transactions to get duplicated multiple time ~avg 2.7 time , highest 28+ count. https://voltmoney.atlassian.net/browse/VSSB-398 This is a major escalations from the redvision, as the daily transaction sync with the with redvision will be unfeasible they requested partner level API to full from our DB. ## API Specification ### Endpoint `GET /v1/partner/platform/transactions` ### Headers | Header | Description | Required | Example | | --- | --- | --- | --- | | X-AppPlatform | Platform identifier | Yes | FUNDS_INDIA | | requestReferenceId | Unique request ID | Yes | b2595c8c-a163-4072 | | Content-Type | Content type | Yes | application/json | ### Request Parameters | Field | Type | Required | Description | Example | | --- | --- | --- | --- | --- | | fromDate | String | Yes | Start date | "2024-01-01" | | toDate | String | Yes | End date | "2024-01-31" | | volt_Partner_id | String | Yes | Partner identifier | "PARTNER123" | | format | String | No | Response format | "JSON" | ### Response Structure | Field | Type | Required | Description | | --- | --- | --- | --- | | status | String | Yes | Response status (SUCCESS/ERROR) | | partnerDetails.partnerId | String | Yes | Unique partner identifier | | partnerDetails.partnerName | String | Yes | Partner name | | partnerDetails.totalCustomers | Number | Yes | Total customers count | | transactions[].transactionId | String | Yes | Unique transaction ID | | transactions[].voltcustomerCode | String | Yes | Customer identifier | | transactions[].description | String | Yes | Transaction description | | transactions[].amount | Number | Yes | Transaction amount | | transactions[].transactionStatus | String | Yes | SETTLED/PENDING_SETTLEMENT | | transactions[].transactionType | String | Yes | CREDIT/DEBIT | | transactions[].settledOn | Number | Yes | Settlement timestamp | |

---

## #97 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #98 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #99 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** February 26, 2024 1:22 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #100 — B2B2C RM Flows
**Status:** In progress | **Last edited:** February 25, 2025 5:07 PM

# B2B2C RM Flows Problem statements - Agents have no context on the Incoming calls as they only see the Mobile number - There is no place to Use this mobile number to see the details of the MFD calling and past context - If the MFD has a chat with other RM then i can’t see there messages - Disposition forms in the RUNO and Zendesk are not MECE for the need of RMs - Tech Tickets status don’t get auto updated - RM have to remember to follow up with MFDs, they don’t have a workflow requiring it - [tech issues ](B2B2C%20RM%20Flows/tech%20issues%201a5e8d3af13a8016b001f22540049447.md)

---

## #101 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #102 — MFD Partner Portal Access
**Status:** Not started | **Last edited:** February 21, 2025 1:31 PM

# MFD Partner Portal Access Problem statements 1. Some MFDs forget which number they have used to create the account. 2. The MFD employees struggle to find the Portal, the number to log in, and OTP from their MFD 3. MFDs don’t set up passwords as the process to set up a password is deep in the portal. Solutions 1. We can send the Link with Phone number / Account ID and password over email to MFD 2. Generally, MFD employees too have access to the E-mail, they can search Volt money Email

---

## #103 — Periscope
**Status:** Not started | **Last edited:** February 20, 2024 7:01 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #104 — Pre-fetch flow Optimisation Consolidating PAN flow
**Status:** Done | **Last edited:** February 19, 2026 9:43 AM

**Problem:**
are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

**Solution:**
?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

---

## #105 — Line enhancement Loan renewal BRE
**Status:** Not started | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

1. Line enhancement and loan renewal fees BRE changes
2. Fee and charges verification for fresh application, line enhancement and loan renewal for both lender

**Solution:**
?**

---

## #106 — Redemption regret calculator
**Status:** In progress | **Last edited:** February 19, 2026 7:15 PM

**Problem:**
are we solving?**

- Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively.
- Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan.
- Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal.
- Currently,  MFDs rely on pen and paper to explain to their clien

**Solution:**
?**

---

## #107 — Interest, shortfall, renewal table on partner dash
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

## #108 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #109 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #110 — Capture foreclosure reasons from customer
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

## #111 — Centralised issue reporting process
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

## #112 — Downtime handling [Post loan]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #113 — MFC fetch in Volt Journey
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

## #114 — Partial lodgement handling - DSP
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

## #115 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #116 — Push application id and type in LSQ
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Currently we do not push loan application ID against the opportunity and because of this data team are not able to perform recon of LSQ data with Volt DB

---

**Solution:**
?**

---

## #117 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #118 — Shortfall experience optimisation
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

## #119 — TATA loan renewal
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #120 — Ticketing Tool Evaluation Document
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# Ticketing Tool Evaluation Document ## 1. Introduction ### Purpose of Evaluation The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation. ### Scope and Objectives This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include: - Analyzing feature sets and usability - Evaluating system performance and reliability - Reviewing security and compliance standards - Assessing cost-effectiveness and support options DATA sharing over WA and 1:1 WA chat with MFD - PI Data and any other data ## 2. Current Challenges ## Agent Challenges/process gap | # | Challenge | Impact | Priority | | --- | --- | --- | --- | | 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 | | 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 | | 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 | | 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 | | 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 | | 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 | | 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 | | 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 | | 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 | | 10 | No visibility into **TAT of internal ticket and resolution TAT from the 3P** | Inability to provide ETAs to customers | P0 | | 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 | |

---

## #121 — Untitled
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Untitled ```mermaid flowchart TD A[User Login] --> B{Account Status Check} B --> C[Only LAS Account] B --> D[Only LAMF Account] B --> E[Both Accounts] B --> F[No Accounts] %% Only LAS Flow C --> C1[LAS Dashboard] C1 --> C2{User Action} C2 --> C3[View Account Details] C2 --> C4[Make Repayment] C2 --> C5[Top Up Collateral] C2 --> C6[Apply for LAMF] C2 --> C7[View Statements] C6 --> G[LAMF Application Flow] G --> G1[Document Upload] G1 --> G2[Verification] G2 --> G3[Approval/Rejection] G3 --> |Approved| H[Dual Account User] G3 --> |Rejected| C1 %% Only LAMF Flow D --> D1[LAMF Dashboard] D1 --> D2{User Action} D2 --> D3[View Account Details] D2 --> D4[Make EMI Payment] D2 --> D5[Top Up Collateral] D2 --> D6[Apply for LAS] D2 --> D7[View Statements] D6 --> I[LAS Application Flow] I --> I1[Collateral Setup] I1 --> I2[Verification] I2 --> I3[Approval/Rejection] I3 --> |Approved| H I3 --> |Rejected| D1 %% Both Accounts Flow E --> H[Unified Dashboard] H --> H1{Account Selection} H1 --> H2[LAS View] H1 --> H3[LAMF View] H1 --> H4[Combined View] H2 --> H5{LAS Actions} H5 --> H6[LAS Account Details] H5 --> H7[LAS Repayment] H5 --> H8[LAS Top Up] H5 --> H9[Switch to LAMF] H3 --> H10{LAMF Actions} H10 --> H11[LAMF Account Details] H10 --> H12[LAMF EMI Payment] H10 --> H13[LAMF Top Up] H10 --> H14[Switch to LAS] H4 --> H15{Combined Actions} H15 --> H16[Cross-Account Summary] H15 --> H17[Unified Repayment] H15 --> H18[Portfolio Analysis] H15 --> H19[Recommendations] %% No Accounts Flow F --> F1[Welcome Screen] F1 --> F2{Product Selection} F2 --> F3[Apply for LAS] F2 --> F4[Apply for LAMF] F2 --> F5[Learn More] F3 --> J[LAS Onboarding] F4 --> K[LAMF Onboarding] %% Common Flows C4 --> L[Repayment Flow] D4 --> L H7 --> L H12 --> L H17 --> M[Multi-Account Repayment] L --> L1[Select Amount] L1 --> L2[Choose Payment Method] L2 --> L3[Confirm Payment] L3 --> L4[Payment Processing] L4 --> L5{Payment Result} L5 --> |Success| L6[Success Screen] L5 --> |Failed| L7[Error Handling] M --> M1[Allocate Amount] M1 --> M2[Choose Payment Method] M2 --> M3[Confirm Split Payment] M3 --> L4 C5 --> N[Top Up Flow] D5 --> N H8 --> N H13 --> N N --> N1[Select Collateral Type] N1 --> N2[Enter Amount/Quantity] N2 --> N3[Verify Collateral] N3 --> N4[Confirm Top Up] N4 --> N5[Processing] N5 --> N6{Result} N6 --> |Success| N7[Success Screen] N6 --> |Failed| N8[Error Handling] %% Support & Help C1 --> O[Help Center] D1 --> O H

---

## #122 — Volt Apps & Web Multiple Loan Handling - Launching
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

## #123 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #124 — Ticketing system for Volt
**Status:** In progress | **Last edited:** February 19, 2025 3:20 PM

# Ticketing system for Volt # **Problem Statement:** Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. Applications successful = With + without assist = Count * Cost Current Support team are facing following challenges Borrower - Long wait times for the agents to get back - Chat support - visibility - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product. - RMs and agents have to provide context in sending the client Between RMs or on Leave - We would have a data on the issues raised by a particular customer or to maintain history of support - If the support request is not OPS or Tech realted then taking followup - High Inbound Traffic :- Agents are move from call to call and saving - Lack of a single source of truth for customer issues. - Inconsistent tracking across calls, WhatsApp, and emails. - Unrecorded issues, especially from phone calls. - No SLA tracking or identification of common problems. **Key Requirements:** - **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket. - **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes. - **Workflow Needs**: - Easy ticket creation and search by phone number. - Visibility into all tickets per customer/issue. - Strong APIs and customizable workflows. - **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database. **Goals:** - Achieve 100% ticketing for all interactions. - Track and measure issue resolution times (SLAs). - Identify bottlenecks and common problems. - Prevent any customer issue from being overlooked. The Workflows that need to be enabled - Grouping of users - Page-nation for the pending and completed application The Filter for the lead stage to be added Add filters in the pending application User stories - Customer will call us - customer is routed to a agent - How is this routing setup? - Agent takes notes on the call - Dispostion

---

## #125 — Track inbound calls
**Status:** Not started | **Last edited:** February 19, 2024 5:26 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #126 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** February 16, 2024 7:07 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #127 — Post loan Status APIs for MFD SaaS Partner Platfor
**Status:** Done | **Last edited:** February 14, 2025 12:59 PM

# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal # Product Requirements Document (PRD) [API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md) ## **Project Title:** **Development of External APIs for MFD Dashboard Integration** --- ## **1. Introduction** This document outlines the requirements for developing a set of External APIs intended for MFD platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners --- ## **2. Objective** To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base. --- ## **3. Target Audience** - **Primary Users:** - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards. - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data. - **Stakeholders:** - **Product Management Team** - **Development Team** - QA - **MFD SAAS Partners** --- ## **4. Scope** ### **In-Scope:** - Development of four External APIs: 1. **Get Active Customers** 2. **Get Shortfall Details** 3. **Get Interest Due Details** 4. **Get Renewal Details** - Documentation and specifications for each API. - Implementation of business logic within each API. - Security measures for data protection. ### **Out-of-Scope:** - Development of UI components for MFD dashboards. - Integration of common headers and authentication mechanisms (handled separately). --- ## **5. API Specifications** ### **5.1. Get Active Customers** ### **Endpoint:** ``` GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber} ``` ### **Description:** Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively. ### **Parameters:** - **Path Parameters:** - `partnerAccountId` (string, **required**): Unique identifier for the partner account. - **Query Parameters:** - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve. ### **Response Payload:** ```json { "activeCustomerDetails": [ { "mobileNumber": "+919876501234", "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "email": "dummy@voltmoney.in", "pan": "AUWPA7175L", "dob": "30-03-1988", "creditDetails": { "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "creditType": "OVERDRAFT", "lenderCreditId": "9911725722", "lenderName": "Bajaj", "totalCreditAmount": 332300, "availableCreditAmount": 282300, "principalOutStandingAmount": 50000, "currentApplicableInterestRate": 9.95, "pledgedPortfolioAmount": 738723, "overUtilizationAmount": 0, "chargesDueAmount":

---

## #128 — Attribution for Volt applications
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

## #129 — MFC Pledge error handling - V1
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

## #130 — Reducing Limit on DSP from 25K
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

## #131 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** December 6, 2024 2:49 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #132 — Volt LOS journey optimisations
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

## #133 — one page application for Partners RMs
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

## #134 — [B2B2C] Improving lead quality in partner journey
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

## #135 — [Volt LSP] Pre fill bank account number from MFC d
**Status:** In progress | **Last edited:** December 27, 2024 10:40 AM

**Problem:**
are we solving?**

Customers on the bank verification step are currently required to enter their complete Bank account number and IFSC code to verify their bank account this is a pain for customers. 

[https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99](https://app.amplitude.com/analytics/volt-hq/chart/vnjl9new/edit/5ajc3t99)

---

**Solution:**
?**

---

## #136 — Mobile email dedupe check in case on in-progress m
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

## #137 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #138 — LSQ Service Desk
**Status:** Not started | **Last edited:** December 24, 2025 11:59 AM

# LSQ Service Desk ## **1. Overview** **Objective:** Phase 1 focuses on building an LSQ-based internal Service Desk that enables structured internal ticketing, SLA management, and Jira integration. **Scope Includes:** - Jira Integration with LSQ - Internal Ticket Management (Sales, Support, Ops) - Ticket Creation & Assignment Logic - Volt Operations Team Workflow - Email Integration (Phase-ready foundation) ## [Jira Integration on LSQ Service desk](LSQ%20Service%20Desk/Jira%20Integration%20on%20LSQ%20Service%20desk%202aee8d3af13a80e8a5f7c0b8e990256a.md) [Support Requirement](LSQ%20Service%20Desk/Support%20Requirement%202aee8d3af13a80e3ae45c08bfa32a8bf.md) [Volt Ops Requirements The child ticket will be created and assigned to Volt Ops.](LSQ%20Service%20Desk/Volt%20Ops%20Requirements%20The%20child%20ticket%20will%20be%20cre%202afe8d3af13a80b9be04e4c2eb5d9880.md) # **3. Internal Ticketing Framework:** This section defines the **complete ticket lifecycle** for the LSQ Service Desk used by Support, Sales, and Operations teams. It covers how a ticket is created, assigned, triaged, escalated (Volt Ops, Product, Lender), and resolved, including SLA behaviour, parent–child ticket logic, and exception handling. # **Actively Involved** - **Customer / MFD** - **Agent (Chat / Email / Calling)** - **System (LSQ Automations & Integrations)** - **Volt Ops Team** - **Product / Tech (via Jira)** - **Lender Partners** # **Ticket Lifecycle Overview** A ticket progresses through the following high-level stages: 1. **Intake & Ticket Creation** 2. **Classification** 3. **Work / Investigation** 4. **Child Ticket Creation (Volt Ops / Product / Tech / Lender)** 5. **Resolution & Customer Validation** 6. **Closure & CSAT** 7. **Reopen, RCA** # **Detailed Step-by-Step Ticket Flow** ## **In Take & Ticket Creation** 1. **Customer initiates contact** via Chat, Call, Email 2. **System identifies the customer** - If contact exists → attach to contact. - If new → create new contact with basic details. Use cases where a ticket will be created and a ticket will not be created: | Channel | Scenario | Condition | Ticket? | Notes | | --- | --- | --- | --- | --- | | Call | Registered number call | Lead exists | YES | Auto-link ticket to lead; capture disposition. | | Call | Unregistered number call | Lead not found | YES | Capture disposiiton and Create new ticket. | | Call | Telemarketing calls | | NO | Mark as Spam | | Call | Missed call from registered number | Customer dropped | YES | New Ticket with status open with associated lead | | Call | Missed call from non registered number | Customer dropped | YES | New Ticket with status open | | Email | Any email sent to support@ | Incoming email | YES | LSQ

---

## #139 — MFD Communications for MFDs and Customers
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

## #140 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #141 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #142 — [Platform] Agent session management
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

## #143 — GET Transaction API - Volt
**Status:** Not started | **Last edited:** December 21, 2024 12:36 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #144 — Figma file organisation
**Status:** Not started | **Last edited:** December 2, 2024 3:59 PM

**Problem:**
are we solving?**

- Searching for updated files of features and different stages of the journey
- Get visibility on how each stage is handled for different lender
- Easy visibility on version history, compliance updates etc. done in the past - need to view in one place
- Allow storing secondary flows like: error handling, drop-off flows etc

---

## #145 — [Platform] Mobile verification method
**Status:** Not started | **Last edited:** December 17, 2024 7:42 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #146 — Renewal applications in the LSQ
**Status:** Not started | **Last edited:** December 17, 2024 7:16 PM

# Renewal applications in the LSQ # Customer Lead Renewal Flow ## Customer lead and opportunity creation steps for Renewal - Create renewal opportunity using lead create and update API - Save renewal opportunity id - Post opportunity update - Post activity on opportunity ## Case Scenarios ### Case 1: Customer initiating renewal through MFC Landing page - Create renewal opportunity if existing loan is near maturity - When user clicks on "Renew loan" update opportunity stage to renewal_initiated - If renewal opportunity already exists, post activity for existing opportunity ### Case 2: Customer initiating renewal through Android/iOS app When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Post "Renewal initiated" activity - Update portfolio verification status ### Case 3: Customer initiating renewal through Web App When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Update portfolio verification status - Post activity for renewal journey progress ### Case 4: System-initiated renewal notification - System identifies loans approaching maturity (30 days before) - Create renewal opportunity if eligible - Send notification to customer - Track customer response through activities ## Renewal Lead/Opportunity Attributes | Lead field name | Data type | Lead Schema name | Opportunity Schema name | Comment | Status | | --- | --- | --- | --- | --- | --- | | Original Loan ID | Text | mx_Original_Loan_Id | mx_Custom_70 | Required | sending | | Renewal Type | Dropdown | mx_Renewal_Type | mx_Custom_71 | Standard/Enhanced | sending | | Original Maturity Date | Date | mx_Original_Maturity_Date | mx_Custom_72 | Required | sending | | Portfolio Re-verification | Boolean | mx_Portfolio_Verified | mx_Custom_73 | Required | sending | | Renewal Amount | Number | mx_Renewal_Amount | mx_Custom_74 | Required | sending | | Original Loan Amount | Number | mx_Original_Loan_Amount | mx_Custom_75 | Required | sending | | Days to Maturity | Number | mx_Days_To_Maturity | mx_Custom_76 | System Calculated | sending | | Renewal Eligibility | Boolean | mx_Renewal_Eligible | mx_Custom_77 | System Calculated | sending | ## Renewal Stage Progression ### Active Stages - Renewal_Eligible - Renewal_Initiated - Portfolio_Verification - Documentation_Update - Agreement_Signing - Mandate_Setup - Renewal_Processed - Renewal_Complete ## Custom Activities for Renewal |

---

## #147 — MFD Servicing
**Status:** Not started | **Last edited:** December 17, 2024 1:46 PM

# MFD Servicing # MFD servicing We need to provide assistance to the MFDs in completing the application process on behalf of there customers and provide servicing. These issues need to be identified and to be solved for reduced effort on the MFD and Volt side. We want to provide quick resolution to any issues our MFD might be facing , Goal of the document is to describe the process and current challenges faced by us Ideal process 1. MFD communicates the issues with us using WhatsApp. 2. RM understands the issues from the Communications and raise a ticket 3. Agent then communicates the resolution and mark the tickets as resolved 4. We track the WhatsApp chat and Ticket analytics to understand and improve our servicing ## Current issues ### Communications - **Issue communication:** We use WhatsApp based tools for the MFD to communicate with us (preferred mode of communication by the MFDs). We have the two tools that we currently use - **Periskope: U**sed for providing Group chats to the MFD. - Periskope is based on Whatsapp app. It does not provide good tracking for the chats and expect us to create tickets to track issues - Pros - If MFD has a employees then they can be served by a whatsapp group better to have a one channel for updates *~ 300 groups currently with >1 MFD member.* - If MFD has a escalation then escalation can be handled on group ~ *this really has a bandwidth issues for Kapil or Bharat. We should have a separate channel for the grievance.* - If the RM is on leave and we have a group to solve then someone else can take the handover and solve the problem ~ *Currently only RM has the context on the issues of the MFD and rest of the people in group can’t takeover. The new RM has to gain context from the chat history or notes on the tickets.* - Convert WhatsApp messages into tickets or tasks - Connect with CRM systems, ticketing platforms, and other tools via APIs and web-hooks. - Cons - The platform is no longer supported by the Company - The API integration need to developed by Volt - We are not provided with most Chat level tracking like First time response, Time spend on a chat, How long the message hasn’t been responded to. - Tickets has to

---

## #148 — User engagement on the LSQ
**Status:** Not started | **Last edited:** December 12, 2024 5:55 PM

# User engagement on the LSQ Currently issues # Ticketing System Requirements & Workflow Chief Product Officer Document | December 2024 ## Executive Summary Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency. ## Current Pain Points Analysis 1. Issue Resolution Tracking - No unified system to track resolution progress - Limited visibility into resolution time frames - Inability to measure team performance effectively 2. Organizational Context - Disconnected systems leading to fragmented customer context - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos - Limited cross-functional visibility 3. Support Coverage - Backup handling inefficiencies - Lack of structured handover processes - No clear escalation matrices 4. Performance Metrics - Missing TAT (Turn Around Time) tracking at issue level - No trend analysis capabilities - Unable to identify recurring issues and root causes ## Core Requirements ### Ticket Creation & Management 1. Mandatory Ticket Creation - 100% ticket creation for all customer interactions - Channels: Phone calls, WhatsApp, Email - Required fields: Partner ID, Issue Category, Description - Clear resolution confirmation before ticket closure 2. Channel-Specific Workflows - MFD Channel specific routing rules - Direct customer support workflow - B2B partner interface requirements 3. SLA Management - Channel-specific SLA definitions - Real-time SLA tracking - Escalation workflows - Performance dashboards ### User Management & Access Control 1. Internal Users - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support) - Support Channel Team (10 agents) - Sales Team (7 members) - Ops and Tech on-call teams - Admin users 2. External Users - Direct MFDs - Platform MFDs - B2C customers - B2B platform partners ### Integration Requirements 1. Communication Systems - Exotel for call routing - RUNO for call visibility - Periskope and WATI for WhatsApp - Email integration 2. Internal Systems - Retool for DB state visibility - LSQ CRM - Slack for internal communications ## Key Features 1. Unified Dashboard - Single view of customer interactions - Real-time status tracking - SLA monitoring - Team performance metrics 2. Analytics & Reporting - Issue frequency analysis - Resolution time tracking - Team performance metrics - Channel-wise analysis - Custom report generation 3. Workflow Automation - Automatic

---

## #149 — Volt DLS 2 0
**Status:** In progress | **Last edited:** December 12, 2024 1:59 PM

# Volt DLS 2.0 # Why —————————————————— - Reduce front end effort to create new features and products - Reduce effort of maintaining multiple DLS - Faster design + dev time: Faster decision making and alignment on design - Significantly higher consistency - Easier onboarding for new joinees <aside> 🎯 **Goal:** To create a singular org level DLS that helps build all our products: Core, web, dashboards, command center, etc. </aside> # What —————————————————— ### Process 1. Brand positioning doc - : *in progress* [Brand Positioning Doc](Volt%20DLS%202%200/Brand%20Positioning%20Doc%207b616b64989b4dd68419a624c15997eb.md) 2. User research: *in progress* 3. Market research/Competitor analysis - benchmarking [Market research](Volt%20DLS%202%200/Market%20research%20856a208a18e54d899487aa1703345e80.md) 4. Heuristic evaluation of current design 5. Finalise tokens 1. Keyword mapping 2. Options 1. UI language 2. Typography scale + tokens 3. Color scale + tokens 4. Components In-depth implementation [WIP]: [https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing) ## Scope [Scope](Volt%20DLS%202%200/Scope%20ad8083b8d6fd44fa8e0d2d347d7c5fe0.md) **Tokenization representation** - L3: Mapped - L2: Alias - L1: Primitives [https://thedesignsystem.guide/design-tokens](https://thedesignsystem.guide/design-tokens) [https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676) ![image.png](Volt%20DLS%202%200/image.png) ## ⛳️ Typography scale - Ability to update Heading font style separately than Body - Allow having capitalisation in subheaders, tags etc - Allow using singular token for a style which auto switches between mobile (14px), web, MFD, DSP (16px), command center (12px) ### **How →** - Primitives: xs, sm, md, lg… ,etc. - Alias (Text styles) - Tokens: H1, H2, H3, H4… B1, B2, B3, B4… - Theme: Core-mobile, Core-web, DSP-mobile, DSP-web ## ⛳️ Color scale - Allow switching themes for light and dark mode - Allow switching primary, secondary, success, etc colors for different products/brands/SDKs - Allow modifying individual component level colors. Eg: borders, CTAs, headings, secondary text, disabled, etc ### **How (WIP) →** - Primitives: blue (50, 100, 200…900), turquoise (50, 100, 200… 900)… red (50, 100… 900) - Alias - Primary (50, 100… 900), Secondary (50, 100… 900), Success (50, 100… 900) - Theme: Core, DSP - Mapped - Types: - Text (primary, secondary, action, disabled, success, warning…) - Surface (background, primary, secondary, info, action…) - Border (primary, secondary, warning, error…) - Icon (primary, action, error…) - Theme: Light, Dark ## ⛳️ Component level - Allow switching component styles (corner radius, padding, color…etc.) for different use-cases: Core, DSP, dashboards, command center etc. ### Priority components: 1. Top header bars 2. Buttons 3. Bottom sheet 4. Input fields 5. Form logic + behaviour 6. Bottom nav bars 7. Toasts, notification 8. Tabs - Refer to small case filter screen + chips + tabs inside MF selection 9.

---

## #150 — Single drawdown Term Loan LMS Requirements
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

## #151 — PRD - Capturing UTM-Based parameters for acquisiti
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

## #152 — LSQ Requirements for UTM Attribution
**Status:** Not started | **Last edited:** August 28, 2025 11:55 AM

# LSQ Requirements for UTM Attribution ## Objective Enable LSQ (LeadSquared) to **store, track, and act upon attribution data** for each MFD by capturing both **initial UTM** and **last UTM**. Ensure every UTM update creates **activities and follow-up tasks** for better engagement tracking. ## Data Flow 1. **Event Logging** - Each time an MFD clicks on a campaign link or engages with a communication containing UTMs, the event is logged with: - MFD phone number (identifier) - UTM parameters (`campaign_id`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) - Timestamp of event - Activity context (page visited, registration, activation milestone, etc.) 2. **MFD Matching** - The backend matches the UTM event to the MFD via phone number. - If no MFD record exists, UTM data is stored and linked upon registration. 3. **Stack Ranking of UTM Events** - UTM events are ranked by **timestamp**. - Two attribution markers are defined: - **Initial UTM** = first UTM triggered (never overwritten). - **Last UTM** = most recent UTM triggered (always updated). ## Data Storage in LSQ 1. **Custom Fields (Lead Record)** - Store **Initial UTM** and **Last UTM** parameters in dedicated custom fields (see earlier table). 2. **Activity Logging (Mandatory)** - For every **Initial UTM capture** → create an **Activity** in LSQ: - Activity Name: *“Initial UTM Recorded”* - Fields: UTM parameters, timestamp, campaign type. - For every **Last UTM update** → create an **Activity** in LSQ: - Activity Name: *“Last UTM Updated”* - Fields: UTM parameters, timestamp, campaign type. 3. **Follow-Up Task Creation (Linked to Last UTM)** - Each time a **Last UTM** is updated: - A **Follow-up Task** must be automatically created for the assigned RM/Owner. - Task Type: *“Follow-Up on Campaign Lead”* - Due Date: Based on **Last UTM Activity timestamp** (e.g., +24 hours). - Linked to the same MFD Lead. - This ensures **freshest campaign interaction → RM engagement**. 4. **Last Activity Field Update** - Each **Last UTM Activity** must also update the **system’s Last Activity Date field** in LSQ. - This allows LSQ’s native filters/reports to stay accurate. ## Rules & Logic 1. **Initial UTM** - Captured once on first campaign click. - Not overwritten. - Activity logged → *“Initial UTM Recorded”*. 2. **Last UTM** - Updated on every new campaign click. - Always overwrites previous Last UTM fields. - Activity logged → *“Last UTM Updated”*. - Follow-up Task created → *“Follow-Up on Campaign Lead”*. - Last Activity Date updated.

---

## #153 — Payment gateway integration
**Status:** Not started | **Last edited:** August 28, 2024 3:44 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #154 — LSQ Revamp
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

## #155 — Amplitude Audit and Additions
**Status:** Not started | **Last edited:** August 20, 2025 12:02 PM

**Problem:**
are we solving?**

Auditing the existing amplitude implementation and listing out all the events to add.

---

**Solution:**
?**

---

## #156 — MFC Journey - Fetch
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #157 — MFC implementations
**Status:** Not started | **Last edited:** August 2, 2024 9:12 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #158 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** August 16, 2024 5:19 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #159 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #160 — Amplitude issues
**Status:** Not started | **Last edited:** April 4, 2024 2:09 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #161 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #162 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #163 — MFD - Removing google SSO from PLJ
**Status:** Ready for Tech | **Last edited:** April 22, 2025 10:53 AM

# MFD - Removing google SSO from PLJ Problem statement 1. The **Email field is not Pre-filled** even when the MFD has already fetched the MFC for the client. 2. **Email verification via Google SSO** doesn’t work well for the MFD channel—Google pulls the MFD's email from the device instead of the client’s. ![Screenshot 2025-04-11 at 1.31.35 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.35_PM.png) - MFDs often manually enter their email in the **“Continue with other email”** option, leading to operational effort to remove the Email. ![Screenshot 2025-04-11 at 1.31.44 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.44_PM.png) ## **Proposed Solution:** **After customer registration (Name + Mobile Number + OTP):** 1. The MFD lands on the **Customer Registered** screen. 2. The screen gives two options: - Learn how to **create an application** on the Partner Portal, or - **Share a link** with the customer. 3. If the MFD chooses **“Continue creating customer application”**: - The flow will continue to the next application journey step skipping the App homepage as the intended action at this step is to complete the application. - The Data like Email ID and Fetched portfolio will be Pre-filled if the MFC has been previously fetched for the customer - If the MFD needs to access the App home page then they can go back on the application process using the top ← arrow on the top left. Text changes on the verify Email step ” The provided email will be used by lenders as the Client’s registered Email for all communications “ ### Key Changes from the Current Flow 1. **Skip the email selector page** — go directly to the “Add Email” screen. 2. **Show the client’s name** clearly to ensure the email being entered is for the right person. 3. **Include a note** saying the email will be used by lenders for important updates. 4. **Update the header** to: “Add client’s email.” 5. **Streamline the journey** by removing extra steps and taking MFDs directly to the email input screen.

---

## #164 — Untitled
**Status:** Not started | **Last edited:** April 17, 2025 11:42 AM

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #165 — PRD MFC Revised Flow
**Status:** Not started | **Last edited:** April 14, 2026 1:03 PM

**In scope:**
- 
    - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including::
        - Partners who have directly integrated with MFC  fetch flow (eg-Paytm)
        - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter)
        - Partners who are using Volt fetch journey

# PRD: MFC Revised Flow ## **Background and Context** - - Since MFC is going to deprecate the MFC fetch apis and moving to SDK based flow for fetching (concerns from AMFI around fintech platforms accessing investor data freely w/o explicit customer consent.) - This change is expected to go live by 31st January - Since all Volt channel flows (B2B,B2C & B2B2C) as well as LSP flows will be impacted by this change, figuring out how to tackle this transition to esnure business continuity in the near and long terms is critical --- ## **1. Problem scope** ### In scope - - We need to ensure smooth continuity and optimal user experience for fund fetch flows across all affected partners, including:: - Partners who have directly integrated with MFC fetch flow (eg-Paytm) - Partners who have their own UI for the fetch flow user journey but using our MFC fetch wrapper API (Jupiter) - Partners who are using Volt fetch journey ### Out of scope - N~~ot covered as part of current scope:~~ - ~~Loan journey changes ‘post fetch’ for Volt channels~~ - ~~B2C website journey changes wrt MFC SD~~K - While the MFC SDK flow implementation is currently suboptimal from tech/ UX POV, improving it by working with the MFC team is not feasible given our tight deadline. --- ## **2. Success Criteria** - - Overall fund fetch SR & first time SR - Overall Fetch TAT - MFC SDK flow SR & TAT - MFC SDK & RTA flow stability /uptime ## **3. Solution Scope** ### [Detailed solution /Journey](https://whimsical.com/internal-mfc-fetch-updated-flow-copy-FDDhzqEJNzTbNnkUCW73b5) ### 1. Entry point (Volt/LSP channels) Volt B2C - Android/IOS app/Partner app: DSP SDK will be triggered on on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen ![Screenshot 2026-02-08 at 2.51.52 PM.png](PRD%20MFC%20Revised%20Flow/Screenshot_2026-02-08_at_2.51.52_PM.png) - ‘Sign in’ entry point on Website : DSP SDK will be triggered on ‘Get my Portfolio’ CTA click on ‘Check eligible credit limit’ screen in the web app - Check eligibility’ entry point on VoltWebsite: DSP SDK will be triggered on submitting ‘PAN & mob no’ screen & will open in an iframe Volt B2B2C/B2B partners - Partners fetching in own UI:The ‘DSP SDK’ flow is triggered from the partner UI - Partners using Volt UI for fetching: Flows will be same as that mentioned under ‘B2C’ section LSP - The ‘DSP SDK’ flow is triggered from the partner UI ### 2.User

---

## #166 — Unpledge and Disbursement Enhancement
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

## #167 — Admin tool migration to Appsmith
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

## #168 — Analytics setup for MFD channel
**Status:** In progress | **Last edited:** April 10, 2025 11:11 AM

# Analytics setup for MFD channel **Problem Statements:** 1. **Source Identification:** - We currently lack detailed data to distinguish the source platform/interface for applications. Examples include: - Partner Portal Web vs. Partner App - Customer App vs. specific SDKs 2. **SDK Tracking:** - We cannot accurately identify which SDK version or type was used by a partner platform for an application. 3. **TAT Calculation:** - Relying on the audit table for TAT is not ideal for analyzing detailed stage performance. --- ### **Proposed Solutions:** 1. **Source Markers:** - Add unique markers/attributes to application records to identify the origin: - Volt Partner Portal (Desktop) - Volt Partner Portal (Mobile Web) - Volt Customer Web - Volt Customer Mobile App (iOS/Android) - Volt Partner Mobile App (iOS/Android) - SDK (Identify SDK Type/Partner) - Device Type (where applicable) - Application step level - Source (e.g., in the MFD channel where both Partner and Customer may complete steps) 2. **Dedicated TAT Metrics:** - Implement fields/timestamps to capture: - Add Created add of the step , to capture the the First time stage change - **Overall TAT:** From Lead Creation/Customer Registration to Loan Complete status. - **Stage-Level TAT:** Track start times for each key state to calculate the duration spent in each stage (e.g., Start of State A → Start of State B). 3. **Logging for FE UI related bugs:** - Tracking sluggishness on the website - If the Elements fail to load or are stuck

---

## #169 — UPI Autopay
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

## #170 — Template (Duplicate this for new PRDs) - PN
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #171 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #172 — MFD comms
**Status:** Unknown | **Last edited:** Unknown

# MFD comms Drive link [https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph](https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph) 1. **6 Day MFD activation plan** – Last modified on Oct 10, 2023, by Ranjan Kumar Singh. 2. **Comms content - MFD drop off during reg...** – Last modified on Aug 29, 2023, by Kapil Nagal. 3. **Comms content - MFD Referral** – Last modified on Jul 24, 2023, by Kapil Nagal. 4. **Comms content - Welcome email to MFD** – Last modified on Mar 18, 2023, by Kapil Nagal. 5. **Mastersheet Volt Money - MFD Comms** – Last modified on Jul 24, 2023, by Kapil Nagal. 6. **partner comms status** – Last modified on May 3, 2023, by Ranjan Kumar Singh. 7. **partnerComm[Signup]** – Last modified on May 1, 2023, by Ranjan Kumar Singh. 8. **Referral activation message** – Last modified on Aug 29, 2023, by Ranjan Kumar Singh. [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) Consumer comms :- [https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing)

---

## #173 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #174 — Copy Plugin
**Status:** Unknown | **Last edited:** Unknown

# Copy Plugin # ✅ Product Requirements Document: Volt Copy Assistant (Figma Plugin) ## 📌 Overview **Volt Copy Assistant** is a Figma plugin for designers and product managers working on the Volt Money app. It helps improve UX copy across product flows by offering tone-corrected, compliant, and user-friendly rewrites using Google Gemini's AI API — directly within Figma. --- ## 🎯 Core Objectives - Improve fintech UX copy with tone-aligned suggestions - Reduce copywriting guesswork for product designers - Ensure consistency with Volt's design principles (Clarity, Helpfulness, Simplicity, Transparency, Accessibility) - Save time by suggesting, editing, and replacing copy inside Figma --- ## 🧩 Plugin Actions ### 🔹 When a text layer is selected: - Show the original text in an editable input box - Let the user select a tone or context (e.g., CTA, Error, Tooltip, Instructional) - On clicking “Suggest Rewrite”, send the text + tone to Gemini API - Show AI-generated suggestion in a preview area - Allow one-click replacement of the Figma text layer with the suggestion ### 🔸 When **no text layer is selected**: - Show a clear message: “Please select a text layer to get started” - Disable suggestion and replace buttons --- ## 💡 Key Features | Feature | Description | | --- | --- | | **Text input** | Auto-populated from selected Figma text layer | | **Tone/context selector** | Dropdown to choose tone (e.g., Clear & Formal, Conversational, Empathetic) | | **Suggest button** | Triggers Gemini API call and returns rewrites | | **Preview suggestion** | Displays new copy in plugin UI | | **Replace button** | Replaces selected layer’s text with suggested rewrite | | **Fallback logic** | If Gemini fails, show “Something went wrong. Please try again.” | --- ## 🧱 UI Layout (Plugin Panel) | Section | Description | | --- | --- | | Header | “Volt Copy Assistant” with logo (optional) | | Original Text | Textarea (pre-filled from selected layer) | | Context Selector | Dropdown: Error, CTA, Tooltip, Instruction | | Suggest Button | Click to call Gemini | | Suggestion Output | Textarea showing new UX copy | | Replace Button | Click to update Figma layer | --- ## 🔌 External APIs & Data - **Gemini API (Google)** `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent` Authentication via API Key: AIzaSyANJ1RcD5FBIAzxndjvjkZdcmjWDJxl2OA - **Prompt Template (example):** `"You're a UX writer for an Indian fintech app. Rewrite the following copy in

---

## #175 — Frontend UI fixes [small]
**Status:** In progress | **Last edited:** Unknown

# Frontend UI fixes [small] Charter: Design Initiatives # Context While watching screen recording i have been noticing small UI frontend fixes that need to be done. List is added below with screenshots. Session recording ID and User ID # Issues ### Mobile number icon **Issue**: There is an unecessary fill on the mobile icon **Fix** remove the fill. **Account id**: 27028d22-2807-428c-9ffa-73e584decd09 **Session recording id:** https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1320386903165?sessionReplayId=34b38273-eb63-45d7-955e-25cbe0d1e8ca/1756790681555&sessionStartTime=1756790681555 ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image.png) ### Surface page color on B2B theme looks very off for many partners - Can we change the surface page to Fill primary? ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%201.png) ### Wrong logo I have seen we are using the wrong logo for DSP Finance in many of our communications. ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%202.png) ### Avg time on Anchor page is - 10s ### Time take to get OTP is 8-9s for MFC fetch # Figma

---

## #176 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #177 — MFD UI screen exploration
**Status:** Deprioritised | **Last edited:** Unknown

# MFD UI screen exploration Charter: MFD Pod # Context Post fetch, offer screen. HMW optimise for faster TAT. Not club and make is a non linear journey. https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6090-1797&t=MmlJYS7TFHPgzhgQ-11 https://whimsical.com/mfd-board-SQzR6Ph8GAR7cMj6RtBVfL # Process - [ ] Benchmarking - [ ] Explorations # Figma

---

## #178 — Pre fetch optimisation
**Status:** Ready for kickoff | **Last edited:** Unknown

# Pre fetch optimisation Charter: LOS Pod Priority: P0 Task type: Sprint # Context - Need replace DOB input with mobile number before MFC fetch since it is unnecessary and has drop offs - [Pre-fetch flow Optimisation: Consolidating PAN flow](../PRDs/PRDs/Pre-fetch%20flow%20Optimisation%20Consolidating%20PAN%20flow%20207e8d3af13a80e2b744f8bd135a6319.md) # Process # Figma

---

## #179 — MFD Processes
**Status:** Unknown | **Last edited:** Unknown

# MFD Processes # Activation Process To connect with Ashik, # Application Process MFD portal flow - RMs to explain. LSQ + sales flow like Exotel. # Servicing Process Whatsapp groups process like Periskope - Sowmya, # Payout Process

---

## #180 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #181 — Selfie capture journey
**Status:** Unknown | **Last edited:** Unknown

# Selfie capture journey In the Tata journey, we have a step to capture a selfie, but this is not included in the Bajaj journey. While the selfie feature is part of the Bajaj Figma design, it is neither implemented in production nor required. **User Flow for Selfie Capture (Bajaj Journey):** 1. The user sees a "Click Selfie" button, which activates the front camera after obtaining permission. 2. If an MFD creates the application, they can share a link with the customer. 3. The customer flow is as follows: - MFD shares the link with the customer. - Customer receives the link and opens it. - Customer logs in by verifying their phone number and entering the OTP. - The customer continues the application, completes KYC, and provides camera permissions. - Customer clicks the "Click Selfie" button, captures, and uploads the selfie. - Once the selfie is verified, the customer proceeds to the next steps.

---

## #182 — Inbound call assignment
**Status:** Unknown | **Last edited:** Unknown

# Inbound call assignment Future requests - Moving to a RM and Central team structure - Having a auto dialler for the central team - For inbound and Outbound Dialler Plan - One central team for the MFD channel - One number to be used for inbound and outbound December 11, 2024 @Tushar Luthra - The MFD are assigned to RMs and the RMs number is given to the MFD - If the RMs are busy then the Backup RM teams - There are B2C sales calling team with X number of people Tushar has tried auto dialer for the outbound for the Sales team to call the priorised leads and not have team cherry pick the applications #

---

## #183 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #184 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #185 — MFD Payout dashboard
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout dashboard We have a commercial relationship with MFD , where we pay them as per the business they bring Commercials | trail income | 0.5% of AUM | | --- | --- | | account opeing | 200rs | | Selfline | Processing fees waived | | Cashback | | | Content | | | referral | | - MFD payout is calculated based on commercials agreed on with them - MFD payout is different if the MFD is registed for GST - MFD with Gst number has to be paid 18% extra as GST - we collect 5 % TDS for any payout >15000rs - we payout on 10th on month to volt MFDs - we payout on 15th to SAAS partner platform MFDs - we payout on 18 th to MFD GST payout - we clear all pending and charges till 25th - MFD may not want to share the PAYOUT amount to there employees - MFD need to see the payout status - GST issues - Payout starts at 1 of the money - Time preiod is month to month - And 10 to 15 th of month payout disbursement happen - 10 MFD get paid - 15 Platform , - 18 MFD GST payout - 25 th anything pending - Puneet compute the payout MFD , 0.5% of AUM yearly trail income/ 12 200 rs per account opening , creditline open MFD selfline - we refund the family of MFDs , RMs fill a sheet Cashback for MFD’s end customers , - we gave 10.49 % customer we have given 0.5 % cashback as we advertised on 9.99% Contest , referrals price, activated MFD referral rs 1000 Platform , :- payout Affiliate - payout - MFD - - partner - - Platform - Affilaetes - Bharat sign off, Labdhi comms - Total amount August Pain points - GST filling , we have to 18% as a TDS of the total payout of the month. - we collect 5% TDS ,

---

## #186 — One Pagers
**Status:** Unknown | **Last edited:** Unknown

# One Pagers [OP - Selloff and Withdrawal request mismatch](One%20Pagers/OP%20-%20Selloff%20and%20Withdrawal%20request%20mismatch%20106e8d3af13a808cbebffae82d466652.md) [**Handling Discrepancies Between Assumed and Actual Limits**](One%20Pagers/Handling%20Discrepancies%20Between%20Assumed%20and%20Actual%20%20106e8d3af13a80748d1cd01661d83138.md) [Missed calls from customers aren't being called back or addressed](One%20Pagers/Missed%20calls%20from%20customers%20aren't%20being%20called%20ba%207dfeec301f004c0586694a51de935466.md) [Sales team is calling customers who complete the journey on their own](One%20Pagers/Sales%20team%20is%20calling%20customers%20who%20complete%20the%20j%2010ae8d3af13a80e4ba2af4aee3ad9ee8.md) [LaMF funnel ](One%20Pagers/LaMF%20funnel%2010ae8d3af13a80ef8b19ccc25e547569.md) [LSQ: Leedsquared](One%20Pagers/LSQ%20Leedsquared%20119e8d3af13a80a0b441ed3d3b464180.md) [MFD Payout dashboard ](One%20Pagers/MFD%20Payout%20dashboard%20120e8d3af13a80f5980de9438ff2e277.md) [Periskope](One%20Pagers/Periskope%20120e8d3af13a80b9ad82c524050ef3a2.md)

---

## #187 — Banking partner finalization
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #188 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #189 — FD Fixerra
**Status:** Unknown | **Last edited:** Unknown

# FD: Fixerra Last Edited: December 1, 2025 2:13 PM ### Product Alignment Note – Fixerra FD Offering via Partner Dashboard *(DSP Finance × Volt Platform)* --- ### **Problem statement** Volt x DSP have a strong distribution via IFAs, we want to experiment distribution of different products via this channel, because of DSP Finance (NBFC) is looking to expand its retail investment footprint beyond LAMF (Loan Against Mutual Funds) by introducing a Fixed Deposit (FD) product. On the Volt platform today, distributors (primarily MFDs) only have LAMF as the monetizable product. While LAMF has strong unit economics, it is not a top-of-funnel product for retail customers. Fixerra provides the underlying FD product and infrastructure. The hypothesis is: - We already have arms-reach access to a large base of customers with mutual fund holdings. - These customers have a natural affinity for low-risk investment instruments. - FDs can act as a trust-building, widely accepted entry product, opening the funnel for both direct revenue (FD) and future LAMF conversions. This note outlines the scope for v1 of FD origination and servicing through the Volt Partner Dashboard, and is intended to align stakeholders across DSP Finance, Volt, and Fixerra. --- ### 2. Problem statement ### 2.1 Current state - MFDs on Volt can only offer LAMF. - Monetization is limited to one product with a relatively narrow target audience. - No simple “safe” product exists to attract or engage a wider customer base. - Distributors lack tools to deepen customer relationships beyond MF transactions. ### 2.2 Opportunity Introducing FDs: - Expands the product portfolio for MFDs. - Helps create a trust-led entry point (“mouth of the funnel”), improving conversions into higher-ticket products like LAMF. - Offers DSP Finance a scalable retail deposit base. - Allows Fixerra to distribute its FD product through MFD networks. --- ### 3. Product hypothesis **FDs can become a high-trust, low-friction product that increases distributor engagement and revenue, while simultaneously opening the pipeline for LAMF upsell.** Supporting hypotheses: 1. Customers with MF holdings are more likely to evaluate FD products with high confidence. 2. MFDs will be able to deepen their relationship and improve overall earnings by offering a broader product suite. 3. The NBFC can explore differentiated FD structuring based on distribution performance (for example, special rates, bulk programs). --- ### 4. High-level GTM - **Channel:** Volt Partner Dashboard - **Actors:** Mutual Fund Distributors on Volt - **v1

---

## #190 — IFSC addition Account opening enhancement
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

## #191 — NESL report
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #192 — Pincode addition Account opening enhancement
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

## #193 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #194 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #195 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #196 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #197 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #198 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #199 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #200 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #201 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #202 — FAQs on CGS landing page
**Status:** Unknown | **Last edited:** Unknown

# FAQs on CGS landing page - What is capital gain statement? How is it generated? **Capital gain statement** is a document that summarizes your redemption activities and the resulting capital gains or losses on your mutual fund holdings. It provides crucial information for filing your income tax return accurately. Volt is partnering up with MFCentral to generate a detailed mutual fund capital gain statement for you. - What is MFCentral? MFCentral is a unified platform launched in September 2021 to simplify mutual fund investments for individuals in India. It is a collaborative effort between the two leading Transfer Agents (RTAs) in the Indian mutual fund industry, CAMS and KFintech. It is also a close partner of Volt Money in facilitating effortless LAMF eligibility check and capital gain report generation. - What are the different classes of Mutual Funds with respect to taxation? Currently there are mainly three types of mutual funds based on their equity or debt instrument allocation: Equity, Debt and Hybrid. Taxation of a mutual fund depends on their domestic equity allocation percentage. - What are Equity Mutual Funds? How are they taxed? Equity Mutual Funds allocate a minimum of 65% of their investable assets to Equity-oriented instruments like domestic Equity shares. From a tax perspective, Equity Mutual Funds are subject to the same treatment as domestic Equity shares. Short-term capital gains (STCG) at a rate of 15% are applicable to profits from Equity Mutual Fund units held for 12 months or less. If the holding period exceeds 12 months, capital gains from Equity Mutual Funds are considered Long-term Capital Gains (LTCG). In such cases, the LTCG rate is 10% on cumulative capital gains exceeding Rs. 1 lakh in a financial year. Popular equity mutual funds include: [] - What are Debt Mutual Funds? How are they taxed? Debt Mutual Funds must allocate a minimum of 65% of their assets to Debt instruments, including bonds, T-bills, Certificates of Deposits, and similar securities. The tax rates and holding periods applicable to Debt Funds differ significantly from those of Equity Mutual Funds. From a tax perspective, for investments made before April 1, 2023: STCG is taxed as per your applicable Income Tax slab rate. However, long-term capital gains are taxed at 20% with indexation benefits. For investments made after April 1, 2023: LTCG and STCG earned on the debt mutual funds are taxable as per your income tax slab.

---

## #203 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #204 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #205 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled - routing to multpe RM , elimates COntext - Call duration average, conversion per RM, overall call per day - inbound patterns - rm have indirect insentive to help customer - list of issues, solution - rm motiwation, rm doesn’t know who to call - call are long, mfd says please hild while i create a case - t90 call - create dashboard for user information - transition mfd to auto serve Wati - templates and analytics - - Expired chats >24 hrs after user message

---

## #206 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #207 — LSQ Swach
**Status:** Unknown | **Last edited:** Unknown

# LSQ Swach **Title:** LSQ Opportunity Management – Solution Document **Date:** 18/07/2025 **Version:** v1.0 --- ## 🔷 Section 1: Customer Journey Solutioning ### 🔹 Objective To transition from a lead-centric to an opportunity-centric model in LSQ, enabling granular tracking across different types of customer interactions and ensuring all workflows are governed through opportunity objects. --- ### ✅ Key Requirements ### 1. Opportunity Types Configuration for Customers Set up the following distinct opportunity types in LSQ: - **Main Application (LAMF)** - **Enhancement** - **Foreclosure** - **LAS** (To be configured at a later stage) - **Renewal** Each opportunity type must be independently configurable, with distinct stages, activities, and associated automations. --- ### 2. Opportunity Attribute Support - All relevant **lead fields** (except name, email, and phone) will be replicated in the opportunity object. - A one-time schema sync between the LSQ backend and opportunity fields will be done to maintain consistency. - The Opportunity object will act as the **source of truth** for all downstream processes and reporting. --- ### 3. Lead to Opportunity Migration - All existing leads (excluding core identifiers: name, email, phone) will be migrated into new opportunities. - Migration logic will ensure backwards compatibility and data integrity. - **The migration from lead to opportunity will be interdependent, as all current flows are tightly integrated. Changes must be deployed simultaneously—partial implementation without complete migration is not feasible.** --- ### 4. Activity Management - Activities will be recorded and managed at the opportunity level, based on opportunity type. - Post-activity workflows will be executed based on opportunity state transitions. --- ### 5. Field Directionality - **One-way sync** from Opportunity → Lead for core fields (name, email, phone). - No data will flow from Lead → Opportunity to avoid overwrites. --- ### 6. Lead Automation Deprecation - Legacy lead-level automations (routing, field updates) will be **disabled**. - All process automations will now be driven by opportunity logic and configuration. --- ## 🔷 Section 2: Partner Journey Solutioning ### 🔹 Objective To establish a dedicated flow for managing the lifecycle of Partner (MFD) leads and activities using a structured, opportunity-driven model. --- ### ✅ Key Requirements ### 1. New Partner Lead Table - Introduce a **dedicated database table** for Partner (MFD) leads. - This will sync with LSQ and create a new partner lead distinct from the customer lead table. --- ### 2. New Opportunity Type: **MFD Activation** - Dedicated opportunity type

---

## #208 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #209 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #210 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #211 — Repeat B2B2C
**Status:** Unknown | **Last edited:** Unknown

# Repeat B2B2C MFD Activation Journey Field Update & Lead Schema Integration ### **Purpose:** To define and manage the set of fields that must be updated post-MFD activation journey completion and ensure these updates are shared with the lead schema for downstream processing by the Repeat team. ### **Scope:** - Capturing required data fields. - Defining when and how these fields are updated. - Updating the lead schema with the captured data. - Triggering opportunity closure upon journey completion. **The following fields need to be replicated in the lead schema:"** 1. MFD Name 2. MFD Phone Number 3. MFD Employee Name 4. MFD AUM 5. MFD ARN 6. MFD Email 7. MFD Activation Date 8. MFD Origin 9. MFD Partner Referral Link 10. MFD Customer Referral Link 11. Referred By 12. Referrer Name 13. Referrer Phone 14. Partner Account ID Additionally, include the list of customers referred so far. 1. All the customer-referred activity must be populated in the lead once activated. **In conclusion, the repeat team can work completely on the lead level, and the MFD activation team can work on the opportunity level** The activities that must be polluted in the lead fields are as follows: 1. Daily partner details update 2. Customer referred 3. Customer loan created

---

## #212 — LSQ BRD For MFD Activations
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

## #213 — Current Volt setup
**Status:** Unknown | **Last edited:** Unknown

# Current Volt setup We have around ~ 2500 MFDs Number of activated MFDs? Number of tickets chats on the Periskope /per day We have these tools - Periskope for group chat - Wati for Chat support - Exotel for call support - Zendesk for the internal ticketing - Retools for the Customer details -

---

## #214 — Periskope handling
**Status:** Unknown | **Last edited:** Unknown

# Periskope handling Problem ? - we have too many tools in servicing - As we have Wati and periskope for whatsapp we want to move to one platform - we are having difficulty in managing and reviewing the service SLA. we are missing out on the parter comms and not responding in many hours , this leads to lower MFD retention Goal ? - Increase MFD engagement and retention. - Do we have to add new number to Wati, or one number would suffice ? - If One number then how the handling between agents? - if Two then how will we handle the Display on the MFD , MFD based Number on dashboard ? Current Wati number for mFD? Current agent assigned to Wati? List of 500 MFD to move ? can we add the number and chat to Wati? We will be moving from Periskope to Wati List of the MFD to move ➖ Identify the MFDs to move communicate the Change to MFD Surge planning for the WATI Periskope to Wati Transition plan - Identify the MFDs to move :- https://docs.google.com/spreadsheets/d/1ONAVTJh3wK8kxfcf9j_GvWPis71DKvNbr78d7c342Lk/edit?usp=sharing - Communicate the change to MFD - Message template Dear <name>, We are updating our support communication channel to enhance our service quality. Please note the following: Effective immediately, all support interactions will be conducted through our new channel. Please use the WhatsApp number mentioned below for any Support request. CTA—> Link to Wati Number for message - Surge planning Day 0 - Create a bulk message template - Train and prepare agents Day 1 - We move the Single and inactive MFDs. By sending the message. We will not reply to Periskope after the message (Exception - If Wati is not working ) - Wati will be Serviced by → <Agent name>. Making sure that we have a dedicated resource and they have tools needed to help MFDs - Observe the Volume , allocate the Bandwidth from Periskope to Wati → <name of the agent > - We should expect some Comms from inactive MFDs due to confusion /curiosity. - Day 2 - Review the channel from yesterday - We move rest of the Single MFDs , Barring the top ~100 - We move Inactive 2 MFDs today as well - Same process of handling the Chat support - Day 3 - We move all the MFDs apart from the Top MFDs identified Analytics

---

## #215 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #216 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #217 — Notes Bharat
**Status:** Unknown | **Last edited:** Unknown

# Notes <>Bharat Negotiations table - we will close self-line until we can ensure 1 self-line per partner account. - Rate change, and PF - In tata we can’t change the Rate , so cashback is the option for the Tata. TDS Accounts payable Payment ops Commercials data on the entity - there are three entities applications partner platform that dictate commcials there is a base rate as per the lender that will be assigned by the BRE now once the ROI and PF are assigned to the user then the commencial terms should be added to the application as well on a applciations level we have We have different commercial terms with the on three entity levels application Partner Platfrom the commercials are the the param used to calculate the payout made for the user the Base rate is assigned as per the lender pricing grid of the time of application creation There is default commercials rate that get assigned to Partners and platform by default there are admin actions which assign for a application differenct ROI and PF and the split between the Volt and partner s we are currently not storing the commercials data on the entities level instead its a excel sheet , which casuses issues when calciualting the Solution possible to add object to the right entity that stores he commercials data Application level - ROI - PF - ROI split - PF slip - Base ROI - Base PF Partner level - offer applicable ? - Offer code - ROI - PF - ROI split - PF slip the ROI , PF and splits can be added to the application or to the partner, if added to the partner all the application created by the partner will be assigned the new commercials. Offer code is applied if the applicable. offer can be set of rules like >5 application in the month x = 5000 rs in the payouts Offer has a applicable to and from date the platfrom Platfroms have the similar - ROI - PF - SLITs - Slab based rules the data flow will be 1. application is created 2. assign base ROI and PF from the Lender pricing Grid 3. assign the Application level negotiated Rates collected from Admin actions 4. Assign the MFD commercials as default , then change if changed by the admin action 5. the Platform commercials will

---

## #218 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #219 — Cost estimates
**Status:** Unknown | **Last edited:** Unknown

# Cost estimates # AWS Infrastructure Cost Projections (2024-2026) ## Constants & Assumptions | Parameter | Value | Notes | | --- | --- | --- | | Growth Rate | 2x yearly | Partner base doubles each year | | Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) | | Retention Period | 84 months | 7 years for regulatory compliance | | Emails per Partner | 3/month | Registration, payout, GST notifications | | API Calls per Partner | 20/month | Includes all interactions | | Lambda Executions per Partner | 10/month | All automated processes | ## Growth & Cost Projections | Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | | --- | --- | --- | --- | | Active Partners | 2,500 | 5,000 | 10,000 | | Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB | | Cumulative Storage | 93 GB | 279 GB | 558 GB | | Monthly Emails | 7,500 | 15,000 | 30,000 | | Monthly API Calls | 50,000 | 100,000 | 200,000 | ## Monthly Cost Breakdown (USD) | Service | Year 1 | Year 2 | Year 3 | Scaling Factor | | --- | --- | --- | --- | --- | | S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation | | RDS | $45 | $65 | $110 | Step Function* | | Lambda | $3 | $6 | $12 | Linear | | SES (Email) | $0.75 | $1.50 | $3 | Linear | | API Gateway | $5 | $10 | $20 | Linear | | CloudWatch | $15 | $25 | $45 | Step Function* | | Route 53 | $0.50 | $0.50 | $0.50 | Fixed | | Step Functions | $2 | $4 | $8 | Linear | | **Total Monthly** | **$73.39** | **$118.42** | **$211.33** | | | **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** | |

---

## #220 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #221 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #222 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #223 — Payout Working File
**Status:** Unknown | **Last edited:** Unknown

# Payout Working File Errors earliar - We Currently don’t provide visibilty to MFD partner on there accrued balance( AP account data) to the MFD causing confusion between Payable and actual transaction. This is Due the way we have report format is configured - We are taking ad hoc payout request without proper recon process , this causes issues downstream. This is due to lack of visibility internally - We receive GST issues as Customer raise wrong invoices, This is because we don’t provide GST tax invoice to the partners - We get calls to get the visibility on the Payouts status and Ledger, as we don’t share the data before actual payout. as engineering uploads the data once a month - We have recon issues and Payout delays due to Commercial file changing and analytics need to debug the issues the commercial changes. This was just 10 applications in September - need to review previous months’ data. - We are unable to keep a upto date transactions table due to poor server infra at the lenders end. our transaction table is a month out of date - We need to streamline GST and TDS filing - We Don’t have a way to handle MFD ‘s without added bank account . ~~accrue payouts to a MFD~~ list , journey , use case ## Meeting notes - customer - cashback- - previously - partner - platform customer cashback Base rate - 10.49% , volt base rate - 9.95, —>9.99—> 10.49 march 2022. —>23—>24 <may 1st 9.99 9.99 -ROI base rate - 10.49%. 0.5 % cashback on may 1 we changed the base rate for the customer to 10.49% cusotmer cashback , partner to partner Selfline partner payout - MFD - Volt empaneeled MFD - MFD direct - through Software, redvisison or invest well, assest plus , zfunds , - MFD software - affiliates, - Ytbers , - Partner payout - apps like phonepe , jupiter, niyo, part+ - Money is calculated on the Principal outstanding , monthly average daily average, payout is calculated customer wise average POS, eod, for debit-credit sharing percentage with partners - 1. customer —> loan —> 1. credit to borrower 2. Credit to partner 3. Credit to platform 2. partner - volt- 3. upfront - one time payment, rs 200 for opening a account 4. trail income - 0.5 % into POS 5. category —> upfront and

---

## #224 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #225 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #226 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #227 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #228 — Query for MFD tiering
**Status:** Unknown | **Last edited:** Unknown

# Query for MFD tiering: WITH partnet_cte AS ( SELECT vdl_audit_partneraccounts.accountid AS partner_account_id, max(NULLIF(partnername,'nan')) as partner_name, MAX(NULLIF(accountholderphonenumber,'nan')) AS partner_phone_number, MAX( COALESCE(NULLIF(accountholderphonenumber, 'nan'),NULLIF(pa_sub.pa_alt_phonenumber, 'nan'))) AS partner_phone_number, max(case when address = 'nan' then null else json_extract_scalar(REPLACE(address, '''', '"'), '$.city') end) as partner_city, MAX(partnercode) AS partnercode, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') END) AS partner_arn, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') END) AS companyName, MAX(NULLIF(accountholderemail,'nan')) AS partner_email, MIN(CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END) + INTERVAL '330' MINUTE AS registered_date, MIN( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END )+ INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" left join (select accountid,coalesce(accountholderphonenumber,json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) as pa_alt_phonenumber from "volt-data-lake"."vdl_partneraccounts") pa_sub on pa_sub.accountid = vdl_audit_partneraccounts.accountid GROUP BY vdl_audit_partneraccounts.accountid UNION - - PART 2: From Partner Table not present in Audit SELECT partner.accountid AS partner_account_id, NULLIF(partnername, 'nan') AS partner_name, COALESCE(NULLIF(accountholderphonenumber, 'nan'), json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) AS partner_phone_number, json_extract_scalar(REPLACE(address, '''', '"'), '$.city') as partner_city, partnercode, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') AS partner_arn, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') AS companyName, NULLIF(accountholderemail, 'nan') AS partner_email, ( CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END ) + INTERVAL '330' MINUTE AS registered_date, ( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END ) + INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-data-lake"."vdl_partneraccounts" partner LEFT JOIN ( SELECT DISTINCT accountid FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" ) audit_check ON partner.accountid = audit_check.accountid WHERE audit_check.accountid IS NULL ), customer_cte AS ( select partner_account_id,date(first_created_on) as partner_active_date_application_first_created_on,partner_partially_active_date,partner_active_date,dhanda_activity_date from ( SELECT partner_account_id, first_created_on, MIN(date(first_created_on)) OVER (PARTITION BY partner_account_id) AS partner_partially_active_date, MIN(date(completed_on)) OVER (PARTITION BY partner_account_id) AS partner_active_date, MAX(date(completed_on)) OVER (PARTITION BY partner_account_id) AS dhanda_activity_date, ROW_NUMBER() OVER (PARTITION BY partner_account_id ORDER BY completed_on ASC) AS rn FROM "volt-analytics"."primary_application_full_info" -- WHERE partner_account_id = '072f9922-abe0-4c79-9883-1b26044767b8' ) sub where rn=1 ), partner_customer_detail_cte as ( select count(distinct application_id) as total_no_of_completed_applications,sum(app_pledged_credit_limit) as toal_pledged_credit_limit,partner_account_id,max(business_channel) as business_channel ,max(operating_channel) as operating_channel,max(platform_name) as platform_name from "volt-analytics"."primary_application_full_info" where current_step_id='COMPLETED' group by partner_account_id ), final_cte as ( select p.*, c.partner_active_date_application_first_created_on, c.partner_partially_active_date, c.partner_active_date, c.dhanda_activity_date, pc.total_no_of_completed_applications, pc.toal_pledged_credit_limit, pc.business_channel, pc.operating_channel, pc.platform_name from partnet_cte p left join customer_cte c on p.partner_account_id=c.partner_account_id left join partner_customer_detail_cte pc on p.partner_account_id=pc.partner_account_id ), volt_cte as ( select *,CASE WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10 THEN 'Super Gold' WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <=

---

## #229 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #230 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #231 — MFD Login data
**Status:** Unknown | **Last edited:** Unknown

# MFD Login data "total_partner_users": 77588, "never_logged_in": 12310, "first_login_mobile": 4978, "first_login_web": 31789, "first_login_other": 28511, "total_mobile_users": 24608, "total_web_users": 37813, "used_both_platforms": 21165, "used_only_other_platforms": 24028, "never_logged_in_percent": 15.87, "mobile_adoption_percent": 31.72, "web_adoption_percent": 48.74, "both_platforms_percent": 27.28 query ```jsx WITH first_logins AS ( SELECT user_id, MIN(created_date_time) as first_login_date, -- Get the platform of their first login platform as first_platform FROM user_login_audits WHERE created_date_time = ( SELECT MIN(created_date_time) FROM user_login_audits ua2 WHERE ua2.user_id = user_login_audits.user_id ) GROUP BY user_id, platform ), platform_usage AS ( SELECT DISTINCT rutpm.user_id, fl.first_login_date, fl.first_platform, CASE WHEN EXISTS (SELECT 1 FROM user_login_audits ua WHERE ua.user_id = rutpm.user_id AND ua.platform = 'VOLT_MOBILE_APP') THEN 1 ELSE 0 END as has_used_mobile, CASE WHEN EXISTS (SELECT 1 FROM user_login_audits ua WHERE ua.user_id = rutpm.user_id AND ua.platform = 'VOLT_WEB_APP') THEN 1 ELSE 0 END as has_used_web FROM relationship_user_to_partner_main rutpm LEFT JOIN first_logins fl ON rutpm.user_id = fl.user_id ) SELECT -- Total Users with Partners COUNT(*) as total_partner_users, -- Users who have never logged in COUNT(CASE WHEN first_login_date IS NULL THEN 1 END) as never_logged_in, -- First Platform Distribution COUNT(CASE WHEN first_platform = 'VOLT_MOBILE_APP' THEN 1 END) as first_login_mobile, COUNT(CASE WHEN first_platform = 'VOLT_WEB_APP' THEN 1 END) as first_login_web, COUNT(CASE WHEN first_platform NOT IN ('VOLT_MOBILE_APP', 'VOLT_WEB_APP') AND first_platform IS NOT NULL THEN 1 END) as first_login_other, -- Platform Usage Distribution COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END) as total_mobile_users, COUNT(CASE WHEN has_used_web = 1 THEN 1 END) as total_web_users, COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END) as used_both_platforms, COUNT(CASE WHEN has_used_mobile = 0 AND has_used_web = 0 AND first_login_date IS NOT NULL THEN 1 END) as used_only_other_platforms, -- Calculate percentages ROUND(100.0 * COUNT(CASE WHEN first_login_date IS NULL THEN 1 END)::numeric / COUNT(*), 2) as never_logged_in_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 THEN 1 END)::numeric / COUNT(*), 2) as mobile_adoption_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as web_adoption_percent, ROUND(100.0 * COUNT(CASE WHEN has_used_mobile = 1 AND has_used_web = 1 THEN 1 END)::numeric / COUNT(*), 2) as both_platforms_percent FROM platform_usage; ``` --- **Subject:** Empanelment Funnel & Landing Page Data (/partner) Hi Shivansh, Here’s the data for the initial landing page views of **/partner** and the subsequent steps in the empanelment journey. **Limitations:** - This data is for the **first two weeks of April** only. - Note: `/signup` and `/signup/` both refer to the empanelment flow. --- **Page Views (Apr 1–14, from Google Analytics)** | Page URL | Unique

---

## #232 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #233 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #234 — Kapture CX
**Status:** Unknown | **Last edited:** Unknown

# Kapture CX - they are connect with incred , phone pe (to be ) ![Screenshot 2024-12-23 at 4.16.58 PM.png](Kapture%20CX/Screenshot_2024-12-23_at_4.16.58_PM.png) - connectors with exotell and other functions - they have customer 360 with all the data that we can send , history , details , txns, - auto QA, for the call summary and interaction quality scoring - 13 years of experience. - Auto translate - Ticket history and summary - solutioning team , —> commercials —> timelines —>

---

## #235 — ARN mandatory for new Registrations
**Status:** Unknown | **Last edited:** Unknown

# ARN mandatory for new Registrations ### **Problem Statement:** - Currently, the partner registration flow allows users to sign up with or without providing an ARN. This has led to a high volume of registrations from individuals who are not certified Mutual Fund Distributors (MFDs). - Approximately 70% of current partner registrations fall into this category. This influx of non-MFD sign-ups places a significant strain on the onboarding team, requiring manual filtering and follow-up, reducing overall efficiency. ### **Proposed Solution:** Modify the partner registration process to require a valid AMFI Registration Number (ARN) for successful sign-up. This will ensure that only verified MFDs can register as partners on the platform. ### **Implementation Requirements:** - **Target Page:** https://staging.voltmoney.in/partner/signup/ (and subsequently production) - Only applicable on New registrations , not existing MFDs - **UI Changes:** - Remove the option/checkbox/link currently allowing users to proceed without an ARN (e.g., "I don't have an ARN number"). - Modify the ARN input field to be mandatory. - **Field Validation:** - The ARN field must not be empty upon form submission. - ~~The entered ARN must consist of exactly **6 digits**.~~ - *(Note: For this initial implementation phase, no external validation against the AMFI database is required.)* - **Error Handling:** - If the user attempts to submit the form without entering an ARN, display a clear inline error message (e.g., "ARN is required."). - ~~If the user enters an ARN that is not exactly 6 digits, display a clear inline error message (e.g., "ARN must be exactly 6 digits.").~~ - **Informational Text:** - Add clear text near the ARN field to inform users about the requirement and guide non-MFDs. Use the following text: > Enter your AMFI Registration Number (ARN)* > > > *Only registered Mutual Fund Distributors (MFDs) can sign up as partners. If you are an investor looking to use Volt Money, please go to our [**Customer registration**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.voltmoney.in%2F%3Fstartnew%3Dtrue).* > **Expected Outcomes & Benefits:** - **Reduced Non-MFD Registrations:** Significantly decrease (estimated 70% reduction) the number of sign-ups from users without a valid ARN. - **Improved Onboarding Efficiency:** Allow the onboarding team to focus solely on qualified MFD partners, streamlining the verification and activation process. - The Existing MFD has no impact / change **Potential Risks & Considerations:** - **Lower Overall Registration Volume:** Expect an initial decrease in the *total* number of registration submissions. However, the number of *qualified* registrations should remain stable or increase relative

---

## #236 — API Integration Changes for MFD Migration to LSQ A
**Status:** Unknown | **Last edited:** Unknown

# API Integration Changes for MFD Migration to LSQ Accounts **Document: API Integration Changes for MFD Migration to LeadSquared Accounts** ## **1. Introduction & Goal** This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module. The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner. ## **2. Current API Usage Summary (Pre-Migration)** - **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD). - **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record. - **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*. - **Activity Logging:** - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*. - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*. ## **3. Required API Changes (Post-Migration)** The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked. **3.1 MFD Creation** - **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API. - **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate - **Changes Required:** - Replace API calls creating MFD Leads with calls to the Account creation endpoints. - **Payload Construction:** - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first. - CompanyProperties: Provide an array of Attribute/Value pairs. - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name] - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup). - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" } - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" } - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" } - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field,

---

## #237 — MFCentral CAS API Response Structure Analysis
**Status:** Unknown | **Last edited:** Unknown

# MFCentral CAS API Response Structure Analysis ## Top-Level Structure ```json { "reqId": "string", // Request identifier "pan": "string", // PAN number of the investor "pekrn": "string", // PEKRN (optional identifier) "mobile": "string", // Mobile number with country code "email": "string", // Email address (optional) "data": [ // Array of fund house holdings { "summary": [...], // Summary data for this fund house "schemes": [...] // Array of schemes under this fund house }, // Additional fund houses... ], "portfolio": [ // Overall portfolio summary { // Non-demat holdings summary }, { // Demat holdings summary } ], "investorDetails": { // Investor information // Address and contact details }, "statementHoldingFilter": "string" // Filter applied (e.g., "NON-ZERO") } ``` ## Fund House Data Structure Each element in the `data` array represents holdings from a single AMC: ```json { "summary": [ { "amc": "string", // AMC code "amcName": "string", // AMC full name "isDemat": "string", // "Y" or "N" for demat status "currentMktValue": "number", // Current market value "costValue": "number", // Total investment amount "gainLoss": "number", // Profit/loss amount "gainLossPercentage": "number" // Profit/loss percentage } ], "schemes": [ { // Detailed information for each scheme } // Additional schemes... ] } ``` ## Scheme-Level Structure Each scheme contains detailed investment information: ```json { "amc": "string", // AMC code "amcName": "string", // AMC full name "folio": "string", // Folio number "investorName": "string", // Investor name "age": number, // Investor age "mobile": "string", // Registered mobile "email": "string", // Registered email "taxStatus": "string", // Tax status code "modeOfHolding": "string", // Single, Joint, etc. "transactionSource": "string", // Source of transaction (BSE, etc.) "schemeCode": "string", // Unique scheme identifier "schemeName": "string", // Complete scheme name "idcwChangeAllowed": "string", // Income Distribution Change allowed flag "schemeOption": "string", // Growth, IDCW, etc. "assetType": "string", // EQUITY, DEBT, etc. "schemeType": "string", // Classification "nav": "number/string", // Current NAV "navDate": "string", // NAV as of date "closingBalance": "number/string", // Total units held "availableUnits": "number/string", // Redeemable units "availableAmount": "number/string", // Value of available units "currentMktValue": "number/string", // Total current value "costValue": "number/string", // Total investment amount "gainLoss": "number/string", // Profit/loss amount "gainLossPercentage": "number/string", // Profit/loss percentage "isDemat": "string", // "Y" or "N" "lienUnitsFlag": "string", // "Y" or "N" "decimalUnits": number, // Decimal places for units "decimalAmount": number, // Decimal places for amounts "decimalNav": number, // Decimal places for NAV "brokerCode": "string", // Distributor ARN code "brokerName": "string", // Distributor name "isin":

---

## #238 — MFD Payout Calculation Automation
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout Calculation Automation **Introduction** Volt currently manages payout calculations for its Direct Mutual Fund Distributors (MFDs) through a highly manual process involving multiple Google Sheets, individual SQL queries, and significant analyst effort. This process is prone to errors, lacks scalability, presents a business continuity risk due to analyst dependency, and lacks clear auditability. This document outlines the requirements for building an automated, robust, and scalable Payout Calculation Engine to address these challenges specifically for Volt Direct MFDs. This engine will serve as the foundation for improving the overall payout experience, ensuring accuracy, timeliness, and transparency. 1. we need to handle changing factors like - Monthly Transactions table - Marketing Offers /Referral bonuses - New Platforms additions - Changes in commercials with existing platforms /partners - Changes in base rates / Format - Negotiations with MFDs 2. We need to be able to audit how an amount was generated 3. we need to be able to accrue the credits to an account based on the activity 4. We need to have the DB that is specific to transactions i.e we can't modify or delete the transactions that have happened, we can only rollback Problem statements Before base payout calculations - Delay in updating transaction table due to TATA API rate limits. We can’t differentiate the New transactions so we have download from beginning , this process currently take 3 days and growing. - We have to reconcile missing Credit applications between transaction table and second data source, currently this process is manual and second data source is not reliable. - Attribution of customer to correct Platfrom and partner require manual intervention. - We don’t store the PF and ROI paid by the customer in Credits table. - Commercials on transactions are added from the Partner commercials sheet manually, we don’t store share and Rates with the Credit application Data adding steps to calculate the payouts After the Base payout calculation - TDS rules change and have to accommodate - GST payout are tracked manually Payout process - Tracking payout transactions Reconciliation takes 4 (2+2) days with HSBC - For Platform Payouts we need to provide a statement and how the Payout amount is calculated. - Partners have a hard time understanding statements. Potential solutions - Get TATA to improve the API data provided to get the updated transactions - Better fall-back handling on our side Activity activity triggers a

---

## #239 — MFD payouts payment reconciliation
**Status:** Unknown | **Last edited:** Unknown

# MFD payouts payment reconciliation Problem statements - It takes 3-4 days to reconcile payouts to MFDs - It takes 2 day to make bulk payments and get the status back from the HSFC. - We have to wait 2 days and try to make payment again to MFDs for whom the Payment have failed , this takes another 2 days to reconcile -

---

## #240 — Periskope to wati plan
**Status:** Unknown | **Last edited:** Unknown

# Periskope to wati plan # Periscope to Wati Migration Plan ## 1. Current Periscope Issues - No effective tracking of incoming chats or resolutions - Lack of chat status visibility (open/resolved/WIP) - Unable to monitor active chat groups - No categorization between sales and service chats - Missing bulk chat download capability - No response time (TAT) tracking - Agents losing track of ongoing conversations - Limited team capacity (2 people per shift) - No chat closure mechanism - Unclear analytics definitions - Missed chats going unnoticed - Integration issues with WATI ## 2. Metrics Comparison ### Current Periscope Metrics - Total interactions count - Unopened messages - Basic chat volume - Group activity status ### Available Wati Metrics - Open/Pending/Solved tickets - First Response Time - Resolution Time - Bot vs. Operator solutions - Expired conversations - Missed chats - Operator performance - Message delivery status - Conversation types - Tag distribution ## 3. Migration Goals 1. Improved Tracking - Real-time chat status - Response time monitoring - Issue categorization 2. Better Resource Management - Automated workflows - Clear agent allocation 3. Enhanced Analytics - Detailed performance metrics - Customer satisfaction tracking 4. Streamlined Operations - Automated responses - Efficient ticket management ## 4. Migration Plan with Checkpoints ### Phase 1: Setup (Day 0) - [ ] Configure Wati dashboard - [ ] Set up automated responses - [ ] Create tags and categories - [ ] Test message templates - [ ] Train agents **Checkpoint Metrics:** - System functionality - Template delivery success - Agent readiness scores ### Phase 2: Initial Migration (Day 1) - [ ] Migrate single and inactive MFDs - [ ] Monitor initial responses - [ ] Track conversion rate - [ ] Handle exceptions **Checkpoint Metrics:** - Message delivery rate - Response times - System stability ### Phase 3: Main Migration (Day 2-3) - [ ] Migrate remaining MFDs excluding top 250 - [ ] Monitor scalability - [ ] Adjust resources as needed **Checkpoint Metrics:** - Chat volume handling - Resolution rates - Customer feedback ## 5. Communication Templates ### Periscope Exit Message ``` Dear [MFD Name], To enhance your support experience, we're upgrading our communication channel. From [Date], we'll be transitioning to a new WhatsApp support system. Key Points: - Last day on current system: [Date] - New support number: [Number] - Transition period: [Duration] For any questions, please contact

---

## #241 — rough
**Status:** Unknown | **Last edited:** Unknown

# rough notes - Tat on a chat , - ticket resolution and creation - check whatsapp api changes Ideal flow MFD is had a request or a issue they communicate the issue with us we mark it as issue and solve it MFD —> Issues —> communications —> Tickets—> solution - IF a MFD or there employees have issues they can reachout to volt and we want to solve the issues promtly - MFD can communicate with us through WhatsApp chat - Now we need to Identify the issues , create a ticket and resolve the ticket Current problems - We don’t have the ticketing system in place - Current tools we are using are not optimal for creating and tracking Tickets Raw notes - The MFD facing challenges in getting timely response - All the onboarded MFD are added to periscope group - MFD’s uses WATI when they interact through Dashboard chat - MFD’s has to use two separate chat channel if they open up a Whatsapp channel through Wati - MFD’s ask , servicing , payout topic of communications are of general nature. our challenges - We have limited ( can’t) tracking of the incoming chats and there resolution - This is a Periskope limitation. we don’t get Open , resolved , WIP status of a Chat - we are unable to check “How many chats groups are active “ , “were active last week “ - We can’t identify if chats are Sales or service related - we get ~100 chats a day - There is no Bulk download chat option in Periscope - we can’t see TAT for a response and resolution - - agents loose track of the ongoing chats , as it chats are pushed to the bottom of the que and it become a issue to differentiate between the chat groups - 2 people work on the periscope - No way of closing the chats and mark that issue was solved - Analytics- daily number of message counts, Flagged messages - no explanation of what these terms are - How to raise tickets is not clear to the team - we use Periscope to reach out to MFDs , If a MFD reach-out and RM are unavailable then we assign another agent to Periscope - group is already connected with Periscope , all all the MFD are added to periscope they are

---

## #242 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs

---

## #243 — Activation LSQ Task Creation
**Status:** Unknown | **Last edited:** Unknown

# Activation: LSQ Task Creation Flow: 1. Link generated gets generated and sent to the MFD over whatsapp 2. Task gets published in LSQ 3. RMs follow the tasks for calling and supporting the MFD with the VKYC flow and the link

---

## #244 — KT discussion 19th Feb
**Status:** Unknown | **Last edited:** Unknown

# KT discussion 19th Feb ## Flows - MFDs number - Customer number MFD flow - Pre-empanelment - Outbound → Labdhi - Inbound → OE team - Post empanelment - Outbound → OE team - Inbound → OE team (lead owner) - RM - RM **Leadsquared tracking** - **Inbound call picked** - **Inbound call task with disposition** - **Backup lead owner** - Check team / attribute - Backup assignee should have lead access - Missed call task - Outside business hours - No Assignee available - Assigned but not picked - Inbound call activity / duration / activity **Other questions** - If lead doesn’t exist? **Notes:** - whats will happen if we change role/team name on LSQ, how switch case will work - Discuss in exotel - Need to check if we are saving owner details of all lead on volt DB - Need to check with ENOSH - If no lead found on LSQ then what will happen in case of exotel inbound, create lead and assign to team based on lead origin - Exotel inbound call - lead info modal should open on LSQ dashboard - If outside of business hours, create missed call task - If unanswered, create task for lead owner - Labdi teams call should assign to Volt Onboarding team - Ask Exotel to share BRD and take sign-off from Volt - What will be ETA on Exotel to implement solutions

---

## #245 — Detailed scope
**Status:** Unknown | **Last edited:** Unknown

# Detailed scope # Design Language System Documentation A comprehensive guide for Volt Money and DSP Finance ## Table of Contents - [1. Foundation](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#1-foundation) - [2. Components](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#2-components) - [3. Behaviors & Interactions](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#3-behaviors--interactions) - [4. Usage Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#4-usage-guidelines) - [5. Developer Tools](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#5-developer-tools) - [6. Logic & Business Rules](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#6-logic--business-rules) - [7. Platform-Specific Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#7-platform-specific-guidelines) ## 1. Foundation ### A. Design Tokens ### Colors - Primary palette - Secondary palette - Neutral colors - Semantic colors - Success - Error - Warning - Info ### Typography - Font families - Font weights - Size scales - Line heights - Letter spacing - Semantic styles - Headings (h1-h6) - Body text - Labels - Display text ### Spacing - Scale system - Layout spacing - Component spacing - Margin and padding rules ### Borders - Width scales - Radius scales - Styles - Color tokens ### Shadows - Elevation levels - Usage guidelines - Color and opacity ### Motion - Duration tokens - Easing functions - Animation patterns ### Grid/Layout - Grid system - Breakpoints - Container widths - Column configurations ### B. Brand Assets ### Logo - Primary logo - Secondary variations - Clear space rules - Minimum size - Usage guidelines ### Icons - Icon system - Size guidelines - Style guidelines - Usage rules - Icon library ### Illustrations - Style guide - Usage scenarios - Color application - Size guidelines ### Photography - Style guide - Composition rules - Color treatment - Usage scenarios ## 2. Components ### A. Base Components (Atoms) ### Buttons - Primary - Secondary - Tertiary - Icon buttons - States: - Default - Hover - Active - Disabled - Loading ### Inputs - Text input - Number input - Select - Checkbox - Radio - Toggle - States and validation ### Typography Elements - Headings - Paragraphs - Links - Lists - Inline elements ### Icons - Usage - Sizes - Colors - Alignment ### B. Composite Components (Molecules) ### Input Groups - Label + Input - Input + Button - Input + Icon - Validation messages ### Form Fields - Layout - Label placement - Helper text - Error states - Required fields ### Search Bars - Simple search - Advanced search - Filters - Results display ### Navigation Items - Menu items - Breadcrumbs - Tabs - Pills ### C. Patterns (Organisms) ### Forms - Layout patterns - Validation patterns - Submission patterns - Error

---

## #246 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: AUM, Short of this trail, Weekly reports, Impact of AUM on their customers, interactive way Kevin (Servicing): the number needs changed, choose funds, for tenure, lender change, MFD customers, 2 time sefie enchancement process Mahesh: Short videos, Error. Govt app, Graphs to explain shortfall Names: Dashboard feedback

---

## #247 — Hindi Questionnaire
**Status:** Unknown | **Last edited:** Unknown

# Hindi Questionnaire ### Warm-Up Questions 1. Aapne Volt Money ke baare mein kaise suna? 2. Volt ka use karte hue aapka anubhav kaisa raha? 3. Aap kya karte hain? Din lamba raha hoga? 4. Aapne Mutual Fund mein invest karna kab aur kaise shuru kiya? --- ### **Exploring Financial Interests and Habits** 1. Aapne Mutual Fund mein invest karna kab aur kaise shuru kiya? - "Aapne wo particular fund kaise choose kiya?" - "Us samay aapne aur kaunse investment options consider kiye?" 2. Aap apni finances ki planning kitni baar karte hain? - Kya aap ye yearly, monthly, ya daily karte hain? - Iske liye aap kaunsa tool use karte hain? 3. Pichhle kabhi unexpected expense ya financial emergency ke baare mein bataye. - "Aapne isse handle karne ke liye kya kiya?" - "Aapne kaunse options consider kiye?" - "Aapne kaunsa option choose karne ka decision liya aur kyun?" 4. Aakhri baar aapne kisi asset (jaise gold, FD, shares) ka use kab kiya tha? Jaise FD todna, shares bechna, ya Mutual Fund se paisa nikalna? 5. Aap abhi kin banks ke saath jude hain, aur unke saath apna experience kaise rate karte hain? - Aapne XYZ bank ko baaki banks se zyada rate kyun kiya? --- ### Identifying Influences 1. Kya koi kahani, anubhav, ya salah hai jisne aapke loans lene ya financial planning ka tarika badla ho? - Kya koi friend, family member, ya expert hai jinki financial advice par aap pura bharosa karte hain? Kyun? 2. Apne investments, liquidity, aur overall planning ke liye aap kin sources par rely karte hain? 3. Aapko kaunse financial apps sabse zyada pasand hain aur kyun? --- ### Uncovering Motivations and Goals - Maal lijiye ki aapke paas do alag-alag lenders hain. Kaun-si cheezein aapko ek ko dusre se better lagne ka ehsaas karati hain? - Aapka agla bada kharidaari ya investment kya hai? - Aap loan ya credit lene ke liye kin reasons ki wajah se zarurat mahsoos karte hain? - Aapko loan kitni jaldi chahiye hota hai? - Loan kitne samay ke liye lena aapko theek lagta hai? - Koi aisa goal ya sapna jo aap kaafi samay se achieve karne ki koshish kar rahe hain? Yeh aapke liye kitna important hai? - (Kya aisa koi sapna hai jiske liye aap paise jama kar rahe hain?) - Kya aap asset-backed loans aur unsecured loans ke beech koi preference rakhte

---

## #248 — User Research Framework
**Status:** Unknown | **Last edited:** Unknown

# User Research Framework ### User research guide ## **Step 1 : Defining Purpose & Objectives** Define the goals of the research to ensure alignment across stakeholders. The research objective should answer - What decision do you need to make for which you need data through user research? - What assumptions are you trying to validate - What would success of this user research look like ## **Step 2 : Target the right and varied User Segments** To ensure comprehensive insights, target varied user groups based on relevant characteristics. Use the following parameters to define your user cohorts: 1. **By User Personas:** - Leverage pre-defined personas representing key demographics, behaviors, or motivations. - Example: - **Persona A**: New users exploring the product. - **Persona B**: Long-term users engaging with advanced features. 2. **By Task-Based Segmentation:** - Categorize users based on their interactions with specific features or tasks: - **Completion:** Users who successfully completed the task. - **Abandonment:** Users who started the task but dropped off. - **Non-Starters:** Users who never attempted the task. ## Step 3 : Selecting the right Research Method Select methods tailored to your objectives and audience. | **Stage** | **Method** | **Purpose** | Examples | Focus on | | --- | --- | --- | --- | --- | | **Exploration** | User Interviews | Discovering Needs and Pain Points | Amazon or Airbnb uses exploratory research when entering new markets or identifying adjacent user needs | Understand attitudes, motivations, and unmet needs. | | | Surveys | | | Gather quantitative preferences at scale. | | **Validation** | Usability Testing | Testing Solutions for Effectiveness | Google routinely conducts rapid validation for its features using A/B testing | Test ease of use for loan application processes. | | | Surveys | | | Assess clarity of repayment terms and options. | | **Tracking** | Behavioral Analytics | Monitoring User Interactions | Facebook employs tracking through behavioral analytics to refine its News Feed algorithm, using live user data rather than pre-launch tests | Identify friction points in user flows (e.g., drop-off rates). | ### Good articles on user research [Defining the Objectives of User Research](https://www.interaction-design.org/literature/article/defining-the-objectives-of-user-research) [How to conduct user research: A step-by-step guide](https://designstrategy.guide/ux/ux-research-guide/) [The Key Factors Driving Silicon Valley Companies' Success - Attorney Aaron Hall](https://aaronhall.com/the-key-factors-driving-silicon-valley-companies-success/) ## Parameters for types of research **Exploration Type:** Discovering Needs and Pain Points - Motivations - Aspirations - Influences - Context

---

## #249 — V0 1 for User Research
**Status:** Unknown | **Last edited:** Unknown

# V0.1 for User Research Hypothesis (Investment profile, Debt profile, Evaluation criteria, Repayment behaviour ## What do we need to know about our users 1. Basic details - Age range - Location type (urban/suburban/rural) - Occupation - Family situation (single, married, dependents) 2. Financial Profile - Asset types they own (stocks, bonds, crypto, etc.): - Asset value range - Income level - Existing debt obligations - Investment experience level - Financial goals and priorities 3. Evaluation Behavioural - How do they evaluate on taking loans - Research habits before financial decisions - Level of detail needed for decision-making - Key questions they need answered - Required reassurances about the process 4. Motivations & Goals - Primary reason for seeking a loan - Urgency for loan - Preferred loan amount range - Plans for using the loan - Long-term financial objectives - What makes them choose asset-backed loans over traditional loans 5. Pain Points & Fears - Concerns about using assets as collateral - Trust issues - Knowledge gaps about lending processes - Previous negative experiences with loans 6. Information Needs - Types of content they consume - Preferred learning style about financial products 7. Journey Touchpoints - How they discovered Volt - Research methods used - Key decision factors - Support needed during the application process ## Questionnaire: User Calls [20] ### Warm-Up Questions 1. How did you hear about Volt money? 2. How has your experience been using volt? 3. What do you do, must have been a long day? 4. When and how did you start investing in Mutual Funds? ### **Exploring Financial Interests and Habits** 1. When and how did you start investing in Mutual Funds? - "Walk me through how you chose that particular fund?" - "What other investment options did you consider at that time? 2. How often do you plan your finances? 1. Do you do it every year, month or daily? 2. What tool do you use to track the same 3. Tell me about the last unexpected expense/financial emergency you faced? - "Walk me through exactly what you did to handle it?" - "What options did you consider?" - "How did you decide which option to go with?" 4. When was the last time you used an asset (like gold, FD, shares) i.e break our FD, Shares or MF? 5. Which banks do you currently have relationships with, and how would you

---

## #250 — DSP Finance Website About DSP Group
**Status:** Unknown | **Last edited:** Unknown

# DSP Finance Website: About DSP Group DSP finance is part of the broader DSP Group, a leading financial services conglomerate in the capital markets space. DSP Asset Managers Pvt. Ltd. (commonly known as **DSP Mutual Fund**) is one of India’s most trusted asset management companies, managing investments across equity, debt, and hybrid categories. With a strong legacy of over 160 years through the DSP Group, the AMC focuses on long-term wealth creation, prudent risk management, and investor-centric solutions. - The **DSP Group** traces its roots back to the 19th century and has a rich history in Indian capital markets. - In the 1990s, DSP partnered with Merrill Lynch to launch DSP Merrill Lynch Asset Management, which later became DSP BlackRock. - In 2018, the DSP Group bought back BlackRock’s stake, and the AMC was rebranded as **DSP Mutual Fund**. - Today, DSP AMC continues to operate as a 100% Indian-owned asset manager, combining **global best practices** with deep understanding of Indian markets. DSP AMC serves lakhs of investors across the country, offering a diversified suite of mutual fund products to help individuals and institutions achieve their financial goals. Key items to talk about. - AUM of 1.5L CR - Investor base of 50L - Distributor base of 80K+ - 28+ years of investment experience More about DSP AMC can be found at https://www.dspim.com/about-us.

---

## #251 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #252 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #253 — Bug Fix Process
**Status:** Unknown | **Last edited:** Unknown

# Bug Fix Process # Challenges Currently, Volt’s platform is being constantly modified to suit the requirements of new initiatives and business scenarios. As we grow rapidly, we need to streamline our bug-fix process to drive higher quality across the board. - Increased man-hours spent on fixing issues - Customers escalating about functional or technical issues - Partners escalating about functional or technical issues - Increased number of bugs being reported - Lack of a feedback loop or learning from each bug The above challenges arise due to the below elements. - Bugs and fixes are being rolled without product sign-off - Bugs and fixes are being rolled without design sign-off - Bugs aren’t religiously analyzed for RCAs - Product team isn’t involved or doesn’t drive bug fixes - Stakeholders ask oncall for enhancements or even new features # Proposed Solution Below are the interventions proposed to solve these challenges. - Streamline the reporting process from multiple sources (TBD). - Oncall dev unblocks the customer quickly where feasible. - Oncall dev identifies the RCA. - All reported issues are categorized into features, enhancements or bugs. - Bugs are prioritized and addressed as per impact and routed through release process. - Features and enhancements are prioritized and addressed as per impact and routed through sprint process. Link to [Product Release Process](Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md). # Proposed Process Below is the proposed process to address these challenges. - Oncall dev receives the ticket from any one of the sources of reporting. - Oncall dev unblocks the customer through a quick-fix or moving the application forward where possible. - Oncall dev classifies the ask into one of the buckets on Jira and tags the program manager after conducting a detailed RCA after the quick fix. - **New feature**: this could be anywhere from a large feature to a small feature but is a capability that doesn’t exist in the system and needs product intervention. - **Enhancement**: this could be a tweak in the logic or minor scenario handling for an existing feature and needs product intervention. - **Bug fix**: this could be an issue at Volt’s end due to a technical or functional issue and impacts users. - All new features and enhancements are tagged to the respective PM on Jira. - PM evaluates the ask and prioritizes it as part of the backlog. - PM informs the stakeholder about the timelines when picked up by

---

## #254 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #255 — Referral Product Note (1)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note (1) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and

---

## #256 — Referral Product Note
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility and program

---

## #257 — Referral Product Note [Claim approaches]
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Referral Product Note [Claim approaches] ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - **Existing Volt users (borrowers / opportunities)** Existing Volt users have no structured way to refer Volt to friends and get incentivised for the same. - **New potential users (referees)** They lack guidance in terms of trust and credibility on Volt as a platform to avail fast digital loans against Mutual funds and are dependent on friends who have already used Volt. Also there is no incentive that they receive on completing loan journey. - **Business team** Business lacks a scalable, low-CAC acquisition lever to leverage the existing user base to acquire new users - What is the challenge that they are facing? What is broken today? - Referrals might happen **informally** but there is no robust mechanism **to track** end to end and motivate existing users to refer more. - There is no system currently to scale the trust factor and brand of Volt being via low-CAC word of mouth viral mechanism. - Business cannot reliably measure **ROI, conversion** on new acquisitions via referral in an organised and systematic manner. - Why is it important? or What is getting impacted? - **High CAC** from paid channels continues to scale. - We miss out on **trust-led growth** from existing users. - Drop-offs in referee journey remain high due to lack of motivation. - Poor operational scalability risks future campaign launches. - Inability to experiment with referral-led growth limits topline impact. --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics - First 1000 referral signups - # of successful referrals (loan account opened above Rs.25000) --- ## **3. Solution Scope** ### Solution overview - We are introducing a **configurable B2C Referral & Rewards system** that allows eligible Volt users to refer friends, track their progress across the loan lifecycle, and earn rewards when referred user successfully completes the loan application journey along with achieving other defined outcomes as per mentioned Terms & Conditions of the program . The solution includes: - Backend-driven eligibility