# Term Loan: LOS requirements

: Priyamvada S
Created time: August 9, 2025 2:23 PM
Status: In progress
Last edited: May 14, 2026 10:50 AM
Owner: Priyamvada S

# **What problem are we solving?**

- **Low awareness of line-based lending products:** Most Indian consumers do not understand the concept of a reusable credit line or overdraft (OD)-style borrowing.
- **Poor use of the product as a one-time loan:** Even when users opt in, they typically draw down only once and never return, leading to poor utilization of the approved credit limit.
- **Lack of lifecycle borrowing behavior:** Users do not engage in multiple drawdowns or reborrowing after repayment, resulting in limited customer lifetime value (LTV).
- **Ineffective product positioning:** The existing product framing fails to communicate flexibility, leading to poor adoption and underuse.

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
- LSP-wise distribution of loan applications initiated across OD and Term Loan products(SD&MD)
- T~~otal Term Loan AUM per LSP (as % of total DSP Term Loan AUM)~~
- ~~Median term loan ticket size per LSP~~
- ~~%Active term loans per LSP~~

# **How are others solving this problem?**

NA

# **What is the solution?**

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
- DSP manages the **loan** as the credit container; **each tranche** is a separate drawdown linked to it.
- Multiple **active tranches** can exist simultaneously, each with its own amount, tenure, and repayment.
- On full **repayment of a tranche,** the loan limit is replenished, enabling **re-borrowing**.

This enables:

- A **term-loan-style UX** for each drawdown.
- Centralised collateral management via the loan with clear LSP visibility into both loan and tranche lifecycles.

## User Journey/ Requirements (LOS)

### **First drawdown**

![image.png](Term%20Loan%20LOS%20requirements/image.png)

                   **LOS JOURNEY V0: 1st Drawdown** 

## **Step 1: MF Fund Fetch**

## *V0 Scope*

- **Frontend Experience:**
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdyBPzPEGuLwpHn2DWMvwwBUlpMbGeF-iwUrSYY8D-dJmjys3b4wVymzGFhOQZHY8O4sKZXtYgC4gxE-kLQVidlSRltTPeAN6wX8eHTDWS6pPLH1e50dJ4z-b-PTwgOb1QWIJ6T?key=IMeOW9gZebz0hJgmfrnt6A)
    
    Description:
    
    *First drawdown*
    
    User logs into the LSP application with their mob no, enters their PAN number along with other details that LSPs deem required (pincode etc) 
    
    Post details submission, the Mutual fund fetch flow is triggered in the backend by the LSP & user is prompted to provide OTP-based consent to allow access to fetch their mutual fund portfolio.
    
- Backend Experience
    
    ***First drawdowns:***
    
    LSP Backend flow 
    
    Description: 2 options exist for LSPs
    
    - LSPs use their own MFC/RTA fetch APIs:
        - MF fund details are  returned.
        - However eligible fund list, their LTV / NAV values and drawing power maintained by DSP are not available.
        - To access this data, the LSP must hit DSP’s offer generation API.
    - LSPs use DSP’s wrapper APIs:
        - LSP shares the user’s PAN and mobile number.
        - DSP returns:
            - List of eligible funds with LTVs.
            - List of ineligible funds (unapproved/others).
            - Summary of total portfolio value, eligible fund value, and overall eligible limit.
    
    **DSP Backend Flow**
    
    Description: LSPs hitting DSP’s MF fetch wrapper APIs will receive the total portfolio value, eligible fund value, and overall eligible limit.
    
- **Specific LSP flows**
    
    **Cred: Using** their own fund fetch APIs instead of relying on DSP’s wrapper API for MF fetch
    
- **Edge Cases**
    
    **NA**
    

## ***Future Scope***

NA

## **Step 2: Client Dedupe**

## ***VO Scope***

- **Frontend Experience**
    
     **NA**
    
- Backend Experience
    
    ***First drawdown/tranche*** 
    
    LSP Backend flow
    
    LSP calls DSP’s client dedupe API with customer PAN and product type (e.g., LAS_TL) to check if an **active loan** exists for the same ‘PAN + Product type+LSP’ combo
    
    - If the loan is inactive, the journey continues.
    - If the loan is active, the application is blocked.
    
    Following table illustrates the dedupe logic across different product type combinations:
    
    | **Supported Product Pairings** | TL_MD(CRED) | TL_Volt | TL_MD(Paytm) |
    | --- | --- | --- | --- |
    | TL_MD(Paytm) | Y | Y | N |
    | TL_Volt | Y | N | Y |
    | TL_MD (CRED) | N | Y | Y |
    
    Note: 
    
    ‘Product type’ value configuration for the multi-drawdown term loan construct: LAS_TL
    
    This logic is only applicable for TermLoan and not for OD  (ie if user has an OD from Cred, they cannot take an OD from Paytm ie current dedupe  logic of OD continues to exist for OD )
    
    **DSP Backend Flow:**
    
    DSP on receiving the customer’s ‘PAN & product’ type from LSP , performs dedupe to accept/reject the request
    
- **Edge Cases**
    
     **NA**
    

## ***Future Scope***

NA

## **Step 3: Overall eligible limit determination /Offer Gen API**

## ***V0 Scope***

- **Frontend Experience**
    
    ***First drawdown***
    
    Post successful fund fetch, user is shown their list of eligible/non eligible mutual funds along with an overall credit/loan eligibility in LSP UI as a total available loan limit
    
    User can then choose to pick their desired first tranche drawdown amount(≤available loan limit) using the slider UI
    
    ![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/image%201.png)
    
