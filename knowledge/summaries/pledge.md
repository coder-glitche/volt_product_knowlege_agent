# Current State: Pledge

> Auto-generated from 51 PRD(s). Most recently edited shown first.


---

## 🟢 LATEST — MF Pledge optimizations
**Status:** In progress | **Last edited:** September 16, 2024 8:23 PM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #2 — [IronGrid] Adding un-pledge validations in BE
**Status:** Not started | **Last edited:** October 25, 2024 1:20 PM

# [IronGrid] Adding un-pledge validations in BE ### Validations present in FE **FE Checks** - Manage limit - Remove pledge - Pledge more - Pledge history - At this page we have a starting check of buffer - User taps on Remove pledge and lands on the screen with list of funds - Buffer check applied again to calculate the number of units which can be selected by the user for un-pledging **Checks to be added** - Jay to share the tech solutioning doc of the customer - Folio level checks need to be added - Need to create validation in init API using this API : app/borrower/lms/credit/lender/manageLimitConfig

---

## #3 — Pledge error handling v1
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

## #4 — Lien removal SLA tracking report
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

## #5 — Lodgement decoupling from enhancement
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

## #6 — [IronGrid] Un-lien related issues
**Status:** Not started | **Last edited:** November 5, 2024 12:48 PM

# [IronGrid] Un-lien related issues ## Fund level status of un-pledge request **Phase 1** - Terminal statuses of funds’ un-pledge request are SUCCESS, FAILED. - We will keep polling the status of all the funds until we get the terminal statuses of each of the funds - We keep polling the API for 4 days every hour until we get the status of all the fund - Un-pledge request level terminal status (will be updated once terminal state of all the funds is reached) - If all the funds’ status is SUCCESS, we mark the status of un-pledge as SUCCESS → In FE we will show Success as the status of unpledge request - If any of one the funds’ status is SUCCESS, we mark the status of un-pledge as PARTIAL_SUCCESS → In FE we will show Success as the status of unpledge request - If status of all the funds are rejected/failed then we store status as FAILED → In FE we will show Failed as the status of unpledge request - We will store the individual status of all the funds under the un-pledge request - API Documentation : [Release Status 1 (1).docx](%5BIronGrid%5D%20Un-lien%20related%20issues/Release_Status_1_(1).docx) **Phase 2** - We will monitor the partial success un-pledge request occurrence, and accordingly chart out a UI handling, where we can show and convey partial un-pledge success to the user. ## Excess margin handling in un-pledge request **For BFL (only need to make this change for BAJAJ)** - While a user is requesting, we get the net payable from the ForeClosure details API for using it in our buffer calculation to calculate the number of units the user can raise for un-pledge. - 3 fields which are present in Foreclosure details API : - net payable = Total due - Excess Margin - Total Due - Excess Margin - For BAJAJ, we will use totalDue field in place of net payable field for calculating total outstanding. ### **User not able to request un-lien request if stocks present in their holding** - **Issue** - When a user has stock in their account, and when they tap on view details, they we get a null pointer error. This is because we hit asset_meta_data table for showing fund details in the manage limit screen, but this table just contains data for MFs and not stocks, hence gives a null pointer error - **Solution** - We will only

---

## #7 — Lodgement maker
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

## #8 — MFC Pledge error handling - V1 (1)
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

## #9 — MFD Client registration to KYC flow
**Status:** In progress | **Last edited:** May 28, 2025 12:45 PM

