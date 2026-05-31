# Current State: Comms

> Auto-generated from 289 PRD(s). Most recently edited shown first.


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

## #5 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

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

## #7 — Streamlining Support Communication by Segregating
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

## #8 — AI Chatbot
**Status:** Not started | **Last edited:** September 1, 2025 10:48 AM

**Problem:**
are we solving?**

Currently the FRT for the response is higher (9+ minutes)
Average resolution time of the chat is 60+ minutes)
No 24 hour service limited hour servicing

---

**Solution:**
?**

The **AI Chatbot Proof of Concept (POC)**, this document outlines the **Phase 1 scope**, focused on backend integration, benchmarking, and foundational design to prepare for future customer-facing deployment via **WATI**.

---

## #9 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #10 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #11 — Email Validation Approach PhonePe
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

## #12 — [Lending stack] Welcome mail
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

## #13 — DSP communication email template
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

## #14 — MFD Payouts
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

## #15 — Bulk email automation
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

## #16 — Integrated Sales tool
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

## #17 — [Lending stack] KYC Flow
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

## #18 — API and Transaction Logging
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

## #19 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #20 — Process note Creating a new user on Command Centre
**Status:** Done | **Last edited:** November 8, 2024 9:36 AM

# Process note: Creating a new user on Command Centre # Process Note: Creating a User on Command Centre ## Overview This document outlines the step-by-step process for creating a new user account on the Command Centre system. ## Prerequisites - Admin access to the Command Centre system - New user's details (full name, email address, role, department) - Approval from Head of Operations (@Nishant Athmakoori) [Access level details](https://docs.google.com/spreadsheets/d/1VSPMYia-Kmwob9X3pH-T3nMTYNZxXpEC_Afpfq27e-o/edit?gid=0#gid=0) ## Steps 1. Request for access on Email from the business counterpart, in this case, all access will be shared by @Nishant Athmakoori 1. Details required in the email: 1. Name 2. Designation 3. Role (Admin / Approver / Read only) 4. Employee ID 5. Mobile number 6. Email address (DSP Email address) Any requests without the aforementioned details will get rejected 2. Forward the access with consent and approval to tech-ops@dspfinance.com 3. Access will be shared within 1 working day of request. 4. Once access is shared (User name and password), logon to the command centre using the following URL: https://cc.dspfin.com/login 5. Once logged on, users will be able to use the command centre for the following utilities: 1. Client search (all roles) 2. Loan search (all roles) 3. Review client details (all roles) 4. Review client KYC details (all roles) 5. Review client risk details (all roles) 6. Review loan details (all roles) 7. Review transactions (money and collateral) (all roles) 8. View servicing tasks (Approver and admin only) 9. View collateral tasks (Approver and admin only) 10. View application tasks (Approver and admin only) 11. View NBFC operations tasks (Approver and admin only) 12. Approve or reject tasks (Approver and admin only) ## Post-Creation Steps - Document the new user creation in your system log or user management spreadsheet ## Troubleshooting If you encounter any issues during this process, please contact the IT support team at tech-ops@dspfinance.com

---

## #21 — Lodgement maker
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

## #22 — Periskope
**Status:** In progress | **Last edited:** November 29, 2024 1:55 PM

# Periskope [Periskope to wati plan ](Periskope/Periskope%20to%20wati%20plan%2014ce8d3af13a80849cf2d1d5e048585e.md) ### Current Challenges: 1. **Limited Tracking**: We cannot effectively track incoming chats or their resolutions due to limitations in Periscope. 2. **Chat Status Visibility**: There is no visibility into chat statuses (e.g., open, resolved, work-in-progress). 3. **Active Chat Monitoring**: We cannot determine how many chat groups are currently active or were active in the last week. 4. **Categorization Issues**: There's no way to identify whether chats are related to sales or service. 5. **Chat Volume**: We receive around 100 chats daily. This a 6. **Lack of Bulk Chat Download**: Periscope does not offer a bulk download feature for chat records. 7. **Response Time (TAT)**: We are unable to track response times or resolution times for chats. 8. **Agent Tracking Issues**: Agents lose track of ongoing chats as new chats push older conversations to the bottom of the queue, making it difficult to manage multiple conversations. 9. **Limited Team Capacity**: Only two people manage Periscope at a time, which limits our ability to handle high chat volumes effectively. 10. **No Chat Closure Mechanism**: There is no way to close chats or mark them as resolved. 11. **Unclear Analytics**: Terms such as "daily message counts" and "flagged messages" lack clear definitions and explanations. 12. **Ticketing Process**: The process for raising tickets is unclear to the team. 13. **Unavailability of RM (Relationship Managers)**: If an MFD reaches out and the assigned RM is unavailable, another agent is assigned to Periscope to manage the chat. 14. **Periscope and WATI Integration**: While all MFDs are connected to Periscope, they are not added to WATI, leading to inconsistencies in communication channels. 15. **Missed Chats**: Missed chats often go unnoticed until they escalate, as there is no way to flag or track missed communications in real time. ## Visibility There are three visibility that we need. - Visibility on Chat messages - Visibility on the issue resolution - Visibility on the Impact of the Providing support Table 1: Visibility on Interactions with MFD Partners | Metric | Description | Current | Wati (option 1 ) | Suggested | | --- | --- | --- | --- | --- | | Total Interactions | Number of interactions with MFD partners | Tracked in Periskope | | | | Call Volume | Number of calls between RMs and MFDs | exotell | | | | Chat Volume | Number of chat conversations

---

## #23 — LSQ misattribution b2c of B2b2c data
**Status:** Ready for Tech | **Last edited:** November 27, 2024 11:25 AM

# LSQ misattribution b2c of B2b2c data # B2C to B2B2C Lead Update Specification ## Background When MFD (Mutual Fund Distributor) B2B2C leads originate from a B2C platform, we currently use admin actions to assign a lead MFD partner. While the MFD details are stored in our database, they are not synchronized with LeadSquared (LSQ). This creates two primary issues: 1. Lead tracking inefficiencies 2. Service misalignment (B2B2C leads incorrectly assigned to B2C support teams) 3. MFD partner dissatisfaction with direct customer contact ## Objective Reduce misattributed leads - Reduce Creation of the new Misattributed leads. - Update LSQ with admin action (tech pickup) - Backfill data to correct misattribution Implement functionality to update existing B2C leads to B2B2C leads in LeadSquared by synchronizing referral data from our database. ## Technical Implementation ### API Details - **Endpoint**: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate) - **Identifier**: Mobile Number (unique in LSQ) ### Required Field Updates ```json { "LeadDetails": [ {"Attribute": "mx_Channel", "Value": "B2B2C"}, {"Attribute": "Source", "Value": "MFD Referral"}, {"Attribute": "mx_Referred_By", "Value": "MFD"}, {"Attribute": "mx_Referrer_Name", "Value": "[MFD_NAME]"}, {"Attribute": "mx_Referrer_Phone", "Value": "[MFD_PHONE]"}, {"Attribute": "mx_Referrer_Email", "Value": "[MFD_EMAIL]"}, {"Attribute": "mx_Referrer_Account_Id", "Value": "[MFD_ID]"}, {"Attribute": "mx_Referral_Code", "Value": "[REFERRAL_CODE]"}, {"Attribute": "Phone", "Value": "[CUSTOMER_PHONE]"}, {"Attribute": "SearchBy", "Value": "Phone"} ] } ``` ## Data Migration Plan ### Initial Data Reconciliation - Tech team to provide excel export of leads updated via admin actions - Data to be shared with LSQ team for backfill - Impact: Approximately 12% of leads are currently miscategorized (Extrapolated form a daily count) ### Scope Limitations - Full LSQ-DB reconciliation not feasible due to lack of MFD assignment markers in LSQ - Focus on forward data synchronization and provided historical data only ### MFD Status Handling - Automated daily updates for partially-activated MFD status ## Requirements ### Technical Requirements 1. Admin action implementation for borrower-partner relationship updates 2. API integration with error handling 3. Comprehensive update logging for audit purposes ### Acceptance Criteria 1. Successful lead type transition (B2C to B2B2C) 2. Accurate referrer information mapping 3. Proper API response handling 4. Complete audit logging 5. Visual verification in LSQ dashboard ## Important Notes - Mobile Number serves as the unique identifier in LSQ - Lead merges occur when same email is used with different phone numbers - Implementation must include robust error handling for API failures - API failures should be notified to the team.

---

## #24 — Internal Alerting Platform v1
**Status:** Ready for Tech | **Last edited:** November 25, 2024 4:56 PM

**Problem:**
are we solving?**

Volt works with multiple 3rd parties (lenders, public repositories and vendors) to help power its journeys. While this helps expedite development and reduces development effort, it does indeed induce additional points of failure like performance degradations and downtimes (scheduled & unscheduled). 

The impact of these can be seen across acquisition, conversions and retention.

- Customers not able to complete the journey due to disruptions impacting conversions
- Partners not happy with Volt’s platform due to disruptions impacting business
- Customers give poor rating to V

**Solution:**
?**

---

## #25 — Volt B2B Redirection Enhancement - Park+
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

## #26 — QC rejection flow handling for DSP - Volt LOS
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

## #27 — New Posidex report template
**Status:** In progress | **Last edited:** November 20, 2024 4:54 PM

**Problem:**
are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

**Solution:**
?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

---

## #28 — QA setup for Partners
**Status:** Not started | **Last edited:** November 20, 2024 2:05 PM

# QA setup for Partners ## Current Challenges 1. No test coverage for SDK implementations 2. Absence of platform logging 3. No standardized testing setup for partner journeys 4. Limited testing capabilities through playground environment ## Immediate Priority Areas ### 1. Test Coverage Implementation (Q1) - **SDK Testing Framework** - Implement unit testing for all SDK versions (JS, RN, Android, iOS) - Set up integration testing framework - Target initial coverage of 60% for critical paths - Required Resources: 2 QA Engineers, 1 DevOps Engineer - **Frontend Testing** - Implement E2E testing using Cypress/Playwright - Create component testing suite - Setup visual regression testing - Required Resources: 1 QA Engineer, 1 Frontend Developer ### 2. Logging & Monitoring System (Q1) - **Platform Logging** - Implement centralized logging system (ELK Stack/Splunk) - Set up real-time monitoring dashboards - Create alert mechanisms for critical failures - Required Resources: 1 DevOps Engineer, 1 Backend Developer ### 3. Partner Journey Testing Framework (Q2) - **Automated Testing Setup** - Create standardized test cases for each integration type - Redirection flows (PhonePe, Park+, etc.) - SDK implementations (Jupiter, Zype, etc.) - Implement automated testing pipeline - Setup test data management system - Required Resources: 2 QA Engineers ### 4. Testing Environment Enhancement (Q2) - **Enhanced Playground** - Develop comprehensive testing interface - Create partner-specific testing scenarios - Implement mock services for external dependencies - Required Resources: 1 Frontend Developer, 1 Backend Developer ## Resource Requirements Summary - 2 QA Engineers (Full-time) - 1 DevOps Engineer - 1 Frontend Developer - 1 Backend Developer - Testing Infrastructure Budget ## Implementation Timeline ### Phase 1 (Q1) 1. Week 1-2: Setup basic testing infrastructure 2. Week 3-6: Implement logging system 3. Week 7-10: Develop SDK testing framework 4. Week 11-12: Initial frontend testing implementation ### Phase 2 (Q2) 1. Week 1-4: Partner journey framework development 2. Week 5-8: Enhanced playground implementation 3. Week 9-12: Integration and system testing ## Success Metrics 1. Test Coverage: - 80% coverage for critical paths - 60% overall coverage 2. Platform Stability: - 99.9% uptime for integration services - <1% failed transactions due to technical issues 3. Partner Satisfaction: - <4 hours mean time to resolution for critical issues - Zero production deployments with partner-impacting bugs ## Budget Considerations 1. Infrastructure costs - Testing environments - Monitoring tools - CI/CD pipeline enhancements 2. Team costs - New hires - Training - Tools and licenses

---

## #29 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #30 — Foreclosure handling for DSP
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

## #31 — [Lending stack] Agreement execution flow
**Status:** In progress | **Last edited:** November 12, 2025 1:01 PM

**Problem:**
are we solving?**

- Customer signing through platforms like Leegality and Digio has their own disadvantages. They don’t support clickwrap agreement making it hard for customers to sign on agreement.
- These vendors don’t provide the ideal flow which balances for regulation and cost of stamping.

---

**Solution:**
?**

---

## #32 — Repayment flow for DSP
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

## #33 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #34 — Enhancement to MFD partner Signup page
**Status:** Pending Review | **Last edited:** May 8, 2025 4:19 PM

# Enhancement to MFD partner Signup page **Product Updates** ## **1. Enhanced Partner Login Experience:** - **Feature:** Mobile Number Pre-fill & Browser Autofill Support. - **Problem:** Returning partners re-enter mobile numbers, causing friction. - **Goal:** Faster, more convenient login. - **Solution:** - **Custom Pre-fill:** Store last successfully used/OTP-requested mobile number in browser local storage for automatic pre-population. (Editable by partner). - **Browser Autofill Hint:** Add autocomplete="tel" to the mobile number field to allow browsers (like Chrome) to suggest saved phone numbers. - **Benefit:** Quicker login, reduced errors, improved partner experience. ## **2. Improved Partner Empanelment Form:** - **Feature:** Browser Autofill for Empanelment Details. - **Problem:** Manual entry of common details (name, email, city, company) is time-consuming. - **Goal:** Faster and more accurate empanelment. - **Solution:** Implement standard HTML autocomplete attributes (e.g., name, email, address-level2, organization) on relevant input fields. - **Benefit:** Quicker form completion, fewer typing errors, smoother empanelment. ## **3. Branding & Content Updates:** - **Logo Update:** Replaced Bajaj Finserv logo with DSP logo in "Our trusted partners" section. - **Partner Count Update:** Updated "2000+ Partners have joined Volt Money" to "3000+ Partners have joined Volt Money". - **Benefit:** Reflects current partnerships and growth accurately.

---

## #35 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #36 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #37 — PhonePe Contact support changes - 12th April 2024
**Status:** Not started | **Last edited:** May 6, 2024 9:14 AM

**Problem:**
are we solving?**

1. PhonePe has sent a requirement to stop lead leakage due to Volt support number available on the landing page. 
2. Number of junk inbound calls has increase 4x

---

**Solution:**
?**

---

## #38 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #39 — MFC Pledge error handling - V1 (1)
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

## #40 — Custom Comms based for Ad-hoc situations v2
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

## #41 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #42 — [DSP] Additional customer comms (compliance)
**Status:** In progress | **Last edited:** May 28, 2025 12:27 PM

**Problem:**
are we solving?**

Sending additional comms to users to comply with DLG and internal compliance requirements. 

---

**Solution:**
?**

---

## #43 — PRD – Volt MFD Payouts Process
**Status:** In progress | **Last edited:** May 27, 2025 2:52 PM

# PRD – Volt MFD Payouts Process # **PRD – Volt MFD Payouts Process** ## **1. What Problem Are We Solving?** ### **Key Issues Identified** 1. Business continuity risk as we are too dependent on one analyst for the calculations 2. **~~GST Invoice Issues:** No GST invoices sent to MFDs, leading to ad-hoc payments, accounting issues, incorrect payouts, and complaints.~~ 3. **Payout Report Clarity:** Reports are difficult to read, leading to customer support queries. 4. **Partner Accounts Payable Tracking:** Currently tracked monthly, leading to missed payouts for MFDs without added bank accounts. 5. **Payout Processing Issues:** Manually triggered payments through HSBC takes 3-4 days to get the Payment status and to retry payment if failed. 6. **Accounting Errors (~2% of partners):** Issues only discovered during tax filings (26AS). 7. **Support Visibility:** No centralized tracking for payout-related support issues. 8. **Reconciliation Issues:** Discrepancies due to outdated commercial excel files. 9. **Tracking Ad-hoc Payouts:** Older ad-hoc payouts are scattered across multiple files and emails. 10. **GSTN Verification:** No automated verification of correct GST numbers. --- ## **2. Changes needed for Payout automation (Current vs. Proposed)** | Database | Current | Proposed | | --- | --- | --- | | Application Data | DB | No change | | Transaction Data | DB | No change | | Principle Outstanding | Google Sheets | DB | | Partner Commercials | Google Sheets | DB | | Payout Ledger Table | Google Sheets | DB | | Account Payable (AP) | Not tracked | DB | | Base Payout Calculations | Google Sheets | DB | | GST & TDS Calculations | Google Sheets | DB | | Payout & GST Invoice | Google Sheets | DB | | GST Tax & TDS Filing | Google Sheets | DB | | Bank Account Data | Manual Check | DB | | Payout File to Bank | Excel | API | | Payout Payment Status | Statement | API | | Reconciliation & UTR Backfill | Google Sheets | DB | --- ## **3. User Needs** ### **MFD / Partner** - Expect accurate, on-time payments. - Need clear payout breakdowns, including GST invoices. - Require an easy way to highlight and resolve discrepancies. - Want Volt to handle tax filings accurately. - Prefer a payout experience similar to top AMCs. ### **Business Team** - Aims to improve MFD service by resolving payout issues efficiently.

---

## #44 — Migrating MFD Partners to the LSQ Accounts
**Status:** Ready for Tech | **Last edited:** May 27, 2025 2:25 PM

# Migrating MFD Partners to the LSQ Accounts [**API Integration Changes for MFD Migration to LSQ Accounts**](Migrating%20MFD%20Partners%20to%20the%20LSQ%20Accounts/API%20Integration%20Changes%20for%20MFD%20Migration%20to%20LSQ%20A%201cae8d3af13a8009aa10eac1a34936f0.md) - Accounts are now enabled for org: volt - Reading LSQ documentation to understand and create a transition plan - MFD is currently treated as lead and should be moved to accounts - RMs will be assigned accounts and will be responsible for its success - All the customer of a MFD will be under their account - **1. Purpose & Goal:** - **Current State:** Mutual Fund Distributors (MFDs) are currently managed as Leads within LeadSquared, identified by a specific Lead Type (e.g., "MFD"). This mixes partner data with end-customer data. - **Desired State:** Migrate MFD entities to the dedicated **Accounts** module for better organization, relationship management, reporting, and utilization of B2B features. This clearly separates partners from end-customer leads. - **Benefit:** Improved clarity, focused partner management workflows, ability to associate end-customer Leads under the correct MFD Account, and leverage specific Account-level features (stages, activities, ownership). **3. Procedure:** **Phase 1: Configure the Accounts Module for MFDs** Setting up the Accounts entity for MFDs - **3.1 Identify Required MFD Fields:** - Review the current Lead fields list - List *all* fields containing essential MFD information that needs to be moved to the Account record. Examples: - PAN - ARN No - Referral Code / Partner Code - Partner Referral Link - Partner Type - Platform / Platform Id - Empanelment Date - Company (if used for MFD firm name) - Key contact details (Email, Mobile Number, Address, City, State, Zip Code) - Ownership (Owner) - Any other relevant custom fields. - **3.2 Create Custom Account Fields:** - Adding all the Lead files to account - For every required MFD field *not* present by default in Accounts, create a custom field: - Navigate: My Profile -> Settings -> Accounts-> Account settings>Account type>Actions - Click **Add**. - Define: - **Display Name:** - **Schema Name:** format cf_display_name. custom field for easy reference - **Field Type:** Match - **Reference:** [https://help.leadsquared.com/account-settings/](https://help.leadsquared.com/account-settings/) - 3.3 Add Drop-downs in fields like stage, etc. **Phase 2: Migrate MFD Data from Leads to Accounts** - **3.4 Extract MFD Leads:** - Manage leads - Use **Advanced Search** Lead Type != MFD - **Manage Columns:** Add *all* source Lead fields identified in Step 3.1, **including the Lead Id (ProspectID)**. - **Export:** Select Actions -> Export Leads -> Export as CSV. - **3.5 Prepare the Import File

---

## #45 — Phase 0 LTV Tenure Update_LOS
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

## #46 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #47 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #48 — LSQ Chat workflow - Phase 1
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

## #49 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #50 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #51 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #52 — Consent Architecture FE requirements
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

## #53 — Phase 0 LTV update to 70 (servicing)
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

## #54 — Dues Comms Updation
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

## #55 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #56 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #57 — Product Note LTV update to 70
**Status:** Not started | **Last edited:** May 12, 2026 10:39 AM

# Product Note : LTV update to 70 --- # **1. Problem Statement** --- ## **2. Objective** --- ## **3. Scope** --- - LTV update task - Finflux - Multiple approved script management - Validations - Any sort of handling - Fenix - Multiple approved scripts handling - Risk and RMS validations required - Impact of all collateral transactions - Collateral addition - Collateral removal - Collateral invocation - Shortfall handling - Communications and statements - ROI auditing - Current offer visibility for NBFC and LSPs - Volt - Journey - Enhancement (Fetch/Pledge/Offer/Agreement) - Nudges - B2B2C & B2C - PF/ROI changes - Journey - Admin actions (PF increase to work out of the box) - Payout - Scope reduction - Loan offer - PF/ROI - Contract level - Volt UI --- - Nudge - Current limit - Updated Limit - Current ROI - New ROI - LTV update charges - KFS/Agreement - Task name - Service request approval - Left panel - Request details - Request ID - Service request type : Limit enhancement - Requested on - Current collateral limit - Additional collateral limit - Updated collateral limit - Limit enhancement charges - AMC charges - Substatus - Maker name - Maker remark - Maker created on - Collateral details - ISIN - Asset type - Collateral sub type - Folio - Value - Existing limit - New limit - Right panel - Client details - Loan details - With loan contract - Transactions - Collaterals - Collaterals with details (LTV) - Loan kit - KFS - Agreement - Generate offer what happens? - Request - FXLAN (with collateral details) - Response - Funds with higher LTV - Limit enhancement charge ranges - AMC charge ranges - ROI ranges - Accept offer - Request - Fund with LTV, charges & ROI details - Response - Offer ID - Service request and collateral addition in parallel, what validations to happen

---

## #58 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #59 — MFD Payout Process Revamp
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

## #60 — [IronGrid] Email trigger for ops in case of disbur
**Status:** Not started | **Last edited:** March 31, 2026 8:24 AM

**Solution:**
?

- We raise a send grid email to the ops team as soon as a disbursal is rejected due bank mis-mismatch, so that Ops is notified and they can quickly un-block the customer by contacting lender’s operation team and getting bank account updated at their end.

---

## #61 — BharatPe changes
**Status:** In progress | **Last edited:** March 28, 2024 7:26 PM

**Problem:**
are we solving?**

For our B2B partner BharatPe we are making a few changes to make the post loan application journey for the user as smooth as possible.

---

**Solution:**
?**

---

## #62 — Custom Comms based for Ad-hoc situations
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

## #63 — Lien status lifecycle tracking
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

## #64 — Withdrawal issues enhancement
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

## #66 — Credit Bureau Reporting Comms
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

## #67 — Selfie Link - MFD Prudent PRD
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

