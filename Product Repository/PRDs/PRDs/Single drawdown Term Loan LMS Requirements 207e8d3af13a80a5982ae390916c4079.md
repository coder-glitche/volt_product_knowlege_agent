# Single drawdown Term Loan: LMS Requirements

: Priyamvada S
Created time: June 3, 2025 12:00 PM
Status: In progress
Last edited: August 9, 2025 11:23 AM
Owner: Priyamvada S

# **What problem are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Lack of lifecycle borrowing behaviour:** Users do not engage in re-borrowing after repayment, resulting in limited customer lifetime value (LTV).

---

# **How do we measure success?**

### **1.Product Metrics (LOS)**

Measured at an overall as well at an individual LSP level

**Adoption & Conversion** 

L1

- **% of eligible users initiating term loan sign-up**
    - ‘Initiation’ refers to the first API call made by LSPs to DSP, which may occur at the MFC fetch, offer generation, or opportunity creation stage.
- **% of initiated users completing onboarding** (from initiation to loan account creation)
- **P95 onboarding TAT** (time from initiation to loan account creation)

L2

- Daily % of users initiating each milestone step (KYC, Bank Verification, Mandate Setup, Agreement Signing), and among them:
    - % who successfully completed the step
    - % who were rejected at the step
    - Error code distribution at each step
    - % who retried the step at least once
    - Median & Avg no of retries at the step
- Avg & P-95 TAT (initiated to success/failure)across each of the journey milestone step

**~~Product Utilisation~~**

- ~~Repeat drawdown rate ( *%users who take >1 drawdown within a line)*~~
- ~~Average and median number of drawdowns per user per line~~
- ~~Avg & Median utilisation rate per drawdown~~
- ~~% of eligible limit utilised per user segmented by aging buckets (e.g., at 30, 90 etc days from line creation)~~
- ~~Average time interval (in days) between successive drawdowns per user~~

### **2.Business Metrics (LOS)**

- % of onboarded LSPs who have gone live with Term Loan product
- LSP-wise distribution of loan applications initiated across OD and Term Loan (SD&MD)
- T~~otal Term Loan AUM per LSP (as % of total DSP Term Loan AUM)~~
- ~~Median term loan ticket size per LSP~~
- ~~%Active term loans per LSP~~

# **How are others solving this problem?**

NA

# **What is the solution?**

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
- Future drawdowns (ie top up loans) will map to the same line but appear as new loans.

This enables:

- Abstraction of backend complexity
- Future-readiness for reborrowing from the same line

## User Journey/ Requirements (LOS)

                        ****

![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/image.png)

                                  **  LOS JOURNEY FOR V0**

## **Step 1: MF Fund Fetch**

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdyBPzPEGuLwpHn2DWMvwwBUlpMbGeF-iwUrSYY8D-dJmjys3b4wVymzGFhOQZHY8O4sKZXtYgC4gxE-kLQVidlSRltTPeAN6wX8eHTDWS6pPLH1e50dJ4z-b-PTwgOb1QWIJ6T?key=IMeOW9gZebz0hJgmfrnt6A)

Description:

User logs into the LSP application with their mob no, OTP verifies it and enter their PAN number along with other details that LSPs deem required. 

Post details submission, the MF fetch flow is triggered in the backend by the LSP & user is prompted to provide OTP-based consent to allow access to fetch their mutual fund portfolio.

Step scope:  Typically done during the first drawdown or for ad-hoc enhancements, but LSPs can execute it at either the line or loan level at their discretion.

**LSP Backend flow**

Two models exist for LSPs

- LSPs use their own MFC/RTA fetch APIs:
    - MF fund details are returned.
    - However, eligibility, fund-level LTV / NAV and drawing power are not available.
    - To access this data, the LSP must hit DSP’s offer generation API.
- LSPs use DSP’s wrapper APIs:
    - LSP shares the user’s PAN and mobile number.
    - DSP returns:
        - List of eligible funds with LTVs.
        - List of ineligible funds (unapproved/others).
        - Summary of total portfolio value, eligible fund value, and overall eligible limit.

Step Scope: Applicable at the loan only and is executed each time a new loan is created—whether for the same product or a different one.

- Note: New loan creation for the same product can only occur if previous loan is closed