- Backend Experience
    
    ***First drawdown***
    
    LSP Backend flow
    
    LSP determines the list of eligible/ineligible funds along with overall eligible limit using  DSP’s ‘Offer generation’ api which will return the following based on the inputs received:
    
    - Get the overall eligible loan limit.
    - Receive min and max supported values for parameters like tenure, interest, fee [(](https://docs.google.com/spreadsheets/d/1e9TUa7HzIL87ExWvZ3DjmbXA9uZDPBOxPfZy_jICgJs/edit?gid=1933961055#gid=1933961055)[**list here](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=636736939#gid=636736939)).** For ‘tenure ‘& ‘interest’ min /max ranges apply at a tranche level while fee consists of items that apply at loan/tranche level
    
    However, LSPs can skip this API if they are using DSP's wrapper APIs (V2), as the same details are returned via the wrapper itself—provided that interest rates, fee, and tenure (min/max) configurations for the tranche have been pre-aligned offline.
    
    Note: 
    
    - DSP does not support offline NAV/LTV updates via file sharing due to legal constraints under its CMOD vendor agreement. Hence, LSPs must either use DSP’s wrapper fetch API or combine their own fetch APIs with DSP’s offer generation API for eligibility amount determination
    - LSPs can compute eligible limits using their own LTV data sources( MFC/Morning star) and offline-aligned DSP fund lists with periodic LTV updates. However, this approach is discouraged, as it may lead to eligible  limit mismatches between LSP and DSP, causing offer rejections at the contract stage.
    
    DSP Backend Flow
    
    ***First drawdown***
    
    DSP supports eligibility limit determination directly via ‘offer generation’ api as well as ‘mutual fund fetch wrapper’ APIs as well 
    
- Specific Partner flows
    
    Cred:
    
    Need to support custom LTVs passed on by Cred for overall eligible limit determination 
    
    - LTV ≤ DSP-defined value for that fund.If valid, DSP uses passed LTVs to calculate eligibility.
    - If invalid, DSP rejects and provides reason with original DSP eligibility.
- **Edge Cases:**
    
    In case user drops off post eligibility determination and resumes flow later, its recommended to LSPs to use DSP’s offer generation api to get the updated NAV/LTV values
    

## ***Future Scope***

 ****Support LSPs in receiving global NAV/LTV updates from DSP to compute eligible limits on their end  with their fetched funds and skip the offer generation API

## **~~Step 3: Term Loan offer generation~~**

## ***~~V0 Scope~~***

- **~~Frontend Experience~~**
    
    ***First + Subsequent drawdowns:***
    
    Once the user selects the  loan drawdown amount(less than or equal to their eligible limit), they are presented with 2–3 loan offer combinations. Each combination includes a tenure, interest rate,  EMI and repayment schedule preview(optional). The user can then choose their preferred offer.
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcZAjo3Du5Han0b22uKIg6g9J-4U5czI2xf5WiQ2GGtgNbxTb4cX9PqRpsJR8YrvOKQpPC5B27p90WChQcPTD-81x9mViZNVnJ_9n8DBdzsSIKrROvttEfoecig6SDF3RPBOu8w?key=IMeOW9gZebz0hJgmfrnt6A)
    
- **~~Backend Experience~~**
    
    ***~~First + Subsequent drawdowns:~~***
    
    ~~LSP Backend flow~~
    
    ~~Description: LSPs generate offers on their end using an offline-aligned policy that mirrors DSP’s logic for EMI calculation and valid loan parameters (e.g., interest rate, tenure,PF)~~
    
    **~~DSP Backend Flow: NA~~**
    
- **~~Specific Partner flows~~**
    
    **~~Cred** generate offers on their end using pre-aligned offer logic.~~
    
- **~~Edge Cases~~**
    
    **~~NA~~**
    

## ***~~Future Scope~~***

**~~Term Loan Offer Generation via DSP:**  LSPs can trigger DSP’s backend with the user-selected loan amount, upon which DSP’s internal engine returns 2–3 valid combinations of tenure, interest rate,  EMI & PF all within the configured parameter bounds.~~

~~For example, if the user’s eligibility is ₹5L but they opt for ₹3L, DSP will generate appropriate offers based on the selected amount which are then shared with the LPS to display to users~~

## **Step 4: Lead journey tracking/Create Opportunity**

## ***V0 Scope***

- **Frontend Experience:**
    
    NA
    
- Backend Experience
    
    ***First drawdown:***
    
    **LSP Backend flow**
    
    Description: 
    
    Once user proceeds with an offer at LSP’s end,  LSPs need to hit DSP’s backend to create an unique opportunity in the backend to track the status of this request through all downstream stages such as KYC, mandate, agreement, pledging, etc  
    
    Below table below outlines the execution frequency for each journey step, specifying whether it applies at the loan (ie only on first drawdown) or tranche level (on every drawdown)
    
    | **Step** | Execution frequency |
    | --- | --- |
    | MFC Fund Fetch | Ad-hoc |
    | Client Dedupe | Loan |
    | Eligible Limit Determination (offer gen api) | Ad-hoc |
    | Term Loan offer Generation | Tranche |
    | KYC & Personal Details (incld Purpose of Loan) | Loan |
    | Bank a/c set up & verification | Tranche (optional) |
    | Mandate set up | Tranche (optional) |
    | Pledging | Tranche (optional) |
    | KFS +Sanction letter | Tranche |
    | Agreeement | Loan |
    | Term Loan offer Validation | Tranche |
    | A/c Creation | Tranche (tranche ID) + Loan(loan ID) |
    
    **DSP Backend Flow:** 
    
    On LSP hit, DSP backend creates an unique opportunity ID which is  shared with LSP to enable E2E tracking through the funnel.
    
    Note: While pledging is tracked /executed at the tranche level, the pledged assets will be mapped to the loan in DSP’s backend
    
- **Specific Partner flows**
    
    Cred: NA
    
- **Edge Cases**
    
     **NA**
    

## ***Future Scope***

NA

## **Step 5: KYC**

## ***V0 Scope***

- **Frontend Experience**
    
    ***First drawdown:***
    
    The KYC journey for the user includes  CKYC journey with OTP trigger, selfie capture and  fallback to Digilocker in case CKYC fails
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXfSbrF8TIShK4BVJJzDKE8ifx8EuoY_y-qBKZX-ee2vw8O08lM7m8VNrC5nwDZAOHddY4fgHtIu_NWn2SDHEQZh-C5TSmTno-TrsKNK2FOtRR2eRspFzQhLVjn8RxpZ8EAhKLGdTw?key=IMeOW9gZebz0hJgmfrnt6A)
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcHxbK81ggCJuBhmFoAbl7msLaQTslyE4FqjdgfKMzfAY4bVjHlPAKJE4P0waiopyFB3ib9vN6uoZ-_e8dnrfVTpaFnRslgQieJelyg8FhSqLTeo_s5yGf69MivIsCBFY73476wXg?key=IMeOW9gZebz0hJgmfrnt6A)
    
- Backend Experience
    
    ***First drawdown:***
    
    **LSP Backend flow:**
    
    Two integration options are supported:
    
    a) LSP using DSP CKYC + Digilocker Wrapper APIs:
    
    - LSP sends PAN, Name, DOB for CKYC fetch and data verification
    - LSP captures selfie
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
    
    DSP **Backend flow:** 
    
    Description:
    
    - Flow same as above
    - DSP will be the source of truth for liveliness, KYC name, and face match—performing these checks internally, with LSPs relying on DSP's response for approval or rejection
    - Deviation logic & handling:
        
            Logic for triggering deviation flows is as below
        
        **1. Liveliness Confidence Score < 40**
        
        - **Outcome:** Liveliness rejected.
        - **Action:** User must retake and resubmit the selfie to DSP. No face match is attempted.
        
        **2. Liveliness Confidence Score 40–70**
        
        - **Outcome:** Borderline liveliness.
        - **Action Flow:** Face match is initiated.
            - If face match > 95: Face match successful; liveliness deviation triggered — additional documents required.
            - If face match < 95: Face match failed; face match deviation flow triggered — additional documents required.
        
        **3.Liveliness Confidence Score > 70**
        
        - **Outcome:** Liveliness check passed.
        - **Action Flow:** Face match is initiated.
            - If face match > 95: Face match successful; no deviation triggered.
            - If face match < 95: Face match failed; face match deviation flow triggered — additional documents required.
        
         Based on the above logic, following deviation handling flow is triggered:
        
         Delta from Current Capabilities: ****Support for CKYC flow (applies to both OD & TL)
        
- **Specific Partner flows**
    
    **Cred**:  
    
    - Currently captures the selfie after KYC, which breaks DSP’s expected flow.To address this, we either need to make DSP’s CKYC API flexible enough to accept the selfie post data fetch, or request the partner to move the selfie step before CKYC initiation, or alternatively adopt DSP’s KYC SDK which handles the flow end-to-end.
    - Will not support DSP’s deviation flow in V0 for low face/data match thresholds.
- **Edge Cases**
    
     ****NA
    

## ***Future Scope***

- ~~Enable LSP to perform liveliness, name matching & face matching at their end by pre-aligning the  logic &  thresholds~~
- ~~However, KYC data (CKYC/Digilocker) must still be fetched via DSP APIs due to RBI compliance requiring REs to perform KYC~~

## **Step 6: Additional Details Capture**

## ***V0 Scope***

- **Frontend Experience**
    
    
    ***First drawdown:***
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXdFQn24rfZp69AynfBzTi7E7hlT1H45YycAVByqDMOzSIDidB_I6B0dMbBE_JVbUWiF75fOdedDt3J9AWIiHxIsoYXVlYYNHO87oQgqgIhwvQHcLcWDRyZwNuiqXrOQvKzYtcn0ZA?key=IMeOW9gZebz0hJgmfrnt6A)
    
    After successful KYC, the user is prompted to enter additional personal details. These fields include father's first and last name, income bracket, employment status, Educational qualification, purpose of the loan, confirmation on whether current address is the same as permanent address
    

