# Current State: Kyc

> Auto-generated from 161 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — PRD - Mandate conversion optimisation via swap in
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

## #4 — Standard Operating Procedure Approving Uploaded Fi
**Status:** In progress | **Last edited:** September 27, 2024 10:40 AM

# Standard Operating Procedure: Approving Uploaded Files on CKYC ## Version Control - Version: 1.0 - Last Updated: 26 September 2024 - Drafted By: @Vaibhav Arora - Approved By: @Gautam Mahesh @Nishant Athmakoori (Please verify here) ## Purpose This SOP outlines the steps for approving an uploaded file on the Central KYC Records Registry (CKYCRR) system. This document covers the list of activities to undertaken by the operations team after the system has passed the data to CKYC for upload. The files that are accepted by CKYC are to be approved on the portal for the records to be finally accepted and updated at their end. ## Scope This procedure applies to all checker users responsible for authorising bulk uploads in the CKYCRR system. ## Prerequisites - Access to the CKYCRR system with checker privileges - Only following users can approve an uploaded file on Cersai dashboard: - Institutional admin - (Amrita and Priya) - Regional admin (For region level files) - No user as of now - Branch admin (for Branch level files) - No user as of now - Familiarity with the CKYCRR user interface Refer user manual attached below **Note**: Additional users can be added as needed. [User_Manual_CKYC1.pdf](Standard%20Operating%20Procedure%20Approving%20Uploaded%20Fi/User_Manual_CKYC1.pdf) ## Procedure 1. **Access the Bulk Upload Authorization Screen** - Log in to the CKYCRR system - Navigate to "KYC Management" in the main menu - Click on "Bulk KYC Authorization" 2. **Review Pending Uploads** - The screen will display a list of batches pending for checker approval - Each batch will show details such as Batch ID, Upload Date, Upload Type, and Number of Records 3. **Select a Batch for Review** - Click on the radio button next to the batch you want to review 4. **Examine Uploaded Data** - Click on the "Upload file" link to open and review the uploaded data file - Ensure the data complies with KYC requirements and institutional policies 5. **Make Approval Decision** - If the data is correct and compliant: - Click the "APPROVE" button - If there are discrepancies or issues: - Enter the reason for rejection in the "Remarks" field - Click the "REJECT" button 6. **Digital Signing (for Approval)** - When approving, a pop-up will appear to select your digital certificate - Select your registered digital certificate from the list - Click the "Sign" button to complete the approval process 7. **Confirmation** - Verify that the system displays

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

## #6 — Additional documents upload for Bajaj for AS ES DI
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

## #7 — Bajaj PAN verification API
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

## #8 — [Lending stack] LOS - Command centre
**Status:** Not started | **Last edited:** September 18, 2024 3:52 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #9 — MFD Saas channel
**Status:** Not started | **Last edited:** October 8, 2024 6:02 PM

# MFD Saas channel we have a partner channel where we integrate with MFD(mututal fund distributors) SAAS providers to offer Loan agaisnt Mfs, funtianlity - this service allows MFD to check credit linmit of there clinets and guide them with credit loans instead of selling there securities - We want to manage these partners as they are a high leverage way to get new clients in crease AUM - this will provide compitive advantage and Distribution - We need to solve the product stack for the SAAS partners, MFDs, Clients/customers - we need to support Potenttial custoomer with education and details about the product - we need to suppoirt Live incase or error or bloackages in the funnel - we need to support in case of Servicing requests currently all customer/loan leads are piped in LSQ, MFD details from partner are not mapped , Saas compaines like redvision etc ” ” | In Redvision, Platform & customer mapping is there, but MFD mapping is not there.Problem- RM can't see which MFD's customer is this via redvision- MFD number has to be fetched via Retool- OBD & IBD calls are not updated in LSQ- -Partner reachout % cannot be tracked as the call doesn't get mapped in LSQ.- Redvision POS with us is of 62 CrAsk-B2B2C functionality in LSQ to be replicated for RedVision-Customers tagged to an MFD should be tagged to MFD owner(RM)-Outbond/Inbound activity to be captured in LSQ | Shivansh | P0 | Out of 190 cases cases completed in August in none of the cases parter I'd is tagged. | | --- | --- | --- | --- | | Periscope integration -Delayed chat timing | Shivansh | P0 | -~120-150 unique group chats daily.-30% cases are for pre loan queries (mandate, KYC, Sanction, OTP, etc)-35% of cases are for post loan (SOA, Lien, Mandate failure,Interest, GST etc)-Increase in average response time-Escalations due to non response, customer experience.-Nitin Ohri response after 2.5 hrs on tuesday-Pooja - Chat not closed, response not provided timely-issue SS attached -[MFD issues/escalation](https://docs.google.com/document/d/1IATz2SYr_cjjeU4biepT2_1_1hRnusCd9wO5sXpwDtM/edit?addon_store) | | MFD and customer tagging for FundsIndiaAsk- B2B2C functionality in LSQ to be replicated for FundsIndia- Twin platform functionality for Funds India different user base to be checked for feasibility from soluting POV | Shivansh | P1 | 10/15 cases per day are assigned wrongly to B2B RM (Mrigaank) | | Partner dashboard revamp | Shivansh | P1 | -Display

---

## #10 — User getting stuck at KYC verification step in cas
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

## #11 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** October 7, 2024 11:27 AM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #12 — Volt - DSP LSP Integration Flow
**Status:** Not started | **Last edited:** October 7, 2024 11:14 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #13 — Email Validation Approach PhonePe
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

## #14 — Change in audit trail flow for PAN Validation API
**Status:** Pending Review | **Last edited:** October 17, 2024 8:05 PM

**Problem:**
are we solving?**

In the applications in which we are not able to fetch PAN details (POV=null), the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

**Solution:**
?**

---

## #15 — Integrated Sales tool
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

## #16 — Lender selection logic for BRE for production
**Status:** Ready for Tech | **Last edited:** October 11, 2024 4:47 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

I’m not able to find the logic of TATA/BAJAJ based on fetch limit

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

## #18 — Name storing from different sources
**Status:** Not started | **Last edited:** October 11, 2024 11:26 AM

**Problem:**
are we solving?**

Currently, we don’t store user names from different sources (PAN, Aadhar, Bank) in a structured, queryable format. This leads to inefficiencies during analysis and debugging, as names must be individually retrieved from writing query for each source through Amazon CloudWatch, resulting in increased latency.

---

**Solution:**
?**

---

## #19 — Pledge error handling v1
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

## #20 — Process note Creating a new user on Command Centre
**Status:** Done | **Last edited:** November 8, 2024 9:36 AM

# Process note: Creating a new user on Command Centre # Process Note: Creating a User on Command Centre ## Overview This document outlines the step-by-step process for creating a new user account on the Command Centre system. ## Prerequisites - Admin access to the Command Centre system - New user's details (full name, email address, role, department) - Approval from Head of Operations (@Nishant Athmakoori) [Access level details](https://docs.google.com/spreadsheets/d/1VSPMYia-Kmwob9X3pH-T3nMTYNZxXpEC_Afpfq27e-o/edit?gid=0#gid=0) ## Steps 1. Request for access on Email from the business counterpart, in this case, all access will be shared by @Nishant Athmakoori 1. Details required in the email: 1. Name 2. Designation 3. Role (Admin / Approver / Read only) 4. Employee ID 5. Mobile number 6. Email address (DSP Email address) Any requests without the aforementioned details will get rejected 2. Forward the access with consent and approval to tech-ops@dspfinance.com 3. Access will be shared within 1 working day of request. 4. Once access is shared (User name and password), logon to the command centre using the following URL: https://cc.dspfin.com/login 5. Once logged on, users will be able to use the command centre for the following utilities: 1. Client search (all roles) 2. Loan search (all roles) 3. Review client details (all roles) 4. Review client KYC details (all roles) 5. Review client risk details (all roles) 6. Review loan details (all roles) 7. Review transactions (money and collateral) (all roles) 8. View servicing tasks (Approver and admin only) 9. View collateral tasks (Approver and admin only) 10. View application tasks (Approver and admin only) 11. View NBFC operations tasks (Approver and admin only) 12. Approve or reject tasks (Approver and admin only) ## Post-Creation Steps - Document the new user creation in your system log or user management spreadsheet ## Troubleshooting If you encounter any issues during this process, please contact the IT support team at tech-ops@dspfinance.com

---

## #21 — MFD Channel
**Status:** Not started | **Last edited:** November 4, 2024 1:23 PM

# MFD Channel Volt provides LAMF MFD are important MFD - Onboarding - Activation - Servicing Capabilities - To Disburse loans - In 30mins - without documents # MFD Channel PRD ## Executive Summary - Product Overview - Volt provides loan against mutual fund. - - Business Objectives - Stakeholders - MFDs - ### MFD User Persona for Volt Money At Volt Money, Mutual Fund Distributors (MFDs) play a vital role in connecting clients to our Loan Against Mutual Funds (LAMF) product. These professionals manage their clients' investments and are constantly on the lookout for opportunities to increase their revenue streams, primarily relying on trail commissions from their AUM (Assets Under Management). LAMF allows MFDs to provide liquidity to their clients without the need to redeem their mutual fund units, offering a seamless option to access funds while keeping investments intact. This approach also benefits MFDs by earning them commissions in the process, making it a win-win situation. ### Why MFDs Choose Volt Money The reasons MFDs opt for Volt Money go beyond just financial incentives. Sure, we offer competitive interest rates on LAMF products, generally ranging between 10.4% and 10.69%, which attracts both MFDs and their clients. We also give MFDs ₹200 for every account opened, along with an annual 0.5% commission on trades. However, the service we offer makes a big difference too. Each MFD is assigned a dedicated Relationship Manager (RM) to ensure smooth operations and personalized support, something many competitors don’t provide. ### The MFD Journey at Volt Money The MFD journey starts with client sign-ups, which we’ve designed to be as frictionless as possible. Clients go through OTP verification followed by PAN validation through Decentro’s API, which doesn’t require a date of birth, making the process smoother for clients. The next step is fetching collateral data, a critical process for securing loans. We retrieve this data from major RTAs like CAMS and KFintech, using the ISIN number to identify available and locked mutual fund units. For added security and ease, we also integrate MF Central to obtain transaction data. Once collateral is secured, the client is assigned a lender. We work with multiple lenders, such as Tata, which requires a minimum CIBIL score of 650. Our business rule engine ensures that the client is matched with the right lender, though we have had occasional fallback mode issues that we’re actively addressing. ### Verification and Disbursement

---

## #22 — Father’s name validation removal
**Status:** Not started | **Last edited:** November 30, 2025 12:18 PM

**Problem:**
are we solving?**

LSPs are currently seeing high rejection rates at the **Submit Opportunity** stage due to mismatches between the user-entered *father’s name* and the value returned from KYC.

Since the RBI’s KYC Master Directions do **not** mandate verification of the father’s name—and it is required only for CKYC reporting—strict validation is unnecessary. Most regulated entities rely on customer-provided details with minimal checks, which aligns with our revised approach.

---

**Solution:**
?**

---

## #23 — TCL Credit Referral Automations & optimisations
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

## #24 — Volt B2B Redirection Enhancement - Park+
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

## #25 — QC rejection flow handling for DSP - Volt LOS
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

## #26 — New Posidex report template
**Status:** In progress | **Last edited:** November 20, 2024 4:54 PM

**Problem:**
are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

**Solution:**
?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

---

## #27 — NLP-736 Timestamp value is not captured with hh mm
**Status:** Not started | **Last edited:** November 19, 2024 7:41 AM

# NLP-736: Timestamp value is not captured with hh:mm:ss due to which the default value 05:30:00 is shown in the UI Command centre search result pages: Client creation date (client search) Expiry date (loan search) Bureau pull date (client details risk section) AML pull date (client details risk section) Mandate expiry date (loan details section) Expiry date (is in small case) KYC expiry date is comming as invalid date Completed on (repayment detail is coming as invalid detail)

---

## #28 — External reporting requirements
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

## #29 — CC design QC
**Status:** Not started | **Last edited:** November 13, 2024 2:21 PM

# CC design QC ## To-do - [ ] QC approve buttons size - [ ] QC approve buttons color - [ ] Unify primary color across command center - [ ] Do a QC of color of tags used and standardise the colors according to use case - [ ] Toast colors ## Items to check | **Item** | Problem | **Action** | Notes | **Status** | | --- | --- | --- | --- | --- | | CTA size: QC/Approval | Button size is small | Update size from 22 → 32 | | | | | | | | | | Nav link selected item | Accessibility issues | - BG: #F1FCFA → Primary 50 - Text: #1CCDBC → Primary 600 | | | | CTA: filled | Brand green clashes with success | #1C8980 → Primary 600 | | | | CTA: filled | Unnecessary shadow | Remove shadow | | | | CTA: Link | Brand green clashes with success | #1C8980 → Primary 600 | | | | CTA: Outline | Brand green clashes with success | #1C8980 → Primary 600 | Used in: - Table: Action - | | | Pagination CTA | Brand green clashes with success | #1C8980 → Primary 600 | | | | Review CTA in Application table | | - Remove shadow - #1C8980 → Primary 600 | | | | Line tabs: active | Brand green clashes with success | #1C8980 → Primary 600 | Text + Underline color | | | Box tabs: active | Brand green clashes with success | #1C8980 → Primary 600 | Text + outline color | | | Box tabs: unselected | Unselected looks as if it’s selected | Text: #1C8980 → Indigo 900 | Tabs in QC | | | | | | | | | Radio | Brand green clashes with success | #1C8980 → Primary 600 | In “Search” modal | | | | | | | | | Tag refer img 1A | Wrong color | Green preset from AntD | Cust details → KYC → verified tag | | | Tag: Success, Active | Accessibility | Green preset from AntD | | | | Tag: Filter | | | | | | | | | | | | Loader | Aesthetics | Skeleton loader | Library to implement it | | ## Legend - Neon

---

## #30 — KYC Risk Status (NBFC Platform)
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

## #31 — MFD Tier & Performance Data Activity Passing in LS
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

## #32 — Bajaj VCIP (VKYC) Integration
**Status:** In progress | **Last edited:** May 5, 2025 11:56 AM