Specific Partner flows

Paytm: Using their own fund fetch APIs instead of relying on DSP’s wrapper API for MF fetch

DSP Backend Flow

LSPs hitting DSP’s MF fetch wrapper APIs will receive the total portfolio value, eligible fund value, and overall eligible limit.

Step Scope: Applicable at the loan level only

**Edge Cases: NA**

**Delta from Current Capabilities: NA**

## ***Future Scope***

NA

## **Step 2: Client Dedupe**

## ***VO Scope***

**Frontend Experience: NA**

**LSP Backend flow:** 

LSP calls DSP’s client dedupe API with customer PAN and product type (e.g., LAS_TermLoan_SD) to check if an active line exists for the same ‘PAN + Product type’ combo.

- If the line is inactive, the journey continues.
- If the line is active, the application is blocked.

‘Product type’ value configuration for the multi-drawdown term loan construct: LAS_TL_SD

Following table illustrates the dedupe logic across different product type combinations:

| **Supported Product Pairings** | TL_MD(CRED) | TL_SD(Paytm) | OD(Volt) |
| --- | --- | --- | --- |
| TL_MD(Paytm) | N | Y | Y |
| TL_SD(Volt) | Y | N | Y |
| OD (Groww) | Y | Y | N |

Step Scope:The dedupe logic applies at the Loan **level** 

**DSP Backend Flow:**

DSP on receiving the customer’s ‘PAN & product’ type from LSP , performs dedupe to accept/reject the client

Step Scope:The dedupe logic applies at the **loan level** 

**Edge Cases: NA**

**Delta from Current Capabilities: NA**

## ***Future Scope***

NA

## **Step 3: Overall Eligible limit determination**

## ***V0 Scope***

**Frontend Experience**

Post successful fund fetch, user is shown their list of eligible/non eligible mutual funds along with an overall credit/loan eligibility in LSP UI as a total available loan limit

User can then choose to pick their desired first loan drawdown amount(≤available loan limit) using the slider UI

![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/image%201.png)

**LSP Backend flow**

LSP determines the list of eligible/ineligible funds along with overall eligible limit using  DSP’s ‘Offer generation’ api which will return the following based on the inputs received:

