# Current State: Pledge

> Auto-generated from 258 PRD(s). Most recently edited shown first.


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

## #5 — PRD - Handling MF Central CAS Summary API fields r
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

## #6 — Deferring email capture and verification during on
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

## #7 — Manage Limit Error messaging handling
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

## #8 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #9 — MF Pledge optimizations
**Status:** In progress | **Last edited:** September 16, 2024 8:23 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #10 — BRE Proposal for cases above 1 Cr
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

## #11 — Streamlining Support Communication by Segregating
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

## #12 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #13 — BAJAJ New KFS+Agreement flow
**Status:** Done | **Last edited:** October 8, 2024 1:04 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload

---

**Solution:**
?**

---

## #14 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #15 — LSQ Revamp Solution Doc
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

## #16 — Master collections PRD (NBFC)
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

## #17 — [IronGrid] Adding un-pledge validations in BE
**Status:** Not started | **Last edited:** October 25, 2024 1:20 PM

# [IronGrid] Adding un-pledge validations in BE ### Validations present in FE **FE Checks** - Manage limit - Remove pledge - Pledge more - Pledge history - At this page we have a starting check of buffer - User taps on Remove pledge and lands on the screen with list of funds - Buffer check applied again to calculate the number of units which can be selected by the user for un-pledging **Checks to be added** - Jay to share the tech solutioning doc of the customer - Folio level checks need to be added - Need to create validation in init API using this API : app/borrower/lms/credit/lender/manageLimitConfig

---

## #18 — [Lending stack] Welcome mail
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

## #19 — DSP communication email template
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

## #20 — invest well partners
**Status:** Not started | **Last edited:** October 18, 2024 4:01 PM

# invest well partners - they are unable , clienttsnames - even if the appllucation is completed , showing in progress next steps , undertand the implementation

---

## #21 — Withdrawal Optimisations
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

## #22 — LOS and LMS admin actions (LSP with DSP as lender)
**Status:** In progress | **Last edited:** October 16, 2024 2:25 PM

**Problem:**
are we solving?**

We have developed multiple admin actions (ops controlled actions) that help in servicing our customers in the onboarding as well as the servicing journey. 

This requirement covers utilising the admin actions (where needed) to cover use cases currently served by LSP (for customers) with DSP as a lender.

---

**Solution:**
?**

---

## #23 — Bulk email automation
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

## #24 — Integrated Sales tool
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

## #25 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

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

## #27 — [TL] Shortfall handling
**Status:** Pending Review | **Last edited:** October 1, 2025 1:26 PM

**Problem:**
are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

**Solution:**
?**

---

## #28 — Process note Creating a new user on Command Centre
**Status:** Done | **Last edited:** November 8, 2024 9:36 AM

# Process note: Creating a new user on Command Centre # Process Note: Creating a User on Command Centre ## Overview This document outlines the step-by-step process for creating a new user account on the Command Centre system. ## Prerequisites - Admin access to the Command Centre system - New user's details (full name, email address, role, department) - Approval from Head of Operations (@Nishant Athmakoori) [Access level details](https://docs.google.com/spreadsheets/d/1VSPMYia-Kmwob9X3pH-T3nMTYNZxXpEC_Afpfq27e-o/edit?gid=0#gid=0) ## Steps 1. Request for access on Email from the business counterpart, in this case, all access will be shared by @Nishant Athmakoori 1. Details required in the email: 1. Name 2. Designation 3. Role (Admin / Approver / Read only) 4. Employee ID 5. Mobile number 6. Email address (DSP Email address) Any requests without the aforementioned details will get rejected 2. Forward the access with consent and approval to tech-ops@dspfinance.com 3. Access will be shared within 1 working day of request. 4. Once access is shared (User name and password), logon to the command centre using the following URL: https://cc.dspfin.com/login 5. Once logged on, users will be able to use the command centre for the following utilities: 1. Client search (all roles) 2. Loan search (all roles) 3. Review client details (all roles) 4. Review client KYC details (all roles) 5. Review client risk details (all roles) 6. Review loan details (all roles) 7. Review transactions (money and collateral) (all roles) 8. View servicing tasks (Approver and admin only) 9. View collateral tasks (Approver and admin only) 10. View application tasks (Approver and admin only) 11. View NBFC operations tasks (Approver and admin only) 12. Approve or reject tasks (Approver and admin only) ## Post-Creation Steps - Document the new user creation in your system log or user management spreadsheet ## Troubleshooting If you encounter any issues during this process, please contact the IT support team at tech-ops@dspfinance.com

---

## #29 — Excess amount handling
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

## #30 — Lien removal SLA tracking report
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

## #31 — Lodgement decoupling from enhancement
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

## #32 — [IronGrid] Un-lien related issues
**Status:** Not started | **Last edited:** November 5, 2024 12:48 PM

# [IronGrid] Un-lien related issues ## Fund level status of un-pledge request **Phase 1** - Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED. - We will keep polling the status of all the funds until we get the terminal statuses of each of the funds - We keep polling the API for 4 days every hour until we get the status of all the fund - Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached) - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request - We will store the individual status of all the funds under the un-pledge request - API Documentation : [Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx) **Phase 2** - We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user. ## Excess margin handling in un-pledge request **For BFL (only need to make this change for BAJAJ)** - While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge. - 3 fields which are present in Foreclosure details API : - net payable = Total due - Excess Margin - Total Due - Excess Margin - For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding. ### **User not able to request un-lien request if stocks present in their holding** - **Issue** - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error - **Solution** - We will only

---

## #33 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #34 — Lodgement maker
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

## #35 — TATA Dedupe API with updated BRE
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

## #36 — NLP-736 Timestamp value is not captured with hh mm
**Status:** Not started | **Last edited:** November 19, 2024 7:41 AM

# NLP-736: Timestamp value is not captured with hh:mm:ss due to which the default value 05:30:00 is shown in the UI Command centre search result pages: Client creation date (client search) Expiry date (loan search) Bureau pull date (client details risk section) AML pull date (client details risk section) Mandate expiry date (loan details section) Expiry date (is in small case) KYC expiry date is comming as invalid date Completed on (repayment detail is coming as invalid detail)

---

## #37 — TCL getDisbursementAPI logic updation
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

## #38 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #39 — Enhancement optimization
**Status:** In progress | **Last edited:** November 14, 2024 7:21 PM

**Problem:**
are we solving?**

- For the customers whose DP is significantly less than sanction limit when try to enhance (pledge more funds) such that there sanction limit does not get updated then user are not given information

---

**Solution:**
?**

---

## #40 — [Lending stack] Agreement execution flow
**Status:** In progress | **Last edited:** November 12, 2025 1:01 PM

**Problem:**
are we solving?**

- Customer signing through platforms like Leegality and Digio has their own disadvantages. They don’t support clickwrap agreement making it hard for customers to sign on agreement.
- These vendors don’t provide the ideal flow which balances for regulation and cost of stamping.

---

**Solution:**
?**

---

## #41 — KYC Risk Status (NBFC Platform)
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

## #42 — MFC Summary API calculations update
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

## #43 — Repayment flow for DSP
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

## #44 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #45 — Replacing the MFD referral messgage
**Status:** Not started | **Last edited:** May 8, 2025 4:10 PM

# Replacing the MFD referral messgage change the Referral message to ” Greetings 🙏 Help your clients meet short-term cash needs without redeeming mutual funds. Use Volt to open a credit line against mutual funds in 5 minutes with trusted lenders such as DSP Finance. Interest rates starting at 10.49. Use this link to empanel now. [https://voltmoney.in/partner?ref=HMWGGX](https://voltmoney.in/partner?ref=HMWGGX) Regards, Naman agarwal” ![Screenshot 2025-04-14 at 1.57.44 PM (1).png](Replacing%20the%20MFD%20referral%20messgage/Screenshot_2025-04-14_at_1.57.44_PM_(1).png) [https://voltmoney.in/partner/referredpartner](https://voltmoney.in/partner/referredpartner) Whatsapp, telegram , copy message

---

## #46 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #47 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #48 — MFC Pledge error handling - V1 (1)
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

## #49 — Phase 1 LTV Tenure Update_LOS
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

## #50 — Sell-off Repayment Reconciliation — Maker Automati
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

## #51 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #52 — STP validation for Sell-off Repayment Reconciliati
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

## #53 — CAMS min_unit Validation for LAMF Lien Transaction
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

## #54 — Phase 0 LTV Tenure Update_LOS
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

## #55 — Handling LOS Application Rejections
**Status:** Not started | **Last edited:** May 25, 2026 12:22 PM

**Problem:**
are we solving?**

Currently in LOS , several business-critical validation checks are performed — such as client deduplication, MNRL checks, and AML/PEP screenings. 

However when any of these checks fail, the system surfaces a generic ‘declined’  error message (”Something went wrong”) to the user. The root cause is that the backend does not propagate the specific error code or reason to the frontend, so the frontend cannot render contextual, actionable error screens.

---

**Solution:**
?**

---

## #56 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #57 — MFC Summary API integration
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

## #58 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #59 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #60 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #61 — Lodgement STP optimisations
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

## #62 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #63 — STP validation for Bulk Sell off
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

## #64 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #65 — Product Note LTV update to 70
**Status:** Not started | **Last edited:** May 12, 2026 10:39 AM

# Product Note : LTV update to 70 --- # **1. Problem Statement** --- ## **2. Objective** --- ## **3. Scope** --- - LTV update task - Finflux - Multiple approved script management - Validations - Any sort of handling - Fenix - Multiple approved scripts handling - Risk and RMS validations required - Impact of all collateral transactions - Collateral addition - Collateral removal - Collateral invocation - Shortfall handling - Communications and statements - ROI auditing - Current offer visibility for NBFC and LSPs - Volt - Journey - Enhancement (Fetch/Pledge/Offer/Agreement) - Nudges - B2B2C & B2C - PF/ROI changes - Journey - Admin actions (PF increase to work out of the box) - Payout - Scope reduction - Loan offer - PF/ROI - Contract level - Volt UI --- - Nudge - Current limit - Updated Limit - Current ROI - New ROI - LTV update charges - KFS/Agreement - Task name - Service request approval - Left panel - Request details - Request ID - Service request type : Limit enhancement - Requested on - Current collateral limit - Additional collateral limit - Updated collateral limit - Limit enhancement charges - AMC charges - Substatus - Maker name - Maker remark - Maker created on - Collateral details - ISIN - Asset type - Collateral sub type - Folio - Value - Existing limit - New limit - Right panel - Client details - Loan details - With loan contract - Transactions - Collaterals - Collaterals with details (LTV) - Loan kit - KFS - Agreement - Generate offer what happens? - Request - FXLAN (with collateral details) - Response - Funds with higher LTV - Limit enhancement charge ranges - AMC charge ranges - ROI ranges - Accept offer - Request - Fund with LTV, charges & ROI details - Response - Offer ID - Service request and collateral addition in parallel, what validations to happen

---

## #66 — Term loan CC enhancements
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

## #67 — [Platform] Unpledging of unlinked funds bulk appro
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

## #68 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** March 24, 2026 11:57 AM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #69 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #70 — Revocation Status API
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

## #71 — [Platform] Wrapper APIs for RTAs
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

## #72 — Lien status lifecycle tracking
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

## #73 — Foreclosure lifecycle tracking + Tata EOD report
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

## #74 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #75 — Improving Mandate Conversions
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

## #76 — [B2B2C] Modification for financial terms functiona
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

## #77 — Product note Co-lending foreclosure - Deprecated -
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

## #78 — Capital gains tax calculator
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

## #79 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #80 — Margin pledge charges
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

## #81 — Margin pledge charges
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

## #82 — PhonePe KFS & Agreement
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

## #83 — B2B Zype integration FE and SDK callbacks
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

## #84 — MFC Pledge (revocation & invocation)
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

## #85 — [Platform +Volt ] MFC Pledge wrapper APIs + Volt J
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

## #86 — Razorpay PG SDK integration DSP (1)
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

## #87 — Razorpay PG SDK integration DSP
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

## #88 — [Volt LSP] MFC pledge
**Status:** Not started | **Last edited:** July 21, 2025 3:33 PM

**Problem:**
are we solving?**