# Bajaj VCIP (VKYC) Integration [ PRD - presentation](Bajaj%20VCIP%20(VKYC)%20Integration/PRD%20-%20presentation%20111e8d3af13a8091bb28f05972a78172.md) [https://voltmoney.atlassian.net/browse/PSB-225](https://voltmoney.atlassian.net/browse/PSB-225) [API details ](Bajaj%20VCIP%20(VKYC)%20Integration/API%20details%20115e8d3af13a80ddb907e9f5f03d68bf.md) [VCIP GTM Plan ](Bajaj%20VCIP%20(VKYC)%20Integration/VCIP%20GTM%20Plan%2013be8d3af13a8047bfbecaf270f9594d.md) # Product Requirements Document (PRD) ![Loan agaisnt MF journey (1).png](Bajaj%20VCIP%20(VKYC)%20Integration/Loan_agaisnt_MF_journey__(1).png) ## **Table of Contents** ## **Executive Summary** Volt Money aims to integrate the RBI-mandated Video KYC (V-KYC) into our loan disbursement process with Bajaj Finance. The proposed solution enhances regulatory compliance while maintaining a seamless customer experience by restructuring the loan application flow. This document outlines a strategic plan to implement V-KYC effectively, addressing potential challenges and ensuring robust support mechanisms. --- ## **1. Objective** - **Primary Goals:** - **Regulatory Compliance:** Fully comply with RBI's V-KYC guidelines and Bajaj Finance's KYC protocols. - **Enhanced User Experience:** Minimize friction in the KYC process to reduce drop-off rates. - **Operational Efficiency:** Streamline backend operations and reduce manual interventions. - **Flexibility:** Allow users to complete V-KYC within a 72-hour window post DigiLocker KYC. --- ## **2. Challenges** ### **Regulatory and Operational Constraints** 1. **Compliance:** Adherence to RBI's V-KYC guidelines is mandatory. 2. **Time Window:** Users have 72 hours post DigiLocker KYC to complete V-KYC. 3. **Customer Availability:** V-KYC sessions are limited to working hours (9 AM - 6 PM). 4. **Operational Costs:** un-pledging due to drop-offs is costly and dependent on Bajaj. ### **Technical and User Experience Challenges** 1. **Integration Complexity:** Synchronizing with Bajaj's V-KYC APIs across multiple platforms. 2. **Potential Drop-Offs:** Additional mandatory steps may overwhelm users. 3. **Technical Issues:** Connectivity, device compatibility, and API reliability concerns. 4. **Re-Engagement:** Effectively re-engaging users who abandon the process. --- ## **3. Solution** ### **Proposed Approach** Loan application Flow 1. Digilocker 2. BAV 3. Pledge 4. Agreement 5. Mandate 6. VKYC - New 7. Disbursement Key Points - Reduced top of the funnel drop - Reduced number of Leads for sales for VCIP step improving sales efficiency **~~Loan Application Flow:~~** 1. **~~DigiLocker KYC:** Initial KYC verification.~~ 2. **~~V-KYC:** Users can either:~~ - **~~Start Now:** Immediate V-KYC session.~~ - **~~Schedule Later:** Choose a convenient time within the 72-hour window.~~ 3. **~~Bank Account Verification (BAV):** Verify bank details.~~ 4. **~~Agreement:** Sign loan agreement.~~ 5. **~~Mandate Setup:** Set up automatic debit mandate.~~ 6. **~~Pledge:** Final pledge of securities.~~ 7. **~~Disbursement:** Loan amount disbursed after V-KYC completion.~~ **~~Key Components:~~** - **~~Flexible V-KYC Scheduling:** Users can opt to start V-KYC immediately or schedule it, reducing immediate friction.~~ - **~~Moved Pledge Step:** Pledge is moved to the final step to ensure V-KYC completion before

---

## #33 — NSDL PAN Verification — Non-STP Rejection Handling
**Status:** Not started | **Last edited:** May 28, 2026 3:16 PM

**Solution:**
?**

---

## #34 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #35 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 6:56 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #36 — Jupiter webhook requirements
**Status:** Not started | **Last edited:** May 22, 2024 12:00 PM

**Problem:**
are we solving?**

1. Create webhooks that jupiter will consume to send utility comms

---

**Solution:**
?**

---

## #37 — Dropping PAN Verification flow
**Status:** Not started | **Last edited:** May 21, 2026 7:53 AM

**Problem:**
are we solving?**

In the LAMF digital loan journey, customers are required to set up an eNACH mandate as part of the Loan Origination System (LOS) process. The **mandate value is fixed at ₹10 lakhs**, irrespective of the customer’s actual credit limit, which may range from **₹10,000 to ₹2 crore**.

This “one-size-fits-all” approach creates friction for customers with lower credit limits. For example, a customer with a sanctioned limit of ₹50,000 may be reluctant to authorize a ₹10 lakh mandate, leading to abandonment of the journey at this step and/or increase in the number of support queries

**Solution:**
?**

---

## #38 — Consent Architecture FE requirements
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

## #39 — PhonePe Funnel conversion - 14th May
**Status:** Not started | **Last edited:** May 15, 2024 11:00 AM

**Problem:**
are we solving?**

1. Reducing friction in PhonePe journey and increasing conversion

---

**Solution:**
?**

---

## #40 — Term Loan LOS requirements
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

## #41 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** May 12, 2026 4:07 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #42 — DSP PhonePe PG Integration for PhonePe
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

## #43 — [Volt LSP] Integrating DSP KYC
**Status:** Not started | **Last edited:** March 3, 2025 2:38 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #44 — New Product Spec (PRD)
**Status:** Not started | **Last edited:** March 24, 2026 11:57 AM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #45 — [Volt LOS] KYC optimisations
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

## #46 — MFD channel Journey
**Status:** In progress | **Last edited:** March 18, 2025 3:22 PM

# MFD channel Journey Goals - Reduce RM dependency per application by 50% - Increase application within 20 min TAT to 20% ## Problem statements ![Tata TAT between steps.png](MFD%20channel%20Journey/Tata_TAT_between_steps.png) ![DSP TAT between steps.png](MFD%20channel%20Journey/DSP_TAT_between_steps.png) ### **Portal Layout** 1. MFDs prioritize seeing all customer names in one place rather than their application status. Currently, customers are split into "Pending Applications" and "Completed Applications," which makes it harder for MFDs to locate them. ### **Registering Customers** 1. Multiple entry points exist for application creation, such as "Register Customer" and "Check Eligibility." ### **Fetch** 1. MFDs often don’t see all customer-held funds during the application journey, requiring RMs to explain ineligible funds and guide them to MFC detailed fetch (Check Eligibility). 2. MFDs find changing the mobile number at the fetch step unintuitive. They assume the system is wrong when the customer has funds, but the entered number does not. The system does not highlight the need to change the number if there is no data for the mobile number. 3. MFDs frequently miss the “Get Portfolio” step after fetching from the first RTA, leading them to call RMs saying, *"Saare funds nahi dikh rahe" (not all funds are visible).* The MFC fetch resolved this issue. 4. We don’t show in-eligible funds in the app journey. 5. We can check if the PAN has funds from MFC API, MFC summary Vs RTA fetch vs. detailed 6. NFT app I take phone number 1, phone number 2 and fetch all the funds from there , see Small case journey. ### **Offer Page** 1. Customers are unclear about the benefits of LAMF over redemption when presented on the offer page. 2. Customers hesitate to proceed if the limit is significantly lower than their expected amount based on available funds. 3. MFDs want to understand why certain funds are ineligible and call RMs for clarification. 4. The limit is first calculated and selected by Tata which has fewer approved fund from DSP 5. ~~MFDs cannot select the loan tenure and must contact RMs to change lenders. They frequently request a shift from a 3-year to a 1-year tenure to meet their clients' short-term needs. the New RBI regualrtioons will be one tenure~~ 6. Approved ISIN tool, approved list of isin share to aMFD ### **KYC** 1. MFDs are unaware of the required steps in the application journey. They do not anticipate that Digilocker KYC requires the customer's

---

## #47 — Pre-fetch flow optimisation Email entry verificati
**Status:** Not started | **Last edited:** June 9, 2025 11:10 AM

**Problem:**
are we solving?**

Friction in the user onboarding journey due to capturing and verifying email too early (before MFC fetch), resulting in unnecessary drop-offs and poor user experience.

Additionally, the early verification step adds tech complexity without delivering tangible value during the initial steps of the journey.

---

**Solution:**
?**

---

## #48 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #49 — Bajaj KYC Coborrower enhancement and renewal
**Status:** Not started | **Last edited:** June 5, 2024 1:29 PM

**Problem:**
are we solving?**

1. Currently users with joint holdings can not do KYC.
2. Customer with Bajaj lender will not be able to enhance or renew their line. 

---

**Solution:**
?**

---

## #50 — Aadhaar QR scan
**Status:** Not started | **Last edited:** June 26, 2025 11:33 AM

# Aadhaar QR scan 1. Perfios Walk-through completed: SDK includes: 1. Scan QR (scanner) 2. Upload QR 3. Fetches and displays the data 4. To verify the email and phone, the customer has to enter email and phone Steps: 1. Scan QR/ Upload QR 2. Perfios de-codes the data on the QR 3. Fetches the data from UIDAI 4. Verify the email and phone Downside of SDK: Cannot be used for web-app (MFD portal) Perfios gave a walk through for the OCR KYC Plus: 1. Upload the Aadhaar 2. Scans the QR itself 3. Gives the address as the outputD 1. Bureau ID gave the following demo: 1. Upload the Aadhaar QR of the customer 2. It provides: 1. Adhaar last 4 digits 2. careOf 3. District 4. DOB 5. gender 6. location 7. landmark 8. mobile number registered? 9. email registered? 10. name of the customer 11. signature base64 12. state 13. street 14. sub district But when I gave it my black and white aadhaar and another coloured aadhaar card photo, they could not process it. They provide an API based solution thus it can be used across for web-app and mobile-app usage.

---

## #51 — DSP UPI Autopay Integration for PhonePe
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

## #52 — Addition of City-State to CKYC Request in Decentro
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

## #53 — DSP UPI Autopay Integration for NBFC
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

## #54 — [DSP] NSDL PAN Verification alignment
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

## #55 — B2B Zype integration FE and SDK callbacks
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

## #56 — UPI Autopay Product note
**Status:** In progress | **Last edited:** July 9, 2025 12:24 PM

**Problem:**
are we solving?**

- Customers need to keep their Debit card or Netbanking details handy for setting up NACH, which results in drop-offs.
- MFDs need to ask customers for their Debit card or Netbanking details, which involves OTP, etc resulting in drop-offs and increased queries.
- Physical NACH which covers most banks requires considerable human intervention in completing the flow resulting in drop-offs.
- ESign NACH which covers ~450 banks has very high failure rates due to bank account not linked to Aadhaar, mobile linkage issue b/w account and Aadhaar, etc.

---

## #57 — Tata Video KYC Integration V0
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

## #58 — NBFC Capturing Additional details post KYC
**Status:** Ready for Tech | **Last edited:** July 11, 2025 12:42 PM

**Problem:**
are we solving?**

Few LSPs integrating with our stack do not capture all the necessary ‘Additional Details’ or ‘declarations’ required by DSP to process the loan. In such cases, LSPs expect the DSP to collect these details directly from the customer.

---

**Solution:**
?**

---

## #59 — Untitled
**Status:** Not started | **Last edited:** July 11, 2025 10:33 AM

**Problem:**
are we solving?**

For DSP lender, finalising the values of additional details and decalarations that we need to take from the customer. 

---

**Solution:**
?**

---

## #60 — Front loading the MF Fetch step in application
**Status:** Not started | **Last edited:** January 8, 2025 9:00 PM

**Problem:**
are we solving?**

Our current application conversion stand at ~14%, while the industry standard for conversion is closure to 70%. We have a lot of ground to cover in our conversion percentage. 

---

**Solution:**
?**

---

## #61 — DSP PhonePe LSP Integration
**Status:** In progress | **Last edited:** January 30, 2025 1:26 PM

# DSP: PhonePe LSP Integration # Context # Journey ## Application ### KYC - Customer initiates the KYC flow through DL on the PhonePe TPAP - PhonePe calls their internal DL KYC API managed by their KYC platform team - The PhonePe internal KYC API calls Signzy DL integration - The customer is shown the UI of DL on the TPAP - The customer is redirected to the DL page and completes the journey - PhonePe KYC team receives the KYC datapoints from DL through Signzy - PhonePe lending team receives the KYC datapoints from their KYC team - PhonePe/Signzy triggers the datapoints to DSP’s endpoint as mentioned [here](DSP%20PhonePe%20LSP%20Integration%2018ae8d3af13a80f4ae4df92506d24898.md). - DSP does the name check at its end as well as photo match and responds to PhonePe with Success or Failure ### Mandate ## Servicing # Integration ## KYC - PhonePe’s DL account is at PhonePe level (parent entity) - DSP finance can get a sub-account under the above account Open points. - Can Signzy trigger an independent webhook to DSP’s endpoint? - Can PhonePe KYC team trigger an independent webhook to DSP’s endpoint instead of the lending entity? | Request Curl | Parameter Description | Max Field Length | Data Type | Mandatory / Non Mandatory | | --- | --- | --- | --- | --- | | { | | | | | | "uid": "8879608641", | Alphanumeric Id to be generated | 15 | Varchar | Mandatory | | "productCategory": "CL", | Fixed value = "CL" to be passed | 5 | Varchar | Mandatory | | "sourcingChannel": "CLEAG", | Fixed value = "CLEAG" to be passed | 10 | Varchar | Mandatory | | "type": "kycValidate", | Fixed Value | 50 | Varchar | Mandatory | | "id": "a3m0k0000033lQTAAY", | Common and Unique Identifier across all the APIs | 50 | Varchar | Mandatory | | "AddressLine1P": "Bhayander", | | 255 | Varchar | Mandatory | | "AddressLine2P": "Thane", | | 255 | Varchar | Non Mandatory | | "PincodeP": "400033", | | 6 | Numeric | Mandatory | | "kycType": "Digilocker", | Digilocker | | | Mandatory | | "ekycId": "K13656433547667", | Digilocker id | | | Non Mandatory | | "applicantFirstName": "Shankar", | | | | Mandatory | | "applicantLastName": "Paradkar", | | | | Mandatory | | "applicantMiddleName": "Ramesh", | | | | Non Mandatory | | "applicantDOB": "1994-02-11" | | yyyy-mm-dd

---

## #62 — [Volt LSP] DSP QC rejection handling
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

## #63 — CKYC Upload for DSP
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

## #64 — White Labeled Partner portal for the MFDs
**Status:** Ready for Tech | **Last edited:** January 22, 2025 12:46 PM

# White Labeled Partner portal for the MFDs ### **1. Objective** To provide a white-labeled version of the Volt Partner Dashboard, tailored for Investwell's MFD partners, enabling seamless loan application creation and management with long-term support and enhanced user experience. ### **Problems to Solve** Investwell has two modes of integration with Volt **MFD Portal - investwell.voltmoney.in** - The existing MFD partner dashboard lacks updates, leading to technical issues and poor user experience. - KYC and Selfie capture journey steps get stuck **User facing Application** - Currently Investwell has implemented URL redirection journey. which has Stablity issues whenever the URL redirection happens in the journey Overall - SaaS partners like Investwell routing volumes conservatively due to limited support of the Portal provide - MFD’s having stuck are unlikely to come back - Users might issue in journey on KYC or mandate steps ### **Target Users** - **MFDs (Mutual Fund Distributors):** Facilitate the creation and management of loans for their customers. - **Platform Integrators (e.g., Investwell):** Ensure seamless integration with their ecosystem. ### **Requirements** ### **Login and Signup** - **Access Control:** - Auto-login from the Invest well MINT platform. - **User Journey:** - MFDs log in directly via custom Investwell-branded login. - Access to the new dashboard in a new browser tab. ![Customers - shortfall (1) (1).png](White%20Labeled%20Partner%20portal%20for%20the%20MFDs/Customers_-_shortfall_(1)_(1).png) ### **Dashboard Features** **Application Management:** - Create, track, and manage loan applications. - Credit limit checks in 15 seconds. - Pending applications with page-nation - interest , renewals, shortfalls, dashboard - Completed applications **Branding** - Removal of Volt logos where feasible (except certain unavoidable pages). - **Stability** - SDK implementation for improved customer LAMF journey experience. - Enhanced stability over the existing URL redirection. Dashboard /portal - Ability to create application - Ability to check Credit limit - Ability to send the application links - Ability to service the customers - List of registered customer and their status - Download SOA - See Interest , shortfall, renewal details - Un-utilised credit limits - ~~Partner profile~~ - Customer management features: - Customer registration - Customer Journey - Eligibility check tool - ~~Customer portfolio viewing~~ - Shortfall - Renewall - Interest payment - all partner customers - ~~Marketing resources:~~ - IFA tools - ~~Capital gain statement viewing~~ - ~~Interest calculator~~ - Support channels - Call - ~~Collected SOA~~ - ~~Raise service ticket~~ - ~~Earnings~~ - ~~Referral program~~ - ~~AUM redemption savings tracking~~ **Phase 2** - FAQs (

---

## #65 — [Platform] Photo verification and liveliness check
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

## #66 — [Platform] QC rejection handling
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

## #67 — [Final] End use capture of transactions
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

## #68 — [Email Template] Decoupling of Lodgement and Agree
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

## #69 — ADMIN Actions for the RM Sales Team
**Status:** Pending Review | **Last edited:** February 27, 2025 3:34 PM