- If LSPs share the list of MF funds and user PAN:
    - Get the overall eligible loan limit.
    - Receive min and max supported values for parameters like tenure, interest, fee [(**list here](https://docs.google.com/spreadsheets/d/1e9TUa7HzIL87ExWvZ3DjmbXA9uZDPBOxPfZy_jICgJs/edit?gid=1933961055#gid=1933961055)).** These parameters apply at **a line level** and act as bounds for all loan drawdowns

However, LSPs can skip this API if they are using DSP's wrapper APIs (V2), as the same details are returned via the wrapper itself—provided that interest rates, charges, and tenure (min/max) configurations have been pre-aligned offline.

Note: DSP does not support offline NAV/LTV updates via file sharing due to legal constraints under its CMOD vendor agreement. Hence, LSPs must either use DSP’s wrapper fetch API or combine their own fetch APIs with DSP’s offer generation API for eligibility amount determination

Step Scope: ‘Eligibility determination’ apply at the loan level

**Specific Partner flows**

Paytm:  Will independently calculate eligible limits using DSP’s offline eligible fund list and NAV updates from the MFC fetch API, without relying on DSP’s offer generation API.

**DSP Backend Flow**

DSP supports eligibility limit determination directly via ‘offer generation’api and via ‘MFC fetch wrapper’ APIs as well 

Step Scope: ‘Eligibility determination’ apply at the loan level

**Edge Cases:** 

In case user drops off post eligibility determination and resumes flow later, its recommended to LSPs to use DSP’s offer generation api to get the updated NAV/LTV values

**Delta from Current Capabilities**

- Need to support custom LTVs passed on by partners for overall eligible limit determination
    - LTV ≤ DSP-defined value for that fund.If valid, DSP uses passed LTVs to calculate eligibility.
    - If invalid, DSP rejects and provides reason with original DSP eligibility.

## ***Future Scope***

 ****Support LSPs in receiving global NAV/LTV updates from DSP to compute eligible limits on their end  with their fetched funds and skip the offer generation API

## **Step 3: Term Loan offer generation**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZAjo3Du5Han0b22uKIg6g9J-4U5czI2xf5WiQ2GGtgNbxTb4cX9PqRpsJR8YrvOKQpPC5B27p90WChQcPTD-81x9mViZNVnJ_9n8DBdzsSIKrROvttEfoecig6SDF3RPBOu8w?key=IMeOW9gZebz0hJgmfrnt6A)

Once the user selects the first loan drawdown amount(less than or equal to their eligible limit), they are presented with 2–3 loan offer combinations. Each combination includes a tenure, interest rate,  and EMI. The user can then choose their preferred offer.

**LSP Backend flow**

Description: LSPs generate offers on their end using an offline-aligned policy that mirrors DSP’s logic for EMI calculation and valid loan parameters (e.g., interest rate, tenure)

Step Scope: ****Applies at the **loan level** (for each drawdown)

**Specific Partner flows**

Paytm generate offers on their end using pre-aligned offer logic.

**DSP Backend Flow: NA**

**Edge Cases: NA**

**Delta from Current Capabilities:** NA

## ***Future Scope***

**Term Loan Offer Generation via DSP:**  LSPs can trigger DSP’s backend with the user-selected loan amount, upon which DSP’s internal engine returns 2–3 valid combinations of tenure, interest rate, and EMI, all within the configured parameter bounds.

For example, if the user’s eligibility is ₹5L but they opt for ₹3L, DSP will generate appropriate offers based on the selected amount.

## **Step 4: Lead journey tracking**

## ***V0 Scope***

**Frontend Experience: NA**

**LSP Backend flow**

Description: 

Once user proceeds with an offer at LSP’s end,  LSPs need to hit DSP’s backend to create an unique opportunity in the backend to track the status of this lead through all downstream stages such as KYC, mandate, agreement, pledging, etc.  

Step scope: All stages tracked at a loan level 

**Specific Partner flows**

Paytm: NA

**DSP Backend Flow**

While pledging is tracked at the loan level by the LSP, the pledged assets will be mapped to the line in DSP’s backend

Note: Subsequent loans or top up loans is not supported in V0  

**Edge Cases: NA**

**Delta from Current Capabilities**

In the current construct,  all journey stages are tracked at a line level and hence needs to be tweaked to support loan level tracking for all stages

bank a/c verification ,KFS & agreement signing will be at a loan level only

## ***Future Scope***

Explore skipping KYC, Additional Details (excl. Purpose of Loan), and Mandate Setup for  top-up loans ie execution of these flows only at a line level in DSP BE POV or only on first loan from LSP’s /customer’s POV

Note: KYC validity is 3 year .If Video KYC done, this can be extended to 10 years

## **Step 5: KYC**

## ***V0 Scope***

**Frontend Experience**

The KYC journey for the user includes selfie capture, CKYC-based document fetch and matching, and fallback to Digilocker in case CKYC fails. 

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSbrF8TIShK4BVJJzDKE8ifx8EuoY_y-qBKZX-ee2vw8O08lM7m8VNrC5nwDZAOHddY4fgHtIu_NWn2SDHEQZh-C5TSmTno-TrsKNK2FOtRR2eRspFzQhLVjn8RxpZ8EAhKLGdTw?key=IMeOW9gZebz0hJgmfrnt6A)

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHxbK81ggCJuBhmFoAbl7msLaQTslyE4FqjdgfKMzfAY4bVjHlPAKJE4P0waiopyFB3ib9vN6uoZ-_e8dnrfVTpaFnRslgQieJelyg8FhSqLTeo_s5yGf69MivIsCBFY73476wXg?key=IMeOW9gZebz0hJgmfrnt6A)

**LSP Backend flow:**

Two integration options are supported:

a) LSP using DSP CKYC Wrapper APIs+ DSP Digilocker redirection:

- LSP captures selfie and sends PAN, Name, DOB, and selfie to DSP.
- DSP performs liveliness check.
    - If it fails, DSP sends selfie retry response to LSP.
- If successful, DSP returns CKYC wrapper API endpoint for OTP validation and document fetch.
- Post successful OTP verification & document fetch, DSP checks document validity and performs name + face match.
    - If either fails, DSP shares Digilocker redirection URL with CKYC status as 'failed'.
