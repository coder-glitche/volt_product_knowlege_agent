# Current State: Loan Origination

> Auto-generated from 266 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — Deferring email capture and verification during on
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

## #2 — Manage Limit Error messaging handling
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

## #3 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #4 — BAJAJ Dedupe API
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

## #5 — Interest calculator - landing page
**Status:** In progress | **Last edited:** October 9, 2024 8:22 PM

**Problem:**
are we solving?**

1. Before applying for Volt LAMF or withdrawals users want an estimate of what is the interest that they will pay.
2. Since alot of user consider Volt LAMF as term loan, they want to get an understanding of how to close the loan in X duration with equal monthly payments. MFDs are asked this query alot as well. 

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

## #7 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #8 — BAJAJ New KFS+Agreement flow
**Status:** Done | **Last edited:** October 8, 2024 1:04 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload

---

**Solution:**
?**

---

## #9 — LSQ Revamp Solution Doc
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

## #10 — Multi Drawdown Term Loan LMS Requirements
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

## #11 — DSP BRE for Beta
**Status:** Pending Review | **Last edited:** October 28, 2024 10:53 AM

**Problem:**
are we solving?**

Currently, customers can avail a loan from Volt app or web through DSP only through whitelisting or URL based parameters. This will not be possible to handle in the beta stage as we need to route applications real-time to DSP.

In addition, the segment where the credit limit offered by Volt is between 10K and 25K is ~12% of the total eligible applications which isn’t catered to by our other lenders, Bajaj and Tata. This opens up a new set of customers for us to acquire and eventual enhance from a limit perspective. 

---

**Solution:**
?**

---

## #12 — TATA KFS and Agreement Phase 2
**Status:** In progress | **Last edited:** October 24, 2024 10:46 AM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge.

---

**Solution:**
?**

---

## #13 — [Lending stack] Welcome mail
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

## #14 — DSP communication email template
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

## #15 — Change in audit trail flow for PAN Validation API
**Status:** Pending Review | **Last edited:** October 17, 2024 8:05 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details (POV=null), the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

---

## #16 — Withdrawal Optimisations
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

## #17 — LOS and LMS admin actions (LSP with DSP as lender)
**Status:** In progress | **Last edited:** October 16, 2024 2:25 PM

**Problem:**
are we solving?**

We have developed multiple admin actions (ops controlled actions) that help in servicing our customers in the onboarding as well as the servicing journey. 

This requirement covers utilising the admin actions (where needed) to cover use cases currently served by LSP (for customers) with DSP as a lender.

---

**Solution:**
?**

---

## #18 — Bulk email automation
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

## #19 — Lender selection logic for BRE for production
**Status:** Ready for Tech | **Last edited:** October 11, 2024 4:47 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

I’m not able to find the logic of TATA/BAJAJ based on fetch limit

---

## #20 — [Lending stack] KYC Flow
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

## #21 — BAJAJ New KFS+Agreement flow (with re-query)
**Status:** Pending Review | **Last edited:** October 11, 2024 12:42 PM

**Problem:**
are we solving?**

When the user rejects the KFS/Agreement, the link isn't regenerated; they have to contact Ops who recreate the lender application (SFDC regeneration) to generate new KFS/Agreement link. This causes a lot of user & operational overload as well as results in customer drop-offs.

---

**Solution:**
?**

---

## #22 — Mandate Set up optimisation - Error Messaging + Ne
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

## #23 — [IronGrid] Un-lien related issues
**Status:** Not started | **Last edited:** November 5, 2024 12:48 PM

# [IronGrid] Un-lien related issues ## Fund level status of un-pledge request **Phase 1** - Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED. - We will keep polling the status of all the funds until we get the terminal statuses of each of the funds - We keep polling the API for 4 days every hour until we get the status of all the fund - Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached) - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request - We will store the individual status of all the funds under the un-pledge request - API Documentation : [Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx) **Phase 2** - We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user. ## Excess margin handling in un-pledge request **For BFL (only need to make this change for BAJAJ)** - While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge. - 3 fields which are present in Foreclosure details API : - net payable = Total due - Excess Margin - Total Due - Excess Margin - For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding. ### **User not able to request un-lien request if stocks present in their holding** - **Issue** - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error - **Solution** - We will only

---

## #24 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #25 — Periskope
**Status:** In progress | **Last edited:** November 29, 2024 1:55 PM

# Periskope [Periskope to wati plan ](Periskope/Periskope%20to%20wati%20plan%2014ce8d3af13a80849cf2d1d5e048585e.md) ### Current Challenges: 1. **Limited Tracking**: We cannot effectively track incoming chats or their resolutions due to limitations in Periscope. 2. **Chat Status Visibility**: There is no visibility into chat statuses (e.g., open, resolved, work-in-progress). 3. **Active Chat Monitoring**: We cannot determine how many chat groups are currently active or were active in the last week. 4. **Categorization Issues**: There's no way to identify whether chats are related to sales or service. 5. **Chat Volume**: We receive around 100 chats daily. This a 6. **Lack of Bulk Chat Download**: Periscope does not offer a bulk download feature for chat records. 7. **Response Time (TAT)**: We are unable to track response times or resolution times for chats. 8. **Agent Tracking Issues**: Agents lose track of ongoing chats as new chats push older conversations to the bottom of the queue, making it difficult to manage multiple conversations. 9. **Limited Team Capacity**: Only two people manage Periscope at a time, which limits our ability to handle high chat volumes effectively. 10. **No Chat Closure Mechanism**: There is no way to close chats or mark them as resolved. 11. **Unclear Analytics**: Terms such as "daily message counts" and "flagged messages" lack clear definitions and explanations. 12. **Ticketing Process**: The process for raising tickets is unclear to the team. 13. **Unavailability of RM (Relationship Managers)**: If an MFD reaches out and the assigned RM is unavailable, another agent is assigned to Periscope to manage the chat. 14. **Periscope and WATI Integration**: While all MFDs are connected to Periscope, they are not added to WATI, leading to inconsistencies in communication channels. 15. **Missed Chats**: Missed chats often go unnoticed until they escalate, as there is no way to flag or track missed communications in real time. ## Visibility There are three visibility that we need. - Visibility on Chat messages - Visibility on the issue resolution - Visibility on the Impact of the Providing support Table 1: Visibility on Interactions with MFD Partners | Metric | Description | Current | Wati (option 1 ) | Suggested | | --- | --- | --- | --- | --- | | Total Interactions | Number of interactions with MFD partners | Tracked in Periskope | | | | Call Volume | Number of calls between RMs and MFDs | exotell | | | | Chat Volume | Number of chat conversations

---

## #26 — TCL Credit Referral Automations & optimisations
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

## #27 — Volt B2B Redirection Enhancement - Park+
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

## #28 — TATA Dedupe API with updated BRE
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

## #29 — QC rejection flow handling for DSP - Volt LOS
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

## #30 — TATA KFS and Agreement Phase 1
**Status:** In progress | **Last edited:** November 18, 2024 1:08 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the KFS format as specified. While the KFS is designed keeping borrower protection in mind, handling it in a elegant way without compromising on the experience is a challenge. 

---

**Solution:**
?**

---

## #31 — Foreclosure handling for DSP
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

## #32 — External reporting requirements
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

## #33 — White-labelled Redirection Journey for B2B Partner
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

## #34 — Enhancement optimization
**Status:** In progress | **Last edited:** November 14, 2024 7:21 PM

**Problem:**
are we solving?**

- For the customers whose DP is significantly less than sanction limit when try to enhance (pledge more funds) such that there sanction limit does not get updated then user are not given information

---

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

## #36 — Repayments Handling For MFD
**Status:** Not started | **Last edited:** May 9, 2025 4:58 PM

# Repayments Handling For MFD # **Ongoing Credit lines & Client Servicing** - **Repayment Dynamics & Facilitation:** - **Comprehensive Initial Explanation of Repayment Mechanics (Post Loan Activation):** - Reiterate the primary mode of interest servicing: Monthly auto-debit via the registered e-NACH/physical NACH mandate. - Clearly explain the interest calculation basis (e.g., daily accrual on outstanding principal, monthly debit). - Specify the typical due date or debit cycle for interest payments. - Detail the process for making **voluntary principal repayments**: - Available channels (e.g., Volt Money client app/portal, designated Virtual Account Number (VAN) for NEFT/RTGS/IMPS). - Minimum/maximum amounts for voluntary principal repayments (if any). - Impact of principal repayment on subsequent interest calculations and loan tenure (if applicable, though LAMF is typically open-ended). - Explain **payment cut-off times**: Clarify by what time a payment must be made to be considered for same-day credit or to avoid late fees. - Describe **apportionment logic** for payments: How payments are applied (e.g., typically Penal Interest -> Normal Interest -> Principal, or CIP/ICP – Charges, Interest, Principal). - Outline consequences of **missed or delayed payments**: Penal interest, potential impact on future dealings, implications for margin calls if default persists. - Explain where clients can view their **repayment schedule/history** and upcoming due amounts (e.g., client portal, app, Statement of Account). - **Managing Auto-Debit (e-NACH/Mandate) Process:** - Confirm with client that their mandate is successfully registered and active post-loan setup. - Proactively remind clients (especially new ones) before the first few due dates to maintain sufficient funds in their mandated bank account. - Guide clients on how to check the status of their auto-debit (e.g., through their bank statements, Volt Money portal notifications). - **Troubleshooting Mandate Failures:** - If auto-debit fails, promptly communicate with the client (if not already alerted by Volt). - Help diagnose reasons for failure (e.g., insufficient funds, mandate revoked/expired, technical issues at bank end, account frozen/closed). - Advise on immediate alternative payment methods to cover the due amount and avoid penalties. - Guide on steps to rectify the mandate issue (e.g., ensure funds, re-register mandate if necessary through Volt's process). - **Facilitating Voluntary Repayments (Principal or Dues):** - **Guidance on Payment Initiation (Client App/Portal):** - Assist clients in navigating the app/portal to find the "Repay Loan," "Make Payment," or similar section. - Explain options like "Pay Interest Due," "Pay Custom Amount," or "Pay Full Outstanding." - Guide them through selecting payment method (Net

---

## #37 — enhancement in MFD Dashbaord
**Status:** Not started | **Last edited:** May 8, 2025 4:02 PM

# enhancement in MFD Dashbaord ### Process Enhancements & Issues Summary 1. **overall Process Communication Gaps** - Many users are unaware of the process, applicable charges, and resolution timelines. - Since there are *charges* involved are not deducted as of now and the *Turnaround Time (TAT) is 1 hour*, this should be **clearly communicated**. - Several funds are missing **phone numbers or PAN**, causing processing delays. 2. **Pledge Error Messaging** - Current error messages like “some error” or “unable to pledge” are too generic. - **Action:** Use more descriptive error messages, similar to those used in Slack (e.g., “Pledge failed due to missing PAN details”). 3. **Bajaj - Account Setup** - we are not doing - Clarify next steps the status is: **“Account setup in progress.”** - Define whether any user action is needed, and communicate this proactively. 4. **TATA – Sanction Limit Increase** - When fund value increases and limit adjustment is required: - Use **Admin Action** to increase the sanction limit. - Then, **trigger the agreement step** manually. 5. **Elevate Cases**

---

## #38 — Phase 1 LTV Tenure Update_LOS
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

## #39 — [Platform] Callbacks for LSP APIs for core servici
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

## #40 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #41 — Phase 0 LTV Tenure Update_LOS
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

## #42 — Handling LOS Application Rejections
**Status:** Not started | **Last edited:** May 25, 2026 12:22 PM

**Problem:**
are we solving?**

Currently in LOS , several business-critical validation checks are performed — such as client deduplication, MNRL checks, and AML/PEP screenings. 

However when any of these checks fail, the system surfaces a generic ‘declined’  error message (”Something went wrong”) to the user. The root cause is that the backend does not propagate the specific error code or reason to the frontend, so the frontend cannot render contextual, actionable error screens.

---

**Solution:**
?**

---

## #43 — Higher LTV Product – Customer Communication Framew
**Status:** Pending Review | **Last edited:** May 23, 2026 9:07 PM

# Higher LTV Product – Customer Communication Framework # Background As part of the Higher LTV Product initiative, the NBFC will enable eligible customers to increase their sanctioned credit limit basis revised LTV eligibility on pledged mutual fund holdings. Since the LTV enhancement flow involves execution of revised loan documentation and customer consent, it introduces the following communication requirements: 1. Customers must receive the revised KFS and Agreement/Amendment documents executed as part of the LTV update flow. 2. Customers must be notified once their revised credit limit is successfully updated. 3. From the LSP perspective, the feature needs to be promoted proactively while also ensuring customers receive timely status notifications throughout the journey. --- # Proposed Solution ## 1. NBFC (DSP) Communications From the NBFC side, a post-facto communication shall be sent once the customer’s limit enhancement request is successfully processed through the LTV update flow. The communication will serve the following purposes: - Inform customers regarding successful limit enhancement - Share revised loan documentation for customer reference - Ensure regulatory and audit compliance for executed agreements ### Communication Channels - Email - SMS --- ### DSP Email Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding revised credit limit and share updated KFS/Agreement | | Template ID | d-dbcef3df48ca4908a47b8e1c98e5c5c9 | | Variables | clientId, date, lan, updated_credit_limit, additional_credit_limit, previous_credit_limit | | Attachments | Loan kit (KFS + Amendment) | --- ### DSP SMS Communication | Field | Details | | --- | --- | | Communication Trigger | Successful completion of LTV update flow | | Purpose | Notify customer regarding successful credit limit enhancement | | Template ID | 1107177910598106787 | | Tempalte Name | LTV_Update_Limit_enhancement_V2 | | Copy | Congratulations {{customerName}}, your credit limit for the loan account {{lan}} has been successfully increased to Rs {{updated_credit_limit}}. Find the ROI & charge details in the KFS document available on DSP Finance app : {{dsp_app_url}} | | VilPower Copy | Congratulations {#alphanumeric#}, your credit limit for the loan account {#alphanumeric#} has been successfully increased to Rs {#alphanumeric#}. Please find the ROI & charge details in the KFS document available on DSP Finance app : {#url#} | --- # 2. LSP (Volt) Communications From the LSP side, communications will focus on: - Promoting the Higher LTV offering to eligible customers -

---

## #44 — MFC Summary API integration
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

## #45 — Jupiter FE requirements
**Status:** Not started | **Last edited:** May 23, 2024 12:54 PM

**Problem:**
are we solving?**

Because we are removing bottom NAV and My account section, we need to move entry point of functionalities to main dashboard, following PRD covers those cases.

---

**Solution:**
?**

---

## #46 — LSQ Chat workflow - Phase 1
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

## #47 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #48 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #49 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #50 — PRD MFD Performance Metrics & Earnings Display
**Status:** Not started | **Last edited:** May 21, 2025 12:46 PM

# PRD: MFD Performance Metrics & Earnings Display ## **1. Introduction** This feature will give empanelled MFDs a clear, transparent, and motivating view of their performance related to the *Volt Money* program offered by Volt. The dashboard will show: - Their sourced **MF Loan AUM** - Applicable **trail income rate** - **Trail income earned** - **Account opening bonuses** The goal is to make it simple for MFDs to understand how their efforts are driving their earnings. --- ## **2. Goals & Objectives** ### **Primary Goal** To clearly display an MFD’s Volt Money performance, including MF Loan AUM, trail income, and incentives. ### **MFD User Objectives** - Understand how MF Loan AUM translates into income or Increase visibility to the MFDs - Track progress toward higher income tiers - See a breakdown of earnings and new account bonuses - View historical trends and performance ### **Business Objectives** - Encourage MFDs to grow MF Loan AUM - Boost Volt Money customer acquisition - Reduce support queries about commissions ## **Success Metrics** - MFD Monthly visits to partner portal - MFD Repeat rate - MFD Avg number of applicaitons per month - upward move in MFD LAMF AUM Buckets --- ## **3. User Stories** - *As an MFD*, I want to view my current MF Loan AUM so I know my payout tier. - I want to know my current trail income rate based on slabs. - I want to see how close I am to the next earning tier. - I want to track monthly/quarterly/yearly trail income. - I want to verify bonuses for each new LAMF line opened. - I want a full summary of earnings: trail income + bonuses. - I want to view historical performance trends. - I want to quickly reference the trail income slab table. --- ## **4. Feature Breakdown & UI/UX** ### **4.1 Main Dashboard: Volt Money Performance Overview** **Key Metrics:** | Metric | Example | Tooltip | | --- | --- | --- | | **Current AUM** | ₹12.5 Cr | Outstanding principal under Volt Money | | **Trail Rate** | 0.55% | Based on current AUM slab | | **Trail Income (This Month)** | ₹57,291 | Clarify if based on daily accrual, etc. | | **New Accounts (MTD)** | 5 | From Onboarding CRM | | **Bonus Earned (MTD)** | ₹1,000 | ₹200 x new accounts | | **Total Earnings (MTD)** | ₹58,291 |

---

## #51 — Redemption vs LAMF Calculator & Comparison Tool
**Status:** In progress | **Last edited:** May 20, 2025 3:46 PM

# Redemption vs. LAMF Calculator & Comparison Tool ## Problem We’re Solving - Our TG sell their assets to meet short-term cash needs, unaware that they can leverage their assets to achieve their short-term goals more effectively. - Others explore alternatives to meet short-term need such as personal loans or business loans, but often encounter challenges such as high interest rates & other charges, cumbersome application processes, closure of loan. - Some are hesitant to take loans due to a lack of understanding between good loans and bad loans and end up selling assets to meet goal. - Currently, MFDs rely on pen and paper to explain to their clients the benefits of LAMF and the potential losses associated with selling mutual funds. - Through RRC, we aim to address the following objectives: - Education and awareness about LAMF to out TG - Branding through marketing and organic sharing ## Objectives - Educate and raise awareness around LAMF. - Help clients make **informed financial decisions**. - Arm MFDs with a professional, branded, easy-to-use digital tool. - Drive brand trust through co-branded PDF reports and shareable content. ## User Stories (MFD-Focused) 1. **Fetch & Consent** - *As an MFD, I want to enter a client’s phone and PAN, trigger OTP-based consent, and fetch LAMF eligibility in real time.* 2. **Custom Amount & Instant Comparison** - *Once I have the LAMF limit, I want to enter any amount (up to the limit) and instantly show a side-by-side comparison of “Redeeming” vs. “Taking LAMF.”* 3. **Crystal-Clear Visuals** - *I want to show tax impact, exit load, interest costs, and future value—so my client easily sees the pros and cons.* 4. **Branded Takeaway** - *I want to download a co-branded PDF with this comparison to give my client a clear, professional summary.* ## 🛠️ Tool Overview & Flow ### 1. **Customer Consent & Details (Screen 1)** - Inputs: Client Mobile Number, Client PAN - Button: “Enter OTP” ### 2. **OTP & Eligibility Fetch (Screen 2)** - Input: OTP - Fetch: MF holdings + Max LAMF limit - Errors:- - Combination is not registered on the MF central - No funds - Available limit is insufficient. ### 3. **Input Desired Amount (Screen 3)** - Display: Max eligible amount (e.g., ₹5,00,000) - Input: Desired amount (editable) - Button: “Compare Redemption vs. LAMF” ### 4. **Comparison View (Screen 4)** Two-column layout: | Parameter | Redeeming MFs |

---

## #52 — Lead Follow-Up Mechanism — Old Leads
**Status:** Not started | **Last edited:** May 19, 2026 6:08 PM

# Lead Follow-Up Mechanism — Old Leads ## Objective Design a structured follow-up mechanism for old leads to: - Ensure periodic engagement - Maximize lead conversion - Control automation usage - Avoid excessive calling - Standardize disposition-driven follow-ups # 1. Lead Segmentation ## Lead Types ### 1. New Leads - Real-time lead assignment - Immediate engagement journey - Separate automation flow ### 2. Old Leads - Leads not converted - Re-engagement campaign - Monthly task-based follow-up mechanism # 2. Old Lead Follow-Up Workflow ## Monthly Trigger ### Automation 1 At the beginning of every month: - Create calling task for all eligible old leads ### Eligibility Conditions - Lead not converted - Lead not closed permanently - Lead not activated - Lead within retry policy # 3. Agent Calling Workflow ## Step 1 — Agent Filters Pending Tasks Agent opens: - Same-day pending tasks - Older pending tasks ## Step 2 — Open Task Agent initiates call. ## Step 3 — Add Disposition Agent marks call outcome. # 4. Disposition-Based Follow-Up Logic | Call Outcome | Sub-Disposition | Action | Next Follow-Up | | --- | --- | --- | --- | | Connected | Interested | Create Follow-Up Task | T+4 | | Connected | Follow-Up Required | Create Follow-Up Task | T+3 | | Connected | Not Interested | Close Task | No Retry | | Connected | MFD Activated | Close Task | No Retry | | Connected | Other Dispositions | Close Task | No Retry | | RNR | — | Create Retry Task | T+2 | | Asked to Call Back | — | Create Retry Task | T+1 | # 5. Calling Attempt Policy ## Monthly Attempt Limits | Criteria | Count | | --- | --- | | Minimum Calls per Lead | 4 | | Recommended Maximum | 8 | | Absolute Maximum | 10 | # 6. Retry Logic ## Retry Rules - Retry only if: - RNR - Callback Requested - Follow-Up Needed - Interested - Stop retries if: - Not Interested - Activated - Invalid - Duplicate - DND - Converted # 7. Automation Consumption Model ## A. Initial Monthly Task Creation | Activity | Automations | | --- | --- | | Monthly Task Creation | 1 | ## B. Per Call Attempt Each call consumes: | Automation Activity | Count | | --- | --- |

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

## #55 — Term Loan LOS requirements
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

## #56 — MFD onboarding Revamp
**Status:** In progress | **Last edited:** May 12, 2025 5:05 PM

# MFD onboarding Revamp ## Problem statements In the sales workflow - Fragmented Lead management: Non-website MFD leads are tracked manually in spreadsheets, separate from website leads captured in LSQ. - The team has to manually mark the call activity on the Leads in sheets - Re-engaging leads after RNR calls is a manual process. - Currently don’t have a setup to trigger automated 'attempted contact' communications (e.g., SMS/Email) to unresponsive MFD leads. - We can’t track the outbound call activity on the leads, making the QA and input metrics hard to track - There is no auto-dialer, and the team has to spend time in RNR and voicemails - Inbound calls from MFD, and processing should be done by the same Agent. - We don't have a defined sales workflow, i.e., 4 Calls to mark lead as lost, sales copy to re-engage - ~~Agents are unable to assign the Activated MFD to RMs~~. solved - There are activated MFDs with the lead type Customer, as they were not properly added to LSQ. - MFD as a b2c customer - add to lsq - The activation team wants to realign on dispositions - The activation team uses Base WhatsApp for communications with MFD leads - MFDs are not familiar with the LAMF product and the commission Potential. In Partner/signup - Many Not MFD customers register on the partner page, causing the onboarding team to waste time. ~70 % non-eligible leads - People registering are not entering a Valid email ID - We can’t validate ARN with MFD - ARN is currently not mandatory - We provide an access token to the Dashboard to the User after they authenticate their number with OTP. - The landing page of the partner is similar to that of a regular customer and has not been updated for 2 years - Many people intentionally mislead to get self-line benefits Low convertion funnel - we calls 150 leads a day , that lead sto 50 connects per person , for 2 person we connect with 100 leads, results into 3-4 activatins a day - ## Proposed solutions - Rewamp registration Flow in the MFD channel to filter the MFD out: *See Benchmarking* - Make Email verification mandatory - Make ARN verification mandatory - Clear call out to customers who need to be an MFD to continue - A Calculator tool with an illustration will help Agents

---

## #57 — Enhanced Customer Registration & Deduplication for
**Status:** Done | **Last edited:** May 12, 2025 12:46 PM