# ADMIN Actions for the RM Sales Team ### **Problem Statement** 1. RMs spend considerable time Raising ops tickets and following up. - ALL B2B2C Admin actions | admin_action | COUNTA of admin_action | | --- | --- | | APPLICATION_ROI_OVERRIDE | 6 | | APPLICATION_RULE_OVERRIDE | 337 | | APPROVE_MANDATE | 45 | | APPROVE_PARTIAL_LIEN_REMOVAL | 14 | | APPROVE_REJECT_LOAN_FORECLOSURE | 44 | | CHANGE_LENDER_FOR_APPLICATION | 927 | | FORECLOSE_LOAN_ACCOUNT | 27 | | FORECLOSURE_REMOVE_SECURITIES_RETRY | 46 | | OVERRIDE_CREDIT_APPROVAL | 4 | | OVERRIDE_ISIN_LTV_BASED_ON_ISIN | 209 | | PROCESSING_FEE_OVERRIDE | 16 | | RECREATE_LENDER_APPLICATION | 96 | | REFRESH_CREDIT_INFO | 173 | | REGENERATE_AGREEMENT_LINK | 1 | | REGENERATE_MANDATE_LINK | 6 | | REVIEW_APPLICATION | 4 | | REVIEW_CO_BORROWER_DOCUMENTS | 65 | | SKIP_PLEDGING_FOR_ENHANCE_LIMIT_APPLICATION | 23 | | SUSPEND_CREDIT_APPLICATION | 563 | | TATA_COLLECTION_SETTLEMENT_RETRY | 199 | | UNIFY_MF_DATA_V2 | 2 | | UPDATE_BANK_ACCOUNT_AFTER_CREDIT_CREATION | 37 | | UPDATE_PARTNER_DETAILS | 13 | | VERIFY_BANK_ACCOUNT | 3 | | Grand Total | 2860 | 1. Actions that RMs can take but have to raise to ops can be reduced 1. Change the user's mobile number and Email, should be able to be changed by RM before Loan agreement creation. ## Success metrics - Reduction in Pre-loan customer details change tickets to Ops - TAT for customer requests for the customer details change Impact The current count is 121 cases in the past 2 months ## Proposed solution - We have built APIs with Lenders Tata and DSP for Post loan Customer details change. Borrowers can use the account details in the Volt portals to alter their details - These APIs are limited to post-loan as they update Client details, and the Client ID is created after the loan creation. For Tata - We create an opportunity for the customer on Tata at the Pan verification step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. For DSP - We create an opportunity for the customer on DSP after the fetch step and share the customer's mobile number. We need to share the change with the lender before making the change in our DB. # **Previous Understanding Proposed Solution** ### **Admin Action Portal Enhancements** - Introduce a **new admin action task** specifically for pre-loan applications to allow agents to process requests efficiently. ### **Workflow for Pre-Loan Admin

---

## #70 — CKYC (Decentro) API integration
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

## #71 — LSQ data sync
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

## #72 — Pledge error handling
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

**Solution:**
?**

---

## #73 — Push missing details on LSQ [PhonePE]
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

For PhonePe, we are creating a lead after the MFC fetch, but the customer name and email are not being pushed to LSQ. This makes it difficult for RMs to conduct sales calls effectively.

---

**Solution:**
?**

---

## #74 — Increase Top-up TOFU & conversion [TCL & DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

The **Line Enhancement (Top-up)** feature allows customers to pledge additional mutual funds to increase their available credit limit. While this is a valuable option for users seeking additional liquidity—such as for emergency needs or after exhausting their approved loan limit—the current adoption of this feature remains significantly low.

**Solution:**
?**

---

## #75 — Loan renewal for TCL customer’s
**Status:** Not started | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

1. We need to handle the loan renewal experience for TCL customers.

---

**Solution:**
?**

---

## #76 — MFC fetch in Volt Journey
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

## #77 — Multiple mandate presentation [DSP]
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

**Solution:**
?**

DSP will **initiate a second mandate presentation on 20th of every month** for accounts with overdue interest and charges, targeting recovery from customers who failed the first attempt and not paid overdue amount till [presentation date - file approval date]

---

## #78 — [Platform] Enabling alternate mandate registration
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

## #79 — Volt LOS journey optimisations
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

## #80 — one page application for Partners RMs
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

## #81 — [Platform] Liveliness check
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

## #82 — [Volt LSP] Liveliness check
**Status:** Not started | **Last edited:** December 23, 2024 8:08 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #83 — [Platform] Risk report
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

## #84 — Volt LSP PAN verification
**Status:** Not started | **Last edited:** December 13, 2024 3:02 PM

**Problem:**
are we solving?**

A high number of customers are currently facing issues with Decentro PAN verification step on the LSP, this need to be solved.

---

**Solution:**
?**

---

## #85 — Lead stage handling on LSQ
**Status:** Not started | **Last edited:** December 13, 2024 11:58 AM

# Lead stage handling on LSQ Lead stages in LSQ Initial Registration Stages: 1. Unregistered 2. Registered Portfolio Stages: 3. Portfolio Fetch 4. Portfolio Fetch KFIN 5. Portfolio Fetch CAMS 6. Portfolio Pledge 7. Portfolio Pledge KFIN 8. Portfolio Pledge CAMS Application Processing Stages: 9. KYC Verification 10. Sign Agreement 11. Link bank account 12. Setup Mandate 13. Verify Photo 14. Application Submitted 15. Loan Created 16. Empaneled Final Status Stages: 17. Partially activated 18. Activated 19. Closed

---

## #86 — Single drawdown Term Loan LMS Requirements
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

## #87 — Amplitude Audit and Additions
**Status:** Not started | **Last edited:** August 20, 2025 12:02 PM

**Problem:**
are we solving?**

Auditing the existing amplitude implementation and listing out all the events to add.

---

**Solution:**
?**

---

## #88 — VKYC for DSP and Co-Lending
**Status:** In progress | **Last edited:** August 19, 2025 7:01 PM

# VKYC for DSP and Co-Lending [LSP Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/LSP%20Focused%20VKYC%20Journey%20Alignment%20238e8d3af13a80cd80c6f64c76ab3aed.md) [Volt Focused VKYC Journey Alignment](VKYC%20for%20DSP%20and%20Co-Lending/Volt%20Focused%20VKYC%20Journey%20Alignment%20216e8d3af13a801bbba2eb686074c82b.csv) [VKYC: Vendor Evaluation](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Vendor%20Evaluation%20217e8d3af13a80dfb53bed7d04c1e7f3.md) [VKYC: Regulatory Understanding](VKYC%20for%20DSP%20and%20Co-Lending/VKYC%20Regulatory%20Understanding%20217e8d3af13a809f88e9f173d73f3d5a.md) [Discussion with Rohan (Groww)](VKYC%20for%20DSP%20and%20Co-Lending/Discussion%20with%20Rohan%20(Groww)%20254e8d3af13a8085a070ce018cec0f02.md)

---

## #89 — [DSP] KYC v2 (including CKYC)
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

## #90 — Command Centre design requirements
**Status:** In progress | **Last edited:** August 13, 2024 7:21 PM

# Command Centre design requirements Problem statement: User should be able to navigate between different interfaces/utilities on the platform **Possible interfaces:** - Side navigation panel (Left) [Example: Material.io](https://m3.material.io/) - Top navigation bar [Example: Apple](https://www.apple.com/) - Drop down menu Example: Trello - Floating action buttons: [https://m3.material.io/components/floating-action-button/accessibility](https://m3.material.io/components/floating-action-button/accessibility) - Card based notifications https://trello.com/u/vaibhavarora56/boards **Utilities between which the user will be able to navigate:** Tasks - All tasks tracking and assignment Search (Client/Application/Credit) - Application level search Notifications NBFC dashboard: SLA tracking Internal user management and access control Analytics dashboard Following are details of each section: - Search requirements - Search - Ops agent should be able to search clients basis the following parameters: - Search customer - Name (Partial match) - Email address (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Client ID (Exact match) - Mobile number (Exact match): Inputs will be validated basis regex validations (Need capability of showing error messaging to the user) - Search line - Line ID (Loan account number) - Client ID (Exact match) - Bank account number (To identify lines to which disbursements were made) - Transaction ID - Search loan application - Application ID (Exact match) - Mobile Number (Exact match) - Search will be partial and absolute basis the match of the metric entered in the search box, if multiple matches are received, Ops agent will see a list of possible matches in the result section. If one match is received directly the client details section will be opened for the ops agent to review (Can this be confusing for the ops agent? Need Design input) - The result screen should include the following parameters in order: - Client - Client ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Client Name (Name of the client) - Client Mobile (Mobile number of the client) - Client Email address (Hyperlinked for one click communication capabilities) - Last 4 digits of Aadhaar for the client - Client creation date (DD-MM-YYYY) - Client status (Active, Pending - in tab format) - Line - Line ID (Alphanumeric, can be trimmed with the last 4 digits visible and the ops agent should be able to copy it directly via a small CTA (sample: Service desk) - Product

---

## #91 — Bank-PAN Name Mismatch in BAJAJ
**Status:** In progress | **Last edited:** August 12, 2024 4:18 PM

**Problem:**
are we solving?**

- Loan Application of users getting rejected by BAJAJ during the Credit Review by BAJAJ due to Bank-PAN name mismatch.

---

**Solution:**
?**

---

## #92 — Product note NSDL PAN Verification
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

## #93 — Application form, T&C and Agreement updation
**Status:** Not started | **Last edited:** April 4, 2025 1:49 PM

**Problem:**
are we solving?**

RBI guidelines requires that lenders and LSP showcase the Agreement, Application form and T&C clearly as per the specified format. Meeting the compliance and clearly stating the terms to user in a elegant way is a challenge.

---

**Solution:**
?**

---

## #94 — Bajaj KYC Pod Requirements
**Status:** Not started | **Last edited:** April 4, 2024 1:53 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #95 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #96 — NSDL PAN integration
**Status:** Not started | **Last edited:** April 29, 2026 5:11 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #97 — Account opening STP optimisations
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

## #98 — Co-Lending (Internal CUG)
**Status:** Not started | **Last edited:** April 26, 2026 4:37 PM

**Problem:**
are we solving?**

-

---

**Solution:**
?**

---

## #99 — VKYC Integration PRD
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

## #100 — CKYC Comms for Regulatory Compliance
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

## #101 — KYC & Mandate Workflow PRD
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

## #102 — CKYC Internal Report
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

## #103 — UPI Autopay
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

## #104 — CKYC Flow integration
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC Flow integration Charter: LOS Pod # Context [[Lending stack] KYC Flow](../PRDs/PRDs/%5BLending%20stack%5D%20KYC%20Flow%20f322514482d7490dbcf3675515b16276.md) # Process - [x] Map flow - [x] Scope out screens - [x] Benchmarking on flows # Figma xhttps://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/%5BNew%5D-Loan-application-journey?node-id=3740-1840&t=182AaW1ur1jUPPnI-11 https://www.figma.com/design/khuVsTb01ruke7QxxOuCYR/Animation?node-id=4-1425&t=xNwnuqSfvRvHUnP7-11

---

## #105 — CKYC New flow
**Status:** Ready for kickoff | **Last edited:** Unknown

# CKYC New flow Charter: LOS Pod Priority: P0 Task type: Sprint # Context Need to work on creating a loader for CKYC flow which would last 10-12s # Process - [x] Selfie screen illustrations - [x] Wireframes for loader - [ ] Final Design # Figma https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=5170-7847&t=zvlUVrpOudLY6mV1-11

---

## #106 — Volt Plugin Knowledge Base
**Status:** Unknown | **Last edited:** Unknown

# Volt Plugin Knowledge Base # Introduction This project aims to build a unified UX writing system for Volt based on fintech best practices. The goal is to have a unified, brand-aligned tone of voice across screens, touchpoints, and teams. ## Problem - Right now we handle error case copies differently throughout the app. - Different writers/designers use different tones, leading to a fragmented experience. - No shared rules for writing error messages, CTAs, success screens, etc. - Designers or PMs often write placeholder text or inconsistent copy due to lack of writing support & time constraints. ## Solution A self-serve figma plugin where anyone can write first version of the copy that’s on-brand, on-tone, and compliant without needing support ## Approach - Align stakeholders on a unified brand voice - Setup brand voice guidlines (Tone) for cases like success, error, New features and so on. - Present guidelines that will be used as the first config for the figma app - Create the figma plugin with the help of Devs - Present a working model, to stakeholders - Take feedback and iterate if necessary - Replace copy throughout app using the figma plugin ## Brand Voice Based on the conversation with Lalit this is what volt stands for. based on these I want to define what the tone of language we want through out the app. - Call with Lalit on volt brand 1. If volt was a person how would you describe it? 1. Supportive 2. Reliable and Fast to help 3. Motivating 4. Enabler to achieve your financial needs 5. A saviour when you need most 2. Describe Volt in 3-4 words 1. Transparent, Trustworthy, Easy, Fast <aside> 💡 **Interacting with Volt should feel like:** Interacting with Volt should feel like interacting with a modern, banking savvy friend/ RM — someone who guides me towards my goals and makes everything feel simple, supportive, and effortless. - **Like a smart, supportive money guide** - **Your effortless, goal-driven money companion** </aside> Voice: **Smart, Supportive, Calm, and Clear.** <aside> 💡 Volt speaks like a modern financial guide — someone who knows money inside out, and explains it with warmth & clarity, not jargon. </aside> ## Scenarios / Possible Usecases - Error like PAN verification failed, No CKYC data found and so on - Success like Completion of Payment, Loan application, Increase limit and so on - Onboarding like App screenshots

---

## #107 — Enhance limit Research
**Status:** Unknown | **Last edited:** Unknown

# Enhance limit Research ### Objective 1. **User Motivation:** Why do people enhance their limit? 2. **Mental Models** How do they currently think about credit lines? - Currently our users think about credit line like a personal loan, They only choose increase their credit limit if they are in need. - What we can work towards is building the mindset like a credit card where increased credit limit is something people go for even when they don’t feel the need for it. - Folks tried to 3. **Context of Use** When do they increase limit? - After a withdrawal (they see low balance) - Utilisation > 70% - If they see the value of their MF has increased. . . 4. **Flow Drop Offs** Why do users abandon this? - Users who dropped out usually didn’t get the limit they wanted - They also were ineligible for the loan since there is a 10K limit Unclear next steps. Lack of feedback Screen fatigue 5. **Purpose & Value** Why does this feature matter to users? > It’s a fast, low-effort way to access more cash without applying for a new loan. KYC, Mandate and Agreement not required (If new total limit is below SL) > --- ### Feedback from users - No one complained of any difficulty, lack of information for dropping off. - When asked “What’s one thing stopping you from increasing your limit right now?” - The answer always is they don’t have the need for it. - Minimum 10K being the reason for drop-off. --- ### Segments of Users and Questionnaire 1. **Repeat Users (Used Top-Up More Than Once- Ideal Users)** - Why did you “Enhance Limit”? - What made you come back and do it again? - How easy or difficult was it to find the increase limit option? - Was anything unclear or unexpected in your experience? - Hindi - Aapne pehli baar limit enhance kyun kiya tha? - Aapne phir se kyun kiya? - Pura process aapko kaisa laga — easy ya confusing? - Koi ek step jo aapko helpful ya clear laga? - Aapko paise milne mein kitna time laga tha? - Kya koi cheez aisi thi jo alag thi ya samajh nahi aayi? - Aapko is process pe trust kyun hua? - Aapne jo extra limit mili uska use kaha kiya? - Kya kuch aisa hai jo aur better banaya ja sakta hai?

---

## #108 — Product Note Post limit fetch optimisation
**Status:** Unknown | **Last edited:** Unknown