## #68 — Improving Mandate Conversions
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

## #69 — credit_bureau_reporting_comms_product_note
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - VoltMoney is a Loan Against Mutual Funds (LAMF) LSP operating on DSP Finance’s NBFC lending infrastructure. As part of its regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is manual or absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP

---

## #70 — credit_bureau_reporting_comms_product_note 325e8d3
**Status:** Not started | **Last edited:** March 16, 2026 3:38 PM

**In scope:**
- Building an automated, event-triggered communication job that fires when credit bureau reporting is completed for interest-defaulting borrowers
    - **What specific problems are we solving:**
        - Automated identification of borrowers eligible for the bureau reporting notification using the LMS mandate summary API, by filtering accounts where `totalInterestDue > 0`
        - Dispatch of a 

# credit_bureau_reporting_comms_product_note 325e8d3af13a808b82ebe94969cbc741 # credit_bureau_reporting_comms_product_note # Credit Bureau Reporting Communication — Interest Payment Default Notification --- ## **Background and Context** - .As part of regulatory obligations, DSP Finance is required to report borrowers with outstanding interest dues to credit bureaus within a defined reporting window. - **Who is facing the problem:** - **Borrowers (primary):** Customers with outstanding interest dues on their LAMF accounts are being reported to credit bureaus without receiving any prior or concurrent notification — directly impacting their credit profile without their awareness - **Compliance team (internal):** Responsible for ensuring bureau reporting obligations are met, but currently has no automated comms confirmation to demonstrate borrower notification was completed at time of reporting - **Technology / Engineering team (internal):** No existing trigger or job in place to dispatch comms at the point of bureau reporting; all communication today is absent for this event - **Data Analytics team (internal):** Generates the defaulter list and executes reporting but has no downstream comms handoff mechanism - **What is broken today:** - There is no automated communication workflow that notifies a borrower at the time their interest default is reported to a credit bureau - The current reporting cadence is 2x per month (15th and EOM); from July 1, 2026, this increases to 4x per month (9th, 16th, 23rd, EOM) — increasing the frequency of the compliance gap - The data analytics team generates the defaulted accounts list at 11:59 PM on the reporting date and completes bureau reporting within a 7-day window, but no borrower notification is triggered at the point of reporting - Manual triggering of communications is error-prone and does not scale with increased reporting frequency - **Why it is important / What is getting impacted:** - **Regulatory risk:** RBI’s Fair Practices Code and consumer protection norms require that borrowers be made aware of actions that adversely impact their credit history. Absence of notification creates a direct compliance risk for DSP Finance - **Credit impact transparency:** Borrowers who are unaware of a bureau report have no opportunity to respond, dispute, or clear dues — leading to grievances and regulator escalations - **Scale:** As reporting frequency doubles from July 2026, the gap between reporting events and borrower awareness widens significantly without an automated solution - **Brand trust:** VoltMoney’s positioning as a fair, transparent LAMF LSP depends on proactive borrower communication at critical account events --- ## **1. Problem scope** ### In

---

## #71 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #72 — Margin pledge charges
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

## #73 — Increase Credit Utilization via Whatsapp Drips
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

## #74 — Aadhaar QR scan
**Status:** Not started | **Last edited:** June 26, 2025 11:33 AM

# Aadhaar QR scan 1. Perfios Walk-through completed: SDK includes: 1. Scan QR (scanner) 2. Upload QR 3. Fetches and displays the data 4. To verify the email and phone, the customer has to enter email and phone Steps: 1. Scan QR/ Upload QR 2. Perfios de-codes the data on the QR 3. Fetches the data from UIDAI 4. Verify the email and phone Downside of SDK: Cannot be used for web-app (MFD portal) Perfios gave a walk through for the OCR KYC Plus: 1. Upload the Aadhaar 2. Scans the QR itself 3. Gives the address as the outputD 1. Bureau ID gave the following demo: 1. Upload the Aadhaar QR of the customer 2. It provides: 1. Adhaar last 4 digits 2. careOf 3. District 4. DOB 5. gender 6. location 7. landmark 8. mobile number registered? 9. email registered? 10. name of the customer 11. signature base64 12. state 13. street 14. sub district But when I gave it my black and white aadhaar and another coloured aadhaar card photo, they could not process it. They provide an API based solution thus it can be used across for web-app and mobile-app usage.

---

## #75 — 1400 160 Series Outbound Implementation
**Status:** Not started | **Last edited:** June 25, 2025 1:15 PM

# 1400/160 Series Outbound Implementation Check list: 1. Internal Approval- sent heads-up mail 2. Commercial alignment 3. Exotel-implementation - for DSP → Phone number acquisition for Volt → Outbound implementation Step 1: DLT registration We need DLT registration with Tata. Understand the automations made and how the change might affect these automations. Step 2: Confirm and Acquire the number.

---

## #76 — Chat CSAT and DSAT Capture WATI
**Status:** Not started | **Last edited:** June 24, 2025 5:00 PM

# Chat CSAT and DSAT Capture <> WATI ## 🧩 **Objective** To capture structured customer satisfaction (CSAT) and dissatisfaction (DSAT) data via a chatbot workflow that can be automatically stored, tagged, and actioned via escalation or closure, based on customer responses. --- ## 📌 **Platform** **Tool Used:** **WATI** WATI is used to automate and manage the chatbot-based feedback collection journey on WhatsApp. --- ## 🧭 **User Journey Overview** 1. Agents initiates feedback collection chatbot after service interaction. 2. Customer gives a feedback rating (1 to 3 scale). 3. Depending on the rating: - DSAT (Not Satisfied1 or 2): Capture reason and offer callback. - CSAT (Satisfied)3): Thank the customer and end. 4. Store all responses in a Google Sheet and update chat status. --- ## 🤖 ⏳Wati CSAT Automation **Flow :** --- ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image.png) Updated Flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%201.png) Old Flow: ## Customer experience in the CSAT Automation flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%202.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%203.png) **Bot Auto closing the chat and ending the chatbot flow once the chatbot flow is completed by customer:** ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%204.png) Updated Journey: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%205.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%206.png) ## 🔧 **Flow Components** ### 1. **Initiation** - **Step:** Send Message - **Message:** Hi {{name}}, Can you please share with us your valuable feedback? Instead, it should be this *Hey!, How was your experience with us today?* *A) Satisfied* *B) It was okay/Average* *C) Not Satisfied* --- ### 2. **Tagging & Storage** - **Set Tags:** Mark feedback process started (e.g., `feedback_triggered`) - **Google Spreadsheet:** Record initial engagement - This tag is used to record the agent bot initiation time and also this can be used as the tat for resolving the ticket even if the customer do not fill the feedback options --- ### 3. **Feedback Rating** - **Step:** Button Input - **Message:** Please rate us from 1 to 3 - 1 (Not Satisfied) - 2 (Satisfied) - 3 (Very Satisfied) --- ### 4. **DSAT Handling (Rating 1 or 2)** - **Step:** Button Input - **Message:** We are sorry your experience wasn't great. Could you help us improve by sharing what went wrong? - Yes, Please Call Me - Just Share Feedback - **Step:** Button Input (Detailed Issue) Can you help us understand what went wrong? - Delay in Service - Poor Support - App/Portal Issues - **Storage:** Log issue category and callback preference to Google Sheet - **Tagging:** e.g., `CSAT`, `Feedback`, or `issue_logged` --- ### 5. **CSAT Handling (Rating 3)** - **Step:** Direct conditional path - **Message: @Name,**

---

## #77 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #78 — Support Incoming Call pick-up delay
**Status:** Not started | **Last edited:** June 19, 2025 11:10 AM

# Support Incoming Call pick-up delay # Problem statement: Currently it takes 20-25 seconds from the time of the call being landed to exotel to the agent current call distribution is equally across all meembers of the group ## Goals The Goal for the project is to analysis and find the problem or the cause for delay for call pick up. ## Non-goals What is explicitly not in scope and why? # Proposed solution Proposed solution: 1. reduce the ivr duration from 4 sec to 2 sec 1. Enable the Parallel ringing option. **What are the high level architectural changes?** Diagrams can be very helpful here. **What are the high level data model changes?** These should include any database schema changes, or any changes to structured fields, e.g. an existing JSON column. **What are the main changes to the UI?** ## Risks What risks might be introduced by this set of changes? Consider running a [pre-mortem](https://www.notion.so/templates/pre-mortem-template) to raise risks. Be sure to capture mitigating these risks in the Implementation and Rollout Plans. **Are there any backwards-incompatible changes?** **Does this project have special implications for security and data privacy?** **Could this change significantly increase load on any of our backend systems?** **Does this project have any dependencies?** # Alternative solutions What alternatives did you consider? Describe the evaluation criteria for how you chose the proposed solution. # Implementation and rollout plan Fill this section out based on what is relevant for the size and scope of this project. This section can also be TBD as the project is started, but you should gradually fill this in as the project progresses towards launch. **Does this project require a migration?** If an extensive migration is necessary, write a separate tech spec for it, and link it here. Describe how to rollback in the event of an unsuccessful migration. **Is this project in an experiment or feature flagged?** Describe how to support an incremental release if needed. ## Success Criteria **How will you validate the solution is working correctly?** Describe what automated and/or manual testing you will do. Does this project need load or stress testing? This can also be a separate Testing Plan doc that is shared with QA, and linked here. **What monitoring and alerting will you do to ensure this project doesn’t decrease performance and reliability?** E.g. Increased requests, latency, and error rates.

---

## #79 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #80 — MFC Pledge (revocation & invocation)
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

## #81 — Tata Video KYC Integration V0
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

## #82 — Razorpay PG SDK integration DSP (1)
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

## #83 — Razorpay PG SDK integration DSP
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

## #84 — Repayment Lifecycle Tracking
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

## #85 — [DSP] Borrower agreement execution flow change
**Status:** Ready for Tech | **Last edited:** July 21, 2025 2:52 PM

**Problem:**
are we solving?**

Making sure the agreement execution happens in the newly aligned order

---

**Solution:**
?**

---

## #86 — Making Mobile & Email Verification Log Optional LO
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

## #87 — [Platform] BRE configurations for approval tasks
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

## #88 — Front loading the MF Fetch step in application
**Status:** Not started | **Last edited:** January 8, 2025 9:00 PM

**Problem:**
are we solving?**

Our current application conversion stand at ~14%, while the industry standard for conversion is closure to 70%. We have a lot of ground to cover in our conversion percentage. 

---

**Solution:**
?**

---

## #89 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #90 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #91 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #92 — [Volt LSP] DSP QC rejection handling
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

## #93 — B2B Platform Dashboard v1
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

## #94 — CKYC Upload for DSP
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

## #95 — [Email Template] Decoupling of Lodgement and Agree
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

## #96 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #97 — New Brainstorm
**Status:** Not started | **Last edited:** February 8, 2024 7:29 PM

# New Brainstorm <aside> 💡 **Notion Tip:** Use this template to source ideas from your team even when you're not in the same room. Articulate a question you'd like to have answered. At the same time, people can add their bulleted ideas below that question and tag themselves. Click New topic to generate a new question to answer. </aside> # [Question to answer] - First idea - Second idea - Third idea - Fourth idea # Whiteboard <aside> 💡 **Notion Tip:** Notion makes it easy to pull in brainstorming resources from other apps so you all stay focused on the same doc. For instance, you can embed mind-mapping boards from Miro and files from Figma that will update in real time. </aside> ↓ Embed examples below [https://app.notion.com](https://app.notion.com) [https://app.notion.com](https://app.notion.com) [https://app.notion.com](https://app.notion.com)

---

## #98 — New Technical Spec
**Status:** Not started | **Last edited:** February 8, 2024 7:29 PM

# New Technical Spec # Problem statement What problem are you trying to solve? If there is a PRD, this can be a sync’ed block from the PRD. Link to any other documents that are relevant for background or context. ## Goals What should be true after this project is implemented? ## Non-goals What is explicitly not in scope and why? # Proposed solution What changes are required to solve this problem and achieve the project goals? **What are the high level architectural changes?** Diagrams can be very helpful here. **What are the high level data model changes?** These should include any database schema changes, or any changes to structured fields, e.g. an existing JSON column. **What are the main changes to the UI?** ## Risks What risks might be introduced by this set of changes? Consider running a [pre-mortem](https://www.notion.so/templates/pre-mortem-template) to raise risks. Be sure to capture mitigating these risks in the Implementation and Rollout Plans. **Are there any backwards-incompatible changes?** **Does this project have special implications for security and data privacy?** **Could this change significantly increase load on any of our backend systems?** **Does this project have any dependencies?** # Alternative solutions What alternatives did you consider? Describe the evaluation criteria for how you chose the proposed solution. # Implementation and rollout plan Fill this section out based on what is relevant for the size and scope of this project. This section can also be TBD as the project is started, but you should gradually fill this in as the project progresses towards launch. **Does this project require a migration?** If an extensive migration is necessary, write a separate tech spec for it, and link it here. Describe how to rollback in the event of an unsuccessful migration. **Is this project in an experiment or feature flagged?** Describe how to support an incremental release if needed. ## Success Criteria **How will you validate the solution is working correctly?** Describe what automated and/or manual testing you will do. Does this project need load or stress testing? This can also be a separate Testing Plan doc that is shared with QA, and linked here. **What monitoring and alerting will you do to ensure this project doesn’t decrease performance and reliability?** E.g. Increased requests, latency, and error rates.

---

## #99 — [CC] Lodgement Enhancement
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

## #100 — PhonePe PG Implementation
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

## #101 — Measuring Customer Support Events and 5XX errors
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

## #102 — DSP QC Reject Handling in LSQ
**Status:** In progress | **Last edited:** February 27, 2025 7:48 PM

# DSP QC Reject Handling in LSQ # Custom Activity Configuration: DSP QC Rejection ### Problem Statement Currently, when DSP operations team rejects an applicationBased on Risk/compliance reasons, they need customer to Re attempt some step. - That increases Risk of customer application Abandonment - Customer might not see the message based communication - Sales team don’t have the List of applications in QC reject to reach out to Customer over a call and get them to complete the applications ### Success Metrics 1. **Primary Metrics** - Reduction in application abandonment rate post-QC rejection - Decrease in time to resolution for QC issues - Sales team response time to QC rejections 2. **Secondary Metrics** - Increase in first-time-right applications by understanding the Common QC reject issues ## User Personas & Journey ### 1. DSP Ops Team - Reviews loan applications - Identifies risk/compliance issues - Rejects the application on CC - Provides detailed feedback on CC ### 2. Sales Team - Receives QC rejection notifications - Contacts customers for updates - Guides application completion - Updates activity status ### 3. Customer - borrower - Receives rejection notification - Needs to update application - Requires clear guidance - Expects minimal friction ## 1. Activity Setup in LeadSquared Using LeadSquared's Custom Activities & Scores section: ### 1 Basic Configuration - Activity Display Name: DSP_QC_Rejection - Activity Code: 268 - Score: 0 - Show in Activity List: Yes - Delete Activity: Yes ### 1.1 Activity Setup in LeadSquared ```json { "ActivityEventName": "DSP_QC_Rejection", "Code": "268", "Score": 0, "ShowInActivityList": true, "CanDeleteActivity": true } ``` ![Screenshot 2025-02-21 at 4.00.31 PM.png](DSP%20QC%20Reject%20Handling%20in%20LSQ/Screenshot_2025-02-21_at_4.00.31_PM.png) ### 1.2 Custom Fields 1. **Notes Field** - Display Name: Notes - Schema Name: ActivityEvent_Note - Type: String - Purpose: Capture rejection reasons 2. **Status Field** - Display Name: Status - Schema Name: Status - Type: Dropdown - Options: - Pending Review - Customer Contacted - Update Required - Update Received - Resolved 3. **Owner Field** - Display Name: Owner - Schema Name: Owner - Type: User - Purpose: Track responsibility ### 2.1 API Call for Creating Activity ```json POST https://{host}/v2/ProspectActivity.svc/Create { "RelatedProspectId": "[LEAD_ID]", "ActivityEvent": "268", "ActivityNote": "[QC_REJECTION_NOTES]", "Fields": [ { "SchemaName": "Status", "Value": "Pending" }, { "SchemaName": "Owner", "Value": "[ASSIGNED_SALES_REP]" } ] } ``` ### 2.2 Application Logic 1. When QC team rejects application: - Create activity with rejection details - Set initial status as "Pending" - Assign to original sales owner - Return customer

---

## #103 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #104 — [Volt] Photo and Bank Deviations enhancement
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

## #105 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #106 — Shortfall communication enhancement Ignoring accou
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

## #107 — Check eligibility overhaul
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

## #108 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #109 — MFD Partner Portal Access
**Status:** Not started | **Last edited:** February 21, 2025 1:31 PM

# MFD Partner Portal Access Problem statements 1. Some MFDs forget which number they have used to create the account. 2. The MFD employees struggle to find the Portal, the number to log in, and OTP from their MFD 3. MFDs don’t set up passwords as the process to set up a password is deep in the portal. Solutions 1. We can send the Link with Phone number / Account ID and password over email to MFD 2. Generally, MFD employees too have access to the E-mail, they can search Volt money Email

---

## #110 — Pre-fetch flow Optimisation Consolidating PAN flow
**Status:** Done | **Last edited:** February 19, 2026 9:43 AM

**Problem:**
are we solving?**

Currently, users have to go through multiple sequential screens : PAN & DOB entry screen, followed by a PAN validation pop-up, and then a separate eligibility initiation screen-ie a  lengthy pre-fetch flow which is adding friction & causing user drop-offs in top of funnel.

---

**Solution:**
?**

We propose streamlining the pre-fetch flow by removing non-essential inputs for fetch like DOB and consolidating the key fields—PAN and mobile number—along with the eligibility check into a single ‘Check Eligibility’ screen. This simplification is intended to reduce friction by shortening the journey and improve fetch initiation rates

---

## #111 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #112 — Pledge error handling
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

**Solution:**
?**

---

## #113 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #114 — AA integrations - Fetch journey
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

## #115 — Centralised issue reporting process
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

## #116 — Charges only handling for collection - DSP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Volt is responsible for fetching the billing amount from the lender and managing the user’s collection experience through both the UI and communication channels.

**Solution:**
?**

---

## #117 — Comms config - OTP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and *

**Solution:**
s:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

---