# Enhanced Customer Registration & Deduplication for MFDs **Enhanced Customer Registration & Deduplication for MFDs** ### **Problem** 1. MFDs often hit blockers or need RM support when trying to register customers who already exist in Volt’s system (e.g., as B2C users, under another B2B partner, or with active loans). 2. The current error message—“Failed to register customer”—is vague and doesn’t guide the MFD on what to do next based on the type of duplicate. 3. There were 1,200 such error on MFD portal. ~50% of the registered TOFU. and 185 admin actions to Map partners ### **Goal** - Simplify the customer registration journey for MFDs, especially in common duplicate scenarios. - Reduce RM dependency, particularly for B2C linking. - Provide clear, actionable feedback to MFDs when a duplicate is found. ### **Proposed Solution: Automat** When an MFD submits “Register Customer” with Name, Mobile, and: ### 1. **Backend Deduplication Check** - Use Mobile and to detect existing customer records. ### 2. **Modal-Based Responses Based on Scenario** - **A. New Customer (No Prior Account)** - **Action:** Add customer —> OTP - **UI:** No modal or interruption. - **B. Customer Exists as B2C (Registered directly on Volt)** - **Modal Title:** *Customer Found in Volt* - **Message:** “This customer is already registered directly with Volt. To add them to your portfolio, OTP verification is required.” - **CTAs:** - “Send OTP & Add Customer” (launches OTP flow) - “Cancel” - **C. Customer Linked to Another Partner or Has Active Application** - **Modal Title:** *Customer Already Registered* - **Message:** “This customer ([Name or Masked ID]) is already registered with Volt and may be linked to another partner or have an active application/loan. Please contact your RM for support.” - **CTA:** “Okay” (returns MFD to form) - **D. Typo/Error in Initial Input (Pre-dedupe)** - If the MFD catches a mistake before dedupe runs (e.g., wrong PAN), allow them to use the existing “Edit details” button. - Once dedupe identifies a match, scenario-specific modals override the generic error message. ### **Key Requirements** - Backend API for robust deduplication using PAN/Mobile. - API must return customer status: - Not found - Existing B2C - Linked to another partner - Active loan/application - Dynamic modals based on API response. - OTP flow for linking B2C customers to MFDs. - Clear attribution/commission logic for B2C linking. ### **Benefits** - Fewer MFD drop-offs and RM escalations. - Seamless onboarding for B2C customers

---

## #58 — Term loan CC enhancements
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

## #59 — [Volt LSP] Volt LOS Journey 2 0
**Status:** Not started | **Last edited:** March 31, 2025 5:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #60 — [Platform] Foreclosure handling and enhancement
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

## #61 — TOS calculation for foreclosures [TCL]
**Status:** In progress | **Last edited:** March 24, 2025 7:28 PM

**Problem:**
are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

**Solution:**
?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

---

## #62 — Lien status lifecycle tracking
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

## #63 — Foreclosure lifecycle tracking + Tata EOD report
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

## #64 — [Volt LOS] KYC optimisations
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

## #65 — Calling Support Workflow – Exotel + LeadSquared In
**Status:** Not started | **Last edited:** March 17, 2026 7:00 PM

# Calling Support Workflow – Exotel + LeadSquared Integration ```mermaid flowchart TD A[Customer calls support number] --> B[Exotel receives call] B --> C[Exotel triggers API to LeadSquared] C --> D[Fetch customer details using phone number] D --> E[Open Customer 360] E --> F[Show call popup in Marvin] F --> G{Agent available?} G -- Yes --> H[Connect call to agent] H --> I[Agent discusses issue] I --> J{Existing ticket?} J -- Yes --> K[Associate call with existing ticket] J -- No --> L{Closed ticket exists?} L -- Yes --> M[Reopen ticket] L -- No --> N{Issue resolved?} N -- Yes --> O[Capture disposition] N -- No --> P[Create new ticket] K --> Q[Capture call disposition] M --> Q O --> Q P --> Q Q --> R[Exotel collects CSAT] R --> S[Send CSAT to LeadSquared] S --> T[Call process completed] %% MISSED CALL FLOW G -- No --> U[Call not connected] U --> V[Create missed call ticket] V --> W[Assign ticket via round robin] W --> X[Agent opens ticket] X --> Y[Click to Call] Y --> H ```

---

## #66 — Product note Co-lending foreclosure - Deprecated -
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

## #67 — Capital gains tax calculator
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

## #68 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #69 — Margin pledge charges
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

## #70 — MFD Activation Flow in LSQ
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

## #71 — Increase Credit Utilization via Whatsapp Drips
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

## #72 — Chat CSAT and DSAT Capture WATI
**Status:** Not started | **Last edited:** June 24, 2025 5:00 PM

# Chat CSAT and DSAT Capture <> WATI ## 🧩 **Objective** To capture structured customer satisfaction (CSAT) and dissatisfaction (DSAT) data via a chatbot workflow that can be automatically stored, tagged, and actioned via escalation or closure, based on customer responses. --- ## 📌 **Platform** **Tool Used:** **WATI** WATI is used to automate and manage the chatbot-based feedback collection journey on WhatsApp. --- ## 🧭 **User Journey Overview** 1. Agents initiates feedback collection chatbot after service interaction. 2. Customer gives a feedback rating (1 to 3 scale). 3. Depending on the rating: - DSAT (Not Satisfied1 or 2): Capture reason and offer callback. - CSAT (Satisfied)3): Thank the customer and end. 4. Store all responses in a Google Sheet and update chat status. --- ## 🤖 ⏳Wati CSAT Automation **Flow :** --- ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image.png) Updated Flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%201.png) Old Flow: ## Customer experience in the CSAT Automation flow: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%202.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%203.png) **Bot Auto closing the chat and ending the chatbot flow once the chatbot flow is completed by customer:** ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%204.png) Updated Journey: ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%205.png) ![image.png](Chat%20CSAT%20and%20DSAT%20Capture%20WATI/image%206.png) ## 🔧 **Flow Components** ### 1. **Initiation** - **Step:** Send Message - **Message:** Hi {{name}}, Can you please share with us your valuable feedback? Instead, it should be this *Hey!, How was your experience with us today?* *A) Satisfied* *B) It was okay/Average* *C) Not Satisfied* --- ### 2. **Tagging & Storage** - **Set Tags:** Mark feedback process started (e.g., `feedback_triggered`) - **Google Spreadsheet:** Record initial engagement - This tag is used to record the agent bot initiation time and also this can be used as the tat for resolving the ticket even if the customer do not fill the feedback options --- ### 3. **Feedback Rating** - **Step:** Button Input - **Message:** Please rate us from 1 to 3 - 1 (Not Satisfied) - 2 (Satisfied) - 3 (Very Satisfied) --- ### 4. **DSAT Handling (Rating 1 or 2)** - **Step:** Button Input - **Message:** We are sorry your experience wasn't great. Could you help us improve by sharing what went wrong? - Yes, Please Call Me - Just Share Feedback - **Step:** Button Input (Detailed Issue) Can you help us understand what went wrong? - Delay in Service - Poor Support - App/Portal Issues - **Storage:** Log issue category and callback preference to Google Sheet - **Tagging:** e.g., `CSAT`, `Feedback`, or `issue_logged` --- ### 5. **CSAT Handling (Rating 3)** - **Step:** Direct conditional path - **Message: @Name,**

---

## #73 — Margin pledge charges
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

## #74 — UPI Autopay Research Doc
**Status:** In progress | **Last edited:** June 19, 2025 3:55 PM

# UPI Autopay Research Doc ## Overview UPI Autopay is a recurring payment feature introduced by the National Payments Corporation of India (NPCI) that enables users to set up automated transactions directly from their bank accounts via UPI. It eliminates manual intervention for periodic payments such as subscription fees, loan EMIs, insurance premiums, and utility bills. Platforms(Decentro, Razorpay, PayU) enhance this system by offering APIs that allow businesses to collect payments seamlessly. Operates via its RBI-approved PA Escrow account, facilitating a hassle-free experience for businesses and end users. Entities with Payment Aggregator licenses are allowed to operate Autopay & Nach products. ## 2. Problem Statements 1. High Manual Dependency – Traditional systems require users to manually authorize each transaction. (Autopay also needs AFA in certain conditions) 2. Complex Onboarding Process – Paper-based mandates like NACH & eNach require time-consuming approvals from banks. 3. Missed or Delayed Payments: Many users forget to make payments on time, leading to penalties, service disruptions, and credit score deterioration. 4. Manual Effort in Recurring Payments: Customers need to remember due dates and manually initiate payments each time, increasing inconvenience. 5. Lack of Flexibility in Modifying Payment Mandates: Existing recurring payment solutions, such as Physical NACH, require users to go through manual procedures for updates or cancellations. 6. Limited Adoption for Small Ticket Payments: High-value recurring payments (such as loan EMIs) have established solutions, but there are limited options for small-ticket payments like OTT subscriptions, utility bills, and microfinance EMIs. ## 3. Use Cases 1. EMI Repayments – Enables NBFCs, banks, and fintech platforms to collect loan EMIs through automated debits. 2. Insurance Premiums – Automates life and general insurance premium collections. 3. Subscription Services – Used by OTT platforms, B2C marketplaces, and SaaS providers for automated payments. 4. Investment Contributions – Supports SIPs and investment-based payments for asset management companies (AMCs) and fintech platforms. 5. Utility Bills – Ensures timely payments for electricity, water, mobile, and broadband services. ## 4. Autopay Features 1. Seamless Recurring Payments – Automates periodic transactions without requiring user intervention. 2. Flexible Scheduling – Users can choose payment intervals such as daily, weekly, monthly, or annually. 3. Instant Mandate Setup – Unlike NACH, which requires days for activation, UPI Autopay works in real-time with UPI PIN authentication. 4. Pre-Debit Notifications – Notify the user in advance before debits occur. 5. User-Controlled Modifications – Allows users to modify, pause, or cancel mandates

---

## #75 — Making Mobile & Email Verification Log Optional LO
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

## #76 — Product note LMS integration with Tally
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

## #77 — Front loading the MF Fetch step in application
**Status:** Not started | **Last edited:** January 8, 2025 9:00 PM

**Problem:**
are we solving?**

Our current application conversion stand at ~14%, while the industry standard for conversion is closure to 70%. We have a lot of ground to cover in our conversion percentage. 

---

**Solution:**
?**

---

## #78 — MFD partner dashbaord Onboarding Rewamp
**Status:** Not started | **Last edited:** January 8, 2025 1:39 PM

# MFD partner dashbaord Onboarding Rewamp ## Current problems -

---

## #79 — [NBFC] DSP Finance Website (Aug25)
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

## #80 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #81 — Testing DSP Comms
**Status:** Pending Review | **Last edited:** January 7, 2025 10:11 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #82 — B2B Partners - New Volt Webhooks
**Status:** Done | **Last edited:** January 6, 2025 6:45 PM

**Problem:**
are we solving?**

1. **Lack of Loan Account Status Updates:** B2B partners like Zype are not notified if a loan account has been successfully created for a user. This leads to delays in servicing their customers effectively.
2. **Absence of Critical Callbacks:** Partners do not receive essential webhooks such as margin shortfall notifications and their aging details, leading to confusion and data disparities across systems.
3. **Missed Updates on Key Events:** Important lifecycle events like foreclosure, lien removal, and repayments are not communicated to B2B partners, hindering their abilit

**Solution:**
?**

---

## #83 — [Platform] Mandate collection BRE optimisation
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

## #84 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #85 — B2B Platform Dashboard v1
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

## #86 — [Platform LSP] All transactions requirements
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

## #87 — [LSP] Total outstanding amount correction and over
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

## #88 — [Platform] Photo verification and liveliness check
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

## #89 — [Platform] QC rejection handling
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

## #90 — [Email Template] Decoupling of Lodgement and Agree
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

## #91 — OPS RM
**Status:** Not started | **Last edited:** January 13, 2025 3:46 PM

# OPS <>RM - Sales team, In progress - ops team receice tickets for the Pre created loan - KT to Sales team to Assign tasks to tech incases of Loan created - Document is needed form the customer that needs to be uploaded on the APP , sales team take it offline and send to ops - As/Es application, Upload form If corrects ops team approves , if the Team rejcets then the RMs are attaching the updated form on the tickets. - OPS team don’t have a way to upload the attached document. Customer needs to attach in APP. - KT to Teach How to use Retool, RM are not checking on the Retool. - DSP repayment - Accounted - Check SOA - Training of Lender delayed and requests. Sales manager to handle and tell how to tell if the Lender needs a document - Sales manager to Learn from Ops team on issues - TATA foreclosure, support team - We need to know the Lien status of the Funds during Lien removal - un- Pledge , Understand the Details from the user - Tata credit Referral , stuck in 1 hr - RMs are connecting are all channel, call, sms, slack sales <>Product January 13, 2025 - DSP drawing power , how it is calculated , 11 lacks in Bajaj to 9 in DSP - How is the DP calculated , - Mandate issues , customer is dropped , why can’t we recreate the Mandate , waiting 24hrs - IT can vary from 5 mins to 24 hrs depending on the bank - KFIN logement issues , - TATA , customer is able to create applications, without eligible limit - Account opening in the DSP - Why is the account opening is delayed

---

## #92 — [CC] Showcase the reason for freezing on CC
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

## #93 — [Platform] Handling of below 1 Rs transactions for
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

## #94 — Offer page - Limit too low
**Status:** In progress | **Last edited:** February 28, 2025 3:51 PM

# Offer page:- Limit too low [MFCentral CAS API Response Structure Analysis](Offer%20page%20-%20Limit%20too%20low/MFCentral%20CAS%20API%20Response%20Structure%20Analysis%201a6e8d3af13a80cf9118d9fa17dfd4e7.md) ### Overview LAMF helps borrowers access financing by offering a **credit line**, where the credit limit is determined as a **percentage of the eligible portfolio value** at the time of the offer. The **eligible portfolio** is retrieved via APIs from mutual fund custodians' RTAs or their joint venture, MF Central. ### **Objective** This document aims to: - Define the process for fetching all **folios associated with an investor**. - List all possible reasons for **folio ineligibility**. - Outline processes for converting **ineligible folios into eligible ones**. - Address **borrower visibility issues** related to folio details. ## **Success Criteria** 1. **First-Time Right Credit Limit %** – This measures customers who fetch their limits once and proceed to take a loan. 2. **Conversion Rate** – Tracking the transition from the offer page to loan creation. 3. **Reduction in Inbound Queries** – Decreasing customer support inquiries regarding missing funds or eligibility issues. ## **Current MFD Process & Challenges** ### **Current Process** - MFDs initiate applications and check the credit limit for the customer. - If the **limit appears low**, they contact RMs for clarification. - RMs advise them to perform a **detailed MFC fetch** to get a comprehensive list of associated funds. - RMs compare the fetched data with the **summary API** and identify missing funds. - If funds are missing, RMs request AMC statements from MFDs to determine why certain folios are ineligible. This process **consumes significant RM bandwidth (15–30 minutes per case).** ### **Key Challenges** 1. **Mismatch in Credit Limit Calculation** - **Detailed API** does not include **lien-eligible units**, and custom logic applied can be inaccurate. - Summary API provides accurate limit but we don’t show the Total portfolio of the user. - This discrepancy **causes customer confusion and increases inbound queries**. 2. **Customer Reluctance to Borrow** - If the limit appears **too low**, MFDs hesitate to proceed with the loan. 3. **High RM Bandwidth Utilization** - RMs spend **significant time** explaining the credit limit and Funds ineligibility. - 16 % of inbound calls were for assisted journeys (966 calls), where the majority of the issues were Limit related. - RMs can spend upwards of 30 mins in collecting and analysing AMC statements and mentioning in-eleigiblity reasons to MFDs 4. **Lack of Visibility for Ineligible Funds** - The current journey only shows **eligible funds**, which may be significantly lower

---

## #95 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #96 — Product note - DRPS
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

## #97 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #98 — Pricing Grid change For B2B2C and Platforms (WIP)
**Status:** In progress | **Last edited:** February 21, 2025 6:02 PM

# Pricing Grid change For B2B2C and Platforms (WIP) Implementation Details: Eligibility: Feature flag-enabled for selected platforms Eligible Platforms: RedVision, Investwell, Prudent, Assetplus, Zfunds, FundsIndia, Advisorkhoj, Compound Express, MFD Direct(B2B2C) partners with Partner ID Not Eligible: Affiliate partners Rates based on Pledged Portfolio amount at Final Agreement stage: < ₹50L: 10.49% =₹50L - <1Cr: 10.35% ≥ ₹1Cr: 10.25% PF : 999 Enhancement : 499 Next Steps: Resolve mandate step issue Complete QA testing Get approvals from Business team Deploy to production **Rates excluding Gst** | **SL Grid** | **ROI** | **PF(Rs.)** | **Enhancement fee(Rs.)** | **AMC(Rs.)** | | --- | --- | --- | --- | --- | | Upto 50L | 10.49% | 999 | 499 | 499 | | 50L-1Cr | 10.35% | 999 | 499 | 499 | | >1cr | 10.25% | 999 | 499 | 499 | | | | | | | what the SL is the Limit Pledged by the customer ? What happens incase of Enhancement or lien removal ? Intrest calculator changes ? AMC? - FAQ How will we collect ? When will we post the AMC charges ? How can we vaive AMC charges ? how can we modify PF and enhancements? Is AMC charges are taken by LSP or DSP? Is AMC is part of SOA? is AMC scheduled in the 2nd year ? Identify the Design screens Identify the messaging sms, Website, WA, email KFS and agreement changes Questions ? When are AMC charges posted - Along with PF ( ~2000 PF) - 1 year after 1 PF * 3 - 1y after PF *2 for a 3 y loan Date of posting? ROI changes based on slabs - Identify the DP range - above the range rate change user registed and take a fetch they select the Funds and select a limit Next screen they see a offer offer contains - PF 999 - AMC 499 - Interest rate 10.49— % Refundablity of AMC if <7 days to foreclose? Annual Maintaince charges AMC Definition - Annual maintenance fee for servicing the loan account - Charged on loan anniversary date - Non-refundable after first 3 days of charging Closure Rules - No pro-rata refund on early closure - Full AMC charged even if closed within year - Next AMC cycle starts from Loan Anniversary date - AMC not applicable if loan is closed or Suspended # ## Billing

---

## #99 — Redemption regret calculator
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

## #100 — Foreclosure payment handling (EOD) repayment in fo
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

## #101 — LSQ data sync
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

## #102 — Phone and Email validation on PLJ
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

On the partner dashboard, we allow MFDs to complete the loan application journey on behalf of customers. During the registration process, we require the MFDs to enter the customer's phone number, email address, PAN, and date of birth. However, we do not currently verify the phone number and email address with OTP, leading to errors and escalations.

**Solution:**
?**

---

## #103 — AA integrations - Fetch journey
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

## #104 — Capture foreclosure reasons from customer
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

## #105 — Comms config - OTP
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?

We have experienced multiple instances of **SMS service provider outages**, which have **impacted critical business operations**. Since SMS was our **only channel** for sending OTPs used in **login and transaction verification**, we introduced **WhatsApp** as a **backup channel** to ensure continuity.

However, SMS service disruptions are **intermittent**, and we want to maintain SMS as the **primary channel** for OTP delivery while using **WhatsApp and Email** as **secondary fallback channels** during downtime. This approach will help ensure **seamless user experience** and *

**Solution:**
s:

OTP delivery settings will be **event-driven** and **fully configurable** through AWS Config, allowing dynamic control without requiring code-level changes.

---

## #106 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #107 — Foreclosure repayment - Handle PenalInterestAccrue
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

## #108 — Handle excess amount in foreclosure request [TCL]
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

## #109 — In app user review [Play store]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

We currently do not collect user experience feedback directly at key moments in the app journey, which has led to the following challenges. 

- **Missed Pain Points:** Without timely feedback, we risk missing critical pain points during specific stages of the app journey, such as loan applications, payments, or withdrawals. These missed insights can result in unresolved issues, leading to decreased user satisfaction.
- **Lost Improvement Opportunities:** Journey-based feedback offers real-time insights into what’s working and what needs improvement. Without this feedback, we

**Solution:**
?**

---

## #110 — Interest feature handling for TCL
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

## #111 — LAS LMS approach notes
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

# LAS LMS approach notes # Summary: We are planning to launch LAS (Loan Against Securities) for the B2B2C channel, targeting the first 1,000 customers(10 application per day) to measure adoption and define success metrics. For Phase 1, the objective is to enable this launch with minimal changes to the existing product experience. Key considerations: No changes for users who have only a LAMF (Loan Against Mutual Funds) account. No changes in the loan servicing experience for users with only an LAS account. For users holding both LAS and LAMF accounts, we will adopt an “elevate approach” (In elegant way) to effectively manage multiple loan accounts within the same interface. ## LMS service scenarios ### Customer with only LAMF account 1. No change in existing behaviour, flow and configurations ### Customer with only LAS account Expected changes in existing modules | **Modules** | Requirements | Edge cases scenarios | Action items | | --- | --- | --- | --- | | Lodgement + Account opening | 1. For LAS, this is expected that pledge confirmation may take 3-4 days. and hence we shouldn’t allow to place disbursal request immediately after loan application is completed 2. We need to show Account setup status along with helper text with expected TAT on dashboard to customer | 1. Handling of LAS specific account opening status on UI 2. Non STP flow 3. Partial pledge confirmation 4. Partial lodgement | 1.Account status life cycle 2. Account status scenarios | | Disbursal | 1. No change in existing user experience(UI/UX) 2. LAS specific Validations will be applicable 3. TAT BRE for LAS will same as LAMF | - In what cases disbursal can be rejected? | 1. Validations: - Based on Account status - Min amount allowed 2. TAT BRE for LAS 3. Lifecycle management on UI + comms | | Principal Repayment | No change | | | | Transactions | No change | | | | Lien removal | 1. Lien removal entry point: No change 2. Pledged collateral list: LAS specific Data points 3. Un-pledge request validation: No change 4. Un-pledge request lifecycle handling: No change in UI/UX (Data points will be LAS specific) | - Data points to show collateral details - Allowable qty criteria - Rejections cases | | | Line enhancement | Line enhancement is not a part of Phase 1 Launch | NA | | | Collateral

---

## #112 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #113 — Mandate registration post loan
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

## #114 — Project Elevate - LMS
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

## #115 — Rounding of Accrued Interest before Posting bill a
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

## #116 — TCL foreclosure API integration
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

## #117 — Untitled
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

# Untitled ```mermaid flowchart TD A[User Login] --> B{Account Status Check} B --> C[Only LAS Account] B --> D[Only LAMF Account] B --> E[Both Accounts] B --> F[No Accounts] %% Only LAS Flow C --> C1[LAS Dashboard] C1 --> C2{User Action} C2 --> C3[View Account Details] C2 --> C4[Make Repayment] C2 --> C5[Top Up Collateral] C2 --> C6[Apply for LAMF] C2 --> C7[View Statements] C6 --> G[LAMF Application Flow] G --> G1[Document Upload] G1 --> G2[Verification] G2 --> G3[Approval/Rejection] G3 --> |Approved| H[Dual Account User] G3 --> |Rejected| C1 %% Only LAMF Flow D --> D1[LAMF Dashboard] D1 --> D2{User Action} D2 --> D3[View Account Details] D2 --> D4[Make EMI Payment] D2 --> D5[Top Up Collateral] D2 --> D6[Apply for LAS] D2 --> D7[View Statements] D6 --> I[LAS Application Flow] I --> I1[Collateral Setup] I1 --> I2[Verification] I2 --> I3[Approval/Rejection] I3 --> |Approved| H I3 --> |Rejected| D1 %% Both Accounts Flow E --> H[Unified Dashboard] H --> H1{Account Selection} H1 --> H2[LAS View] H1 --> H3[LAMF View] H1 --> H4[Combined View] H2 --> H5{LAS Actions} H5 --> H6[LAS Account Details] H5 --> H7[LAS Repayment] H5 --> H8[LAS Top Up] H5 --> H9[Switch to LAMF] H3 --> H10{LAMF Actions} H10 --> H11[LAMF Account Details] H10 --> H12[LAMF EMI Payment] H10 --> H13[LAMF Top Up] H10 --> H14[Switch to LAS] H4 --> H15{Combined Actions} H15 --> H16[Cross-Account Summary] H15 --> H17[Unified Repayment] H15 --> H18[Portfolio Analysis] H15 --> H19[Recommendations] %% No Accounts Flow F --> F1[Welcome Screen] F1 --> F2{Product Selection} F2 --> F3[Apply for LAS] F2 --> F4[Apply for LAMF] F2 --> F5[Learn More] F3 --> J[LAS Onboarding] F4 --> K[LAMF Onboarding] %% Common Flows C4 --> L[Repayment Flow] D4 --> L H7 --> L H12 --> L H17 --> M[Multi-Account Repayment] L --> L1[Select Amount] L1 --> L2[Choose Payment Method] L2 --> L3[Confirm Payment] L3 --> L4[Payment Processing] L4 --> L5{Payment Result} L5 --> |Success| L6[Success Screen] L5 --> |Failed| L7[Error Handling] M --> M1[Allocate Amount] M1 --> M2[Choose Payment Method] M2 --> M3[Confirm Split Payment] M3 --> L4 C5 --> N[Top Up Flow] D5 --> N H8 --> N H13 --> N N --> N1[Select Collateral Type] N1 --> N2[Enter Amount/Quantity] N2 --> N3[Verify Collateral] N3 --> N4[Confirm Top Up] N4 --> N5[Processing] N5 --> N6{Result} N6 --> |Success| N7[Success Screen] N6 --> |Failed| N8[Error Handling] %% Support & Help C1 --> O[Help Center] D1 --> O H

---

## #118 — Volt Apps & Web Multiple Loan Handling - Launching
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