# Product Note : Post limit fetch optimisation # Objective - This is **post-credit limit fetch, pre-KYC**. - User already knows eligibility → now reviewing loan terms. - Goal: Maximise conversion from this page to KYC initiation. # Current journey ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image.png) # Funnel metrics ## Overall Funnel [Only Eligible Users] ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%201.png) ## First time success rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%202.png) ## Median time to convert of overall funnel ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%203.png) ## P75t and P90th conversion time ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%204.png) ## MF Fetch Anchor Page Analysis ## Median time to convert from step 1 to 2 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%205.png) ### No. of users who clicked on ‘Mutual Funds Fetched Card’ In LOS i.e new users ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%206.png) In LOS + LMS combined ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%207.png) ### No. of users to clicked on back button after being eligible ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%208.png) - ### No. of users to clicked on back from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%209.png) ### No. of users who clicked on refresh portfolio from ‘fetched mutual funds page’ ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2010.png) ### No. of users who refreshed portfolio from ‘fetched mutual funds page’ and moved ahead to set credit limit and loan offer ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2011.png) ### Refresh portfolio on MFC Anchor page ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2012.png) ## Set Credit Limit Page Analysis ## Median time to convert from step 2 to 3 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2013.png) ## No of users who clicked on edit limit pencil icon ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2014.png) ## Loan Offer Page Analysis ## Median time to convert from step 3 to 4 ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2015.png) ### Loan offer page CTA clicked ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2016.png) ### No. of users who clicked prepayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2017.png) ### No. of users who clicked withdrawal and repayment expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2018.png) ### No. of users who clicked charges expanded ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2019.png) ### No. of users who clicked info icon on loan tenure ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2020.png) ### No. of users who clicked info icon on interest rate ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2021.png) ### No. of users who clicked info icon on credit limit ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2022.png) ## WATI Chats queries [https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/board/det66jRkfaE4H0La4DLail/WATI-Chats-on-Loan-Offer-Drop-Offs?node-id=2-261&t=Q9fiB4fNTa7iy0Ql-11&embed-host=notion&footer=false&theme=system) --- # Insights **Step 1 → Step 2 (Eligibility → Credit Limit) is the biggest drop off point**. - Users get eligibility but hesitate at credit limit setup - Around 28% of the users who land on the anchor page go and click ‘fetched mutual funds’ button to view their mutual funds. - Image ![image.png](Product%20Note%20Post%20limit%20fetch%20optimisation/image%2023.png) - Rest refresh portfolio(~6-7%) and some hit back button. - While median conversion time of the entire funnel is ~1min, p75th and p90th conversion time is anywhere from 1hr to 14hrs **Possible reasons of the drop-offs**

---

## #109 — 📄 Loan Offer Funnel Optimisation Document
**Status:** Unknown | **Last edited:** Unknown

# 📄 Loan Offer Funnel Optimisation Document ## **Problem Statement** Users are dropping off heavily between **Eligibility → Credit Limit setup**, with first-time success at ~36% (vs ~50% overall conversion). Trust, comprehension, and late surfacing of loan details are the biggest blockers. ## **Problem Breakdown (L1 → L2 → L3)** ### **L1 Problem 1: Early Drop-Off at Credit Limit Setup** - **L2.1:** Incomplete visibility of portfolio value. - **L3:** Users don’t understand why “eligible limit” < “portfolio amount” (45% LTV logic hidden). - **L2.2:** Fetched MF page creates doubt. - **L3:** Users who click here convert 50% less. Refresh/back CTA adds friction. ### **L1 Problem 2: Lack of Clarity on Loan Structure** - **L2.1:** Flexi-repay not understood. - **L3:** Most users think in EMI terms; confusion elongates decision cycle. - **L2.2:** EMI/Charges/Rate appear late. - **L3:** Users rely on WATI/FAQs to understand basics → long-tail conversions (p75–p90 = hours). ### **L1 Problem 3: Low Trust & Confidence** - **L2.1:** Mutual fund safety doubts. - **L3:** “Will my MF be locked?”, “Will it stop growing?” - **L2.2:** Competitive comparison behaviour. - **L3:** Users revisit multiple times to benchmark vs other lenders. --- ## **Current Journey** 1. **Eligibility Check** → Shows eligible limit only. 2. **Anchor Page (Fetched MFs optional)** → Users click “Fetched Mutual Funds” or Refresh → major drop-offs. 3. **Set Credit Limit Page** → Users reduce eligible limit 75% of the time. 4. **Loan Offer Page** → EMI, fees, rate only revealed here. 5. **KYC** → Initiation post-offer. --- ## **Proposed Journey** 1. **Eligibility Check (improved)** → Show eligible limit + simple breakdown of how it’s calculated (45% LTV). 1. **Portfolio Transparency (optional disclosure)** → Clear net eligible vs non-eligible MFs with logos. 2. **Set Credit Limit Page** → Inline EMI calculator (slider updates EMI/fees instantly). 2. **Review details** → Focus on trust badges (RBI registered lender, secure pledge), repayment clarity, upfront EMI vs Flexi toggle. 3. **KYC** → Smooth handoff.

---

## #110 — Credit line Journey Metrics
**Status:** Unknown | **Last edited:** Unknown

# Credit line Journey Metrics We have an opportunity for us to improve how we manage and access our API data. Right now, we don’t have formal documentation for the APIs or tables capturing the data logs, which could make it difficult for us to track user behavior effectively or run data-driven experiments. **Here’s what I think we could achieve with a stronger data process:** 1. **Empowering Better Decision-Making:** • One of the first things I’ve noticed is that our ability to make timely, data-driven decisions is limited by how we handle our data. By formalizing the documentation of our APIs and creating a system of structured tables, we’ll be in a position to quickly identify user patterns, track conversion rates, and pinpoint where users drop off in the flow. • I believe this will help us move from reacting to issues to proactively improving the user experience based on solid data. 2. **Establishing a Data Lake for Efficient Access:** • By creating tables from our API logs and building a **data lake**, we can make our data more accessible across teams. This would make it easier to query information, run analysis, and track critical metrics like user progression through the funnel or the success rates of various stages (e.g., KYC, bank verification). • I think this would enable faster, more accurate insights and help us optimize the product iteratively, without relying on manual log pulls or guesswork. 3. **Laying the Foundation for Scalability:** • Right now, the absence of formal documentation and structured data is adding some inefficiency to how we operate. By documenting our APIs and creating these data structures, we’ll not only address immediate challenges but also lay a foundation that can scale with us as we grow. • This could also prevent future issues where manual data collection slows down our response times or limits our ability to act quickly on insights. 4. **Creating Transparency Across Teams:** • A clear, organized data process would give everyone—product, engineering, and other teams—better visibility into how our product is performing. With standardized documentation and data tables, we can create a culture where data is accessible, and decisions are made with transparency and accountability. **Suggestions for Next Steps:** • We could start by identifying key API logs that need to be structured into tables and documented. This would give us a good foundation for creating a **data lake** that we

---

## #111 — Flow charts
**Status:** Unknown | **Last edited:** Unknown

# Flow charts Certainly! Below is the visualization of the user journey map provided, represented in PlantUML diagrams. Due to the complexity and length of the entire journey, I've divided the visualization into sections corresponding to each main phase of the user journey. Each section includes the PlantUML code for the activity diagram, which you can use to generate the diagrams. --- ## **1. User Acquisition and Onboarding** ### **1.1. Launching the App and User Signup** ``` @startuml start partition "User (FE)" { :Launch App; :View Signup Page; if (Click T&C or Privacy Policy?) then (Yes) :Click T&C or Privacy Policy; :View T&C or Privacy Policy; endif :Edit Phone Number; :Navigate to OTP Page; } partition "Backend (BE)" { :Trigger OTP; } partition "User (FE)" { repeat :Enter OTP; :Submit OTP; partition "Backend (BE)" { :Verify OTP; if (OTP Valid?) then (No) :OTP Invalid; endif } if (OTP Valid?) then (No) :Display Error Message; :Resend OTP?; if (Resend OTP?) then (Yes) partition "Backend (BE)" { :Trigger OTP; } endif endif repeat while (OTP Invalid) :Complete Signup; :View Verify Email Page; if (Verify Email with Google?) then (Yes) :Verify Email with Google; else :Verify Email with Other Method; :View Enter Email Page; :Enter Email Address; endif :Email Verification Result; } partition "Backend (BE)" { :Create User Context; :Update User Email; } stop @enduml ``` --- ## **2. Eligibility and Limit Check** ### **2.1. PAN Verification and Eligibility Check** ``` @startuml start partition "User (FE)" { :Enter PAN; :Verify PAN; :PAN Verification Result; if (PAN Verification Successful?) then (Yes) :Confirm PAN Details; else :Edit PAN Details; :Resubmit PAN; endif } partition "Backend (BE)" { :Initiate PAN Verification; :Complete PAN Verification; if (PAN Verification Failed?) then (Yes) :PAN Verification Failed; endif } partition "User (FE)" { :Trigger Eligibility Check; :Eligibility Check Result; if (Eligible?) then (Yes) :Proceed to Next Step; else :Application Under Review or Rejected; stop endif } partition "Backend (BE)" { :Create Credit Application; :Receive Credit Approval Request; :LAN Generation Successful?; if (LAN Generation Failed?) then (Yes) :LAN Generation Failed; stop endif } stop @enduml ``` --- ## **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** ``` @startuml start partition "User (FE)" { :View Check Limit Page; :Edit Details if Necessary; :Update Portfolio Source; :Request MF Portfolio Details; :Choose CAMS or KFIN?; } partition "User (FE)" #LightBlue { if (CAMS Selected?) then (Yes) :Request OTP for CAMS MF Fetch;

---

## #112 — Journey Table
**Status:** Unknown | **Last edited:** Unknown

# Journey Table 1. **Phase** 2. **Sub-Phase** 3. **Action ID** 4. **User Action** 5. **Description** 6. **Platform** --- ## **1. User Acquisition and Onboarding** | Phase | Sub-Phase | Action ID | User Action | Description | Platform | | --- | --- | --- | --- | --- | --- | | User Acquisition and Onboarding | Launching the App | 1.1.1 | Launch the App | Open the Volt platform by tapping the app icon from the splash screen. | Mobile App / Web | | User Acquisition and Onboarding | User Signup | 1.2.1 | View Signup Page | Access the signup interface to create a new account. | | | User Acquisition and Onboarding | User Signup | 1.2.2 | Click T&C or Privacy Policy | Review the Terms & Conditions or Privacy Policy documents. | | | User Acquisition and Onboarding | User Signup | 1.2.3 | Edit Phone Number | Modify the phone number entered during signup. | | | User Acquisition and Onboarding | User Signup | 1.2.4 | Navigate to OTP Page | Proceed to the OTP (One-Time Password) verification step. | | | User Acquisition and Onboarding | User Signup | 1.2.5 | Resend OTP | Request a new OTP if the initial one was not received or expired. | | | User Acquisition and Onboarding | User Signup | 1.2.6 | Enter Invalid OTP | Attempt to enter an incorrect OTP for testing purposes. | | | User Acquisition and Onboarding | User Signup | 1.2.7 | Complete Signup | Finalize the signup process after successful OTP verification. | | | User Acquisition and Onboarding | User Signup | 1.2.8 | View Verify Email Page | Access the email verification interface. | | | User Acquisition and Onboarding | User Signup | 1.2.9 | Verify Email with Google | Use Google authentication to verify the email address. | | | User Acquisition and Onboarding | User Signup | 1.2.10 | Verify Email with Other Method | Utilize alternative methods for email verification. | | | User Acquisition and Onboarding | User Signup | 1.2.11 | View Enter Email Page | Input the email address for account verification. | | | User Acquisition and Onboarding | User Signup | 1.2.12 | Email Verification Result | View the outcome of the email verification process. | | --- ## **2. Eligibility and Limit

---

## #113 — API grouping
**Status:** Unknown | **Last edited:** Unknown

# API grouping Sure! Below is a comprehensive list of all the APIs you've provided, organized into logical steps involved in the credit application process. I've included their descriptions and organized them into a table format that can be easily transferred to an Excel sheet. The total count of APIs is **112**. ### Step 1: Application Retrieval and Management | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 1 | `/app/borrower/application/{applicationId}` | GET | Retrieves application data using the application ID. | | 1 | `/app/borrower/application/change/state/progress/{applicationId}/{currentStepId}` | GET | Updates the step state to 'in progress' for the given application. | | 1 | `/app/borrower/application/override` | POST | Overrides application rules for exceptional cases. | | 1 | `/app/borrower/application/stepper` | POST | Retrieves stepper data for the given application. | ### Step 2: KYC Additional Details | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 2 | `/app/borrower/application/additionalDetails/{applicationId}` | GET | Retrieves the list of additional KYC details present in the system. | | 2 | `/app/borrower/application/additionalDetails/{applicationId}` | POST | Adds additional KYC details to the application. | ### Step 3: Agreement Processing | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 3 | `/app/borrower/application/agreement/link/{applicationId}` | GET | Retrieves the e-agreement setup link. | | 3 | `/app/borrower/application/agreement/status/{applicationId}` | GET | Retrieves the agreement acceptance status. | | 3 | `/app/borrower/application/agreement/stepper/{applicationId}` | GET | Retrieves agreement stepper information. | | 3 | `/app/borrower/application/doc/digio/init/{applicationId}` | GET | Initiates a Digio e-sign request for the agreement. | | 3 | `/app/borrower/application/doc/digio/status/{applicationId}` | GET | Checks the status of the Digio e-sign request. | | 3 | `/app/borrower/application/doc/digio/status/deep/{applicationId}` | GET | Performs a deep status check of the Digio e-sign request. | | 3 | `/app/borrower/application/signdesk/esign/init/{applicationId}` | GET | Initiates e-sign via SignDesk. | | 3 | `/app/borrower/application/signdesk/esign/status/deep/{applicationId}` | GET | Checks SignDesk e-sign status in depth. | | 3 | `/app/borrower/application/signdesk/esign/validate` | POST | Validates the SignDesk token. | ### Step 4: Loan Approval and Eligibility | Step | API Endpoint | Method | Description | | --- | --- | --- | --- | | 4 | `/app/borrower/application/approval/check/{applicationId}` | GET | Retrieves loan approval status. | | 4 | `/app/borrower/application/check/shallow/creditApproval/{applicationId}` | GET | Checks credit approval status for

---

## #114 — APIs
**Status:** ** Retrieves the status of the KYC verification. | **Last edited:** Unknown

# APIs **Explanation of the API Sequence in the Volt Money Application Flow** Welcome aboard! As the head developer for the Volt Money product, I'd like to walk you through the sequence of APIs that power our application flow. This explanation will help you understand how each step functions, the APIs involved, and how they contribute to the overall user experience. --- ### **Overview** The Volt Money application process involves several key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** Each of these steps is supported by specific APIs and may involve external partners. I'll explain each step in detail. --- ### **1. Login** - **API Used:** *Custom Authentication API (Not listed in the provided APIs)* - **Functionality:** - **User Authentication:** The user logs in using their mobile number and an OTP (One-Time Password) sent to their phone. - **Notes:** - This step establishes a secure session for the user. - While not specified in the provided API list, we use a standard authentication service to handle this process. --- ### **2. PAN Verification** - **API Used:** - `POST /app/borrower/application/kyc/pan/panVerify` - **Partner:** Decentro (facilitates connection to NSDL) - **Functionality:** - **PAN Validation:** Verifies the user's PAN number with NSDL to ensure it is valid. - **Data Retrieval:** Fetches the full name associated with the PAN. - **Notes:** - Essential for KYC compliance and identity verification. - Helps prevent fraudulent applications. --- ### **3. Fetch Folio** - **APIs Used:** - `POST /app/borrower/application/fetch/init/otp/v3` - `POST /app/borrower/application/fetch/authCAS/v2` - **Partners:** Cams, KFintech, MF Central - **Functionality:** - **Initiate Fetch:** Sends an OTP to the user to authenticate the retrieval of their mutual fund folio. - **Authenticate and Retrieve:** Verifies the OTP and fetches the folio details. - **Notes:** - The folio contains information like ISIN and NAV, which are crucial for assessing the user's assets. - This data is used later in the asset pledge and eligibility assessment. --- ### **4. Eligibility Assessment and Lender Assignment** - **API Used:** - `POST /app/borrower/application/credit/profile/evaluate` - **Partner:** Internal Business Rule Engine (BRE) - **Functionality:** - **Eligibility Calculation:** Uses BRE to compute the eligible loan limit based on the user's assets and lender criteria. - **Lender Assignment:** Assigns the user to a lender (either Bajaj Finance or TATA Capital) based