- Upon successful Digilocker attempt by the customer, DSP receives the documents and performs face match against the previously submitted selfie.

b) LSP using DSP’s CKYC SDK +  DSP Digilocker redirection::

Two scenarios supported here for CKYC SDK:

- LSP can either pass on just the opportunity ID & mob no to DSP for it to initiate the CKYC UI flow starting with collection of PAN inputs, NSDL PAN verification, selfie & CKYC
- Alternatively, LSPs can pass PAN, Name, DOB, and Opportunity ID for DSP to trigger PAN verification via NSDL in the backend, while selfie capture happens via DSP SDK, followed by CKYC initiation and data/face matching

Step scope: KYC is to be done at the **loan level**. 

**Specific Partner flows**

Paytm:  

- Will not support DSP’s deviation flow in V0 for low face/data match thresholds.

DSP **Backend flow:** 

- Flow same as above
- Step scope: KYC is to be done at the **loan level**.
- DSP will be the source of truth for liveliness, KYC name, and face match—performing these checks internally, with LSPs relying on DSP's response for approval or rejection

**Edge Cases:** NA

**Delta from Current Capabilties:** Support for CKYC flow (applies to both OD & TL)

## ***Future Scope***

- Enable LSP to perform liveliness, name matching & face matching at their end by pre-aligning the  logic &  thresholds . However, KYC data (CKYC/Digilocker) must still be fetched via DSP APIs due to RBI compliance requiring REs to perform KYC
- Explore skipping KYC for  top-up loans ie  only at a line level in DSP BE POV or only on first loan from LSP’s /customer’s POV  as long as KYC validity is not expired

## **Step 6: Additional Details Capture**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFQn24rfZp69AynfBzTi7E7hlT1H45YycAVByqDMOzSIDidB_I6B0dMbBE_JVbUWiF75fOdedDt3J9AWIiHxIsoYXVlYYNHO87oQgqgIhwvQHcLcWDRyZwNuiqXrOQvKzYtcn0ZA?key=IMeOW9gZebz0hJgmfrnt6A)

After successful KYC, the user is prompted to enter additional personal details. These fields include father's first and last name, income bracket, employment status, Educational qualification, purpose of the loan, confirmation on whether current address is the same as permanent address

**LSP Backend Flow** 

Description:

- The LSP is expected to call DSP’s ‘Save Additional Data’ API and pass the above-collected user data along with the user's consent flags.
- Following are the mandatory fields for this API:
    - Father's first & last name
    - Purpose of loan
    - Income range
    - Employment status

Step Scope :This step is to be executed for every loan

**Specific Partner flows**

Paytm: None

**DSP Backend Flow**

- Flow : Same as above
- Step Scope :Every field to be captured at a loan level

**Edge Cases: NA**

**Delta from Current Capabilities: All fields to b**e captured at a loan level 

## ***Future Scope***

Explore skipping ‘Additional details’ (except ‘Purpose of loan’) for  top-up loans ie instead capturing  only at a line level in DSP BE POV or only on first loan from LSP’s /customer’s POV

## **Step 7: Bank Account Verification**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWmRU9OwFEMH8QKl5gUywBMmXGKkLFhaEwSy_FGi2jRF2_ykQRjVVnO95gqG9Fgg4oNUvl9ZIcCSis8Toauusaz8yx190i-eQNwZgVmwFSm3HQ9mRmSVnCHB_eadBX3LLh45fr?key=IMeOW9gZebz0hJgmfrnt6A)

The user either sees their pre-filled bank account information or enters it manually. On submission, penny drop and name match checks are run. If the verification fails, the user is prompted to retry /update bank a/c depending on the error code (in case of penny drop) or provide additional documents (in case of name match failures) by the LSP

**LSP Backend Flow** 

LSP calls DSP’s ‘Bank Utility Init’ API with bank account details.

- DSP performs a penny drop (₹1 transfer) and if rejected, the reason is passed along to LSP to prompt the user to retry  with same or alternate bank a/c depending on the error code
- On penny drop success, the name returned by the bank is matched against Aadhaar/PAN name by DSP
    - If name match score is ≥ 90%, verification succeeds.
    - If the score is below threshold, verification status is marked as DEVIATION and shared with LSP. DSP expects LSPs to share supporting documents (cancelled cheque/passbook/etc.) to proceed in such cases.