## #119 — Volt Mandate re-registration Post loan
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

## #120 — [DSP] SMA & NPA Tagging at Customer Level
**Status:** Done | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

This document outlines the requirements for implementing Special Mention Account (SMA) and Non-Performing Asset (NPA) classification system. The system (Finflux) will automatically classify customer accounts based on Days Past Due (DPD) and manage the lifecycle of these classifications.

**Solution:**
?**

---

## #121 — End to end API Documentation
**Status:** Not started | **Last edited:** February 12, 2025 5:50 PM

**Problem:**
are we solving?**

We currently lack documentation that logs all the APIs used in the flow, their purpose, and the request and response details. This results in significant time spent during debugging or when trying to understand the flow and APIs.

---

**Solution:**
?**

---

## #122 — Attribution for Volt applications
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

## #123 — Reducing Limit on DSP from 25K
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

## #124 — Volt LOS journey optimisations
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

## #125 — Lead prioritisation in LSQ
**Status:** In progress | **Last edited:** December 3, 2024 3:45 PM

# Lead prioritisation in LSQ volt is loan against MF , targeting customers in india , ususlly 25 k to 1 cr - Lead Generation - Lead Capture - Lead qualification - Lead nurturing - Sales qualified Lead - Opportunity - Closed

---

## #126 — [B2B2C] Improving lead quality in partner journey
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

## #127 — Skip Email verification
**Status:** Not started | **Last edited:** December 29, 2025 11:59 AM

**Problem:**
are we solving?**

Email verification is currently mandatory for loan application creation. However, we’re seeing around 15% **user drop-off** at this step. To reduce friction, we propose letting users **choose their preferred primary communication channel — SMS or Email** — and **skip email verification** for those who select SMS. This allows users who rely on SMS to continue without being blocked by email OTP verification.

---

**Solution:**
?**

---

## #128 — Show accrued interest on UI
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

## #129 — [Platform] Liveliness check
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

## #130 — LSQ Service Desk
**Status:** Not started | **Last edited:** December 24, 2025 11:59 AM

# LSQ Service Desk ## **1. Overview** **Objective:** Phase 1 focuses on building an LSQ-based internal Service Desk that enables structured internal ticketing, SLA management, and Jira integration. **Scope Includes:** - Jira Integration with LSQ - Internal Ticket Management (Sales, Support, Ops) - Ticket Creation & Assignment Logic - Volt Operations Team Workflow - Email Integration (Phase-ready foundation) ## [Jira Integration on LSQ Service desk](LSQ%20Service%20Desk/Jira%20Integration%20on%20LSQ%20Service%20desk%202aee8d3af13a80e8a5f7c0b8e990256a.md) [Support Requirement](LSQ%20Service%20Desk/Support%20Requirement%202aee8d3af13a80e3ae45c08bfa32a8bf.md) [Volt Ops Requirements The child ticket will be created and assigned to Volt Ops.](LSQ%20Service%20Desk/Volt%20Ops%20Requirements%20The%20child%20ticket%20will%20be%20cre%202afe8d3af13a80b9be04e4c2eb5d9880.md) # **3. Internal Ticketing Framework:** This section defines the **complete ticket lifecycle** for the LSQ Service Desk used by Support, Sales, and Operations teams. It covers how a ticket is created, assigned, triaged, escalated (Volt Ops, Product, Lender), and resolved, including SLA behaviour, parent–child ticket logic, and exception handling. # **Actively Involved** - **Customer / MFD** - **Agent (Chat / Email / Calling)** - **System (LSQ Automations & Integrations)** - **Volt Ops Team** - **Product / Tech (via Jira)** - **Lender Partners** # **Ticket Lifecycle Overview** A ticket progresses through the following high-level stages: 1. **Intake & Ticket Creation** 2. **Classification** 3. **Work / Investigation** 4. **Child Ticket Creation (Volt Ops / Product / Tech / Lender)** 5. **Resolution & Customer Validation** 6. **Closure & CSAT** 7. **Reopen, RCA** # **Detailed Step-by-Step Ticket Flow** ## **In Take & Ticket Creation** 1. **Customer initiates contact** via Chat, Call, Email 2. **System identifies the customer** - If contact exists → attach to contact. - If new → create new contact with basic details. Use cases where a ticket will be created and a ticket will not be created: | Channel | Scenario | Condition | Ticket? | Notes | | --- | --- | --- | --- | --- | | Call | Registered number call | Lead exists | YES | Auto-link ticket to lead; capture disposition. | | Call | Unregistered number call | Lead not found | YES | Capture disposiiton and Create new ticket. | | Call | Telemarketing calls | | NO | Mark as Spam | | Call | Missed call from registered number | Customer dropped | YES | New Ticket with status open with associated lead | | Call | Missed call from non registered number | Customer dropped | YES | New Ticket with status open | | Email | Any email sent to support@ | Incoming email | YES | LSQ

---

## #131 — LAS LOS
**Status:** Not started | **Last edited:** December 21, 2025 12:48 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #132 — [Platform] Risk report
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

## #133 — Product Note
**Status:** Done | **Last edited:** December 18, 2025 11:28 PM

**In scope:**
- What specific problems are we solving?
- Who are we solving it for? Consider both primary and secondary users

# Product Note ## **Background and Context** - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? --- ## **1. Problem scope** ### In scope - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) --- ## **3. Solution Scope** ### Solution overview Explain in 2-3 lines the overview of the solution - Explain overview of the solution with key product and system changes - Explain the rationale on scoping/phasing of the solution - Call out scope that has been scoped out and explain the rationale ### Detailed solution scope: Bullet list of user and system use cases that are supported: - Define all use cases applicable and what are in scope - Core happy path - Key edge cases that must be handled at launch - Consider all the stakeholders that are impacted - Has to answer questions like: - How does this change existing operational SOPs? - How does this change the experience for the end user? - How does this impact sales or onboarding conversations? | Description | Details | | --- | --- | | | | | | | | | | --- ## **5. High level s***ystem or user interaction flow* - Cover the overview of the process or the journey - Exclude error cases or edge cases

---

## #134 — MF Fetch optimizations
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

## #135 — Lead stage handling on LSQ
**Status:** Not started | **Last edited:** December 13, 2024 11:58 AM

# Lead stage handling on LSQ Lead stages in LSQ Initial Registration Stages: 1. Unregistered 2. Registered Portfolio Stages: 3. Portfolio Fetch 4. Portfolio Fetch KFIN 5. Portfolio Fetch CAMS 6. Portfolio Pledge 7. Portfolio Pledge KFIN 8. Portfolio Pledge CAMS Application Processing Stages: 9. KYC Verification 10. Sign Agreement 11. Link bank account 12. Setup Mandate 13. Verify Photo 14. Application Submitted 15. Loan Created 16. Empaneled Final Status Stages: 17. Partially activated 18. Activated 19. Closed

---

## #136 — User engagement on the LSQ
**Status:** Not started | **Last edited:** December 12, 2024 5:55 PM

# User engagement on the LSQ Currently issues # Ticketing System Requirements & Workflow Chief Product Officer Document | December 2024 ## Executive Summary Our current ticketing infrastructure needs a significant overhaul to address critical gaps in issue tracking, resolution monitoring, and customer service delivery across multiple channels. This document outlines the requirements for a new unified ticketing system that will serve our diverse user base and improve operational efficiency. ## Current Pain Points Analysis 1. Issue Resolution Tracking - No unified system to track resolution progress - Limited visibility into resolution time frames - Inability to measure team performance effectively 2. Organizational Context - Disconnected systems leading to fragmented customer context - Multiple tools (Exotel, RUNO, Retool, LSQ CRM, Zendesk) creating data silos - Limited cross-functional visibility 3. Support Coverage - Backup handling inefficiencies - Lack of structured handover processes - No clear escalation matrices 4. Performance Metrics - Missing TAT (Turn Around Time) tracking at issue level - No trend analysis capabilities - Unable to identify recurring issues and root causes ## Core Requirements ### Ticket Creation & Management 1. Mandatory Ticket Creation - 100% ticket creation for all customer interactions - Channels: Phone calls, WhatsApp, Email - Required fields: Partner ID, Issue Category, Description - Clear resolution confirmation before ticket closure 2. Channel-Specific Workflows - MFD Channel specific routing rules - Direct customer support workflow - B2B partner interface requirements 3. SLA Management - Channel-specific SLA definitions - Real-time SLA tracking - Escalation workflows - Performance dashboards ### User Management & Access Control 1. Internal Users - MFD Channel Team (5 RMs, 2 backup RMs, 2 Chat support) - Support Channel Team (10 agents) - Sales Team (7 members) - Ops and Tech on-call teams - Admin users 2. External Users - Direct MFDs - Platform MFDs - B2C customers - B2B platform partners ### Integration Requirements 1. Communication Systems - Exotel for call routing - RUNO for call visibility - Periskope and WATI for WhatsApp - Email integration 2. Internal Systems - Retool for DB state visibility - LSQ CRM - Slack for internal communications ## Key Features 1. Unified Dashboard - Single view of customer interactions - Real-time status tracking - SLA monitoring - Team performance metrics 2. Analytics & Reporting - Issue frequency analysis - Resolution time tracking - Team performance metrics - Channel-wise analysis - Custom report generation 3. Workflow Automation - Automatic

---

## #137 — Volt DLS 2 0
**Status:** In progress | **Last edited:** December 12, 2024 1:59 PM

# Volt DLS 2.0 # Why —————————————————— - Reduce front end effort to create new features and products - Reduce effort of maintaining multiple DLS - Faster design + dev time: Faster decision making and alignment on design - Significantly higher consistency - Easier onboarding for new joinees <aside> 🎯 **Goal:** To create a singular org level DLS that helps build all our products: Core, web, dashboards, command center, etc. </aside> # What —————————————————— ### Process 1. Brand positioning doc - : *in progress* [Brand Positioning Doc](Volt%20DLS%202%200/Brand%20Positioning%20Doc%207b616b64989b4dd68419a624c15997eb.md) 2. User research: *in progress* 3. Market research/Competitor analysis - benchmarking [Market research](Volt%20DLS%202%200/Market%20research%20856a208a18e54d899487aa1703345e80.md) 4. Heuristic evaluation of current design 5. Finalise tokens 1. Keyword mapping 2. Options 1. UI language 2. Typography scale + tokens 3. Color scale + tokens 4. Components In-depth implementation [WIP]: [https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1h0oju4JeUEeljtEJnrhdD5nIc9nrlzBwNRhAHvMU5YI/edit?usp=sharing) ## Scope [Scope](Volt%20DLS%202%200/Scope%20ad8083b8d6fd44fa8e0d2d347d7c5fe0.md) **Tokenization representation** - L3: Mapped - L2: Alias - L1: Primitives [https://thedesignsystem.guide/design-tokens](https://thedesignsystem.guide/design-tokens) [https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676](https://medium.com/eightshapes-llc/naming-tokens-in-design-systems-9e86c7444676) ![image.png](Volt%20DLS%202%200/image.png) ## ⛳️ Typography scale - Ability to update Heading font style separately than Body - Allow having capitalisation in subheaders, tags etc - Allow using singular token for a style which auto switches between mobile (14px), web, MFD, DSP (16px), command center (12px) ### **How →** - Primitives: xs, sm, md, lg… ,etc. - Alias (Text styles) - Tokens: H1, H2, H3, H4… B1, B2, B3, B4… - Theme: Core-mobile, Core-web, DSP-mobile, DSP-web ## ⛳️ Color scale - Allow switching themes for light and dark mode - Allow switching primary, secondary, success, etc colors for different products/brands/SDKs - Allow modifying individual component level colors. Eg: borders, CTAs, headings, secondary text, disabled, etc ### **How (WIP) →** - Primitives: blue (50, 100, 200…900), turquoise (50, 100, 200… 900)… red (50, 100… 900) - Alias - Primary (50, 100… 900), Secondary (50, 100… 900), Success (50, 100… 900) - Theme: Core, DSP - Mapped - Types: - Text (primary, secondary, action, disabled, success, warning…) - Surface (background, primary, secondary, info, action…) - Border (primary, secondary, warning, error…) - Icon (primary, action, error…) - Theme: Light, Dark ## ⛳️ Component level - Allow switching component styles (corner radius, padding, color…etc.) for different use-cases: Core, DSP, dashboards, command center etc. ### Priority components: 1. Top header bars 2. Buttons 3. Bottom sheet 4. Input fields 5. Form logic + behaviour 6. Bottom nav bars 7. Toasts, notification 8. Tabs - Refer to small case filter screen + chips + tabs inside MF selection 9.

---

## #138 — Single drawdown Term Loan LMS Requirements
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

## #139 — PRD - Capturing UTM-Based parameters for acquisiti
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

## #140 — SL updation & additional limit calculation optimis
**Status:** On Hold | **Last edited:** August 27, 2024 5:20 PM

**Problem:**
are we solving?**

For users who are undergoing line enhancement and loan renewal flow, when we are calculating the additional limit, then we are not considering the increased value of the already pledged portfolio in calculation of SL in front-end

---

**Solution:**
?**

---

## #141 — [DSP] Dues collection comms
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

## #142 — Productisation of admin tool Change email address
**Status:** Not started | **Last edited:** August 21, 2024 12:14 PM

**Problem:**
are we solving?**

- When customers need to change their email or mobile number, they need to send the details to the RMs to be updated via registered email. This may cause manual errors at the customer and RMs end due to absence of validation of email and phone number.
- The admin tool for these changes cannot be used in isolation and requires communication with all third parties involved after the Loan account is created.

---

**Solution:**
?**

---

## #143 — LSQ Revamp
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

## #144 — NBFC NACH Mandate Limit Change
**Status:** Ready for Tech | **Last edited:** August 13, 2025 6:31 PM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit line, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries.

**Solution:**
?**

---

## #145 — [DSP] KYC v2 (including CKYC)
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

## #146 — [Platform] Validation to Stop Un-pledging, closure
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

## #147 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #148 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #149 — MNRL Compliance Validation Integration
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

## #150 — NSDL PAN integration
**Status:** Not started | **Last edited:** April 29, 2026 5:11 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #151 — Product Note – DRPS (Final Version – Unified Forma
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

## #152 — B2B2C call incoming reduction
**Status:** In progress | **Last edited:** April 17, 2025 11:41 AM

# B2B2C call incoming reduction [Takeaways from Call analysis ](B2B2C%20call%20incoming%20reduction/Takeaways%20from%20Call%20analysis%201d0e8d3af13a801c8684fe6a207f97d7.md) [](B2B2C%20call%20incoming%20reduction/Untitled%201d8e8d3af13a803d92e9cdb6778f4809.md) # Detailed Breakdown of Customer Call Issues ## Loan Application Issues - **Withdrawal Process Assistance (80 calls)**: Customers frequently struggle with the loan withdrawal process after approval. - They face confusion about where and how to initiate withdrawals, authentication requirements, and processing times. - Many calls include statements like: *"I can see my loan is approved but I don't understand where to click to get my money"* or *"The withdrawal button is grayed out even though my loan shows as approved."* - The withdrawal interface appears to lack clear instructions for first-time users. - **OTP Issues (75 calls)**: One-time password delivery and acceptance is a major friction point in the application process. - Customers report: *"I never received the OTP message"*, *"The system says my OTP is invalid even though I'm entering exactly what was sent"*, and *"The OTP expires too quickly before I can enter it."* - This frequently blocks application completion and creates frustration as customers must repeatedly request new OTPs. - **Processing Fee Calculation (70 calls)**: Customers express confusion about fee calculations, particularly when the final disbursed amount differs from expectations. - Common complaints include: *"The fee was higher than what was initially shown"* and *"I don't understand why GST is calculated separately after I agreed to the loan terms."* - The fee structure appears to be disclosed incompletely during the application process. - **Loan Eligibility Questions (40 calls)**: Prospective borrowers frequently call with confusion about eligibility requirements. - They mention: *"The website shows different criteria than what the agent told me"* and *"I was rejected but don't understand why since I meet all the listed requirements."* - The eligibility criteria seem inconsistently communicated across different channels. - **Application Timeout Errors (35 calls)**: Users report sessions expiring mid-application, forcing them to restart the process. - Typical complaints include: *"I had filled out everything and when I clicked next, it said my session expired"* and *"The application keeps timing out when I'm uploading documents."* - These timeouts appear to occur most frequently during document upload or verification steps. Payment Processing Issues - **Partner Payout Delays (65 calls)**: Affiliate partners frequently report delayed commission payments. - Partners state: *"It's been three months since I was supposed to receive my commission"* and *"The dashboard shows payments as 'processed' but nothing has arrived in my account."* - These delays severely

---

## #153 — Bajaj compliance requirement - 4th April 2024
**Status:** In progress | **Last edited:** April 10, 2024 9:13 AM

**Problem:**
are we solving?**

Compliance issues for Bajaj

---

**Solution:**
?**

---

## #154 — Website meta description change
**Status:** Unknown | **Last edited:** Unknown

# Website meta description change Benchmarking for: Deliver crisp view of our offering to the user while maintaining/improving SEO Person: Saksham Srivastava **Lalit’s pointers:** most trusted platform to get instant loan (overdraft) against MF and shares. Very low interest rate of 9-11% | No preclosure charges | 100% digital 5 minute process | Funds in 4 business hours 1. Trust 2. Preclosure charges 3. Quick and easy process Benchmarking | Page | Headling | Meta description | Remarks | | --- | --- | --- | --- | | Smallcase | Loan against mutual funds | Low-interest ***loan against*** MF — Need ***loan*** for personal use? Get 10.75% PA ***loan against mutual funds*** on smallcase. Try now. Flexible Repayment terms. No Credit Score needed. No Foreclosure charges. | - Tries to explain the complete functionality - Personal use add comparison point for the use. - The | | SBI | Get Loan Against Mutual Fund Units Online in India | Get ***Loan Against Mutual Fund*** Units Online in India at SBI. Look for various features which contain the minimum & maximum amount, interest rates & renewals. | | | HDFC Bank | **Loan Against Securities** | Get up to 80% of the value of your ***securities against*** a wide range of collaterals, including shares, ***mutual funds***, life insurance policies, bonds, etc. | - LTV mentioned can be a key attraction | | Bajaj Finserv | **Loan Against Mutual Funds (LAMF) up to Rs. 5 crore** | Apply for a ***Loan Against Mutual Funds*** with a minimum fund value of Rs. 50000, and get a loan limit of up to Rs. 5 crores at attractive rates. | | | ICICI Bank | [**Insta Loan Against Mutual Funds | Online Loans**](https://www.icicibank.com/personal-banking/loans/loan-against-securities/mutual-funds) | Now avail of Insta ***Loan Against Mutual Funds*** in just a few minutes! You can now avail of paperless and instant liquidity against your mutual funds through ... | | | FundsIndia | [**Loan Against Mutual Funds, Eligibility, Benefits and Features**](https://www.fundsindia.com/loan-against-mutual-funds) | Raise instant funds online with ***loan against mutual funds*** at just 9% p.a Interest rate. 100% digital process with Mirae Asset Financial Services. | | | Volt Money | [**Volt Money | Instant loan against mutual funds and stocks**](https://voltmoney.in/) | Get credit line/OD limit ***against mutual funds*** starting at 9.95% per annum with trusted lenders in less than 5 minutes. | | Following are the options for headline

---

## #155 — Coms strategy
**Status:** Unknown | **Last edited:** Unknown

# Coms strategy @Naman Agarwal Creating a comprehensive **Communications (Comms) Review Plan** is essential to ensure that all outbound communications are effective, targeted, and free from errors that could lead to customer confusion or dissatisfaction. Below is a structured plan addressing your requirements, along with best practices and industry references to guide implementation. [MFD comms ](Coms%20strategy/MFD%20comms%20120e8d3af13a808297c1f3ec8ab11109.md) --- ## **1. Identify All Outbound Communications** ### **1.1. Inventory of Outbound Channels** - **Email Campaigns:** Promotional, transactional, newsletters. - **SMS Notifications:** Alerts, reminders, confirmations. - **Push Notifications:** Mobile app alerts. - **WhatsApp Messages:** Customer support, updates. - **Social Media Posts:** Announcements, engagements. - **In-App Messages:** User guidance, feature updates. - **Direct Mail:** Physical correspondence for critical communications. ### **1.2. Catalog Existing Communications** - **Create a Communication Matrix:** List all outbound messages, their purpose, channels used, frequency, and responsible teams. - **Regular Audits:** Schedule periodic reviews to update the communication matrix. --- ## **2. Define Trigger Conditions** ### **2.1. Event-Based Triggers** - **Transactional Events:** Payment confirmations, account changes. - **Behavioral Triggers:** Abandoned cart, inactivity alerts. - **System Events:** Downtime notifications, maintenance alerts. ### **2.2. Customer Lifecycle Triggers** - **Onboarding:** Welcome messages, setup guides. - **Milestones:** Anniversary messages, loyalty rewards. - **Churn Prevention:** Re-engagement campaigns. ### **2.3. Define Clear Criteria** - **Specific Conditions:** Clearly outline what event or behavior triggers each communication. - **Thresholds:** Set limits (e.g., number of failed transactions before sending a warning). --- ## **3. Identify Target Customers** ### **3.1. Segmentation** - **Demographics:** Age, location, gender. - **Behavioral Data:** Purchase history, engagement level. - **Psychographics:** Interests, values. ### **3.2. Data Collection and Analysis** - **CRM Systems:** Utilize customer relationship management tools to gather and analyze customer data. - **Behavioral Analytics:** Track and interpret customer interactions across channels. ### **3.3. Continuous Updating** - **Dynamic Segmentation:** Regularly update customer segments based on new data. - **Feedback Loops:** Incorporate customer feedback to refine target groups. --- ## **4. Crafting the Message Text** ### **4.1. Clarity and Conciseness** - **Clear Language:** Avoid jargon; use simple, direct language. - **Concise Messaging:** Communicate the essential information without unnecessary details. ### **4.2. Personalization** - **Use Customer Names:** Personalize messages to increase engagement. - **Tailored Content:** Customize messages based on customer segment and behavior. ### **4.3. Actionable Instructions** - **Next Steps:** Clearly outline what the customer should do next. - **Links and Resources:** Provide direct links for actions like payment or support. ### **4.4. Compliance and Sensitivity** - **Regulatory Compliance:**

---

## #156 — Biometrics addition of 2 screens
**Status:** Developed | **Last edited:** Unknown

# Biometrics addition of 2 screens Charter: LOS Pod # Context We need to add permissions and error pop up for biometrics # Process benchmark design # Figma [https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3591-8894&t=kzwBhN3rHeElEoxX-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3591-8894&t=kzwBhN3rHeElEoxX-11&embed-host=notion&footer=false&theme=system)

---

## #157 — CKYC Flow integration
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC Flow integration Charter: LOS Pod # Context [[Lending stack] KYC Flow](../PRDs/PRDs/%5BLending%20stack%5D%20KYC%20Flow%20f322514482d7490dbcf3675515b16276.md) # Process - [x] Map flow - [x] Scope out screens - [x] Benchmarking on flows # Figma xhttps://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3740-1840&t=182AaW1ur1jUPPnI-11 https://www.figma.com/design/khuVsTb01ruke7QxxOuCYR/Animation?node-id=4-1425&t=xNwnuqSfvRvHUnP7-11

---

## #158 — CKYC New flow
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC New flow Charter: LOS Pod Priority: P0 Task type: Sprint # Context Need to work on creating a loader for CKYC flow which would last 10-12s # Process - [x] Selfie screen illustrations - [x] Wireframes for loader - [ ] Final Design # Figma https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=5170-7847&t=zvlUVrpOudLY6mV1-11

---

## #159 — Compliance changes in loan offer screen
**Status:** Ready for kickoff | **Last edited:** Unknown

# Compliance changes in loan offer screen Charter: LOS Pod Priority: P0 # Context Have to make the following changes on the loan offer page, this will be specific for DSP: 1. Remove (excl. GST) from One time charges. 2. Add another line item in the One time charges collapse menu. Add this below the "Processing fees" item; "GST at 18%" and show the value. 3. Have to include a disclaimer that "Account creation/withdrawals are subject to lender approval" # Process # Figma [https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3465-1374&t=5rViOPN4vsihc8N9-11&embed-host=notion&footer=false&theme=system)

---

## #160 — Volt Plugin Knowledge Base
**Status:** Unknown | **Last edited:** Unknown