---

## #115 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #116 — flows api
**Status:** Unknown | **Last edited:** Unknown

# flows api 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** 1. **Fetch Folio-** 2. **Eligibility Assessment and Lender Assignment** 3. **KYC Verification** 4. **Bank Account Verification** 5. **Mandate Setting** 6. **Asset Pledge** 7. **KFS and Documentation** 8. **Loan Agreement Execution**

---

## #117 — LaMF application journey
**Status:** Unknown | **Last edited:** Unknown

# LaMF application journey [APIs](LaMF%20application%20journey/APIs%2010ae8d3af13a80ca9cb6eb9f1a098ddf.md) [API grouping ](LaMF%20application%20journey/API%20grouping%2010ae8d3af13a8076bcdce2f44a6ea73f.md) [flows api ](LaMF%20application%20journey/flows%20api%2010de8d3af13a80b8ad4dce117eda38b2.md) [Pledge Error PRD](LaMF%20application%20journey/Pledge%20Error%20PRD%2010de8d3af13a8002a237cae253c5b23e.md) The journey to create a loan against mf is as follows - login - user logs in using mobile number and otp validation - PAN verification - user enter DOB and PAN to validate pan , API - decentro - Fetch folio - we ping Cams/KFin to get the folio for the user - We ping them manually - we have option of gettign both from MF central - One the folio is fetched we run BRE to calcualte eligible LImits as per lender prescribed calculation and appored lists - Folio have ISIN , NAV etc details - We assign the customer basis BRE to either Bajaj ot TATA capital - KYC of the customer aadhar - API is diifetent for tata and bajaj - Bank account verification - Mandate setting - Logement - KFS and docuemnttation Support I have created and displayed the table documenting the journey steps, partners, and API names in Google Sheets format. Let me know if you'd like to modify or download the table. [Journey_Steps_with_Partner_and_API_Info.csv](LaMF%20application%20journey/Journey_Steps_with_Partner_and_API_Info.csv) | Step | improvements | Description | Partner/Service | API Name | | | --- | --- | --- | --- | --- | --- | | Login | | User logs in using mobile number and OTP validation | | [https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true](https://api.staging.voltmoney.in/api/client/auth/requestOtp/v2/+919892732644?enableWhatsapp=true) | | | Verify OTP | | | | https://api.staging.voltmoney.in/api/client/auth/verifyOtp/ | | | user details | | | | https://api.staging.voltmoney.in/app/borrower/user | | | Email verification | | | Google sso | https://accounts.google.com/o/oauth2/iframerpc?action=checkOrigin&origin=https%3A%2F%2Ftest.staging.voltmoney.in&client_id=62646021413-queb1g13go0snvnotl0ee06t68jcgb98.apps.googleusercontent.com | | | | | | Email / manual | | | | | | | | [https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913](https://api.staging.voltmoney.in/app/borrower/accountAttributes/3a11389a-c67f-4e79-b4ab-fce1d385e913) | | | | | | | | | | PAN Verification | | User enters DOB and PAN to validate PAN | Decentro | Decentro PAN API | | | Fetch Folio | | Ping CAMS/KFin to get the folio for the user | CAMS/KFin, MF Central (optionally) | CAMS/KFin API, MF Central API | | | Run BRE and Calculate Eligible Limits | | Run BRE to calculate eligible limits as per lender prescribed calculations | Internal BRE system | | | | Assign Lender | | Assign customer to either Bajaj or TATA Capital based on BRE | Internal BRE system | | | | KYC Verification | | KYC of the customer with different APIs for Bajaj and TATA Capital

---

## #118 — Selfie capture journey
**Status:** Unknown | **Last edited:** Unknown

# Selfie capture journey In the Tata journey, we have a step to capture a selfie, but this is not included in the Bajaj journey. While the selfie feature is part of the Bajaj Figma design, it is neither implemented in production nor required. **User Flow for Selfie Capture (Bajaj Journey):** 1. The user sees a "Click Selfie" button, which activates the front camera after obtaining permission. 2. If an MFD creates the application, they can share a link with the customer. 3. The customer flow is as follows: - MFD shares the link with the customer. - Customer receives the link and opens it. - Customer logs in by verifying their phone number and entering the OTP. - The customer continues the application, completes KYC, and provides camera permissions. - Customer clicks the "Click Selfie" button, captures, and uploads the selfie. - Once the selfie is verified, the customer proceeds to the next steps.

---

## #119 — flow
**Status:** Unknown | **Last edited:** Unknown

# flow **User Journey Map for a Loan Against Mutual Funds Application** This user journey map outlines the steps a user goes through when applying for a loan against mutual funds (MF) using our platform. The journey is segmented into logical phases, incorporating both front-end (FE) interactions and back-end (BE) events. The map also considers different sourcing channels: B2C (Business-to-Consumer), B2B (Business-to-Business), and B2B2C (Business-to-Business-to-Consumer). --- ### **1. User Acquisition and Onboarding** ### **1.1. Launching the App** - **FE Snippet:** - *Splash Screen > Launch App* ### **1.2. User Signup** - **FE Snippets:** - *Signup > View Signup Page* - *Signup > Click T&C or Privacy Policy* - *Signup > Edit Phone Number* - *Signup > Navigate to OTP Page* - *Signup > Resend OTP* - *Signup > Enter Invalid OTP* - *Signup > Complete Signup* - *Signup > View Verify Email Page* - *Signup > Verify Email with Google* - *Signup > Verify Email with Other Method* - *Signup > View Enter Email Page* - *Signup > Email Verification Result* - **BE Events:** - *Backend Events > OTP > Trigger OTP* - *Backend Events > OTP > Verify OTP* - *Backend Events > User Management > Create user context* - *Backend Events > User Management > Update user email* --- ### **2. Eligibility and Limit Check** ### **2.1. PAN Verification** - **FE Snippets:** - *Cash Limit > Enter PAN* - *Cash Limit > Verify PAN* - *Cash Limit > PAN Verification* - *Cash Limit > Edit PAN Details* - *Cash Limit > Confirm PAN Details* - **BE Events:** - *PAN Verification > Initiate PAN verification* - *PAN Verification > Complete PAN verification* - *PAN Verification > PAN verification failed* ### **2.2. Eligibility Check** - **FE Snippets:** - *Cash Limit > Trigger Eligibility Check* - *Cash Limit > Eligibility Check Result* - *Cash Limit > Application Under Review* - *Cash Limit > Application Rejected* - **BE Events:** - *Credit Application > Create credit application* - *Credit Approval Request > Receive credit approval request* - *Credit Approval Request > FAS creates the request* - *Credit Approval Request > LAN generation successful* - *Credit Approval Request > LAN generation failed* --- ### **3. Mutual Fund Portfolio Integration** ### **3.1. Linking MF Portfolio** - **FE Snippets:** - *Cash Limit > View Check Limit Page* - *Cash Limit > Edit Details on Check Limit Sheet* - *Cash Limit > Update Portfolio Source* - *Cash

---

## #120 — Investwell
**Status:** Unknown | **Last edited:** Unknown

# Investwell | | | **Registered** | | | **Pre Fetch** | | | | | | | | | | | | | | **Post fetch** | | | | | | | | | | | | | | | | | | | | | | | | | | | | **Post pledge** | | | | | | | | | | | | | | | | **Completed** | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | **Month** | **Week No** | **Registered Leads** | **mfc_journey** | **app_only_journey** | **Initial Step** | **KYC_PAN_VERIFICATION** | **CHECK_CUSTOMER_ELIGIBILITY** | **MF_FETCH_PORTFOLIO** | **Pass through (from registered)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **MF_PLEDGE_PORTFOLIO** | **OFFER_SELECTION** | **KYC_DOCUMENT_UPLOAD_POI** | **KYC_DOCUMENT_UPLOAD_POA** | **KYC_DOCUMENTS** | **KYC_ADDITIONAL_DETAILS** | **KYC_SUMMARY** | **KYC_PHOTO_VERIFICATION** | **CIBIL_CHECK** | **CO_BORROWER_PAN_DETAILS** | **CO_BORROWER_KYC_DOCUMENTS** | **CO_BORROWER_KYC_SUMMARY** | **CO_BORROWER_ADDITIONAL_DETAILS** | **BANK_ACCOUNT_VERIFICATION** | **DIGIO_MANDATE_SIGN** | **TATA_MANDATE** | **ASSET_PLEDGE** | **Pass through (from post fetch)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Step** | **CREDIT_APPROVAL** | **SIGN_DESK_ESIGN** | **REVIEW_KFS** | **AGREEMENT_SIGN** | **MANDATE_SETUP** | **Pass through (from post pledge)** | **0 and error** | **0-25k** | **25k-50k** | **50k-1L** | **1L-2L** | **2L-5L** | **5L-10L** | **10L-20L** | **>20L** | **Completed Step** | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |

---

## #121 — Visibility
**Status:** Unknown | **Last edited:** Unknown

# Visibility # Application funnel - The Steps - Main funnel ### Loan closed [Closed Loan](Visibility/Closed%20Loan%20159e8d3af13a80c7be2cd6a9a51e4a7e.md) - Loan enhancement - Loan Renewal - Loan disbursed - Repayments - Documents - Service requests - Foreclosure - Shortfall - Loan agreement signing - Loan KFS - Asset Pledge - Bank Mandate - Bank account verification - KYC verification - Offer presentation - Eligibility check - Lead registration - Visitor # The APIs - The APIs involved in each step - Their Metrics - Error code count - Availability - The error codes - Count - Handling - In screen - Messages # The Screens - User flows - Screen events # The calls - Inbound call volume @Tushar Luthra can you add the Doc - Inbound call assignment - Current assignment - Exotell - Auto dialer [Inbound call assignment ](Visibility/Inbound%20call%20assignment%20159e8d3af13a8078962bdbd5d45ac1ee.md) - Inbound call disposition - Qualitative - Quantitative - Source - History # The messages - Message volume - Message assignment - First response time - First resolution time - Associated tickets # The bugs - SDK bugs - API bugs - Partner bugs - Iframe bugs - Investwell partner dashboard bugs [Investwell](Visibility/Investwell%2015ae8d3af13a80bbba17f8cce2113bac.md) - Reported bugs - Bugs RCA - Bug resolution # The Tickets - Ticket volume - Ticket categorisation - Ticket SLAs - Ticket assignment - Ops - Tech - Escalations # The users - Lead details - Payment details - Documents - Referred details - Payout details - Support history - Engagement level # The Numbers - AUM - Unutilised limit - Disbusement # THE CRM

---

## #122 — LSQ Leedsquared
**Status:** Unknown | **Last edited:** Unknown

# LSQ: Leedsquared @Naman Agarwal ### **Overview** LeadSquared (LSQ) is a comprehensive Customer Relationship Management (CRM) tool primarily used by Volt Money to manage lead generation, customer interactions, and the loan application process. LSQ enables sales teams and Relationship Managers (RMs) to track customer journeys, from lead acquisition to loan approval, providing a centralized view of lead data, customer details, and application stages. --- ### **Framework: Business Impact of LSQ** ### 1. **Purpose/Objective** LSQ’s core objective is to **streamline lead management** and **enhance customer support** by providing sales teams with real-time access to lead information and loan application statuses. By organizing customer interactions and loan data in one place, LSQ improves the efficiency and transparency of the sales process, enabling better decision-making and quicker responses to customer needs. ### 2. **Key Features & Functions** | **Feature** | **Description** | | --- | --- | | **Lead Management** | LSQ tracks customer leads from acquisition to conversion, providing visibility into lead status, ownership, and data. | | **Loan Application Tracking** | Displays the current stage of loan applications (e.g., CIBIL check, KYC, approval), helping RMs manage their pipeline. | | **Customer Data Storage** | Stores critical customer details such as name, email, phone number, and loan amounts, enabling personalized outreach. | | **Sales Performance Insights** | Generates reports on lead outreach, conversion, and sales performance, helping teams optimize their strategies. | ### 3. **Business Benefits** - **Improved Lead Conversion**: LSQ helps RMs track the progress of leads efficiently, ensuring no customer falls through the cracks and allowing for timely follow-ups. - **Increased Transparency**: By providing a clear view of each lead’s stage in the loan application process, LSQ reduces ambiguity and improves decision-making. - **Enhanced Customer Support**: Real-time access to customer details and loan data allows RMs to provide more informed and tailored support during customer interactions. ### 4. **Challenges/Current Gaps** - **Lead Stage Sync Issues**: Discrepancies between the stages in LSQ and Volt Money's backend systems can lead to confusion and mismanagement of leads. - **Missing Loan Details**: Critical loan information like Processing Fees (PF), Rate of Interest (ROI), and Sanction Limits are not always available in LSQ, affecting RMs' ability to assist customers. - **Manual Data Updates**: Admin actions (e.g., changes to customer data) are not automatically reflected in LSQ, which can lead to outdated records and inefficiencies. ### 5. **Opportunities for Improvement** - Lead prioritisation - **Automating Data

---

## #123 — LaMF funnel
**Status:** Unknown | **Last edited:** Unknown

# LaMF funnel To document a funnel from a product manager's perspective, especially for opening a credit line with multiple third-party APIs involved, you can follow these steps: ### 1. **Define the Funnel Stages** - **Map the key stages** of the funnel from a user’s perspective. Each stage should represent a meaningful user action: 1. ### 2. **Identify Touchpoints & Third-Party API Dependencies** - **For each stage**, document which third-party API is involved and what data is exchanged. - **E.g.,** ### 3. **Track Conversion & Drop-off Metrics** - At each stage, define **conversion rate** (users who successfully pass to the next stage). - **Identify drop-offs**: Calculate how many users fail or exit the flow at each stage and investigate why. - **E.g., Eligibility Check** → 75% conversion, 25% drop-off due to API failure or ineligible users. ### 4. **Diagnose Breakpoints & Flow Bottlenecks** - **API Response Failures**: Track the rate of success and failure for API calls (e.g., timeout, invalid responses, high failure rate in the KYC stage). - **User Frustration Points**: Analyze user sessions to find out if there are UI/UX challenges (e.g., users leave due to complex form submissions or unclear messaging). - **Incomplete User Inputs**: Check if the flow is breaking due to missing or invalid user input (e.g., incorrect document uploads or failed validation). ### 5. **Attribution of Drop-offs** - **Tag each drop-off** with an attribution reason: 1. **Technical** (API failure, timeout, or 500 error). 2. **User Behavior** (abandonment, confusion with next steps). 3. **Eligibility** (e.g., failed credit check or ineligibility). ### 6. **Major Pain Points** - **Highlight user pain points** by reviewing feedback, support tickets, and analytics. - **E.g., KYC Step**: Users frequently abandon due to the complexity of document uploads. - Use qualitative feedback (e.g., user interviews, support chats) alongside quantitative data (e.g., Google Analytics, session recordings). ### 7. **Set Up Conversion Tracking** - Use **attribution tools** to track how users are progressing through the funnel, and set up **event tracking** in Google Analytics or similar. - **For each stage**, track key metrics like: 1. Average time spent. 2. Bounce rates. 3. API success/failure rates. ### 8. **Monitor Real-Time Data** - Implement **dashboards** that allow you to monitor API response times, error rates, and user journeys in real-time. - Example tools: **DataDog** for API monitoring, **Hotjar** for session recording, **Google Analytics** for user tracking. ### Example Documentation Flow: ``` 1. Stage 1: User Signup