# MFD Client registration to KYC flow ### **Overview** The first step in taking a Loan Against Mutual Funds (LAMF) is to check the eligible credit limit for a customer. This involves: 1. **Registering the customer** 2. **Fetching details of their mutual funds** 3. **Calculating the credit limit** 4. **Presenting a loan offer** The current journey to the offer page can be streamlined to better cater to user needs and improve conversion rates. ## **Objective** - **Increase conversion** from registration to application creation. - **Optimise the top-of-funnel (TOFU) experience** before the KYC stage. ## **Current vs. Proposed Journey** | **Current Journey** | **Proposed Journey** | | --- | --- | | Add phone number | Add phone number | | OTP | Add PAN number | | Email | MFC summary fetch OTP | | Email SSO or OTP | Offer page | | PAN | | | DOB | | | Verify PAN | | | Fetch | | | OTP | | | Unlock limit | | | Set limit | | | Offer page | | ## **Issues in the Current Process** ## Client Registration issues 1. After the Register phone number OTP there is a redundant page confusing MFD to believing the process is complete. ![Screenshot 2025-04-09 at 6.09.56 PM.png](MFD%20Client%20registration%20to%20KYC%20flow/Screenshot_2025-04-09_at_6.09.56_PM.png) 1. The Email is not Pre-Filled if the MFD has MFC fetched for the client 2. The E-mail google SSO is not ideal for MFD channel as the Google picks up MFD email. 3. We want to remove the Page of email selector and move to the add email screen 1. Text “Add client email ID” 4. MFD add their own email in the E-Mail step as it is not explicitly called out. 5. MFDs have to fetch the Limit again after fetching in the Check limit section. ## Offer page issues 1. **Lack of clarity** about LAMF benefits vs. mutual fund redemption. 2. **Customer misconception** that the limit shown is deducted from their mutual funds. 3. **Fear of entire limit being disbursed** instead of flexible withdrawals. 4. **STP (Systematic Transfer Plan) concerns**—customers hesitate as STP stops once funds are in lien. 5. **Limited understanding of Credit Line or Overdraft (OD) accounts.** 6. **Confusion about interest rates**—reducing vs. flat rate. 7. **Processing fees (PF) issues** for smaller ticket loans. 8. **Unfavourable tenure**—customers may not want a fixed 3-year loan. ## **Proposed Solutions** 1. **Decouple credit limit

---

## #10 — CAMS min_unit Validation for LAMF Lien Transaction
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

## #11 — Lodgement STP optimisations
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

## #12 — [Platform] Unpledging of unlinked funds bulk appro
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

## #13 — Revocation Status API
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

## #14 — Lien status lifecycle tracking
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

## #15 — RTA pledge without RTA fetch - PhonePe
**Status:** Not started | **Last edited:** June 6, 2024 2:30 PM

**Problem:**
are we solving?**

1. Reducing steps for the user to complete application on PhonePe

---

**Solution:**
?**

---

## #16 — Margin pledge charges
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

## #17 — Margin pledge charges
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

## #18 — MFC Pledge (revocation & invocation)
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

## #19 — [Platform +Volt ] MFC Pledge wrapper APIs + Volt J
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

## #20 — [Volt LSP] MFC pledge
**Status:** Not started | **Last edited:** July 21, 2025 3:33 PM

**Problem:**
are we solving?**

Current pledging requires customers to submit upto two OTPs, one for CAMS and another from KFin. This add to the friction in our loan application journey. 
MFC pledging APIs solve this by requiring 

---

**Solution:**
?**

---

## #21 — Revocation status for foreclosures
**Status:** Not started | **Last edited:** January 7, 2025 6:10 PM

**Problem:**
are we solving?**

---

- Currently we are not storing the status of un-pledge requests that are raised to the lender at the time of foreclosure requests
- We keep following up with the lender Ops team about the foreclosure status even when the un-pledge request of the foreclosure has itself failed

**Solution:**
?**

---

## #22 — [Fenix] Lodgement maker bulk approval
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

## #23 — [Email Template] Decoupling of Lodgement and Agree
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

## #24 — [CC] Lodgement Enhancement
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

## #25 — Customer Lifecycle Tracking - Lien Unmarking → Rep
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

## #26 — Product Note Separating Portfolio Pledge and Asset
**Status:** Not started | **Last edited:** February 21, 2025 3:29 PM