# Volt Plugin Knowledge Base # Introduction This project aims to build a unified UX writing system for Volt based on fintech best practices. The goal is to have a unified, brand-aligned tone of voice across screens, touchpoints, and teams. ## Problem - Right now we handle error case copies differently throughout the app. - Different writers/designers use different tones, leading to a fragmented experience. - No shared rules for writing error messages, CTAs, success screens, etc. - Designers or PMs often write placeholder text or inconsistent copy due to lack of writing support & time constraints. ## Solution A self-serve figma plugin where anyone can write first version of the copy that’s on-brand, on-tone, and compliant without needing support ## Approach - Align stakeholders on a unified brand voice - Setup brand voice guidlines (Tone) for cases like success, error, New features and so on. - Present guidelines that will be used as the first config for the figma app - Create the figma plugin with the help of Devs - Present a working model, to stakeholders - Take feedback and iterate if necessary - Replace copy throughout app using the figma plugin ## Brand Voice Based on the conversation with Lalit this is what volt stands for. based on these I want to define what the tone of language we want through out the app. - Call with Lalit on volt brand 1. If volt was a person how would you describe it? 1. Supportive 2. Reliable and Fast to help 3. Motivating 4. Enabler to achieve your financial needs 5. A saviour when you need most 2. Describe Volt in 3-4 words 1. Transparent, Trustworthy, Easy, Fast <aside> 💡 **Interacting with Volt should feel like:** Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless. - **Like a smart, supportive money guide** - **Your effortless, goal-driven money companion** </aside> Voice: **Smart, Supportive, Calm, and Clear.** <aside> 💡 Volt speaks like a modern financial guide — someone who knows money inside out, and explains it with warmth & clarity, not jargon. </aside> ## Scenarios / Possible Usecases - Error like PAN verification failed, No CKYC data found and so on - Success like Completion of Payment, Loan application, Increase limit and so on - Onboarding like App screenshots

---

## #161 — FE screen revamp
**Status:** Ready for kickoff | **Last edited:** Unknown

# FE screen revamp Charter: Design Initiatives Priority: P0 ## Tracker LMS https://docs.google.com/spreadsheets/d/1WjZgF-ThWm5-GuLZMDGNnvw5aCT7hQ6e5yxC_EDnoCo/edit?gid=0#gid=0 LOS https://docs.google.com/spreadsheets/d/1NWUmp6-7xX579K1hsehy1tmnkeXTIH_k99rS6Rzy27o/edit?gid=0#gid=0 28/01 - Transaction screen - Account + Profile - LMS home screen states: All notification components, interest due 10/01 Design link: [https://www.figma.com/design/DH8rc6N6qcZ9miF0fv3ILt/Design-system?node-id=2707-36&p=f&t=gPYwv9I0fBY9CrGl-11](https://www.figma.com/design/DH8rc6N6qcZ9miF0fv3ILt/Design-system?node-id=2707-36&p=f&t=gPYwv9I0fBY9CrGl-11) - Start working token implementation for LOS + LMS screens - Update older components - Let frontend pod execute 19/12 Pending: - Documentation and usage of tokens - Improve token naming - PRD to start Update - Token architecture finalised and implemented on Figma and sheet @Vinit Pramod Sarode How do we want to go about the re-vamp LOS revamp

---

## #162 — Figma file arrangement
**Status:** Developed | **Last edited:** Unknown

# Figma file arrangement Charter: Design Initiatives Priority: P0 # Context | Reduction of gap between Figma and prod with better file arrangement and management | | | --- | --- | # Process - [ ] Create Figma file framework - [ ] Add all LMS figma files in the same framework - [ ] Work with Ranjan/Tanmay to understand and mapp all LMS flows - [ ] Arrange all LMS flows in figma new DLS - [ ] Repeat for LOS # Figma

---

## #163 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #164 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #165 — Loan account creation error handling
**Status:** Ready for kickoff | **Last edited:** Unknown

# Loan account creation error handling Charter: LOS Pod # Context MOM 1. Active loan + Cibil score reason 2. Redirect users to try with another PAN [tentative] 3. Handle in pop up if possible 4. Feedback after the pop up in the flow # Figma [https://embed.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/%5BOLD%5D-Loan-application-flow?node-id=11844-61349&t=r1DgLWQIr5SO6puF-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/%5BOLD%5D-Loan-application-flow?node-id=11844-61349&t=r1DgLWQIr5SO6puF-11&embed-host=notion&footer=false&theme=system) Loan profile did not meet out criteria for a loan account. Last checked eligibility on 12/02/24

---

## #166 — Loan foreclosure reasons
**Status:** Developed | **Last edited:** Unknown

# Loan foreclosure reasons Assign: Karuna Sankolli Charter: LMS Pod # Context - [x] Get list of reasons from Ranjan - [x] Make a table with what we will sell for every reason selected. - [x] Redesign FAQs page - [ ] Work with Ranjan for the FAQs page - [ ] Foreclosure landing page 3 options - [ ] Reasons for foreclosure 3 options - [ ] Reconsider page 3 options - [ ] Status of payment page 3 component 3 options - [ ] Last tracking foreclosure page options - [ ] Ability to cancel foreclosure --- [Capture foreclosure reasons from customer](../PRDs/PRDs/Capture%20foreclosure%20reasons%20from%20customer%20170e8d3af13a80ec8d7bff6a6e988d1f.md) ‣ # Figma [https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/x1rDpxstHSGXbMjQTtGvtR/Loan-foreclosure?node-id=76-782&t=QT6CT98ArDhDQ4Fy-11&embed-host=notion&footer=false&theme=system)

---

## #167 — Pre fetch optimisation
**Status:** Ready for kickoff | **Last edited:** Unknown

# Pre fetch optimisation Charter: LOS Pod Priority: P0 Task type: Sprint # Context - Need replace DOB input with mobile number before MFC fetch since it is unnecessary and has drop offs - [Pre-fetch flow Optimisation: Consolidating PAN flow](../PRDs/PRDs/Pre-fetch%20flow%20Optimisation%20Consolidating%20PAN%20flow%20207e8d3af13a80e2b744f8bd135a6319.md) # Process # Figma

---

## #168 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #169 — Events
**Status:** Unknown | **Last edited:** Unknown

# Events Below is an event strategy document for Volt Money, based on the flow and details you provided. The table format includes event name, priority, expected values, and comments on the event's current status. This document is structured to track events from user interactions to backend processes. --- ### Event Strategy Document for Volt Money Certainly! Below is a comprehensive table that outlines the various user flows, actions, corresponding event names, detailed descriptions, and the user journeys they belong to. This should help in tracking and understanding user interactions within your application. | **User Flow** | **User Action** | **Event Name** | **Description** | **User Journey** | | --- | --- | --- | --- | --- | | **Onboarding** | User views onboarding page | ONBOARDING_PAGE_VIEWED | The user has viewed the onboarding page. | Onboarding | | **Onboarding** | First time the app is loaded | LAUNCH_PAGE_VIEWED | The user has launched the app for the first time and viewed the splash screen. | Onboarding | | **Signup** | User Signup on Volt Android | SIGNUP_PAGE_VIEWED | The user has viewed the signup page on the Volt Android app. | Signup | | **Signup** | When user lands on enter OTP page from signup page | SIGNUP_OTP_PAGE_VIEWED | The user has navigated to the OTP entry page from the signup page. | Signup | | **Signup** | When user clicks on T&C, Privacy Policy on signup screen | SIGNUP_T&C_BUTTON_CLICKED | The user has clicked on the Terms & Conditions or Privacy Policy buttons on the signup screen. | Signup | | **Signup** | When user clicks on edit button on enter OTP screen | EDIT_PHONE_BUTTON_CLICKED | The user has clicked the edit button on the OTP entry screen to modify their phone number. | Signup | | **Signup** | When user clicks on resend OTP button on OTP screen, capturing resend attempts | RESEND_OTP_BUTTON_CLICKED | The user has clicked the resend OTP button on the OTP entry screen. | Signup | | **Signup** | When user enters invalid OTP | INVALID_OTP_ENTERED | The user has entered an invalid OTP during signup. | Signup | | **Signup** | When new user is created | SIGNUP_COMPLETED | The user has successfully completed the signup process and a new user account has been created. | Signup | | **Signup** | When user lands on page to select email for signup

---

## #170 — Flow charts
**Status:** Unknown | **Last edited:** Unknown

# Flow charts Certainly! Below is the visualization of the user journey map provided, represented in PlantUML diagrams. Due to the complexity and length of the entire journey, I've divided the visualization into sections corresponding to each main phase of the user journey. Each section includes the PlantUML code for the activity diagram, which you can use to generate the diagrams. --- ## **1. User Acquisition and Onboarding** ### **1.1. Launching the App and User Signup** ``` @startuml start partition "User (FE)" { :Launch App; :View Signup Page; if (Click T&C or Privacy Policy?) then (Yes) :Click T&C or Privacy Policy; :View T&C or Privacy Policy; endif :Edit Phone Number; :Navigate to OTP Page; } partition "Backend (BE)" { :Trigger OTP; } partition "User (FE)" { repeat :Enter OTP; :Submit OTP; partition "Backend (BE)" { :Verify OTP; if (OTP Valid?) then (No) :OTP Invalid; endif } if (OTP Valid?) then (No) :Display Error Message; :Resend OTP?; if (Resend OTP?) then (Yes) partition "Backend (BE)" { :Trigger OTP; } endif endif repeat while (OTP Invalid) :Complete Signup; :View Verify Email Page; if (Verify Email with Google?) then (Yes) :Verify Email with Google; else :Verify Email with Other Method; :View Enter Email Page; :Enter Email Address; endif :Email Verification Result; } partition "Backend (BE)" { :Create User Context; :Update User Email; } stop @enduml ``` --- ## **2. Eligibility and Limit Check** ### **2.1. PAN Verification and Eligibility Check** ``` @startuml start partition "User (FE)" { :Enter PAN; :Verify PAN; :PAN Verification Result; if (PAN Verification Successful?) then (Yes) :Confirm PAN Details; else :Edit PAN Details; :Resubmit PAN; endif } partition "Backend (BE)" { :Initiate PAN Verification; :Complete PAN Verification; if (PAN Verification Failed?) then (Yes) :PAN Verification Failed; endif } partition "User (FE)" { :Trigger Eligibility Check; :Eligibility Check Result; if (Eligible?) then (Yes) :Proceed to Next Step; else :Application Under Review or Rejected; stop endif } partition "Backend (BE)" { :Create Credit Application; :Receive Credit Approval Request; :LAN Generation Successful?; if (LAN Generation Failed?) then (Yes) :LAN Generation Failed; stop endif } stop @enduml ``` --- ## **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** ``` @startuml start partition "User (FE)" { :View Check Limit Page; :Edit Details if Necessary; :Update Portfolio Source; :Request MF Portfolio Details; :Choose CAMS or KFIN?; } partition "User (FE)" #LightBlue { if (CAMS Selected?) then (Yes) :Request OTP for CAMS MF Fetch;

---

## #171 — Journey Table
**Status:** Unknown | **Last edited:** Unknown

# Journey Table 1. **Phase** 2. **Sub-Phase** 3. **Action ID** 4. **User Action** 5. **Description** 6. **Platform** --- ## **1. User Acquisition and Onboarding** | Phase | Sub-Phase | Action ID | User Action | Description | Platform | | --- | --- | --- | --- | --- | --- | | User Acquisition and Onboarding | Launching the App | 1.1.1 | Launch the App | Open the Volt platform by tapping the app icon from the splash screen. | Mobile App / Web | | User Acquisition and Onboarding | User Signup | 1.2.1 | View Signup Page | Access the signup interface to create a new account. | | | User Acquisition and Onboarding | User Signup | 1.2.2 | Click T&C or Privacy Policy | Review the Terms & Conditions or Privacy Policy documents. | | | User Acquisition and Onboarding | User Signup | 1.2.3 | Edit Phone Number | Modify the phone number entered during signup. | | | User Acquisition and Onboarding | User Signup | 1.2.4 | Navigate to OTP Page | Proceed to the OTP (One-Time Password) verification step. | | | User Acquisition and Onboarding | User Signup | 1.2.5 | Resend OTP | Request a new OTP if the initial one was not received or expired. | | | User Acquisition and Onboarding | User Signup | 1.2.6 | Enter Invalid OTP | Attempt to enter an incorrect OTP for testing purposes. | | | User Acquisition and Onboarding | User Signup | 1.2.7 | Complete Signup | Finalize the signup process after successful OTP verification. | | | User Acquisition and Onboarding | User Signup | 1.2.8 | View Verify Email Page | Access the email verification interface. | | | User Acquisition and Onboarding | User Signup | 1.2.9 | Verify Email with Google | Use Google authentication to verify the email address. | | | User Acquisition and Onboarding | User Signup | 1.2.10 | Verify Email with Other Method | Utilize alternative methods for email verification. | | | User Acquisition and Onboarding | User Signup | 1.2.11 | View Enter Email Page | Input the email address for account verification. | | | User Acquisition and Onboarding | User Signup | 1.2.12 | Email Verification Result | View the outcome of the email verification process. | | --- ## **2. Eligibility and Limit

---

## #172 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #173 — flow
**Status:** Unknown | **Last edited:** Unknown

# flow **User Journey Map for a Loan Against Mutual Funds Application** This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer). --- ### **1. User Acquisition and Onboarding** ### **1.1. Launching the App** - **FE Snippet:** - *Splash Screen > Launch App* ### **1.2. User Signup** - **FE Snippets:** - *Signup > View Signup Page* - *Signup > Click T&C or Privacy Policy* - *Signup > Edit Phone Number* - *Signup > Navigate to OTP Page* - *Signup > Resend OTP* - *Signup > Enter Invalid OTP* - *Signup > Complete Signup* - *Signup > View Verify Email Page* - *Signup > Verify Email with Google* - *Signup > Verify Email with Other Method* - *Signup > View Enter Email Page* - *Signup > Email Verification Result* - **BE Events:** - *Backend Events > OTP > Trigger OTP* - *Backend Events > OTP > Verify OTP* - *Backend Events > User Management > Create user context* - *Backend Events > User Management > Update user email* --- ### **2. Eligibility and Limit Check** ### **2.1. PAN Verification** - **FE Snippets:** - *Cash Limit > Enter PAN* - *Cash Limit > Verify PAN* - *Cash Limit > PAN Verification* - *Cash Limit > Edit PAN Details* - *Cash Limit > Confirm PAN Details* - **BE Events:** - *PAN Verification > Initiate PAN verification* - *PAN Verification > Complete PAN verification* - *PAN Verification > PAN verification failed* ### **2.2. Eligibility Check** - **FE Snippets:** - *Cash Limit > Trigger Eligibility Check* - *Cash Limit > Eligibility Check Result* - *Cash Limit > Application Under Review* - *Cash Limit > Application Rejected* - **BE Events:** - *Credit Application > Create credit application* - *Credit Approval Request > Receive credit approval request* - *Credit Approval Request > FAS creates the request* - *Credit Approval Request > LAN generation successful* - *Credit Approval Request > LAN generation failed* --- ### **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** - **FE Snippets:** - *Cash Limit > View Check Limit Page* - *Cash Limit > Edit Details on Check Limit Sheet* - *Cash Limit > Update Portfolio Source* - *Cash

---

## #174 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #175 — Handling Discrepancies Between Assumed and Actual
**Status:** Unknown | **Last edited:** Unknown

# Handling Discrepancies Between Assumed and Actual Limits In our **Loan Against Mutual Funds (MF)** process, we allow users to act based on certain limits displayed on their dashboard throughout the loan journey. These limits are meant to provide a smooth and consistent experience, ensuring users feel confident as they proceed with their loan requests. Two key terms we deal with are the **Drawing Power (DP)** and the **sanction limit**. • **Drawing Power (DP)** is the theoretical maximum amount a user can borrow, based on factors like the NAV, unit price, and LTV of their pledged mutual funds. • **Sanction Limit** is the actual borrowing limit we allow users to access through the platform. We calculate these limits based on the **assumed DP and sanction limit** derived from the formulas and approved lists shared with us by our lending partners. However, in the actual loan processing, the **lender retains the final rights** to determine both the **DP and sanction limit**, since they are the ones disbursing the loan amount. This means that the **assumed DP** and **sanction limit** we show to the user may differ from the **final limits** confirmed by the lender after their internal checks and approvals. In certain cases, there can be discrepancies. For example, the lender may adjust the list of approved mutual fund units or change the loan-to-value (LTV) ratio during the final review, leading to a lower **DP** or **sanction limit** than what was originally calculated. As a result, a user may initiate a withdrawal request based on the higher, **assumed limit**, but it can get **rejected** once the lender processes the loan and confirms the lower final limits. To handle these situations, we notify the user if their **withdrawal request exceeds the final approved limits**. The system will automatically **error handle the request** and inform the user of the discrepancy. We will also guide the user to **submit a new withdrawal request** that falls within the actual, lender-approved DP or sanction limit, ensuring that they can successfully access their funds without further delays or confusion. While these discrepancies can happen due to changes in the lender’s processing, our goal is to keep users informed and ensure that they can quickly adjust their requests to align with the actual limits approved by the lender. This approach minimizes user frustration and maintains transparency throughout the loan process.

---

## #176 — LSQ Leedsquared
**Status:** Unknown | **Last edited:** Unknown

# LSQ: Leedsquared @Naman Agarwal ### **Overview** LeadSquared (LSQ) is a comprehensive Customer Relationship Management (CRM) tool primarily used by Volt Money to manage lead generation, customer interactions, and the loan application process. LSQ enables sales teams and Relationship Managers (RMs) to track customer journeys, from lead acquisition to loan approval, providing a centralized view of lead data, customer details, and application stages. --- ### **Framework: Business Impact of LSQ** ### 1. **Purpose/Objective** LSQ’s core objective is to **streamline lead management** and **enhance customer support** by providing sales teams with real-time access to lead information and loan application statuses. By organizing customer interactions and loan data in one place, LSQ improves the efficiency and transparency of the sales process, enabling better decision-making and quicker responses to customer needs. ### 2. **Key Features & Functions** | **Feature** | **Description** | | --- | --- | | **Lead Management** | LSQ tracks customer leads from acquisition to conversion, providing visibility into lead status, ownership, and data. | | **Loan Application Tracking** | Displays the current stage of loan applications (e.g., CIBIL check, KYC, approval), helping RMs manage their pipeline. | | **Customer Data Storage** | Stores critical customer details such as name, email, phone number, and loan amounts, enabling personalized outreach. | | **Sales Performance Insights** | Generates reports on lead outreach, conversion, and sales performance, helping teams optimize their strategies. | ### 3. **Business Benefits** - **Improved Lead Conversion**: LSQ helps RMs track the progress of leads efficiently, ensuring no customer falls through the cracks and allowing for timely follow-ups. - **Increased Transparency**: By providing a clear view of each lead’s stage in the loan application process, LSQ reduces ambiguity and improves decision-making. - **Enhanced Customer Support**: Real-time access to customer details and loan data allows RMs to provide more informed and tailored support during customer interactions. ### 4. **Challenges/Current Gaps** - **Lead Stage Sync Issues**: Discrepancies between the stages in LSQ and Volt Money's backend systems can lead to confusion and mismanagement of leads. - **Missing Loan Details**: Critical loan information like Processing Fees (PF), Rate of Interest (ROI), and Sanction Limits are not always available in LSQ, affecting RMs' ability to assist customers. - **Manual Data Updates**: Admin actions (e.g., changes to customer data) are not automatically reflected in LSQ, which can lead to outdated records and inefficiencies. ### 5. **Opportunities for Improvement** - Lead prioritisation - **Automating Data

---

## #177 — Missed calls from customers aren't being called ba
**Status:** Unknown | **Last edited:** Unknown

# Missed calls from customers aren't being called back or addressed # Missed Calls and Customer Support Optimization Missed calls from customers are a significant issue, as many are not being addressed. Customers reach out to us for help during various stages, such as onboarding, opening credit lines, post-account opening support, or product inquiries. To effectively manage these requests and reduce missed calls, we need a strategy that not only addresses customer needs but also balances the cost of support channels. ## Understanding the Support Categories: We can categorize customer interactions into three key areas: 1. **Awareness**: Customers seek to understand the product better. 2. **Sales**: Customers eligible for the service but who have not yet opened an account. 3. **Support**: Customers who already have accounts and need assistance with specific issues. ## Support Channel Options: There are several ways we can provide support, each with its own cost and effectiveness: - **Online Documentation**: Free but less accessible for most users. - **Product Journey (In-App Help)**: Accessible but costly in terms of development time. - **Chat Support**: Affordable and accessible for general queries. - **Call Support**: Highly impactful but also the most expensive to maintain. ### Optimizing Customer Support: Our goal is to provide the right support channel for each category of customer, depending on their needs, to maximize effectiveness while minimizing costs. This means segmenting customers into "buckets" based on their status and needs and directing them to the appropriate support channel: | **Bucket** | **Identifier** | **Channel to Retarget** | | --- | --- | --- | | **Awareness** | No record of the number in the system, ineligible | Chat or WhatsApp | | **Sales** | Eligible number, account not yet opened | Call Support | | **Support** | Customer with an open account | Chatbot with common services | ### Proposed Changes: To reduce call support costs, we should remove the call option for ineligible customers and instead provide them with WhatsApp support. This will help to ensure that calls are only directed to customers who are further along the funnel, and likely to require higher-touch support. ### Key Objectives: - **Address customer needs** through the appropriate support channels. - **Reduce support costs** by minimizing unnecessary call support. - **Reduce missed calls and errors** by routing customers more effectively. ### Data Requirements: To implement this strategy, we need to collect and analyze the following data: -

---

## #178 — Sales team is calling customers who complete the j
**Status:** Unknown | **Last edited:** Unknown

# Sales team is calling customers who complete the journey on their own To maximize the efficiency of our sales team and ensure that our limited resources are used effectively, we aim to distinguish between customers who genuinely need assistance and those who can self-serve. By enabling our sales team to focus on "struck" customers—those facing difficulties in the application or onboarding process—we can optimize our support efforts, increase customer satisfaction, and drive higher conversion rates. ## Strategy: We are building a **customer classifier** that will automatically detect whether a customer is "stuck" in the journey or can self-serve. This will allow our CRM to prioritize customers based on their likelihood to convert or their need for human assistance. By focusing on high-priority leads, we can drive better performance with the same resources. ### Key Steps: 1. **Develop a Classifier**: - Build a mechanism that identifies "struck" customers based on their interaction with the platform. This classifier will be able to distinguish between users who are struggling and those who can proceed independently. 2. **Highlight in CRM**: - Integrate the classifier with our CRM system to ensure that sales representatives are notified in real-time when a customer is identified as "stuck." The CRM should highlight these customers, offering the sales team clear, actionable insights. 3. **Update Sales Incentives**: - Modify the incentive structure for sales executives to align with the new system, rewarding them for focusing on and resolving cases where their intervention is truly needed. ## Identifying "Struck" Applicants: To accurately identify struck customers, we will deploy the following tactics: - **Telemetry on Errors**: - Implement error tracking throughout the customer journey. If a customer encounters a technical problem (e.g., form submission fails, API error), they will be flagged as "struck." - **Abandoned Journey**: - Monitor customer activity in real-time. If a user abandons a critical stage of the application process (e.g., KYC, loan application) for more than 30 minutes, they will be marked as "stuck." - **Custom Rules**: - We will determine additional logic based on further data analysis and customer feedback to enhance the classifier. ### Classifier Logic: The classifier's logic will be based on a combination of: - **User behavior telemetry** (e.g., error reports, time spent on a task). - **Abandonment tracking** (e.g., inactivity beyond a defined threshold). - **Data-driven insights** (e.g., patterns in customers’ prior journeys that lead to successful or failed conversions). ### CRM

---

## #179 — API flow for KFS and Agreement
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

## #180 — Analytics requirement for amortisation of PF
**Status:** Pending review | **Last edited:** Unknown

# Analytics requirement for amortisation of PF Last Edited: April 24, 2026 8:59 AM PRD ETA: April 24, 2026 PRD Owner: Vaibhav Arora # **1. Objective** Generate month-level amortised accounting entries for Processing Fee (PF) income against loan accounts across LAMF, LAS, and Term Loan product lines. The report will be consumed by the Finance team and downloaded on-demand from the Finflux analytics module. The design must be extensible to accommodate other fee/cost types in future iterations without structural rework. # **2. Scope & Exclusions** ## **2.1 In Scope** - Product lines: LAMF, LAS, Term Loan (TL) - Charge type: Processing Fee (PF) - Accounting entries: Income recognition at monthly amortisation level - Amortisation method: Straight Line Method (SLM) - Report period: M-N (N>0) (previous calendar months only) - Waiver handling: Partial and complete waivers with corresponding reverse entries - Loan closure handling: Remaining balance acceleration on closure date ## **2.2 Explicitly Out of Scope** - GST component of processing fee excluded from amortisation entries - Current month entries - report is strictly retrospective - Real-time or intra-month amortisation schedules # **3. Source Data & Key Fields** All data will be sourced from the accounting report. The following fields are required at a schedule/charge level: | **Field** | **Source / Table** | **Notes** | | --- | --- | --- | | FXLAN / Term Loan Account No. | LMS – Loan Master | External loan identifier | | Client External ID | LMS – Loan Master | FXCID reference | | Product Type | LMS – Loan Master | LAMF / LAS / TL | | Charge Application Date | LMS – Fee Schedule | Date PF was applied | | PF Income Amount | LMS – Fee Schedule | Excludes GST; 'Income from Fees' leg only | | Transaction ID (Fees) | LMS – Transaction Log | Original fee transaction reference | | Loan Status | LMS – Loan Master | Active / Closed | | Closure Date | LMS – Loan Master | Populated only if loan is closed | | Loan Tenure (Original) | LMS – Loan Master | In days, for SLM denominator | | Waiver Amount | LMS – Waiver Log | Partial or full waiver on fee | | Waiver Date | LMS – Waiver Log | Date waiver was applied | | Waiver Type | LMS – Waiver Log | Partial /