---

## #124 — Sales team is calling customers who complete the j
**Status:** Unknown | **Last edited:** Unknown

# Sales team is calling customers who complete the journey on their own To maximize the efficiency of our sales team and ensure that our limited resources are used effectively, we aim to distinguish between customers who genuinely need assistance and those who can self-serve. By enabling our sales team to focus on "struck" customers—those facing difficulties in the application or onboarding process—we can optimize our support efforts, increase customer satisfaction, and drive higher conversion rates. ## Strategy: We are building a **customer classifier** that will automatically detect whether a customer is "stuck" in the journey or can self-serve. This will allow our CRM to prioritize customers based on their likelihood to convert or their need for human assistance. By focusing on high-priority leads, we can drive better performance with the same resources. ### Key Steps: 1. **Develop a Classifier**: - Build a mechanism that identifies "struck" customers based on their interaction with the platform. This classifier will be able to distinguish between users who are struggling and those who can proceed independently. 2. **Highlight in CRM**: - Integrate the classifier with our CRM system to ensure that sales representatives are notified in real-time when a customer is identified as "stuck." The CRM should highlight these customers, offering the sales team clear, actionable insights. 3. **Update Sales Incentives**: - Modify the incentive structure for sales executives to align with the new system, rewarding them for focusing on and resolving cases where their intervention is truly needed. ## Identifying "Struck" Applicants: To accurately identify struck customers, we will deploy the following tactics: - **Telemetry on Errors**: - Implement error tracking throughout the customer journey. If a customer encounters a technical problem (e.g., form submission fails, API error), they will be flagged as "struck." - **Abandoned Journey**: - Monitor customer activity in real-time. If a user abandons a critical stage of the application process (e.g., KYC, loan application) for more than 30 minutes, they will be marked as "stuck." - **Custom Rules**: - We will determine additional logic based on further data analysis and customer feedback to enhance the classifier. ### Classifier Logic: The classifier's logic will be based on a combination of: - **User behavior telemetry** (e.g., error reports, time spent on a task). - **Abandonment tracking** (e.g., inactivity beyond a defined threshold). - **Data-driven insights** (e.g., patterns in customers’ prior journeys that lead to successful or failed conversions). ### CRM

---

## #125 — API flow for KFS and Agreement
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

## #126 — Additional details enhancement
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

## #127 — DSP Consent Architecture (Oct25)
**Status:** In progress | **Last edited:** Unknown

**Problem:**
are we solving?**

DSP currently captures consents as 2-3 line items. This is mostly restricted to email and mobile verification. None of the other consents in the journey are recorded in our DB from an audit trail perspective.

As per DPDP act, REs need to capture consent for data that’s absolutely required and more importantly store and mange it in a structured manner. This would require DSP to revoke consents if not applicable or not required as per policy. This would require DSP to maintain a strong audit trail for each consent in the journey.

---

**Solution:**
?**

---

## #128 — IFSC addition Account opening enhancement
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

## #129 — Pincode addition Account opening enhancement
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

## #130 — Product Note LAS Customer Consent Capture
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

## #131 — [Platform] Decoupling of dishonour fees with manda
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

## #132 — tech issues
**Status:** Unknown | **Last edited:** Unknown

# tech issues ## ### KYC & Authentication Issues 1. **KYC verification process fails with no clear error messaging** - Example (VTS-9511): "AKGPV3060R - Not able to move forward in kyc step" - Customer was stuck during verification with no indication of what went wrong or how to proceed. - Example (VTS-9981): "Stuck in kyc summary" - Process halted after completing verification with no error details provided to the customer. 2. **Digilocker integration failures during KYC verification** - Example (VTS-9770): "9415307644 - VIKAS KUMAR - KYC issue with digilocker's end" - API connection to Digilocker failing, preventing document verification. - Example (VTS-9964): "Discrepancies in CKYC record associated with the KYC Identifier: 50072772797161" - Records in Digilocker not matching with application data. 3. **Unusual KYC errors without diagnostic information** - Example (VTS-9711): "Unusual KYC Error" - Generic error message without actionable details for troubleshooting. - Example (VTS-10138): "CFCPS2351M - Facing error on KYC Page" - Customer encountered undefined error with no clear next steps. ### Pledging Process Failures 1. **KFin OTP delivery system failures** - Example (VTS-10085): "8928846293 - ATUL TIWARI - not getting otp at pledging for kfintech" - Customer attempted multiple times from web and app but never received OTP. - Example (VTS-10227): "8884052766 - DINESH KUMAR INALA - Kfintech pledging OTP issue" - System-wide failure in OTP delivery when pledging through KFin. 2. **Pledging failure despite eligibility** - Example (VTS-9396): "EQSPK8350P - KFin Pledging error" - "Fund is in approved list of TATA and is also visible when we did 15sec eligibility check" but still failing. - Example (VTS-9358): "DIWPP4809P - Unable to pledge Kfin funds" - Eligible funds appearing in portfolio but pledge transaction failing. 3. **Funds pledged but not lodged in system** - Example (VTS-9884): "Lodgment issue -ANNPS4596F" - "One of the pledged funds of the above client is not lodged in the system yet". - Example (VTS-10044): "BEPPB3956Q, Units pledged but lodgment not done" - Pledge transaction completed but credit not applied to account. ### API Integration Failures 1. **Timeouts in partner integrations** - Example (VTS-9597): "Frequent API Timeout Issues" - FundsIndia experiencing frequent API timeouts, preventing operations completion. - Example (VTS-9529): "Assistance Required: User Facing PAN Mobile Number Error in SDK" - API timeout causing user verification failures. 2. **Document API failures** - Example (VTS-9346): "Volt - Documents are Missing" - "I checked the webtops and I am unbale to find. Requesting you to

---

## #133 — API details
**Status:** Unknown | **Last edited:** Unknown

# API details This API documentation outlines various attributes in both the **Request Header** and **Request Body** sections. Below, I will explain each attribute in both sections for a better understanding. ### Request Header Attributes 1. **Ocp-Apim-Subscription-Key** (String, Mandatory): - A unique subscription key required for accessing the API. This is a static key that needs to be obtained from the APIM Gateway authority. 2. **MOAuthorization** (String, Mandatory): - A dynamic authorization token (Mauth Token) that must be obtained and passed. This is managed by the respective authority and is not required if the request is initiated from an SFDC channel. 3. **Content-Type** (String, Mandatory): - Default value is `"application/json"`. It specifies the format of the data being sent. 4. **Authorization** (String, Mandatory): - An authorization token, typically OAuth2, used for accessing the API securely. ### Request Body Attributes 1. **XML_PACKET** (String, Optional): - Specifies whether CKYC XML Data will be included in the response. Default value is 'Y'. Possible values: - `'Y'`: XML Data will be included. - `'N'`: Only extracted fields will be returned. 2. **BITLY** (String, Optional): - Indicates whether a URL will be sent in the response or through SMS. Default value is 'N'. Possible values: - `'N'`: URL will be included in the response. - `'Y'`: URL will be sent via SMS. 3. **SOURCE_REQUEST_TIME** (String, Mandatory): - The timestamp of the request in the format `YYYY-MM-DD HH:MM:SS`. 4. **PROCESS_MODE** (String, Mandatory): - Indicates the mode of the process. Possible values: - `'UI'`: For user interface modes such as CKYC, OKYC. - `'API'`: Applicable when KYC Mode is CKYC. 5. **SOURCE_REQUEST_ID** (String, Mandatory): - A unique ID to identify the source channel request. 6. **APPLICATION_ID** (String, Optional): - A unique Application ID of the sourcing channel. 7. **CHANNEL_KEY** (String, Mandatory): - A static key that identifies the sourcing channel, obtained during the initial setup. 8. **CUSTOMER_ID** (String, Optional): - The customer identifier. 9. **POI_TYPE** (String, Optional): - Proof of Identity Type. Possible values include PAN, PASSPORT, UID, etc. 10. **POI_NO** (String, Optional): - The corresponding number for the specified POI type. 11. **DOB** (String, Mandatory): - Customer's Date of Birth in the format `YYYY-MM-DD`. 12. **CUSTOMER_TYPE** (String, Optional): - Customer type for reporting purposes. Possible values: New, Existing. 13. **FORCE_REFRESH_FLAG** (String, Optional): - Indicates whether to bypass the KYC search for an existing customer. Possible values: 'Y', 'N'. 14. **GENDER** (String, Optional): - Customer gender. Mandatory

---

## #134 — PRD - presentation
**Status:** Unknown | **Last edited:** Unknown

# PRD - presentation @Naman Agarwal # **Executive Summary** Volt Money aims to integrate the RBI mandated V-KYC into our loan disbursement process with Bajaj. The challenge is to comply with regulatory requirements without compromising the customer experience or increasing drop-off rates. This document outlines a strategic plan to implement V-KYC seamlessly, ensuring regulatory compliance, enhancing customer satisfaction, and maintaining a competitive edge. --- ![Loan agaisnt MF journey (1).png](Loan_agaisnt_MF_journey__(1).png) # 1. **Objective** - Our primary goals are to ensure full compliance with RBI's VCIP guidelines and Bajaj's KYC protocols, enhance user experience by minimising friction in the KYC process, streamline backend operations, and provide flexibility for users to complete V-KYC within a 72-hour window after completing DigiLocker KYC. --- # **2. Success Metrics** Our primary goal is to integrate V-KYC while maintaining an exceptional customer experience. Success will be measured using the following Key Performance Indicators (KPIs): | Metric | Target | Measurement Method | Current Baseline | Priority | | --- | --- | --- | --- | --- | | **Regulatory Compliance** | 100% compliance with RBI V-KYC guidelines | Audit reports and compliance checklists | N/A | Critical | | **V-KYC Completion Rate** | >90% of initiated V-KYC processes | Analytics tracking completion events | N/A | High | | **Drop-Off Rate Post-Digilocker KYC** | <10% | Funnel analysis using analytics tools | N/A | High | | **Average Time to Complete KYC** | 5-7 minutes (digilocker) 3 min + (V-KYC) 5-7 min | Time-stamped process tracking | Current average: 3 minutes (without V-KYC) | Medium | | **Re-Engagement Success Rate** | >70% of drop-offs re-engaged | Monitoring re-engagement campaigns | N/A | High | | **72-Hour V-KYC Completion Rate** | 100% within 72 hours | Automated deadline tracking | N/A | High | | **Overall Funnel Completion Rate** | 95% of users who start KYC complete the loan process | End-to-end funnel analysis | ~ | High | --- # **3. Background / Context** - **Current Funnel**: 1. **Digilocker KYC**: Users complete KYC through Digilocker. 2. **Bank Account Verification**: The user's bank account is verified. 3. **Pledge**: The loan collateral is pledged. 4. **KFS + Agreement**: Key Fact Statement and agreement are shared and signed. 5. **Mandate**: A mandate is established for loan repayment. 6. **Disbursement**: Loan is disbursed to the user. - **New Flow**: 1. **Digilocker +Details + Video KYC**: Users complete Digilocker KYC +

---

## #135 — SDK
**Status:** Unknown | **Last edited:** Unknown

# SDK - JS sdk - IOS sdk - Android SDK - RN sdk - partner mobile APP, web , PLJ - Iframe - webhook for partner , v-kyc done or not to partners - API exposed, Get application status , KYC done , bifurcation -

---

## #136 — V-KYC Integration with Bajaj
**Status:** Unknown | **Last edited:** Unknown

# V-KYC Integration with Bajaj We are asked by Bajaj to include V-kyc to do full KYC according to compliance Scope | [S.No](http://s.no/) | Feature | Description | Why | Approach 1 / Tradeoff | Approach 2 | Approach 3 | | --- | --- | --- | --- | --- | --- | --- | | 1 | Add Agent Call | Full KYC (DIGI+VCIP) | RBI compliance and Bajaj requirement | Integrate Bajaj V-KYC – may lower conversion rates | Do not integrate V-KYC and send to Tata – lower flexibility | Get Bajaj to waive V-KYC for existing customers | | 2 | Digilocker KYC | Existing KYC | Required for KYC | Start V-KYC with Digilocker; if not completed, run it in parallel | Start V-KYC after Digilocker; user must complete V-KYC before Bank Account Verification (BAV) | Continue current funnel and start V-KYC at the end | | 3 | In-app Link | URL callback with KYC URL | For an in-app experience | Use current setup for in-app view – requires testing | Send SMS from Bajaj with URL, schedule, and notification | | | 4 | Present Address Check | Bajaj will disable this from the frontend | To verify registered and present addresses | Bypass and mark address as the same, as the check is within India | Ask user to select Yes/No; if No, ask for proof of present address | | | 5 | URL Timeout | 1 hour from API call | N/A | Have a screen where the user triggers the API just before starting the call | | | | 6 | Update Transaction ID | Required once V-KYC is complete | Needed in the agreement | Send the Transaction ID via the new API developed by the SFDC team | | | | 7 | Existing Customer Handling | N/A | Existing customers do not require V-KYC | No V-KYC needed; we will get an "existing customer" flag in the response | | | | 8 | Where to Add Agent Call | N/A | Integrate agent call into the flow | - Provide an option in the KYC step to continue with V-KYC. - If the user chooses "Do V-KYC later" or skips, start at the end. - Pros: Lets users know V-KYC is required early and keeps flexibility. - Cons: May increase drop-off and

---

## #137 — VCIP GTM Plan
**Status:** Unknown | **Last edited:** Unknown

# VCIP GTM Plan - First to decide default : - what will happen if we don’t develop ? - to Schedule call with bajaj - They will start on 15th Nov - they have asked us for the Timelines - IF we Decide to not build then what should happen - We should move out of Bajaj - We should move to Tata or DSP - Tata is p3 as the lien charges are high - DSP will take 1-2 months to be operational - If we decide to build then what the flow should be ? - VCIP stop:- We can Block all the steps till V-kyc is Done - Safer and operationally less challenging, but higher dropoffs - VCIP end:- We can allow all the steps and V-kyc can be done last - Easier and recommended by Bajaj, But more customer complains and Higher operations cost - To integrate the VCIP we need to make additions to the UI screens in Bajaj flow - Figma? - API integration, testing , and response handling. - Permissions handling - Platform changes | Platform | Changes | | | --- | --- | --- | | Web | New UI screens, chrome permissions, | API | | Android/IOS | New UI screens , API, Permissions | | | MFD Saas | | | | B2B | | | | MFD | Need to stop MFD and have a link that user can Open | | | VendorName | State | Country | GSTIN | InvoiceNo | InvoiceDate | Terms | DueDate | BillToName | BillToGSTIN | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Vendor 1 | KA | India | ... | INV001 | 2024-01-01 | ... | ... | Client 1 | ... | | Vendor 2 | MH | India | ... | INV002 | 2024-01-02 | ... | ... | Client 2 | ... | - Tech side , most volume channels - Step ID - Analytics , LSQ, DB, OPS - SDK complatablity - Sagar - Neo - Is oversees - JS/React native SDK verison update required ? - Android SDK New AAR file required? - IOS SDK new Framework files required ? - Webhook URL to send the Updated Status to the partner - UI / Copy changes for the

---

## #138 — message template
**Status:** Unknown | **Last edited:** Unknown