# Product Note: Separating Portfolio Pledge and Asset Pledge Steps in LSQ # Product Note: Separating Portfolio Pledge and Asset Pledge Steps ## Current Behavior Currently, the system combines two distinct steps - MF Portfolio Pledge (offer page) and Asset Pledge - into a single step labeled as `ASSET_PLEDGE_STEP` in the CRM event mapping. This creates ambiguity in tracking and managing these separate processes. ## Problem Statement The current implementation: 1. Does not distinguish between portfolio pledge (offer page) and actual asset pledge steps 2. Sales agents have hard time understanding is the application is on offer or pledge for calling 3. Creates confusion in the application flow tracking 4. Reduces granularity in analytics and monitoring ## Proposed Solution Separate the current combined step into two distinct steps: 1. **Portfolio Pledge** (`PORTFOLIO_PLEDGE_STEP`) - Represents the offer page where customers view their eligible portfolio - Maps to `MF_PLEDGE_PORTFOLIO` in application flow 2. **Asset Pledge** (`ASSET_PLEDGE_STEP`) - Represents the actual asset pledging process - Maps to `ASSET_PLEDGE` in application flow ## Implementation Changes Required 1. Update CRM event mapping in `getCRMEvenTypeForStepStart`: ```java case MF_PLEDGE_PORTFOLIO -> CRMEventType.PORTFOLIO_PLEDGE_STEP; case ASSET_PLEDGE -> CRMEventType.ASSET_PLEDGE_STEP; ``` 1. Update DB schema to reflect new step definitions: - Add `PORTFOLIO_PLEDGE` as a distinct step after `MF_FETCH_PORTFOLIO` - Keep `ASSET_PLEDGE` in its current position in the flow ## Expected Benefits 1. Improved tracking and analytics 2. Better user journey mapping 3. Better lead prioritisation in outbound ## Migration Plan 1. Understand current Lead stage update activity send to LSQ 2. Create new step definitions in DB 3. Verify the changes in LSQ 4. (Backfill) ## Next Steps 1. PN :- Tech Review

---

## #27 — Pledge error handling
**Status:** In progress | **Last edited:** February 19, 2026 7:14 PM

**Problem:**
are we solving?**

Users are encountering difficulties when pledging folios due to the following error encountered during validation and authentication for CAMS and KFIN:

**Solution:**
?**

---

## #28 — Foreclosure and lien removal request validation
**Status:** In progress | **Last edited:** February 19, 2026 7:12 PM

**Problem:**
are we solving?**

- We allow user to foreclose loan when repayment, withdrawal and lien removal request are in progress which are leading to inaccuracy in calculation of net payable amount and eventually leading to request rejection from the lender ends.
- Foreclosure request are getting rejected when user are placing foreclosure when lien-removal request are already in progress.

---

**Solution:**
?**

---

## #29 — Partial lodgement handling - DSP
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

## #30 — Revocation MIS - TCL customer
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

## #31 — Pledged portfolio API (KFIN)
**Status:** Done | **Last edited:** February 1, 2025 1:21 PM

# Pledged portfolio API (KFIN) ### **Purpose** The API enables a lender to request detailed information about an investor's mutual fund folios that are pledged as collateral. It provides insights into folio numbers, pledged units, ISINs, and related details. --- ### **Request Method** **POST** `/PortfolioRequest` --- ### **Request Headers** | **Name** | **Type** | **Description** | **Default Value** | | --- | --- | --- | --- | | `CLIENT` | string (header) | Client Header | XXXXXX | | `CLIENT-ID` | string (header) | Client ID Header | XXXX | | `CLIENT-SECRET` | string (header) | Client Secret Header | XXX | | `Content-Type` | string (header) | Content Type | application/json | --- ### **Request Body** The body accepts a JSON object containing: ```json json Copy code { "PortfolioRequest": { "InvPan": "ABC123", // Investor PAN "RequestID": "123", // Unique Request ID "AgentCode": "ABC123" // Agent Code } } ``` --- ### **Response** ### **Success (Code: 0)** Returns detailed data for pledged mutual fund units. Example: ```json json Copy code { "Dtinformation": [ { "Return_Code": 0, "Return_Msg": "Success" } ], "DtData": [ { "RequestID": "123", "InvestorPAN": "ABC123", "InvestorName": "ABC", "FolioNo": "123", "ISIN": "ABC123", "LienMarkedUnits": 0.1, "CurrentNAV": 0.1, "CurrentValue": "0", ... } ] } ``` ### **Failure (Code: -100)** Returns a message if the data does not exist. Example: ```json json Copy code { "Dtinformation": [ { "Return_Code": 0, "Return_Msg": "Data Does not exist" } ] } ``` --- ### **Key Features** - **Parameters:** Accepts investor PAN, request ID, and agent code. - **Output Details:** Comprehensive folio and pledged unit details like: - Folio number - Pledged units and amount - NAV and current value - Investor and lender information - **Error Handling:** Indicates when no data is found. This API is primarily intended for lenders to access mutual fund collateral data securely and efficiently.

---

## #32 — MFC Pledge error handling - V1
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