---

## #181 — BRD Enhancements to Schedule & Derived Details Pro
**Status:** Completed | **Last edited:** Unknown

# BRD: Enhancements to Schedule & Derived Details Processing for OD (Loan Against Mutual Funds) Last Edited: December 11, 2025 2:41 PM PRD Owner: Vaibhav Arora ## **1. Problem Statement** Our OD product relies heavily on Finflux’s **schedule** and **schedule-derived details** for: - Accurate repayment allocation - DPD computation - Interest/charge tracking - Reconciliation, reporting (internal and external) Currently, certain system behaviours in the LMS lead to **incomplete or incorrect schedule updates**, which introduces reconciliation gaps and incorrect ageing/DPD calculations. We need Finflux to enhance how the LMS **creates, updates, and settles obligations** and **populates derived details** whenever specific transactions occur. --- ## **2. Context: How It Should Work (High Level)** - Any due created on a line (interest, charge, fee, penalty) should create an **obligation** in the schedule. - Currently we do not get the source transaction that created that obligation, we require source transaction to be mapped with the schedule ID so that we can directly map the transactions that created the corresponding schedule - When a transaction settles that obligation, the schedule and derived details should reflect: - obligation met - amount accounted - linkage to the transaction identifier - timestamps for audit - For OD products, interest accrues daily and becomes due only under certain events (billing, foreclosure (clear dues) etc.). Finflux already follows this pattern for regular repayments. The gaps occur only for specific transaction types listed below. --- ## **3. Issues & Required Enhancements** --- ## **3.1 Issue 1: *Clear Dues (used for Foreclosure) does not update schedule or derived details*** ### **Current Behaviour** - During foreclosure, Fenix performs a **“clear dues”** transaction to make the accrued interest due for the line: - Accrued-but-not-yet-due interest is first made due. - Finflux then settles this newly created due using excess funds when the clear dues API is hit - However: - The **schedule table is not updated** to reflect the new temporary obligation. - The **obligation is not marked as met**. - **Derived details** are not populated with the settlement transaction. ### **Impact** - Reporting discrepancies (interest recognised vs. interest settled). - Incorrect DPD because obligations appear “unmet”. ### **Required Behaviour** Finflux should: 1. **Create an obligation** in the schedule whenever clear-dues makes an amount due (accrued interest or any charge). 2. **Immediately settle the obligation** and mark: - obligation_met = true - obligation_met_on = timestamp 3. **Populate derived details** with: - linkage to the

---

## #182 — Charge reversal enhancement
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

## #183 — Colending Disbursement and Charge knock off
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

## #184 — Corporate action - Data feed
**Status:** Completed | **Last edited:** Unknown

# Corporate action - Data feed Last Edited: March 19, 2026 9:44 PM PRD Owner: Vaibhav Arora # Corporate Actions Data Feed ## Overview To support monitoring of securities pledged as collateral, we have reviewed a **Corporate Actions data feed sourced from BSE end-of-day bulletins**. This feed provides information on **events and disclosures that may impact the value, structure, or tradability of securities**. The data is consumed daily and can be used by the Risk team to monitor portfolio changes and identify events that may require action. The data covers the following broad categories: - Corporate action events - Company structural changes - Market disclosures - Large market transactions - Insider activity - Liquidity indicators --- # 1. Corporate Action Events This dataset contains information about **corporate actions declared by listed companies** that may affect the number of shares, price, or entitlement of shareholders. Typical corporate actions include: - Dividends - Stock splits - Bonus issues - Rights issues - Buybacks - Capital restructuring events For each event, the feed provides key reference dates such as: - **Record Date** – Date used to determine shareholder eligibility - **Ex-Date** – Date after which the security trades without the entitlement - **Cum Date** – Date before which investors must hold shares to be eligible - **Effective Dates** – Time period during which the action is applicable In addition, where applicable, the feed also provides: - Dividend amount or payout value - Share conversion ratios (e.g., split or bonus ratios) - Share quantity adjustments - Offer price or premium for rights issues These events are critical for adjusting **collateral valuation and share quantities** in pledged portfolios. --- # 2. Corporate Action Classification A separate master dataset provides the **mapping of corporate action identifiers to the specific event type** (e.g., dividend, split, bonus). This allows systems to interpret the corporate action feed and determine the **nature of the event impacting a security.** ---

---

## #185 — Credit note PRD
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

## #186 — IFSC addition Account opening enhancement
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

## #187 — LAS CMS Unlodgement
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

## #188 — External integrations LOS and LMS
**Status:** Done | **Last edited:** Unknown

**Problem:**
are we solving?**

There is no dedicated system to centrally manage the lifecycle of collateral for Loan Against Securities (LAS). Currently, lien requests, revocations, and monitoring are either partially tracked in LMS or manually handled by operations. This leads to operational risk, poor scalability, and delayed exception handling.

---

**Solution:**
?**

Build a standalone CMS with tight integrations to both LOS and LMS. CMS will be the source of truth for lien status and collateral health, while LOS and LMS remain the system of record for application and loan lifecycle.

---

## #189 — Sample PMR transactions
**Status:** Done | **Last edited:** Unknown

# Sample PMR transactions ## CDSL (Lien marking): Pledge marking | Date | BO ID | ISIN | ISIN Description | Pledged Quantity | Pledgee Name | Status | Pledge Type | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Confirmed | Margin | Pledge created successfully | ## CDSL (Lien revocation): Pledge closure | Date | BO ID | ISIN | ISIN Description | Closed Quantity | Pledgee Name | Status | Closure Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 100 | DSP Finance Pvt Ltd | Released | 05-Jul-2025 | Pledge closed successfully | ### CDSL: (Lien invocation) | Date | BO ID | ISIN | ISIN Description | Invoked Quantity | Pledgee Name | Status | Invocation Date | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 07-Jul-2025 | 1201916305123456 | INE018A01030 | RELIANCE EQ | 50 | DSP Finance Pvt Ltd | Invoked | 07-Jul-2025 | Partial invocation triggered | ### NSDL (Lien marking): Pledge marking | Execution Date | Client ID | ISIN | ISIN Description | Pledged Quantity | Pledgee | Pledge Type | Margin Pledge | Status | Agreement No. | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 01-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Margin | Yes | Confirmed | AGMT-56789 | ### NSDL (Lien revocation) Pledge closure | Closure Date | Client ID | ISIN | ISIN Description | Closed Quantity | Pledgee | Status | Lock-In Reason | Remarks | | --- | --- | --- | --- | --- | --- | --- | --- | --- | | 05-Jul-2025 | 41111111 | INE018A01030 | RELIANCE EQ | 100 | DSP1234 | Released | NA | Closure on user request | ### NSDL (Lien invocation) | Execution Date | Client ID | ISIN | ISIN Description | Invoked Quantity | Pledgee | Status | Remarks | | ---

---

## #190 — LAS Collateral management system
**Status:** Completed | **Last edited:** Unknown

# LAS: Collateral management system Last Edited: July 28, 2025 8:43 PM PRD ETA: June 27, 2025 PRD Owner: Vaibhav Arora # **What is CMS?** The Collateral Management System (CMS) will act as the central infrastructure for managing pledged shares for a Loan Against Shares (LAS) product. It will interface with the Loan Origination System (LOS), Loan Management System (LMS), and Depository Participant (DP) — SHCIL — to manage the full lifecycle of collateral from validation to lien marking, valuation, revocation, and reconciliation. It will also include risk management via real-time LTV monitoring, handling of corporate actions, and tools for operations teams. [CMS system architecture](https://claude.ai/public/artifacts/b5a68c3c-4705-4c9d-b34b-52a1d6bb8ec4) --- # Why do we need a CMS? A **Collateral Management System (CMS)** is essential for a **Loan Against Shares (LAS)** product because collateral (in the form of pledged shares) is **the core security** backing the loan. Without an automated, secure, and integrated system to manage this collateral, the business is exposed to **operational risk, financial risk, and regulatory gaps**. 1. Centralised tracking and management of collaterals: Currently all collaterals are managed by the LMS which makes it very risk prone: A CMS ensures each step is trackable, audit-logged, and consistent with external systems (DP/SHCIL) and internal ones (LMS/LOS). 2. CMS constantly monitors Loan-to-Value (LTV) ratios. If share prices fall, LTV breaches can be automatically flagged (exposure tracking), triggering margin calls or partial lien revocation. 3. Logic separation from LMS: CMS has a lot of collateral management intelligence which should be LMS agnostic, this will make our LMS very modular and easily replaceable since majority of the complexity of collateral management will be handled via CMS. --- # **How are others solving this problem?** The approach to collateral management for Loan Against Shares (LAS) varies widely across the lending ecosystem, largely depending on a company’s scale, tech maturity, and risk appetite. Broadly, solutions fall into two categories: ### 1. **Tightly Coupled CMS-LMS Systems (Usually Vendor-Provided)** Some lenders use **end-to-end lending platforms** where the CMS is embedded within the LMS — often provided by a third-party vendor. These platforms offer: - Pre-integrated lien workflows - Basic LTV tracking - Unified borrower and collateral view ### 2. **No CMS — Operations-Led Collateral Tracking** Most early-stage or mid-sized lenders operate without a dedicated CMS. Instead, they rely on: - Manual **ops processes** to initiate and track lien/revocation files - **Excel sheets or shared dashboards** to monitor pledged ISINs

---

## #191 — LAS LMS Product Note
**Status:** Completed | **Last edited:** Unknown

# LAS LMS Product Note Last Edited: March 16, 2026 4:03 PM PRD Owner: Vaibhav Arora ## **Concept Journey Note: Blended Loan Against Shares & Mutual Funds** --- ### **Overview** This document outlines the transaction and servicing lifecycle for the **blended LAS-LAMF product**. While loan origination and management remain unified, **collateral management bifurcates at the asset level** (Shares vs Mutual Funds). Key principles: - A **combined DP account** is maintained per customer, but **collateral operations are asset-specific**. - **RMS (Risk Management System)** provides real-time valuation (15-min intervals), while **LMS (Loan Management System)** runs off daily NAVs or EOD market prices. - All DP negative impact money and collateral transactions are **double-validated by LMS + RMS** to ensure real-time coverage, DP sufficiency. --- ## **1. MONEY TRANSACTIONS** --- ### **1.1 Disbursement (Forward + Reverse)** - **Forward Disbursement:** - Triggered post approval and sufficient DP validation (LMS) - RMS validates real-time prices (every 15 minutes). - LMS validates EOD price consistency - Both systems must independently confirm DP sufficiency. - On success: disbursement request is sent to TSP; loan status updated. (Cashfree) - **Reverse Disbursement:** - Used in cases of failed payout - Transaction reversed, collateral DP recalculated. --- ### **1.2 Repayment (Forward + Reverse)** - **Forward Repayment:** - Triggered via user mandate or manual repayment (UPI/netbanking/DC/VA) - LMS receives repayment; validates against due and excess amounts. - **Reverse Repayment:** - Applicable when repayment fails due to banking errors or incorrect credit. - LMS adjusts ledger and reverses credit. --- ### **1.3 Excess Refund** - LMS calculates overpayment (e.g., duplicate repayment, excess interest). - Refund is initiated after checking **updated DP position** via (RMS + LMS) - Final payout initiated via TSP only when RMS confirms buffer post-refund. --- ### **1.4 Charge Application (Forward + Waiver + Refund)** - **Forward:** - Charges (processing, penal charge, Dishonour fees) posted via LMS on configured triggers. - **Waiver:** - Ops-triggered waiver requests. - **Refund:** - Charge reversed, and refund processed. (Credit note) --- ## **2. SERVICING** --- ### **2.1 Closure** - Triggered after full repayment and complete collateral release. - LMS validates: - Zero principal (LMS) - No pending charges (LMS) - No open collateral pledges (CMS) - Closure confirmation sent to DP, TSP, and customer. --- ### **2.2 Renewal** - Applicable for LAMF/LAS products with fixed-term limits. - At maturity, a renewal window opens. --- ### **2.3 Mobile / Email / Bank Account Update

---

## #192 — Loan cancellation - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Loan cancellation - No cost EMI / TL (Cred) Last Edited: May 26, 2026 9:08 PM PRD ETA: May 26, 2026 PRD Owner: Vaibhav Arora --- ## Background and context ### Who is facing the problem - Borrowers who have taken a No Cost EMI loan against a merchant purchase and subsequently return the product or drop off mid-journey. - Borrowers who have an Insurance Premium Financing (IPF) loan where the insurance policy is cancelled either by the insurer or by the borrower. - CRED TL customers who have taken a loan and want to cancel within the loan cancellation period. - Ops and collections teams who currently have no automated lifecycle event for cancellation, distinct from foreclosure. - Risk teams who need cancelled loans excluded from bureau reporting which requires a distinct CANCELLED status, not CLOSED. ### What is broken today - There is no cancellation event in the current loan lifecycle. Cancellation and foreclosure are conflated, which creates incorrect P&L treatment, incorrect bureau reporting, and incorrect charge recovery. - When a merchant initiates a product return, there is no clean mechanism to unwind the loan, waive obligations, and return collected funds to the borrower. - Excess parking at line level does not work for cancelled tranches because excess needs to be tagged to the specific cancelled tranche for the refund to be correctly attributed. ### Why it matters - **Bureau reporting:** loans cancelled due to product return or policy cancellation must not be reported to credit bureaus. This requires a distinct CANCELLED status that bureau reporting logic can filter on. - **P&L accuracy:** interest waiver on cancellation must be treated as an income reversal, not a write-off. Without a proper cancellation flow, P&L entries are incorrect. - **Customer experience:** borrowers who return products or cancel policies are entitled to a refund of collected amounts. Without this flow, refunds are manual and error-prone. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | No Cost EMI (NCEMI) term loan tranche cancellation | Foreclosure (separate flow — live) | | Insurance Premium Financing (IPF) loan cancellation | Partial cancellation | | All four obligation state scenarios (see Section 3) | Borrower-unilateral cancellation (enforced at Fenix layer) | | Configurable cancellation window (beyond 14 days) | Merchant settlement and MMS integration (Fenix layer) | | Obligation-level configurability for waiver and refund

---

## #193 — PPSL UPI mandate presentation
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

## #194 — Part payments - No cost EMI TL (Cred)
**Status:** Pending review | **Last edited:** Unknown

# Part payments - No cost EMI / TL (Cred) Last Edited: May 22, 2026 11:34 AM PRD ETA: May 22, 2026 PRD Owner: Vaibhav Arora ## Background and context ### Who is facing the problem - Borrowers with active TL tranches under a credit line who wish to reduce their repayment burden, improve collateral coverage, or avoid forced liquidation of pledged securities. - Collections teams who need a structured tool to help distressed borrowers reduce delinquency probability without full foreclosure. - Risk and ops teams who currently have no automated principal-reduction pathway and handle these requests manually. ### What is broken today - Borrowers have no self-serve mechanism to make a partial principal repayment against a tranche. - The only options available are full EMI payment, excess parking at line level, or full foreclosure — none of which address the mid-path use case of reducing outstanding principal while keeping the tranche live. - Excess parking, while improving the shortfall formula on paper, does not reduce tranche-level obligations. Borrowers who park excess as a shortfall cure remain exposed to re-triggering if security values drop further. - Collections teams have no product-supported tool to recommend structured partial paydowns as part of a repayment sustainability plan. ### Why it matters - Forced liquidation of pledged securities is a high-friction, high-cost event for both borrower and lender. A structured part payment pathway can prevent this. - Borrowers with temporary liquidity (bonus, redemption, salary inflow) have no way to deploy it productively against their loan exposure. - Without this, borrowers approaching shortfall thresholds have only two outcomes: excess parking (fragile cure) or sell-off. Part payment creates a third, durable path. --- ## 1. Problem scope | In scope | Out of scope | | --- | --- | | Term loan (TL) tranches on active credit lines | Overdraft (OD) products | | Tranche-level principal reduction | Line-level part payments | | Payment-led part payment (with repayment order) | Accrued interest settlement | | Excess-led part payment (consuming existing excess) | Overdue / due settlement via part payment | | Reduce EMI amortisation mode | Generic repayment wallet behaviour | | Reduce tenure amortisation mode | Prepayment charges | | Shortfall reduction via principal paydown | Lender-triggered restructuring | | Tactical deleveraging | Foreclosure flows | | Collections-assisted restructuring | Unpledging workflows | | SOA remark on part payment receipt | Borrower communications (separate

---

## #195 — Pincode addition Account opening enhancement
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

## #196 — Product Note LAS Customer Consent Capture
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

## #197 — Product Note Penalty migration to Fenix (Colending
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

This enhancement addresses the following problems.

# Product Note: Penalty migration to Fenix (Colending) Last Edited: April 14, 2026 4:02 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Currently, penal charges for overdue loan accounts are computed by an **automated job in Finflux**. This job runs daily at 4 AM and applies penalties when interest becomes overdue. These charges are stored as **applicable charges in Finflux** and surfaced to downstream systems primarily through foreclosure simulations. This architecture introduces several operational and product limitations. **Who is impacted** - Operations teams - Product and engineering teams - Finance and customer support teams - Borrowers indirectly (through slower issue resolution) **Challenges in the current setup** 1. **Limited product control** Penal charge computation logic currently resides inside Finflux jobs. Any change to the logic requires dependency on Finflux configuration and third party coordination. 2. **Limited configurability** The current implementation applies a **flat penalty of ₹10 per day**, whereas the Key Fact Statement (KFS) requires **slab-based penalty computation based on overdue amount**. (This is a compliance observation) 3. **No operational control** Since penalties are not created as **transactions inside Fenix (internal LMS)**: - Operations cannot **waive or refund penalties directly** - Charge-level audit and tracking are difficult 4. **Colending complexity** In Loan-90 / Loan-10 structures, penalties must be **orchestrated across loan legs**. The Finflux-driven penalty logic does not provide sufficient control to ensure accurate charge allocation across colending loans. 5. **Foreclosure simulation dependency** Foreclosure calculations rely on Finflux charge simulations. This makes enhancements difficult and increases dependency on an external system for a critical borrower-facing calculation (Finflux). Additionally, the current system lacks a **generalised framework for defining and applying loan charges**. Future charges such as **Annual Maintenance Charges (AMC)** or other contingent fees would require ad-hoc implementations. This enhancement addresses these limitations by: - Migrating **penal charge computation to Fenix** - Introducing a **generic Applicable Charges framework** - Enabling **charge-level operational controls** - Supporting **future charge types such as AMC** --- # **1. Problem Scope** ## **In Scope** This enhancement addresses the following problems. ### **Migration of penalty computation to Fenix** Daily penal charge computation will move from **Finflux jobs to Fenix**, eliminating system dependency and enabling full product control. ### **Penalty pricing enhancement** Penalty logic will be enhanced from **flat charges to slab-based pricing**, as defined in the KFS. ### **Minimum overdue threshold** Penalties will only be applied when: Overdue Amount ≥ ₹10 This

---

## #198 — Product note Credit note for TL
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

We are solving:

# Product note: Credit note for TL Last Edited: April 28, 2026 4:45 PM PRD ETA: April 17, 2026 PRD Owner: Vaibhav Arora # **PRD: Interest Refund via Credit Note – Term Loan (Tranche-Level)** --- ## **Background and Context** **Who is facing the problem:** - End customers awaiting resolution of incorrectly charged interest - Operations team handling refund/waiver requests - Finance team managing manual income reversals and reconciliation - Product/Tech teams currently intervening via backend/API --- **What is the challenge today?** - Interest refunds require **manual intervention via engineering or Finflux access** - No standardized **maker-checker workflow** - **Not supported for Term loans, currently productised and implemented only for OD** - Manual JV posting required for income reversal - No **system-driven dedupe or validation** - No **tranche-level visibility or audit tracking** - Turnaround time is **2–3 days**, impacting CX --- **Why is it important?** - Poor customer experience due to delays - High operational dependency and inefficiency - Risk of duplicate or incorrect refunds - Manual accounting overhead for finance - Lack of audit trail and reconciliation visibility --- ## **1. Problem Scope** ### **In Scope** We are solving: ### **1. Operational Independence** - Enable Ops to process **interest refunds without engineering dependency for Term loans** - Introduce **maker-checker workflow** --- ### **2. Standardized Accounting** - Eliminate manual JV posting - Introduce **credit note + automated income reversal** --- ### **3. Tranche-Level Refund Handling** - Refunds applied at **tranche level (not line level)** - Excess created is: - Initially **tranche-tagged** - **Not usable across tranches while tranche is active** - Becomes **line-level usable only after tranche closure** --- ### **4. Validation & Dedupe** - Prevent duplicate refunds via: - Schedule validation - Credit note existence checks --- ### **5. Audit & Traceability** - Full linkage: - Interest → Credit Note → JV - Tranche-level enrichment and reporting --- ### **Out of Scope** - Principal refunds - Bulk refund processing - Automated eligibility rules - Reversal of incorrect refunds (no reversal flow) --- ## **2. Success Criteria** ### **Outcomes** - Maker → Checker → Accounting completion within **1 hour** - **>90% reduction** in Jira dependency - Capability to refund interest for Term Loan - **Zero duplicate refunds** at tranche-month level --- ### **Post-launch Good State** - All refunds processed via maker-checker - Credit notes posted correctly at tranche level - Automated JV posted for income reversal - Finance can reconcile via

---

## #199 — Product note Excess refund Colending
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

## #200 — Product note Foreclosure (Colending)
**Status:** Completed | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure (Colending) Last Edited: May 19, 2026 2:47 PM PRD ETA: March 15, 2026 PRD Owner: Vaibhav Arora # **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across **Loan 90 and Loan 10 in the Colending Loan Management System (CLMS)**. ### Who is impacted - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting ### What is broken today Foreclosure today largely operates based on **Loan 100 balances**, while the actual liabilities exist across **Loan 90 and Loan 10**. This creates several limitations: 1. **Incorrect foreclosure simulation** Foreclosure amounts may be computed using only Loan 100 data without validating Loan 90 and Loan 10 balances. 2. **Pending transaction inconsistencies** Foreclosure may be initiated even when **pending transactions exist in CLMS**, leading to inaccurate payoff calculations. 3. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring that: - Loan 90 and Loan 10 are closed - All charges and interest are posted - Excess settlement is completed 4. **Penalty and applicable charge dependency** Applicable charges (such as penal charges) may be applied after repayment due to **daily charge jobs**, which may cause foreclosure attempts to fail if charges are posted after repayment. 5. **Incorrect collateral release timing** Securities may be released before confirming that **both loan legs are closed**, which introduces risk. ### Why this is important Foreclosure is a **regulatory and customer-sensitive workflow**. Incorrect sequencing may lead to: - Incorrect payoff amounts shared with borrowers - Operational rework due to partial closures - Accounting mismatches across loan legs - Risk of releasing collateral before loan closure creating financial exposure for the NBFC This PRD defines a **colending foreclosure workflow** that ensures: - Correct payoff simulation - Transaction sequencing across loan legs - Controlled collateral release - Accurate excess settlement. --- # **1. Problem Scope** ## **In Scope** ### **Colending foreclosure simulation** Foreclosure simulation will incorporate balances from: - Loan

---

## #201 — Product note Foreclosure V2 for Colending
**Status:** Pending review | **Last edited:** Unknown

**In scope:**
**