- Backend Experience

***First drawdown:***

**LSP Backend Flow** 

Description:

- The LSP is expected to call DSP’s ‘Save Additional Data’ API and pass the above-collected user data along with the user's consent flags.
- Following are the mandatory fields for this API:
    - Father's first & last name
    - Purpose of loan (has to be propogated for every tranche)
    - Income range
    - Employment status

All the fields (including Purpose of loan)are to be captured once at a line level only 

**Specific Partner flows**

Cred: Cred doesn’t have ‘Purpose of loan’ captured pre-application completion, needs to be closed

**DSP Backend Flow**

- Flow : Same as above

**Edge Cases: NA**

**Delta from Current Capabilities: NA** 

## ***Future Scope***

NA

## **Step 7: Bank Account Verification**

## ***V0 Scope***

![image.png](Term%20Loan%20LOS%20requirements/image%201.png)

- **Frontend Experience**
    
    ***First drawdown:***
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeWmRU9OwFEMH8QKl5gUywBMmXGKkLFhaEwSy_FGi2jRF2_ykQRjVVnO95gqG9Fgg4oNUvl9ZIcCSis8Toauusaz8yx190i-eQNwZgVmwFSm3HQ9mRmSVnCHB_eadBX3LLh45fr?key=IMeOW9gZebz0hJgmfrnt6A)
    
    The user either sees their pre-filled bank account information or enters it manually. On submission, penny drop and name match checks are run. If the verification fails, the user is prompted to retry /update bank a/c depending on the error code (in case of penny drop) or provide additional documents (in case of name match failures) by the LSP
    
    ***Subsequent drawdowns***
    
    - Users can choose the bank from their previous tranche or  add a new bank if desired.
    - In case a new bank a/c is getting added, user will be taken through the penny drop verification & name matching process
    
    ***Step Scope***
    
    In conclusion, this step is optional at the tranche level—users may either set up a new disbursement account or proceed with the existing one.
    
- Backend Experience
    
    ***First drawdown***
    
    **LSP Backend Flow** 
    
    - LSP calls DSP’s ‘Bank Utility Init’ API with bank account details.
        - Parameters passed: Opportunity ID, Bank a/c type, a/c no and IFSC code
        - Existing parameter validations apply; no new ones added.
    - DSP performs a penny drop (₹1 transfer) and if rejected, the reason is passed along to LSP to prompt the user to retry  with same or alternate bank a/c depending on the error code
    - On penny drop success, the name returned by the bank is matched against Aadhaar/PAN name by DSP
        - If name match score is ≥ 90%, verification succeeds.
        - If the score is below threshold, verification status is marked as DEVIATION and shared with LSP. DSP expects LSPs to share supporting documents (cancelled cheque/passbook/etc.) to proceed in such cases.
    
    **DSP Backend Flow** 
    
    Flow: DSP performs penny drop and name match logic at their end and shares verification result with LSP to action on ie DSP serves as the source of truth for both penny drop & name match verification
    
    Deviation logic & handling: 
    
    If the name match score is ≥ 90, the bank verification is auto-approved.
    
    If < 90, it triggers a deviation flow where the customer is prompted to upload supporting documents, such as:
    
    - Chequebook
    - Cancelled cheque
    - Bank app screenshot
    
    These documents are manually reviewed by the operations team for final approval
    
- **Edge Cases: NA**
- **Specific Partner flows**
    
    Cred:  Will not support DSP’s deviation flow in V0 for low name match thresholds.
    

## ***Future Scope***

- Support for LSPs to do penny drop & name match verifications at their end, provided logic and threshold is aligned with DSP.

## **Step 8: Mandate Setup Flow**

## ***V0 Scope***

![image.png](Term%20Loan%20LOS%20requirements/image%202.png)

- **Frontend Experience**
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXerC8uLsAMdbcN-6MaGoHtLsdBuVCrO8PSRHthkoFpkjlhptehtTnXKJv6WyMMJcOoCNuzL6gCkAknxO5SJiWctgSq_9EFDYR_oJqlWdpn-5XzvE0IyI_MJr3r3pTxcVx_gh8hBuQ?key=IMeOW9gZebz0hJgmfrnt6A)
    
    ***First drawdown***
    
    User selects the mode of mandate registration( only eNach in V0 )and reviews displayed loan amount, EMI payment date, tenure and EMI amount . User is then redirected to either LSPs/DSPs mandate set up flow based on whether LSP/DSP is handling the registration.On successful setup, a confirmation screen is displayed.
    
- Backend Experience
    
    **LSP /DSP Backend Flow** 
    
    ***First drawdown***
    
    ~~Scenario 1:~~
    
    - ~~LSP initiates mandate setup using DSP’s ‘Create Mandate’ API. The re-mandate logic remains with the LSP—they will call this API only if they decide a re-mandate is needed; otherwise, they’ll skip it.Following are the params passed in the API~~
        - ~~Opportunity ID~~
        - ~~BankAccountVerificationId~~
            - ~~The mandate will be set on this bank account, and all EMI pulls across tranches will be made from it, irrespective of the disbursement account set for the tranche~~
        - ~~Mandate amount~~
            - ~~DSP won’t validate ‘mandate amt/limit’ at this stage; min/max amount checks will occur at Submit Opportunity stage~~
        - ~~Mandate type:  UPI or e-NACH~~
            - ~~Validate whether the specified ‘mandate type’ is enabled for the given partner.~~
        - ~~End date:~~
            - ~~DSP won’t validate ‘end date’ at this stage; min/max amount checks will occur at Submit Opportunity stage (as visibility on chosen offer details is req for the same)~~
        - ~~Presentation date:~~
    - ~~DSP returns the Digio SDK URL or redirection link for LSP’s user to complete the flow~~
    
    Scenario 2:
    
    - LSP uses their own mandate set up flow  with DSP utility code and uses web hook to post the registration details via DSP’s ‘**Mandate Registration’ API**
        - StartDate &End date
            - DSP won’t validate ‘end date’ at this stage; min/max amount checks will occur at Submit Opportunity stage (as visibility on chosen offer details is req for the same)
        - Mandate amount
            - DSP won’t validate ‘mandate limit at this stage; min/max amount checks will occur at Submit Opportunity stage.
        - bankAccountVerificationId
            - The mandate will be set on this bank account, and all EMI pulls across tranches will be made from it, irrespective of the disbursement account set for the tranche.Following table illustrates the same
        
        | Tranche | Selected bank | Disbursement a/c | Details passed in Mandate api | New mandate? | Active Mandate (Post Tranche) | Bank a/c 4 mandate pull |
        | --- | --- | --- | --- | --- | --- | --- |
        | Tranche 1 | B1 | B1 | Amt = x, Expiry= y & Bank=B1 | Yes | M1 | B1 (tranche 1) |
        | Tranche 2 | B2 | B2 | Amt = x, Expiry= y & **Bank**=B2 | Yes | M2 | B2 (tranche 1 &2) |
        | Tranche 3 | B1 | B1 | **Amt** = a, Expiry= y & Bank=B1 | Yes | M3 | B1 (tranche 1,2 &3) |
        | Tranche 4 | B3 | B1 | Amt = a, Expiry= y & Bank=B1 | No | M3 | B1 (tranche 1,2,3 &4) |
        | Tranche 5 | B2 | B2 | Amt = a, **Expiry**= b & Bank=B1 | Yes | M4 | B1 (tranche 1,2,3 &4 |
        - Mandate type: UPI/eNach
            - Validate whether the specified ‘mandate type’ is enabled for the given partner.
        - Mandate frequency
            - Validate whether its set to ”as and when presented”
        - Presentation date
            - Only one presentation date should be supported per customer across all tranches, though different customers can have different dates within the allowed ‘2nd–7th of the month’ range.
        - UMRN no
            - Needs to be a valid UMRN no
    - In addition to posting the details via API, LSPs must share ‘T+1’ MIS on registered mandates for reconciliation. DSP will reconcile the received MIS with the MIS received from the source directly (TSP) for reconciliation
    
    Note: DSP’s guardrails/product policy for ‘re-mandate’ logic needs to be configured for validating mandate details at the time of ‘submit opprtunity 
    

- STP/Non STP checks:
    
    Once the mandate is completed, the backend initiates a workflow for AML/CIBIL checks  concurrently to decide if the application will follow the STP or non-STP path.
    
    - **AML check** is done via TrackQuis; **CIBIL check** via Transunion
    - If TrackQuis finds a match, it returns:
        - AML/PEP score
        - UNSC and MHA score
        - Credit score
    - There is **no hard threshold** for CIBIL; Score less than 300 marked as ‘High’ but no action taken on this
    - Any positive match in AML/PEP/UNSC/MHA results in auto-flagging & request is auto-created in the CC dashboard with reports and scores.
    - A **maker-checker task** is assigned to the Ops team for manual review of the AMLAML/PEP/UNSC/MHA docs
    - While the check is in progress, the user **cannot proceed to sign the agreement**.
    - Once Ops approves, a callback updates the status, and the customer can proceed with signing.
- Partner Specific Flows
    - Cred will only be going live with eNach in V0
    - Cred is registering the mandate themselves using Digio/Razorpay(only if Digio is down) integration but DSP’s utility code
        - Cred will send webhook to DSP on successful registration.
        - Cred will share ‘T+1’ MIS for  ‘mandate registration’ reconciliation at DSP’s end
    - Cred will be handling the re-mandate logic; Re-mandate logic attached here.
- **Edge Cases**
    
    **NA**
    

## ***Future Scope***

- DSP’s UPI mandate setup to be supported with required changes in registration api, if any
- DSPs to have their own re-mandate logic at their end to support cases where DSP is controlling the mandate registration.However in this case DSP will need visibility on the chosen loan offer details  to determine whether or not to go for a re-mandate

## **Step 10: Pledging**

## ***V0 Scope***

- **Frontend Experience**
    
    ***First   drawdown***
    
    Users on initiating the ‘Pledge flow’ will receive an OTP on entering which the pledge process gets initiated
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeb9n3NaAi-iw9-HWr-YCvnSxh7WVS4-dr4wP7n4eeR2b-35Uzv9gUpkBArJimH7lvVX_2GpsT12J5MQEvgd6sfoZUYrZ7U0teZSkd6f65_iAoeZzXIgMRpsNLlt0YPdGTqMWyIJg?key=IMeOW9gZebz0hJgmfrnt6A)
    