Step Scope :Executed at loan level

**DSP Backend Flow** 

Flow: DSP performs penny drop and name match logic at their end and shares verification result with LSP to action on ie DSP serves as the source of truth for both penny drop & name match verification

Step Scope : Executed at loan level

**Edge Cases: NA** 

**Specific Partner flows**

Paytm:  Will not support DSP’s deviation flow in V0 for low name match thresholds.

## ***Future Scope***

- Support for LSPs to do penny drop & name match verifications at their end, provided logic and threshold is aligned with DSP
- Explore skipping ‘Bank a/c setup’ for  top-up loans ie execution of these flows only at a line level in DSP BE POV or only on first loan from LSP’s /customer’s POV as long as a/c is active

## **Step 8: Mandate Setup Flow**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerC8uLsAMdbcN-6MaGoHtLsdBuVCrO8PSRHthkoFpkjlhptehtTnXKJv6WyMMJcOoCNuzL6gCkAknxO5SJiWctgSq_9EFDYR_oJqlWdpn-5XzvE0IyI_MJr3r3pTxcVx_gh8hBuQ?key=IMeOW9gZebz0hJgmfrnt6A)

## ***V0 Scope***

**Frontend Experience**

User selects the mode of mandate registration – UPI Autopay or e-NACH and reviews displayed loan amount, EMI payment date, tenure and EMI amount . User is then redirected to either LSPs/DSPs mandate set up flow.On successful setup, a confirmation screen is displayed.

**LSP Backend Flow** 

Flow: Two scenarios 

- LSP uses DSP’s mandate set up  flow by hitting DSP’s Create Mandate API with the following:
    - Opportunity ID
    - Mandate limit: Set by the LSP, but subject to DSP validation and approval
    - Mandate type:  UPI or e-NACH
    - Mandate presentation date:  **:** Only one presentation date is supported per customer across all loans, though different customers can have different dates
- DSP returns the Digio SDK URL or redirection link for LSPs user to complete the flow
    - LSP uses their own mandate set up flow and uses webhook to post the registration update on our API.

Step Scope: Mandate set up done at a loan level

Partner Specific Flows

Paytm: Using their own mandate setup flows via PA/PG.

- Must send webhook to DSP on successful registration.
- Must share T+1 MIS for reconciliation.
- Logic for mandate limit amount for Paytm : TBC

**DSP Backend Flow** 

Flow:

- DSP’s UPI mandate setup to be supported in V0  with required changes in registration api, if any

Step Scope: Mandate set up done at a loan level

**Edge Cases**

UPI mandate may not be created on the same account as the disbursal account, creating repayment risk (P+I)

**Delta from Current capabilities:** Support for multiple mandate types is new (applicable for both TL &OD)

## ***Future Scope***

- Support for multiple mandate presentation across loans per customer
- Support for multiple active mandates at a line level (both UPI & eNach supported)
- DSP ‘Mandate limit’ logic configuration to be done

## **Step 10: Pledging**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeb9n3NaAi-iw9-HWr-YCvnSxh7WVS4-dr4wP7n4eeR2b-35Uzv9gUpkBArJimH7lvVX_2GpsT12J5MQEvgd6sfoZUYrZ7U0teZSkd6f65_iAoeZzXIgMRpsNLlt0YPdGTqMWyIJg?key=IMeOW9gZebz0hJgmfrnt6A)

**LSP Backend Flow**

- Two scenarios:
    - LSPs can either hit our Pledge wrapper APIs with their fund units and get the pledge status at a fund level
    - LSPs can use their Pledge APIs but with DSP’s child credentials (To be finalised) as DSP ultimately needs to own the pledge flow
- Step Scope **:** Pledging process executed at a loan level

Partner Specific Flows

Paytm: To use our Pledge wrapper APIs

**DSP Backend Flow**

- Flow: Same as above
- Step scope: Pledging mapped to a line in DSP’s backend

**Edge Cases: NA**

**Delta from Current capability:** Support for pledge execution at a loan level 

## ***Future Scope***

NA