# Product note: Foreclosure V2 for Colending Last Edited: April 24, 2026 7:43 AM PRD ETA: April 7, 2026 PRD Owner: Vaibhav Arora ## **Background and Context** Foreclosure is the process by which a borrower closes the loan account by repaying all outstanding dues including principal, interest, and applicable charges. In the current system architecture, loans are represented internally as **Loan 100**, while in a **colending setup** the exposure is split across: - **Loan 90 (NBFC exposure)** - **Loan 10 (Partner/Lender exposure)** Although Loan 100 represents the borrower-facing account, the underlying accounting and settlement obligations exist across Loan 90 and Loan 10 in the Colending Loan Management System (CLMS). --- ### **Who is impacted** - Borrowers initiating foreclosure - Lending partners (colending participants) - Operations teams processing closures - Product and engineering teams responsible for transaction sequencing - Finance teams responsible for settlement and accounting --- ### **What is broken today** 1. **Incorrect foreclosure simulation** Foreclosure amounts are often computed using Loan 100 without fully reconciling Loan 90 and Loan 10 balances. 1. **Pending transaction inconsistencies** Foreclosure may be initiated even when pending transactions exist in CLMS, leading to incorrect payoff calculations. 1. **Transaction sequencing issues** Loan closure and collateral release may occur without ensuring: - Loan 10 and Loan 90 are closed - All dues and interest are settled - Excess is correctly handled 1. **Penalty and applicable charge dependency** Charges (such as penal charges) may be posted after repayment due to system jobs, leading to foreclosure failures. 1. **Incorrect collateral release timing** Collateral may be released before confirming closure of underlying loan legs. 1. **Excess handling gap in colending** - Excess is parked in Loan 100 - Excess does not auto-settle dues or accrued interest - There is no native way to use excess during foreclosure This leads to: - Incorrect net payable shown to users - Failed foreclosure despite sufficient excess - Manual intervention for settlement - Reconciliation gaps --- ### **Why this is important** Foreclosure is a **high-intent and customer-sensitive journey**. Incorrect handling leads to: - Poor customer experience - Increased operational workload - Financial and accounting mismatches - Risk of incorrect collateral release This PRD ensures: - Accurate payoff computation - Deterministic transaction sequencing - Proper utilization of excess - Correct closure and refund handling --- # **1. Problem Scope** ## **In Scope** ### **1. Colending foreclosure simulation** Foreclosure simulation will compute payoff using: -

---

## #202 — Razorpay SDK enhancement for Colending
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

## #203 — Term loan gaps
**Status:** Unknown | **Last edited:** Unknown

# Term loan gaps Last Edited: July 24, 2025 5:10 PM PRD Owner: Vaibhav Arora ### **Spend & Convert Enhancements** - Support for **flat PF (Processing Fee)** values in spend and convert requests. - Allow **knockoff remarks** to be passed in the spend and convert payload. - Support passing **different charge types** and **collecting multiple charges** in a single spend and convert request. --- ### 🧾 **Repayment Logic** - Enable both **loan-level and line-level repayments** to co-exist for term loans. - Mark **repayment at loan level** as a current **gap** in configuration. - Support **EMI-level repayments**. - Include **apportionment details** in the repayment response (internal checks needed). - Support **loan-level excess refunds**. - **Excess amounts**: - Should remain **parked** after due generation (do not auto-settle dues via FIFO). - At **line level**, should **increase available limit**. --- ### 🧮 **Due/Bill Generation** - Bills should be generated **independent of the due generation job**—on demand. --- ### 📆 **Schedule and Simulation** - Provide a **preview schedule API** without needing to create a line. - Enable **tranche-level simulation API** for a given date. - All **date fields** must be passed as **EPOCH timestamps**. --- ### 🧠 **Tagging & Status Configurations** - SMA tagging should be **configurable**. - **NPA to be tracked at client level**, while **SMA is tracked at loan level**. --- ### 📉 **Interest & Limit Management** - Support **interest rate updates** on loans. - **Limit replenishment** should only occur when the **underlying loan is fully closed**, whether via EMI or part-payment.

---

## #204 — Trackwizz continuos monitoring enhancement
**Status:** Unknown | **Last edited:** Unknown

# Trackwizz continuos monitoring enhancement Last Edited: November 13, 2025 12:39 PM PRD Owner: Vaibhav Arora # Contract Changes Required for Stopping Continuous Monitoring - AS504 API ## Executive Summary Based on the AS504 API documentation, the following contract modifications are necessary to effectively discontinue continuous monitoring (Purpose 04) for customers while managing ongoing screening operations. --- ## 1. API Purpose Codes & Termination Logic ### Current Purpose Definitions - **Purpose 01**: Initial Screening with API Response and No Storage - **Purpose 03**: Initial Screening with API Response and TW Workflow - **Purpose 04**: Continuous Screening with TW Workflow ### Key Finding To stop continuous monitoring, contracts must clarify the mechanisms for Purpose 04 discontinuation, as there is no explicit "Purpose 05" for stopping monitoring in the current API specification. --- ## 2. Required Contract Amendments ### 2.1 Data Retention & Deactivation Terms **Required Changes:** ### 2.1.1 Customer Status Field Modification - **Field**: `status` (Customer Status Enum) - **Current Values**: Active, Closed, Dormant, Inactive, Suspended - **Contract Change**: Add explicit condition: `When a customer record's purpose changes from "04" (Continuous Screening) to either "01" or "03" (Initial Screening only), the system must: 1. Cease real-time continuous screening operations 2. Maintain historical screening records for audit/compliance purposes 3. Update effectiveDate to reflect when continuous monitoring ended 4. Mark continuous monitoring as "Terminated" in internal tracking` **Effective Date Requirements:** - Must be provided in "DD-MMM-YYYY" format - Should reflect the exact date when continuous monitoring ceases - Cannot be a future date (must be current or past) --- ### 2.2 Purpose Code Combination Restrictions **Contract Required Clause:** The API currently allows: - Purpose 01 & Purpose 04 (combination allowed) - Purpose 03 & Purpose 04 (combination allowed) **To Stop Continuous Monitoring**, the contract must specify: `Transition Rules for Discontinuing Continuous Monitoring: 1. If Purpose 04 is removed from a request while Purpose 01 or 03 remains: - Continuous monitoring CEASES immediately - Initial screening continues as specified - Customer record remains in TrackWizz but without ongoing monitoring 2. If ONLY Purpose 04 is passed in a new request: - Continuous monitoring CONTINUES unchanged 3. If NEITHER Purpose 01, 03, nor 04 is passed: - Request is REJECTED per validation MRV12` --- ### 2.3 Mandatory Fields for Terminating Continuous Monitoring **Contract Clause - Purpose 04 Discontinuation:** When removing Purpose 04, the following fields become mandatory: ``` FieldRequirementFormatPurposesourceSystemCustomerCodeMandatoryString (Max 100)Identifies record to stop monitoringsourceSystemNameMandatoryEnum

---

## #205 — [Platform] Foreclosure handling to support Volt fo
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

## #206 — Takeaways from Call analysis
**Status:** Unknown | **Last edited:** Unknown

# Takeaways from Call analysis | Theme Name | Total Calls | % of Grand Total | | --- | --- | --- | | Partner & Rm Relations | 320 | 23.1% | | General Inquiries & Acct Mgmt | 180 | 13.0% | | Banking & Mandate Setup | 162 | 11.7% | | Application Eligibility & Onboarding | 159 | 11.5% | | Repayment & Charges | 135 | 9.7% | | Portfolio Management | 134 | 9.7% | | Identity & Verification | 121 | 8.7% | | Account Closure & Foreclosure | 98 | 7.1% | | Technical Platform Issues | 43 | 3.1% | | Shortfall Management | 30 | 2.2% | | Loan Documentation | 10 | 0.7% | | Inconclusive/Unclassified | 17 | 1.2% | | **Grand Total** | **1387** | **100.0%** | [](Takeaways%20from%20Call%20analysis/Untitled%201d6e8d3af13a808490ece2edfb53e225.md) # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - The portal freezing, crashing, or becoming unresponsive. - Specific components are

---

## #207 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled # **Partner & MFD Relations (320)** ## **Commission Issues** - Delays in commission payments are a major concern among MFDs. - Partners often don’t understand how commissions are calculated, especially with enhancement applications. - Many partners are unaware of the offer details and frequently call to check eligibility and get updates. - Payouts are blocked due to missing or incorrect bank details, and partners struggle to update their payout information. **Action step:** - Automate payouts and simplify bank detail updates to ensure timely payments. - Provide a commission calculator so MFDs can check and understand their earnings on their own. - Plan GTM strategy to effectively communicate offers and updates. - Redesign onboarding and sidebar to make it easier for MFDs to update payout details. ## **Partner Portal & Tools:** ### **Functional Issues:** - If a customer is already registered, MFDs must call the RM for resolution. - Difficulty finding specific clients or application details. - Data inaccuracies in the shortfall and interest due tables. - Login issues: forgetting login numbers, and challenges with sharing access with employees. - No option to request a bank account change through the UI. **Action step:** - Implement improved multistep deduplication logic to handle already registered customers. - Redesign the pending and completed application tabs to organize them by customer. - Enable data checks before uploads (in development). - Introduce a new login flow: user ID + password login, with pre-filled mobile number for returning users. --- ### **Technical Issues:** - Portal freezing, crashing, or becoming unresponsive. - Specific components not loading or working properly. - General slowness and lag, reducing productivity. - **UI/UX Issues:** Confusing navigation, inactive buttons without context, and poor mobile usability. **Action step:** - Refactor the Partner app to improve performance and fix freezing issues. - Add logging for slow UI and stuck screens for better debugging and monitoring. 1. **MFD Onboarding & Profile Management:** - MFD finds the dashboard hard to navigate. - Issues if the MFD is from Redvision or investwell - MFD is not clear on the application steps and documents required for LAMF - MFD can update there email , phone etc through UI. Action items - Resign of dashbaord - Alignment on how to handle rv and insvestwell mfds - add simple, easy to read learning material for the LAMF 2. **Relationship Management & Support:** - Assigned RMs being unresponsive or difficult to

---

## #208 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #209 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #210 — FAQs on CGS landing page
**Status:** Unknown | **Last edited:** Unknown

# FAQs on CGS landing page - What is capital gain statement? How is it generated? **Capital gain statement** is a document that summarizes your redemption activities and the resulting capital gains or losses on your mutual fund holdings. It provides crucial information for filing your income tax return accurately. Volt is partnering up with MFCentral to generate a detailed mutual fund capital gain statement for you. - What is MFCentral? MFCentral is a unified platform launched in September 2021 to simplify mutual fund investments for individuals in India. It is a collaborative effort between the two leading Transfer Agents (RTAs) in the Indian mutual fund industry, CAMS and KFintech. It is also a close partner of Volt Money in facilitating effortless LAMF eligibility check and capital gain report generation. - What are the different classes of Mutual Funds with respect to taxation? Currently there are mainly three types of mutual funds based on their equity or debt instrument allocation: Equity, Debt and Hybrid. Taxation of a mutual fund depends on their domestic equity allocation percentage. - What are Equity Mutual Funds? How are they taxed? Equity Mutual Funds allocate a minimum of 65% of their investable assets to Equity-oriented instruments like domestic Equity shares. From a tax perspective, Equity Mutual Funds are subject to the same treatment as domestic Equity shares. Short-term capital gains (STCG) at a rate of 15% are applicable to profits from Equity Mutual Fund units held for 12 months or less. If the holding period exceeds 12 months, capital gains from Equity Mutual Funds are considered Long-term Capital Gains (LTCG). In such cases, the LTCG rate is 10% on cumulative capital gains exceeding Rs. 1 lakh in a financial year. Popular equity mutual funds include: [] - What are Debt Mutual Funds? How are they taxed? Debt Mutual Funds must allocate a minimum of 65% of their assets to Debt instruments, including bonds, T-bills, Certificates of Deposits, and similar securities. The tax rates and holding periods applicable to Debt Funds differ significantly from those of Equity Mutual Funds. From a tax perspective, for investments made before April 1, 2023: STCG is taxed as per your applicable Income Tax slab rate. However, long-term capital gains are taxed at 20% with indexation benefits. For investments made after April 1, 2023: LTCG and STCG earned on the debt mutual funds are taxable as per your income tax slab.

---

## #211 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #212 — problems
**Status:** Unknown | **Last edited:** Unknown

# /problems To effectively document the problems you’re facing with **Wati**, **Exotel**, **Zendesk**, and **1. Wati (WhatsApp Integration)** **Problem**: Lack of visibility and tracking of WhatsApp communications • **Details**: Wati handles a high volume of inbound customer queries, but there is no systematic way to track query status (open, pending, resolved). This leads to issues where agents miss or forget to follow up on important customer queries. • **Impact**: Queries often go unresolved, causing delays in customer service and frustrating customers, particularly MFDs who rely on quick resolutions to onboard and serve their clients. • **User Story**: *As an agent, I am overwhelmed by the volume of WhatsApp messages coming in. There is no mechanism to mark whether I’ve responded to a message or if it’s still unresolved, which leads to missed follow-ups and unhappy customers.* **2. Exotel (Call Management)** **Problem**: Inefficient call tracking and follow-up system • **Details**: Exotel manages inbound calls, currently there is a manul batch process to send the list of the customer with missed calls to support team to reachout through Exotell portal. we need more real time way to track whether queries have been resolved after a missed calls. Agents cannot easily see if the customer issue requires follow-up or if it has been addressed fully during the initial call. • **Impact**: Critical customer issues often require additional attention but get lost after the first call, resulting in unresolved problems, repeat calls, and customer dissatisfaction. • **User Story**: *As an agent, I receive many customer calls, but there’s no system to track whether their issues were fully resolved. Without follow-up reminders or logs, important cases are forgotten, and customers have to call back multiple times.* **3. Zendesk (Ticketing System)** **Problem**: Fragmented ticketing and lack of SLA tracking • **Details**: While Zendesk manages tickets across multiple channels (email, chat, etc.), it does not integrate well with other tools like Wati or Exotel. This leads to fragmented reporting and ticketing, where some queries are logged in Zendesk but others (from WhatsApp or calls) are not. Additionally, there is no clear tracking of SLAs for different customer segments (e.g., MFDs vs. direct customers). • **Impact**: Incomplete visibility of customer queries and SLA breaches result in delays, lost tickets, and poor prioritization of high-value customers. • **User Story**: *As a service manager, I cannot track SLAs for different customer types, which leads to some high-priority issues being neglected.

---

## #213 — LSQ Swach
**Status:** Unknown | **Last edited:** Unknown

# LSQ Swach **Title:** LSQ Opportunity Management – Solution Document **Date:** 18/07/2025 **Version:** v1.0 --- ## 🔷 Section 1: Customer Journey Solutioning ### 🔹 Objective To transition from a lead-centric to an opportunity-centric model in LSQ, enabling granular tracking across different types of customer interactions and ensuring all workflows are governed through opportunity objects. --- ### ✅ Key Requirements ### 1. Opportunity Types Configuration for Customers Set up the following distinct opportunity types in LSQ: - **Main Application (LAMF)** - **Enhancement** - **Foreclosure** - **LAS** (To be configured at a later stage) - **Renewal** Each opportunity type must be independently configurable, with distinct stages, activities, and associated automations. --- ### 2. Opportunity Attribute Support - All relevant **lead fields** (except name, email, and phone) will be replicated in the opportunity object. - A one-time schema sync between the LSQ backend and opportunity fields will be done to maintain consistency. - The Opportunity object will act as the **source of truth** for all downstream processes and reporting. --- ### 3. Lead to Opportunity Migration - All existing leads (excluding core identifiers: name, email, phone) will be migrated into new opportunities. - Migration logic will ensure backwards compatibility and data integrity. - **The migration from lead to opportunity will be interdependent, as all current flows are tightly integrated. Changes must be deployed simultaneously—partial implementation without complete migration is not feasible.** --- ### 4. Activity Management - Activities will be recorded and managed at the opportunity level, based on opportunity type. - Post-activity workflows will be executed based on opportunity state transitions. --- ### 5. Field Directionality - **One-way sync** from Opportunity → Lead for core fields (name, email, phone). - No data will flow from Lead → Opportunity to avoid overwrites. --- ### 6. Lead Automation Deprecation - Legacy lead-level automations (routing, field updates) will be **disabled**. - All process automations will now be driven by opportunity logic and configuration. --- ## 🔷 Section 2: Partner Journey Solutioning ### 🔹 Objective To establish a dedicated flow for managing the lifecycle of Partner (MFD) leads and activities using a structured, opportunity-driven model. --- ### ✅ Key Requirements ### 1. New Partner Lead Table - Introduce a **dedicated database table** for Partner (MFD) leads. - This will sync with LSQ and create a new partner lead distinct from the customer lead table. --- ### 2. New Opportunity Type: **MFD Activation** - Dedicated opportunity type

---

## #214 — Elevate Cases in LSQ- LAMF
**Status:** Open | **Last edited:** Unknown

# Elevate Cases in LSQ- LAMF: ### 1. **Purpose** To define the business and system requirements for handling **Elevate Cases** in LeadSquared (LSQ). Elevate Cases allow creation of a **new LAMF opportunity** for a borrower even if they already have an won LAMF opportunity with a different lender, enabling **parallel opportunities** under the same borrower account while keeping the opportunity name consistent. ### 2. **Background** Currently, LSQ enforces a “one-active-opportunity-per-lender” rule for each customer, identified by phone number. In *Elevate* scenarios, a borrower who has availed or is availing a LAMF loan from **Tata** or **Bajaj** may now seek a **new LAMF loan from DSP**. The Elevate mechanism ensures: - The **existing opportunity remains untouched**, and - A **new parallel LAMF opportunity** is created for DSP, maintaining full visibility and independent tracking without renaming opportunities. ### 3. **Scope** **In Scope** - Creation of a **new LAMF opportunity** when an existing LAMF opportunity belongs to another lender. - Detection and handling of duplicate opportunities via lender-based exception logic. - Full journey and disposition tracking for both opportunities. - Tagging and reporting visibility for all opportunities per borrower. **Out of Scope** - Changes to standard LAMF journey flow for non-elevate cases. - Changes to lender onboarding or scoring logic. - Non-LAMF product types. ### 4. **Trigger Condition for Elevate Case Creation** An **Elevate Case** is triggered when **all** of the following are true: 1. **Existing Opportunity Check** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = TATA or BAJAJ - Phone Number matches existing record (primary identifier) - Status = WON 2. **New Opportunity Request** - Opportunity Type = Loan Against Mutual Fund - Opportunity Name = CREDIT AGAINST SECURITIES BORROWER - Lender = DSP - Phone Number matches existing opportunity’s phone number 3. **Borrower Account ID Check** - Borrower Account ID ≠ Existing opportunity’s Borrower Account ID If all conditions above are true → **flag as Elevate case** and create a new opportunity with the same name. ### 5. **Functional Requirements** | **#** | **Requirement** | **Description** | | | --- | --- | --- | --- | | 1 | Elevate Case Detection | System should detect when a new opportunity matches Elevate trigger conditions. | | | 2 | Parallel Opportunity Creation | Allow creation of a new LAMF opportunity for a different lender without overwriting existing opportunities. |

---

## #215 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #216 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #217 — MFD Activation Journey
**Status:** Unknown | **Last edited:** Unknown

# MFD Activation Journey ### Objective To define the complete **MFD (Mutual Fund Distributor) Activation Journey** in CRM (LSQ), covering lead onboarding, empanelment, customer referral tracking, and loan activation. The journey ensures consistent activity logging, lead stage progression, and daily data refresh for partner details. ## Lead Creation Use Cases The MFD activation journey must accommodate **multiple lead creation sources**, including: 1. **Bulk Uploads** – Admin-led upload of MFD leads in CRM. 2. **Partner Portal Submissions** – MFDs registering directly via the self-service partner dashboard. 3. **Third-Party Integrations** – Leads ingested via B2B partners and platforms such as **Redvision, Investwell, and other aggregator systems**. 4. **Webinars** – Leads generated through online events and webinars. 5. **In-Person Meetups** – Leads generated via offline events, roadshows, or branch interactions. 6. **Referral Programs** – Leads created through referral schemes from existing MFDs or partners. The mfd activation journey opportunity schema: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | MFD Activation Journey | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: MFD Activation Journey | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:MFD is Activated-> Won, then the actual closure date is updated | | Partner ID | MX_CUSTOM_94 | strind | Volt backend | Add the partner id | | Status -> Status Stage | Status | Statusstring | Volt backend | Status = OPEN -> Unregistered/Registered/Empanelled/Partially Activated WON -> ActivatedLOST -> Not a MFD/Closed - Lost / Close Deferred / Invalid / Not Interested | | Origin | mx_Custom_11 | String | Volt backend | It will be applicable for bulk upload | | Source | Mx_Custom_3 | Source | Volt backend | Event/ Webinar | | Name | mx_Custom_3 | String | Volt backend | Event name | | Campaign | mx_Custom_20 | String | Volt backend | Marketting / WA | | Medium | mx_Custom_21 | String | Volt backend | WA/ Email | | Content | mx_Custom_23 | String | Volt backend | Marketing Content | | First Name | mx_Custom_4 |

---

## #218 — Repeat B2B2C
**Status:** Unknown | **Last edited:** Unknown

# Repeat B2B2C MFD Activation Journey Field Update & Lead Schema Integration ### **Purpose:** To define and manage the set of fields that must be updated post-MFD activation journey completion and ensure these updates are shared with the lead schema for downstream processing by the Repeat team. ### **Scope:** - Capturing required data fields. - Defining when and how these fields are updated. - Updating the lead schema with the captured data. - Triggering opportunity closure upon journey completion. **The following fields need to be replicated in the lead schema:"** 1. MFD Name 2. MFD Phone Number 3. MFD Employee Name 4. MFD AUM 5. MFD ARN 6. MFD Email 7. MFD Activation Date 8. MFD Origin 9. MFD Partner Referral Link 10. MFD Customer Referral Link 11. Referred By 12. Referrer Name 13. Referrer Phone 14. Partner Account ID Additionally, include the list of customers referred so far. 1. All the customer-referred activity must be populated in the lead once activated. **In conclusion, the repeat team can work completely on the lead level, and the MFD activation team can work on the opportunity level** The activities that must be polluted in the lead fields are as follows: 1. Daily partner details update 2. Customer referred 3. Customer loan created

---

## #219 — Support Requirement
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

## #220 — Volt Ops Requirements The child ticket will be cre
**Status:** Unknown | **Last edited:** Unknown

# Volt Ops Requirements The child ticket will be created and assigned to Volt Ops. Ticket Schema: The ticket can be replicated with a click using the option of Capture properties from parent ticket. Additional Tags required are as follows, and the mapping against the parent tags: | **Parent Tag** | **Child Tag** | | --- | --- | | account_opening | 1. pending_account_opening2. account_opening_/_lodgement_delayed | | lodgement | 1. pending_lodgement2. lodgement3. lodgement_issue4. account_opening_/_lodgement_delayed | | enhancement | 1. pending_account_enhancement 2. pending_enhancement | | disbursal | 1. pending_disbursal2. withdrawal_issue3. withdrawal_rejected4. unable_to_place_withdrawal5. manual_manual_disbursement | | foreclosure | 1. unable_to_submit_foreclosure2. foreclosure3. foreclosure_pending4. foreclosure_success_but_account_not_closed5. expired_loan | | lien_removal | 1. foreclosure_success_but_lien_not_removed2. lien_removal3. unable_to_submit_lien_removal4. lien_removal_pending5. lien_removal_success_but_lien_not_removed | | repayment | 1. repayment_issue2. repayment_not_accounted3. offline_repayment4. repayment_screen_not_opening | | service_request | 1. servicerequest-others2. service_request3. interest_certificate4. interest_calculation5. noc6. excess_refund | | details_update | 1. details_update2. customer_details_update3. bank_account_update4. email_id_update5. phone_number_update | | voluntary_sell_off | 1. voluntary_sell_off2. sell_off_dispute3. sell-off_request | | customer_drop_off | 1. customer_dropoff2. customer_doesn_t_want_to_continue | | shortfall | 1. sell_off_dispute2. shortfall_issue3. short_fall | | interest | 1. interest_/_charge_dispute 2. interest_amount_incorrect 3. interest_and_charges | | renewal | 1. renewal |

---

## #221 — LSQ BRD For MFD Activations
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

## #222 — MFD Accounts Payable
**Status:** ** Current payout stage. | **Last edited:** Unknown