- Backend Expereince
    
    ***First  drawdown***
    
    **LSP Backend Flow**
    
    - Two scenarios:
        - LSPs can either hit our Pledge wrapper APIs (MFC/RTAs)with their fund units and get the pledge status at a fund level
        - LSPs can use their Pledge APIs but with DSP’s child credentials
    - Step Scope **:** Pledging process executed at a loan level
    
    Partner Specific Flows
    
    Cred: Planning to rely on their own Pledge APIs using DSP child credentials in V0
    
    **DSP Backend Flow**
    
    - Flow: Same as above
    - Step scope: Pledging mapped to a line in DSP’s backend
    
    **Edge Cases: NA**
    
    **Delta from Current capability:** Support for pledge execution at a loan level
    

## ***Future Scope***

NA

## **Step 11: KFS & Agreement Signing**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVE4iIiD3sbD8MnHsSOO-7gNPZlQW8w_qp7_drG8zlZJGkYw2M4-zjPPbNDtBNVZnqf1atjRzjmKSwsVxWmZkNsz0QlmHd5Nq9mAy7jvOx5bFJngAEjjTk_TUV0_8OrAGFMVNi6g?key=IMeOW9gZebz0hJgmfrnt6A)

User reviews and digitally signs the agreement &  KFS document(both click-wrap based).

Backend Experience

**LSP Backend Flow**

Two step process:

Step 1: Validation of LSP’s term loan offer

LSPs who are calculating offers at their end will be sharing the offer chosen by the user for the first time at this stage.They need to share the following parameters:

- Loan amount
- Tenure
- Interest rate
- EMI
- Sanction limit : a function of ‘eligible limit’

DSP at their end will first validate the first 3 values at their end (ie are they within the permissable range set for the line).If yes, we will validate the EMI using DSP’s internal offer generation engine (ie PMT calc for EMI) and the sanactioIf yes to both, DSP will proceed to step 2.

In case of rejection wrt any of the parameters we reject the offer and share the response to LSP

Step 2: Contract generation/signing

a) LSP uses DSP generated  KFS & agreement PDF and renders it in their UI for customer  digital consent (click-wrap) and shares signature metadata (IP + timestamp) with DSP.

b)  LSP uses DSP’s redirection link for agreement /KFS review & signing:

- Link hosts KFS &  Agreement . On user acceptance (via click-wrap), DSP captures the consent details

Step Scope: **KFS & Sanction letter to be generated at a loan level while agreement at a line level**

Note: For the first loan drawdown, all 3 will be generated (KFS,Sanction letter & Agreement) and need to be reviewed/accepted by the customer 

**Specific Partner Flows**

Cred: 

- Generates KFS and agreement at their end and share digital consent metadata with DSP.\
- Aligned to send flat values to DSP even for % based charges in V0

**DSP Backend Flow**

Need to support the generation of KFS & Sanction letter at a loan level and Master agreement at a line level

Attached is the [list of parameters](https://docs.google.com/document/d/1ffsx9F4Z-jztOGAqGe8fR3JoVb8su1ugHZ1pJ43-9Gw/edit?tab=t.0) going into KFS,Agreement,MITC & Sanction letter

Attached is the template for KFS,Agreement,MITC & Sanction letter along with the exact details that need to go into the same

**Edge Cases: NA**

**Delta from Current capabilities**

- Support for term loan offer generation engine to validate the offer details passed on by LSP
- KFS & Sanction letter to be generated at a loan level

## ***Future Scope***

- Explore how to optimise the flow in case of offer mismatches (eg: modified offer instead of straightaway rejections)
- Explore the possibility of migrating both KFS and Agreement to line-level

## **Step 12: Submit Opportunity**

## ***V0 Scope***

**Frontend Experience:** 

***First  drawdown***

![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/0ef8af1d-6ecf-44d9-936f-60b8668da74d.png)

User sees a loader screen indicating that the disbursement process has been initiated and is in progress.

Backend Experience

***First drawdown***

**LSP  Backend Flow**

- Flow: LSP hits DSP’s  ‘submit opportunity’ api after all onboarding steps (KYC, Bank, Mandate, Agreement, etc.) are completed.

DSP Backend Flow

When the LSP triggers the **Submit Opportunity API**, DSP first performs a set of API validations. Only upon successful completion of these validations, the internal ‘**Submit Opportunity Workflow’** initiated.

**1. Pre-Workflow Validation Checks (at API trigger)**

- **Utility ID Presence Check:**
    
    Ensures required utility IDs are present in the ‘approved state’ for the following:
    
    - Agreement
    - KFS
    - Mandate
    - Bank account
    - Photo verification
    - Email verification logs
    - Mobile verification logs
    - Additional data
- **Client Dedupe Check:**
    - Re-validates de-duplication on the combination of `PAN + Product + LSP`.
- **Agreement Reference IDs check:**
    - Confirms that the 4 utility reference IDs passed in Submit Opportunity match those passed at the time of Loan contract generation ie Photo,Additional data ,KYC, Bank verification
- **Pledge ID Validation (for Submit Opportunity V2 API):**
    - Ensures all pledge reference IDs are in an **approved state**.(request approved for kfin)
- **Pledge status verification with RTAs/MFC & DP calculation:**
    
    User requested amount vs Pledge Value (DP) Check:
    
    - Check the fund pledge status with RTAs/ MFC and calculate the eligible DP
    - Compares the **user-requested loan amount (loan offer)** with the **eligible disbursal amount (DP)**.
        - If **requested amount <= DP**: the application proceeds to the next step in the workflow.
        - If **requested amount > DP**:
            
            A  **webhook** with an **error** indicating the eligible DP will be triggered, the LSP must either:
            
            **Option 1: Additional Pledge**
            
            - Initiate an additional pledge by calling DSP’s **Pledge API**, passing the reference IDs in **Submit Opportunity** API ( using the existing opportunity id)
            - *Note: All API validations will re-trigger during this submission.*
            
            **OR**
            
            **Option 2: Proceed with Lower Loan Amount**
            
            - User selects a revised offer with a lower amount and possibly a different tenure.
            - LSP may or may not call the **Mandate API**, depending on their re-mandate logic.
                - If mandate update is required (e.g., due to tenure change), DSP will return a new **Mandate Utility ID**.
            - LSP must then call the **KFS v2 API** with updated offer details to regenerate the KFS and display it to the user.
            - Upon KFS approval, LSP will re-trigger the **Submit Opportunity** API (with existing opportunity id))with the updated **KFS Utility ID** and **Mandate Utility ID** (if applicable).
    
    **Note:**
    
    - **Both DP** & **loan offer is calculated based on custom LTV limits configured by the LSP (Cred: 42%)**