Current pledging requires customers to submit upto two OTPs, one for CAMS and another from KFin. This add to the friction in our loan application journey. 
MFC pledging APIs solve this by requiring 

---

**Solution:**
?**

---

## #89 — Making Mobile & Email Verification Log Optional LO
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

## #90 — [Platform] BRE configurations for approval tasks
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

## #91 — [B2B2C] Fixed deposits via partner dashboard
**Status:** Pending Review | **Last edited:** January 8, 2026 4:23 PM

**Problem:**
are we solving?**

---

- Volt is looking to improve partner engagement by helping partners monetise their existing clients better and sell multiple financial products through one platform. Adding Fixed Deposits (FDs) as a product offering allows partners to offer a popular, high-value product along with loans.
- The objective of this initiative is to integrate FD booking and servicing into the existing Volt Partner Dashboard, leveraging Fixxera for the booking journey while providing partners with a unified interface to initiate, track, and manage FD applications.

**Solution:**
?**

---

## #92 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #93 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #94 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #95 — Delaying getDisbursementInfo API hit after savePle
**Status:** Pending Review | **Last edited:** January 6, 2025 3:50 PM

**Problem:**
are we solving?**

- For the first getDisbursementInfo API call post credit creation we are getting “No data Found” in the response of the getDisbursementInfo API
- Since we run a scheduler of 1 hour of getDisbursementInfo thus it takes another hour to get a valid response from getDisbursementInfo API response (after getting No Data Found in the response first time)

---

**Solution:**
?**

---

## #96 — MFC in-app journey
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

## #97 — B2B Platform Dashboard v1
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

## #98 — [Platform LSP] All transactions requirements
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

## #99 — Shortfall FAQ
**Status:** Not started | **Last edited:** January 21, 2025 8:23 PM

# Shortfall FAQ What is shortfall? Short fall is the when the DP of customer goes below the withdrawn amount. This happens due to Market downfall. LTV SEBI Regulatory LTV As per RBI the Guidelines are the LTV should be 50% DSP Configured LTV we generally keep the LTV 0.45 to keep buffer of 10% for the Market fall There is minimum limit of the Pledging of the 25k

---

## #100 — [LSP] Total outstanding amount correction and over
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

## #101 — [Platform] QC rejection handling
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

## #102 — Redvision Update
**Status:** Not started | **Last edited:** January 20, 2025 12:50 PM

# Redvision Update - When a Redvison a Volt Partner App, then they will have the different partner ID, This causes Payout issues , and the Mobile number get deleted - Bank account details , name not being able to change from redvision Portal - Redvision MFD, Payout visibility and process understanding - Name, Bank account , IFSC are required - DIgilocker , pourpose of loan —> there is difference in Dropdown item , like Medical loans , etc - Partners operate on different platforms. Somesh - Family account have same mobile number HNI clients, How to handle , with same phone number mention the Unique number requirement on the page - There is difference in Login and Fetch mobile number - In pledge is there is a delay of few day and the Pledge Value is changed then the Pledge step fails , MFD needs to Refresh the The portfolio then pledge IF the Customer has come on the app then the Application is not available on the MFD portal even after the Admin action - Invest well issues, Payout ETC, MFD are moving out from Investwell Bank account - Why after bank verification we get the lender IMPS name Mismatch issue , IFSC change of bank accounts Mandate setup - Customer is Registed on a Bank one 1 , then Book the Mandate on other bank , on the CC. - issue limited to Bajaj, not in tata or DSP KFIN -pledging issues \ - Redi After loan created , withdraw option is not shown instantly , instead “pending logement “ till logement happens 50 soa

---

## #103 — [Fenix] Lodgement maker bulk approval
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

## #104 — External APIs for Holdings Statement and Statement
**Status:** In progress | **Last edited:** January 16, 2025 7:53 PM

# External APIs for Holdings Statement and Statement of Accounts (SOA) External APIs for Holdings Statement and Statement of Accounts (SOA) --- ## 1. Introduction This document outlines the requirements for developing external APIs that will provide Holding Statements and Statement of Accounts (SOA) to MFD partners. These APIs will enable partners to access comprehensive financial statements and holdings data for their customers, enhancing transparency and operational efficiency. ## 2. Objective To develop robust external APIs that provide detailed holdings statements and transaction histories, allowing MFD partners to: - Access real-time holdings data - Retrieve historical transaction statements - Generate comprehensive financial reports - Support customer portfolio management ## 3. Target Audience ### Primary Users - MFD Platform Developers - MFD Operations Teams - MFDs ## 4. Scope ### In-Scope - Development of two primary APIs: 1. Get Holdings Statement API 2. Get Statement of Accounts (SOA) API - Documentation and specifications - Data validation and error handling - Integration with existing systems like Invest well dashboard ### ## 5. API Specifications ### 5.1. Get Holdings Statement API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/holdings?date={date} ``` ### Description Retrieves a comprehensive holdings statement for a specific date, showing all active mutual fund investments and their current values. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `date` (string, optional, format: YYYY-MM-DD): Date for which holdings are requested. Defaults to current date ### Response Payload ```json { "holdingsStatement": { "statementDate": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "holdings": [ { "folioNumber": "1041038180", "schemeName": "Aditya Birla Sun Life Flexi Cap Fund", "isinCode": "INF209K01AJ8", "units": 22.7620, "navValue": 1670.00, "currentValue": 38021.64, "lienMarked": true, "lienQuantity": 22.7620, "lienMarkingDate": "2024-09-14" } ], "summaryMetrics": { "totalPortfolioValue": 2454930.52, "totalLienMarkedValue": 801000.00, "availableValue": 1653930.52 } } } ``` ### 5.2. Get Statement of Accounts (SOA) API ### Endpoint ``` GET /v1/partners/{partnerAccountId}/soa?startDate={startDate}&endDate={endDate} ``` ### Description Retrieves a detailed statement of accounts showing all transactions within the specified date range. ### Parameters - **Path Parameters:** - `partnerAccountId` (string, required): Unique identifier for the partner account - **Query Parameters:** - `startDate` (string, required, format: YYYY-MM-DD): Start date for the statement period - `endDate` (string, required, format: YYYY-MM-DD): End date for the statement period ### Response Payload ```json { "statementOfAccounts": { "periodStart": "2024-07-01", "periodEnd": "2025-01-16", "customerDetails": { "name": "Shubham Kapoor", "accountNumber": "30345", "pan": "AUWPA7175L" }, "transactions": [ { "date": "2024-07-02", "transactionType": "DEBIT", "description":

---

## #105 — [Email Template] Decoupling of Lodgement and Agree
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

## #106 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #107 — [CC] Lodgement Enhancement
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

## #108 — [Platform] Handling of below 1 Rs transactions for
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

## #109 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #110 — PhonePe PG Implementation
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

## #111 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #112 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #113 — Shortfall communication enhancement Ignoring accou
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

## #114 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #115 — Product Note Separating Portfolio Pledge and Asset
**Status:** Not started | **Last edited:** February 21, 2025 3:29 PM

# Product Note: Separating Portfolio Pledge and Asset Pledge Steps in LSQ # Product Note: Separating Portfolio Pledge and Asset Pledge Steps ## Current Behavior Currently, the system combines two distinct steps - MF Portfolio Pledge (offer page) and Asset Pledge - into a single step labeled as `ASSET_PLEDGE_STEP` in the CRM event mapping. This creates ambiguity in tracking and managing these separate processes. ## Problem Statement The current implementation: 1. Does not distinguish between portfolio pledge (offer page) and actual asset pledge steps 2. Sales agents have hard time understanding is the application is on offer or pledge for calling 3. Creates confusion in the application flow tracking 4. Reduces granularity in analytics and monitoring ## Proposed Solution Separate the current combined step into two distinct steps: 1. **Portfolio Pledge** (`PORTFOLIO_PLEDGE_STEP`) - Represents the offer page where customers view their eligible portfolio - Maps to `MF_PLEDGE_PORTFOLIO` in application flow 2. **Asset Pledge** (`ASSET_PLEDGE_STEP`) - Represents the actual asset pledging process - Maps to `ASSET_PLEDGE` in application flow ## Implementation Changes Required 1. Update CRM event mapping in `getCRMEvenTypeForStepStart`: ```java case MF_PLEDGE_PORTFOLIO -> CRMEventType.PORTFOLIO_PLEDGE_STEP; case ASSET_PLEDGE -> CRMEventType.ASSET_PLEDGE_STEP; ``` 1. Update DB schema to reflect new step definitions: - Add `PORTFOLIO_PLEDGE` as a distinct step after `MF_FETCH_PORTFOLIO` - Keep `ASSET_PLEDGE` in its current position in the flow ## Expected Benefits 1. Improved tracking and analytics 2. Better user journey mapping 3. Better lead prioritisation in outbound ## Migration Plan 1. Understand current Lead stage update activity send to LSQ 2. Create new step definitions in DB 3. Verify the changes in LSQ 4. (Backfill) ## Next Steps 1. PN :- Tech Review

---

## #116 — Verify interest and charges revamp
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

## #117 — Redemption regret calculator
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

## #118 — Attribution for Jupiter
**Status:** Not started | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

- We need to create a BRE which will allow Jupiter platform to create customer even if customer account exist.

---

**Solution:**
?**

---

## #119 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #120 — Pledge error handling
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

**Solution:**
?**

---

## #121 — Capture foreclosure reasons from customer
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

## #122 — Comms config - OTP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and *

**Solution:**
s:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

---

## #123 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #124 — Foreclosure repayment - Handle PenalInterestAccrue
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

## #125 — Handle excess amount in foreclosure request [TCL]
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

## #126 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #127 — Interest feature handling for TCL
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

## #128 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #129 — Loan servicing - LAS VOLT
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

## #130 — MFC fetch in Volt Journey
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

## #131 — Partial lodgement handling - DSP
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

## #132 — Partner MFD Dashboard PRD (LAS Servicing)
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

## #133 — Project Elevate - LMS
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

## #134 — Revocation MIS - TCL customer
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

## #135 — Supporting shares as a collateral - LMS (Volt)
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

## #136 — Volt Mandate re-registration Post loan
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

## #137 — Ticketing system for Volt
**Status:** In progress | **Last edited:** February 19, 2025 3:20 PM

# Ticketing system for Volt # **Problem Statement:** Volt intent to provide best in class support to the Partners and customer. Due to the Nature of product being the Credit application, significant amount of support is needed to provided to the Users To scale efficiently we need to Move more applications to Zero touch and and Handle the support Requests that we do get more efficient. Applications successful = With + without assist = Count * Cost Current Support team are facing following challenges Borrower - Long wait times for the agents to get back - Chat support - visibility - we don’t have rich visibility on the Ongoing calls and messages to the Agents. We would like to How many query of a particular issue was received and can we solve it through product. - RMs and agents have to provide context in sending the client Between RMs or on Leave - We would have a data on the issues raised by a particular customer or to maintain history of support - If the support request is not OPS or Tech realted then taking followup - High Inbound Traffic :- Agents are move from call to call and saving - Lack of a single source of truth for customer issues. - Inconsistent tracking across calls, WhatsApp, and emails. - Unrecorded issues, especially from phone calls. - No SLA tracking or identification of common problems. **Key Requirements:** - **Mandatory Ticketing**: Every interaction (calls, WhatsApp, emails) must generate a ticket. - **Ticket Details**: Include customer phone, partner/platform ID, creator ID, issue category, description, channel, owner, status, and resolution notes. - **Workflow Needs**: - Easy ticket creation and search by phone number. - Visibility into all tickets per customer/issue. - Strong APIs and customizable workflows. - **Tool Integration**: Must work with Exotell, WABA, email, Slack, and the customer database. **Goals:** - Achieve 100% ticketing for all interactions. - Track and measure issue resolution times (SLAs). - Identify bottlenecks and common problems. - Prevent any customer issue from being overlooked. The Workflows that need to be enabled - Grouping of users - Page-nation for the pending and completed application The Filter for the lead stage to be added Add filters in the pending application User stories - Customer will call us - customer is routed to a agent - How is this routing setup? - Agent takes notes on the call - Dispostion

---