# MFD Accounts Payable # Problem Statements - Lack of real-time tracking for partner account balances, requiring monthly queries. - Payout delays due to missing or incorrect bank details from MFDs. - No centralized tool for viewing MFD transactions and balances. - MFDs receive payout details via Excel files instead of a dashboard display. ## Expected Impact - Reduce manual calculations and offline payout verification. - Minimize payout delays by removing reliance on Puneet. - Mitigate risk of data loss from local file storage. - Free up analytics team bandwidth from payout calculations. - Simplify payout calculation review, monitoring, and approval. - Provide MFDs with performance visibility to enhance motivation. - Enable future payout-related features, such as processing fees based on credit limits. # Proposed Solution The solution will be implemented in phases: 1. **Foundation Tech:** Automate live commission tracking and accrual calculation. 2. **UI Enhancement:** Integrate real-time financial data into the MFD dashboard. ## Bank Accounts 1. **Volt Bank Account:** - A dedicated account for payout-related transactions. - **Future:** API integration for real-time payment status. 2. **MFD Bank Account:** - Collect bank details during registration. - Notify MFDs about missing or incorrect details via dashboard alerts. - Additional fields for verification: - Joint account status. - Separate "Company Name" and "Bank Account Holder's Name." ## Accounts Payable/Receivable - **AP/AR Table** linked to partner IDs to track accruals and payouts. - Automated accruals based on: - Partner activity. - Commercial agreements. - Balances cleared upon payout. - **Account Ledger** for a clear record of credits (accruals) and debits (payouts). # Requirements ## 1. Registration Process MFDs must provide: - Bank details (Name, Type, Joint Account indicator). - GSTN and Company Name. ## 2. Earnings Page A redesigned "Earnings Page" will feature: 1. **Payout Overview:** Real-time accrual tracking. 2. **Statements:** - Downloadable Commission Statements and GST invoices (PDF). - Real-time transaction data for accuracy. 3. **GST Invoice Management:** - "Raise GST Invoice" button. - E-signable invoice generation and automatic upload. - Downloadable copy for records. 4. **Payout Triggering:** - Without GST: Manual trigger by Volt. - With GST: Automated monthly consolidated payout. # Implementation Details ## Domain Entities ### Partner - **Partner:** Commission-earning entity. - **Partner Company:** Legal entity representation. - **Partner Bank:** Settlement banking details. - **Partner Commercials:** Commission structures. ### Commission - **Accrual:** Earned, unsettled commission. - **Commission Base:** Base amount for calculation. - **Trail Commission:** Recurring AUM-based commission.

---

## #223 — Notes Bharat
**Status:** Unknown | **Last edited:** Unknown

# Notes <>Bharat Negotiations table - we will close self-line until we can ensure 1 self-line per partner account. - Rate change, and PF - In tata we can’t change the Rate , so cashback is the option for the Tata. TDS Accounts payable Payment ops Commercials data on the entity - there are three entities applications partner platform that dictate commcials there is a base rate as per the lender that will be assigned by the BRE now once the ROI and PF are assigned to the user then the commencial terms should be added to the application as well on a applciations level we have We have different commercial terms with the on three entity levels application Partner Platfrom the commercials are the the param used to calculate the payout made for the user the Base rate is assigned as per the lender pricing grid of the time of application creation There is default commercials rate that get assigned to Partners and platform by default there are admin actions which assign for a application differenct ROI and PF and the split between the Volt and partner s we are currently not storing the commercials data on the entities level instead its a excel sheet , which casuses issues when calciualting the Solution possible to add object to the right entity that stores he commercials data Application level - ROI - PF - ROI split - PF slip - Base ROI - Base PF Partner level - offer applicable ? - Offer code - ROI - PF - ROI split - PF slip the ROI , PF and splits can be added to the application or to the partner, if added to the partner all the application created by the partner will be assigned the new commercials. Offer code is applied if the applicable. offer can be set of rules like >5 application in the month x = 5000 rs in the payouts Offer has a applicable to and from date the platfrom Platfroms have the similar - ROI - PF - SLITs - Slab based rules the data flow will be 1. application is created 2. assign base ROI and PF from the Lender pricing Grid 3. assign the Application level negotiated Rates collected from Admin actions 4. Assign the MFD commercials as default , then change if changed by the admin action 5. the Platform commercials will

---

## #224 — PRD - GST Invoice and Payout statement creation an
**Status:** Unknown | **Last edited:** Unknown

# PRD - GST Invoice and Payout statement creation and approval Volt provides payout to its MFD partners, due to lack of visibility of the Payout amounts Volt gets lots of support tickets. To reduce the number of support tickets we are introducing GST invoice created by volt , Updating the Payout statement , and building flows for getting MFD sign on the Invoices on a regular basis. high level MFD GST invoice flow - Volt Calculate accurate base Payouts - Generate GST Invoice - Send GST tax Invoice to partner - Get approval from Partner over Email - Pay GST invoices - Handle issue if mentioned - Close the GST for the month. ## Phase 1 - Development needed ### Tech - Generate correct Payout and GST number (RCA or Confirmation required from anlytics). We want to know if we are unable to calculate correct number then why. - Generate Invoice creation - Fix Invoice templates (Payout + GSTN) + recon templates - Generation bulk Invoices - Sending Bulk invoices - Email with personalised invoices and confirmation google form (need to verify if we can use google form for this ) - Storing the Invoices and consent agasint Accounts payable and payments - creation of Accounts payable <>invoice, Payment <>UTR, Accounts payable <>Debits/credits ledgers ### Business - Process to Verify GSTN (manual) - Process to collect / modify Bank accounts with maintained records - Process to take approvals for Payouts and GSTN - Process for tracking and storing issues in Payouts - Process for triggering reconciliation payouts and communications - Process for sharing GST data with Jars - Process for updating reconciled payouts with Ledgers - Process for approval of the Reconciled payouts ## Phase 2 - Role based access and dashboard for MFD, Admin and others. ## User flows ### Registration - MFD need to Register and be activated with us to be eligible for a payout - MFD need to provide there bank account and GSTN - Take it on UI , partner dashboard - Take it over Email - We need to Verify Bank account and GSTN - - For Bank account verification - Get the bank account data from partner Database - IF there is no Bank account data / Invalid bank account data/ Customer requests a change then we trigger a email to add/update bank account - We verify the bank account with Penny

---

## #225 — VOLT MFD Payout Process Overview
**Status:** Unknown | **Last edited:** Unknown

# VOLT MFD Payout Process Overview ## **1. Introduction** VOLT provides **Loan Against Securities (LAS)** services, with **Mutual Fund Distributors (MFDs)** accounting for **70%** of the business. The payout process must ensure: - **Accuracy** - **Visibility** - **Transparency** - **Quick turnaround time (TAT)** - **Efficient issue resolution** ### **1.1 Payout Process Workflow** 1. **Registration** – Onboarding entities for payouts 2. **Activation** – Meeting eligibility requirements 3. **Calculation** – Computing payouts and tax deductions 4. **Payment** – Disbursement of funds to entities 5. **Reconciliation** – Verifying and settling transactions --- ## **2. Registration** Entities must be registered with VOLT to be eligible for payouts. ### **2.1 Entity Categories** 1. **Customers / Borrowers** – Required to open credit accounts. 2. **MFDs** - **Volt Direct** – Registered on VOLT platform - **SaaS MFDs** – Onboarded through partner platforms - **Affiliates** – Engaged through business deals 3. **Platforms** - **B2B / SaaS** – Engaged through business agreements ### **2.2 Registration Platforms** - **Volt B2C** (App & Web) - **Volt Partner Dashboard** - **B2B SDK** - **MFD SaaS SDK** ### **2.3 Registration Details** - Customer: Basic details - MFD: Commercial agreements, POC details ### **2.4 Communication Channels** - MFD Partner Dashboard - Email - WhatsApp --- ## **3. Payout Activation** ### **3.1 Customers** 1. **MFD Selfline** - Special LAS offer at reduced rates for MFD family members - **Current Process**: Eligible MFDs report to RMs → RMs submit Excel file for approval - **Proposed Process**: Automate self-line applications for registered MFD numbers 2. **Customer Cashback** - Offered when base rate **exceeds** advertised rate (e.g., 10.49% > 9.99%) - **The system detects eligible customers through queries** ### **3.2 MFDs** 1. **Volt Direct MFDs** - Eligible when: - A referred customer opens a credit line - The referred customer signs up with the MFD’s code - MFD registers a bank account & GSTN 2. **SaaS MFDs** - Eligible when: A referred customer opens a credit line - **Issues:** - Unclear data collection process for bank accounts & commercials - No clear data storage process 3. **Affiliates** - Non-MFD influencers (e.g., YouTubers) - Eligible when leads convert to credit lines 4. **Platforms** - Activated by Business Development - Payouts based on: - **Total business volume** - **Agreed commercial terms** --- ## **4. Payout Calculation** Payouts consist of: - **Base Payout** (Base rates, Negotiated rates, Marketing offers, Slab-based rules) - **TDS** (Tax Deducted at Source) - **GST Tax** -

---

## #226 — Volt MFD Payout & GST Invoice Process
**Status:** Unknown | **Last edited:** Unknown

# Volt MFD Payout & GST Invoice Process ## Overview Volt provides payouts to its MFD partners. However, due to a lack of visibility into payout amounts, there are frequent support tickets. To reduce these, we are introducing: - GST invoices generated by Volt. - Updates to the payout statement. - A structured process for MFD sign-off on invoices. ## MFD GST Invoice Flow 1. Calculate accurate base payouts. 2. Generate the GST invoice. 3. Send the invoice to the partner. 4. Obtain partner approval via email. 5. Process payments for approved invoices. 6. Address any reported issues. 7. Close GST for the month. --- ## **Phase 1: Development Requirements** ### **Tech Development** - Ensure accurate payout and GST calculations (analytics RCA required if discrepancies arise). - Invoice generation: - Fix the templates (Payout + GSTN) and reconciliation templates. - Enable bulk invoice generation. - Email bulk invoices: - Personalized invoices. - Use Google Forms for confirmation (verify feasibility). - Store invoices and consent records: - Map invoices to accounts payable, payments, and debit/credit ledgers. ### **Business Processes** - Manually verify GST numbers. - Maintain a structured process to update bank accounts. - Define approval workflows for payouts and GST. - Track and store payout-related issues. - Trigger reconciliation for payouts and communicate updates. - Share GST data with Jars. - Update reconciled payouts in ledgers and get approvals. --- ## **Phase 2: Enhancements** - Role-based access and dashboards for MFDs, Admin, and other stakeholders. --- ## **User Flows** ### **MFD Registration** 1. MFDs must register and provide: - Bank account details. - GSTN. - Submission via UI (partner dashboard) or email. 2. Verification Process: - Fetch bank details from the partner database. - If missing/invalid, trigger an email request for updates. - Verify via Penny Drop (avoid joint accounts). - Validate GSTN through [gov.in](https://services.gst.gov.in/services/searchtp). - Manually verify 140+ GSTNs and update records. ### **Payout Processing** 1. **Eligibility:** - MFDs receive payouts as per agreed terms. - GST-registered MFDs receive GST invoices. - Payouts above ₹15,000 incur TDS. 2. **Invoice Generation:** - Analytics generates payout and GST calculations. - Verifies bank accounts and GSTN. - Creates payout and GST invoices. - Updates ledgers accordingly. - Assists business in resolving partner queries. ### **Acknowledgment & Communication** - Payout details are shared via email and dashboard (Phase 2). - Email templates: - **Registration request** (if bank account/GSTN is missing). - **Payout confirmation

---

## #227 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #228 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #229 — Product log issues
**Status:** Unknown | **Last edited:** Unknown

# Product log issues # Product Issues Analysis (Dec 2024 - Feb 2025) | Issue Type | Count | Key Instances | Impact & Details | | --- | --- | --- | --- | | Partner Portal 400/403 Error | 15+ | • Jan 20, 2025: Mithun Bar (919732809934) • Jan 17-20, 2025: Sagar Panchal (919033356722) • Dec 2024: Multiple MFDs | • Recurring access issues • Usually resolved with refresh/incognito model • Major impact on RMs | | DigiLocker/Verification Issues | 12+ | • Dec 31 - Jan 2: 78 customers affected • VTS-8619 • VTS-8159 | • System-wide outage • Blocked customer onboarding • Required provider digio intervention | | SEBI Debarred Error | 6+ | • Jan 16: AAHPF9809K, AYUPK7591E • Jan 13: VTS-8892 (4 PANs) | • False positives for valid PANs • KFin integration issue • Delayed customer processing | | TATA Agreement Issues | 8+ | • Jan 23-24: VTS-9171 • Jan 31: VTS-9344 (5 days stuck) | • Agreement loading failures • Extended processing delays • Required tech intervention | | Mandate Setup Issues | 10+ | • Jan 22: VTS-9149 • Jan 23: VTS-9176 • Jan 28: VTS-9291 | • NPCI redirect failures • Physical mandate problems • Bank account validation errors | | Shortfall Communication Issues | 7+ | • Jan 20: BCFPC7140B • Dec 27: Multiple MFD complaints | • Incorrect notifications • Persisting alerts post-payment • Customer confusion | | MF Fetch Issues | 5+ | • Jan 27: Multiple RTA failures • Jan 29: 2 TATA account cases | • RTA integration problems • Portfolio visibility issues • Fetch retries needed | | Partner Portal Download Issues | 4+ | • Dec 29: Statement download failure • Jan 31: VTS-9439 | • Mobile app limitations • Document access problems • Required web portal workaround | | Wrong Customer Details Display | 10+ | • Feb 1: VTS-9443 • Feb 1: DSNPD8476F/AEXPA7781B mix-up | • Data mismatch issues • Partner confusion • Transaction risks | | Payment Gateway Issues | 3+ | • Jan 15: 1.15cr limit issue • Jan 18: BUWPR6312M PG error | • Transaction limits • Payment processing errors • Required manual intervention | ## Summary Statistics - Total Unique Issues: ~80+ - Most Frequent: Partner Portal 400/403 errors (15+ instances) - Highest Impact: DigiLocker outage (78+ customers affected) - Longest Duration Issue: TATA Agreement

---

## #230 — ARN mandatory for new Registrations
**Status:** Unknown | **Last edited:** Unknown

# ARN mandatory for new Registrations ### **Problem Statement:** - Currently, the partner registration flow allows users to sign up with or without providing an ARN. This has led to a high volume of registrations from individuals who are not certified Mutual Fund Distributors (MFDs). - Approximately 70% of current partner registrations fall into this category. This influx of non-MFD sign-ups places a significant strain on the onboarding team, requiring manual filtering and follow-up, reducing overall efficiency. ### **Proposed Solution:** Modify the partner registration process to require a valid AMFI Registration Number (ARN) for successful sign-up. This will ensure that only verified MFDs can register as partners on the platform. ### **Implementation Requirements:** - **Target Page:** https://staging.voltmoney.in/partner/signup/ (and subsequently production) - Only applicable on New registrations , not existing MFDs - **UI Changes:** - Remove the option/checkbox/link currently allowing users to proceed without an ARN (e.g., "I don't have an ARN number"). - Modify the ARN input field to be mandatory. - **Field Validation:** - The ARN field must not be empty upon form submission. - ~~The entered ARN must consist of exactly **6 digits**.~~ - *(Note: For this initial implementation phase, no external validation against the AMFI database is required.)* - **Error Handling:** - If the user attempts to submit the form without entering an ARN, display a clear inline error message (e.g., "ARN is required."). - ~~If the user enters an ARN that is not exactly 6 digits, display a clear inline error message (e.g., "ARN must be exactly 6 digits.").~~ - **Informational Text:** - Add clear text near the ARN field to inform users about the requirement and guide non-MFDs. Use the following text: > Enter your AMFI Registration Number (ARN)* > > > *Only registered Mutual Fund Distributors (MFDs) can sign up as partners. If you are an investor looking to use Volt Money, please go to our [**Customer registration**](https://www.google.com/url?sa=E&q=https%3A%2F%2Fapp.voltmoney.in%2F%3Fstartnew%3Dtrue).* > **Expected Outcomes & Benefits:** - **Reduced Non-MFD Registrations:** Significantly decrease (estimated 70% reduction) the number of sign-ups from users without a valid ARN. - **Improved Onboarding Efficiency:** Allow the onboarding team to focus solely on qualified MFD partners, streamlining the verification and activation process. - The Existing MFD has no impact / change **Potential Risks & Considerations:** - **Lower Overall Registration Volume:** Expect an initial decrease in the *total* number of registration submissions. However, the number of *qualified* registrations should remain stable or increase relative

---

## #231 — API Integration Changes for MFD Migration to LSQ A
**Status:** Unknown | **Last edited:** Unknown

# API Integration Changes for MFD Migration to LSQ Accounts **Document: API Integration Changes for MFD Migration to LeadSquared Accounts** ## **1. Introduction & Goal** This document outlines the necessary changes to the existing API integration between our internal systems (e.g., Redvision/Middleware) and LeadSquared (LSQ) to support the migration of Mutual Fund Distributors (MFDs) from the LSQ **Leads** module to the **Accounts** module. The primary goal is to leverage LSQ's Accounts feature for better B2B relationship management of MFDs, separating them distinctly from end-customer leads while maintaining the ability to track their performance and associate customer activities/loans back to the correct MFD partner. ## **2. Current API Usage Summary (Pre-Migration)** - **MFD Creation/Updates:** Using LSQ Lead APIs (Lead.Create, Lead.CreateOrUpdate, Lead Capture) to create/update MFDs as Lead records (Lead Type = MFD). - **Customer Lead Creation:** Using LSQ Lead APIs or ULC Connector. MFD referrer information is likely stored in custom fields on the customer Lead record. - **Opportunity Creation:** Using LSQ Opportunity APIs (Opportunity.Create), linked to the *customer Lead*. - **Activity Logging:** - Using LSQ Activity APIs (Activity.CreateOnLead) or ULC to post activities (like status changes, performance metrics updates, PARTNER_... events) *directly onto the MFD Lead record*. - Customer-specific activities (loan creation, MFC check) are posted on the *customer Lead record*. ## **3. Required API Changes (Post-Migration)** The core change involves shifting MFD record management from Lead APIs to Account APIs and adjusting how activities are logged and linked. **3.1 MFD Creation** - **Old Method:** Lead.Create / Lead.CreateOrUpdate / Lead Capture API. - **New Method:** POST {{host}}CompanyManagement.svc/Company.Create or POST {{host}}CompanyManagement.svc/Company/Bulk/CreateOrUpdate - **Changes Required:** - Replace API calls creating MFD Leads with calls to the Account creation endpoints. - **Payload Construction:** - CompanyType: Must specify the correct CompanyTypeName configured in LSQ for MFDs (e.g., "MFD Partners", "Distributors"). This needs to be set up in LSQ Account Settings first. - CompanyProperties: Provide an array of Attribute/Value pairs. - **Mandatory:** Attribute: "CompanyName", Value: [MFD's Name or Firm Name] - **Map Existing Lead Fields:** Map current MFD Lead fields (PAN, ARN, Partner Code, Type, Email, Phone*, etc.) to corresponding Account fields (default or custom cf_... schema names created during setup). - Example Pair: { "Attribute": "cf_arn_no", "Value": "ARN12345" } - Example Pair: { "Attribute": "EmailAddress", "Value": "mfd@example.com" } - Example Pair: { "Attribute": "cf_partner_code", "Value": "PARTNERXYZ" } - **Phone Number Handling (Redvision MFDs):** If the requirement is to *not* use the primary Phone field,

---

## #232 — Term Loan Communications
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

## #233 — Term Loan Customer Statements
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

## #234 — Term Loan DPD handling
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: DPD handling ## **Handling of Days Past Dues (DPD) for Overdue Tranches** ### **Definition of DPD** - **Days Past Due (DPD)** is the number of calendar days an EMI remains unpaid beyond its scheduled due date. - DPD shall be calculated **per tranche/EMI** and maintained at both: - **Tranche level** → to identify overdue EMIs. - **Loan account level** → to reflect overall delinquency status. --- ### **DPD Lifecycle & Tracking** - **0 DPD:** EMI due on the due date but not yet paid. - **1–13/18 DPD:** Period after the due date until the 2nd Mandate presentation. - **14/19 DPD onwards:** If the 2nd NACH also bounces, account enters persistent delinquency. - Post sell-off, if dues are cleared, DPD for corresponding tranches resets to **0**. - If sell-off proceeds are **insufficient**, DPD continues to accrue on residual overdue balance. --- ### **DPD & Apportionment Interaction** - When sell-off proceeds are received: 1. First, they are applied to the **oldest overdue tranche (highest DPD)**. 2. Within a tranche, proceeds are apportioned as: - Interest component → Principal component → Charges. 3. Once all overdue tranches are cleared, any remaining proceeds are applied towards: - Upcoming EMIs (not yet due), then - Loan-level excess balance. --- ### **DPD in Customer Communication(To be closed)** - Customer statements and notifications shall explicitly display: - Current DPD status per tranche. - Total overdue amount by DPD bucket (e.g., 1–30 days, 31–60 days). - Post-sell-off DPD reset (or residual overdue if sell-off insufficient). --- ### **Regulatory & Credit Bureau Reporting** - DPD values shall be reported to credit bureaus as per regulatory guidelines (CIBIL/Experian/Equifax). - If overdue persists beyond sell-off (due to insufficient collateral proceeds), the updated DPD must continue until full settlement. - Correct mapping of **tranche-level DPD → loan-level delinquency** must be ensured in reporting systems. --- ### **Exception Handling** - If AMC redemption is delayed (T+1/T+2), DPD continues to accrue until proceeds are actually realized. - In case of system error or partial sell-off, DPD is adjusted retrospectively once final proceeds are credited.

---

## #235 — Term Loan Disbursement
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Disbursement ### First Drawdown Based on the Submit opportunity status the subsequent flow will be decided: **Submit Opportunity Failure:** - Loan and Tranche Account won’t be created and LSP will have to re-trigger the request **Submit Opportunity Success(Disbursal Success):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. - Our payout partner acknowledges the request and initiate the payout from their end. - Once the amount gets debited from our bank account we get a debit success response. - Post the debit from our Bank Account the amount will get credited to the customer’s bank account. This is when we get a credit success response. - Once we receive a credit success response we will be posting the disbursal in the ledger and accordingly a Tranche account will be opened. - Based on the disbursal amount, tenure and interest rate the repayment/EMI schedule gets generated. **Submit Opportunity Success(Disbursal Failure):** - Loan Account is created and Disbursement workflow is triggered. - Once the Disbursement workflow is triggered we will block the DP of the user. - The Disbursement/Payout request is then sent to our Payout partner. There are multiple scenarios once the disbursal/payout request is triggered from our systems: 1. The request is not triggered resulting in an instant failure of the disbursement. In such a case we need to retry initiating the request until it gets triggered to the Payout partner. 2. The request is triggered from our system but due to the Payout partner system being down we get an error resulting in disbursement failure. In such a case we need to re-trigger the request at the same time we receive the error from our payout partner or we can wait for sometime before re-triggering the request. 3. The request is received by the payout partner and the same is acknowledged through a response but the debit from our bank account does not happen and we get a debit failure response. In such a case we need to re-trigger the disbursal request(Depends on tech handling, if we are not able to handle this in V0 then we can mark the disbursal as failure and inform the LSP of the same for them to re-trigger the request and we unblock

---

## #236 — Term Loan Foreclosure
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

## #237 — Term Loan Manual Repayments(PG)
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

## #238 — Term Loan Manual Repayments(VA)
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

## #239 — Term Loan Prepayments and Excess Handling
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

## #240 — Term Loan Unpledge Eligibility API(Post loan creat
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

## #241 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #242 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #243 — MFCentral CAS API Response Structure Analysis
**Status:** Unknown | **Last edited:** Unknown

# MFCentral CAS API Response Structure Analysis ## Top-Level Structure ```json { "reqId": "string", // Request identifier "pan": "string", // PAN number of the investor "pekrn": "string", // PEKRN (optional identifier) "mobile": "string", // Mobile number with country code "email": "string", // Email address (optional) "data": [ // Array of fund house holdings { "summary": [...], // Summary data for this fund house "schemes": [...] // Array of schemes under this fund house }, // Additional fund houses... ], "portfolio": [ // Overall portfolio summary { // Non-demat holdings summary }, { // Demat holdings summary } ], "investorDetails": { // Investor information // Address and contact details }, "statementHoldingFilter": "string" // Filter applied (e.g., "NON-ZERO") } ``` ## Fund House Data Structure Each element in the `data` array represents holdings from a single AMC: ```json { "summary": [ { "amc": "string", // AMC code "amcName": "string", // AMC full name "isDemat": "string", // "Y" or "N" for demat status "currentMktValue": "number", // Current market value "costValue": "number", // Total investment amount "gainLoss": "number", // Profit/loss amount "gainLossPercentage": "number" // Profit/loss percentage } ], "schemes": [ { // Detailed information for each scheme } // Additional schemes... ] } ``` ## Scheme-Level Structure Each scheme contains detailed investment information: ```json { "amc": "string", // AMC code "amcName": "string", // AMC full name "folio": "string", // Folio number "investorName": "string", // Investor name "age": number, // Investor age "mobile": "string", // Registered mobile "email": "string", // Registered email "taxStatus": "string", // Tax status code "modeOfHolding": "string", // Single, Joint, etc. "transactionSource": "string", // Source of transaction (BSE, etc.) "schemeCode": "string", // Unique scheme identifier "schemeName": "string", // Complete scheme name "idcwChangeAllowed": "string", // Income Distribution Change allowed flag "schemeOption": "string", // Growth, IDCW, etc. "assetType": "string", // EQUITY, DEBT, etc. "schemeType": "string", // Classification "nav": "number/string", // Current NAV "navDate": "string", // NAV as of date "closingBalance": "number/string", // Total units held "availableUnits": "number/string", // Redeemable units "availableAmount": "number/string", // Value of available units "currentMktValue": "number/string", // Total current value "costValue": "number/string", // Total investment amount "gainLoss": "number/string", // Profit/loss amount "gainLossPercentage": "number/string", // Profit/loss percentage "isDemat": "string", // "Y" or "N" "lienUnitsFlag": "string", // "Y" or "N" "decimalUnits": number, // Decimal places for units "decimalAmount": number, // Decimal places for amounts "decimalNav": number, // Decimal places for NAV "brokerCode": "string", // Distributor ARN code "brokerName": "string", // Distributor name "isin":