## #33 — Un-pledge optimisations
**Status:** In progress | **Last edited:** December 3, 2024 3:13 PM

**Problem:**
are we solving?**

For BFL users, who make a withdrawal request of complete available amount while an un-pledge request is in-progress then the withdrawal requests gets processed first and un-pledge request gets rejected due to update in the value of net-payable due to the withdrawal processing  

---

**Solution:**
?**

When user is making a withdrawal is making a withdrawal while an un-pledge request is in “In progress” we will give a heads-up to the user that the withdrawal request might interfere with the un-pledge request if the outstanding is not zero. [This change only needs to be done for BFL]

---

## #34 — Un-pledging bug fixes & UI optimisation
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

## #35 — Lien removal buffer enhancement (Note)
**Status:** Not started | **Last edited:** August 10, 2024 3:51 PM

# Lien removal buffer enhancement (Note) [Bajaj buffer handling for lien removal](https://app.notion.com/p/Bajaj-buffer-handling-for-lien-removal-90fa191a67ec4f38b2bff1cfe6d99a98?pvs=21) For Bajaj, we had placed a buffer of 5% on total outstanding when users raise collateral removal requests to handle NAV changes. Collateral removal requests take 1-2 working days to be processed by the lender and hence to ensure requests are not cancelled this buffer is maintained. Due to high volatility in markets our requests are still getting rejected despite the 5% buffer. We need to solve for the cancellations. One proposed method by the business team is to increase the buffer to 10% however that impacts customer experience. Need solutioning for the same.

---

## #36 — [Platform] Validation to Stop Un-pledging, closure
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

## #37 — MFD client management
**Status:** In progress | **Last edited:** April 30, 2025 10:50 AM

**Problem:**
are we solving?**

---

**Solution:**
?**

---

## #38 — Unpledge and Disbursement Enhancement
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

## #39 — Lodgement Enhancement
**Status:** Deprioritised | **Last edited:** Unknown

# Lodgement Enhancement Assign: Karuna Sankolli Charter: NBFC Pod Task type: Sprint # Context [[Platform] RTA portfolio API integration](../PRDs/PRDs/%5BPlatform%5D%20RTA%20portfolio%20API%20integration%20166e8d3af13a80a7a325c550ed9f8c04.md) # Design - [ ] Partial approval component - [ ] Button sizes Ops https://www.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2431-157171&t=wnkdjY7E7DaaJvbj-11

---

## #40 — Lodgement addition and removal maker
**Status:** Ready for kickoff | **Last edited:** Unknown

# Lodgement addition and removal maker Assign: Karuna Sankolli Charter: NBFC Pod Task type: Sprint # Context [https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469](https://volt-ea96402.slack.com/archives/D07UQN9REE7/p1736322208430469) **MOM** 1. Discovery you can maker for lodgement 2. Upload 3. Review 1. Dedupe check -> Already lodegd or not 2. Pledge check -> Pledged with the LSP 4. Data points 1. Folio 2. Loan acct number -Future 3. PAN number 4. Investor name 5. Units 6. Scheme name 7. Lien ref number CAMs 8. IHNO Kfintech 9. ISIN 10. Status 11. Remarks 5. Do I want to ops to work on the file, RTA level 6. Grouping based on PAN & Loan acct number # Figma [https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system](https://embed.figma.com/design/HpVXJgl9FRLeWiFFdlWGpS/LMS%3A-Command-center?node-id=2496-121040&t=kmmbGgrjuKoI4i0e-11&embed-host=notion&footer=false&theme=system)

---

## #41 — Pledge Error PRD
**Status:** Unknown | **Last edited:** Unknown