## **Step 11: KFS & Agreement Signing**

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVE4iIiD3sbD8MnHsSOO-7gNPZlQW8w_qp7_drG8zlZJGkYw2M4-zjPPbNDtBNVZnqf1atjRzjmKSwsVxWmZkNsz0QlmHd5Nq9mAy7jvOx5bFJngAEjjTk_TUV0_8OrAGFMVNi6g?key=IMeOW9gZebz0hJgmfrnt6A)

User reviews and digitally signs the agreement &  KFS document(both click-wrap based).

**LSP Backend Flow**

Two step process:

Step 1: Validation of LSP’s term loan offer

LSPs who are calculating offers at their end will be sharing the offer chosen by the user for the first time at this stage.They need to share the following parameters:

- Loan amount
- Tenure
- Interest rate
- EMI

DSP at their end will first validate the first 3 values at their end (ie are they within the permissable range set for the line).If yes, we will validate the EMI using DSP’s internal offer generation engine (ie PMT calc for EMI).If yes to both, DSP will proceed to step 2.

In case of rejection wrt any of the parameters we reject the offer and share the response to LSP

Step 2: Contract generation/signing

a) LSP uses DSP generated  KFS & agreement PDF and renders it in their UI for customer  digital consent (click-wrap) and shares signature metadata (IP + timestamp) with DSP.

b)  LSP uses DSP’s redirection link for agreement /KFS review & signing:

- Link hosts KFS &  Agreement . On user acceptance (via click-wrap), DSP captures the consent details

Step Scope: KFS ,Sanction letter & agreement to be generated at a loan level

Note: For the first loan drawdown, all 3 will be generated (KFS,Sanction letter & Agreement) and need to be reviewed/accepted by the customer 

**Specific Partner Flows**

Paytm: 

- Generates KFS and agreement at their end and share digital consent metadata with DSP.\
- Aligned to send flat values to DSP even for % based charges in V0

**DSP Backend Flow**

Need to support the generation of KFS , Sanction letter & Master agreement at a loan level

**Edge Cases: NA**

**Delta from Current capabilities**

- Support for term loan offer generation engine to validate the offer details passed on by LSP
- Generation of KFS , Sanction letter & Master agreement at a loan level

## ***Future Scope***

- Explore how to optimise the flow in case of offer mismatches (eg: modified offer instead of straightaway rejections)

## **Step 12: Loan Account Creation**

## ***V0 Scope***

**Frontend Experience:** 

![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/0ef8af1d-6ecf-44d9-936f-60b8668da74d.png)

User sees a loader screen indicating that the disbursement process has been initiated and is in progress.

**DSP Backend Flow**

- Flow: LSP hits DSP’s backend after all onboarding steps (KYC, Bank, Mandate, Agreement, etc.) are completed. API validates the following before creating  loan & line entities:
    - KYC completion
    - Agreement signed
    - Mandate registered
    - Bank verification
    - Photo, email, and mobile verified
    
    If all validations pass, DSP creates:
    
    - Client ID
    - Line ID
    - Loan ID

Note: Only loan entity will be exposed to the LSP

- **Step Scope: All except Pledging to be done at a loan level**

**Edge Cases: NA**

**Specific Partner Flows(Paytm): NA**

**Delta from Current Capabilities:**  Loan a/c creation will create both a line and loan account 

## ***Future Scope***

NA

# **Design**

CKYC redirection/SDK flow: 

Agreement & KFS redirection/SDK flow: TBC

eNach & UPI mandate  redirection/SDK flow: TBC

# **Analytics**

LSP level view of journey stages  api status (initiated, sucessfull, rejected with error codes, retries) wrt the following stages:

- **MF Fund Fetch**
- **Client Dedupe**
- **Overall Eligible Limit Determination**
- **Term Loan Offer Generation**
- **Lead Journey Tracking & Mapping**
- **KYC**
- **Additional Details Capture**
- **Bank Account Verification**
- **Mandate Setup Flow**
- **Pledging**
- **KFS & Agreement Signing**
- **Loan Account Creation**

---

# **Timeline/Release Planning**

---

# **Go to market**

## Marketing

## Ops & Sales training

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - [ ]  -
- [ ]  Business
    - [ ]  -
- [ ]  Design
    - [ ]  -

---

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

# **Feedback**

---

# **Learnings & Next steps**

---

# **Appendix**

## Meeting notes