If all the above checks pass, the **Submit Opportunity  internalWorkflow** is triggered.

**2. Checks post workflow trigger**

The following checks determine whether the workflow proceeds directly or is routed to the checker flow for ops review.

**A. Skipping of AML & CIBIL Checks: LOAN**

- AML and CIBIL are **skipped** at this stage **if already completed** post-mandate setup.
    - If not completed, to re-perform these checks again at this stage:
        - If checks fails(ie match found in trawizz or CIBIL<300), then application moves to checker flow
            - Attached is the [list of data points](https://docs.google.com/spreadsheets/d/1a9O4jmwPg6_nXeFatjQbZaveh0hbB1vCJIo-Y4Dq5vk/edit?gid=1906805600#gid=1906805600) to be stored or captured in the LOS backend as well as the fields to be passed to the Command Centre.
        - If checks didn’t get triggered successfully, then workflow is blocked
        - If checks pass successfully, then workflow continues to the nest step
            - CIBIL success if CB score >300 or CIBIL=-1 (NTC)
            - AML success if no match found in traquis

**B. Document Check : LOAN**

- **Document Availability Validation:**
    
    Confirms that all mandatory documents are available:
    
    - Aadhaar
    - PAN (optional?)
    - KYC report (fetched from Digio)
    
    In case any of these docs are not available, the workflow is blocked and system will try to pull these docs in real time from Digio. Post successful pull, the workflow is unblocked 
    

After the above validations are complete, the following checks are executed to determine whether the flow will follow the STP or Non-STP path:

- Following five sub-checks are executed:
    
    **a1. Sourcing Channel Validation: — LOAN & TRANCHE**
    
    - Verifies if the sourcing channel (e.g., Cred) is enabled for  the STP flow
        - Eg: In initial CUG process, STP is disabled for sourcing channel partners
    
    **a2. Father’s Name Match Check: — LOAN**
    
    - If KYC contains father’s name, validates ≥90% match with captured value.
    - If not present in KYC, compares father’s name with applicant name (<90% match).
    
    a3.  KFS **Financial Parameter Thresholds for STP: — TRANCHE**
    
    Validates that parameters passed in the KFS are within the  below mentioned values:
    
    | Parameter | STP Range |
    | --- | --- |
    | Mandate limit value | Min:(New tranche disbursement amount + Outstanding POS) 
    Max: 1Cr |
    | Tenure | 72 to 76 months (6 yrs and 4 months) |
    | Interest Rate | 9% to 15% |
    | Processing Fees | To be shared by Business |
    | Margin Pledge Fees | 0 (V0) |
    | Annual Maintenance Fees | 0 (V0) |
    
    If any of the above STP values is not met, application to be routed to NON-stp flow.
    
    [a4.](http://a4.AL) Request tranche amount vs Available Limit check for STP/Non STP
    
    - If AL **>= requested tranche amount** → **STP**
    - If AL **<requested tranche amount**  →NON- **STP routing**
        
        
        Calculation of AL & requested amount:
        
        AL= MIN(Sanction Limit - Agg. disbursed amount, Drawing Power - POS)
        
        Requested tranche amount= User requested amount (in agreement)
        
        See below for the  SL/‘Sanctioned limit’ bucketing:
        
        | Eligible Portfolio value | Sanction limit capping |
        | --- | --- |
        | <= 5 lakhs | 20 L |
        | <=15 lakhs | 50L |
        | <=25 lakhs | 1 Cr |
        | < 50 lakhs | 2 Cr |

**a5. Mandate Check: — TRANCHE**

- Following are the validations for the mandate amount/tenure limit /bank :
    - Amount
        - Min:(  New tranche disbursement amount + Outstanding POS across all tranches))
        - Max: 1Cr
    - Tenure
        - Min: Max of  tenures of all ongoing tranches
        - Max: 30 yrs
    - Bank
        - Mandate needs to point to the latest tranche bank

If any of the above validations fail, the application is routed to Non-STP flow.

a6.Disbursement amount checks- TRANCHE

- Disbursement amount greater than 20 Lacs >> Non STP
- More than 2 disbursements in a single day >> Non STP

**3. If All Checks Pass → STP Flow is Initiated**

The application proceeds via the STP route, triggering the following sequential steps:

1. **Client Creation:**
    - A client ID is generated in Finflux LMS.
        - The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture and storage logic
2. **Risk Data Mapping:**
    - CIBIL score and KYC flags (e.g., High Risk) are mapped to the client profile.
        - The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture and storage logic
3. **Loan creation:**
    - Loan is created against the client ID.
        - The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture /storage logic
4. **AML Monitoring:**
    - Automatically triggered after loan creation.
        - The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture/storage logic
5. **Bank Account & Mandate Linkage:**
    - Mandate will be mapped to tranche disbursement a/c for first drawdown
        - The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture /storage logic
6. **Co-Borrower Step:**
    - Dummy placeholder; no operations performed.
7. **Charge Application:**
    - PF (Processing Fee) is applied to the tranche
    - **~~Elevate customers** (those with an active Bajaj loan) receive a **PF waiver (₹0 for DSP)**.~~
    - Duplicate fee errors ("Already Applied") are programmatically handled.
8. **Agreement Signing Workflow:**
    - Customer sign is attached to the agreement
    - NBFC stamps and signs the agreement.
    - Final signed copy and welcome documents are sent to the customer
9. **Collateral Addition:**
    - Attach the successfully pledged assets to the created loan a/c
10. Tranche creation
    1. Tranche created against  the loan ID/client ID
    2. The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture /storage logic
11. Welcome docs trigger
    1. Welcome letter PDF attachment containing the following documents are triggered to the user via email
        - Signed loan cum pledge agreement
        - Key fact statement
        - Loan schedule
    2. Following is the email template and template ID

    

1. Command centre requirements

Following are the list of fields that need to be captured in the BE for powering command centre r[equirements](https://docs.google.com/spreadsheets/d/1a9O4jmwPg6_nXeFatjQbZaveh0hbB1vCJIo-Y4Dq5vk/edit?gid=1906805600#gid=1906805600) 

## ***Future Scope***

NA

### SUBSEQUENT  DRAWDOWNS

[](https://imgr.whimsical.com/object/E1Kuapabt4KKLi61vH5enr)

## **Step 1: MF Fund Fetch (Ad-hoc)**

- Frontend Experience
    
    LSPs might provide an option in UI for users to refresh their limit.On hitting the same, LSPs will initiate a mutual fund fetch to pull up the latest list of eligible funds against the user
    
- Backend Experience
    
    LSP Backend flow 
    
    LSP’s may re-fetch eligible funds whenever required ie on ad-hoc basis, to refresh the eligible limit of user . 2 options for fetch exist for LSPs
    
    - LSPs use their own MFC/RTA fetch APIs:
        - MF fund details are  returned.
        - However eligible fund list, their LTV / NAV values and drawing power maintained by DSP are not available.
        - To access this data, the LSP must hit DSP’s offer generation API.
    - LSPs use DSP’s wrapper APIs:
        - LSP shares the user’s PAN and mobile number.
        - DSP returns:
            - List of eligible funds with LTVs.
            - List of ineligible funds (unapproved/others).
            - Summary of total portfolio value, eligible fund value, and overall eligible limit.
    
    **DSP Backend Flow**
    
    Description: LSPs hitting DSP’s MF fetch wrapper APIs will receive the total portfolio value, eligible fund value, and overall eligible limit.
    
- **Specific LSP flows**
    
    **Cred: Using** their own fund fetch APIs instead of relying on DSP’s wrapper API for MF fetch
    
- **Edge Cases**
    
    **NA**
    

## **Step 2: Eligible limit determination /Offer Gen API (Ad-hoc)**

## ***V0 Scope***

- **Frontend Experience**
    
    User chooses drawdown amount from their refreshed eligible limit, which comprises a combination of replenished limit (replenished on closure of ongoing tranches through repayment) and /or  fund re-fetch
    
    ![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/image%201.png)
    
- Backend Experience
    
    ***Subsequent drawdowns***
    
    Same as first drawdown with the below highlighted differences:
    
    a)Tenure handling:
    
    For subsequent drawdowns, the  ’max’ value  for tenure will vary based on the period left in the  ‘loan facility’  tenure . Logic for calculating the max value is :
    
    max_tenure_months = (facility_expiry.year - today.year)*12
    + (facility_expiry.month - today.month)
    
    Note: Here ’today’ refers to the date on which this API is invoked.
    
     For eg: User takes a loan facility  on  5July 2025, based on product policy the expiry of this line will be on 31st July 2031. Say:
    
    - User takes first tranche for 36 months on 5 July 2025
    - User now comes for a second tranche on 10th Aug 2027, in this case since our line expires on 31st July 2030, the max tenure we can offer is 35 months
    
    b)Only tranche level parameters need to be included in the offer gen API for subsequent :
    
    - Tenure
    - Interest
    - Fee parameters : Only PF
    
    **Note:** *Max tenure of each tranche can be 5 year, whereas loan expiry of 6 years*
    
    DSP Backend Flow
    
    DSP supports eligibility limit determination directly via ‘offer generation’ api as well as ‘mutual fund fetch wrapper’ APIs as well .However loan offer parameters like (tenure,Int) & fee details are only available via the latter
    
- Specific Partner flows
    
    Cred:
    
    Need to support custom LTVs passed on by Cred for overall eligible limit determination 
    
    - LTV ≤ DSP-defined value for that fund.If valid, DSP uses passed LTVs to calculate eligibility.
    - If invalid, DSP rejects and provides reason for LSP to retry
- **Edge Cases:**
    
    In case user drops off post eligibility determination and resumes flow later, its recommended to LSPs to use DSP’s offer generation api to get the updated NAV/LTV values
    

## ***Future Scope***

 ****Support LSPs in receiving global NAV/LTV updates from DSP to compute eligible limits on their end  with their fetched funds and skip the offer generation API

## **Step 3: Opportunity Creation**

## ***V0 Scope***

- **Frontend Experience:**
    
    NA
    
- Backend Experience
    
    **LSP Backend flow**
    
    Description: 
    
    Once user proceeds with an offer at LSP’s end,  LSPs need to hit DSP’s backend to create an unique opportunity in the backend to track the status of this request through all downstream stages such as KYC, mandate, agreement, pledging, etc  
    
    Below are the steps applicable at a tranche/adhoc-level
    
    | **Step** | Execution frequency |
    | --- | --- |
    | MFC Fund Fetch  | Ad-hoc (optional) |
    | Eligible Limit Determination | Ad-hoc(optional) |
    | Bank a/c set up & verification | Tranche (optional) |
    | Mandate set up | Tranche (optional) |
    | Pledging | Tranche |
    | KFS +Sanction letter | Tranche |
    | Term Loan offer Validation | Tranche |
    | A/c Creation (Submit opportunity) | Tranche (tranche ID) + Loan(loan ID) |
    
    **DSP Backend Flow:** 
    
    On LSP hit, DSP backend creates an unique opportunity ID which is  shared with LSP to enable E2E tracking through the funnel.
    
    Note: While pledging is tracked /executed at the tranche level, the pledged assets will be mapped to the loan in DSP’s backend
    
- **Specific Partner flows**
    
    Cred: NA
    
- **Edge Cases**
    
     **NA**
    

## ***Future Scope***

NA

## **Step 7: Bank Account Verification**

## ***V0 Scope***

![image.png](Term%20Loan%20LOS%20requirements/image%201.png)

- **Frontend Experience**
    - Users can choose the bank from their previous tranche or  add a new bank if desired.
    - In case a new bank a/c is getting added, user will be taken through the penny drop verification & name matching process
    
    ***Step scope***
    
    In conclusion, this step is optional at the tranche level—users may either set up a new disbursement account or proceed with the existing one.
    
- Backend Experience
    
    **LSP Backend Flow** 
    
    LSP will call the DSP API to fetch the list of pre-configured disbursement banks (across different tranches). Based on customer input, the LSP can either:
    
    a) select a bank from this list, or
    
    b) submit a new bank account for disbursement
    
    If the selected bank is from the pre-configured list, DSP will **skip penny drop verification**. If a new bank account is provided, DSP will initiate the **penny drop verification & name matching flows (mentioned earlier)** to validate it.
    
    **DSP Backend Flow** 
    
    Same as above
    
    Note: The final bank selected for a tranche—whether an existing or new account—will be the account to which the tranche disbursement is routed.
    

      Note: In case multiple bank a/cs are added at a loan level, the latest added bank a/c becomes      the default/primary bank a/c (only after tranche is created )