# Pledge Error PRD # Product Requirements Document (PRD) ## Title **Volt Money Pledge Error Handling Enhancement** --- ## Table of Contents --- ## Introduction The Volt Money application facilitates users in managing their mutual fund investments, particularly through the pledging of folios for loan purposes. This PRD focuses on enhancing the error handling mechanisms during the pledge process to improve user experience, reduce drop-offs, and minimize support queries. ## Problem Statement Users are experiencing significant difficulties during the folio pledging process, primarily due to various errors encountered during validation and authentication with CAMS and KFIN. These errors lead to user frustration, increased drop-offs, and higher support queries. ### Common Errors Encountered: - **CAMS Validation Errors** - **CAMS Authentication Errors** - **KFIN Validation Errors** - **KFIN Authentication Errors** A comprehensive analysis of these errors is documented [here](https://docs.google.com/spreadsheets/d/1CZb4S4mbcpAM-oEOeQ9nx_Z8iG_5YhfQvAajhIE0IGc/edit?gid=1944442342#gid=1944442342). ## Objectives - **Reduce Drop-offs:** Minimize user abandonment during the pledge step due to errors. - **Enhance User Experience:** Provide clear, actionable error messages and guidance. - **Decrease Support Queries:** Lower the volume of customer support requests related to pledge errors. - **Improve Conversion Rates:** Increase the number of successful pledge completions. - **Efficient Error Resolution:** Shorten the time required to resolve pledge-related errors. - **Optimize Sanction and Disbursement TAT:** Reduce turnaround time for sanction and disbursement processes. ## User Journey The Volt Money loan process involves the following key steps: 1. **Login** 2. **PAN Verification** 3. **Fetch Folio** 4. **Eligibility Assessment and Lender Assignment** 5. **KYC Verification** 6. **Bank Account Verification** 7. **Mandate Setting** 8. **Asset Pledge** 9. **KFS and Documentation** 10. **Loan Agreement Execution** ## Success Metrics - **Drop-off Reduction:** Decrease in user drop-offs at the pledge step. - **Support Query Reduction:** Fewer customer support queries related to pledge errors. - **Escalation Minimization:** Reduction in escalations and negative public feedback. - **Conversion Rate Improvement:** Higher rates of successful pledge completions. - Increased authentication success rates. - Increased validation success rates. - **Resolution Time:** Shorter time to resolve pledge-related errors. - **Retry Attempts:** Fewer repeated user attempts to complete pledges. - **Turnaround Time (TAT):** Reduced sanction and disbursement TAT. ## Competitive Analysis *Currently, no specific competitors are detailed. This section can be expanded based on market research.* ## Solution ### Requirements Overview ### 1. Portfolio Refresh Prompt - **Trigger:** User lands on the pledge landing page. - **Condition:** Last fetch date for both RTAs is older than 72 hours. - **Action:** -

---

## #42 — LAS CMS Lodgement
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

## #43 — LAS CMS Unlodgement
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

## #44 — Unpledge - Stocks selection logic
**Status:** Completed | **Last edited:** Unknown

**Solution:**
?**

---

## #45 — Sameer Minde Vaibhav
**Status:** Unknown | **Last edited:** Unknown

# Sameer Minde <> Vaibhav Meeting Notes: Preliminary Notes: **Step 1: User requests lien removal from app** - Volt sends email to Bajaj ops. - Zendesk ticket is created - Ticket is created for collateral team at BFL - User is communicated that request is being processed - On Volt app, securities are not removed from Holding statement, but not removed from BFL LMS. **[Need to review this, if we should remove]** - User is shown a lien removal in progress task **Step 2: Request is processed by collateral team** - Request is processed by collateral team - Collateral is removed from LMS - How is holding statement updated? - How is task closed? **Step 3: Request is submitted to AMC** - It take 2-3 business days for AMC to remove lien. - Beyond this not possible to track Amount level selection of folio that can be pledged, this becomes a request which is sent to BFL via email That created a ticket in their CRM if sent before 7 PM on T0, T+1 they send letters to RTA (physical lien removal letters) CAMS and Kfintech T+1 5 PM they get timestamped acknowledgement (BFL) on request they send this acknowledgement to volt. Follow up is sent to BFL for this acknowledgement Important: keep pending requests in a separate section discovery of which is somewhat behind steps so that it is not very apparent to the customer. T+3/T+4 Lien removal happens they get CAMS or KFIN data dump (lien status) Kfin (lien marked date and lien unmarked date)

---

## #46 — Term Loan Unpledge Eligibility API(Post loan creat
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

## #47 — Term Loan Unpledging
**Status:** Unknown | **Last edited:** Unknown