# message template **Engagement Messages:** - **Push Notification:** ```css css Copy code You’re almost there, [Name]! Complete your V-KYC to proceed with your loan approval. It only takes a few minutes! ``` - **SMS/Text:** ```vbnet vbnet Copy code Hi [Name], your loan application is nearly complete. Finish your V-KYC verification now to get one step closer to your loan disbursement! [Link] ``` - **WhatsApp:** ```css css Copy code Hey [Name], just a quick reminder! Complete your V-KYC today to secure your loan. Need help? We’re here for you. [Link to V-KYC] ``` - **Email:** ```vbnet vbnet Copy code Subject: [Name], Your Loan is Almost Ready! Complete V-KYC to Continue Hi [Name], Great news! You’re just one simple step away from moving forward with your loan. Complete your V-KYC now, and we’ll handle the rest. If you have questions, our support team is ready to assist. [Link to V-KYC] ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. You’re almost there! Please complete your V-KYC to proceed with your loan application. If you need any help, our team is ready to assist. ``` ### **Segment 2: Users Who Start V-KYC but Don’t Complete It** **Challenges:** - Technical difficulties. - Time constraints. - Confusing process. **Engagement Messages:** - **Push Notification:** ```css css Copy code Hi [Name], your V-KYC is almost complete! Pick up where you left off and finish it in just a few minutes. [Link] ``` - **SMS/Text:** ```css css Copy code Hi [Name], we noticed you started your V-KYC but haven’t finished it yet. It only takes a few more minutes! Complete it now to move forward. [Link] ``` - **WhatsApp:** ```css css Copy code Hi [Name], we noticed you haven’t completed your V-KYC. Need help finishing it? Our team is here to assist. Finish your V-KYC now for faster loan approval. [Link] ``` - **Email:** ```vbnet vbnet Copy code Subject: Complete Your V-KYC Now for a Faster Loan Approval Hi [Name], You’re so close! Your V-KYC is nearly finished, and we just need a little more from you to move forward. Don’t worry—it’ll only take a few more minutes. [Link to complete V-KYC] Need assistance? Our team is happy to help. ``` - **IVR/Phone Call:** ```python python Copy code This is a reminder from Volt Money. We see that you’ve started your V-KYC, but it’s not yet complete. Can we help you finish

---

## #139 — SEO Text
**Status:** Unknown | **Last edited:** Unknown

# SEO Text A Loan against mutual funds (LAMF) allows you to borrow money by using your mutual fund units as collateral. Volt Money’s loan against mutual funds calculator can help you estimate the interest costs associated with this financing option. **What is a loan against mutual funds (LAMF)?** A loan against mutual funds (LAMF) is a secured loan where you pledge your mutual fund units as security to borrow money. The lender will determine the maximum loan amount you can qualify for based on a Loan-to-Value (LTV) ratio. This ratio represents the percentage of your mutual fund's market value that the lender is willing to lend against. You are then issued a credit limit which functions like a bank overdraft facility, where you are charged interest only on the amount you withdraw from this credit limit. **How to get a loan against mutual funds?** With Volt Money, you can get loan against mutual funds in 4 simple steps: 1. Check credit limit: We’ll evaluate your mutual fund portfolio & confirm credit limit. Check your credit limit from here. 2. Instant KYC: Complete digital KYC process. No paperwork required! 3. Pledge your assets: Mark your mutual funds as a security with a trusted lender. 4. Withdraw money: Withdraw & repay as per you requirement. No hidden charges. **How interest is calculated on loan against mutual funds?** Loan against mutual fund works like a bank overdraft limit, where you are only charged interest on the amount you withdraw. Interest is calculated daily and is deducted on a particular date every month. Interest calculation works on the following formula: Daily interest = P*(R/365) Monthly interest = Daily interest*N P = Principal outstanding on the day R = Annual rate of interest N = Number of days in a month Example: Suppose you withdraw ₹50,000 from Volt Money credit line at an interest of 10.49%. The daily interest rate would be calculated as (10.49% / 365) = 0.0287% per day. If the limit is utilized for 30 days, the interest accrued would be: *Interest = ₹50,000 × 0.0287% × 30 = ₹43.05* You can also make part payments to reduce your principal outstanding and thus reducing your interest payable. **Why Volt money’s overdraft like credit limit is better than a loan?** 1. Flexibility: With Volt money’s credit limit, you only pay interest on the amount you actually use, and you can repay it

---

## #140 — LAMF Enhancement
**Status:** Unknown | **Last edited:** Unknown

# LAMF Enhancement ## Objective To introduce a new opportunity type for customers who already have a successful LAMF loan and want to increase their sanctioned credit limit by pledging additional securities. Schema and fields: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | Enhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:Enhacement: Loan Created -> Won, then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DON'T ADD FOR LAMF KEEP IT EMPTY. ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend |

---

## #141 — LAMF Opportunity
**Status:** Unknown | **Last edited:** Unknown

# LAMF Opportunity The LAMF opportunity will be used to capture and track a customer’s first LAMF application, with its own defined opportunity schema. Below mentioned is the opportunity schema of the LAMF opportunity: | **Field Name** | **Schema Name** | **Schema Type** | **Field Update Type** | **Logic** | | --- | --- | --- | --- | --- | | Associated Lead | | Hyperlink | This will be a phone number to redirect to lead | | | Mobile Number | mx_Custom_13 | Phone | Volt backend | | | Opportunity Name | mx_Custom_1 | String | Volt backend | | | Owner | Owner | User | LSQ Automation | | | Current Application Type | mx_Custom_25 | string | Volt backend | LAMF: CREDIT_AGAINST_SECURITIES_BORROWEREnhancement: CREDIT_MODIFICATION_AGAINST_SECURITES | | Excepted Closure Date | mx_Custom_8 | DateTime | Not Required | | | Actual Closure Date | mx_Custom_9 | DateTime | Volt backend | Once the Opportunity is completed:LAMF : Loan Created -> Won then the actual closure date is updated | | Latest Loan Application ID | mx_Custom_49 | String | Volt backend | rename it to loan application id -- this must match the appsmith application id | | Status -> Status Stage | Status | Statusstring | Volt backend | **Status = OPEN ->** Unregistered/Registered/Portfolio Fetch/Portfolio Fetch KFIN/Portfolio Fetch CAMS/Portfolio Pledge/Portfolio Pledge KFIN/Portfolio Pledge CAMS/KYC Verification/Sign Agreement/Link Bank Account/Setup Mandate/Verify Photo/Application Submitted/Credit Approval/Credit Offer Page/ QC Reject **WON ->** Loan Created**LOST ->** Closed - Lost / Close Deferred / Invalid / Not InterestedSTAGE : - To be sent blank | | Origin | mx_Custom_11 | String | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Source | Mx_Custom_3 | Source | Not Required | DONT ADD FOR LAMF KEPP IT EMPTY ADD FOR ONLY MFD ACTIVATION | | Name | mx_Custom_3 | String | Not Required | | | Campaign | mx_Custom_20 | String | Not Required | | | Medium | mx_Custom_21 | String | Not Required | | | Term | mx_Custom_22 | String | Not Required | | | Content | mx_Custom_23 | String | Not Required | | | First Name | mx_Custom_4 | String | Volt backend | | | Last Name | mx_Custom_57 | String | Volt backend | | | KFIN Limit | mx_Custom_52 | Number | Volt backend

---

## #142 — B2B2C Journey Approach
**Status:** Unknown | **Last edited:** Unknown

# B2B2C Journey Approach - MFDs need a **quick and simple way** to check a customer's limit and initiate an application. - MFDs want **clear next steps** for the customer, depending on their status: - If it is **new**, create an application. - If **in process**, continue the application. - If Active application then if **interest is due**, handle repayment, shortfall, or charges. TAT DSP | Channel | B2C | B2B2C | overall volt | B2C | B2B2C | overall volt | | --- | --- | --- | --- | --- | --- | --- | | **Current Step** | **Median (in Sec)** | **Median (in Sec)** | **Median (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | **90 Percentile (in Sec)** | | KYC_PAN_VERIFICATION | 34.03 | 41.86 | 31.8 | 106.28 | 365.15 | 57.23 | | MF_FETCH_PORTFOLIO | 46.05 | 54.65 | 235.15 | 1,33,307.03 | 53,280. | 99,347.14 | | MF_PLEDGE_PORTFOLIO | 262.76 | 197.34 | 37.8 | 1,11,780 | 41,199.34 | 1,509.07 | | KYC_DOCUMENTS | 267.42 | 265.62 | 272.17 | 95,040 | 38,551.15 | 77,981.13 | | KYC_ADDITIONAL_DETAILS | 59.18 | 147.17 | 96.66 | 274 | 297 | 284.46 | | KYC_SUMMARY | 30.3 | 30.46 | 30.31 | 54.43 | 54.78 | 54.54 | | KYC_PHOTO_VERIFICATION | 125.39 | 253.71 | 136.64 | 42,240 | 24,078.21 | 22,688.76 | | BANK_ACCOUNT_VERIFICATION | 46.25 | 47.72 | 41.39 | 435 | 569 | 405.27 | | DIGIO_MANDATE_SIGN | 295.88 | 397.92 | 340.16 | 34,331.54 | 56,355.43 | 54,798.93 | | ASSET_PLEDGE | 92.48 | 132.92 | 104.79 | 286 | 411.56 | 291.74 | | LOAN_CONTRACT | 153.87 | 50.23 | 99.2 | 469.46 | 275.2 | 406.81 | | CREDIT_APPROVAL | 30.07 | 30.37 | 30.19 | 54 | 54.62 | 54.32 | ## Enhancing existing Journey - MFD shares the link to the Customer (~40%) to complete the application and raise a query to Volt in case the Customer faces an issue. - MFDs and RMs are familiar with the current journey and can adapt more easily if changes are introduced gradually. - Most MFDs prefer Volt’s journey over competitors’ **form-heavy desktop interfaces**, which they find cumbersome (based on benchmarking). - The B2C journey is effective for all users, as it keeps the focus on one step at a time, preventing confusion from multiple

---

## #143 — Customer vs MFD
**Status:** Unknown | **Last edited:** Unknown

# Customer vs MFD ### Comparison of Customer and MFD Concerns | **Category** | **Customer** | **MFD** | | --- | --- | --- | | **Motivation** | Solve the money need | Avoid losing AUM | | **Primary Concern** | Worried about EMI amount and repayment schedule | Concerned about Volt not solving customer queries on time | | **Security Concerns** | Worried about the safety of securities | Concerned about access to customer securities, ease of un-pledging, enhancement, etc. | | **Credit Limit Issues** | Limit too low - whole portfolio not fetched | Limit too low - whole portfolio not fetched | | | Limit too low - why is this fund ineligible? | Limit too low - why is this fund ineligible? | | **Portfolio Concerns** | Wants to remove STP folios | Wants to remove specific folios | | **Understanding Credit Line (CL)** | Doesn’t understand CL without Sales help | MFDs have to explain CL to customers | | **Mistakes & Liability** | Concerned about making a mistake that locks/sells securities | Except for big MFDs, others worry about liability as an intermediary | | **Processing Fees (PF)** | High PF for a small amount/short-term need + GST charges | High PF for a small amount/short-term need | | **Loan Repayment & Security Registration** | Will my funds be sold for the loan? | Will customer funds be sold for the loan or registered in Volt’s name? | | Disbursement | Will the entire credit limit be transferred to my account? | Will the entire credit limit be transferred to the customer’s account? | | **Comparison with Other LAMF Providers** | ABFL - 9.5% Jio Finance - 9.99% | | | **KYC** | No issues - Familiar with Digilocker | Customers trust MFDs with OTP | | **Live Selfie** | No major concerns | Customer may not be available with MFD | | **Mandate** | 10 lakhs is too high | 10 lakhs is too high | | **Disbursement** | How to take disbursement? | How to take disbursement? | --- Key Takeaways % of users reduced limit = count of applications with Pledged_limit/Fetched_limit | Partner Status | 0-10% | 10-20% | 20-30% | 30-40% | 40-50% | 50-60% | 60-70% | 70-80% | 80-90% | 90-100% | 100% | Total | | --- | --- | --- | --- | --- | ---

---

## #144 — Mandate failure analysis
**Status:** 13 | **Last edited:** Unknown

# Mandate failure analysis Top 5 banks with highest failure rates (minimum 20 transactions): 1. State Bank of India has the highest number of failures (429) with failure rate of 33.36% 2. Airtel Payments Bank: 64.71% (22/34) 3. Fino Payments Bank: 52.00% (13/25) 4. UCO Bank: 46.15% (18/39) 5. AU Small Finance Bank & Dhanlaxmi Bank: 45.00% (9/20) 6. IDBI: 40.28% (29/72) Customer-Related (738 cases): - No response received from customer while performing: 415 @Vinit Pramod Sarode @Nihal Simha M S can you call these customers ? / - Transaction rejected/cancelled by Customer: 122 - Browser closed by customer in mid transaction: 96 - User rejected transaction on pre-Login page: 23 - Previous Request in Progress: 21 - Maximum tries exceeded for OTP: 5 - Time expired for OTP: 1 Authentication/Validation Issues (217 cases): - Aadhaar Number not linked with Debtor AccNo: 77 - Debit card validation failed - Invalid PIN: 25 - Authentication Failed: 9 - Debit card not activated: 11 - Invalid User Credentials: 5 - Invalid OTP value: 2 - Invalid Aadhaar Number/Virtual ID: 2 - Debit card Blocked: 5 - Invalid bank OTP: 1 - OTP invalid: 1 - Debit card validation failed - Invalid card: 1 - Debit card validation failed - Invalid CVV: 1 Technical Issues (168 cases): - UNNKNOWN_ERROR: 79 - Technical errors/connectivity at bank: 75 - Error in Processing Mandate: 3 - Error in decrypting: 3 - Error in Posting Details: 2 - INVALID BANK RESPONSE: 1 - Error processing Aadhaar OTP: 1 Account-Related Issues (127 cases): - Mandate Not Registered (insufficient balance): 47 - Account not in regular Status: 13 - No such account: 7 - Account Number not registered with Net-banking: 7 - Account Number registered for view-only: 8 - Account inactive: 3 - Account Inoperative: 1 - Account type mismatch with CBS: 1 Limit/Restriction Issues (32 cases): - Bank Restricts Duplicate request/Amount Exceeds Limit: 21 - Amount Exceeds E-mandate Limit: 11 Other Issues (49 cases): - Merchant MsgId duplicate: 11 - Mandate registration not allowed for Joint account: 8 - Bank RjctRsn ReasonCode empty/incorrect: 5 - AUA license expired: 2 - Aadhaar number does not have mobile number: 8

---

## #145 — Digio Volt Exploring mandate authorisation flows
**Status:** Unknown | **Last edited:** Unknown

# Digio <> Volt: Exploring mandate authorisation flows What are the different ways via which we can authorise mandates? Debit Card Net Banking Aadhaar OTP Bank OTP - Bank level integrations Some users dont have net banking and aadhaar card, how can we create digital journeys for them for easy mandate set ups? Does digio support direct bank otp based mandate set ups? is it for all banks or specific banks? if yes can we get a list of the supported banks? Check internally bank level requests, how many of our requests can be eased via direct integrations? If not how does one do that? does She have context

---

## #146 — Mandate Limit Change for LSPs
**Status:** Unknown | **Last edited:** Unknown