- **Edge Cases: NA**
- **Specific Partner flows**
    
    Cred:  Will not support DSP’s deviation flow in V0 for low name match thresholds.
    

## ***Future Scope***

- Support for LSPs to do penny drop & name match verifications at their end, provided logic and threshold is aligned with DSP.

## **Step 8: Mandate Setup Flow**

## ***V0 Scope***

![image.png](Term%20Loan%20LOS%20requirements/image%202.png)

For subsequent drawdowns, the user may or may not be taken through the mandate flow, depending on whether the tranche bank is updated/ LSP determines that a re-mandate is necessary.

- Backend Experience
    
    **LSP /DSP Backend Flow** 
    
    For subsequent drawdowns/tranches, the LSP’s internal logic determines whether a re-mandate is required based on which they hit DSP’s ‘mandate set up’/’registration posting ‘apis. If triggered, the existing mandate is deactivated, and only the new one remains active in the LSP/DSP backend. At any point, only one active mandate can exist at a loan level in the LSP/DSP system.
    
    Note: If bank is updated for subsequent tranche, remandate needs to be done to point to the latest tranche bank 
    
    ***Step Scope***
    
    Mandate set up happens at a loan level. At any point in time ,only one active mandate can exist at a loan level
    
- Partner Specific Flows
    - Cred will only be going live with eNach in V0
    - Cred is registering the mandate themselves using Digio/Razorpay(only if Digio is down) integration but DSP’s utility code
        - Cred will send webhook to DSP on successful registration.
        - Cred will share ‘T+1’ MIS for  ‘mandate registration’ reconciliation at DSP’s end
    - Cred will be handling the re-mandate logic; Re-mandate logic attached here.