## #138 — Post loan Status APIs for MFD SaaS Partner Platfor
**Status:** Done | **Last edited:** February 14, 2025 12:59 PM

# Post loan Status APIs for MFD SaaS Partner Platform. Shortfall, Interest, Renewal # Product Requirements Document (PRD) [API doc ](Post%20loan%20Status%20APIs%20for%20MFD%20SaaS%20Partner%20Platfor/API%20doc%20198e8d3af13a80b995eecf251432a056.md) ## **Project Title:** **Development of External APIs for MFD Dashboard Integration** --- ## **1. Introduction** This document outlines the requirements for developing a set of External APIs intended for MFD platforms like redvision. These APIs will enable MFD partners to integrate with our system, allowing them to create comprehensive dashboards that provide essential customer data and financial metrics. The goal is to facilitate seamless data exchange, enhancing the operational efficiency and decision-making capabilities of our MFD partners --- ## **2. Objective** To develop a suite of External APIs that replicate the functionalities of existing Internal APIs, providing MFD platforms with secure and efficient access to customer data related to active customers, shortfalls, interest dues, and renewals. These APIs will empower MFD partners to build detailed dashboards, enabling better management and support of their customer base. --- ## **3. Target Audience** - **Primary Users:** - **MFD Platform Developers:** Responsible for integrating the External APIs into their dashboards. - **MFD Operations Teams:** Utilize the dashboards for monitoring and managing customer data. - **Stakeholders:** - **Product Management Team** - **Development Team** - QA - **MFD SAAS Partners** --- ## **4. Scope** ### **In-Scope:** - Development of four External APIs: 1. **Get Active Customers** 2. **Get Shortfall Details** 3. **Get Interest Due Details** 4. **Get Renewal Details** - Documentation and specifications for each API. - Implementation of business logic within each API. - Security measures for data protection. ### **Out-of-Scope:** - Development of UI components for MFD dashboards. - Integration of common headers and authentication mechanisms (handled separately). --- ## **5. API Specifications** ### **5.1. Get Active Customers** ### **Endpoint:** ``` GET /v1/partner/platform/las/partner/{partnerAccountId}/activeCustomers?pageNumber={pageNumber} ``` ### **Description:** Retrieves a paginated list of active customers associated with a specific partner account. This API provides detailed customer information, including credit details and pledged portfolio items, enabling MFD partners to manage and support their active clientele effectively. ### **Parameters:** - **Path Parameters:** - `partnerAccountId` (string, **required**): Unique identifier for the partner account. - **Query Parameters:** - `pageNumber` (integer, **optional**, default: 1): The page number to retrieve. ### **Response Payload:** ```json { "activeCustomerDetails": [ { "mobileNumber": "+919876501234", "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "email": "dummy@voltmoney.in", "pan": "AUWPA7175L", "dob": "30-03-1988", "creditDetails": { "voltCustomerCode": "E16433AFAE80FAE2404FDCFE8BDE40D7", "creditType": "OVERDRAFT", "lenderCreditId": "9911725722", "lenderName": "Bajaj", "totalCreditAmount": 332300, "availableCreditAmount": 282300, "principalOutStandingAmount": 50000, "currentApplicableInterestRate": 9.95, "pledgedPortfolioAmount": 738723, "overUtilizationAmount": 0, "chargesDueAmount":

---

## #139 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #140 — Pledged portfolio API (KFIN)
**Status:** Done | **Last edited:** February 1, 2025 1:21 PM

# Pledged portfolio API (KFIN) ### **Purpose** The API enables a lender to request detailed information about an investor's mutual fund folios that are pledged as collateral. It provides insights into folio numbers, pledged units, ISINs, and related details. --- ### **Request Method** **POST** `/PortfolioRequest` --- ### **Request Headers** | **Name** | **Type** | **Description** | **Default Value** | | --- | --- | --- | --- | | `CLIENT` | string (header) | Client Header | XXXXXX | | `CLIENT-ID` | string (header) | Client ID Header | XXXX | | `CLIENT-SECRET` | string (header) | Client Secret Header | XXX | | `Content-Type` | string (header) | Content Type | application/json | --- ### **Request Body** The body accepts a JSON object containing: ```json json Copy code { "PortfolioRequest": { "InvPan": "ABC123", // Investor PAN "RequestID": "123", // Unique Request ID "AgentCode": "ABC123" // Agent Code } } ``` --- ### **Response** ### **Success (Code: 0)** Returns detailed data for pledged mutual fund units. Example: ```json json Copy code { "Dtinformation": [ { "Return_Code": 0, "Return_Msg": "Success" } ], "DtData": [ { "RequestID": "123", "InvestorPAN": "ABC123", "InvestorName": "ABC", "FolioNo": "123", "ISIN": "ABC123", "LienMarkedUnits": 0.1, "CurrentNAV": 0.1, "CurrentValue": "0", ... } ] } ``` ### **Failure (Code: -100)** Returns a message if the data does not exist. Example: ```json json Copy code { "Dtinformation": [ { "Return_Code": 0, "Return_Msg": "Data Does not exist" } ] } ``` --- ### **Key Features** - **Parameters:** Accepts investor PAN, request ID, and agent code. - **Output Details:** Comprehensive folio and pledged unit details like: - Folio number - Pledged units and amount - NAV and current value - Investor and lender information - **Error Handling:** Indicates when no data is found. This API is primarily intended for lenders to access mutual fund collateral data securely and efficiently.

---

## #141 — Attribution for Volt applications
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

## #142 — MFC Pledge error handling - V1
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

## #143 — Reducing Limit on DSP from 25K
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

## #144 — Volt LOS journey optimisations
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

## #145 — Update user details (for TCL, BFL, DSP)
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

## #147 — Un-pledge optimisations
**Status:** In progress | **Last edited:** December 3, 2024 3:13 PM

**Problem:**
are we solving?**

For BFL users, who make a withdrawal request of complete available amount while an un-pledge request is in-progress then the withdrawal requests gets processed first and un-pledge request gets rejected due to update in the value of net-payable due to the withdrawal processing  

---

**Solution:**
?**

When user is making a withdrawal is making a withdrawal while an un-pledge request is in “In progress” we will give a heads-up to the user that the withdrawal request might interfere with the un-pledge request if the outstanding is not zero. [This change only needs to be done for BFL]

---

## #148 — Show accrued interest on UI
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

## #150 — Test campaign for MFDs
**Status:** Not started | **Last edited:** December 25, 2024 10:43 AM

# Test campaign for MFDs # Re-engagement Campaign Message Templates 1. **Segment Definition:** - Create 3 segments based on time since empanelment: [https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1G_4aPZn5m2YpGtMWaAKz5kGLTVihWlO0Ls7XnhO9XYs/edit?usp=sharing) - Recent (0-30 days): 807 partners - Mid-term (31-90 days): 1,244 partners - Long-term (90+ days): 9,763 partners 1. **Experiment Design:** - Split each segment into 3 groups: - Control Group (20%) - Treatment Group A (40%): Personalized WhatsApp/SMS - Treatment Group B (40%): WhatsApp/SMS + Email follow-up 1. **Intervention Plan:** - Treatment A: - Day 1: Initial WhatsApp message with personalized activation link - Day 3: SMS reminder with key benefits - Day 7: Final WhatsApp message with time-limited incentive - Treatment B: - Day 1: WhatsApp message + Email with detailed activation guide - Day 3: SMS reminder + Email success stories - Day 7: Final WhatsApp + Email with time-limited incentive # Re-engagement Campaign Message Templates ## Recent Partners (0-30 days) ### Treatment A (WhatsApp/SMS Only) **Day 1 - WhatsApp:** ``` Hi {partner_name}, Help your clients keep their investments growing! 📈 With Volt Money, your clients can: • Get instant credit against MF holdings • Access funds in just 5 minutes • Keep their investment journey uninterrupted Try it now: {partner_dashboard_link} Need help? Chat with us Mon-Sat (9:30 AM - 8 PM) ``` **Day 3 - SMS:** ``` {partner_name}, stop redemptions today! Your clients can get credit against MFs in 5 mins while keeping their investments intact. 2000+ partners trust Volt Money. Start here: {partner_dashboard_link} ``` **Day 7 - WhatsApp:** ``` Hi {partner_name}, Your clients need quick funds? Help them avoid redemption with Volt Money! ✨ Special offer: Extra 5% commission on your first 5 client referrals Get started: {partner_dashboard_link} Questions? We're here to help! ``` ### Treatment B (WhatsApp/SMS + Email) **Day 1 - Email:** Subject: Stop Client Redemptions with Instant Credit Solutions ``` Dear {partner_name}, Are your clients considering redemption for short-term needs? Volt Money has a better way! Help Your Clients: 1. Keep Their Investments Growing 2. Get Credit in 5 Minutes 3. Meet Urgent Cash Needs 4. Stay on Track for Long-term Goals Join 2000+ partners who are helping clients preserve their wealth. Try It Today: 1. Visit your dashboard: {partner_dashboard_link} 2. Share with your first client 3. Watch their portfolio stay intact Our expert team is available Monday through Saturday (9:30 AM - 8 PM) to assist you. Best regards, Team Volt Money ``` ## Mid-term Partners (31-90 days)

---

## #151 — [Platform] Risk report
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

## #152 — MF Fetch optimizations
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

## #153 — Lead stage handling on LSQ
**Status:** Not started | **Last edited:** December 13, 2024 11:58 AM

# Lead stage handling on LSQ Lead stages in LSQ Initial Registration Stages: 1. Unregistered 2. Registered Portfolio Stages: 3. Portfolio Fetch 4. Portfolio Fetch KFIN 5. Portfolio Fetch CAMS 6. Portfolio Pledge 7. Portfolio Pledge KFIN 8. Portfolio Pledge CAMS Application Processing Stages: 9. KYC Verification 10. Sign Agreement 11. Link bank account 12. Setup Mandate 13. Verify Photo 14. Application Submitted 15. Loan Created 16. Empaneled Final Status Stages: 17. Partially activated 18. Activated 19. Closed

---

## #154 — Un-pledging bug fixes & UI optimisation
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

## #155 — SL updation & additional limit calculation optimis
**Status:** On Hold | **Last edited:** August 27, 2024 5:20 PM

**Problem:**
are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

**Solution:**
?**

---

## #156 — [Platform] RTA portfolio API integration
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

## #157 — [DSP] Dues collection comms
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

## #158 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #159 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #160 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #161 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #162 — Lien removal buffer enhancement (Note)
**Status:** Not started | **Last edited:** August 10, 2024 3:51 PM

# Lien removal buffer enhancement (Note) [Bajaj buffer handling for lien removal](https://app.notion.com/p/Bajaj-buffer-handling-for-lien-removal-90fa191a67ec4f38b2bff1cfe6d99a98?pvs=21) For Bajaj, we had placed a buffer of 5% on total outstanding when users raise collateral removal requests to handle NAV changes. Collateral removal requests take 1-2 working days to be processed by the lender and hence to ensure requests are not cancelled this buffer is maintained. Due to high volatility in markets our requests are still getting rejected despite the 5% buffer. We need to solve for the cancellations. One proposed method by the business team is to increase the buffer to 10% however that impacts customer experience. Need solutioning for the same.

---

## #163 — [Platform] Validation to Stop Un-pledging, closure
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

## #164 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #165 — MNRL Compliance Validation Integration
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

## #166 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #167 — VKYC Integration PRD
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

## #168 — MFD - Removing google SSO from PLJ
**Status:** Ready for Tech | **Last edited:** April 22, 2025 10:53 AM