# Mandate Limit Change for LSPs ## **Context** In the Loan Against Mutual Funds (LAMF) journey, customers complete the Registration → Selfie → KYC process → Fetch their Funds →Select a Credit Limit→Add and Verify Bank account and are required to register a mandate. Currently, the mandate amount is fixed at **₹10 lakhs**, irrespective of the actual loan/limit sanctioned. This often creates friction for customers with smaller credit lines, leading to: - Drop-offs at the mandate step - Customer confusion & higher support queries - Lower overall funnel conversion To address this, we conducted an **A/B test** across Volt journeys with three mandate structures: 1. Fixed ₹10 lakh (Control) 2. 20% of selected limit (Test 1) 3. 100% of selected limit (Test 2) **Result:** Test 2 (100% of selected limit) showed the **highest mandate completion rate.** The jump in conversion rate which we observed was ~500 basis points compared to the other two cohorts. --- ## Benefits (for LSP & Customers) ### LSP: **Higher Conversion** – Familiarity with the amount led to higher conversion as tested internally. **Reduced Queries** – Lower customer support tickets related to high mandate value. ### Customer: **Customer Trust** – Avoids mismatch between Selected Limit and Mandate authorization amount. **Improved UX** – Intuitive mandate journey for end customers. --- ## **Proposed Change for LSP** - A minor change in the Create Mandate/Mandate Init API in order to ****have **Mandate value = 100% of the selected loan limit** (capped at ₹10 lakh). - DSP will handle the rest of the process (mandate creation, presentation, and maintenance). --- ## API Changes API: [https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init) Current API Parameters: ``` "opportunityId" "bankAccountVerificationId" "endDate" "mandateType" "mandateAmount" "redirectionUrl" ``` Parameter which needs to be added and passed: “selectedLimit” New API request: curl --location '[https://api.staging.dspfin.com/los/api/v1/utility/mandate/init](https://api.staging.dspfin.com/los/api/v1/utility/mandate/init)' \ --header 'Content-Type: application/json' \ --header 'X-SourcingChannelCode: Code Provided by DSP' \ --header 'X-Signature: Signature generated from the authentication script' \ --header 'X-Timestamp: Timestamp generated from the authentication script' \ --data '{ "opportunityId": "OPP8724213445", "bankAccountVerificationId": "URBANK4674555244", “selectedLimit”: “40000” "endDate": "2039-09-20", "mandateType": "API_MANDATE", "mandateAmount": "10000000", "redirectionUrl": "[https://www.voltmoney.in](https://www.voltmoney.in/)" }' --- ## **Next Steps for LSPs** 1. **Integration Update**: Pass the selected loan limit in DSP’s Create mandate API. 2. **Testing**: Validate mandate creation and completion in staging. 3. **Rollout**: Intimate release plan with DSP to move to production. ---

---

## #147 — Activation LSQ Task Creation
**Status:** Unknown | **Last edited:** Unknown

# Activation: LSQ Task Creation Flow: 1. Link generated gets generated and sent to the MFD over whatsapp 2. Task gets published in LSQ 3. RMs follow the tasks for calling and supporting the MFD with the VKYC flow and the link

---

## #148 — Discussion with Rohan (Groww)
**Status:** Unknown | **Last edited:** Unknown

# Discussion with Rohan (Groww) 1. Building in-house after 1 year of operations is recommendable instead of building it in-house from the start 2. VideoSDK has good solution for the video session. 3. Groww built all the in-house cause they were aiming for 4. Hyperverge gives a high amount of false negatives 5. Initially: Success rate → 80% and VKYC completion rate → 70% 6. After spending 2 quarters improving on the Vkyc stack, Success rate → 95% and VKYC completion rate → 80% 7. It is important to store the data correctly and in a reproducible manner. 8. IDfy and Digio are recommended VKYC solution providers 9. Digio uses VideoSDK for their video stack - confirmed 10.

---

## #149 — LSP Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# LSP Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an NBFC, our control is limited over the Pre-VKYC and Post-VKYC user experience. Following are the steps of a VKYC journey which we govern: ## Journey Flow: ### Pre-VKYC Session: 1. Check the 3 day rule and Stitch e-KYC flow (depending on the LSP) - What is the 3 days Rule? RBI mandates VKYC be completed within 3 days from completing e-KYC. If the customer does not, lender will need to initiate the e-kyc flow

---

## #150 — VKYC Regulatory Understanding
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Regulatory Understanding - RBI Direction for V-CIP Infrastructure and Procedure [Reserve Bank of India](https://www.rbi.org.in/CommonPerson/english/scripts/notification.aspx?id=2607) Definition of V-CIP (from Section 3): > "Video based Customer Identification Process (V-CIP)": -CIP an alternate method of customer identification with facial recognition and customer due diligence by an authorised official of the RE by undertaking seamless, secure, live, informed-consent based audio-visual interaction with the customer to obtain identification information required for CDD purpose, and to ascertain the veracity of the information furnished by the customer through independent verification and maintaining audit trail of the process. Such processes complying with prescribed standards and procedures shall be treated on par with face-to-face CIP for the purpose of this Master Direction." > ### **Risk Classification:** - **High Risk designation** for customers until face-to-face KYC completion within 2 years - **VKYC serves as alternative** to in-person verification for borrowal accounts - **Debit restrictions** apply for high risk customers if KYC is not updated every 2 years ### **Documentation Requirements:** - **E-PAN accepted** - no physical PAN card showcase needed - **Photo matching mandatory** - agent must verify customer photo consistency across Aadhaar/OVD and PAN/e-PAN documents ### **Timeline Compliance:** - **3 working days maximum** from initial identification information collection to VKYC completion - The customer's economic and financial profile/information must be confirmed directly with the customer during the V-CIP process - 3 way check of the face of the customer using the selfie, photo on the OVD/Aadhaar Card and the e-PAN/PAN Card - V-CIP technology infrastructure must be housed on the RE's own premises, with connections and interactions originating only from its secured network. Any outsourced technology must comply with RBI guidelines. For cloud deployments, data ownership must remain solely with the RE, and all data—including video recordings—must be immediately transferred to the RE's owned or leased servers after V-CIP completion. Cloud service providers or third-party technology vendors must not retain any data from the V-CIP process. - ###

---

## #151 — Name
**Status:** Unknown | **Last edited:** Unknown

# Name Column 1: Does it check if the permissions are given? Column 2: Switch On Permission automatically/guide the customer? Column 3: Is Scheduling Available? Column 4: Configure communications for scheduled customers? Column 5: Is Digi Locker Integrated? Column 6: Is Pan Required? Column 7: Does Dashboard have Analytics Available?

---

## #152 — VKYC Vendor Evaluation
**Status:** Unknown | **Last edited:** Unknown

# VKYC: Vendor Evaluation # Evaluation Criteria # Vendor List List of vendors. - Hyperverge - Demo completed (SDK) - IDFy - Perfios - Signzy - Demo Complete (API driven) - Digio - Demo Completed - AuthBridge - Demo Completed - Pixl - Demo not Completed - KYC Hub - Demo Completed # Evaluation ## Summary [Untitled](VKYC%20Vendor%20Evaluation/Untitled%20216e8d3af13a80248558f522cbf900a8.csv) ## Hyperverge ## IDFy ## Perfios

---

## #153 — Volt Focused VKYC Journey Alignment
**Status:** Unknown | **Last edited:** Unknown

# Volt Focused VKYC Journey Alignment With the latest updation to Know Your Customer (KYC) Direction, face-to-face KYC is mandatory for all digital lending (except term loans under Rs. 60,000). V-CIP (Video Customer Identification Process) has been presented by the RBI as an alternative to offline KYC. This document outlines the complete V-CIP journey implementation based on competitive benchmarking of 6 Video KYC journeys (of Slice saving account opening, LazyPay BNPL LOS journey, Navi PL LOS journey, Shivalik SFB FD (Super.Money), Unity SFB (Stable Money) and Refyne PL LOS journey). - Brief about VKYC and its process Video KYC is a face-to-face KYC method recognised by RBI as an alternative to offline KYC. This involves the agent (Employee of the RE) following checks: 1. Customer verification 2. 3 way Photo Verification 3. Live location Check (Cx needs to be in India) 4. Liveness Check Pre-VKYC contains following need to be managed steps: 1. Pre-session messaging 2. Device permission enablement and Instructions 3. Consent for doing VKYC 4. Scheduling 5. Queuing During VKYC session following steps need to be completed: 1. Security Questions 2. Livininess Check 3. PAN Capture 4. Face Match 5. Location Capture Post VKYC session following steps need to 1. Based on Agent Marking the session as: 1. Marking Session Success: Customer’s VKYC session is completed and pushed to the Auditor’s bucket for final review. 2. Marking Session Failure: Customer needs to re-attempt VKYC. 3. Marking Session Incomplete: Webhooks to inform the LSP; will require the customer to complete the session using the same video link 2. Once the agent marks the session as a success, next is the Auditor Review: 1. Marking Session Success: Webhooks to inform LSP; complete application and initiate withdrawal on LSPs end 2. Marking Session Failure: Webhooks to inform the LSP; will require the customer to redo their VKYC 3. Marking Session Reopen: Webhooks to inform the LSP; will require the customer to redo their VKYC ![image.png](LSP%20Focused%20VKYC%20Journey%20Alignment/image.png) As an LSP, we control the Pre-VKYC and Post-VKYC (except the queuing process). ## Pre-VKYC 1. Initiation Page: 1. Pre-messaging: 1. Educate about VKYC 1. Context Setting for the customer: 1. Mandatory Step by RBI 2. Inform about the 3days rule - What is the 3 days Rule? RBI mandates VKYC be completed within 3 working days from completing e-KYC. If the customer does not, lender will need to initiate the e-KYC flow before initiating VKYC

---

## #154 — Untitled
**Status:** Unknown | **Last edited:** Unknown

# Untitled Amrit: Process kaise hoga, loan disbursal process, their commission, Referral program Kevin (Servicing): 10% buffer for Bajaj Mahesh: Repayment queries, How is my interest calculated, Stop growing, ownership changed, low ticket sizes, Dont need the loan right now, they want to check limit. Names: Common questions Naveen: - Processing fee channel - Transparency KYC - Fetch and Setting during this time we dont see the interestv or fees

---

## #155 — CKYC OTP verify error cases
**Status:** Unknown | **Last edited:** Unknown

# CKYC OTP verify error cases | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | Customer enters wrong OTP | | | | | Resend tried by customer before 90 secs | | | | | Exceeded OTP verify attempts | | | | | | | | |

---

## #156 — CKYC S&D error handling
**Status:** Unknown | **Last edited:** Unknown

# CKYC S&D error handling | **Case description** | CKYC terminal status | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | PAN or Mobile number do not match with the records in Cersai. | | | | | Mobile number doesn’t match | | | | | Mobile number doesn’t exist | | | | | Customer doesn’t exist in CKYCRR | | | |

---

## #157 — Design requirements
**Status:** Unknown | **Last edited:** Unknown

# Design requirements - Complete journey in DSP theme - Do we need a new anchor page on the Volt side? - What will happen in case customer drops off and starts the KYC journey again? - What will happen if the user faces an error in KYC? - Include an optional “Secondary logo”. This will be configured for each LSP - How can we make sure customers enter PAN details as per PAN only? - Add digilocker screens as well in the flow, this will be added in case CKYC fetch is failed - Do we need the KYC successful bottom sheet **Wed 19th March, 2025** - [x] Two sections one for Volt and another for DSP - [x] DSP will have a header as well, LSPs can pass a parameter to show or hide the header - [x] Primary, secondary, tertiary colour change option @Karuna Sankolli - [x] Retry KYC screen, this will be from Volt Side @Karuna Sankolli - [x] Secondary logo pendikng @Karuna Sankolli - [x] Rethink retake selfie flow @Karuna Sankolli - [ ] What will Volt header show when the DSP KYC is in progress @Saksham Srivastava - [ ] Deviation flow will be there or not? @Saksham Srivastava - [x] Jupiter colors @Saksham Srivastava

---

## #158 — NSDL error messaging
**Status:** Unknown | **Last edited:** Unknown

# NSDL error messaging | **Case description** | **Condition** | **Error message from HV** | **Error message to be shared with LSPs** | | --- | --- | --- | --- | | NSDL returns name not matching | | | | | NSDL returns DOB not matching | | | | | NSDL returns | | | |

---

## #159 — NBFC B2B LSP API List
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : API List - Pledge API on DSP - pending - Fetch API on DSP - pending - Submit opportunity - create account - Mobile & Email update - no verification - Add verification timestamp for mobile & email - KFS & Agreement: we might have to decouple and make KFS pass the response in parameters - Offer API on DSP - LSP passes back the confirmation to DSP - PAN verification - LSP not required to integrate -

---

## #160 — NBFC B2B LSP Journey
**Status:** Unknown | **Last edited:** Unknown

# NBFC B2B LSP : Journey # Journey Overview Below is the envisaged customer journey as part of the B2B stack. - **Mobile verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP based) in an API to DSP. - **Email verification**: there’s no explicit customer verification since the customer is already verified. Instead, the B2B partner passes the timestamp of customer verification (OTP/SSO based) in an API to DSP. - **Fetch**: this step requires explicit consent through OTP from the customer using MFC or CAMS/KFin. This can be done through one of the methods mentioned in [Fetch step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a802a83dac810aab506a5). - **Offer acceptance**: this step requires the customer to confirm the offer on the partner’s UI and the partner intimates DSP as mentioned in [Offer Acceptance step](https://www.notion.so/volt-money/NBFC-B2B-LSP-Journey-123e8d3af13a806f9cfedd7a811c96f9?pvs=4#123e8d3af13a8056b782ece5c9307d35). - **KYC verification**: - **Bank account validation**: - **Mandate registration**: - **Pledge**: - **KFS**: - **Agreement**: - Loan creation: - **Withdrawal**: - # Journey Points ## Approach Overview Below are the key interactions/ touchpoints in the journey and the preferred and fallback approach for each step. | Step | Preferred Approach | Secondary Approach | | --- | --- | --- | | Mobile verification | Approach 2: LSP passes the mobile verification log to DSP | | | Email verification | Approach 2: LSP passes the email verification log to DSP | | | Funds fetch | Approach 2: LSP fetches the funds from MFC through DSP APIs | | | NAV and LTVs | DSP to maintain the NAV and LTVs of each fund at its end. LSP can use that or can use their list as long as the values are aligned to our policy | | | Offer acceptance | Approach 2: LSP fetches the offer from DSP passes the offer acceptance details to DSP | | | KYC verification | Approach 2: LSP verifies the KYC through DSP’s APIs directly | | | Bank account validation | Approach 2: LSP passes the bank account to be added which will be validated async | | | Mandate registration | Approach 2: LSP integrates with DSP’s APIs and handles redirection to NPCI, etc | | | Pledge | Approach 2: LSP pledges the funds from MFC through DSP APIs | | | KFS | Approach 2: LSP integrates with DSP’s APIs and renders the KFS on their UI

---

## #161 — NBFC Launch GTM
**Status:** Unknown | **Last edited:** Unknown

# NBFC Launch GTM # Overview This document gives an outline of the key phases of our NBFC launch across multiple channels with Volt and outside as well. This is to drive alignment in terms of the segments, channel as well as efforts from a product, technology, business and operations perspective. # Objective The broad objectives of launching this in phases are. - To test the stack end-to-end to ensure accuracy when launched at scale - To test the process end-to-end to ensure customer experience is met - To ensure internal users are fully aware of the new flow - To identify and address any gaps in the flow to ensure minimal impact at scale - To ensure uptime and reliability of the stack for optimum experience at scale # Success Criteria Below are the key funnel metrics that define the CUG program and expected thresholds. - Lead to Pledge %age - 50% - Sanction TAT - 15 minutes - KYC completion %age - - NACH completion %age - - Lead to sanction conversion %age - - Sanction to disbursement %age - - Disbursement TAT - 2 hours - Disbursement success rate - At least 95% Below are the key internal operational metrics that define the CUG program and expected thresholds. - QC Ops approval TAT - 30 minutes - Credit deviation approval TAT - 30 minutes - Checker approval TAT - Not more than 30 minutes from request placed - QC approval rate - 95% (At least 95% of cases should turn out to be accurate decisions) - Checker approval rate - 95% (At least 95% of maker request should be accurate decisions) # Phases We intend to roll out the NBFC platform in a phased manner as aligned to our objectives. ## Phase 1 **Objective**: To test out the flow with at least 100 customers to identify issues and fix them proactively. Below are the points of consideration. | Aspect | Consideration | Comments | | --- | --- | --- | | Timeframe | Upto 10 days | | | Total number of applications | 100 - 120 | | | Sourcing channel | MFD | | | Partners | Whitelisted partners | MFD team to share the MFDs for whitelisting | | Drawing Power | 25K - 2CR | | | Number of applications/day | 10-15 | | | Recommended DP | Upto 10L | Can