# Term Loan: Unpledging **Pre Loan A/C creation:** 1. If user pledges their collateral but does not proceed with the loan account creation then after 90 days from pledging we will initiate unpledging of the collaterals. The unpledging of the collaterals will be an Ops driven process. 2. If before 90 Days, user reaches out to us to unpledge their collateral instead of going ahead with the loan account creation then Ops will initiate the unpledge on the customer’s request. Customer won’t bear any charge(In V0) for getting their collaterals unpledged. In both the above cases the Ops process remains the same as OD. Ops team will be uploading the collateral unpledge file(Data team will be providing the collateral file to Ops) through the Bulk Upload option on the Command Centre. There won’t be any change in the file type, processing of the bulk upload and further process executions for unpledging of collaterals related to Term Loans. **Post Loan A/C creation:** - Loan Foreclosure: In case user Forecloses the Loan then the unpledging request will go through the non-STP flow same as it is currently happening in OD Loan Foreclosure. - If customer forecloses all the tranches before the expiry of the Facility/Loan tenure, we won’t initiate the collateral unpledging automatically. - If customer takes the first drawdown and closes/cancels the tranche during the Cool-off period then we won’t be unpledging the collaterals automatically until loan foreclosure or Facility(Loan) tenure expiry. Post Cool-off tranche cancellation three cases arise: 1. Customer proceeds to foreclose the Loan: Unpledging request will go through the non-STP flow as currently happening in OD Loan Foreclosure. 2. Facility/Loan Tenure expires: This has currently not happened for OD product as well and no process is in place currently. Hence not a part of V0, we can take this up in V2. 3. Customer requests for collateral unpledging from LSP: If there is a Loan level outstanding then the flow is discussed in Partial Unpledging. If there is no Loan level outstanding then the user will be able to select the fund/s they want to unpledge and raise the request for the same(User can raise the unpledging request either in one go or in multiple times). Once the user raises the unpledge request/s through the LSP to DSP it will either go through the STP or nSTP flow, described below. - Partial Unpledging: Customers can only initiate partial

---

## #48 — Analytics requirement Revocation request
**Status:** Unknown | **Last edited:** Unknown

# Analytics requirement: Revocation request | | **T0** | **T-1** | **T-2** | T-2 | T-3 | T-4 | T-5 | T-6 | T-7 | | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | | Number of revocation requests | (count of total revocation requests made today) | | | | | | | | | | Number of revocation requests automatically closed | (count of requests made and settled today) | | | | | | | | | | Number of revocation pending closure | (Count of requests made today but pending closure) | | | | | | | | | | | **Today** | **This week** | **This month** | | | | | | | | Average closure TAT | For requests closed today avg(closed_on - created_on) - difference of hours | | | | | | | | | | % requests settled automatically | % of requests that were settled closed today (identify requests settled manually via admin action) | | | | | | | | | ## Tables and Important fields: ### Table: Credit_applications.default.revocationrequests ### Field: revocationrequest: created_on - When payment was created revocationrequest: settled_on - When payment was settled automatically revocation requests status (If equals to closed - request was closed either using admin action or automatically) ### Table: admin_action_audit admin action name: CLOSE_REVOCATION_REQUEST To identify which requests were closed manually Format: Email with CSV attached Recipients: @Vaibhav Arora @Lalit Bihani @Ranjan kumar Singh @Ankit Agarwal @Bharat Lamba @Nishant Athmakoori @Saksham Srivastava

---

## #49 — Cancel unpledge request
**Status:** Solutioning pending | **Last edited:** Unknown

# Cancel unpledge request Classification: Cancel unpledge Notes: User asked to cancel unpledge request, understand why this happened? User decided to not do it? PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13889 Status: Solutioning pending

---

## #50 — I have a ticket open for unpledge ”
**Status:** PRD pending | **Last edited:** Unknown

# """I have a ticket open for unpledge""” Classification: Unpledge request status Notes: User asked for the status of their unpledge request PRD/Solution mapping: PRD under progress Platform: Wati Reference Link/ID: 919437780780 Status: PRD pending

---

## #51 — User’s pledging failed for Karvy and when they ret
**Status:** Solutioning pending | **Last edited:** Unknown

# User’s pledging failed for Karvy and when they retried, we charged the user processing fee twice without withdrawal - Tata Classification: Karvy pledging issue Notes: Check with Karvy why pledging failed, we should have updated our creditapplication data automatically on pledge failure PRD/Solution mapping: Pending Platform: Zendesk Reference Link/ID: https://volt7307.zendesk.com/agent/tickets/13013 Status: Solutioning pending