# MFD - Removing google SSO from PLJ Problem statement 1. The **Email field is not Pre-filled** even when the MFD has already fetched the MFC for the client. 2. **Email verification via Google SSO** doesn’t work well for the MFD channel—Google pulls the MFD's email from the device instead of the client’s. ![Screenshot 2025-04-11 at 1.31.35 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.35_PM.png) - MFDs often manually enter their email in the **“Continue with other email”** option, leading to operational effort to remove the Email. ![Screenshot 2025-04-11 at 1.31.44 PM.png](MFD%20-%20Removing%20google%20SSO%20from%20PLJ/Screenshot_2025-04-11_at_1.31.44_PM.png) ## **Proposed Solution:** **After customer registration (Name + Mobile Number + OTP):** 1. The MFD lands on the **Customer Registered** screen. 2. The screen gives two options: - Learn how to **create an application** on the Partner Portal, or - **Share a link** with the customer. 3. If the MFD chooses **“Continue creating customer application”**: - The flow will continue to the next application journey step skipping the App homepage as the intended action at this step is to complete the application. - The Data like Email ID and Fetched portfolio will be Pre-filled if the MFC has been previously fetched for the customer - If the MFD needs to access the App home page then they can go back on the application process using the top ← arrow on the top left. Text changes on the verify Email step ” The provided email will be used by lenders as the Client’s registered Email for all communications “ ### Key Changes from the Current Flow 1. **Skip the email selector page** — go directly to the “Add Email” screen. 2. **Show the client’s name** clearly to ensure the email being entered is for the right person. 3. **Include a note** saying the email will be used by lenders for important updates. 4. **Update the header** to: “Add client’s email.” 5. **Streamline the journey** by removing extra steps and taking MFDs directly to the email input screen.

---

## #169 — CKYC Comms for Regulatory Compliance
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

## #170 — Untitled
**Status:** Not started | **Last edited:** April 17, 2025 11:42 AM

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #171 — Unpledge and Disbursement Enhancement
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

## #172 — KYC & Mandate Workflow PRD
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

## #173 — Admin tool migration to Appsmith
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

## #174 — Check eligibility overhaul
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

## #175 — UX Writing for Indian Fintech Users (Volt) – Resea
**Status:** Unknown | **Last edited:** Unknown

# UX Writing for Indian Fintech Users (Volt) – Research & Guidelines # Introduction Designing a UX writing system requires a deep understanding of **local users**, **financial regulations**, and **effective copy practices**. Every label, message, and CTA must inspire confidence and clarity, since <aside> 💡 > *Fintech content design and UX writing is all about building user trust, and it couldn’t matter more when we’re dealing with people’s money.* https://uxcontent.com/ux-writing-in-the-fintech-industry/#:~:text=Fintech%20content%20design%20and%20UX,we%E2%80%99re%20dealing%20with%20people%E2%80%99s%20money > </aside> ## Understanding the Indian Fintech User ### **Trust is paramount** Indian users, especially first-time investors and borrowers, tend to be cautious with new financial services. <aside> 💡 A McKinsey report found that *trust is the primary factor influencing customer adoption and engagement with fintech services* [thence.co](https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=User%20confidence%20is%20the%20degree,and%20engagement%20with%20fintech%20services) </aside> Users need to feel their money and data are safe. UX copy should therefore reassure at every step (e.g. using phrases like “securely powered by XYZ bank” or highlighting RBI oversight) to strengthen this trust foundation. ### **Broad, diverse audience** Volt’s target users include salaried professionals investing in mutual funds, stocks, insurance, bonds, etc. Many are financially savvy to an extent, but there’s a **wide range of literacy** Some may be first-time investors from Tier-2 cities (as seen with apps like Groww), while others are seasoned market participants. Copy must hit a sweet spot where **both novices and experts can understand it easily** <aside> 💡 As one UX guide advises, F*intech UX should prioritize clear, simple language that can be easily understood by both newbies and experts alike* https://www.thence.co/blogs/building-trust-in-fintech-ux-key-psychological-factors-for-user-confidence#:~:text=Problem%3A%20The%20financial%20language%20can,to%20understand%20for%20many%20users </aside> This means avoiding heavy jargon and explaining necessary terms in plain language. For example, instead of “lien marking your mutual fund units,” Volt’s app explains it as *“mark your mutual funds as a security with a trusted lender”* immediately clarifying the action. ### Friendly, guiding tone A friendly tone humanizes complex financial tasks – it’s like having a helpful friend explain things rather than a formal banker. However, the tone should also reflect **professionalism** to build credibility; a balance of *professional yet approachable* works well, as Razorpay’s content team describes: their fintech UX writing maintains a *“consistent tone – professional yet approachable”* to serve users dealing with high-stakes transactions ### Attention span and mobile behaviour Remember that Indian users predominantly access fintech services on mobile (Volt is **mobile-first**, as noted). Mobile users skim and scan due to small screens and on-the-go usage. Studies show people read only ~20–28% of text on

---

## #176 — Volt Plugin Knowledge Base
**Status:** Unknown | **Last edited:** Unknown

# Volt Plugin Knowledge Base # Introduction This project aims to build a unified UX writing system for Volt based on fintech best practices. The goal is to have a unified, brand-aligned tone of voice across screens, touchpoints, and teams. ## Problem - Right now we handle error case copies differently throughout the app. - Different writers/designers use different tones, leading to a fragmented experience. - No shared rules for writing error messages, CTAs, success screens, etc. - Designers or PMs often write placeholder text or inconsistent copy due to lack of writing support & time constraints. ## Solution A self-serve figma plugin where anyone can write first version of the copy that’s on-brand, on-tone, and compliant without needing support ## Approach - Align stakeholders on a unified brand voice - Setup brand voice guidlines (Tone) for cases like success, error, New features and so on. - Present guidelines that will be used as the first config for the figma app - Create the figma plugin with the help of Devs - Present a working model, to stakeholders - Take feedback and iterate if necessary - Replace copy throughout app using the figma plugin ## Brand Voice Based on the conversation with Lalit this is what volt stands for. based on these I want to define what the tone of language we want through out the app. - Call with Lalit on volt brand 1. If volt was a person how would you describe it? 1. Supportive 2. Reliable and Fast to help 3. Motivating 4. Enabler to achieve your financial needs 5. A saviour when you need most 2. Describe Volt in 3-4 words 1. Transparent, Trustworthy, Easy, Fast <aside> 💡 **Interacting with Volt should feel like:** Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless. - **Like a smart, supportive money guide** - **Your effortless, goal-driven money companion** </aside> Voice: **Smart, Supportive, Calm, and Clear.** <aside> 💡 Volt speaks like a modern financial guide — someone who knows money inside out, and explains it with warmth & clarity, not jargon. </aside> ## Scenarios / Possible Usecases - Error like PAN verification failed, No CKYC data found and so on - Success like Completion of Payment, Loan application, Increase limit and so on - Onboarding like App screenshots

---

## #177 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #178 — Lodgement Enhancement
**Status:** Deprioritised | **Last edited:** Unknown

# Lodgement Enhancement Assign: Karuna Sankolli Charter: NBFC Pod Task type: Sprint # Context [[Platform] RTA portfolio API integration](../PRDs/PRDs/%5BPlatform%5D%20RTA%20portfolio%20API%20integration%20166e8d3af13a80a7a325c550ed9f8c04.md) # Design - [ ] Partial approval component - [ ] Button sizes Ops https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2431-157171&t=wnkdjY7E7DaaJvbj-11

---

## #179 — Lodgement addition and removal maker
**Status:** Ready for kickoff | **Last edited:** Unknown

# Lodgement addition and removal maker Assign: Karuna Sankolli Charter: NBFC Pod Task type: Sprint # Context [https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469](https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469) **MOM** 1. Discovery you can maker for lodgement 2. Upload 3. Review 1. Dedupe check -> Already lodegd or not 2. Pledge check -> Pledged with the LSP 4. Data points 1. Folio 2. Loan acct number -Future 3. PAN number 4. Investor name 5. Units 6. Scheme name 7. Lien ref number CAMs 8. IHNO Kfintech 9. ISIN 10. Status 11. Remarks 5. Do I want to ops to work on the file, RTA level 6. Grouping based on PAN & Loan acct number # Figma [https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system)

---

## #180 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #181 — APIs
**Status:** ** Retrieves the status of the KYC verification. | **Last edited:** Unknown

# APIs **Explanation of the API Sequence in the Volt Money Application Flow** Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience. --- ### **Overview** The Volt Money application process involves several key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail. --- ### **1. Login** - **API Used:** *Custom Authentication API (Not listed in the provided APIs)* - **Functionality:** - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone. - **Notes:** - This step establishes a secure session for the user. - While not specified in the provided API list, we use a standard authentication service to handle this process. --- ### **2. PAN Verification** - **API Used:** - `POST /app/borrower/application/kyc/pan/panVerify` - **Partner:** Decentro (facilitates connection to NSDL) - **Functionality:** - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid. - **Data Retrieval:** Fetches the full name associated with the PAN. - **Notes:** - Essential for KYC compliance and identity verification. - Helps prevent fraudulent applications. --- ### **3. Fetch Folio** - **APIs Used:** - `POST /app/borrower/application/fetch/init/otp/v3` - `POST /app/borrower/application/fetch/authCAS/v2` - **Partners:** Cams, KFintech, MF Central - **Functionality:** - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio. - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details. - **Notes:** - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets. - This data is used later in the asset pledge and eligibility assessment. --- ### **4. Eligibility Assessment and Lender Assignment** - **API Used:** - `POST /app/borrower/application/credit/profile/evaluate` - **Partner:** Internal Business Rule Engine (BRE) - **Functionality:** - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria. - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based

---

## #182 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #183 — flows api
**Status:** Unknown | **Last edited:** Unknown

# flows api 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** 1. **Fetch Folio-** 2. **Eligibility Assessment and Lender Assignment** 3. **KYC Verification** 4. **Bank Account Verification** 5. **Mandate Setting** 6. **Asset Pledge** 7. **KFS and Documentation** 8. **Loan Agreement Execution**

---

## #184 — LaMF application journey
**Status:** Unknown | **Last edited:** Unknown

# LaMF application journey [APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md) [API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md) [flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md) [Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md) The journey to create a loan against mf is as follows - login - user logs in using mobile number and otp validation - PAN verification - user enter DOB and PAN to validate pan , API - decentro - Fetch folio - we ping Cams/KFin to get the folio for the user - We ping them manually - we have option of gettign both from MF central - One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists - Folio have ISIN , NAV etc details - We assign the customer basis BRE to either Bajaj ot TATA capital - KYC of the customer aadhar - API is diifetent for tata and bajaj - Bank account verification - Mandate setting - Logement - KFS and docuemnttation Support I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table. [Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv) | Step | improvements | Description | Partner/Service | API Name | | | --- | --- | --- | --- | --- | --- | | Login | | User logs in using mobile number and OTP validation | | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) | | | Verify OTP | | | | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/ | | | user details | | | | https://api.staging.voltmoney.in/app/borrower/user | | | Email verification | | | Google sso | https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com | | | | | | Email / manual | | | | | | | | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) | | | | | | | | | | PAN Verification | | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API | | | Fetch Folio | | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API | | | Run BRE and Calculate Eligible Limits | | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system | | | | Assign Lender | | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system | | | | KYC Verification | | KYC of the customer with different APIs for Bajaj and TATA Capital

---

## #185 — MFD Application Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Application Journey MFD or mutual fund distributors are the B2b2c channel for the Volt money there three parts of a MFD journey Sourcing - We source MFDs from events, sales agents , word of mouth , etc. - Once we get them on the dashboard we call it onbaording - Ashik is reponsible for getting MFD onbaorded Activation - we assign RMs to MFD to provide them relationship support to them to start onbaording clients - 1 rm~400 MFD mapped to them - Activation require MFD to create at least one Active credit line with us - We help through any blocker they might have support - there are list of supportt activities post loan that a customer can request - Payouts to MFDs -

---

## #186 — flow
**Status:** Unknown | **Last edited:** Unknown