- **Edge Cases**
    
    **NA**
    

## ***Future Scope***

- Support for multiple active mandates at a loan level(both UPI & eNach) ; This change will also require supporting multiple mandate presentation dates at a loan level
- DSP’s UPI mandate setup to be supported with required changes in registration api, if any
- DSPs to have their own re-mandate logic at their end to support cases where DSP is controlling the mandate registration.However in this case DSP will need visibility on the chosen loan offer details  to determine whether or not to go for a re-mandate

## **Step 10: Pledging (Optional)**

## ***V0 Scope***

- **Frontend Experience**
    
    Users on initiating the ‘Pledge flow’ will receive an OTP on entering which the pledge process gets initiated
    
    [](https://lh7-rt.googleusercontent.com/docsz/AD_4nXeb9n3NaAi-iw9-HWr-YCvnSxh7WVS4-dr4wP7n4eeR2b-35Uzv9gUpkBArJimH7lvVX_2GpsT12J5MQEvgd6sfoZUYrZ7U0teZSkd6f65_iAoeZzXIgMRpsNLlt0YPdGTqMWyIJg?key=IMeOW9gZebz0hJgmfrnt6A)
    
- Backend Experince
    
    **LSP Backend Flow**
    
    - Two scenarios:
        - LSPs can either hit our Pledge wrapper APIs (MFC/RTAs)with their fund units and get the pledge status at a fund level
        - LSPs can use their Pledge APIs but with DSP’s child credentials
    - Step Scope **:** Pledging process executed at a tranche level
    
    Partner Specific Flows
    
    Cred: Planning to rely on their own Pledge APIs using DSP child credentials in V0
    
    **DSP Backend Flow**
    
    - Flow: Same as above
    - Step scope: Pledging mapped to a loan in DSP’s backend
    
    **Edge Cases: NA**
    
    **Delta from Current capability:** Support for pledge execution at a tranche level
    

## **Step 11: KFS (& Sanction Letter) Signing**

## ***V0 Scope***

**Frontend Experience**

[](https://lh7-rt.googleusercontent.com/docsz/AD_4nXcVE4iIiD3sbD8MnHsSOO-7gNPZlQW8w_qp7_drG8zlZJGkYw2M4-zjPPbNDtBNVZnqf1atjRzjmKSwsVxWmZkNsz0QlmHd5Nq9mAy7jvOx5bFJngAEjjTk_TUV0_8OrAGFMVNi6g?key=IMeOW9gZebz0hJgmfrnt6A)

User reviews and accepts KFS document(click-wrap based).

Backend Experience

**LSP Backend Flow**

Two step process:

Step 1: Validation of LSP’s term loan offer

LSPs who are calculating offers at their end will be sharing the offer chosen by the user for the first time at this stage.They need to share the following parameters:

- Loan amount
- Tenure
- Interest rate
- EMI (EMI figure rounded up to the nearest integer has to match exactly with shared Cred EMI value )
- EMI date
- ~~Sanction limit : a function of ‘eligible limit’; Eg: 4x of eligible limit etc~~

DSP at their end will first validate the first 3 values a (ie are they within the permissable range set for the line).If yes, we will validate the EMI using DSP’s /Finflux’s EMI calc formula (ie PMT).If yes to both, DSP will proceed to step 2.

In case of rejection wrt any of the parameters we reject the request and share the response to LSP

Step 2: KFS generation/signing

 LSP uses DSP generated  KFS PDF and displays it in their UI for customer  digital consent (click-wrap) and shares signature metadata (IP + timestamp) with DSP via KFS V2 api

**Specific Partner Flows**

Cred: 

- Aligned to send flat values to DSP even for % based charges in V0

**DSP Backend Flow**

Need to support the generation of KFS at a tranche level

Attached is the [list of parameters](https://docs.google.com/document/d/1ffsx9F4Z-jztOGAqGe8fR3JoVb8su1ugHZ1pJ43-9Gw/edit?tab=t.0) going into KFS( & Sanction letter)

Attached is the template for KFS( & Sanction letter) along with the exact details that need to go into the same

**Edge Cases: NA**

**Delta from Current capabilities**

- Support validating the offer details passed on by LSP
- KFS & Sanction letter to be generated at a tranche level

## ***Future Scope***

NA

## **Step 12: Submit Opportunity**

## ***V0 Scope***

- **Frontend Experience:**
    
    
    ![image.png](Single%20drawdown%20Term%20Loan%20LMS%20Requirements/0ef8af1d-6ecf-44d9-936f-60b8668da74d.png)
    
    User sees a loader screen indicating that the disbursement process has been initiated and is in progress.
    
- Backend Experience
    
    **LSP  Backend Flow**
    
    - Flow: LSP hits DSP’s  ‘submit opportunity’ api after  relevant onboarding steps [Bank set up, Mandate (optional), Pledge, KFS] are completed.
    
    DSP Backend Flow
    
    When the LSP triggers the **Submit Opportunity API**, DSP first performs a set of API validations. Only upon successful completion of these validations, the internal ‘**Submit Opportunity Workflow’** initiated.
    
    **1. Pre-Workflow Validation Checks (at API trigger)**
    
    - **Utility ID Presence Check:**
        
        Ensures required utility IDs are present for the following:
        
        - KFS
        - Mandate  (If bank is updated for subsequent tranche, re-mandate is mandatory)
        - Pledge (optional)
        - Bank verification
    - Mandate-Bank link check
        - Check to be configured to ensure mandate points to the latest tranche bank a/c.Whenever tranche disbursement bank is updated, mandate needs to be updated (via re-mandate flow) and be linked to this bank a/c
    - **~~Dedupe Check:~~**
        - ~~Re-validates de-duplication on the combination of `PAN + Product + LSP`.~~
    - **~~Agreement Reference IDs check:~~**
        - ~~Confirms that the 4 utility reference IDs passed in Submit Opportunity match those passed at the time of Loan contract generation ie Photo,Additional data ,KYC, Bank verification~~
    - **Pledge ID Validation (for Submit Opportunity V2 API):**
        - Ensures all pledge reference IDs are in an **approved state(optional)**
    - **Pledge status verification with RTAs/MFC & DP calculation:**
        
        User requested amount vs DP Check:
        
        - ~~Check the fund pledge status with RTAs/ MFC and calculate the eligible DP~~
        - Compares the **user-requested loan amount (loan offer)** with the **eligible disbursal amount (DP)**.
            - If **requested amount <= DP**: the application proceeds to the next step in the workflow.
            - If **requested amount > DP**:
                
                The **Submit Opportunity API will fail** with an **error** indicating the eligible DP, the LSP must either:
                
                **Option 1: Additional Pledge**
                
                - Initiate an additional pledge by calling DSP’s **Pledge API**, passing the reference IDs in **Submit Opportunity** API ( using the existing opportunity id)
                - *Note: All API validations will re-trigger during this submission.*
                
                **OR**
                
                **Option 2: Proceed with Lower Loan Amount**
                
                - User selects a revised offer with a lower amount and possibly a different tenure.
                - LSP may or may not call the **Mandate API**, depending on their re-mandate logic.
                    - If mandate update is required (e.g., due to tenure change), DSP will return a new **Mandate Utility ID**.
                - LSP must then call the **KFS v2 API** with updated offer details to regenerate the KFS and display it to the user.
                - Upon KFS approval, LSP will re-trigger the **Submit Opportunity** API (with existing opportunity id))with the updated **KFS Utility ID** and **Mandate Utility ID** (if applicable).
        
        **Note: Both loan offer & DP** is calculated based on **custom LTV limits configured for the LSP (Cred: 42%)**
        
    
    If all the above checks pass, the **Submit Opportunity  internalWorkflow** is triggered. If checks fail, the submit opportunity api request fails
    
    **2. Checks post workflow trigger**
    
    **A. ~~Skipping of AML & CIBIL Checks~~**
    
    - ~~AML and CIBIL are **skipped** at this stage **if already completed** post-mandate setup.~~
        - ~~If not completed, to re-perform these checks again at this stage:~~
            - ~~If checks fails(ie match found in traquis or CIBIL<300), then application moves to checker flow~~
            - ~~If checks didn’t get triggered successfully, then workflow is blocked~~
            - ~~If checks pass successfully, then workflow continues to the nest step~~
                - ~~CIBIL success if CB score >300 or CIBIL=-1 (NTC)~~
                - ~~AML success if no match found in traquis~~
    
    **B~~. Document Check – Final STP/Non-STP Branching Decision~~**
    
    - **~~Document Availability Validation:~~**
        
        ~~Confirms that all mandatory documents are available:~~
        
        - ~~Aadhaar~~
        - ~~PAN~~
        - ~~KYC report (fetched from Digio)~~
        
        ~~In case any of these docs are not available, the workflow is blocked and system will try to pull these docs in real time from Digio. Post successful pull, the workflow is unblocked~~ 
        
    
    The following checks are executed to determine whether the flow will follow the STP or Non-STP path:
    
    - Following five sub-checks are executed:
        
        **~~a1. Sourcing Channel Validation:~~**
        
        - ~~Verifies if the sourcing channel (e.g., Cred) is enabled for  the STP flow~~
            - ~~Eg: In initial CUG process, STP is disabled for sourcing channel partners~~
        
        **~~a2. Father’s Name Match Check:~~**
        
        - ~~If KYC contains father’s name, validates ≥90% match with captured value.~~
        - ~~If not present in KYC, compares father’s name with applicant name (<90% match).~~
        
        a3.  KFS **Financial Parameter Thresholds for STP:**
        
        Validates that parameters passed in the KFS are within the  below mentioned values:
        
        | Parameter | STP Range |
        | --- | --- |
        | Mandate limit value | Min:( New tranche disbursement amount + Outstanding POS) 
        Max: 1Cr |
        | Tenure | 72 to 76 months (6 yrs and 4 months) |
        | Interest Rate | 9% to 15% |
        | Processing Fees | To be shared by Business |
        | Margin Pledge Fees | 0 (V0) |
        | Annual Maintenance Fees | 0 (V0) |
        
        If any of the above STP values is not met, application to be routed to NON-stp flow.
        
        [a4.AL](http://a4.AL) check for STP/Non STP
        
        - If AL **>= requested tranche amount** → **STP**
        - If AL **<requested tranche amount**  →NON- **STP routing**
            
            
            Calculation of AL & requested amount:
            
            | Requested tranche amount | Eligible DP against new tranche |
            | --- | --- |
            | AL | Min (SL,DP) - Aggregate of all disbursements |
            
            See below for the  SL/‘Sanctioned limit’ bucketing:
            
            | Initial Portfolio value | Sanction limit capping |
            | --- | --- |
            | <= 5 lakhs | 20 L |
            | <=15 lakhs | 50L |
            | <=25 lakhs | 1 Cr |
            | < 50 lakhs | 2 Cr |
    
    **a5. Mandate Check:**
    
    - Following are the validations for the mandate amount/tenure limit /bank :
        - Amount
            - Min:( New tranche disbursement amount + Outstanding POS)
            - Max: 1Cr
        
        - Tenure
            - Min: Max of  tenures of all ongoing tranches
            - Max: 30 yrs
        - Bank
            - Mandate needs to point to the latest tranche bank
            
    
    a6.Disbursement amount checks:
    
    - Disbursement amount greater than 20 Lacs >> Non STP
    - More than 2 disbursements in a single day >> Non STP
    
    If any of the above validations fail, the application is routed to Non-STP flow.
    
    ~~If the ‘Submit Opportunity’ call fails due to mandate validation errors, DSP will trigger a ‘Submit Opportunity’ web hook containing the failure reason. LSPs are expected to use this information to reinitiate the Mandate API and complete the mandate setup successfully.~~
    
    **~~a5. AML & CIBIL Status Check:~~**
    
    - ~~Verifies both are marked as **successful**.~~
    
    **3.COMMAND CENTRE** 
    
    Attached is the [list of data points](https://docs.google.com/spreadsheets/d/1a9O4jmwPg6_nXeFatjQbZaveh0hbB1vCJIo-Y4Dq5vk/edit?gid=1906805600#gid=1906805600) (refer ‘LOS_CC_fields)to be stored or captured in the LOS backend as well as the fields to be passed to the Command Centre.
    
    **4. If All Checks Pass → STP Flow is Initiated**
    
    The application proceeds via the STP route, triggering the following sequential steps:
    
    1. **~~Client Creation:~~**
        - ~~A client ID is generated in Finflux LMS.~~
            - ~~The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture and storage logic~~
    2. **~~Risk Data Mapping:~~**
        - ~~CIBIL score and KYC flags (e.g., High Risk) are mapped to the client profile.~~
            - ~~The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture and storage logic~~
    3. **~~Loan Creation:~~**
        - ~~Loan is created against the client ID.~~
            - ~~The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture /storage logic~~
    4. **~~AML Monitoring:~~**
        - ~~Automatically triggered after loan creation.~~
            - ~~The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped to the client and the corresponding capture/storage logic~~
    5. **Bank Account & Mandate Linkage:**
        - In case user has added a new bank a./c  then the same is mapped to the existing loan a/c number (ie LAN) ie loan can have multiple bank a/cs mapped to it
        - Mandate needs to point to the latest tranche bank. If tranche or disbursment bank is updated, then. mandate need to carry this latest bank
        - In case, user has updated their mandate via re-mandate flow then the same is mapped to the loan a/c and the previous mandate becomes inactive ie only one active mandate can be associated with a loan a/c at any pt in time
        
    6. **~~Co-Borrower Step:~~**
        - ~~Dummy placeholder; no operations performed.~~
    7. **Charge Application:**
        - PF (Processing Fee) is applied to the tranche
        - **~~Elevate customers** (those with an active Bajaj loan) receive a **PF waiver (₹0 for DSP)**.~~
        - Duplicate fee errors ("Already Applied") are programmatically handled.
    8. **~~Agreement Signing Workflow:~~**
        - ~~Customer sign is attached to the agreement~~
        - ~~Final signed copy and welcome documents are sent to the customer~~
            - ~~NBFC stamps and signs the agreement.~~
    9. **Collateral Addition (Optional based on pledging)**
        - Attach the successfully pledged assets to the existing loan a/c
    10. Tranche creation
        1. New Tranche created against  the loan ID/client ID
        2. The attached sheet outlines the [relevant data](https://docs.google.com/spreadsheets/d/1J4reb5cl5uM14Nbsh2NFaU4vgUIOUhH4GVdcN4bCp8Q/edit?gid=1686442422#gid=1686442422) to be mapped at a tranche level and the corresponding capture /storage logic
    11. Welcome docs trigger
        1. Welcome letter PDF attachment containing the following documents are triggered to the user via email
            - ~~Agreement~~
            - KFS
                - Loan schedule
        2. Following is the email template and template ID
            1. 
- **Edge Cases: NA**
- **Specific Partner Flows(Cred): NA**

## ***Future Scope***

NA

## Additional Requirements /Considerations

- Even though ‘Purpose of loan’ field is captured in the ‘additional details’ flow executed at a loan level, while storing it needs to be stored at a tranche level in and

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