## #118 — Comms config
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Comms config Customer loan renewals ```json { "LOAN_RENEWAL_REMINDER_1ST": { "eventInFiltering": { "customerChannel": [ "B2C", "B2B", "B2B2C" ], "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "loan_renewal_1st_day_of_month_v1", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "loan_renewal_1st_day_of_month_v1" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "loan_renewal_1st_day_of_month_v1" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "contactnumber" ] }, "MAIL": { "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb", "overrideTemplates": [ { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" }, { "customerPlatform": [ "PHONEPE", "PHONEPE", "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-2530f187fa8b45a4ae6b537ab36503fb" } ], "variables": [ "customername", "brand_name", "credit_limit", "loan_expiry_date", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_2ND": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "15th_day_of_loan_expiry_v1", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "15th_day_of_loan_expiry_v1" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "15th_day_of_loan_expiry_v1" }, ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "contactnumber" ] }, "MAIL": { "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "d-49e58b0e2a624431a61eb991ed2fa6de" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "loan_renewal_landing_page_link", "contactnumber" ] } }, "isActive": true }, "LOAN_RENEWAL_REMINDER_LAST_WEEK_DUE": { "eventInFiltering": { "customerChannel": [ "B2B", "B2C", "B2B2C" ], "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ] }, "eventOutFiltering": {}, "communicationMedium": [ "WHATSAPP", "MAIL" ], "triggerTime": {}, "templateConfig": { "WHATSAPP": { "templateId": "20days_to_last_day_amount_due", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Bajaj" ], "templateId": "20days_to_last_day_amount_due" }, { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP", "PHONEPE", "PHONEPE", "BHARAT_NXT", "BharatNxt1", "VOLT_API_UAT" ], "lenderPlatform": [ "Tata" ], "templateId": "20days_to_last_day_amount_due" } ], "variables": [ "customername", "brand_name", "credit_limit", "days_left", "outstanding_amount", "contactnumber" ] }, "MAIL": { "templateId": "d-78f7acdde85248798dfda7f480312e31", "overrideTemplates": [ { "customerPlatform": [ "VOLT_MOBILE_APP", "VOLT_PARTNER_ANDROID_APP", "VOLT_WEB_APP",

---

## #119 — DSP - Charges Deduction Identification Wrapper API
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

## #120 — DSP Bank Account Update and Mandate Re-Registratio
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

## #121 — Foreclosure repayment - Handle PenalInterestAccrue
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

## #122 — Interest feature handling for TCL
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

## #123 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #124 — Loan servicing - LAS VOLT
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

## #125 — MFC fetch in Volt Journey
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

## #126 — Maker checker for servicing comms
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

Our servicing communications system has critical reliability issues, resulting in both inaccurate content delivery and inconsistent communication delivery to customers. This impacts our service quality and customer experience.

**Solution:**
?**

---

## #127 — Partial lodgement handling - DSP
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

## #128 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #129 — Project Elevate - LMS
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

## #130 — Rounding of Accrued Interest before Posting bill a
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

## #131 — SYNC shortfall status with Principal & shortfall r
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

## #132 — Send partner comms to redvision MFD
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

A new communication configuration is required to handle communications for MFDs operating on B2B platforms (such as RedVision and InvestWell) separately from those on the Volt platform.

---

**Solution:**
?**

---

## #133 — Setup new and fix existing MIS for lender BFL and
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- Setup new and fix existing MIS for lender BFL and TCL

---

**Solution:**
?**

---

## #134 — Shortfall experience optimisation
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

## #135 — TCL Dynamic repayment schedule
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

## #136 — TCL foreclosure API integration
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

## #137 — Ticketing Tool Evaluation Document
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# Ticketing Tool Evaluation Document ## 1. Introduction ### Purpose of Evaluation The purpose of this document is to evaluate the ticketing tool based on various predefined criteria. The evaluation aims to determine the tool’s efficiency, usability, integration capabilities, security features, and overall challenges faced by the organisation. ### Scope and Objectives This evaluation focuses on assessing the ticketing tool’s ability to handle support tickets, automate workflows, and integrate with other systems. The objectives include: - Analyzing feature sets and usability - Evaluating system performance and reliability - Reviewing security and compliance standards - Assessing cost-effectiveness and support options DATA sharing over WA and 1:1 WA chat with MFD - PI Data and any other data ## 2. Current Challenges ## Agent Challenges/process gap | # | Challenge | Impact | Priority | | --- | --- | --- | --- | | 1 | Agents do not have visibility into a customer’s history when handling chats, calls, or emails. | Incomplete context, repetitive customer interactions | P0 | | 2 | Agents has to navigate multiple tools to gather customer details, as there is no unified **Customer 360** view. | Inefficient workflows, longer resolution times | P0 | | 3 | Agent handling MAIL support check AppSmith to verify customer registration when responding to emails. | Process fragmentation, additional steps | P2 | | 4 | Extensive manual data entry for internal tickets Like Phone, PAN, issue category etc | Time-consuming, error-prone processes | P0 | | 5 | No notifications for **JIRA** ticket updates/comments [ Automation issue] | Missed updates, lack of case transparency | P0 | | 6 | Agents working on **LSQ** lack visibility into any ongoing tickets while handling the customer or MFD. | Incomplete information, potential duplicate work | P0 | | 7 | Missing knowledge base for handling basic queries | Inconsistent responses, unnecessary escalations | P0 | | 8 | Agents not updated on product changes and features | Misinformation to customers, escalations | P0 | | 9 | Manual email ticket handling with spreadsheet tracking | Inefficient processes, risk of missed tickets, Longer TAT for CX | P0 | | 10 | No visibility into **TAT of internal ticket and resolution TAT from the 3P** | Inability to provide ETAs to customers | P0 | | 11 | No automated greeting/acknowledgment emails | Poor initial customer experience | P0 | |

---

## #138 — Volt Apps & Web Multiple Loan Handling - Launching
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

## #139 — Ticketing system for Volt
**Status:** In progress | **Last edited:** February 19, 2025 3:20 PM

# Ticketing system for Volt # **Problem Statement:** Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. Applications successful = With + without assist = Count * Cost Current Support team are facing following challenges Borrower - Long wait times for the agents to get back - Chat support - visibility - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product. - RMs and agents have to provide context in sending the client Between RMs or on Leave - We would have a data on the issues raised by a particular customer or to maintain history of support - If the support request is not OPS or Tech realted then taking followup - High Inbound Traffic :- Agents are move from call to call and saving - Lack of a single source of truth for customer issues. - Inconsistent tracking across calls, WhatsApp, and emails. - Unrecorded issues, especially from phone calls. - No SLA tracking or identification of common problems. **Key Requirements:** - **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket. - **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes. - **Workflow Needs**: - Easy ticket creation and search by phone number. - Visibility into all tickets per customer/issue. - Strong APIs and customizable workflows. - **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database. **Goals:** - Achieve 100% ticketing for all interactions. - Track and measure issue resolution times (SLAs). - Identify bottlenecks and common problems. - Prevent any customer issue from being overlooked. The Workflows that need to be enabled - Grouping of users - Page-nation for the pending and completed application The Filter for the lead stage to be added Add filters in the pending application User stories - Customer will call us - customer is routed to a agent - How is this routing setup? - Agent takes notes on the call - Dispostion

---

## #140 — Post loan Status APIs for MFD SaaS Partner Platfor
**Status:** Done | **Last edited:** February 14, 2025 12:59 PM

# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal # Product Requirements Document (PRD) [API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md) ## **Project Title:** **Development of External APIs for MFD Dashboard Integration** --- ## **1. Introduction** This document outlines the requirements for developing a set of External APIs intended for MFD platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners --- ## **2. Objective** To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base. --- ## **3. Target Audience** - **Primary Users:** - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards. - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data. - **Stakeholders:** - **Product Management Team** - **Development Team** - QA - **MFD SAAS Partners** --- ## **4. Scope** ### **In-Scope:** - Development of four External APIs: 1. **Get Active Customers** 2. **Get Shortfall Details** 3. **Get Interest Due Details** 4. **Get Renewal Details** - Documentation and specifications for each API. - Implementation of business logic within each API. - Security measures for data protection. ### **Out-of-Scope:** - Development of UI components for MFD dashboards. - Integration of common headers and authentication mechanisms (handled separately). --- ## **5. API Specifications** ### **5.1. Get Active Customers** ### **Endpoint:** ``` GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber} ``` ### **Description:** Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively. ### **Parameters:** - **Path Parameters:** - `partnerAccountId` (string, **required**): Unique identifier for the partner account. - **Query Parameters:** - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve. ### **Response Payload:** ```json { "activeCustomerDetails": [ { "mobileNumber": "+919876501234", "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "email": "dummy@voltmoney.in", "pan": "AUWPA7175L", "dob": "30-03-1988", "creditDetails": { "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "creditType": "OVERDRAFT", "lenderCreditId": "9911725722", "lenderName": "Bajaj", "totalCreditAmount": 332300, "availableCreditAmount": 282300, "principalOutStandingAmount": 50000, "currentApplicableInterestRate": 9.95, "pledgedPortfolioAmount": 738723, "overUtilizationAmount": 0, "chargesDueAmount":

---

## #141 — UPI Autopay Evaluation
**Status:** In progress | **Last edited:** February 12, 2025 6:14 PM

# UPI Autopay Evaluation # Overview UPI Autopay is a digital payment solution introduced by NPCI to enable seamless, recurring payments through Unified Payments Interface (UPI). It allows users to set up automatic debits for subscriptions, EMIs, utility bills, insurance, and other recurring expenses without manual intervention. Merchants can integrate UPI Autopay to ensure frictionless collections, improve customer retention, and reduce payment failures. Key evaluation criteria include commercials, performance metrics, ease of integration, reconciliation processes, and support availability. Comparison across providers like PhonePe and Razorpay helps determine the best solution based on reliability, cost, and performance. # PhonePe Evaluation Report [PhonePe UPI Autopay Evaluation](UPI%20Autopay%20Evaluation/PhonePe%20UPI%20Autopay%20Evaluation%20190e8d3af13a80a59b09d18401c8fd89.md) | **Criteria** | **Priority** | **Expectations** | **Comments** | | --- | --- | --- | --- | | Commercials for registration | High | | Need to confirm | | Commercials for presentation | High | | Need to confirm | | Settlement timelines | High | T+0 / T+1 | Needs confirmation | | Registration API performance | High | 95p TAT < 100ms | Not explicitly stated in docs, need benchmarks | | Pre-debit API performance | High | 95p TAT < 100ms | Needs performance validation | | Presentation API performance | High | 95p TAT < 100ms | Needs performance validation | | Ease of integration | High | Yes (2 weeks - 2 devs) | APIs are well-defined, should be achievable | | Post-integration support | High | PhonePe support required | Need clarity on support SLAs | | SDKs available | High | Java, Python | APIs are also available | | Registration modes | High | - Intent - QR - Collect | Intent and Collect supported, QR we need to convert | | Debit & Pre-debit orchestration | High | Managed by PhonePe & Merchant can also handle | APIs allow merchant to trigger debit | | Registration Error Codes | High | Not provided in documentation | Need list from PhonePe | | Pre-debit Error Codes | High | Not provided in documentation | Need list from PhonePe | | Presentation Error Codes | High | Not provided in documentation | Need list from PhonePe | | Transaction reconciliation | High | MIS reports for presentation | | | Settlement reconciliation | High | MIS reports for settlement | | | Registration reconciliation | High | MIS reports for registration | | | Mandate Expiry Handling

---

## #142 — DSP website revamp
**Status:** Not started | **Last edited:** February 12, 2025 4:29 PM

# DSP website revamp # Problems to solve 1. “Make the website a public website” 1. Make it accessible on Google and other search engines (already visible through Bing) 2. Brand impression: currently looks like a placeholder website 3. Improve “About DSP” section 1. More prominently referencing to the DSP group - Review other DSP children websites 4. Product offerings 1. Structured lending 2. LAMF - understand what’s missing 3. LAS - show coming soon? 5. Regulatory 1. Link RBI’s sachet portal 2. Prominently display name, email, contact number of grievance redressal officer on website 3. Prominently display details of COO - Principal Nodal officer on website 6. Minor fixes 1. Update address - 11th floor instead of 10th floor 2. Update CIN 3. Operating timings: customer care 4. Update partners list 5. Benefits → “RBI registered” needs to come with a disclaimer - refer to flexiloans footer 7. Logo finalisation ![image.png](DSP%20website%20revamp/image.png) # Solution space - [ ] Understand scope - [ ] Talk to priya - What is “headers” - Pankaj notes - [ ] Get feedback shared by Pankaj Thapar (policy consultant) - [ ] New website mood board - how much brand referencing is needed? | Problem | Proposed solution | | --- | --- | | 1.a | - Submit site on Google Search Console - Make sitemap.xml - Make robots.txt | | | | WEBSITE LAYOUT ### Header - Partners - Products - About ### Hero - Title - “Loans against securities” - “digital first approach” - CTA ### About Organisation stats - Money disbursed, Loans given, no. of partner tie ups - Since 160+ years ![image.png](DSP%20website%20revamp/image%201.png) ### Our products - LAMF - LAS - Structured lending ### LAMF features ### How it works ### Footer ## Additions - FAQs - About us → our team

---

## #143 — Volt LOS journey optimisations
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

## #144 — Update user details (for TCL, BFL, DSP)
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

## #145 — [Platform] Mandate presentation request optimisati
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

## #146 — one page application for Partners RMs
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

## #147 — [B2B2C] Improving lead quality in partner journey
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

## #148 — Skip Email verification
**Status:** Not started | **Last edited:** December 29, 2025 11:59 AM

**Problem:**
are we solving?**

Email verification is currently mandatory for loan application creation. However, we’re seeing around 15% **user drop-off** at this step. To reduce friction, we propose letting users **choose their preferred primary communication channel — SMS or Email** — and **skip email verification** for those who select SMS. This allows users who rely on SMS to continue without being blocked by email OTP verification.

---

**Solution:**
?**

---

## #149 — [Platform] Liveliness check
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

## #150 — Mobile email dedupe check in case on in-progress m
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

## #151 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #152 — LSQ Service Desk
**Status:** Not started | **Last edited:** December 24, 2025 11:59 AM

# LSQ Service Desk ## **1. Overview** **Objective:** Phase 1 focuses on building an LSQ-based internal Service Desk that enables structured internal ticketing, SLA management, and Jira integration. **Scope Includes:** - Jira Integration with LSQ - Internal Ticket Management (Sales, Support, Ops) - Ticket Creation & Assignment Logic - Volt Operations Team Workflow - Email Integration (Phase-ready foundation) ## [Jira Integration on LSQ Service desk](LSQ%20Service%20Desk/Jira%20Integration%20on%20LSQ%20Service%20desk%202aee8d3af13a80e8a5f7c0b8e990256a.md) [Support Requirement](LSQ%20Service%20Desk/Support%20Requirement%202aee8d3af13a80e3ae45c08bfa32a8bf.md) [Volt Ops Requirements The child ticket will be created and assigned to Volt Ops.](LSQ%20Service%20Desk/Volt%20Ops%20Requirements%20The%20child%20ticket%20will%20be%20cre%202afe8d3af13a80b9be04e4c2eb5d9880.md) # **3. Internal Ticketing Framework:** This section defines the **complete ticket lifecycle** for the LSQ Service Desk used by Support, Sales, and Operations teams. It covers how a ticket is created, assigned, triaged, escalated (Volt Ops, Product, Lender), and resolved, including SLA behaviour, parent–child ticket logic, and exception handling. # **Actively Involved** - **Customer / MFD** - **Agent (Chat / Email / Calling)** - **System (LSQ Automations & Integrations)** - **Volt Ops Team** - **Product / Tech (via Jira)** - **Lender Partners** # **Ticket Lifecycle Overview** A ticket progresses through the following high-level stages: 1. **Intake & Ticket Creation** 2. **Classification** 3. **Work / Investigation** 4. **Child Ticket Creation (Volt Ops / Product / Tech / Lender)** 5. **Resolution & Customer Validation** 6. **Closure & CSAT** 7. **Reopen, RCA** # **Detailed Step-by-Step Ticket Flow** ## **In Take & Ticket Creation** 1. **Customer initiates contact** via Chat, Call, Email 2. **System identifies the customer** - If contact exists → attach to contact. - If new → create new contact with basic details. Use cases where a ticket will be created and a ticket will not be created: | Channel | Scenario | Condition | Ticket? | Notes | | --- | --- | --- | --- | --- | | Call | Registered number call | Lead exists | YES | Auto-link ticket to lead; capture disposition. | | Call | Unregistered number call | Lead not found | YES | Capture disposiiton and Create new ticket. | | Call | Telemarketing calls | | NO | Mark as Spam | | Call | Missed call from registered number | Customer dropped | YES | New Ticket with status open with associated lead | | Call | Missed call from non registered number | Customer dropped | YES | New Ticket with status open | | Email | Any email sent to support@ | Incoming email | YES | LSQ

---

## #153 — MFD Communications for MFDs and Customers
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

## #154 — MFD channel Roadmap Q4 2024
**Status:** Not started | **Last edited:** December 23, 2024 4:13 PM

# MFD channel Roadmap Q4 2024 [Kapture CX](MFD%20channel%20Roadmap%20Q4%202024/Kapture%20CX%20165e8d3af13a8003a45be22c5308f5ea.md) Questions To ask? - For growth in MFD channel is a Lack of market? Lack of information ? lack of distribution? - what is our current per MFD application per month count - What is possible application per month count . AKA we get all the LAMF business form the the MFD - How many MFD are aware of the LAMF solution ? - How many MFD have given a LAMF before? - How many customers come to MFD for a Liquidity need ? - How many Applications are completed without assistance in the current journey - What the major hold up and issues that require manual intervention ? - What is the resolution to these issues ? - Sales based - Product based - How many applications require servicing requests ? - What are the issues ? - What is their resolution - support based - Product based - What is the performance of the sales driven Workflows /solutions ? - Sales efficiency metrics - Inbound - Outbound - What is the performance of the Product driven solutions ? - Product metrics LAMF sales - Unaware - Problem Aware - Solution Aware - Product Aware MFD channel System design Current problems - North star is AUM with check of cost number of MFDs * activity of the MFDs Acquisition Activation Retention Revenue | Acquisition | Top of the funnel | | --- | --- | | | | | Activation | | | Retention | | | Revenue | | User stories 1. MFD hears about the volt money 2. MFD registers on volt platform or tries Volt on partner platform 3. MFD creates application for the customers 4. MFD services the customers 5. MFD get the payout for the business they bring Creating applications for customers require - Volt product , if there is a issue then reach out to servicing Communications Resolutions CRM # Marketing - Not in scope in this qtr # Platfroms ## Volt Platforms - Identify Key usage patterns ( Funnels) - Identify the Key challenges in volt MFD dashboard and MFD app - Prioritise solutions Partner B2B Platforms - Maintain the Funnels provided to partners - Partner will not be able to provide us with the status on the funnels from there side , we have to build solution to catch and identify the issues

---

## #155 — Partner Payout Design
**Status:** In progress | **Last edited:** December 23, 2024 3:44 PM

# Partner Payout Design We need to update the design of the our Payout comms 1. Payout Bank account and email collection mail , 2. Payout commission statement for the month mail 3. Payout GST invoice mail 4. Commission statement invoice 5. GST invoice Redesign needs to - Align with volt design language - Have clear Information Hierarchy - Payout Bank account and GSTn collection mail 1. ### Email Subject **Optional Update: Bank Account & GST Details - Volt Money Partner** --- ### Email Body **Dear {{name}},** We hope this message finds you well. To ensure your payouts continue to be processed seamlessly, we’d like to invite you to review and update your bank account and GST details if needed. **Why Update?** Keeping your information accurate helps: - Process payouts smoothly - Ensure compliance with GST guidelines (if applicable) **How to Update:** 1. Log in to your **Partner Dashboard** [Insert Dashboard Link]. 2. Navigate to the **Account Details** section. 3. Update your **Bank Account** and/or **GST Number (GSTN)** if necessary. If your details are already accurate, you don’t need to do anything further. For your convenience, we’ve included a step-by-step guide with screenshots to assist you. **Need Assistance?** Feel free to contact your Relationship Manager (RM) or use the **Access Dashboard** link below for support. We appreciate your continued partnership with Volt Money. Warm regards, The Volt Money Team - Payout commission statement for the month mail --- ### Monthly Payout Statement Template (For Partners With GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:** Rs. {{total_income}} - **TDS Deducted:** Rs. {{tds_amount}} - **Net Payout:** Rs. {{net_payout}} Your payout has been processed and credited to the following account: **Account Number:** ****{{number}} Additionally, the GST receipt for this transaction has been sent separately to your registered email address. You can view a detailed earnings breakdown in the **Earnings** section of your dashboard. For any assistance, feel free to contact us at **+91 96117 49295**. Thank you for partnering with Volt Money. Warm regards, The Volt Money Team --- ### Monthly Payout Statement Template (For Partners Without GSTN) **Subject:** Payout Statement for {{month}} - {{name}} **Body:** Dear {{name}}, We’re pleased to share the income details for your **Volt Money Partner account** for the month of {{month}}: - **Total Income:**

---

## #156 — [Platform] Agent session management
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

## #157 — Renewal applications in the LSQ
**Status:** Not started | **Last edited:** December 17, 2024 7:16 PM

# Renewal applications in the LSQ # Customer Lead Renewal Flow ## Customer lead and opportunity creation steps for Renewal - Create renewal opportunity using lead create and update API - Save renewal opportunity id - Post opportunity update - Post activity on opportunity ## Case Scenarios ### Case 1: Customer initiating renewal through MFC Landing page - Create renewal opportunity if existing loan is near maturity - When user clicks on "Renew loan" update opportunity stage to renewal_initiated - If renewal opportunity already exists, post activity for existing opportunity ### Case 2: Customer initiating renewal through Android/iOS app When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Post "Renewal initiated" activity - Update portfolio verification status ### Case 3: Customer initiating renewal through Web App When user's existing loan is near maturity: - Create renewal opportunity if renewal opportunity doesn't exist - Post activity and update opportunity attributes if renewal opportunity exists - Update portfolio verification status - Post activity for renewal journey progress ### Case 4: System-initiated renewal notification - System identifies loans approaching maturity (30 days before) - Create renewal opportunity if eligible - Send notification to customer - Track customer response through activities ## Renewal Lead/Opportunity Attributes | Lead field name | Data type | Lead Schema name | Opportunity Schema name | Comment | Status | | --- | --- | --- | --- | --- | --- | | Original Loan ID | Text | mx_Original_Loan_Id | mx_Custom_70 | Required | sending | | Renewal Type | Dropdown | mx_Renewal_Type | mx_Custom_71 | Standard/Enhanced | sending | | Original Maturity Date | Date | mx_Original_Maturity_Date | mx_Custom_72 | Required | sending | | Portfolio Re-verification | Boolean | mx_Portfolio_Verified | mx_Custom_73 | Required | sending | | Renewal Amount | Number | mx_Renewal_Amount | mx_Custom_74 | Required | sending | | Original Loan Amount | Number | mx_Original_Loan_Amount | mx_Custom_75 | Required | sending | | Days to Maturity | Number | mx_Days_To_Maturity | mx_Custom_76 | System Calculated | sending | | Renewal Eligibility | Boolean | mx_Renewal_Eligible | mx_Custom_77 | System Calculated | sending | ## Renewal Stage Progression ### Active Stages - Renewal_Eligible - Renewal_Initiated - Portfolio_Verification - Documentation_Update - Agreement_Signing - Mandate_Setup - Renewal_Processed - Renewal_Complete ## Custom Activities for Renewal |

---

## #158 — MFD Servicing
**Status:** Not started | **Last edited:** December 17, 2024 1:46 PM

# MFD Servicing # MFD servicing We need to provide assistance to the MFDs in completing the application process on behalf of there customers and provide servicing. These issues need to be identified and to be solved for reduced effort on the MFD and Volt side. We want to provide quick resolution to any issues our MFD might be facing , Goal of the document is to describe the process and current challenges faced by us Ideal process 1. MFD communicates the issues with us using WhatsApp. 2. RM understands the issues from the Communications and raise a ticket 3. Agent then communicates the resolution and mark the tickets as resolved 4. We track the WhatsApp chat and Ticket analytics to understand and improve our servicing ## Current issues ### Communications - **Issue communication:** We use WhatsApp based tools for the MFD to communicate with us (preferred mode of communication by the MFDs). We have the two tools that we currently use - **Periskope: U**sed for providing Group chats to the MFD. - Periskope is based on Whatsapp app. It does not provide good tracking for the chats and expect us to create tickets to track issues - Pros - If MFD has a employees then they can be served by a whatsapp group better to have a one channel for updates *~ 300 groups currently with >1 MFD member.* - If MFD has a escalation then escalation can be handled on group ~ *this really has a bandwidth issues for Kapil or Bharat. We should have a separate channel for the grievance.* - If the RM is on leave and we have a group to solve then someone else can take the handover and solve the problem ~ *Currently only RM has the context on the issues of the MFD and rest of the people in group can’t takeover. The new RM has to gain context from the chat history or notes on the tickets.* - Convert WhatsApp messages into tickets or tasks - Connect with CRM systems, ticketing platforms, and other tools via APIs and web-hooks. - Cons - The platform is no longer supported by the Company - The API integration need to developed by Volt - We are not provided with most Chat level tracking like First time response, Time spend on a chat, How long the message hasn’t been responded to. - Tickets has to

---

## #159 — User engagement on the LSQ
**Status:** Not started | **Last edited:** December 12, 2024 5:55 PM

# User engagement on the LSQ Currently issues # Ticketing System Requirements & Workflow Chief Product Officer Document | December 2024 ## Executive Summary Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency. ## Current Pain Points Analysis 1. Issue Resolution Tracking - No unified system to track resolution progress - Limited visibility into resolution time frames - Inability to measure team performance effectively 2. Organizational Context - Disconnected systems leading to fragmented customer context - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos - Limited cross-functional visibility 3. Support Coverage - Backup handling inefficiencies - Lack of structured handover processes - No clear escalation matrices 4. Performance Metrics - Missing TAT (Turn Around Time) tracking at issue level - No trend analysis capabilities - Unable to identify recurring issues and root causes ## Core Requirements ### Ticket Creation & Management 1. Mandatory Ticket Creation - 100% ticket creation for all customer interactions - Channels: Phone calls, WhatsApp, Email - Required fields: Partner ID, Issue Category, Description - Clear resolution confirmation before ticket closure 2. Channel-Specific Workflows - MFD Channel specific routing rules - Direct customer support workflow - B2B partner interface requirements 3. SLA Management - Channel-specific SLA definitions - Real-time SLA tracking - Escalation workflows - Performance dashboards ### User Management & Access Control 1. Internal Users - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support) - Support Channel Team (10 agents) - Sales Team (7 members) - Ops and Tech on-call teams - Admin users 2. External Users - Direct MFDs - Platform MFDs - B2C customers - B2B platform partners ### Integration Requirements 1. Communication Systems - Exotel for call routing - RUNO for call visibility - Periskope and WATI for WhatsApp - Email integration 2. Internal Systems - Retool for DB state visibility - LSQ CRM - Slack for internal communications ## Key Features 1. Unified Dashboard - Single view of customer interactions - Real-time status tracking - SLA monitoring - Team performance metrics 2. Analytics & Reporting - Issue frequency analysis - Resolution time tracking - Team performance metrics - Channel-wise analysis - Custom report generation 3. Workflow Automation - Automatic

---

## #160 — Volt Partners - Request Demo Revamping
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

## #161 — Cashfree PG integration
**Status:** Pending Review | **Last edited:** August 5, 2025 3:56 PM

**Problem:**
are we solving?**

---

- Our current payment infrastructure depends entirely on Razorpay as the sole gateway for processing repayment transactions. This creates a critical single point of failure - if Razorpay experiences service disruptions, our entire repayment collection system becomes unavailable (users are not comfortable with VA payments), directly impacting cash flow and customer experience.
- Several of our partner LSPs are hesitant or unwilling to implement Cashfree PG integration due to various business considerations, including competitive concerns and strategic partnerships.

**Solution:**
?**

---

## #162 — PRD - Capturing UTM-Based parameters for acquisiti
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

## #163 — LSQ Requirements for UTM Attribution
**Status:** Not started | **Last edited:** August 28, 2025 11:55 AM

# LSQ Requirements for UTM Attribution ## Objective Enable LSQ (LeadSquared) to **store, track, and act upon attribution data** for each MFD by capturing both **initial UTM** and **last UTM**. Ensure every UTM update creates **activities and follow-up tasks** for better engagement tracking. ## Data Flow 1. **Event Logging** - Each time an MFD clicks on a campaign link or engages with a communication containing UTMs, the event is logged with: - MFD phone number (identifier) - UTM parameters (`campaign_id`, `utm_source`, `utm_medium`, `utm_campaign`, `utm_term`, `utm_content`) - Timestamp of event - Activity context (page visited, registration, activation milestone, etc.) 2. **MFD Matching** - The backend matches the UTM event to the MFD via phone number. - If no MFD record exists, UTM data is stored and linked upon registration. 3. **Stack Ranking of UTM Events** - UTM events are ranked by **timestamp**. - Two attribution markers are defined: - **Initial UTM** = first UTM triggered (never overwritten). - **Last UTM** = most recent UTM triggered (always updated). ## Data Storage in LSQ 1. **Custom Fields (Lead Record)** - Store **Initial UTM** and **Last UTM** parameters in dedicated custom fields (see earlier table). 2. **Activity Logging (Mandatory)** - For every **Initial UTM capture** → create an **Activity** in LSQ: - Activity Name: *“Initial UTM Recorded”* - Fields: UTM parameters, timestamp, campaign type. - For every **Last UTM update** → create an **Activity** in LSQ: - Activity Name: *“Last UTM Updated”* - Fields: UTM parameters, timestamp, campaign type. 3. **Follow-Up Task Creation (Linked to Last UTM)** - Each time a **Last UTM** is updated: - A **Follow-up Task** must be automatically created for the assigned RM/Owner. - Task Type: *“Follow-Up on Campaign Lead”* - Due Date: Based on **Last UTM Activity timestamp** (e.g., +24 hours). - Linked to the same MFD Lead. - This ensures **freshest campaign interaction → RM engagement**. 4. **Last Activity Field Update** - Each **Last UTM Activity** must also update the **system’s Last Activity Date field** in LSQ. - This allows LSQ’s native filters/reports to stay accurate. ## Rules & Logic 1. **Initial UTM** - Captured once on first campaign click. - Not overwritten. - Activity logged → *“Initial UTM Recorded”*. 2. **Last UTM** - Updated on every new campaign click. - Always overwrites previous Last UTM fields. - Activity logged → *“Last UTM Updated”*. - Follow-up Task created → *“Follow-Up on Campaign Lead”*. - Last Activity Date updated.

---

## #164 — [DSP] Dues collection comms
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

## #165 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #166 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #167 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #168 — Bank account Mandate update
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

## #169 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #170 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #171 — MNRL Compliance Validation Integration
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

## #172 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #173 — MFD - Removing google SSO from PLJ
**Status:** Ready for Tech | **Last edited:** April 22, 2025 10:53 AM

# MFD - Removing google SSO from PLJ Problem statement 1. The **Email field is not Pre-filled** even when the MFD has already fetched the MFC for the client. 2. **Email verification via Google SSO** doesn’t work well for the MFD channel—Google pulls the MFD's email from the device instead of the client’s. ![Screenshot 2025-04-11 at 1.31.35 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.35_PM.png) - MFDs often manually enter their email in the **“Continue with other email”** option, leading to operational effort to remove the Email. ![Screenshot 2025-04-11 at 1.31.44 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.44_PM.png) ## **Proposed Solution:** **After customer registration (Name + Mobile Number + OTP):** 1. The MFD lands on the **Customer Registered** screen. 2. The screen gives two options: - Learn how to **create an application** on the Partner Portal, or - **Share a link** with the customer. 3. If the MFD chooses **“Continue creating customer application”**: - The flow will continue to the next application journey step skipping the App homepage as the intended action at this step is to complete the application. - The Data like Email ID and Fetched portfolio will be Pre-filled if the MFC has been previously fetched for the customer - If the MFD needs to access the App home page then they can go back on the application process using the top ← arrow on the top left. Text changes on the verify Email step ” The provided email will be used by lenders as the Client’s registered Email for all communications “ ### Key Changes from the Current Flow 1. **Skip the email selector page** — go directly to the “Add Email” screen. 2. **Show the client’s name** clearly to ensure the email being entered is for the right person. 3. **Include a note** saying the email will be used by lenders for important updates. 4. **Update the header** to: “Add client’s email.” 5. **Streamline the journey** by removing extra steps and taking MFDs directly to the email input screen.

---

## #174 — Dynamic Contact Us WhatsApp Configuration for Supp
**Status:** Not started | **Last edited:** April 21, 2026 5:20 PM

**Problem:**
are we solving?**

---

Support contact details (WhatsApp and calling numbers) are currently hardcoded across multiple touchpoints (Website, App, Partner Dashboard, and templates).

- This results in high operational effort, as any change requires updates across multiple systems.
- There is a need to centralize these details into a dynamic configuration, enabling updates from a single place for current and future use.

**Solution:**
?**

---

- Introduce a centralized dynamic configuration for Contact Us / WhatsApp details
- Replace all hardcoded instances with config-driven variables
- Ensure all platforms (Partner’s Dashboard, Customer Website and App) fetch this value dynamically
- Create separate variables for different support numbers, as currently multiple numbers are in use :
    - Volt Customer Support WhatsApp Number [ 919611749097 ]
    - Volt Customer Support Calling Number [ 08071174410 ]
    - Partner’s Support Number WhatsApp Number [ 9611749295 ]
    - Partner’s Support Number Calling Number [ 9611749295 ]

**Note** : 

- Update the Volt Customer Support number from existing WhatsApp Number to New WhatsApp Number
    - Existing WhatsApp Number : 919611749097
    - New / Updated Number : 918105574747
- N

---

## #175 — CKYC Comms for Regulatory Compliance
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

## #176 — Unpledge and Disbursement Enhancement
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

## #177 — VA Repayment Handling [Volt LMS]
**Status:** Not started | **Last edited:** April 10, 2025 10:50 AM

**Problem:**
are we solving?**

Currently, Volt cannot create the Virtual Account (VA) repayment requests, resulting in an inability to track and post repayments made through Virtual Accounts. This creates a gap between DSP Finance's successful repayment processing and Volt's internal payment posting system, leading to potential reconciliation issues and incomplete financial records.

---

**Solution:**
?**

We will implement a webhook integration system that receives repayment notifications from DSP Finance when a customer successfully makes a repayment via their Virtual Account. The system will map the FXLAN (Fenix Loan Account Number) provided in the webhook to our internal creditId, allowing us to properly post and track these repayments in our database.

---

## #178 — PhonePe requirements
**Status:** Done | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #179 — Check eligibility overhaul
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

## #180 — Measuring Customer Support Events
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

## #181 — Template (Duplicate this for new PRDs) - PN
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #182 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #183 — Benchmarking
**Status:** Unknown | **Last edited:** Unknown

# Benchmarking [PRD-1](Benchmarking/PRD-1%20fd54aed700c545fd80cdbc5ab0a26b2f.md) [Loan against shares](Benchmarking/Loan%20against%20shares%208930cb11fa444e09a2b887b772822975.md) [Check eligibility overhaul](Benchmarking/Check%20eligibility%20overhaul%2058e0ed33415640dbb7326f1ee8460769.md) [Template (Duplicate this for new PRDs)](Benchmarking/Template%20(Duplicate%20this%20for%20new%20PRDs)%2019e76ba00e5943daae74a811c331b38a.md) [Template (Duplicate this for new PRDs) - PN](Benchmarking/Template%20(Duplicate%20this%20for%20new%20PRDs)%20-%20PN%202cbe8d3af13a80da837afb1cb5e3a856.md) [Measuring Customer Support Events](Benchmarking/Measuring%20Customer%20Support%20Events%2094ecc22b650647c6a85c75efe789c638.md) [This page will be as a database of all benchmarking done by product team](Benchmarking/This%20page%20will%20be%20as%20a%20database%20of%20all%20benchmarkin%20040f588172394cfc80f7fe000b744bac.csv)

---

## #184 — MFD comms
**Status:** Unknown | **Last edited:** Unknown

# MFD comms Drive link [https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph](https://drive.google.com/drive/folders/1W73zwn11nNNtcn97BDIi2cENdxO0qsph) 1. **6 Day MFD activation plan** – Last modified on Oct 10, 2023, by Ranjan Kumar Singh. 2. **Comms content - MFD drop off during reg...** – Last modified on Aug 29, 2023, by Kapil Nagal. 3. **Comms content - MFD Referral** – Last modified on Jul 24, 2023, by Kapil Nagal. 4. **Comms content - Welcome email to MFD** – Last modified on Mar 18, 2023, by Kapil Nagal. 5. **Mastersheet Volt Money - MFD Comms** – Last modified on Jul 24, 2023, by Kapil Nagal. 6. **partner comms status** – Last modified on May 3, 2023, by Ranjan Kumar Singh. 7. **partnerComm[Signup]** – Last modified on May 1, 2023, by Ranjan Kumar Singh. 8. **Referral activation message** – Last modified on Aug 29, 2023, by Ranjan Kumar Singh. [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) [https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1RvyX4bbbV2X8ozgnJgIczZh8lUKLtukuwHPpCMNpIxA/edit?usp=sharing) Consumer comms :- [https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing](https://docs.google.com/spreadsheets/d/14ItOA3XvQs2dHV3JI27c_T2nOG1BYzKcVeQK8ag2reo/edit?usp=sharing)

---

## #185 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #186 — Ai optimisation in current design workflow
**Status:** Unknown | **Last edited:** Unknown

# Ai optimisation in current design workflow - Prompt SO right now the design process at volt **AI is used by UX pros as a thought partner and reviewer** - Resources https://www.userinterviews.com/ai-in-ux-research-report There is around following major steps when it comes to designing - Problem identification - Prioritisation - Benchmarking - Building a user flow - Working on wireframes - Final design Methodologies for problem identification - User Interviews - Surveys - Synthesis of data - Requirements/Insights from the data Benchmarking - Exploration with competitors - Exploration of layout, components, illustrations Building user flow - User journey map - Information architecture - Technical capabilities - Information per screen and hierarchy - Scoping based on the existing designs Working on wireframes - Visual hierarchy - Communication clarity - Navigation - Need to evaluate screens based on :Navigation Ease, Information Clarity, Error Recovery Final designs - Emotional Triggers, Actionability, Consistency, - Illustration design - Interaction with motion --- ## Problem Identification ### User Research - **Automated data analysis** : Transcription, analysis, and synthesis of user research data. - **Sentiment analysis** to identify pain points from user feedback - **Pattern recognition** to spot recurring issues that humans might miss - **Natural language processing** to extract insights from unstructured user comments ### Desk Research - Scanning research papers on psychology eg. Indians’ behaviour in 2020, market trends Eg. How genZ interacts with money, etc, Understanding fintech domain Eg. Understanding how NACH and UPI Autopay works oversimplified. - Tools https://www.perplexity.ai/ https://consensus.app/ https://elicit.com/ ### Process - Designer/PM will take user interviews with the ‣ using ai to generate questionnaire based on the problem statement at hand. - Ai will help to synthesise the data analysis based on the user interview. # Current design workflow [https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/yFQeoxHiAMkkVaOHnqldcl/Ai?node-id=5-1280&t=vozojwF9gna8va8Y-11&embed-host=notion&footer=false&theme=system) # Optimized AI workflow 1. Qualitative data collection - Questionnaire for Surveys and User interviews - Desk research - Tools: Perplexity - Dashboard for CS Tickets - How to build this. ### **1. Centralize All Ticket Data** Export data from Zendesk, WhatsApp, etc. into a single table or sheet. Include fields like user message, date, channel, and status for context. --- ### **2. Analyze with AI (GPT or ML Tools)** Use GPT to extract pain points, tag themes, and identify patterns. Alternatively, use BERTopic or clustering models to detect recurring issues. --- ### **3. Summarize & Visualize Insights** Group findings by theme, volume, and sentiment in a dashboard or table. Highlight

---

## #187 — Changes in OTP component
**Status:** Developed | **Last edited:** Unknown

# Changes in OTP component Charter: LMS Pod # Context Need component for OTP when sent to both email id and phone number # Process # Figma [https://embed.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=148-936&t=ljlEPXofuXB3Tuu6-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/cE4geUqJoahVIl3AB2ChwI/Exploration-Ad-Hoc-tasks?node-id=148-936&t=ljlEPXofuXB3Tuu6-11&embed-host=notion&footer=false&theme=system)

---

## #188 — Copy Plugin
**Status:** Unknown | **Last edited:** Unknown

# Copy Plugin # ✅ Product Requirements Document: Volt Copy Assistant (Figma Plugin) ## 📌 Overview **Volt Copy Assistant** is a Figma plugin for designers and product managers working on the Volt Money app. It helps improve UX copy across product flows by offering tone-corrected, compliant, and user-friendly rewrites using Google Gemini's AI API — directly within Figma. --- ## 🎯 Core Objectives - Improve fintech UX copy with tone-aligned suggestions - Reduce copywriting guesswork for product designers - Ensure consistency with Volt's design principles (Clarity, Helpfulness, Simplicity, Transparency, Accessibility) - Save time by suggesting, editing, and replacing copy inside Figma --- ## 🧩 Plugin Actions ### 🔹 When a text layer is selected: - Show the original text in an editable input box - Let the user select a tone or context (e.g., CTA, Error, Tooltip, Instructional) - On clicking “Suggest Rewrite”, send the text + tone to Gemini API - Show AI-generated suggestion in a preview area - Allow one-click replacement of the Figma text layer with the suggestion ### 🔸 When **no text layer is selected**: - Show a clear message: “Please select a text layer to get started” - Disable suggestion and replace buttons --- ## 💡 Key Features | Feature | Description | | --- | --- | | **Text input** | Auto-populated from selected Figma text layer | | **Tone/context selector** | Dropdown to choose tone (e.g., Clear & Formal, Conversational, Empathetic) | | **Suggest button** | Triggers Gemini API call and returns rewrites | | **Preview suggestion** | Displays new copy in plugin UI | | **Replace button** | Replaces selected layer’s text with suggested rewrite | | **Fallback logic** | If Gemini fails, show “Something went wrong. Please try again.” | --- ## 🧱 UI Layout (Plugin Panel) | Section | Description | | --- | --- | | Header | “Volt Copy Assistant” with logo (optional) | | Original Text | Textarea (pre-filled from selected layer) | | Context Selector | Dropdown: Error, CTA, Tooltip, Instruction | | Suggest Button | Click to call Gemini | | Suggestion Output | Textarea showing new UX copy | | Replace Button | Click to update Figma layer | --- ## 🔌 External APIs & Data - **Gemini API (Google)** `https://generativelanguage.googleapis.com/v1beta/models/gemini-pro:generateContent` Authentication via API Key: AIzaSyANJ1RcD5FBIAzxndjvjkZdcmjWDJxl2OA - **Prompt Template (example):** `"You're a UX writer for an Indian fintech app. Rewrite the following copy in

---

## #189 — FE screen revamp
**Status:** Ready for kickoff | **Last edited:** Unknown

# FE screen revamp Charter: Design Initiatives Priority: P0 ## Tracker LMS https://docs.google.com/spreadsheets/d/1WjZgF-ThWm5-GuLZMDGNnvw5aCT7hQ6e5yxC_EDnoCo/edit?gid=0#gid=0 LOS https://docs.google.com/spreadsheets/d/1NWUmp6-7xX579K1hsehy1tmnkeXTIH_k99rS6Rzy27o/edit?gid=0#gid=0 28/01 - Transaction screen - Account + Profile - LMS home screen states: All notification components, interest due 10/01 Design link: [https://www.figma.com/design/DH8rc6N6qcZ9miF0fv3ILt/Design-system?node-id=2707-36&p=f&t=gPYwv9I0fBY9CrGl-11](https://www.figma.com/design/DH8rc6N6qcZ9miF0fv3ILt/Design-system?node-id=2707-36&p=f&t=gPYwv9I0fBY9CrGl-11) - Start working token implementation for LOS + LMS screens - Update older components - Let frontend pod execute 19/12 Pending: - Documentation and usage of tokens - Improve token naming - PRD to start Update - Token architecture finalised and implemented on Figma and sheet @Vinit Pramod Sarode How do we want to go about the re-vamp LOS revamp

---

## #190 — Frontend UI fixes [small]
**Status:** In progress | **Last edited:** Unknown

# Frontend UI fixes [small] Charter: Design Initiatives # Context While watching screen recording i have been noticing small UI frontend fixes that need to be done. List is added below with screenshots. Session recording ID and User ID # Issues ### Mobile number icon **Issue**: There is an unecessary fill on the mobile icon **Fix** remove the fill. **Account id**: 27028d22-2807-428c-9ffa-73e584decd09 **Session recording id:** https://app.amplitude.com/analytics/volt-hq/session-replay/project/473693/search/amplitude_id%3D1320386903165?sessionReplayId=34b38273-eb63-45d7-955e-25cbe0d1e8ca/1756790681555&sessionStartTime=1756790681555 ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image.png) ### Surface page color on B2B theme looks very off for many partners - Can we change the surface page to Fill primary? ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%201.png) ### Wrong logo I have seen we are using the wrong logo for DSP Finance in many of our communications. ![image.png](Frontend%20UI%20fixes%20%5Bsmall%5D/image%202.png) ### Avg time on Anchor page is - 10s ### Time take to get OTP is 8-9s for MFC fetch # Figma

---

## #191 — MFD Processes
**Status:** Unknown | **Last edited:** Unknown

# MFD Processes # Activation Process To connect with Ashik, # Application Process MFD portal flow - RMs to explain. LSQ + sales flow like Exotel. # Servicing Process Whatsapp groups process like Periskope - Sowmya, # Payout Process

---

## #192 — Events
**Status:** Unknown | **Last edited:** Unknown

# Events Below is an event strategy document for Volt Money, based on the flow and details you provided. The table format includes event name, priority, expected values, and comments on the event's current status. This document is structured to track events from user interactions to backend processes. --- ### Event Strategy Document for Volt Money Certainly! Below is a comprehensive table that outlines the various user flows, actions, corresponding event names, detailed descriptions, and the user journeys they belong to. This should help in tracking and understanding user interactions within your application. | **User Flow** | **User Action** | **Event Name** | **Description** | **User Journey** | | --- | --- | --- | --- | --- | | **Onboarding** | User views onboarding page | ONBOARDING_PAGE_VIEWED | The user has viewed the onboarding page. | Onboarding | | **Onboarding** | First time the app is loaded | LAUNCH_PAGE_VIEWED | The user has launched the app for the first time and viewed the splash screen. | Onboarding | | **Signup** | User Signup on Volt Android | SIGNUP_PAGE_VIEWED | The user has viewed the signup page on the Volt Android app. | Signup | | **Signup** | When user lands on enter OTP page from signup page | SIGNUP_OTP_PAGE_VIEWED | The user has navigated to the OTP entry page from the signup page. | Signup | | **Signup** | When user clicks on T&C, Privacy Policy on signup screen | SIGNUP_T&C_BUTTON_CLICKED | The user has clicked on the Terms & Conditions or Privacy Policy buttons on the signup screen. | Signup | | **Signup** | When user clicks on edit button on enter OTP screen | EDIT_PHONE_BUTTON_CLICKED | The user has clicked the edit button on the OTP entry screen to modify their phone number. | Signup | | **Signup** | When user clicks on resend OTP button on OTP screen, capturing resend attempts | RESEND_OTP_BUTTON_CLICKED | The user has clicked the resend OTP button on the OTP entry screen. | Signup | | **Signup** | When user enters invalid OTP | INVALID_OTP_ENTERED | The user has entered an invalid OTP during signup. | Signup | | **Signup** | When new user is created | SIGNUP_COMPLETED | The user has successfully completed the signup process and a new user account has been created. | Signup | | **Signup** | When user lands on page to select email for signup

---

## #193 — Flow charts
**Status:** Unknown | **Last edited:** Unknown

# Flow charts Certainly! Below is the visualization of the user journey map provided, represented in PlantUML diagrams. Due to the complexity and length of the entire journey, I've divided the visualization into sections corresponding to each main phase of the user journey. Each section includes the PlantUML code for the activity diagram, which you can use to generate the diagrams. --- ## **1. User Acquisition and Onboarding** ### **1.1. Launching the App and User Signup** ``` @startuml start partition "User (FE)" { :Launch App; :View Signup Page; if (Click T&C or Privacy Policy?) then (Yes) :Click T&C or Privacy Policy; :View T&C or Privacy Policy; endif :Edit Phone Number; :Navigate to OTP Page; } partition "Backend (BE)" { :Trigger OTP; } partition "User (FE)" { repeat :Enter OTP; :Submit OTP; partition "Backend (BE)" { :Verify OTP; if (OTP Valid?) then (No) :OTP Invalid; endif } if (OTP Valid?) then (No) :Display Error Message; :Resend OTP?; if (Resend OTP?) then (Yes) partition "Backend (BE)" { :Trigger OTP; } endif endif repeat while (OTP Invalid) :Complete Signup; :View Verify Email Page; if (Verify Email with Google?) then (Yes) :Verify Email with Google; else :Verify Email with Other Method; :View Enter Email Page; :Enter Email Address; endif :Email Verification Result; } partition "Backend (BE)" { :Create User Context; :Update User Email; } stop @enduml ``` --- ## **2. Eligibility and Limit Check** ### **2.1. PAN Verification and Eligibility Check** ``` @startuml start partition "User (FE)" { :Enter PAN; :Verify PAN; :PAN Verification Result; if (PAN Verification Successful?) then (Yes) :Confirm PAN Details; else :Edit PAN Details; :Resubmit PAN; endif } partition "Backend (BE)" { :Initiate PAN Verification; :Complete PAN Verification; if (PAN Verification Failed?) then (Yes) :PAN Verification Failed; endif } partition "User (FE)" { :Trigger Eligibility Check; :Eligibility Check Result; if (Eligible?) then (Yes) :Proceed to Next Step; else :Application Under Review or Rejected; stop endif } partition "Backend (BE)" { :Create Credit Application; :Receive Credit Approval Request; :LAN Generation Successful?; if (LAN Generation Failed?) then (Yes) :LAN Generation Failed; stop endif } stop @enduml ``` --- ## **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** ``` @startuml start partition "User (FE)" { :View Check Limit Page; :Edit Details if Necessary; :Update Portfolio Source; :Request MF Portfolio Details; :Choose CAMS or KFIN?; } partition "User (FE)" #LightBlue { if (CAMS Selected?) then (Yes) :Request OTP for CAMS MF Fetch;

---

## #194 — Journey Table
**Status:** Unknown | **Last edited:** Unknown

# Journey Table 1. **Phase** 2. **Sub-Phase** 3. **Action ID** 4. **User Action** 5. **Description** 6. **Platform** --- ## **1. User Acquisition and Onboarding** | Phase | Sub-Phase | Action ID | User Action | Description | Platform | | --- | --- | --- | --- | --- | --- | | User Acquisition and Onboarding | Launching the App | 1.1.1 | Launch the App | Open the Volt platform by tapping the app icon from the splash screen. | Mobile App / Web | | User Acquisition and Onboarding | User Signup | 1.2.1 | View Signup Page | Access the signup interface to create a new account. | | | User Acquisition and Onboarding | User Signup | 1.2.2 | Click T&C or Privacy Policy | Review the Terms & Conditions or Privacy Policy documents. | | | User Acquisition and Onboarding | User Signup | 1.2.3 | Edit Phone Number | Modify the phone number entered during signup. | | | User Acquisition and Onboarding | User Signup | 1.2.4 | Navigate to OTP Page | Proceed to the OTP (One-Time Password) verification step. | | | User Acquisition and Onboarding | User Signup | 1.2.5 | Resend OTP | Request a new OTP if the initial one was not received or expired. | | | User Acquisition and Onboarding | User Signup | 1.2.6 | Enter Invalid OTP | Attempt to enter an incorrect OTP for testing purposes. | | | User Acquisition and Onboarding | User Signup | 1.2.7 | Complete Signup | Finalize the signup process after successful OTP verification. | | | User Acquisition and Onboarding | User Signup | 1.2.8 | View Verify Email Page | Access the email verification interface. | | | User Acquisition and Onboarding | User Signup | 1.2.9 | Verify Email with Google | Use Google authentication to verify the email address. | | | User Acquisition and Onboarding | User Signup | 1.2.10 | Verify Email with Other Method | Utilize alternative methods for email verification. | | | User Acquisition and Onboarding | User Signup | 1.2.11 | View Enter Email Page | Input the email address for account verification. | | | User Acquisition and Onboarding | User Signup | 1.2.12 | Email Verification Result | View the outcome of the email verification process. | | --- ## **2. Eligibility and Limit

---

## #195 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #196 — LaMF application journey
**Status:** Unknown | **Last edited:** Unknown

# LaMF application journey [APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md) [API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md) [flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md) [Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md) The journey to create a loan against mf is as follows - login - user logs in using mobile number and otp validation - PAN verification - user enter DOB and PAN to validate pan , API - decentro - Fetch folio - we ping Cams/KFin to get the folio for the user - We ping them manually - we have option of gettign both from MF central - One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists - Folio have ISIN , NAV etc details - We assign the customer basis BRE to either Bajaj ot TATA capital - KYC of the customer aadhar - API is diifetent for tata and bajaj - Bank account verification - Mandate setting - Logement - KFS and docuemnttation Support I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table. [Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv) | Step | improvements | Description | Partner/Service | API Name | | | --- | --- | --- | --- | --- | --- | | Login | | User logs in using mobile number and OTP validation | | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) | | | Verify OTP | | | | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/ | | | user details | | | | https://api.staging.voltmoney.in/app/borrower/user | | | Email verification | | | Google sso | https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com | | | | | | Email / manual | | | | | | | | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) | | | | | | | | | | PAN Verification | | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API | | | Fetch Folio | | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API | | | Run BRE and Calculate Eligible Limits | | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system | | | | Assign Lender | | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system | | | | KYC Verification | | KYC of the customer with different APIs for Bajaj and TATA Capital

---

## #197 — flow
**Status:** Unknown | **Last edited:** Unknown

# flow **User Journey Map for a Loan Against Mutual Funds Application** This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer). --- ### **1. User Acquisition and Onboarding** ### **1.1. Launching the App** - **FE Snippet:** - *Splash Screen > Launch App* ### **1.2. User Signup** - **FE Snippets:** - *Signup > View Signup Page* - *Signup > Click T&C or Privacy Policy* - *Signup > Edit Phone Number* - *Signup > Navigate to OTP Page* - *Signup > Resend OTP* - *Signup > Enter Invalid OTP* - *Signup > Complete Signup* - *Signup > View Verify Email Page* - *Signup > Verify Email with Google* - *Signup > Verify Email with Other Method* - *Signup > View Enter Email Page* - *Signup > Email Verification Result* - **BE Events:** - *Backend Events > OTP > Trigger OTP* - *Backend Events > OTP > Verify OTP* - *Backend Events > User Management > Create user context* - *Backend Events > User Management > Update user email* --- ### **2. Eligibility and Limit Check** ### **2.1. PAN Verification** - **FE Snippets:** - *Cash Limit > Enter PAN* - *Cash Limit > Verify PAN* - *Cash Limit > PAN Verification* - *Cash Limit > Edit PAN Details* - *Cash Limit > Confirm PAN Details* - **BE Events:** - *PAN Verification > Initiate PAN verification* - *PAN Verification > Complete PAN verification* - *PAN Verification > PAN verification failed* ### **2.2. Eligibility Check** - **FE Snippets:** - *Cash Limit > Trigger Eligibility Check* - *Cash Limit > Eligibility Check Result* - *Cash Limit > Application Under Review* - *Cash Limit > Application Rejected* - **BE Events:** - *Credit Application > Create credit application* - *Credit Approval Request > Receive credit approval request* - *Credit Approval Request > FAS creates the request* - *Credit Approval Request > LAN generation successful* - *Credit Approval Request > LAN generation failed* --- ### **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** - **FE Snippets:** - *Cash Limit > View Check Limit Page* - *Cash Limit > Edit Details on Check Limit Sheet* - *Cash Limit > Update Portfolio Source* - *Cash

---

## #198 — Notes
**Status:** Unknown | **Last edited:** Unknown

# Notes Redivision DSP - Prakhar to test the DSP flow - OTP for the Fetch taking too much time - The Email Enter earlier was of the Workemail and was not registered - Second time the OTP took too long to Confirm

---

## #199 — LSQ Leedsquared
**Status:** Unknown | **Last edited:** Unknown

# LSQ: Leedsquared @Naman Agarwal ### **Overview** LeadSquared (LSQ) is a comprehensive Customer Relationship Management (CRM) tool primarily used by Volt Money to manage lead generation, customer interactions, and the loan application process. LSQ enables sales teams and Relationship Managers (RMs) to track customer journeys, from lead acquisition to loan approval, providing a centralized view of lead data, customer details, and application stages. --- ### **Framework: Business Impact of LSQ** ### 1. **Purpose/Objective** LSQ’s core objective is to **streamline lead management** and **enhance customer support** by providing sales teams with real-time access to lead information and loan application statuses. By organizing customer interactions and loan data in one place, LSQ improves the efficiency and transparency of the sales process, enabling better decision-making and quicker responses to customer needs. ### 2. **Key Features & Functions** | **Feature** | **Description** | | --- | --- | | **Lead Management** | LSQ tracks customer leads from acquisition to conversion, providing visibility into lead status, ownership, and data. | | **Loan Application Tracking** | Displays the current stage of loan applications (e.g., CIBIL check, KYC, approval), helping RMs manage their pipeline. | | **Customer Data Storage** | Stores critical customer details such as name, email, phone number, and loan amounts, enabling personalized outreach. | | **Sales Performance Insights** | Generates reports on lead outreach, conversion, and sales performance, helping teams optimize their strategies. | ### 3. **Business Benefits** - **Improved Lead Conversion**: LSQ helps RMs track the progress of leads efficiently, ensuring no customer falls through the cracks and allowing for timely follow-ups. - **Increased Transparency**: By providing a clear view of each lead’s stage in the loan application process, LSQ reduces ambiguity and improves decision-making. - **Enhanced Customer Support**: Real-time access to customer details and loan data allows RMs to provide more informed and tailored support during customer interactions. ### 4. **Challenges/Current Gaps** - **Lead Stage Sync Issues**: Discrepancies between the stages in LSQ and Volt Money's backend systems can lead to confusion and mismanagement of leads. - **Missing Loan Details**: Critical loan information like Processing Fees (PF), Rate of Interest (ROI), and Sanction Limits are not always available in LSQ, affecting RMs' ability to assist customers. - **Manual Data Updates**: Admin actions (e.g., changes to customer data) are not automatically reflected in LSQ, which can lead to outdated records and inefficiencies. ### 5. **Opportunities for Improvement** - Lead prioritisation - **Automating Data

---

## #200 — MFD Payout dashboard
**Status:** Unknown | **Last edited:** Unknown

# MFD Payout dashboard We have a commercial relationship with MFD , where we pay them as per the business they bring Commercials | trail income | 0.5% of AUM | | --- | --- | | account opeing | 200rs | | Selfline | Processing fees waived | | Cashback | | | Content | | | referral | | - MFD payout is calculated based on commercials agreed on with them - MFD payout is different if the MFD is registed for GST - MFD with Gst number has to be paid 18% extra as GST - we collect 5 % TDS for any payout >15000rs - we payout on 10th on month to volt MFDs - we payout on 15th to SAAS partner platform MFDs - we payout on 18 th to MFD GST payout - we clear all pending and charges till 25th - MFD may not want to share the PAYOUT amount to there employees - MFD need to see the payout status - GST issues - Payout starts at 1 of the money - Time preiod is month to month - And 10 to 15 th of month payout disbursement happen - 10 MFD get paid - 15 Platform , - 18 MFD GST payout - 25 th anything pending - Puneet compute the payout MFD , 0.5% of AUM yearly trail income/ 12 200 rs per account opening , creditline open MFD selfline - we refund the family of MFDs , RMs fill a sheet Cashback for MFD’s end customers , - we gave 10.49 % customer we have given 0.5 % cashback as we advertised on 9.99% Contest , referrals price, activated MFD referral rs 1000 Platform , :- payout Affiliate - payout - MFD - - partner - - Platform - Affilaetes - Bharat sign off, Labdhi comms - Total amount August Pain points - GST filling , we have to 18% as a TDS of the total payout of the month. - we collect 5% TDS ,

---

## #201 — Missed calls from customers aren't being called ba
**Status:** Unknown | **Last edited:** Unknown

# Missed calls from customers aren't being called back or addressed # Missed Calls and Customer Support Optimization Missed calls from customers are a significant issue, as many are not being addressed. Customers reach out to us for help during various stages, such as onboarding, opening credit lines, post-account opening support, or product inquiries. To effectively manage these requests and reduce missed calls, we need a strategy that not only addresses customer needs but also balances the cost of support channels. ## Understanding the Support Categories: We can categorize customer interactions into three key areas: 1. **Awareness**: Customers seek to understand the product better. 2. **Sales**: Customers eligible for the service but who have not yet opened an account. 3. **Support**: Customers who already have accounts and need assistance with specific issues. ## Support Channel Options: There are several ways we can provide support, each with its own cost and effectiveness: - **Online Documentation**: Free but less accessible for most users. - **Product Journey (In-App Help)**: Accessible but costly in terms of development time. - **Chat Support**: Affordable and accessible for general queries. - **Call Support**: Highly impactful but also the most expensive to maintain. ### Optimizing Customer Support: Our goal is to provide the right support channel for each category of customer, depending on their needs, to maximize effectiveness while minimizing costs. This means segmenting customers into "buckets" based on their status and needs and directing them to the appropriate support channel: | **Bucket** | **Identifier** | **Channel to Retarget** | | --- | --- | --- | | **Awareness** | No record of the number in the system, ineligible | Chat or WhatsApp | | **Sales** | Eligible number, account not yet opened | Call Support | | **Support** | Customer with an open account | Chatbot with common services | ### Proposed Changes: To reduce call support costs, we should remove the call option for ineligible customers and instead provide them with WhatsApp support. This will help to ensure that calls are only directed to customers who are further along the funnel, and likely to require higher-touch support. ### Key Objectives: - **Address customer needs** through the appropriate support channels. - **Reduce support costs** by minimizing unnecessary call support. - **Reduce missed calls and errors** by routing customers more effectively. ### Data Requirements: To implement this strategy, we need to collect and analyze the following data: -

---

## #202 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #203 — API flow for KFS and Agreement
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

## #204 — Additional details enhancement
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

## #205 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #206 — Disbursement simulation - LMS
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
- Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula.
- Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen.
- Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum a

# Disbursement simulation - LMS Last Edited: May 22, 2026 3:49 PM PRD ETA: May 5, 2026 PRD Owner: Vaibhav Arora ## Background and Context - **Who is affected** - Borrowers using Volt (DSP Finance's LSP) who initiate withdrawal requests from their Loan Against Mutual Fund (LAMF) accounts. - All LSP partners integrated with DSP Finance's disbursement infrastructure. - DSP Finance's Risk Operations team, who are exposed to collateral shortfall risk when disbursements breach the safe limit. - **What is broken today** - The current Available Limit calculation — `AL = min(DP, SL) - POS + EM` does not account for accrued interest, charges, or scenarios where non-principal exposure grows to exceed the margin held against collateral. Two specific scenarios expose DSP Finance to risk: - **Case 1 — Collateral Removal:** After a borrower repays principal and requests maximum collateral removal, the remaining collateral may only cover the Drawing Power. Any subsequent withdrawal creates a situation where accrued interest (once booked as Interest Due) pushes total exposure above collateral value. - **Case 2 — Voluntary Sell-off:** After a sell-off settles principal, the sell-off proceeds inflate Excess Money, which inflates the Available Limit. A borrower can withdraw this excess, creating a POS that, combined with accrued interest becoming due, exceeds the remaining collateral value. - Today, the Loan Detail API value is trusted by all downstream systems (Fenix, Volt, and LSP partners) as the authoritative available limit. There is no pre-disbursement validation layer that applies the updated risk-safe AL formula before funds are transferred. - **Why it matters** - Collateral shortfall represents direct credit risk for DSP Finance — in cases of default, outstanding dues cannot be fully recovered. - The gap grows over time as accrued interest compounds, making early intervention critical. - LSP partners rely on the available limit shown to borrowers; without a simulation gate, disbursements that breach exposure limits will be processed without any check. --- ## 1. Problem Scope ### In scope - Building a new Disbursement Simulation API that computes the risk-safe maximum withdrawal amount using the updated AL formula. - Updating the Volt (LSP) frontend to call the Disbursement Simulation API between the 'Enter Withdrawal Amount' screen and the 'Confirm Amount' screen. - Graceful borrower communication on Volt when the entered amount exceeds the simulation limit — showing the maximum allowed amount and enabling re-entry. - API design contract documentation to be shared with

---

## #207 — LAS CMS Confiscation and sale of securities
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

## #208 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #209 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #210 — NBFC PG Evaluation
**Status:** Unknown | **Last edited:** Unknown

# NBFC PG Evaluation Last Edited: April 8, 2025 1:06 PM PRD Owner: Surya Ganesh # Evaluation Criteria ## Business Criteria | Parameter | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | | Same day Settlements | No | No | No | No | | UPI Commercials | | | | | | Netbanking Commercials | | | | | | VISA Commercials | | | | | | Mastercard Commercials | | | | | | | | | | | ## Product Criteria | Parameter | Priority | RazorPay | PhonePe | PayU + HDFC | Easebuzz | | --- | --- | --- | --- | --- | --- | | No user login (OTP) | High | No | Available (Standard checkout flow doesn't require user login) | | | | Transaction level control on payment methods | High | | Available (Can specify payment instruments in the payment initiation request) | | | | Transaction level control on card networks | High | | Available (Can filter specific card networks in payment instruments) | | | | Customer name at transaction level | High | | | | | | Backend callback post transaction level | High | | Available (Via callbackUrl parameter in payment request) | | | | Ability to whitelist multiple URLs | High | | Available (Can configure multiple callback and redirect URLs) | | | | White-labelling of checkout | High | | Limited (PhonePe branded checkout but some customization options) | | | | Error codes and reasons at transaction level | High | | Available (Detailed error codes in status responses) | | | | Settlement webhook | Medium | | Available (Supports settlement notifications) | | | | TPV check for UPI transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for DC transactions | High | | Available (Transaction status API provides verification) | | | | TPV check for Netbanking transactions | High | | Available (Transaction status API provides verification) | | | ## Operations Criteria | Parameter | Priority | Razorpay | PhonePe | PayU + HDFC | YBL (Easebuzz) | | --- | --- | --- | --- | --- | --- | | Settlement timeline | High |

---

## #211 — PMR consumption
**Status:** Pending review | **Last edited:** Unknown

**Problem:**
are we solving?

Today, Pledge Master Reports (PMRs) are received over email at [collaterals@dspfin.com](mailto:collaterals@dspfin.com). The ops team shares these with engineering, who manually hit an API to consume the report - creating an operational bottleneck that directly impacts loan account opening timelines for the Loan Against Shares (LAS) program.

We need to eliminate this manual handoff by automating PMR ingestion the moment the email arrives, while preserving a checker workflow for validation and audit.

In a Loan Against Securities (LAS) setup, collateral positions are dynamic se

**Solution:**
?

---

## #212 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #213 — Product Note LAS Customer Consent Capture
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

## #214 — Product Note Post-Loan ROI Correction Workflow
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

## #215 — Product note Interest rate change handling
**Status:** Pending review | **Last edited:** Unknown

# Product note: Interest rate change handling Last Edited: March 19, 2026 9:51 PM PRD ETA: March 19, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** In the current co-lending construct between DSP (NBFC) and TCL (co-lender), loans are originated and managed across multiple representations within the LMS: - **Loan 90 (TCL Book):** Represents TCL’s capital contribution and is controlled externally by TCL, including interest rate decisions. - **Loan 10 (DSP Book):** Represents DSP’s capital contribution and follows DSP’s internal benchmark and pricing logic. - **Loan 100 (Customer-facing Loan):** A composite loan created in the LMS, reflecting the borrower’s obligation and used for repayment schedules, accruals, and customer communication. The effective interest rate for the borrower is derived as a **weighted average of the underlying lender rates based on capital contribution**: - 90% → TCL (Loan 90) - 10% → DSP (Loan 10) However, from a system and implementation perspective: - The LMS treats **Loan 100 as an independent loan** with its own benchmark and ROI. - Interest rates are currently configured using **benchmark + spread constructs defined at an organizational level**. - There is **no native support for dynamic weighted rate computation** across multiple lender loans within the LMS. --- ### **Problem Statement** As part of ongoing co-lending operations: 1. **Independent Rate Changes by Lenders** - TCL may revise its interest rates (benchmark or spread) independently. - DSP may also revise its own benchmark rates. - These changes directly impact the **effective blended ROI** applicable to the borrower. 2. **Lack of Native Synchronization** - Since Loan 90, Loan 10, and Loan 100 are maintained separately: - Rate changes in Loan 90 (TCL) do not automatically reflect in Loan 100. - Loan 100 must be **manually or systematically updated** to maintain parity with the blended rate. 3. **Risk of Misalignment** - If Loan 90 and Loan 100 are not updated in sync: - Incorrect borrower interest may be charged. - Accruals and repayment splits between lenders may become inconsistent. - Downstream systems (accounting, reconciliation, reporting) may break. 4. **Operational Complexity** - Current benchmark configuration is **organization-wide**, not contract-specific. - With multiple co-lending partners, each having: - Different benchmarks - Different spreads - Different rate change cycles → A single benchmark approach does not scale. --- ### **Constraints** - Loan 100 **must exist as a physical loan in the LMS** and cannot be treated as a derived construct. - LMS

---

## #216 — Product note template evaluation
**Status:** Completed | **Last edited:** Unknown

# Product note template evaluation Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora ### Lifecycle of a feature (Why product note): ```json ┌────────────────────┐ │ │ │ (initial problem, │ │ scope, context) │ └─────────┬──────────┘ │ ▼ ┌──────────────── Grooming / Kickoff ───────────────┐ │ │ │ • Align on scope │ │ • Identify edge cases │ │ • Refine requirements │ └─────────┬───────────────────────────┬─────────────┘ │ │ ▼ ▼ ┌───────────────────┐ ┌────────────────────────┐ │ Design Handoff │ │ Cross-Functional │ │ (UX, flows, │ │ Sign-offs │ │ mocks, journeys) │ │ • Finance │ └─────────┬─────────┘ │ • Compliance │ │ │ • Business Ops │ ▼ └─────────┬──────────────┘ ┌───────────────┐ │ │ │ │ │ Product Note │◄─────────────────┘ └─────────┬─────┘ ▼ ┌───────────────────┐ │ PRD │ │ (final detailed │ │ specifications) │ └─────────┬─────────┘ ▼ ┌──────────────┐ │ Engineering │ │ (breakdown, │ │ estimation, │ │ sprinting) │ └────────────── ┘ ``` ### What is a product note? A product note is a succinct, structured document that brings all stakeholders onto the same page before execution begins. Execution here is function specific: - PRDs for PMs - Low fidelity mockups and high fidelity for Design - System design documents for Engineering team - Development of core product It distils the problem, the scope, the target audience, the desired outcomes, and the key decisions into a single source of truth. Its goal is alignment ensuring everyone understands what we’re solving, why it matters, what success looks like, and what the first version will include. ### Use cases of a product note: **1. What is the problem?** - Clear articulation of the problem statement. (What are we not solving) **2. Who are we solving it for?** - Target audience definition and roll-out strategy. (GTM should be separate from defining the target audience) / Phasing can be a part of the product note however GTM may not be a product note **3. How will we know the problem is solved?** - Success criteria and measurable outcomes. **4. How are we planning to solve it?** - Scope of the solution and key components of the approach. - Entry points (User flow diagram) / Use cases **5. Why does this problem matter now?** - Prioritisation rationale and business/user impact. (Merge with what is the problem?) **6. When will we solve it and who owns what?** - Timeline, milestones, and ownership across teams. (Can be a part of solution scope) **7. How does

---

## #217 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #218 — Suspension framework
**Status:** Completed | **Last edited:** Unknown

**Problem:**
are we solving?

Currently, suspensions or blacklisting actions (triggered by screening alerts, loan irregularities, or risk assessments) are handled inconsistently across different systems and entities within the NBFC. This fragmented approach creates several critical issues:

1. **Inconsistent Enforcement**: Different systems apply suspension logic differently, leading to gaps where suspended entities can still transact through certain channels
2. **`Missing Hierarchy Propagation**: When a customer is flagged at PAN level, the suspension doesn't automatically cascade to their existing leads,

**Solution:**
?

---

## #219 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #220 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #221 — Template (PRD)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #222 — Trackwizz continuos monitoring enhancement
**Status:** Unknown | **Last edited:** Unknown

# Trackwizz continuos monitoring enhancement Last Edited: November 13, 2025 12:39 PM PRD Owner: Vaibhav Arora # Contract Changes Required for Stopping Continuous Monitoring - AS504 API ## Executive Summary Based on the AS504 API documentation, the following contract modifications are necessary to effectively discontinue continuous monitoring (Purpose 04) for customers while managing ongoing screening operations. --- ## 1. API Purpose Codes & Termination Logic ### Current Purpose Definitions - **Purpose 01**: Initial Screening with API Response and No Storage - **Purpose 03**: Initial Screening with API Response and TW Workflow - **Purpose 04**: Continuous Screening with TW Workflow ### Key Finding To stop continuous monitoring, contracts must clarify the mechanisms for Purpose 04 discontinuation, as there is no explicit "Purpose 05" for stopping monitoring in the current API specification. --- ## 2. Required Contract Amendments ### 2.1 Data Retention & Deactivation Terms **Required Changes:** ### 2.1.1 Customer Status Field Modification - **Field**: `status` (Customer Status Enum) - **Current Values**: Active, Closed, Dormant, Inactive, Suspended - **Contract Change**: Add explicit condition: `When a customer record's purpose changes from "04" (Continuous Screening) to either "01" or "03" (Initial Screening only), the system must: 1. Cease real-time continuous screening operations 2. Maintain historical screening records for audit/compliance purposes 3. Update effectiveDate to reflect when continuous monitoring ended 4. Mark continuous monitoring as "Terminated" in internal tracking` **Effective Date Requirements:** - Must be provided in "DD-MMM-YYYY" format - Should reflect the exact date when continuous monitoring ceases - Cannot be a future date (must be current or past) --- ### 2.2 Purpose Code Combination Restrictions **Contract Required Clause:** The API currently allows: - Purpose 01 & Purpose 04 (combination allowed) - Purpose 03 & Purpose 04 (combination allowed) **To Stop Continuous Monitoring**, the contract must specify: `Transition Rules for Discontinuing Continuous Monitoring: 1. If Purpose 04 is removed from a request while Purpose 01 or 03 remains: - Continuous monitoring CEASES immediately - Initial screening continues as specified - Customer record remains in TrackWizz but without ongoing monitoring 2. If ONLY Purpose 04 is passed in a new request: - Continuous monitoring CONTINUES unchanged 3. If NEITHER Purpose 01, 03, nor 04 is passed: - Request is REJECTED per validation MRV12` --- ### 2.3 Mandatory Fields for Terminating Continuous Monitoring **Contract Clause - Purpose 04 Discontinuation:** When removing Purpose 04, the following fields become mandatory: ``` FieldRequirementFormatPurposesourceSystemCustomerCodeMandatoryString (Max 100)Identifies record to stop monitoringsourceSystemNameMandatoryEnum

---

## #223 — Volt - Overdue Communication Enhancement
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

## #224 — Volt - Shortfall Communication Enhancement – Due D
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

## #225 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #226 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #227 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #228 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #229 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # Technical Design Document: Call Recording Processing System ## 1. System Overview The Call Recording Processing System is designed to ingest, store, transcribe, and analyze call recordings at scale. The system follows a microservices architecture to ensure modularity, scalability, and maintainability. ## 2. Detailed Service Architecture ### 2.1 Ingestion Service ### Components 1. **Upload Controller** - Handles HTTP uploads of call recordings - Validates input files and metadata - Initiates storage and processing workflow 2. **S3 Integration Module** - Manages direct integrations with S3 storage - Handles signed URLs for direct uploads - Processes S3 event notifications 3. **Bulk Download Manager** - Schedules and manages batch download jobs - Handles large volume transfers efficiently - Provides download job status tracking 4. **Ingestion Repository** - Stores recording metadata - Tracks ingestion status - Provides query capabilities for monitoring 5. Dedupe Manager - Checks the upload file name for the existing files names - Send callback with error “File already exist” ### Data Models ``` Recording { id: UUID externalId: String (client reference) filename: String mimeType: String fileSize: Long duration: Integer (seconds) source: String (enum: UPLOAD, BULK, S3) status: String (enum: UPLOADED, PROCESSING, COMPLETE, ERROR) storageLocation: String createdAt: Timestamp updatedAt: Timestamp metadata: JSON } ``` ### APIs 1. **Upload API** - `POST /recordings` - Multipart form upload for recording file - JSON metadata - Returns recording ID and status - Return Error is File name exists 2. **Bulk Operations API** - `POST /recordings/bulk` - Batch job creation - Configuration options (source, filters) - Returns job ID - Return Error is File name exists in batch handling allow others 3. **Status API** - `GET /recordings/{id}` - Recording metadata - Processing status - Links to associated resources ### 3.2 Storage Service ### Components 1. **Object Storage Manager** - Abstracts object storage operations - Implements retention policies - Handles object lifecycle management 2. **Database Service** - Manages PostgreSQL connections - Implements connection pooling - Provides transaction management 3. **Cache Service** - Redis-based caching - Frequently accessed metadata - Cache invalidation patterns ### Data Models ``` StorageMetadata { objectKey: String bucket: String region: String (if applicable) contentType: String contentLength: Long eTag: String createdAt: Timestamp lastAccessed: Timestamp } ``` ### APIs 1. **Object API** - `GET /storage/objects/{key}` - Object metadata - Presigned download URLs - `DELETE /storage/objects/{key}` - Mark for deletion or immediate removal 2. **Bucket Operations API** - `GET /storage/buckets/{name}/stats` - Storage statistics -

---

## #230 — Template (Duplicate this for new PRDs)
**Status:** Unknown | **Last edited:** Unknown

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #231 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #232 — BRE Phase 2++ Items
**Status:** Unknown | **Last edited:** Unknown

# BRE Phase 2++ Items ## User stories / User flow 1. Customer fetches the funds through MFC or CAMS or KFin from our end on any of the supported assets basis the funds fetched on [app.voltmoney.in](http://app.voltmoney.in) OR 2. Customer visits the Volt [website](https://voltmoney.in/check-loan-eligibility-against-mutual-funds?utm_source=nl&utm_medium=whatsapp&utm_campaign=welcome) to check the eligibility using MFC fetch and fetches the limit after entering the OTP. 3. DSP provides the limit basis the LTV configured at LSP’s end and derives the complete offer amount. 4. LSP calculates the offer amount (drawing power) into below buckets. 1. ≥25K : the BRE runs keeping DSP, BFL and TCL as lender as per the %age configured 2. 10K - 25K: LSP allocates DSP as the sole lender for now 3. <10K: LSP rejects the customer 5. LSP informs the customer on UI that its not eligible if the credit limit is <10K. This will be messaged something like ‘We regret to inform you that you aren’t eligible for a loan at this stage.’ 6. If the customer is eligible with DSP, they proceed with the offer screen (Select credit limit) on the LSP UI. 7. If the eligible lender allocated as per the BRE is BFL or TCL, the flow will continue to next step on the offer screen (Select credit limit) on the LSP UI. | **Parameter** | **Value** | **Comments** | | --- | --- | --- | | Credit limit | ≥ 25000 AND ≤2,00,00,000 | Beta: lower limit will be 25KPost Beta: we will change this to 10K | | Funds whitelisted | As per the DSP approved list | | | Channel | B2C webAndroid appiOS app | Not to be enabled on MFD, MFD platform, B2B partners. Default lender: TATA for Beta. Post beta: DSP | | Split on B2C (≥ 25K) | 10% | This number will be increased as we ramp up post beta | | Split on B2C (10K - 25K) | 100% | Ticket size : 10L. Whitelisted MFDs - phase 1. 100 loans with master checker flag on. | | Split on B2B2C | | Phase 1 - Ticket size : 10L. Whitelisted MFDs. 100 loans with master checker flag on.Phase 2 - Remove checkers for repayment and withdrawal upto 10L. QC/Ops. Whitelisted MFDs upto 50% of volumes. No age deviations. 1000 loans.Phase 3 - B2C with checkers as Phase 2. B2B2C - 100% (need to take a call

---

## #233 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled - routing to multpe RM , elimates COntext - Call duration average, conversion per RM, overall call per day - inbound patterns - rm have indirect insentive to help customer - list of issues, solution - rm motiwation, rm doesn’t know who to call - call are long, mfd says please hild while i create a case - t90 call - create dashboard for user information - transition mfd to auto serve Wati - templates and analytics - - Expired chats >24 hrs after user message

---

## #234 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #235 — LSQ Swach
**Status:** Unknown | **Last edited:** Unknown

# LSQ Swach **Title:** LSQ Opportunity Management – Solution Document **Date:** 18/07/2025 **Version:** v1.0 --- ## 🔷 Section 1: Customer Journey Solutioning ### 🔹 Objective To transition from a lead-centric to an opportunity-centric model in LSQ, enabling granular tracking across different types of customer interactions and ensuring all workflows are governed through opportunity objects. --- ### ✅ Key Requirements ### 1. Opportunity Types Configuration for Customers Set up the following distinct opportunity types in LSQ: - **Main Application (LAMF)** - **Enhancement** - **Foreclosure** - **LAS** (To be configured at a later stage) - **Renewal** Each opportunity type must be independently configurable, with distinct stages, activities, and associated automations. --- ### 2. Opportunity Attribute Support - All relevant **lead fields** (except name, email, and phone) will be replicated in the opportunity object. - A one-time schema sync between the LSQ backend and opportunity fields will be done to maintain consistency. - The Opportunity object will act as the **source of truth** for all downstream processes and reporting. --- ### 3. Lead to Opportunity Migration - All existing leads (excluding core identifiers: name, email, phone) will be migrated into new opportunities. - Migration logic will ensure backwards compatibility and data integrity. - **The migration from lead to opportunity will be interdependent, as all current flows are tightly integrated. Changes must be deployed simultaneously—partial implementation without complete migration is not feasible.** --- ### 4. Activity Management - Activities will be recorded and managed at the opportunity level, based on opportunity type. - Post-activity workflows will be executed based on opportunity state transitions. --- ### 5. Field Directionality - **One-way sync** from Opportunity → Lead for core fields (name, email, phone). - No data will flow from Lead → Opportunity to avoid overwrites. --- ### 6. Lead Automation Deprecation - Legacy lead-level automations (routing, field updates) will be **disabled**. - All process automations will now be driven by opportunity logic and configuration. --- ## 🔷 Section 2: Partner Journey Solutioning ### 🔹 Objective To establish a dedicated flow for managing the lifecycle of Partner (MFD) leads and activities using a structured, opportunity-driven model. --- ### ✅ Key Requirements ### 1. New Partner Lead Table - Introduce a **dedicated database table** for Partner (MFD) leads. - This will sync with LSQ and create a new partner lead distinct from the customer lead table. --- ### 2. New Opportunity Type: **MFD Activation** - Dedicated opportunity type

---

## #236 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #237 — Repeat B2B2C
**Status:** Unknown | **Last edited:** Unknown

# Repeat B2B2C MFD Activation Journey Field Update & Lead Schema Integration ### **Purpose:** To define and manage the set of fields that must be updated post-MFD activation journey completion and ensure these updates are shared with the lead schema for downstream processing by the Repeat team. ### **Scope:** - Capturing required data fields. - Defining when and how these fields are updated. - Updating the lead schema with the captured data. - Triggering opportunity closure upon journey completion. **The following fields need to be replicated in the lead schema:"** 1. MFD Name 2. MFD Phone Number 3. MFD Employee Name 4. MFD AUM 5. MFD ARN 6. MFD Email 7. MFD Activation Date 8. MFD Origin 9. MFD Partner Referral Link 10. MFD Customer Referral Link 11. Referred By 12. Referrer Name 13. Referrer Phone 14. Partner Account ID Additionally, include the list of customers referred so far. 1. All the customer-referred activity must be populated in the lead once activated. **In conclusion, the repeat team can work completely on the lead level, and the MFD activation team can work on the opportunity level** The activities that must be polluted in the lead fields are as follows: 1. Daily partner details update 2. Customer referred 3. Customer loan created

---

## #238 — Support Requirement
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

## #239 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #240 — LSQ BRD For MFD Activations
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

## #241 — Periskope handling
**Status:** Unknown | **Last edited:** Unknown

# Periskope handling Problem ? - we have too many tools in servicing - As we have Wati and periskope for whatsapp we want to move to one platform - we are having difficulty in managing and reviewing the service SLA. we are missing out on the parter comms and not responding in many hours , this leads to lower MFD retention Goal ? - Increase MFD engagement and retention. - Do we have to add new number to Wati, or one number would suffice ? - If One number then how the handling between agents? - if Two then how will we handle the Display on the MFD , MFD based Number on dashboard ? Current Wati number for mFD? Current agent assigned to Wati? List of 500 MFD to move ? can we add the number and chat to Wati? We will be moving from Periskope to Wati List of the MFD to move ➖ Identify the MFDs to move communicate the Change to MFD Surge planning for the WATI Periskope to Wati Transition plan - Identify the MFDs to move :- https://docs.google.com/spreadsheets/d/1ONAVTJh3wK8kxfcf9j_GvWPis71DKvNbr78d7c342Lk/edit?usp=sharing - Communicate the change to MFD - Message template Dear <name>, We are updating our support communication channel to enhance our service quality. Please note the following: Effective immediately, all support interactions will be conducted through our new channel. Please use the WhatsApp number mentioned below for any Support request. CTA—> Link to Wati Number for message - Surge planning Day 0 - Create a bulk message template - Train and prepare agents Day 1 - We move the Single and inactive MFDs. By sending the message. We will not reply to Periskope after the message (Exception - If Wati is not working ) - Wati will be Serviced by → <Agent name>. Making sure that we have a dedicated resource and they have tools needed to help MFDs - Observe the Volume , allocate the Bandwidth from Periskope to Wati → <name of the agent > - We should expect some Comms from inactive MFDs due to confusion /curiosity. - Day 2 - Review the channel from yesterday - We move rest of the Single MFDs , Barring the top ~100 - We move Inactive 2 MFDs today as well - Same process of handling the Chat support - Day 3 - We move all the MFDs apart from the Top MFDs identified Analytics

---

## #242 — Bulk Email Sender Setup Guide
**Status:** Unknown | **Last edited:** Unknown

# Bulk Email Sender Setup Guide ## Prerequisites 1. Python 3.8 or higher 2. SendGrid account with API key 3. Dynamic email template set up in SendGrid with variables: Template should use these variables: ``` Subject: Volt: GST Invoice for {{invoice_month}} - {{invoice_number}} ``` - {{current_date}} - {{partner_id}} - {{invoice_month}} - {{partner_name}} - {{file_link}} - {{submission_link}} - {{deadline_date}} - {{invoice_number}} ## Setup Steps ### 1. Environment Setup ```bash # Create a new directory mkdir email-sender cd email-sender # Create virtual environment python -m venv venv # Activate virtual environment # For Windows: venv\\Scripts\\activate # For Mac/Linux: source venv/bin/activate # Install required packages pip install pandas python-dotenv sendgrid ``` ### 2. File Structure ``` email-sender/ ├── venv/ ├── .env ├── emailsender.py ├── invoices.csv └── logs/ ``` ### 3. Environment Variables Create a `.env` file with these variables: ``` SENDGRID_API_KEY=<REDACTED> FROM_EMAIL=no-reply@voltmoney.in TEST_MODE=False CSV_PATH=invoices.csv TEMPLATE_ID=d-5a90b23aa1214f3d87f817bffb91ebd9 BATCH_SIZE=100 DELAY=1.0 MAX_RETRIES=3 ``` ### 4. Input CSV Format Create `invoices.csv` with these columns: ``` email_ID,invoice_date,partner_id,invoice_month,partner_name,file_link,Pre-filled Form URL,invoice_number example@company.com,2024-03-01,PART001,March 2024,John Doe,<https://link-to-file>,<https://form-link>,INV-2024-001 ``` ## Running the Script 1. **Test Mode First** ```bash # Keep TEST_MODE=True in .env python emailsender.py ``` Check logs folder for email_log_[timestamp].csv 2. **Live Mode** ```bash # Change TEST_MODE=False in .env python emailsender.py ``` ## Output & Logs - Script creates a `logs` folder - Each run generates a CSV file: `email_log_YYYYMMDD_HHMMSS.csv` - Log contains: - Timestamp - Email status (SUCCESS/FAILED) - Retry attempts - Error messages if any - All email details ## Troubleshooting 1. **Common Issues** - "Missing required environment variables": Check .env file - "API key invalid": Verify SendGrid API key - "Template not found": Check template_id in .env 2. **SendGrid Template** - Ensure all variables are properly defined - Test template in SendGrid dashboard first 3. **CSV Issues** - Check CSV encoding (should be UTF-8) - Verify all required columns are present - No empty rows/cells in required fields ## Best Practices 1. **Before Sending** - Run in TEST_MODE first - Verify template with test data - Check log file format 2. **Production Use** - Start with small batches - Monitor logs actively - Keep DELAY=1.0 to avoid rate limits ## Support For issues: - Check SendGrid logs for delivery status - Review email_log CSV for error messages - Ensure all template variables match CSV data ## Security Notes - Keep .env file secure - Don't commit .env to version control - Use verified sender emails only

---

## #243 — Build vs Buy
**Status:** Unknown | **Last edited:** Unknown

# Build vs Buy # Vendor Analysis & Development Requirements ## Partner Capabilities Matrix | Capability | Zoho | RazorpayX | Clear (Cleartax) | Tally | Custom Build | | --- | --- | --- | --- | --- | --- | | **GST Invoice Generation** | ✅ Built-in | ❌ Basic | ✅ Specialized | ✅ Standard | ✅ Custom | | **Bulk Operations** | ⚠️ Limited | ✅ Excellent | ⚠️ Limited | ❌ Basic | ✅ Custom | | **Bank Integration** | ⚠️ Basic | ✅ Excellent | ❌ None | ⚠️ Limited | ⚠️ Via APIs | | **Email Automation** | ✅ Good | ✅ Good | ⚠️ Basic | ❌ None | ✅ Custom | | **Issue Tracking** | ⚠️ Basic | ❌ None | ❌ None | ❌ None | ✅ Custom | | **Reconciliation** | ✅ Good | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Custom | | **API Flexibility** | ⚠️ Limited | ✅ Excellent | ✅ Good | ❌ Poor | ✅ Full | | **Ledger Management** | ✅ Excellent | ⚠️ Basic | ✅ Good | ✅ Excellent | ✅ Custom | ## Unique Strengths ### Zoho: - better for very large teams - Complete accounting suite - GST-compliant invoicing - Built-in approval workflows - Integrated email systems - Cost: ₹3-5K/month ### RazorpayX - If want to handle transactions - Excellent banking integration - Real-time reconciliation - Bulk payment processing - Strong API documentation - Cost: 0.25-0.5% per transaction ### Clear (Cleartax) - We are not TG, more for CA in a large company - GST expertise - Compliance focused - Good for tax filing - API-first approach - Cost: ₹20-30K/month ### Tally - for Ledger management - Strong accounting - Traditional ledger system - Good for accountants - Limited automation - Cost: One-time ₹18K ## Development Plan & Costs ### Phase 1: Core Infrastructure ``` 1. Email System & Google Forms Integration (<1 week) - Custom email templates - Response tracking - Form automation Cost: 2-4 hrs per month 2. GST Invoice System (2 day ) - Template creation - Bulk generation - Approval - Storage & retrieval Cost: 4-8 hrs per month 3. Basic Issue Tracking (1 day) - Excel based for now - High operational cost - Ticket system - excel - Status tracking - excel - Resolution workflow - Docs/notion Cost: 6-10 hrs

---

## #244 — Cost estimates
**Status:** Unknown | **Last edited:** Unknown

# Cost estimates # AWS Infrastructure Cost Projections (2024-2026) ## Constants & Assumptions | Parameter | Value | Notes | | --- | --- | --- | | Growth Rate | 2x yearly | Partner base doubles each year | | Storage per Partner | 3.1 MB/month | - GST Invoice (0.5MB)<br>- Payout Statement (0.5MB)<br>- Bank & GST Docs (2MB)<br>- Form Responses (0.1MB) | | Retention Period | 84 months | 7 years for regulatory compliance | | Emails per Partner | 3/month | Registration, payout, GST notifications | | API Calls per Partner | 20/month | Includes all interactions | | Lambda Executions per Partner | 10/month | All automated processes | ## Growth & Cost Projections | Metric | Year 1 (2024) | Year 2 (2025) | Year 3 (2026) | | --- | --- | --- | --- | | Active Partners | 2,500 | 5,000 | 10,000 | | Monthly Data Volume | 7.75 GB | 15.5 GB | 31 GB | | Cumulative Storage | 93 GB | 279 GB | 558 GB | | Monthly Emails | 7,500 | 15,000 | 30,000 | | Monthly API Calls | 50,000 | 100,000 | 200,000 | ## Monthly Cost Breakdown (USD) | Service | Year 1 | Year 2 | Year 3 | Scaling Factor | | --- | --- | --- | --- | --- | | S3 Storage | $2.14 | $6.42 | $12.83 | Linear + Accumulation | | RDS | $45 | $65 | $110 | Step Function* | | Lambda | $3 | $6 | $12 | Linear | | SES (Email) | $0.75 | $1.50 | $3 | Linear | | API Gateway | $5 | $10 | $20 | Linear | | CloudWatch | $15 | $25 | $45 | Step Function* | | Route 53 | $0.50 | $0.50 | $0.50 | Fixed | | Step Functions | $2 | $4 | $8 | Linear | | **Total Monthly** | **$73.39** | **$118.42** | **$211.33** | | | **Total Annual** | **$880.68** | **$1,421.04** | **$2,535.96** | |

---

## #245 — Detailed JTBD
**Status:** Unknown | **Last edited:** Unknown

# Detailed JTBD ## MFD Partner Jobs ### Primary Jobs - Get paid correctly for business brought - Mentioned agreed commercials - Access payout statements easily - Need to search Emails - - Generate GST compliant invoices - Track payment status - Raise and resolve discrepancies ### Secondary Jobs - Update bank account & GSTN details - View historical payments - Download invoice copies - Verify commission calculations - Get tax documents for filing ## Finance Team Jobs ### Invoice Processing - Generate accurate commission statements - Calculate GST correctly - Verify bank details before payment - Track invoice approvals - Process bulk payments efficiently ### Compliance & Reporting - Maintain GST compliance - Generate MIS reports - Track tax deductions - Maintain audit trail - Reconcile payments ## Operations Team Jobs ### Partner Management - Verify partner details - Handle bank account updates - Validate GSTN numbers - Track partner documentation - Manage partner queries ### Process Management - Monitor invoice status - Track issue resolution - Handle exceptional cases - Maintain partner communications - Update partner records ## Technology Team Jobs ### System Management - Generate bulk invoices - Store documents securely - Handle email notifications - Track system performance - Manage data backups ### Integration Jobs - Connect with payment systems - Integrate GST verification - Link with accounting software - Enable bank verification - Connect analytics data ## Analytics Team Jobs ### Data Management - Calculate correct payouts - Verify commission rules - Track payment accuracy - Generate performance reports - Identify payment patterns ### Quality Assurance - Validate calculations - Check for anomalies - Monitor error rates - Track resolution times - Report on SLAs ## Critical Success Metrics ### Performance Metrics - Invoice generation time < 1 day - Payment processing time < 3 days - Issue resolution time < 2 days - System uptime > 99.9% - Error rate < 0.1% ### Business Metrics - Support ticket reduction > 50% - Partner satisfaction > 90% - Processing cost reduction > 30% - Compliance rate = 100% - Auto-resolution rate > 80% ## Dependencies & Constraints ### External - GST verification service - Bank verification system - Partner response time - Regulatory requirements - Payment gateway availability ### Internal - Data accuracy - System availability - Team bandwidth - Process compliance - Budget constraints Where are all the commercials agreements stored ?

---

## #246 — payout Email
**Status:** Unknown | **Last edited:** Unknown

# payout Email ### Bank account and GSTN *Subject:* Action Required: Confirm Your Bank Account Details and GSTN *Dear <Partner's Name>,* We hope this message finds you well. To ensure timely and accurate processing of your commission payments, we kindly request you to Confirm/Update your bank account details and GSTN (If applicable) in the link below. [Pre-filled Google Form Link] Best regards, Volt Team ## Commission Payout with GST Invoice *Subject:* Your Monthly Commission Statement and GST Invoice for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement and GST invoice attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt *Subject:* Your Monthly Commission Statement for <month> *Dear <Partner Name>,* We are pleased to inform you that your commission for [Month, Year] has been calculated. Please find the statement attached below To confirm receipt and upload the signed invoice or report any issues, please use the following link: [Pre-filled Google Form Link] Thank you for your trust and we sincerely appreciate our ongoing partnership. To onboard more customers visit <Partner platform> Best regards, Team volt

---

## #247 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #248 — Payouts Phase 2
**Status:** Unknown | **Last edited:** Unknown

# Payouts Phase 2 Issues 1. 1. **Uncertain Base Transaction Data:** Due to challenges in maintaining updated transaction tables with lender APIs, the ETA for receiving accurate base transaction data is unpredictable, often delaying payouts. This process needs to be initiated at the beginning of each month. 2. 2. **Commercials in Credit Application:** The Analytics team has noted difficulties due to the absence of commercials as a parameter in credit applications. Currently commercials for Platforms and Base are hardcoded 3. 3. **GST Invoice Generation:** There is no structured process for GST invoice creation, causing partners to send ad hoc invoices, which are frequently inaccurate, leading to approval delays. 4. 4. **Unmapped Transactions:** Approximately 20k transactions lack a mapped recipient, creating further reconciliation challenges. 5. 5. **Lack of Accessible MFD Account Balance Data:** We do not have comprehensive account balance data, affecting accurate calculations. We need to provide better Partner level account visibility to the Support team and platforms. 6. 6. **HSBC Reconciliation Process:** The current reconciliation process with HSBC could be improved due to unrelated transactions in the account. 7. 7. **Dedicated Support for Payout Issues:** There is no dedicated team member or specific contact for payout-related queries or a dedicated email portal for these issues. 8. 8. **Ad-hoc payments:** There were ad-hoc payments based on partner requests without the required details to be reckoned. 9. 9. **Communication challenges:** In past we have shared Comms with wrong Details to the Partners raising a lot of tickets and Current commission statement could be better.Proposed Phase 1 Solution: GST Invoicing Process Tasks identified - Document the current table creation process end to end - Review and identify bugs and callout limitations - Parter commercials to be moved to a config instead of the a hardcoded values - Resolve 20k Unmapped trasctions - get a more accurate count - find and resolve the audit challanges - Build DB for the balance amounts - HSBC API integration - Dedication individual for Payouts - with accounts and Data background - Build communication Scripts inhouse and have the team Other challanges - - Currently all the process after tables is on Puneets personal laptop and is very risky. we don’t have any backup - We need to move to just supporting the Email channel for payouts and payouts related query. We will depo the MFD dashboard. - we need a dedicated person for payouts as the

---

## #249 — Process note Payouts
**Status:** Unknown | **Last edited:** Unknown

# Process note Payouts Problems ### Data 1. Due to lack of proper APIs From lenders we don’t have upto date transactions table, Transaction table get updated on the startup of the month buy running Jobs ### Calculations 1. Commercials are a Excel file and every time we calculate the Commercials are applied backwards to the credit applications. This breaks and we need to add the commercials params to the Credit application during application creation so that commercials become the property of the application and we don’t rely on the Commercials table ### Payout Processing 1. No process for GST invoice calculation and Generation ### Transaction tracking 1. We have 20k transactions without proper assignment of the recipient and the reason of the payment. 2. We have one bank account for multiple different use cases, complicating the Payout recon. 3. we need to integrate with HSBC to have faster transaction status 4. We don’t store the Data in Audit DB 5. We don’t have balance for MFDs complicating the calculation more then the month ### Reporting 1. Commissions payout file could be a better template 2. Our File to see the a particular MFD account was a excel file and is no longer functional due to capacity issues and need to moved to DB 3. We have manual process for platform payout reporting ### Comms /support 1. We need a dedicated Email id for the payout related tasks 2. There is no dedicated resource for the payout related issues 3. Comms should be correct and need better approval process - Data - Tech - Transactions table - Business - Partner Commercials data - Partner bank account list - Partner GSTN list - Analytics - Team to process data to provide Reconciled Payout data - Calculate the Base Payouts and accounts payable on a Partner level - Calculate the GST and TDS payout calculations - Get approvals and Resolve queries - Prepare Invoices after approval and Files for communication - Approval - Business to provide approval on the Base payouts, TDS , GSTN - communication - After Approval Analytics team will share Comms File with Partner ID , emails and Payout values and Invoices - There 3 possible email - Scheduled Emails - Add/update your bank account and GSTN - Payout commission comms - GSTN Invoice Comms - Ad-hoc emails/ comms to resolve the partner issues - Payment - Payment file

---

## #250 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #251 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #252 — Query for MFD tiering
**Status:** Unknown | **Last edited:** Unknown

# Query for MFD tiering: WITH partnet_cte AS ( SELECT vdl_audit_partneraccounts.accountid AS partner_account_id, max(NULLIF(partnername,'nan')) as partner_name, MAX(NULLIF(accountholderphonenumber,'nan')) AS partner_phone_number, MAX( COALESCE(NULLIF(accountholderphonenumber, 'nan'),NULLIF(pa_sub.pa_alt_phonenumber, 'nan'))) AS partner_phone_number, max(case when address = 'nan' then null else json_extract_scalar(REPLACE(address, '''', '"'), '$.city') end) as partner_city, MAX(partnercode) AS partnercode, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') END) AS partner_arn, MAX(CASE WHEN partnerprofiledetails IS NOT NULL THEN json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') END) AS companyName, MAX(NULLIF(accountholderemail,'nan')) AS partner_email, MIN(CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END) + INTERVAL '330' MINUTE AS registered_date, MIN( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) as TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END )+ INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" left join (select accountid,coalesce(accountholderphonenumber,json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) as pa_alt_phonenumber from "volt-data-lake"."vdl_partneraccounts") pa_sub on pa_sub.accountid = vdl_audit_partneraccounts.accountid GROUP BY vdl_audit_partneraccounts.accountid UNION - - PART 2: From Partner Table not present in Audit SELECT partner.accountid AS partner_account_id, NULLIF(partnername, 'nan') AS partner_name, COALESCE(NULLIF(accountholderphonenumber, 'nan'), json_extract_scalar(partnerprofiledetails, '$.partnerAlternateMobileNumber')) AS partner_phone_number, json_extract_scalar(REPLACE(address, '''', '"'), '$.city') as partner_city, partnercode, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.arnNo') AS partner_arn, json_extract_scalar(REPLACE(partnerprofiledetails, '''', '"'), '$.companyName') AS companyName, NULLIF(accountholderemail, 'nan') AS partner_email, ( CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END ) + INTERVAL '330' MINUTE AS registered_date, ( CASE WHEN accountholderemail IS NOT NULL THEN CASE WHEN lastupdatedtimestamp LIKE '%Z' THEN cast(from_iso8601_timestamp(lastupdatedtimestamp) AS TIMESTAMP) ELSE CAST(lastupdatedtimestamp AS TIMESTAMP) END END ) + INTERVAL '330' MINUTE AS emplanelement_date FROM "volt-data-lake"."vdl_partneraccounts" partner LEFT JOIN ( SELECT DISTINCT accountid FROM "volt-audit-data-lake"."vdl_audit_partneraccounts" ) audit_check ON partner.accountid = audit_check.accountid WHERE audit_check.accountid IS NULL ), customer_cte AS ( select partner_account_id,date(first_created_on) as partner_active_date_application_first_created_on,partner_partially_active_date,partner_active_date,dhanda_activity_date from ( SELECT partner_account_id, first_created_on, MIN(date(first_created_on)) OVER (PARTITION BY partner_account_id) AS partner_partially_active_date, MIN(date(completed_on)) OVER (PARTITION BY partner_account_id) AS partner_active_date, MAX(date(completed_on)) OVER (PARTITION BY partner_account_id) AS dhanda_activity_date, ROW_NUMBER() OVER (PARTITION BY partner_account_id ORDER BY completed_on ASC) AS rn FROM "volt-analytics"."primary_application_full_info" -- WHERE partner_account_id = '072f9922-abe0-4c79-9883-1b26044767b8' ) sub where rn=1 ), partner_customer_detail_cte as ( select count(distinct application_id) as total_no_of_completed_applications,sum(app_pledged_credit_limit) as toal_pledged_credit_limit,partner_account_id,max(business_channel) as business_channel ,max(operating_channel) as operating_channel,max(platform_name) as platform_name from "volt-analytics"."primary_application_full_info" where current_step_id='COMPLETED' group by partner_account_id ), final_cte as ( select p.*, c.partner_active_date_application_first_created_on, c.partner_partially_active_date, c.partner_active_date, c.dhanda_activity_date, pc.total_no_of_completed_applications, pc.toal_pledged_credit_limit, pc.business_channel, pc.operating_channel, pc.platform_name from partnet_cte p left join customer_cte c on p.partner_account_id=c.partner_account_id left join partner_customer_detail_cte pc on p.partner_account_id=pc.partner_account_id ), volt_cte as ( select *,CASE WHEN percentile_completed_cases <= 0.10 -- and percentile_pledged_limit <= 0.10 THEN 'Super Gold' WHEN percentile_completed_cases > 0.10 and percentile_completed_cases <=

---

## #253 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #254 — Analytics Requirement Name verification (TCL)
**Status:** Unknown | **Last edited:** Unknown

# Analytics Requirement: Name verification (TCL) Query 1: (errors consolidation, distributed by providor) Total applications initiated (unique) Total Query 2: (Success rate 7 day window distributed by providor) ```jsx select *,total_attempts/unique_attempts as number_of_attempts_per_user, (successful_attempts*100)/unique_attempts AS success_rate_perc from (select 'Digio' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when umrn is not null then application_id else null end)) as successful_attempts from (select application_id, bank_account_number, created_date_time, bank_ifsc_code, umrn, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') AS npci_auth_failed_error, JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') AS npci_auth_reject_reason, CASE WHEN umrn IS NOT NULL THEN 'COMPLETED' WHEN ( JSON_EXTRACT(digio_mandate_response, '$.npci_auth_failed_error') IS NOT NULL OR JSON_EXTRACT(digio_mandate_response, '$.npci_auth_reject_reason') IS NOT NULL ) THEN 'FAILED' ELSE 'INVALID_REQUEST' END AS status_mandate from "credit_applications_data_audit_digio_mandate_sign" WHERE date(created_date_time) > date_add('day', -6, current_date) ) t group by date(created_date_time) UNION ALL select 'Tata' as mandate_platform ,date(created_date_time) as date,count(application_id) as total_attempts, count(distinct(application_id)) as unique_attempts, count(distinct(case when status='Completed' then application_id else null end)) as successful_attempts from (select application_id, created_date_time, bank_account_number, bank_ifsc_code, case when mandate_status='Finished' then 'Completed' else 'Failed' end as status, JSON_EXTRACT(tata_mandate_data, '$.emandate_error_message') AS emandate_error_message, JSON_EXTRACT(tata_mandate_data, '$.emandate_status') AS emandate_status from "credit_applications_data_audit_tata_mandate" where date(created_date_time) > date_add('day', -6, current_date) and mandate_status!='In Progress' ) t2 group by date(created_date_time) order by 2) ramesh ``` Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #255 — API Integration Changes for MFD Migration to LSQ A
**Status:** Unknown | **Last edited:** Unknown

# API Integration Changes for MFD Migration to LSQ Accounts **Document: API Integration Changes for MFD Migration to LeadSquared Accounts** ## **1. Introduction & Goal** This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module. The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner. ## **2. Current API Usage Summary (Pre-Migration)** - **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD). - **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record. - **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*. - **Activity Logging:** - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*. - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*. ## **3. Required API Changes (Post-Migration)** The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked. **3.1 MFD Creation** - **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API. - **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate - **Changes Required:** - Replace API calls creating MFD Leads with calls to the Account creation endpoints. - **Payload Construction:** - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first. - CompanyProperties: Provide an array of Attribute/Value pairs. - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name] - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup). - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" } - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" } - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" } - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field,

---

## #256 — Term Loan Charges
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Charges 1. No fees will be charged to users for the below scenarios : - Mandate bounce charges - Daily penal charges on interest overdue - Security sell-off charges 2. Business would need visibility on the below scenarios : - How many customers bounced with sourcing channel CRED (at Opportunity ID level) - No of days the EMI was overdue at Opportunity ID level for sourcing channel CRED - No of customers where security sell-off occurred along with sell-off amount and Opportunity ID mapping 3. No communication to be sent from DSP to CRED customers for any penal charges (even if the penal charges are equal to zero)

---

## #257 — Term Loan Communications
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

## #258 — Term Loan Customer Statements
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

## #259 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #260 — Term Loan Excess Handling and Refund
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

## #261 — Term Loan Manual Repayments(PG)
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

## #262 — Term Loan Manual Repayments(VA)
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

## #263 — Term Loan Sell off
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

## #264 — MFCentral CAS API Response Structure Analysis
**Status:** Unknown | **Last edited:** Unknown

# MFCentral CAS API Response Structure Analysis ## Top-Level Structure ```json { "reqId": "string", // Request identifier "pan": "string", // PAN number of the investor "pekrn": "string", // PEKRN (optional identifier) "mobile": "string", // Mobile number with country code "email": "string", // Email address (optional) "data": [ // Array of fund house holdings { "summary": [...], // Summary data for this fund house "schemes": [...] // Array of schemes under this fund house }, // Additional fund houses... ], "portfolio": [ // Overall portfolio summary { // Non-demat holdings summary }, { // Demat holdings summary } ], "investorDetails": { // Investor information // Address and contact details }, "statementHoldingFilter": "string" // Filter applied (e.g., "NON-ZERO") } ``` ## Fund House Data Structure Each element in the `data` array represents holdings from a single AMC: ```json { "summary": [ { "amc": "string", // AMC code "amcName": "string", // AMC full name "isDemat": "string", // "Y" or "N" for demat status "currentMktValue": "number", // Current market value "costValue": "number", // Total investment amount "gainLoss": "number", // Profit/loss amount "gainLossPercentage": "number" // Profit/loss percentage } ], "schemes": [ { // Detailed information for each scheme } // Additional schemes... ] } ``` ## Scheme-Level Structure Each scheme contains detailed investment information: ```json { "amc": "string", // AMC code "amcName": "string", // AMC full name "folio": "string", // Folio number "investorName": "string", // Investor name "age": number, // Investor age "mobile": "string", // Registered mobile "email": "string", // Registered email "taxStatus": "string", // Tax status code "modeOfHolding": "string", // Single, Joint, etc. "transactionSource": "string", // Source of transaction (BSE, etc.) "schemeCode": "string", // Unique scheme identifier "schemeName": "string", // Complete scheme name "idcwChangeAllowed": "string", // Income Distribution Change allowed flag "schemeOption": "string", // Growth, IDCW, etc. "assetType": "string", // EQUITY, DEBT, etc. "schemeType": "string", // Classification "nav": "number/string", // Current NAV "navDate": "string", // NAV as of date "closingBalance": "number/string", // Total units held "availableUnits": "number/string", // Redeemable units "availableAmount": "number/string", // Value of available units "currentMktValue": "number/string", // Total current value "costValue": "number/string", // Total investment amount "gainLoss": "number/string", // Profit/loss amount "gainLossPercentage": "number/string", // Profit/loss percentage "isDemat": "string", // "Y" or "N" "lienUnitsFlag": "string", // "Y" or "N" "decimalUnits": number, // Decimal places for units "decimalAmount": number, // Decimal places for amounts "decimalNav": number, // Decimal places for NAV "brokerCode": "string", // Distributor ARN code "brokerName": "string", // Distributor name "isin":

---

## #265 — Periskope to wati plan
**Status:** Unknown | **Last edited:** Unknown

# Periskope to wati plan # Periscope to Wati Migration Plan ## 1. Current Periscope Issues - No effective tracking of incoming chats or resolutions - Lack of chat status visibility (open/resolved/WIP) - Unable to monitor active chat groups - No categorization between sales and service chats - Missing bulk chat download capability - No response time (TAT) tracking - Agents losing track of ongoing conversations - Limited team capacity (2 people per shift) - No chat closure mechanism - Unclear analytics definitions - Missed chats going unnoticed - Integration issues with WATI ## 2. Metrics Comparison ### Current Periscope Metrics - Total interactions count - Unopened messages - Basic chat volume - Group activity status ### Available Wati Metrics - Open/Pending/Solved tickets - First Response Time - Resolution Time - Bot vs. Operator solutions - Expired conversations - Missed chats - Operator performance - Message delivery status - Conversation types - Tag distribution ## 3. Migration Goals 1. Improved Tracking - Real-time chat status - Response time monitoring - Issue categorization 2. Better Resource Management - Automated workflows - Clear agent allocation 3. Enhanced Analytics - Detailed performance metrics - Customer satisfaction tracking 4. Streamlined Operations - Automated responses - Efficient ticket management ## 4. Migration Plan with Checkpoints ### Phase 1: Setup (Day 0) - [ ] Configure Wati dashboard - [ ] Set up automated responses - [ ] Create tags and categories - [ ] Test message templates - [ ] Train agents **Checkpoint Metrics:** - System functionality - Template delivery success - Agent readiness scores ### Phase 2: Initial Migration (Day 1) - [ ] Migrate single and inactive MFDs - [ ] Monitor initial responses - [ ] Track conversion rate - [ ] Handle exceptions **Checkpoint Metrics:** - Message delivery rate - Response times - System stability ### Phase 3: Main Migration (Day 2-3) - [ ] Migrate remaining MFDs excluding top 250 - [ ] Monitor scalability - [ ] Adjust resources as needed **Checkpoint Metrics:** - Chat volume handling - Resolution rates - Customer feedback ## 5. Communication Templates ### Periscope Exit Message ``` Dear [MFD Name], To enhance your support experience, we're upgrading our communication channel. From [Date], we'll be transitioning to a new WhatsApp support system. Key Points: - Last day on current system: [Date] - New support number: [Number] - Transition period: [Duration] For any questions, please contact

---

## #266 — rough
**Status:** Unknown | **Last edited:** Unknown

# rough notes - Tat on a chat , - ticket resolution and creation - check whatsapp api changes Ideal flow MFD is had a request or a issue they communicate the issue with us we mark it as issue and solve it MFD —> Issues —> communications —> Tickets—> solution - IF a MFD or there employees have issues they can reachout to volt and we want to solve the issues promtly - MFD can communicate with us through WhatsApp chat - Now we need to Identify the issues , create a ticket and resolve the ticket Current problems - We don’t have the ticketing system in place - Current tools we are using are not optimal for creating and tracking Tickets Raw notes - The MFD facing challenges in getting timely response - All the onboarded MFD are added to periscope group - MFD’s uses WATI when they interact through Dashboard chat - MFD’s has to use two separate chat channel if they open up a Whatsapp channel through Wati - MFD’s ask , servicing , payout topic of communications are of general nature. our challenges - We have limited ( can’t) tracking of the incoming chats and there resolution - This is a Periskope limitation. we don’t get Open , resolved , WIP status of a Chat - we are unable to check “How many chats groups are active “ , “were active last week “ - We can’t identify if chats are Sales or service related - we get ~100 chats a day - There is no Bulk download chat option in Periscope - we can’t see TAT for a response and resolution - - agents loose track of the ongoing chats , as it chats are pushed to the bottom of the que and it become a issue to differentiate between the chat groups - 2 people work on the periscope - No way of closing the chats and mark that issue was solved - Analytics- daily number of message counts, Flagged messages - no explanation of what these terms are - How to raise tickets is not clear to the team - we use Periscope to reach out to MFDs , If a MFD reach-out and RM are unavailable then we assign another agent to Periscope - group is already connected with Periscope , all all the MFD are added to periscope they are

---

## #267 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs

---

## #268 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #269 — Analytics requirement Repayment
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Repayment | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of repayments | (count of total repayments made today) | | | | | | | | | | Number of transactions automatically settled | (count of repayments made and settled today) | yesterday | | | | | | | | | Number of transactions pending settlement | (Count of repayments made today but pending settlement) | | | | | | | | | | Average settlement TAT | For payments settled today avg(settled_on - created_on) - difference of hours | | | | | | | | | | % repayments settled automatically | % of payments that were settled automatically today (identify payments settled manually via admin action) | | | | | | | | | | | | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.collections ### Field: Collections: created_on - When payment was created Collections: settled_on - When payment was settled automatically Payment_status (If equals to settled - payment was settled either using admin action or automatically) ### Table: admin_action_audit (Credits) admin action name: UPDATE_COLLECTION_STATUS To identify which collections were settled manually Format: Email with CSV attached Sample query: ```sql SELECT CAST(collections.created_on AS DATE) as transaction_date,collection_status,count(*) FROM collections LEFT JOIN credits ON collections.credit_id = credits.credit_id WHERE lending_partner_id = 'Bajaj' AND CAST(collections.created_on AS DATE) <= current_date - INTERVAL '2' DAY AND CAST(collections.created_on AS DATE) >= current_date - INTERVAL '30' DAY AND collection_status not in ('REQUESTED','CANCELLED','FAILED') group by collection_status,CAST(collections.created_on AS DATE) order by 1,2 ``` Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #270 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #271 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #272 — Activation LSQ Task Creation
**Status:** Unknown | **Last edited:** Unknown

# Activation: LSQ Task Creation Flow: 1. Link generated gets generated and sent to the MFD over whatsapp 2. Task gets published in LSQ 3. RMs follow the tasks for calling and supporting the MFD with the VKYC flow and the link

---

## #273 — Thanks a lot for the explanation Can you also link
**Status:** Solutioning pending | **Last edited:** Unknown

# "Thanks a lot for the explanation. Can you also link to the documentation for this as I couldn't find it directly mentioned in the site, although LLA referenced it. My other query is : The processing fee of 999+GST will be applicable each time I make a withdrawal, or only during the creation of the credit line?" Classification: Processing Fee Notes: User asked if processing fees will be charged every time they make withdrawal, how to ensure this communication is straightforward PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 917005467390 Status: Solutioning pending

---

## #274 — User got charged the processing fee since they did
**Status:** Solutioning pending | **Last edited:** Unknown

# User got charged the processing fee since they did not make a withdrawal within the first month, they were not aware of this and caused an escalation Classification: Processing fee Notes: User got charged fee without disbursal, can comms be changed around this? how to ensure users are not surprised by seeing the charge posted in their account? PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 7974504413 Status: Solutioning pending

---

## #275 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #276 — Name
**Status:** Unknown | **Last edited:** Unknown

# Name Column 1: Does it check if the permissions are given? Column 2: Switch On Permission automatically/guide the customer? Column 3: Is Scheduling Available? Column 4: Configure communications for scheduled customers? Column 5: Is Digi Locker Integrated? Column 6: Is Pan Required? Column 7: Does Dashboard have Analytics Available?

---

## #277 — Detailed scope
**Status:** Unknown | **Last edited:** Unknown

# Detailed scope # Design Language System Documentation A comprehensive guide for Volt Money and DSP Finance ## Table of Contents - [1. Foundation](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#1-foundation) - [2. Components](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#2-components) - [3. Behaviors & Interactions](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#3-behaviors--interactions) - [4. Usage Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#4-usage-guidelines) - [5. Developer Tools](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#5-developer-tools) - [6. Logic & Business Rules](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#6-logic--business-rules) - [7. Platform-Specific Guidelines](https://www.notion.so/volt-money/Detailed-scope-94076bd5bcd54381979f8bc87a54b252#7-platform-specific-guidelines) ## 1. Foundation ### A. Design Tokens ### Colors - Primary palette - Secondary palette - Neutral colors - Semantic colors - Success - Error - Warning - Info ### Typography - Font families - Font weights - Size scales - Line heights - Letter spacing - Semantic styles - Headings (h1-h6) - Body text - Labels - Display text ### Spacing - Scale system - Layout spacing - Component spacing - Margin and padding rules ### Borders - Width scales - Radius scales - Styles - Color tokens ### Shadows - Elevation levels - Usage guidelines - Color and opacity ### Motion - Duration tokens - Easing functions - Animation patterns ### Grid/Layout - Grid system - Breakpoints - Container widths - Column configurations ### B. Brand Assets ### Logo - Primary logo - Secondary variations - Clear space rules - Minimum size - Usage guidelines ### Icons - Icon system - Size guidelines - Style guidelines - Usage rules - Icon library ### Illustrations - Style guide - Usage scenarios - Color application - Size guidelines ### Photography - Style guide - Composition rules - Color treatment - Usage scenarios ## 2. Components ### A. Base Components (Atoms) ### Buttons - Primary - Secondary - Tertiary - Icon buttons - States: - Default - Hover - Active - Disabled - Loading ### Inputs - Text input - Number input - Select - Checkbox - Radio - Toggle - States and validation ### Typography Elements - Headings - Paragraphs - Links - Lists - Inline elements ### Icons - Usage - Sizes - Colors - Alignment ### B. Composite Components (Molecules) ### Input Groups - Label + Input - Input + Button - Input + Icon - Validation messages ### Form Fields - Layout - Label placement - Helper text - Error states - Required fields ### Search Bars - Simple search - Advanced search - Filters - Results display ### Navigation Items - Menu items - Breadcrumbs - Tabs - Pills ### C. Patterns (Organisms) ### Forms - Layout patterns - Validation patterns - Submission patterns - Error

---

## #278 — Scope
**Status:** Unknown | **Last edited:** Unknown

# Scope V1 scope gotten made from claude [Detailed scope](Scope/Detailed%20scope%2094076bd5bcd54381979f8bc87a54b252.md) ## 1. Foundation ```jsx A. Design Tokens ├─ Colors ├─ Typography ├─ Spacing ├─ Border ├─ Shadows ├─ Motion └─ Grid/Layout B. Brand Assets ├─ Logo usage ├─ Icons ├─ Illustrations └─ Photography guidelines ``` ## 2. Components ```jsx A. Base Components (Atoms) ├─ Buttons ├─ Inputs ├─ Typography elements └─ Icons B. Composite Components (Molecules) ├─ Input groups ├─ Form fields ├─ Search bars └─ Navigation items C. Patterns (Organisms) ├─ Forms ├─ Navigation bars ├─ Cards └─ Tables ``` ## 3. Behaviours & interactions ```jsx A. Component States ├─ Hover ├─ Focus ├─ Active ├─ Disabled ├─ Loading └─ Error B. Motion & Animation ├─ Transitions ├─ Micro-interactions ├─ Page transitions └─ Loading states C. Interactive Patterns ├─ Form validation ├─ Error handling ├─ Loading sequences ├─ Data refresh patterns └─ Infinite scroll behaviors ``` ## 4. Usage guidelines ```jsx A. Implementation Rules ├─ Component composition ├─ Spacing rules ├─ Layout guidelines └─ Responsive behaviors B. Accessibility Guidelines ├─ Color contrast ├─ Keyboard navigation ├─ Screen reader support └─ Focus management C. Content Guidelines ├─ Voice & tone ├─ Writing style ├─ Error messages └─ Empty states ``` ## 5. Dev tools & documentation ```jsx A. Technical Documentation ├─ API documentation ├─ Props documentation ├─ Event handling └─ State management B. Code Examples ├─ Usage examples ├─ Integration guides ├─ Common patterns └─ Best practices C. Tools & Resources ├─ Design tokens export ├─ Component library ├─ Storybook documentation └─ Figma libraries ``` ## 6. Logic & business rules ```jsx A. Form Logic ├─ Validation rules ├─ Error handling ├─ Data formatting └─ Submission flows B. Data Display Logic ├─ Sorting ├─ Filtering ├─ Pagination └─ Data refresh rules C. State Management ├─ Loading states ├─ Error states ├─ Empty states └─ Success states ``` ## 7. Platform specific guidelines ```jsx A. Web ├─ Browser support ├─ Responsive breakpoints └─ Performance guidelines B. Mobile ├─ Touch targets ├─ Gesture support └─ Native patterns C. Cross-platform ├─ Consistency guidelines ├─ Platform adaptations └─ Feature parity ```

---

## #279 — User Persona Research
**Status:** ** Married with family responsibilities | **Last edited:** Unknown

# User Persona Research [V0.1 for User Research](User%20Persona%20Research/V0%201%20for%20User%20Research%206d63c60255e247f1a2d7a8b49d5a3bbd.md) [User Research Framework](User%20Persona%20Research/User%20Research%20Framework%20adba50e539a84bf8be27f3377b94ba29.md) ## Why do we need user personas - Empathise our user while designing products - Help target their goals, needs, aspirations and pain points - Make user centric product decisions ## Hypothesis ### Established Investor # Meet Rajesh Gupta - The Established Business Owner ## Demographics - **Age:** 44 years old - **Location:** Tier 1 city (Mumbai/Delhi/Bangalore) - **Profession:** Business Owner - **Income Level:** Upper middle class to affluent - **Family Status:** Married with family responsibilities ## Financial Profile - **Loan Requirements:** ₹7.35L (average for business customers) - **Primary Loan Purpose:** Working capital for business - **Investment Portfolio:** Active mutual fund investor - **Existing Loans:** Has a car loan and possibly a home loan - **Financial Behavior:** Financially aware but prefers quick solutions ## Digital Behavior - **Social Media Usage:** Moderate user of Facebook and Linkedin - **Content Consumption:** Actively watches financial/business content (56%) - **Preferred Platforms:** Newsletters (31%), Facebook (28%), YouTube (21%) - **Financial Influencers:** Follows personalities like Rachna Ranade, Akshat Srivastava ## Pain Points & Needs - **Time Sensitivity:** Needs immediate access to funds (74% unplanned loans) - **Process Friction:** Avoids traditional banks due to lengthy processes (69% don't approach banks first) - **Alternative Consideration:** Considers personal loans (41%) or borrowing (23%) before LAMF - **Social Constraints:** Hesitant to borrow from personal network despite considering it ## Decision Making Behavior - **Planning:** Generally makes quick, unplanned financial decisions for business needs - **Research:** Limited research into alternatives due to urgency - **Priority:** Views liquidating mutual funds as last resort but values speed and convenience - **Motivation:** Driven by immediate business requirements rather than personal expenses ## Product Expectations - **Core Needs:** Quick disbursement, minimal documentation - **User Experience:** Expects digital-first, seamless experience - **Post-Service:** Wants clear visibility of loan status, EMIs, and interest calculations - **Communication:** Prefers digital updates but appreciates timely reminders for payments ## Quote "Quick process, bethe bethe kaam ho gaya" (The work was done while sitting in one place) ### New Investors # Meet Aditya Shah - The Tech-Savvy Growth Seeker ## Demographics - **Age:** 28 years old - **Location:** Tier 1 city (Bangalore/Mumbai) - **Profession:** Senior Software Engineer at a tech startup - **Income:** ₹18-25 LPA - **Living Situation:** Single, lives independently in a rented apartment ## Financial Profile - **Investment Portfolio:** - Started investing 3-4 years ago - 60% equity mutual

---

## #280 — Postman collection
**Status:** Unknown | **Last edited:** Unknown

# Postman collection { "info": { "_postman_id": "unique-postman-id", "name": "Leegality UAT", "schema": "[https://schema.getpostman.com/json/collection/v2.1.0/collection.json](https://schema.getpostman.com/json/collection/v2.1.0/collection.json)" }, "item": [ { "name": "Inventory check", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/series/list](https://sandbox.leegality.com/api/v3.0/series/list)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "series", "list" ] } }, "response": [] }, { "name": "E-sign request - copy to be sent to customer", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"mKJY8rA\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "E-sign request - copy to be stamped and NBFC signed", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"profileId\": \"GpqF8Tf\",\n \"file\": {\n \"name\": \"string\",\n \"file\": \"string\"\n },\n \"stampSeries\": \"03\",\n \"invitees\": [\n {\n \"name\": \"Saksham\",\n \"email\": \"[saksham.srivastava@voltmoney.in](mailto:saksham.srivastava@voltmoney.in)\",\n \"dscConfig\": {\n \"verifyName\": false,\n \"verifySmartName\": false,\n \"verifyPincode\": \"string\",\n \"verifyState\": \"string\"\n }\n }\n ],\n \"irn\": \"string\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/request](https://sandbox.leegality.com/api/v3.0/sign/request)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "request" ] } }, "response": [] }, { "name": "Sign on e-sign request", "request": { "method": "POST", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "body": { "mode": "raw", "raw": "{\n \"signUrl\": \"string\",\n \"profileId\": \"naq2t4g\",\n \"consent\": \"By using this authenticated API and the ProfileID associated with this Document Signer Certificate, I agree that the Document Signer Certificate saved in this Account will be used to eSign documents for me. I also understand that recipients of such electronic documents will be able to see my signing details.\"\n}", "options": { "raw": { "language": "json" } } }, "url": { "raw": "[https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation](https://sandbox.leegality.com/api/v3.0/sign/docSigner/invitation)", "protocol": "https", "host": [ "sandbox", "leegality", "com" ], "path": [ "api", "v3.0", "sign", "docSigner", "invitation" ] } }, "response": [] }, { "name": "Download document", "request": { "method": "GET", "header": [ { "key": "X-Auth-Token", "value": "yYuokNRCRnTXcHC1ZCWOq3nzvSNoiq5R", "type": "text" } ], "url": { "raw": "[https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId={{documentId}](https://sandbox.leegality.com/api/v3.3/document/fetchDocument?documentId=%7B%7BdocumentId%7D)}&documentDownloadType={{documentDownloadType}}", "protocol": "https", "host": [ "sandbox", "leegality", "com"

---

## #281 — DSP Fin Partner Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin: Partner Page # Context RBI requires REs to disclose LSP details in a standard template. While we do the elegant website change, we want to modify only the partners page to be compliant with regulatory requirements. # Requirements As per the RBI guidelines on DLG here, RBI requires REs to disclose the following details. 1. Details of all of its digital lending products and its DLAs; 2. Details of LSPs and the DLAs of the LSPs along with the details of the activities for which they have been engaged for; 3. Particulars of RE’s customer care and internal grievance redressal mechanism; 4. Link to RBI’s Complaint Management System (CMS) and Sachet Portal; 5. Privacy policies and other details as required under extant guidelines of the Reserve Bank. We will display the below details in the current partners page. - Name of LSP - Nature of Service Availed from LSP's - Description of the LSP - DLA of the LSP - Additional Information about the Lender Sample file is attached for reference. [DSPFin Website Disclosures of LSP DLA.odt](DSP%20Fin%20Partner%20Page/DSPFin_Website_Disclosures_of_LSP_DLA.odt) # Benchmarking A few other lenders who display the LSP details are listed below. - InCred: https://incred.com/partnership/ - Piramal : https://www.piramalfinance.com/about-us/lending-partners - BFL: https://www.bajajfinserv.in/bajaj-finserv-partners - ABFL: https://www.adityabirlacapital.com/loans/our-digital-lending-platform-partners

---

## #282 — DSP Fin Website About Us Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin Website: About Us Page **Objective**: To communicate about the values of the company to audience. DSP Finance is a Non-Banking Financial Company (NBFC) backed by the 160+ year legacy of the DSP Group — one of India’s most respected names in financial services. Rooted in trust, innovation, and discipline, we provide customized credit solutions designed to help individuals and businesses unlock value and achieve their financial goals. We are a NBFC with a strong focus on growth through operational excellence and solving problems through technology. **Mission**: To combine deep market expertise with customer-first innovation, ensuring **reliable, transparent, and efficient access to credit** by leveraging technology and robust operational excellence. **Vision**: To be India’s most trusted partner for financial collateral-backed credit, enabling individuals and businesses to unlock value from their investments for exponential financial growth. DSP Finance’s Values. - Customers first - Utmost transparency - People focus - Continuous innovation Key Highlights of DSP finance to be mentioned - AUM of ~2000CR - ~70K customers - 8+ leading partners - AAA rated DSP Finance’s focus is on capital markets led product offerings in the below business lines. - Loan against securities: enabling individuals to leverage their financial assets to get easy access to credit. This page will redirect to the LAS page. - Financial solutions group: providing corporates access to credit by leveraging their assets to get quick access to funds. This page will redirect to the FSG page. DSP Finance works on the below principles. - **Legacy of Trust** – Backed by the DSP Group’s long-standing credibility in Indian finance ecosystem. - **Customer-First Approach** – Transparent processes, no hidden charges, and clear communication. - **Digital-First Experience** – End-to-end paperless solutions with seamless pledge and disbursal. - **Prudent Risk Management** – Strong governance and compliance in line with RBI regulations. - **Expertise & Innovation** – Blend of deep financial knowledge and modern technology to drive deep innovation. DSP has partnered with leading partners to enable customers to leverage their assets. - PhonePe - PayTm - Indmoney - Groww - ETMoney - CRED

---

## #283 — NBFC B2B LSP API List
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : API List - Pledge API on DSP - pending - Fetch API on DSP - pending - Submit opportunity - create account - Mobile & Email update - no verification - Add verification timestamp for mobile & email - KFS & Agreement: we might have to decouple and make KFS pass the response in parameters - Offer API on DSP - LSP passes back the confirmation to DSP - PAN verification - LSP not required to integrate -

---

## #284 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #285 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #286 — Problem Discovery & Tracking
**Status:** Unknown | **Last edited:** Unknown

# Problem Discovery & Tracking # Challenges Currently, Volt’s Product team is solving problems across the board at different stages. In addition, the team gets requirements from stakeholders spanning business, operations, partners, etc. This results in multiple challenges. - Lack of a consolidated view of all items - Lack of visibility of multiple things on the PM’s plate - Man-hours spent in tracking items across business, product and tech - Lack of clear communication/ updates to stakeholders - Lack of visibility of sprint plan and the aligned features. A lot of this is happening due to the below reasons. - PMs are using Notion to document basic PRDs. However, all detailed requirements and its tracking is happening on Jira. - PMs use google sheets to maintain trackers for each features which becomes a challenge as there’s no one-stop visibility - Design team doesn’t have complete visibility and a lot of misses happen post a feature being picked up for development or at PRD review stage. - Calling out blockers and tracking various open items across multiple items becomes a challenge due to lack of holistic visibility. - Sprint goals and plans are maintained on excel which isn’t fully linked to Jira which becomes tough to visualize end-to-end. # Proposed Solution Below is the proposed solution. - Use Google sheets for stakeholder alignment - Use Jira (PSB board) for all problem discovery items - Use Notion for PRDs and detailing out requirements - Use Jira for writing detailed requirements (user stories) The rationale for using Jira is that helps track items under development as well as items that don’t need tech intervention. In addition, Jira has all the required capabilities to track complex items like project tracker, creating list of items, etc # Proposed Process Below is the proposed process. - Stakeholder discusses a problem statement OR the PM/PD finds a problem - PM/PD documents the item on Jira on the PSB board as one of the items. - **Epic**: a large project that requires multiple items for completion - **Story**: a story level item that requires only task level items - **Task**: a single task like sign-off from stakeholders, bug, etc. - PM/PD can add multiple items and keep adding comments as well as move tasks to different statuses - PM/PD should aim to segregate problems into 2 buckets. - Problem discovery, identification, sign-off and prioritization - Solution discovery, identification,

---

## #287 — Product note template (Duplicate this for use)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Product note template (Duplicate this for use) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) --- ## **3. Solution Scope** ### Solution overview - Explain in 2-3 lines the overview of the solution - Explain overview of the solution with key product and system changes - Explain the rationale on scoping/phasing of the solution - Call out scope that has been scoped out and explain the rationale ### Detailed solution scope: - Bullet list of user and system use cases that are supported: - Define all use cases applicable and what are in scope - Core happy path - Key edge cases that must be handled at launch - Consider all the stakeholders that are impacted - Has to answer questions like: - How does this change existing operational SOPs? - How does this change the experience for the end user? - How does this impact sales or onboarding conversations? | Description | Details | | --- | --- | | | | | | | | | | --- ## **5. High level s***ystem, user or process flow* - - Cover the overview of the process or the journey - Include error cases or edge cases (Optional) --- ## **6. Appendix (Optional)** ### Benchmarking: ### User feedback / Calling:

---

## #288 — User Story template
**Status:** Unknown | **Last edited:** Unknown

# User Story template # Guidelines **How should user stories be written?** - Each user story should be atomic — focus on one activity or action. - One feature needs to have multiple user stories for each activity. - For the UPI mandate registration feature, this will be: - Context page. - Mandate registration page. - UPI registration (TPAP). - Post-registration confirmation. - Retry or fallback, if required. - Each user story should be written from a user/customer perspective. - Users can be internal users like sales, support, or operations OR - User can be customer OR - User can be a partner (B2B or LSP) - User stories should document key scenarios and how they will be handled from a UI/UX perspective. - For the UPI mandate feature, this will be: - Mandate registration is pending due to user inactivity. - Mandate registration failure due to user error. - Mandate registration failure due to technical issues. - Mandate registration success. - Delayed confirmation handling. # Template Below is a template for User Stories. - **User Story ID**: this is a unique identifier in a PRD that is linked to a user story. This can be alphanumeric like U1 or US1, etc. - **User Story**: this will be a 1-2 liner that will talk about the user story in question. This will mention what the user is setting out to achieve. - **User requirements**: this will be the detailed requirements, by building which, the user will be able to achieve the requirement. # Example Below is a list of User Stories keeping UPI mandate registration as an example. - **U1**: As a customer, I want to know why a recurring debit needs to be setup so that I can move forward with setting up a mandate. **Flow**: Once the customer has completed the bank account verification step and the bank is verified, the customer is presented a screen to setup a auto-debit (mandate). **Success criteria**: The customer should be able to understand the rationale for an auto-debit and move forward in the journey. **Requirement**: Below are the requirements for this page. - Once the user lands on this page, the user should be conveyed that Volt will setup a mandate to debit the monthly interest. - This will be a common page that will cover both NACH and UPI mandate. - This page will describe that customer’s bank account will

---

## #289 — Product Processes
**Status:** Unknown | **Last edited:** Unknown

# Product Processes [Product Discovery Process](Product%20Processes/Product%20Discovery%20Process%20f37c9edce0b54be18a223d28b3c298f9.md) [Product Requirements Standards](Product%20Processes/Product%20Requirements%20Standards%2011de8d3af13a80eb95a2dd3932920a07.md) [Invoice & Payment Process](Product%20Processes/Invoice%20&%20Payment%20Process%20111e8d3af13a808c9c0bc626c723b28e.md) [Product Feedback Process](Product%20Processes/Product%20Feedback%20Process%2011ce8d3af13a8033be22f9de58e9b4b4.md) [Product Release Process](Product%20Processes/Product%20Release%20Process%2011de8d3af13a80b78dabe101e9ec7d8b.md) [Problem Discovery & Tracking](Product%20Processes/Problem%20Discovery%20&%20Tracking%2011de8d3af13a80268a83ebb07efd9e5f.md) [Product Impact Analysis](Product%20Processes/Product%20Impact%20Analysis%2011fe8d3af13a80a091feda5d39a5d9ad.md) [Bug Fix Process](Product%20Processes/Bug%20Fix%20Process%2011fe8d3af13a801eb2ede8072b602bc3.md) [Product Release Process (Draft)](Product%20Processes/Product%20Release%20Process%20(Draft)%20122e8d3af13a802cbfcacd425595c340.md) [Product Analytics Process](Product%20Processes/Product%20Analytics%20Process%2019ae8d3af13a80eebcb0c66556b20b46.md) [User Story template](Product%20Processes/User%20Story%20template%202d2e8d3af13a8026992dce13d3df6ec9.md) [Product note template (Duplicate this for use)](Product%20Processes/Product%20note%20template%20(Duplicate%20this%20for%20use)%202cde8d3af13a802a9af1eaea66c5f45c.md) [Referral Product Note](Product%20Processes/Referral%20Product%20Note%202cfe8d3af13a80b485fff3273928ebca.md) [Referral Product Note [Claim approaches]](Product%20Processes/Referral%20Product%20Note%20%5BClaim%20approaches%5D%202e7e8d3af13a808da491fa947658081c.md) [Referral Product Note (1)](Product%20Processes/Referral%20Product%20Note%20(1)%202e7e8d3af13a804899c0cad099c6aa81.md) [Referral Product Note (1)](Product%20Processes/Referral%20Product%20Note%20(1)%202e7e8d3af13a807ab9a1fe10c4c8527d.md)