# flow **User Journey Map for a Loan Against Mutual Funds Application** This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer). --- ### **1. User Acquisition and Onboarding** ### **1.1. Launching the App** - **FE Snippet:** - *Splash Screen > Launch App* ### **1.2. User Signup** - **FE Snippets:** - *Signup > View Signup Page* - *Signup > Click T&C or Privacy Policy* - *Signup > Edit Phone Number* - *Signup > Navigate to OTP Page* - *Signup > Resend OTP* - *Signup > Enter Invalid OTP* - *Signup > Complete Signup* - *Signup > View Verify Email Page* - *Signup > Verify Email with Google* - *Signup > Verify Email with Other Method* - *Signup > View Enter Email Page* - *Signup > Email Verification Result* - **BE Events:** - *Backend Events > OTP > Trigger OTP* - *Backend Events > OTP > Verify OTP* - *Backend Events > User Management > Create user context* - *Backend Events > User Management > Update user email* --- ### **2. Eligibility and Limit Check** ### **2.1. PAN Verification** - **FE Snippets:** - *Cash Limit > Enter PAN* - *Cash Limit > Verify PAN* - *Cash Limit > PAN Verification* - *Cash Limit > Edit PAN Details* - *Cash Limit > Confirm PAN Details* - **BE Events:** - *PAN Verification > Initiate PAN verification* - *PAN Verification > Complete PAN verification* - *PAN Verification > PAN verification failed* ### **2.2. Eligibility Check** - **FE Snippets:** - *Cash Limit > Trigger Eligibility Check* - *Cash Limit > Eligibility Check Result* - *Cash Limit > Application Under Review* - *Cash Limit > Application Rejected* - **BE Events:** - *Credit Application > Create credit application* - *Credit Approval Request > Receive credit approval request* - *Credit Approval Request > FAS creates the request* - *Credit Approval Request > LAN generation successful* - *Credit Approval Request > LAN generation failed* --- ### **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** - **FE Snippets:** - *Cash Limit > View Check Limit Page* - *Cash Limit > Edit Details on Check Limit Sheet* - *Cash Limit > Update Portfolio Source* - *Cash

---

## #187 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #188 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #189 — Handling Discrepancies Between Assumed and Actual
**Status:** Unknown | **Last edited:** Unknown

# Handling Discrepancies Between Assumed and Actual Limits In our **Loan Against Mutual Funds (MF)** process, we allow users to act based on certain limits displayed on their dashboard throughout the loan journey. These limits are meant to provide a smooth and consistent experience, ensuring users feel confident as they proceed with their loan requests. Two key terms we deal with are the **Drawing Power (DP)** and the **sanction limit**. • **Drawing Power (DP)** is the theoretical maximum amount a user can borrow, based on factors like the NAV, unit price, and LTV of their pledged mutual funds. • **Sanction Limit** is the actual borrowing limit we allow users to access through the platform. We calculate these limits based on the **assumed DP and sanction limit** derived from the formulas and approved lists shared with us by our lending partners. However, in the actual loan processing, the **lender retains the final rights** to determine both the **DP and sanction limit**, since they are the ones disbursing the loan amount. This means that the **assumed DP** and **sanction limit** we show to the user may differ from the **final limits** confirmed by the lender after their internal checks and approvals. In certain cases, there can be discrepancies. For example, the lender may adjust the list of approved mutual fund units or change the loan-to-value (LTV) ratio during the final review, leading to a lower **DP** or **sanction limit** than what was originally calculated. As a result, a user may initiate a withdrawal request based on the higher, **assumed limit**, but it can get **rejected** once the lender processes the loan and confirms the lower final limits. To handle these situations, we notify the user if their **withdrawal request exceeds the final approved limits**. The system will automatically **error handle the request** and inform the user of the discrepancy. We will also guide the user to **submit a new withdrawal request** that falls within the actual, lender-approved DP or sanction limit, ensuring that they can successfully access their funds without further delays or confusion. While these discrepancies can happen due to changes in the lender’s processing, our goal is to keep users informed and ensure that they can quickly adjust their requests to align with the actual limits approved by the lender. This approach minimizes user frustration and maintains transparency throughout the loan process.

---

## #190 — OP - Selloff and Withdrawal request mismatch
**Status:** Unknown | **Last edited:** Unknown

# OP - Selloff and Withdrawal request mismatch We provide loans against pledged Mutual Funds (MFs), offering customers a credit limit based on the Loan-to-Value (LTV) ratio of their pledged funds. Typically, if a customer pledges Rs. 200,000 worth of MFs at an LTV of 0.5, they receive a credit limit of Rs. 100,000. The process works seamlessly until the customer initiates a selloff request for part of their pledged funds. The challenge arises when a customer requests to sell off a portion of their pledged funds—let’s say Rs. 50,000. This should reduce both the pledged amount and the available credit limit accordingly. However, the process of completing the selloff and reducing the lien on the pledged amount is currently manual and takes time, as it is handled via email or WhatsApp. During this period, the customer still sees their original credit limit in the app, which can lead to issues. The core problem here is not simply a delay in syncing data, but rather the risk of **conflicting requests**. While the selloff is being processed, the customer may attempt to raise a withdrawal request based on their old credit limit, which is no longer valid. By the time this request reaches the lender, the selloff has reduced the customer’s available limit, and the withdrawal request fails because it exceeds the updated limit. To prevent this, we need to ensure that the system doesn’t allow contradictory actions during this process. **Customers should not be able to submit a withdrawal request while a selloff request is still being processed.** ### **Proposed Solution:** The solution is straightforward: the system should block the customer from raising any withdrawal requests while the selloff is in progress. This ensures that the customer cannot make a request based on an outdated credit limit that will result in a failed transaction. By preventing contradictory requests, we create a more efficient process that reduces frustration and enhances the customer experience. During the manual processing of the selloff, we can also empower our operations team to **manually adjust the customer’s credit limit** in the system. This proactive step ensures the app reflects the anticipated reduction in the limit, preventing the customer from attempting to withdraw more than they can. Once the selloff is finalized and confirmed by the lender, the system will restore the updated limit, ensuring that all future transactions are based on the correct, available credit. **New

---

## #191 — API flow for KFS and Agreement
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

## #192 — Additional details enhancement
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

## #193 — Analytics requirement for amortisation of PF
**Status:** Pending review | **Last edited:** Unknown

# Analytics requirement for amortisation of PF Last Edited: April 24, 2026 8:59 AM PRD ETA: April 24, 2026 PRD Owner: Vaibhav Arora # **1. Objective** Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module. The design must be extensible to accommodate other fee/cost types in future iterations without structural rework. # **2. Scope & Exclusions** ## **2.1 In Scope** - Product lines: LAMF, LAS, Term Loan (TL) - Charge type: Processing Fee (PF) - Accounting entries: Income recognition at monthly amortisation level - Amortisation method: Straight Line Method (SLM) - Report period: M-N (N>0) (previous calendar months only) - Waiver handling: Partial and complete waivers with corresponding reverse entries - Loan closure handling: Remaining balance acceleration on closure date ## **2.2 Explicitly Out of Scope** - GST component of processing fee excluded from amortisation entries - Current month entries - report is strictly retrospective - Real-time or intra-month amortisation schedules # **3. Source Data & Key Fields** All data will be sourced from the accounting report. The following fields are required at a schedule/charge level: | **Field** | **Source / Table** | **Notes** | | --- | --- | --- | | FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier | | Client External ID | LMS – Loan Master | FXCID reference | | Product Type | LMS – Loan Master | LAMF / LAS / TL | | Charge Application Date | LMS – Fee Schedule | Date PF was applied | | PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only | | Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference | | Loan Status | LMS – Loan Master | Active / Closed | | Closure Date | LMS – Loan Master | Populated only if loan is closed | | Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator | | Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee | | Waiver Date | LMS – Waiver Log | Date waiver was applied | | Waiver Type | LMS – Waiver Log | Partial /

---

## #194 — Approved Scrips productisation
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
We are solving for:

- A governed, audited maker-checker flow for all approved scrip updates in Command Centre
- Support for the following scrip operations via this flow:
    - **Approve new ISIN** — add a new ISIN (Mutual fund or Share) to the approved scrip with all required parameters
    - **Stop new lodgements** — set min LTV to zero for an ISIN (blocks new pledges without impacting existing 

# Approved Scrips productisation Last Edited: May 8, 2026 12:03 PM PRD ETA: April 21, 2026 PRD Owner: Vaibhav Arora ## Background and Context The approved scrip list is the master reference that controls which ISINs can be pledged as collateral in the LMS, and at what LTV. It has two layers: - **Finflux approved scrip** — Global NBFC-level list managed in the LMS (Finflux). Stores min LTV and max LTV per ISIN and enforces that no lodged collateral exceeds max LTV. (Min LTV for default LTV value, Max LTV as a ceiling validation) - Finflux max LTV should be equal to Risk LTV and Finflux min LTV should be equal to Fenix min LTV - **Fenix approved scrip** — Internal list managed at a co-lender relationship (contract) level (colending vs non-colending) and product level (LAS and LAMF). Fenix carries three LTV values per ISIN: Regulatory LTV (= max LTV), Risk LTV (internal ceiling set by the risk team, ≤ Regulatory LTV), and Min LTV. Today, updates to both scrips require manually calling APIs in Fenix and Finflux separately. This is done by anyone with API access and without any audit trail, approval gate, or role-based control. **Who is affected:** - Risk ops team (makers) who need to update scrips frequently but have no safe, governed tool to do so - Risk managers (checkers) who have no visibility into what changed, when, and by whom - End users and LSPs who are indirectly impacted by incorrect LTV values (inflated or deflated offers, wrong shortfall calculations) **What is broken today:** - Fenix and Finflux scrips are updated separately and can fall out of sync — they should be updated atomically - Direct API updates are error-prone. A documented past incident set LTVs to 50 instead of 50% causing 100x limit inflation - No audit log exists for scrip changes — there is no way to trace who changed what and when - No role-based control — anyone with API access can make changes with immediate live impact on offer generation and shortfall computation **Why it matters now — three upcoming catalysts:** 1. **Colending expansion** — More colending relationships mean more contract-level approved scrip variants, increasing change frequency 2. **LTV increase to 70%** — Moving from 45% to 70% introduces higher risk volatility and requires more frequent scrip tuning by the risk team 3. **Loan against Shares launch** — Shares are more

---

## #195 — Charge details on Command centre
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

## #196 — Corporate action - Data feed
**Status:** Completed | **Last edited:** Unknown

# Corporate action - Data feed Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # Corporate Actions Data Feed ## Overview To support monitoring of securities pledged as collateral, we have reviewed a **Corporate Actions data feed sourced from BSE end-of-day bulletins**. This feed provides information on **events and disclosures that may impact the value, structure, or tradability of securities**. The data is consumed daily and can be used by the Risk team to monitor portfolio changes and identify events that may require action. The data covers the following broad categories: - Corporate action events - Company structural changes - Market disclosures - Large market transactions - Insider activity - Liquidity indicators --- # 1. Corporate Action Events This dataset contains information about **corporate actions declared by listed companies** that may affect the number of shares, price, or entitlement of shareholders. Typical corporate actions include: - Dividends - Stock splits - Bonus issues - Rights issues - Buybacks - Capital restructuring events For each event, the feed provides key reference dates such as: - **Record Date** – Date used to determine shareholder eligibility - **Ex-Date** – Date after which the security trades without the entitlement - **Cum Date** – Date before which investors must hold shares to be eligible - **Effective Dates** – Time period during which the action is applicable In addition, where applicable, the feed also provides: - Dividend amount or payout value - Share conversion ratios (e.g., split or bonus ratios) - Share quantity adjustments - Offer price or premium for rights issues These events are critical for adjusting **collateral valuation and share quantities** in pledged portfolios. --- # 2. Corporate Action Classification A separate master dataset provides the **mapping of corporate action identifiers to the specific event type** (e.g., dividend, split, bonus). This allows systems to interpret the corporate action feed and determine the **nature of the event impacting a security.** ---

---

## #197 — Credit note PRD
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

## #198 — Finflux Product Setup for Co-Lending
**Status:** Completed | **Last edited:** Unknown

# Finflux Product Setup for Co-Lending Last Edited: March 19, 2026 9:44 PM PRD ETA: January 27, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context As part of the co-lending setup, loans are economically split between: - **10% exposure (CLA portion)** - **90% exposure (TCL)** - **100% loan representation** required for operational and accounting purposes Current state: - Finflux is running on a **single instance** supporting **OD and TL products** - All reporting, accounting, SMA/NPA tagging, and operational workflows are currently **instance-scoped** - Finflux manages collateral and exposure deduplication The setup needs to support: - Fast go-live - Clean accounting - Correct delinquency signaling to TCL - Minimal disruption to existing production flows --- ## 2. Problem Statement The co-lending structure introduces multiple complexities: - **Collateral deduplication risk** if multiple loans referencing the same securities exist in the same instance - **Client-level SMA/NPA contagion**, where delinquency in a small CLA exposure may impact unrelated production loans - **Accounting segregation** required across different exposure types - **Operational overhead** introduced by multiple Finflux instances - **Reporting and reconciliation complexity** across LMS, Finflux, and TCL --- ## 3. Design Options Considered ### Option A: Single Finflux Instance with Multiple Products - All co-lending loans (10% and 100%) reside in the same instance - Separation handled purely via product-level configurations **Challenges** - High risk of collateral dedupe conflicts - Client-level NPA impact across all loans - Heavy reliance on product-level filters across reporting and accounting - Higher regression risk for existing OD and TL products --- ### Option B: Multiple Finflux Instances for All Co-Lending Loans - Separate instances for 10% and 100% loans **Challenges** - Higher setup and maintenance effort - Configuration and version-sync risks - Increased reporting and reconciliation overhead - Multiple operational points of failure at launch --- ## 4. Final Recommendation (Chosen Approach) **Recommended Setup** - **10% co-lending loan (CLA exposure)** → Booked in the **existing Finflux instance** - **100% loan** → Booked in a **separate Finflux instance** - **90% exposure** → Booked in **TCL** This approach optimizes for **lower effort, faster go-live, and controlled risk**, while keeping core production flows isolated. --- ## 5. Rationale for the Recommendation ### 5.1 Faster Go-Live with Minimal Change Surface - Existing Finflux instance already supports: - Live products - Accounting - Reporting - Monitoring - Adding a **single CLA product (10%)** is significantly lower effort than: - Standing up and

---

## #199 — IFSC addition Account opening enhancement
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

## #200 — LAS CMS Confiscation and sale of securities
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

## #201 — LAS CMS Lodgement
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

## #202 — LAS CMS Unlodgement
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

## #203 — External integrations LOS and LMS
**Status:** Done | **Last edited:** Unknown

**Problem:**
are we solving?**

There is no dedicated system to centrally manage the lifecycle of collateral for Loan Against Securities (LAS). Currently, lien requests, revocations, and monitoring are either partially tracked in LMS or manually handled by operations. This leads to operational risk, poor scalability, and delayed exception handling.

---

**Solution:**
?**

Build a standalone CMS with tight integrations to both LOS and LMS. CMS will be the source of truth for lien status and collateral health, while LOS and LMS remain the system of record for application and loan lifecycle.

---

## #204 — PMR consumption SHCIL
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

## #205 — Sample PMR transactions
**Status:** Done | **Last edited:** Unknown

# Sample PMR transactions ## CDSL (Lien marking): Pledge marking | Date | BO ID | ISIN | ISIN Description | Pledged Quantity | Pledgee Name | Status | Pledge Type | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Confirmed | Margin | Pledge created successfully | ## CDSL (Lien revocation): Pledge closure | Date | BO ID | ISIN | ISIN Description | Closed Quantity | Pledgee Name | Status | Closure Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Released | 05-Jul-2025 | Pledge closed successfully | ### CDSL: (Lien invocation) | Date | BO ID | ISIN | ISIN Description | Invoked Quantity | Pledgee Name | Status | Invocation Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 07-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 50 | DSP Finance Pvt Ltd | Invoked | 07-Jul-2025 | Partial invocation triggered | ### NSDL (Lien marking): Pledge marking | Execution Date | Client ID | ISIN | ISIN Description | Pledged Quantity | Pledgee | Pledge Type | Margin Pledge | Status | Agreement No. | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Margin | Yes | Confirmed | AGMT-56789 | ### NSDL (Lien revocation) Pledge closure | Closure Date | Client ID | ISIN | ISIN Description | Closed Quantity | Pledgee | Status | Lock-In Reason | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Released | NA | Closure on user request | ### NSDL (Lien invocation) | Execution Date | Client ID | ISIN | ISIN Description | Invoked Quantity | Pledgee | Status | Remarks | | ---

---

## #206 — Untitled
**Status:** Not started | **Last edited:** Unknown

# Untitled Decription: Corporate actions: Swap pledged assets in scenarios of collateral management- Bonus (Add additional units basis pledge instruction number)- Stock split (Management of split ratio and corresponding unit management, in scenarios of ISIN change, update ISIN, and removal of old ISIN and blocking of ISINs across loans - Drawing power management)- Mergers - Demergers Status: Not started

---

## #207 — LAS Collateral management system
**Status:** Completed | **Last edited:** Unknown

# LAS: Collateral management system Last Edited: July 28, 2025 8:43 PM PRD ETA: June 27, 2025 PRD Owner: Vaibhav Arora # **What is CMS?** The Collateral Management System (CMS) will act as the central infrastructure for managing pledged shares for a Loan Against Shares (LAS) product. It will interface with the Loan Origination System (LOS), Loan Management System (LMS), and Depository Participant (DP) — SHCIL — to manage the full lifecycle of collateral from validation to lien marking, valuation, revocation, and reconciliation. It will also include risk management via real-time LTV monitoring, handling of corporate actions, and tools for operations teams. [CMS system architecture](https://claude.ai/public/artifacts/b5a68c3c-4705-4c9d-b34b-52a1d6bb8ec4) --- # Why do we need a CMS? A **Collateral Management System (CMS)** is essential for a **Loan Against Shares (LAS)** product because collateral (in the form of pledged shares) is **the core security** backing the loan. Without an automated, secure, and integrated system to manage this collateral, the business is exposed to **operational risk, financial risk, and regulatory gaps**. 1. Centralised tracking and management of collaterals: Currently all collaterals are managed by the LMS which makes it very risk prone: A CMS ensures each step is trackable, audit-logged, and consistent with external systems (DP/SHCIL) and internal ones (LMS/LOS). 2. CMS constantly monitors Loan-to-Value (LTV) ratios. If share prices fall, LTV breaches can be automatically flagged (exposure tracking), triggering margin calls or partial lien revocation. 3. Logic separation from LMS: CMS has a lot of collateral management intelligence which should be LMS agnostic, this will make our LMS very modular and easily replaceable since majority of the complexity of collateral management will be handled via CMS. --- # **How are others solving this problem?** The approach to collateral management for Loan Against Shares (LAS) varies widely across the lending ecosystem, largely depending on a company’s scale, tech maturity, and risk appetite. Broadly, solutions fall into two categories: ### 1. **Tightly Coupled CMS-LMS Systems (Usually Vendor-Provided)** Some lenders use **end-to-end lending platforms** where the CMS is embedded within the LMS — often provided by a third-party vendor. These platforms offer: - Pre-integrated lien workflows - Basic LTV tracking - Unified borrower and collateral view ### 2. **No CMS — Operations-Led Collateral Tracking** Most early-stage or mid-sized lenders operate without a dedicated CMS. Instead, they rely on: - Manual **ops processes** to initiate and track lien/revocation files - **Excel sheets or shared dashboards** to monitor pledged ISINs

---

## #208 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #209 — LMS Multiple sell off requests
**Status:** Completed | **Last edited:** Unknown

# LMS: Multiple sell off requests Last Edited: March 19, 2026 9:44 PM PRD ETA: January 16, 2026 PRD Owner: Vaibhav Arora ## 1. Background & Context In the current LAS / LAMF sell-off flow, the system allows **only one non-terminal sell-off request per loan** at any point in time. Operationally, this breaks in real-world scenarios where: - Sell-off is raised across **multiple funds** and one or more invocations **fail partially** at the RTA / AMC level - Failed invocations do not cover the **entire overdue or shortfall** - Ops is forced to raise **another sell-off request** while the earlier one is still in progress or stuck (Which is currently blocked by a validation that only one non terminal request is allowed). This leads to: - Manual workarounds by the engineering team to support the use case - Delays in curing shortfall / overdue - Risk of exposure breach if sell-off cannot be retriggered in time - Risk of incorrect updates by the engineering team --- ## 2. Problem Statement **Ops raises a sell-off request for multiple securities.** - Some invocations succeed - One or more invocations fail or get stuck (e.g. CAMS / KFIN issues) - Proceeds received are **insufficient to cover the shortfall** - System blocks Ops from raising another sell-off request due to an existing non-terminal request This creates a deadlock where: - Exposure remains unresolved - Ops cannot act despite legitimate need - Manual intervention becomes necessary --- ## 3. Current Sell-Off Flow (As-Is) 1. **Sell-off Initiation** - Ops raises sell-off via **Bulk Maker** at **collateral level** - Requests are consolidated at **loan level** - A single sell-off request is created per loan 2. **Blocking Logic** - Selected units are blocked in LMS - Blocked units stop contributing to **Drawing Power (DP)** 3. **Threshold Calculation** ``` AvailableThreshold= DP - POS - COS - IOS - Accrued Interest ``` - Blocking ensures: - No excess collateral release - No further disbursement beyond safe exposure 4. **Invocation Flow** - RTA APIs (CAMS / KFIN) invoked - RTAs pass requests to AMCs - AMC sells securities 5. **Settlement & Reconciliation** - Proceeds credited to NBFC bank account - Settlement TAT: 2–3 working days - Ops reconciles proceeds via bulk operation - Proceeds mapped to collateral sell-off requests - Amount posted to respective loan accounts in LMS --- ## 4. Key Issue in Current Design - System enforces **single non-terminal

---

## #210 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

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

## #212 — PPSL UPI mandate presentation
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

## #213 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #214 — Pincode addition Account opening enhancement
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

## #215 — Product Note LAS Customer Consent Capture
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

## #216 — Razorpay SDK enhancement for Colending
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

## #217 — Shortfall Enhancement
**Status:** Completed | **Last edited:** Unknown

**In scope:**
We are solving for six interconnected problems across the shortfall calculation engine:

**A. Fair ageing treatment and correct Exposure definition**
Decompose incremental shortfall into ΔDP and ΔExposure components. Apply ΔExposure recovery independently (FIFO) before any ΔDP worsening creates a new shortfall instance. Exposure throughout the system = POS + Interest Overdue.

**B. Daily shortfall

# Shortfall Enhancement Last Edited: May 6, 2026 2:55 PM PRD ETA: April 23, 2026 PRD Owner: Vaibhav Arora ## Background and Context Loan Against Mutual Funds (LAMF) and Loan Against Shares (LAS) are secured credit products where customers pledge securities as collateral. The Drawing Power (DP) — the maximum permissible loan amount — is a function of the market value of the pledged collateral after applying the applicable LTV. A shortfall arises when the customer's Exposure (Principal Outstanding + Interest Overdue) exceeds DP. Shortfall management is a critical risk control function. Today it is broken in several ways that affect borrowers, the operations team, and the business's risk posture. **Who is affected:** - Borrowers who act in good faith — making repayments or pledging additional collateral — are being penalised because their recovery actions are netted against same-day market movements, stripping them of the ageing benefit they earned - Operations team who manually approve shortfall communications every morning, creating a bottleneck that prevents borrowers from receiving timely notice before markets open - Risk team who have no automated early-warning on severe collateral deterioration until it is too late to act same-day - LSPs who cannot offer a good borrower experience because the shortfall API doesn't expose due dates or the full picture of shortfall types **What is broken today — six specific gaps:** 1. **Ageing is not fair to borrowers.** The incremental shortfall is computed as a single net figure mixing market movements (ΔDP) and customer actions (ΔExposure). A borrower who repays ₹1L on a day the market falls ₹1.2L gets zero ageing benefit — the repayment is silently absorbed. Data shows this is material: across accounts in shortfall, 12% of borrowers at ageing 1 made repayments, 7.8% at ageing 2, 8.6% at ageing 3 — these customers deserved ageing credit that the current logic denies them. 2. **Shortfall does not run on non-market days.** When T is a market holiday, the shortfall job skips T+1 entirely. Borrowers who repaid on the holiday stay in shortfall on the platform for an extra day even though their account is clean — a bad experience with no financial basis. 3. **Interest overdue is excluded from Exposure.** Current shortfall logic only uses Principal Outstanding. RBI regulations require Exposure to be POS + Interest Overdue. This means shortfall is understated today. 4. **No reliable NAV gate.** The shortfall job and the NAV update

---

## #218 — Term loan gaps
**Status:** Unknown | **Last edited:** Unknown

# Term loan gaps Last Edited: July 24, 2025 5:10 PM PRD Owner: Vaibhav Arora ### **Spend & Convert Enhancements** - Support for **flat PF (Processing Fee)** values in spend and convert requests. - Allow **knockoff remarks** to be passed in the spend and convert payload. - Support passing **different charge types** and **collecting multiple charges** in a single spend and convert request. --- ### 🧾 **Repayment Logic** - Enable both **loan-level and line-level repayments** to co-exist for term loans. - Mark **repayment at loan level** as a current **gap** in configuration. - Support **EMI-level repayments**. - Include **apportionment details** in the repayment response (internal checks needed). - Support **loan-level excess refunds**. - **Excess amounts**: - Should remain **parked** after due generation (do not auto-settle dues via FIFO). - At **line level**, should **increase available limit**. --- ### 🧮 **Due/Bill Generation** - Bills should be generated **independent of the due generation job**—on demand. --- ### 📆 **Schedule and Simulation** - Provide a **preview schedule API** without needing to create a line. - Enable **tranche-level simulation API** for a given date. - All **date fields** must be passed as **EPOCH timestamps**. --- ### 🧠 **Tagging & Status Configurations** - SMA tagging should be **configurable**. - **NPA to be tracked at client level**, while **SMA is tracked at loan level**. --- ### 📉 **Interest & Limit Management** - Support **interest rate updates** on loans. - **Limit replenishment** should only occur when the **underlying loan is fully closed**, whether via EMI or part-payment.

---

## #219 — Transaction Sequencing & Transaction Workflows for
**Status:** Completed | **Last edited:** Unknown

**In scope:**
This document defines the **transaction orchestration logic across all supported transaction types**.

Specifically it covers:

# Transaction Sequencing & Transaction Workflows for Co-Lending LMS Last Edited: March 19, 2026 9:44 PM PRD ETA: March 10, 2026 PRD Owner: Vaibhav Arora # Background and Context DSP Finance is implementing a **co-lending structure between DSP and TCL** where a single customer loan is operationally represented by **three loan accounts inside the LMS**. The loan accounts are structured as follows: - **Loan 100** → Customer facing orchestration loan (Finflux) - **Loan 90** → TCL lender loan (Swiffy LMS) - **Loan 10** → DSP lender loan (Finflux) All **customer-facing interactions and repayments occur on Loan 100**, while lender accounting and settlement must be reflected in the **individual lender loan books**. This PRD introduces the need for **systematic orchestration across multiple loan books** to ensure: - lender accounting reconciliation - schedule consistency - correct split of repayments - ransaction ordering - correct DP (Drawing Power) management --- ### Transaction Categories The system processes two categories of transactions. --- ## Money Transactions These impact loan balances or receivables. Examples: - Disbursement - Repayment - Refund / Disbursement reversal - Charge application - Charge knock off - Interest posting - Credit note adjustments - Waivers - Excess payment handling - Excess refunds - Clear dues transactions --- ## Collateral Transactions These impact collateral and **DP calculations**. Examples: - Add collateral - Remove collateral - Sell-off collateral Collateral operations may also **trigger money transactions**, such as: - Margin pledge charges - Invocation charges - Repayment from sell-off proceeds --- # Current Challenge The LMS currently processes transactions **independently per loan account** without orchestration across lender books. This introduces several operational risks in a co-lending structure. --- ## 1. Transaction Ordering Risk Example sequence: Repayment → Interest posting → Charge posting If these are processed **in different orders across lender loan books**, the share calculations become inconsistent. --- ## 2. Money Flow vs Accounting Mismatch Customer funds move through **escrow accounts**, while lender receivables are maintained in the LMS. Without deterministic orchestration: - escrow balances may move - lender books may not reconcile --- ## 3. Collateral and Money Transaction Race Conditions Example: Sell-off collateral and repayment arriving simultaneously. This may result in: - incorrect DP recalculation - incorrect sell-off triggers - incorrect available limit. --- ## 4. Partial Transaction Failures Example: Loan 100 disbursement succeeds but lender loan posting fails. This creates **partial system states** that break reconciliation. --- # Why Solving This

---

## #220 — Unpledge - Stocks selection logic
**Status:** Completed | **Last edited:** Unknown

**Solution:**
?**

---

## #221 — tech issues
**Status:** Unknown | **Last edited:** Unknown

# tech issues ## ### KYC & Authentication Issues 1. **KYC verification process fails with no clear error messaging** - Example (VTS-9511): "AKGPV3060R - Not able to move forward in kyc step" - Customer was stuck during verification with no indication of what went wrong or how to proceed. - Example (VTS-9981): "Stuck in kyc summary" - Process halted after completing verification with no error details provided to the customer. 2. **Digilocker integration failures during KYC verification** - Example (VTS-9770): "9415307644 - VIKAS KUMAR - KYC issue with digilocker's end" - API connection to Digilocker failing, preventing document verification. - Example (VTS-9964): "Discrepancies in CKYC record associated with the KYC Identifier: 50072772797161" - Records in Digilocker not matching with application data. 3. **Unusual KYC errors without diagnostic information** - Example (VTS-9711): "Unusual KYC Error" - Generic error message without actionable details for troubleshooting. - Example (VTS-10138): "CFCPS2351M - Facing error on KYC Page" - Customer encountered undefined error with no clear next steps. ### Pledging Process Failures 1. **KFin OTP delivery system failures** - Example (VTS-10085): "8928846293 - ATUL TIWARI - not getting otp at pledging for kfintech" - Customer attempted multiple times from web and app but never received OTP. - Example (VTS-10227): "8884052766 - DINESH KUMAR INALA - Kfintech pledging OTP issue" - System-wide failure in OTP delivery when pledging through KFin. 2. **Pledging failure despite eligibility** - Example (VTS-9396): "EQSPK8350P - KFin Pledging error" - "Fund is in approved list of TATA and is also visible when we did 15sec eligibility check" but still failing. - Example (VTS-9358): "DIWPP4809P - Unable to pledge Kfin funds" - Eligible funds appearing in portfolio but pledge transaction failing. 3. **Funds pledged but not lodged in system** - Example (VTS-9884): "Lodgment issue -ANNPS4596F" - "One of the pledged funds of the above client is not lodged in the system yet". - Example (VTS-10044): "BEPPB3956Q, Units pledged but lodgment not done" - Pledge transaction completed but credit not applied to account. ### API Integration Failures 1. **Timeouts in partner integrations** - Example (VTS-9597): "Frequent API Timeout Issues" - FundsIndia experiencing frequent API timeouts, preventing operations completion. - Example (VTS-9529): "Assistance Required: User Facing PAN Mobile Number Error in SDK" - API timeout causing user verification failures. 2. **Document API failures** - Example (VTS-9346): "Volt - Documents are Missing" - "I checked the webtops and I am unbale to find. Requesting you to

---

## #222 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled | Issue ID | Theme Name | Sub-Theme/Category | Specific Issue/Observation | No. Calls (Theme) | Priority | | --- | --- | --- | --- | --- | --- | | T1.S1.I1 | Partner & MFD Relations | Commission issues | Partners report that commission payments are often delayed. | 320 | TBD | | T1.S1.I2 | Partner & MFD Relations | Commission issues | Partners find discrepancies and incorrect amounts in their commission payments. | 320 | TBD | | T1.S1.I3 | Partner & MFD Relations | Commission issues | Partners express confusion about how commissions are calculated, especially with offers, contests, or multiple partner codes. | 320 | TBD | | T1.S1.I4 | Partner & MFD Relations | Commission issues | Partners are unclear about the specific rules and eligibility criteria for promotional commission offers and contests. | 320 | TBD | | T1.S1.I5 | Partner & MFD Relations | Commission issues | Partners frequently ask for clarification on payout timelines and calculation methods. | 320 | TBD | | T1.S1.I6 | Partner & MFD Relations | Commission issues | Partners need clear and usable GST invoices related to their commission earnings. | 320 | TBD | | T1.S1.I7 | Partner & MFD Relations | Commission issues | Partners mention that payout issues seem linked to delays in reflecting partner code changes or client mapping updates in the system. | 320 | TBD | | T1.S1.I8 | Partner & MFD Relations | Commission issues | Partners find it difficult to manage or track commissions when they have multiple associated accounts or codes. | 320 | TBD | | T1.S1.I9 | Partner & MFD Relations | Commission issues | Partners report missing or inaccurate client information in the portal, which impacts their ability to track expected commissions. | 320 | TBD | | T1.S1.I10 | Partner & MFD Relations | Commission issues | Partners request more timely updates on the status of their commission payouts. | 320 | TBD | | T1.S1.I11 | Partner & MFD Relations | Commission issues | Partners state that payouts can be blocked due to missing or incorrect bank details in their profile. | 320 | TBD | | T1.S1.I12 | Partner & MFD Relations | Commission issues | Partners often dispute the final commission amount, the timing of the payment, or their eligibility based on specific deals. | 320 |

---

## #223 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #224 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #225 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #226 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #227 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #228 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # Technical Design Document: Call Recording Processing System ## 1. System Overview The Call Recording Processing System is designed to ingest, store, transcribe, and analyze call recordings at scale. The system follows a microservices architecture to ensure modularity, scalability, and maintainability. ## 2. Detailed Service Architecture ### 2.1 Ingestion Service ### Components 1. **Upload Controller** - Handles HTTP uploads of call recordings - Validates input files and metadata - Initiates storage and processing workflow 2. **S3 Integration Module** - Manages direct integrations with S3 storage - Handles signed URLs for direct uploads - Processes S3 event notifications 3. **Bulk Download Manager** - Schedules and manages batch download jobs - Handles large volume transfers efficiently - Provides download job status tracking 4. **Ingestion Repository** - Stores recording metadata - Tracks ingestion status - Provides query capabilities for monitoring 5. Dedupe Manager - Checks the upload file name for the existing files names - Send callback with error “File already exist” ### Data Models ``` Recording { id: UUID externalId: String (client reference) filename: String mimeType: String fileSize: Long duration: Integer (seconds) source: String (enum: UPLOAD, BULK, S3) status: String (enum: UPLOADED, PROCESSING, COMPLETE, ERROR) storageLocation: String createdAt: Timestamp updatedAt: Timestamp metadata: JSON } ``` ### APIs 1. **Upload API** - `POST /recordings` - Multipart form upload for recording file - JSON metadata - Returns recording ID and status - Return Error is File name exists 2. **Bulk Operations API** - `POST /recordings/bulk` - Batch job creation - Configuration options (source, filters) - Returns job ID - Return Error is File name exists in batch handling allow others 3. **Status API** - `GET /recordings/{id}` - Recording metadata - Processing status - Links to associated resources ### 3.2 Storage Service ### Components 1. **Object Storage Manager** - Abstracts object storage operations - Implements retention policies - Handles object lifecycle management 2. **Database Service** - Manages PostgreSQL connections - Implements connection pooling - Provides transaction management 3. **Cache Service** - Redis-based caching - Frequently accessed metadata - Cache invalidation patterns ### Data Models ``` StorageMetadata { objectKey: String bucket: String region: String (if applicable) contentType: String contentLength: Long eTag: String createdAt: Timestamp lastAccessed: Timestamp } ``` ### APIs 1. **Object API** - `GET /storage/objects/{key}` - Object metadata - Presigned download URLs - `DELETE /storage/objects/{key}` - Mark for deletion or immediate removal 2. **Bucket Operations API** - `GET /storage/buckets/{name}/stats` - Storage statistics -

---

## #229 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #230 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #231 — SEO Text
**Status:** Unknown | **Last edited:** Unknown

# SEO Text A Loan against mutual funds (LAMF) allows you to borrow money by using your mutual fund units as collateral. Volt Money’s loan against mutual funds calculator can help you estimate the interest costs associated with this financing option. **What is a loan against mutual funds (LAMF)?** A loan against mutual funds (LAMF) is a secured loan where you pledge your mutual fund units as security to borrow money. The lender will determine the maximum loan amount you can qualify for based on a Loan-to-Value (LTV) ratio. This ratio represents the percentage of your mutual fund's market value that the lender is willing to lend against. You are then issued a credit limit which functions like a bank overdraft facility, where you are charged interest only on the amount you withdraw from this credit limit. **How to get a loan against mutual funds?** With Volt Money, you can get loan against mutual funds in 4 simple steps: 1. Check credit limit: We’ll evaluate your mutual fund portfolio & confirm credit limit. Check your credit limit from here. 2. Instant KYC: Complete digital KYC process. No paperwork required! 3. Pledge your assets: Mark your mutual funds as a security with a trusted lender. 4. Withdraw money: Withdraw & repay as per you requirement. No hidden charges. **How interest is calculated on loan against mutual funds?** Loan against mutual fund works like a bank overdraft limit, where you are only charged interest on the amount you withdraw. Interest is calculated daily and is deducted on a particular date every month. Interest calculation works on the following formula: Daily interest = P*(R/365) Monthly interest = Daily interest*N P = Principal outstanding on the day R = Annual rate of interest N = Number of days in a month Example: Suppose you withdraw ₹50,000 from Volt Money credit line at an interest of 10.49%. The daily interest rate would be calculated as (10.49% / 365) = 0.0287% per day. If the limit is utilized for 30 days, the interest accrued would be: *Interest = ₹50,000 × 0.0287% × 30 = ₹43.05* You can also make part payments to reduce your principal outstanding and thus reducing your interest payable. **Why Volt money’s overdraft like credit limit is better than a loan?** 1. Flexibility: With Volt money’s credit limit, you only pay interest on the amount you actually use, and you can repay it

---

## #232 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #233 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #234 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #235 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #236 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #237 — Term Loan Communications
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

## #238 — Term Loan Customer Statements
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

## #239 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #240 — Term Loan Sell off
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

## #241 — Term Loan Unpledge Eligibility API(Post loan creat
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

## #242 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #243 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #244 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #245 — PhonePe UPI Autopay Evaluation
**Status:** Unknown | **Last edited:** Unknown

# PhonePe UPI Autopay Evaluation API Documentation & Integration - [Link](https://developer.phonepe.com/v1/reference/subscription-v2-authorization) **List of APIs** 1. Authorization API 1. This API is used to generate the auth token to access the rest of the APIs. 2. The auth token is valid for 1 hour. 3. If the auth token is re-generated within 1 hour, the old token will not expire. - Request ```json curl --location 'https://api-preprod.phonepe.com/apis/pg-sandbox/v1/oauth/token' \ --header 'Content-Type: application/x-www-form-urlencoded' \ --data-urlencode 'client_id=' \ --data-urlencode 'client_version=1' \ --data-urlencode 'client_secret=' \ --data-urlencode 'grant_type=' ``` - Response ```json { "access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "encrypted_access_token": ".CX68QgSQj-P6KTTAIapTGLjVUWGoUi61pYJLXtoAO6Q", "expires_in": 3600, "issued_at": 1738669002, "expires_at": 1738672602, "session_expires_at": 1738672602, "token_type": "O-Bearer" } ``` 1. Validate VPA API 1. This API is used to validate the user's VPA. 2. Returns, valid & name of the user. 3. We should ask PhonePe team to share the bank account number & IFSC associated with this VPA. This will help us to limit mandate registration only on verified bank accounts. - Request ```json { "type": "VPA", "vpa": "nihaltest1@ybl" } ``` - Response ```json { "valid": true, "name": "<Name of User>" } ``` 1. Intent 1. This API is used to create the intent link for autopay. 2. amount - this parameter defines the amount to be deducted at the time of registration. 3. maxAmount - this amount defines the maximum amount the mandate is registering for. 4. Android - Generic intent URI will be provided. 5. iOS - Tpap specfic URI will be generated. Only Gpay, PhonePe & Paytm is supported. This will be a drawback as we can’t give users the power to choose the app. - Request ```json { "merchantOrderId": "MOTEST5", "amount": 300, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST5", "authWorkflowType": "TRANSACTION", "amountType": "FIXED", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_INTENT", "targetApp": "com.phonepe.app" } }, "deviceContext" : { "deviceOS" : "ANDROID" } } ``` - Response ```json { "orderId": "OMO2502041725138147510236", "state": "PENDING", "intentUrl": "ppesim://mandate?pa=VOLTMONEYUAT@ybl&pn=SUBSCRIBEMID&am=300&mam=&tr=OM2502041725138157510738&utm_campaign=SUBSCRIBE_AUTH&utm_medium=VOLTMONEYUAT&utm_source=OM2502041725138157510738" } ``` 1. Collect 1. This API is used to send the collect request for mandate setup. 2. In collect request, all the VPAs are supported. Even Gpay, SuperMoney VPAs are supported. - Request Body ```json { "merchantOrderId": "MOTEST6", "amount": 200, "expireAt": 1709058548000, "paymentFlow": { "type": "SUBSCRIPTION_SETUP", "merchantSubscriptionId": "MSTEST6", "authWorkflowType": "TRANSACTION", "amountType": "VARIABLE", "maxAmount": 2000, "frequency": "ON_DEMAND", "expireAt": 1737278524000, "paymentMode": { "type": "UPI_COLLECT", "details": { "type": "VPA", "vpa": "nihaltest1@ybl" } } } } ``` - Response ```json { "orderId": "OMO2502041727154877510267", "state": "PENDING" } ``` 1.

---

## #246 — Cancel unpledge request
**Status:** Solutioning pending | **Last edited:** Unknown

# Cancel unpledge request Classification: Cancel unpledge Notes: User asked to cancel unpledge request, understand why this happened? User decided to not do it? PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13889 Status: Solutioning pending

---

## #247 — I have a ticket open for unpledge ”
**Status:** PRD pending | **Last edited:** Unknown

# """I have a ticket open for unpledge""” Classification: Unpledge request status Notes: User asked for the status of their unpledge request PRD/Solution mapping: PRD under progress Platform: Wati Reference Link/ID: 919437780780 Status: PRD pending

---

## #248 — User was given a higher sanction amount than their
**Status:** Solutioning pending | **Last edited:** Unknown

# User was given a higher sanction amount than their credit limit, was able to place a withdrawal request before lodgement was done Classification: Sanction Amount and credit limit handling Notes: Sanction amount instead of credit line amount is shown to the customer before lodgement, ideally withdrawal should be blocked or better communicated, there should be a failed state for all transactions PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13404 Status: Solutioning pending

---

## #249 — User’s pledging failed for Karvy and when they ret
**Status:** Solutioning pending | **Last edited:** Unknown

# User’s pledging failed for Karvy and when they retried, we charged the user processing fee twice without withdrawal - Tata Classification: Karvy pledging issue Notes: Check with Karvy why pledging failed, we should have updated our creditapplication data automatically on pledge failure PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13013 Status: Solutioning pending

---

## #250 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements ![Untitled](Design%20requirements/Untitled.png) ![Untitled](Design%20requirements/Untitled%201.png) 35% users drop off from the loan summary(Verify interest and charges page) Problems we have identified: 1. Users think that this is the last page of the application. 2. Benefits are not properly communicated. 3. User thinks that the PF is too high. Things that we want to communicate with this page: 1. Highlight selected credit limit, remove selected mutual funds: This might be reminding the users that they are pledging alot of MFs for the limit that they are getting. 2. Show maximum credit limit (maybe). 3. Unlimited withdrawals, repay anytime: Communicate benefits. 4. Pay interest only on the amount you use: Communicate benefits. 5. Monthly interest only EMIs, we can show this for 1,00,00 withdrawal and user can change it to see the IOEMI change: This will quantify the interest that they have to pay 1. 10.49% might feel high but IOEMI will be low for default sum of 1,00,000 2. This will communicate that they only have to pay interest on the sum withdrawn 6. Provided by our trusted lender Tata Capital: User trust 7. Highlight zero hidden charges before showing the charges: User should know that we are transparent with our charges. 8. Other details to be in bottom 25% of the screen: [Content ](Design%20requirements/Content%20aa1bb6ecad904d00b07393fa73ff756a.md)

---

## #251 — Understanding brand (WIP)
**Status:** Unknown | **Last edited:** Unknown

# Understanding brand (WIP) # Notes from 1:1 1. How would you envision users describing volt as a brand? 1. I believe a user would talk about how easy, seamless and fast the journey was to use volt and solve for my need of a loan while my funds are growing 2. If volt was a person how would you describe it? 1. Supportive 2. Reliable and Fast to help 3. Motivating 4. Enabler to achieve your financial needs 5. A saviour when you need most 3. Describe Volt in 3-4 words 1. Transparent, Trustworthy, Easy, Fast - Emphasise to our audience that your investments are for you long term - stay invested in them and by leveraging them - - Smart choice to leverage assets to help with your needs - Someone who will give you right guidance - smart choice - Transparency, easy, instant, trustworthy Your assets pledge - give trust that nothing is happening to them are safe Enablers - “unlocking something that was once only available to HNIs” # Cleaned takeaways ### Keywords - Transparent - Trustworthy - Easy - Instant - Instant

---

## #252 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Pledging will not affect the growth, Financial goal for which you started, long term plan gets hampered, no cibil requirement, Repay any time, Being in control, Reducing interest, Kevin (Servicing): unpledge request 10% buffer, shortfall, bad sell off experience, change in Sanction limit Mahesh: NBFC license, TATA and Bajaj, Names: Trust Naveen: - No brand val - GST india - NBFC license - Lenders

---

## #253 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: rate of interest, foreclousure, processing fees, lein removal, repayment, additional top up, stocks, Kevin (Servicing): Instant disbursals, Delays, Unpledging and Forclosure. ELSS funds are possible for TATA, Schedule the loan disbursal time, Mahesh: Interest, How it works, Repayment. phone pe traffic is greater than influencers, Reconstruct their houses. Names: Main areas of concerns Naveen: Portfolio value, Location. I dont feel like I am doing the Pledging step Requirement : Urgency. Pay somebody, reinvest, NFO Bugs on app vs web

---

## #254 — DSP Fin Website About Us Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin Website: About Us Page **Objective**: To communicate about the values of the company to audience. DSP Finance is a Non-Banking Financial Company (NBFC) backed by the 160+ year legacy of the DSP Group — one of India’s most respected names in financial services. Rooted in trust, innovation, and discipline, we provide customized credit solutions designed to help individuals and businesses unlock value and achieve their financial goals. We are a NBFC with a strong focus on growth through operational excellence and solving problems through technology. **Mission**: To combine deep market expertise with customer-first innovation, ensuring **reliable, transparent, and efficient access to credit** by leveraging technology and robust operational excellence. **Vision**: To be India’s most trusted partner for financial collateral-backed credit, enabling individuals and businesses to unlock value from their investments for exponential financial growth. DSP Finance’s Values. - Customers first - Utmost transparency - People focus - Continuous innovation Key Highlights of DSP finance to be mentioned - AUM of ~2000CR - ~70K customers - 8+ leading partners - AAA rated DSP Finance’s focus is on capital markets led product offerings in the below business lines. - Loan against securities: enabling individuals to leverage their financial assets to get easy access to credit. This page will redirect to the LAS page. - Financial solutions group: providing corporates access to credit by leveraging their assets to get quick access to funds. This page will redirect to the FSG page. DSP Finance works on the below principles. - **Legacy of Trust** – Backed by the DSP Group’s long-standing credibility in Indian finance ecosystem. - **Customer-First Approach** – Transparent processes, no hidden charges, and clear communication. - **Digital-First Experience** – End-to-end paperless solutions with seamless pledge and disbursal. - **Prudent Risk Management** – Strong governance and compliance in line with RBI regulations. - **Expertise & Innovation** – Blend of deep financial knowledge and modern technology to drive deep innovation. DSP has partnered with leading partners to enable customers to leverage their assets. - PhonePe - PayTm - Indmoney - Groww - ETMoney - CRED

---

## #255 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #256 — NBFC B2B LSP API List
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : API List - Pledge API on DSP - pending - Fetch API on DSP - pending - Submit opportunity - create account - Mobile & Email update - no verification - Add verification timestamp for mobile & email - KFS & Agreement: we might have to decouple and make KFS pass the response in parameters - Offer API on DSP - LSP passes back the confirmation to DSP - PAN verification - LSP not required to integrate -

---

## #257 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #258 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can