---

## #244 — Periskope to wati plan
**Status:** Unknown | **Last edited:** Unknown

# Periskope to wati plan # Periscope to Wati Migration Plan ## 1. Current Periscope Issues - No effective tracking of incoming chats or resolutions - Lack of chat status visibility (open/resolved/WIP) - Unable to monitor active chat groups - No categorization between sales and service chats - Missing bulk chat download capability - No response time (TAT) tracking - Agents losing track of ongoing conversations - Limited team capacity (2 people per shift) - No chat closure mechanism - Unclear analytics definitions - Missed chats going unnoticed - Integration issues with WATI ## 2. Metrics Comparison ### Current Periscope Metrics - Total interactions count - Unopened messages - Basic chat volume - Group activity status ### Available Wati Metrics - Open/Pending/Solved tickets - First Response Time - Resolution Time - Bot vs. Operator solutions - Expired conversations - Missed chats - Operator performance - Message delivery status - Conversation types - Tag distribution ## 3. Migration Goals 1. Improved Tracking - Real-time chat status - Response time monitoring - Issue categorization 2. Better Resource Management - Automated workflows - Clear agent allocation 3. Enhanced Analytics - Detailed performance metrics - Customer satisfaction tracking 4. Streamlined Operations - Automated responses - Efficient ticket management ## 4. Migration Plan with Checkpoints ### Phase 1: Setup (Day 0) - [ ] Configure Wati dashboard - [ ] Set up automated responses - [ ] Create tags and categories - [ ] Test message templates - [ ] Train agents **Checkpoint Metrics:** - System functionality - Template delivery success - Agent readiness scores ### Phase 2: Initial Migration (Day 1) - [ ] Migrate single and inactive MFDs - [ ] Monitor initial responses - [ ] Track conversion rate - [ ] Handle exceptions **Checkpoint Metrics:** - Message delivery rate - Response times - System stability ### Phase 3: Main Migration (Day 2-3) - [ ] Migrate remaining MFDs excluding top 250 - [ ] Monitor scalability - [ ] Adjust resources as needed **Checkpoint Metrics:** - Chat volume handling - Resolution rates - Customer feedback ## 5. Communication Templates ### Periscope Exit Message ``` Dear [MFD Name], To enhance your support experience, we're upgrading our communication channel. From [Date], we'll be transitioning to a new WhatsApp support system. Key Points: - Last day on current system: [Date] - New support number: [Number] - Transition period: [Duration] For any questions, please contact

---

## #245 — rough
**Status:** Unknown | **Last edited:** Unknown

# rough notes - Tat on a chat , - ticket resolution and creation - check whatsapp api changes Ideal flow MFD is had a request or a issue they communicate the issue with us we mark it as issue and solve it MFD —> Issues —> communications —> Tickets—> solution - IF a MFD or there employees have issues they can reachout to volt and we want to solve the issues promtly - MFD can communicate with us through WhatsApp chat - Now we need to Identify the issues , create a ticket and resolve the ticket Current problems - We don’t have the ticketing system in place - Current tools we are using are not optimal for creating and tracking Tickets Raw notes - The MFD facing challenges in getting timely response - All the onboarded MFD are added to periscope group - MFD’s uses WATI when they interact through Dashboard chat - MFD’s has to use two separate chat channel if they open up a Whatsapp channel through Wati - MFD’s ask , servicing , payout topic of communications are of general nature. our challenges - We have limited ( can’t) tracking of the incoming chats and there resolution - This is a Periskope limitation. we don’t get Open , resolved , WIP status of a Chat - we are unable to check “How many chats groups are active “ , “were active last week “ - We can’t identify if chats are Sales or service related - we get ~100 chats a day - There is no Bulk download chat option in Periscope - we can’t see TAT for a response and resolution - - agents loose track of the ongoing chats , as it chats are pushed to the bottom of the que and it become a issue to differentiate between the chat groups - 2 people work on the periscope - No way of closing the chats and mark that issue was solved - Analytics- daily number of message counts, Flagged messages - no explanation of what these terms are - How to raise tickets is not clear to the team - we use Periscope to reach out to MFDs , If a MFD reach-out and RM are unavailable then we assign another agent to Periscope - group is already connected with Periscope , all all the MFD are added to periscope they are

---

## #246 — API doc
**Status:** Unknown | **Last edited:** Unknown

# API doc # Partner Platform APIs Documentation from Bipul :-[https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing](https://docs.google.com/document/d/1i2dm7ridzJmCJ9iI1M3cH9Z1VZlo6bbvrS68OjtYLEU/edit?usp=sharing) ## Authorization All APIs require Bearer Token authentication. ### Required Headers | Header Key | Header Value | Mandatory | | --- | --- | --- | | X-AppPlatform | Platform Code, provided at the time of onboarding | Yes | | requestReferenceId | Unique reference Id for request (UUID recommended) | Yes | | Authorization | Bearer Token | Yes | ## APIs ### 1. Interest Collection API Retrieves interest collection details for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/interestDue/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 2, "data": [ { "creditId": "8a807f598f570684018f594c153801ff", "lender": "Tata", "customerName": "VINEET GARG", "customerPhoneNumber": "+919412732271", "customerEmail": "UP81BDK@GMAIL.COM", "interestAmount": 15051.0, "totalDues": 15051.0, "interestPaymentStatus": "Settled" } ] } ``` ### Error Responses - **404:** Partner not found ```json { "voltErrorCode": "BAD_REQUEST_RESOURCE_NOT_FOUND", "message": "Partner with the provided partner code does not exist", "statusCode": "404" } ``` - **500:** Internal server error (in case of internal failure) ### 2. Shortfall API Retrieves shortfall information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/shortfall/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 2, "totalPages": 1, "data": [ { "creditId": "8a807f099026416501902adec63c37d1", "lender": "Bajaj", "accountHolderName": "REETA MAHESHWARI", "accountHolderPhoneNumber": "+917983849357", "accountHolderEmail": "up81charu@gmail.com", "shortfallAmount": 34788.0, "dueAmount": 34788.0, "agingDays": 6, "status": "DUE" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ### 3. Renewal Details API Retrieves renewal information for partner customers. ### Endpoint - **Method:** GET - **URL:** `{{baseUrl}}/v1/partner/platform/las/partner/{{partnerCode}}/partnerdashboard/renewal/{{pagination}}` ### Response ### Success Response (200) ```json { "currentPage": 1, "pageSize": 50, "actualpageSize": 1, "totalPages": 1, "data": [ { "creditId": "8a8078438b71536f018b7157b8d70000", "lender": "Bajaj", "customerName": "RITUL JIGNESHBHAI SANGANI", "customerPhoneNumber": "+918320042935", "customerEmail": "ritujsangani@gmail.com", "principleOutstanding": 835.34, "dueDate": "01 November 2024" } ] } ``` ### Error Responses - **404:** Partner not found - **500:** Internal server error ## Common Features - All APIs support pagination - Default page size is 50 - Responses include pagination metadata (currentPage, pageSize, actualpageSize, totalPages) - All endpoints require the same set of headers - Common error handling patterns across all APIs

---

## #247 — Repayment_Schedule_3900 (4)
**Status:** Unknown | **Last edited:** Unknown

# Repayment_Schedule_3900 (4) ![](Repayment_Schedule_3900%20(4)/image1.png) --- Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) --- RANJAN SINGH S/O: Dinesh Singh,shivalya bhawan,Sector, 03,nandgawn,Singrauli,Singrauli,Madhya, Pradesh,486887 Singrauli- 486887,Madhya Pradesh 7980565882 ranjan.singh@voltmoney.in --- Branch Name DELHI - RAJENDRA PLACE Product Type LAS Customer Name RANJAN SINGH Currency INR Loan Account No. 3900 Frequency Monthly Rate of Interest per annum [%] 10.19 Loan Status Active Loan Amount [Rs.] 315.00 Total Installment [Rs.] Total Tenure (in month) 12 Balance Installment [Rs.] Loan Sanctioned Amount [Rs.] 50,500.00 Charges Outstanding 0.00 Loan maturity date 07-Oct-2026 [Rs.] Available Amount for 49,998.00 Interest Rate type Floating Disbursement [Rs.] ![](Repayment_Schedule_3900%20(4)/image2.png) --- | | | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | Installment no . /TypeDue Date / Transaction DateOpening Balance [Rs.]Installment Amount [Rs.]Principal [Rs.]Interest [Rs.]Closing Balance [Rs.]Efftect Rate(%)Transaction TypeF07-Oct-2025407.000.000.000.00407.0010.19Facility DateD13-Oct-2025407.000.000.000.0010,407.0010.19DisbursementD17-Oct-202510,407.000.000.000.0030,407.0010.19DisbursementD20-Oct-202530,407.000.000.000.0045,407.0010.19DisbursementD27-Oct-202545,407.000.000.000.0049,907.0010.19Disbursement131-Oct-202549,907.00196.840.00196.8449,907.0010.19P17-Nov-202549,907.000.000.000.0049,906.0010.19Part Payment230-Nov-202549,906.00417.900.00417.9049,906.0010.19P02-Dec-202549,906.000.000.000.0030,326.0010.19Part PaymentD08-Dec-202530,326.000.000.000.0031,326.0010.19DisbursementP09-Dec-202531,326.000.000.000.0030,325.0010.19Part PaymentP29-Dec-202530,325.000.000.000.0030,315.0010.19Part Payment331-Dec-202530,315.00268.280.00268.2830,315.0010.19P02-Jan-202630,315.000.000.000.00315.0010.19Part Payment431-Jan-2026315.0011.160.0011.16315.0010.19528-Feb-2026315.002.520.002.52315.0010.19631-Mar-2026315.002.790.002.79315.0010.19 | | | | | | | | | | | | | | | | | | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Repayment Schedule ( Generated on 05/02/2026 16:15:50 ) | | | | | | | | | | | | | | | | | Terms and Condition: The dynamic repayment details provided above are for reference only. Please refer to the Statement of Account (SOA) for actual payments, receipts, and dues. The repayment schedule is drawn from the latest facility date. Interest dues will be basis actual utilisation during the month. The “Available loan amount for disbursement” will be restricted to the net of sanctioned amount and loan amount. | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #248 — Analytics requirement Foreclosure
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Foreclosure | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of foreclosure requests | (count of total requests made today) | | | | | | | | | | Number of requests automatically closed | (count of requests made and closed today) | | | | | | | | | | Number of requests pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(settled_on - created_on) | | | | | | | | | | % requests closed automatically | % of requests that were closed automatically today (identify requests closed manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credits.default.foreclosurerequests ### Field: foreclosurerequests: created_on - When request was created Collections: closed_on - When request was closed automatically Request status ### Table: admin_action_audit admin action name: To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #249 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #250 — Sameer Minde Vaibhav (1)
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav (1) Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #251 — How banks and NBFCs manage rounding of interest an
**Status:** Unknown | **Last edited:** Unknown

# How banks and NBFCs manage rounding of interest and charges, and how they handle accounting in these cases. ## **1. Regulatory & Industry Context** ### RBI Guidelines: RBI doesn’t dictate **how to round**, but it **expects fairness, transparency, and precision** in: - Customer charging - Auto-debit recovery - Tax invoicing - Reconciliation of ledgers So, banks and NBFCs need to: - Ensure **customers aren’t overcharged** - Match debits with invoices/statements - Maintain proper **audit trail** and **variance accounting** if rounding is applied --- ## 2. Rounding Methods Used by Banks & NBFCs | Type | Common Use Case | Real-world Examples | | --- | --- | --- | | **No Rounding (Post exact value)** | Charges with GST, floating interest | HDFC Bank, Axis Bank, Bajaj Finance (on fees), most NBFCs | | **Round to Nearest Rupee** | Interest on EMI loans, penal charges | SBI, ICICI Bank, Fullerton | | **Round Up (Conservative)** | Micro loans, prepaid cards | Some gold loan NBFCs | | **Cumulative Rounding** | Long tenure loans | Used in housing finance | --- ## 3. Detailed Accounting Treatment by Banks/NBFCs ### **A. Exact Posting (No Rounding)** ### Use Case: - Processing fees + GST - Penal charges ### System Flow: 1. Fee computed: ₹100 2. GST @18% = ₹18 3. Total = ₹118.00 (posted and debited as-is) ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹118.00 | | | Processing Fee Income | | ₹100.00 | | GST Payable (Output) | | ₹18.00 | ✅ Matches invoice and is tax compliant --- ### **B. Round at Posting (Nearest Rupee)** ### Use Case: - Accrued interest - EMI interest - Installment schedules ### Example: - Accrued Interest: ₹199.48 → Rounded: ₹199 - Accrued Interest: ₹199.50 → Rounded: ₹200 ### System Flow: - Round value **at the point of debit** ### Accounting Entries: | Ledger Name | Debit (₹) | Credit (₹) | | --- | --- | --- | | Customer Loan Account | ₹200.00 | | | Interest Income | | ₹199.48 | | **Rounding Reserve GL (Internal)** | | ₹0.52 | > 🔸 If we round down, the 0.52 may be debited to an expense account. > ### Why Rounding Reserve GL? To track small deltas between system-calculated interest and posted amount. ✅ Fair

---

## #252 — Activation LSQ Task Creation
**Status:** Unknown | **Last edited:** Unknown

# Activation: LSQ Task Creation Flow: 1. Link generated gets generated and sent to the MFD over whatsapp 2. Task gets published in LSQ 3. RMs follow the tasks for calling and supporting the MFD with the VKYC flow and the link

---

## #253 — KT discussion 19th Feb
**Status:** Unknown | **Last edited:** Unknown

# KT discussion 19th Feb ## Flows - MFDs number - Customer number MFD flow - Pre-empanelment - Outbound → Labdhi - Inbound → OE team - Post empanelment - Outbound → OE team - Inbound → OE team (lead owner) - RM - RM **Leadsquared tracking** - **Inbound call picked** - **Inbound call task with disposition** - **Backup lead owner** - Check team / attribute - Backup assignee should have lead access - Missed call task - Outside business hours - No Assignee available - Assigned but not picked - Inbound call activity / duration / activity **Other questions** - If lead doesn’t exist? **Notes:** - whats will happen if we change role/team name on LSQ, how switch case will work - Discuss in exotel - Need to check if we are saving owner details of all lead on volt DB - Need to check with ENOSH - If no lead found on LSQ then what will happen in case of exotel inbound, create lead and assign to team based on lead origin - Exotel inbound call - lead info modal should open on LSQ dashboard - If outside of business hours, create missed call task - If unanswered, create task for lead owner - Labdi teams call should assign to Volt Onboarding team - Ask Exotel to share BRD and take sign-off from Volt - What will be ETA on Exotel to implement solutions

---

## #254 — User had an existing line with Tata, when he tried
**Status:** Solutioning pending | **Last edited:** Unknown

# User had an existing line with Tata, when he tried to take a loan again it failed due to dedupe logic at Tata Classification: Tata existing loan customer Notes: To be closed and discussed with Tata PRD/Solution mapping: Pending Platform: Wati Reference Link/ID: 918250858364 Status: Solutioning pending

---

## #255 — User was given a higher sanction amount than their
**Status:** Solutioning pending | **Last edited:** Unknown

# User was given a higher sanction amount than their credit limit, was able to place a withdrawal request before lodgement was done Classification: Sanction Amount and credit limit handling Notes: Sanction amount instead of credit line amount is shown to the customer before lodgement, ideally withdrawal should be blocked or better communicated, there should be a failed state for all transactions PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13404 Status: Solutioning pending

---

## #256 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #257 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #258 — Content
**Status:** Unknown | **Last edited:** Unknown

# Content 1. Title: Loan offer 2. Hero details: 1. Selected loan amount. 2. Credit limit available. 3. Benefits: 1. Trusted lender Tata capital 2. Unlimited withdrawals 3. Repay principal anytime 4. Pay interest only on what you withdraw 5. Monthly Interest only EMI of only ₹862 for ₹1,00,000 withdrawal at 10.49% interest (Interest should be communicated upfront) 4. Charges: 1. Interest rates: 10.49% p.a. 2. Early repayment/ foreclosure: Free 3. Withdrawals: within 4 hours 4. One time processing fee (excl. GST): ₹840 1. Processing fee is charged once in the whole term 5. Stamp duty (as per registration state): ₹260 6. Term: 36 months (Renewal available) 5. CTA: 1. Withdraw in 4 steps

---

## #259 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Pledging will not affect the growth, Financial goal for which you started, long term plan gets hampered, no cibil requirement, Repay any time, Being in control, Reducing interest, Kevin (Servicing): unpledge request 10% buffer, shortfall, bad sell off experience, change in Sanction limit Mahesh: NBFC license, TATA and Bajaj, Names: Trust Naveen: - No brand val - GST india - NBFC license - Lenders

---

## #260 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: rate of interest, foreclousure, processing fees, lein removal, repayment, additional top up, stocks, Kevin (Servicing): Instant disbursals, Delays, Unpledging and Forclosure. ELSS funds are possible for TATA, Schedule the loan disbursal time, Mahesh: Interest, How it works, Repayment. phone pe traffic is greater than influencers, Reconstruct their houses. Names: Main areas of concerns Naveen: Portfolio value, Location. I dont feel like I am doing the Pledging step Requirement : Urgency. Pay somebody, reinvest, NFO Bugs on app vs web

---

## #261 — DSP Fin Partner Page
**Status:** Unknown | **Last edited:** Unknown

# DSP Fin: Partner Page # Context RBI requires REs to disclose LSP details in a standard template. While we do the elegant website change, we want to modify only the partners page to be compliant with regulatory requirements. # Requirements As per the RBI guidelines on DLG here, RBI requires REs to disclose the following details. 1. Details of all of its digital lending products and its DLAs; 2. Details of LSPs and the DLAs of the LSPs along with the details of the activities for which they have been engaged for; 3. Particulars of RE’s customer care and internal grievance redressal mechanism; 4. Link to RBI’s Complaint Management System (CMS) and Sachet Portal; 5. Privacy policies and other details as required under extant guidelines of the Reserve Bank. We will display the below details in the current partners page. - Name of LSP - Nature of Service Availed from LSP's - Description of the LSP - DLA of the LSP - Additional Information about the Lender Sample file is attached for reference. [DSPFin Website Disclosures of LSP DLA.odt](DSP%20Fin%20Partner%20Page/DSPFin_Website_Disclosures_of_LSP_DLA.odt) # Benchmarking A few other lenders who display the LSP details are listed below. - InCred: https://incred.com/partnership/ - Piramal : https://www.piramalfinance.com/about-us/lending-partners - BFL: https://www.bajajfinserv.in/bajaj-finserv-partners - ABFL: https://www.adityabirlacapital.com/loans/our-digital-lending-platform-partners

---

## #262 — MNRL Validation - GTM Rollout for LSPs
**Status:** Unknown | **Last edited:** Unknown

# MNRL Validation - GTM Rollout for LSPs **Context** As per the RBI mandate, financial institutions must verify customer mobile numbers against the Mobile Number Revocation List (MNRL) - a DoT dataset of deactivated, fraud-flagged, or cybercrime-linked numbers. Numbers tied to LEA-reported cybercrime, fake/forged documents, or TSP internal flags must be blocked from proceeding to loan creation. LSPs do not need to implement MNRL checks themselves. DSP handles all validation, data sync, and compliance reporting. LSPs only need to handle the rejection response gracefully in their integration. **What gets blocked and why ?** Numbers appear in MNRL for multiple reasons. DSP will block loan creation due to these reasons: - LEA-reported cybercrime: number flagged by law enforcement for cybercrime activity - DoT fake/forged cases: number associated with fraudulent or forged documentation - TSP internal analysis: flagged by telecom operator through internal fraud detection **Where checks happen in the journey ?** There are two validation touchpoints: 1. Create Opportunity - OpportunityID is not created if blocked. 2. Submit Opportunity - LoanID is not created if blocked. **What LSPs need to do ?** LSPs have no action required on the MNRL validation itself, DSP manages that entirely. What LSPs must do: - Handle the `USER_BLACKLISTED_MNRL_CHECK` error code at both the Create Opportunity and Submit Opportunity endpoints - LSPs can display the blocking message to the user on UI **Rejection response - at both endpoints** When a user's number is blocked, DSP returns an HTTP 400 at both `/opportunity` and `/opportunity/{id}/submit`: ``` { "fenixErrorCode": "USER_BLACKLISTED_MNRL_CHECK", "message": "User blacklisted due to MNRL check", "statusCode": "400" } ``` LSPs should look for `fenixErrorCode === "USER_BLACKLISTED_MNRL_CHECK"` and render the blocking UI accordingly. **What error message should LSPs need to show on UI ?** Message Copy : *Sorry, your application currently doesn’t meet lenders eligibility criteria. You can always try again later*.

---

## #263 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #264 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can

---

## #265 — Product Release Process
**Status:** Unknown | **Last edited:** Unknown

# Product Release Process # Challenges Below are the key challenges in the current release process. - Bugs on production environment impacting customers & users - Features being rolled out having bugs/issues leading to quality concerns - Stakeholders have concerns on lack of feature understanding or change - Customers are impacted or have a poor experience on production due to mismatch in requirements vs. development. - Number of man-hours spent on bugfixes increase due to functional clarity lacking. The above challenges arise due to the below elements. - Features are being rolled out with or without QA sign-off but no product sign-off - Bugs and fixes are being rolled without product sign-off - Fixes and changes are being done without any training for stakeholders - There’s no design sign-off before deploying UI capabilities on production - No formal release note is being sent to stakeholders # Proposed Solution Below are the interventions proposed to solve these challenges. - All features would go through a product sign-off is there’s any impact on any existing or new functionality. - All features would go through a design sign-off if there’s any UI/UX impact on any functionalities. - All bugs or fixes including logic changes that impact any functionality will go through a product sign-off. - All bugs or fixes including logic changes that impact any functionality will go through a design sign-off for UI/UX features. - Any feature that won’t meet the product and/or design sign-off criteria will not be allowed to deployed to production. - All new features, including enhancements and bug-fixes that change flow or logic will require a formal release note and training session. While the above items are undertaken, the PM should also setup the required monitoring capabilities by setting up reports or dashboard through Analytics on their own. # Proposed Process ## Sprint Features Below is the broad process for sprint features. - Once the requirements are closed for the sprint, program team informs the PM team of the timelines for QA sign-off. - Product team keeps the test scenarios handy which is shared upfront as part of requirements with tech. - Program team informs the PM and Designer about the timeline for QA sign-off. PM and designer will review the test scenarios on QA or staging environment. - PM and/or designer informs the program team if a feature is signed-off and good to go on Jira. If

---

## #266 — Product note template (Duplicate this for use)
**Status:** Unknown | **Last edited:** Unknown

**In scope:**
- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users

# Product note template (Duplicate this for use) ## **Background and Context** - - Who is facing the problem (users, internal teams, partners) - What is the challenge that they are facing? What is broken today? - Why is it important? or What is getting impacted? --- ## **1. Problem scope** ### In scope - - What specific problems are we solving? - Who are we solving it for? Consider both primary and secondary users ### Out of scope - - Call out on items out of scope - Rationale for exclusion --- ## **2. Success Criteria** - Top 2-3 **clear outcomes that we are looking to achieve**. - Key success metrics (Conversion rate / Error rate / TAT) - Define post launch good state (Expected behaviour / uptime / SR) - Guardrail metrics (Metrics that should not degrade) --- ## **3. Solution Scope** ### Solution overview - Explain in 2-3 lines the overview of the solution - Explain overview of the solution with key product and system changes - Explain the rationale on scoping/phasing of the solution - Call out scope that has been scoped out and explain the rationale ### Detailed solution scope: - Bullet list of user and system use cases that are supported: - Define all use cases applicable and what are in scope - Core happy path - Key edge cases that must be handled at launch - Consider all the stakeholders that are impacted - Has to answer questions like: - How does this change existing operational SOPs? - How does this change the experience for the end user? - How does this impact sales or onboarding conversations? | Description | Details | | --- | --- | | | | | | | | | | --- ## **5. High level s***ystem, user or process flow* - - Cover the overview of the process or the journey - Include error cases or edge cases (Optional) --- ## **6. Appendix (Optional)** ### Benchmarking: ### User feedback / Calling: