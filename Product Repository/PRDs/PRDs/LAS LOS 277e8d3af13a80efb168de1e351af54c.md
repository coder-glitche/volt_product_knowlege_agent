# LAS LOS

: Priyamvada S
Created time: September 23, 2025 7:18 AM
Status: Not started
Last edited: December 21, 2025 12:48 PM

# **What problem are we solving?**

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User Journey/ Requirements (LOS)

**(B2B2C +B2B redirection)**

## *V0 Scope*

PRE-JOURNEY

JOURNEY

### Step 1: Fetch & Offer generation

Screen A: “Check loan eligibility against your stocks” 

Screen Intent: To capture user details for lead creation

![image.png](LAS%20LOS/image.png)

Journey starts with user entering the below basic details to get started with the ‘loan against shares’ eligibility checks:

- PAN no
    - Regex error: Please enter a valid PAN no
- Mobile no
    - Regex check error: Please enter a valid 10 digit mob no

Post entering the details , user hits the ‘Continue’ CTA on which a new lead is created in Volt BE with  provided user details (PAN + mob no) and user is moved to the next step

Screen B:  “Add your stock portfolio”

Screen Intent: Choosing mode of  sharing user portfolio details

![image.png](LAS%20LOS/image%201.png)

In this screen, user is prompted to choose any of the below 2 options by which they can share their stock portfolio details:

1) Upload of  holding statement where user can  upload their broker’s holding statement 

- User uploads their broker holding statement by hitting the ‘Browse file’ CTA
- Uploaded file should meet the following basic checks:
    - Max file size supported: Upto 5MB
    - Supported file formats: PDF/XLS/CSV
    - Only a single file supported, additional file replaces the previous one
    - File should be a  valid broker holding statement : Considered valid if the file contains list of ISINs pointing to stocks (& not MF );  If list contains atleast one valid ISIN, the holding statement is considered valid

Screen 1a: Processing screen for holding statement upload

![image.png](LAS%20LOS/image%202.png)

For users who went with ‘holding statement upload’ mode by clicking on ‘Browse file’ CTA , post successful file upload,  a ‘processing screen’ will be shown while the following process triggered in the BE:

- BE extracts the following data fields  from the file:
    - ISIN
    - Stock Name/Scrip Name/Symbol
    - Quantity/Balance /Free Qty/Available quantity (#units)
- BE then uses the extracted data and internal  BRE to arrive at the eligible loan amount as follows:
    - First filters out the ineligible funds from the extracted data using the DSP ‘eligible stock list’ maintained in RMS
        - Note: For V0, we’re only considering funds belonging to ‘Stock A’ category towards eligibility calculation .This to avoid dynamic interest rate  variations based on the category of stocks  considered towards eligibility calculation
    - Combines the extracted ‘available units’ with the ‘NAV’  and LTV values of each eligible fund  to arrive at the ‘Eligible loan amount ‘against each value
        - NAV values can be fetched from RMS where they are stored  & refreshed at a regular cadence (via CMOT)
        - Supported LTV values for the ISINs to be fetched from RMS
        - In cases where free units or balance is provided explicitly in the holding statement, use only those unit in order to prevent ISIN rejection at the later pledge state (any one unit fails whole iSIN pledge fails)
    - BE to aggregate loan amount calculated across each fund to arrive at the final eligible amount.
        - Total loan eligibility amount = Formula same as that of OD (formula)
        - Rounding logic for the ‘total eligible amount’ to be same as that of OD (ie round up to nearest 100)

2) Manual entry of stocks along with units through a  ‘search & add stocks manually’ widget

- On clicking this widget, a new screen ,’Add stock’, opens up .

Screen 2a: ‘Add stock’ 

Here user can:

- Select their desired stock by searching by ISIN,Name or Symbol
    - Note: The dropdown will only support those stocks that are whitelisted at DSP end (including the ‘stock a’ category restriction for V0)
- Enter the no of units ( for pledging)against the selected stock

The moment a specific stock is selected by the user in the search bar, the ‘stock summary’ section appears with the following details:

- Stock market value/NAV (non editable): NAV values can be fetched from RMS where they are stored  & refreshed at a regular cadence (via CMOT)
- Selected units value (non editable): This is calculated as :Units selected * NAV
- LTV (non editable): This is pulled from RMS
- Eligible loan limit (non editable): This is calculated as : Units selected * NAV * LTV

This summary info helps user determine the no of units to select to get to their desired loan amount against a stock

Once stock is selected along with units, user  hits ‘Save & add stock’ CTA to save the added stock and continues to the  ‘Confirm loan amount’ screen (ie ‘Screen D’) where they can go ahead with the added fund or add additional funds

Screen C:  Eligible loan limit display

- Once successfully calculated, the max eligible loan limit is displayed to the user along with the following options:
    - ‘Update’ option for user which will take the user back to ‘Screen 2’ where they can  refresh the portfolio via a fresh holding statement upload or fresh manual fund entry
    - ‘See how its calculated’ which will take the user to an education screen with the following details:
        - Details
    - ‘Edit loan limit’ CTA
        - On clicking ‘Edit loan limit’ user is taken to ‘Confirm loan amount screen ’ ie  Screen 5
    - ‘Proceed with max loan limit’ CTA
        - On clicking ‘Proceed with max loan limit’ user is taken to ‘Loan offer screen’ ie  Screen 6

Screen D:Confirm loan amount

This screen displays all the added or extracted stocks along with their available units and corresponding loan amount.  Users can perform the following actions on the screen:

1. Update their eligible limit by performing any of the following supported actions:
    - Deselecting any of the already selected stocks: This will update the total est.loan amount value
    - Editing the quantity against any of the already selected stocks
        - On clicking the edit button against a stock, a new screen opens up with the total available units, selected units,,total stock value (ie available units * market value of each unit), selected stock value (ie (ie selected units * market value of each unit), LTV & eligible loan amount
        - User can modify the selected stock units  which will update the ‘selected stock value’ as well as the ‘eligible loan amount’ .
        - On clicking save, the screen is closed and user lands back on the ‘Confirm loan amount’ screen with the  modified stock units & value reflecting in the respective stock card as well as in the  total loan amount
2. View their  list of ineligible stocks (ie from holding statement extraction)
    - Users can click on the ‘X ineligible stocks found’ widget to see the list of ineligible stocks along with the ‘available units’ and ‘total market value’ against each

Screen E: Loan offer  (TO BE CLOSED)

      b)Annual interest rate: This will be a fixed value that doesn’t vary with the loan amount

      c)Max Tenure: Will be the line tenure with the callout that the amount can be paid back  

         anytime  within the tenure. Line tenure will be 3 years

     e)Processing fee: This will be a fixed value that doesn’t vary with the loan amount

      d)Applicable stocks: The list of eligible stocks against which the eligibility is calculated to 

         be abstracted along with the no of eligible/available units, fund value and as well as eligible 

         loan limit  against each security (all fields to be non editable here)

      e)’Know how the amount is calculated’ hyperlink that opens up a  Info section on how

       the loan limit is calculated  with : a) Clarity on total value of eligible funds and resulting 

       eligible loan amount b) Breakdown of eligible funds along with their fund value & 

     corresponding credit limit c) static informational copy on reasons for fund or units inelgibility

- Backend experience
    
    Eligible/Ineligible funds 
    
    - BE to power the breakdown view of eligible fund list with ‘individual fund’ values & loan eligibility  of each
    - Loan amount update/edit
        - If user updates the loan amount, the backend dynamically adjusts the fund selection (maximising diversification, avoiding high concentration in a single fund ) to support the new amount
        - If user modifies the selected fund list, the loan amount accordingly adjusts

### Step 2: Mobile verification

Mob verification step applicability for LAS varies based on :

1. Whether the customer is an **existing or new** user for **Volt /DSP** 
2. Whether the customer also has an ongoing **LAMF** application at the same time (ie concurrent LAMF application)

The grids below show when mob verification can be skipped and when it's required based on these conditions.

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing |  Mob  Skip | Mob  Skip |
| Volt: New | Mob  Skip | Mob Req |

| CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | If  Mob done, skip them for LAS | If Mob done, skip them for LAS |
| Volt: New | Mob required | NA |

Note: Mobile number skip is supported only when the user enters the **same mobile number** as the one already registered. If a **different number** is detected for the same PAN, mobile verification will be required

### Step 3: Client dedupe

 Post successful mobile verification, following ‘client dedupe’ checks are triggered:

a)Client dedupe is done at Volt end

Here client dedupe of ‘PAN +Product +Asset type’  is to be done at a ‘loan application level’ ie dedupe fails if an active LAS application or a/c already exists

| User has an: | Application stage: | Dedupe Pass/Fail | Next step for user |
| --- | --- | --- | --- |
| Existing LAMF application | -Post pledge confirmation-App.Status= 'In progress' | Pass | Continue with existing LAMF |
|  | Pre pledge init confirmation | Pass | Continue with LAS application |
| Existing LAS application | Post pledge init confirmation | Fails | Continue with existing LAS |
|  | Pre pledge confirmation | Fails | Continue with existing LAS OR
Update existing LAS application (with new fetch data) >>Bank,Mandate,Agreement to be redone |
| Existing LAMF Loan account | - | Pass | Start LAS application |
| Existing LAS Loan account | - | Fails | Manage existingLAS a/c |
|  |  |  |  |

b)Client dedupe is done at DSP end (Fenix)

Here client dedupe of ‘PAN +Product +Asset type’  is to be done at a ‘loan a/c level’ ie dedupe fails only if an active LAS a/c already exists

| User has an: | Dedupe Pass/Fail | Next step for user |
| --- | --- | --- |
| Exisitng LAMF Loan account | Pass | Start LAS application |
| Exisitng LAS Loan account | Fails | Manage exisitng LAS a/c |

 Note: For LAS, ‘Asset type’ is ‘Shares’  

Step 3: KYC & Photo verification

KYC /Photo verification step applicability for LAS varies based on :

1. Whether the customer also has an ongoing **LAMF** application at the same time.
2. Whether the customer is an **existing or new** user for **Volt /DSP** 

The grids below show when KYC can be skipped and when it's required based on these conditions.

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | KYC Skip | KYC Req |
| Volt: New | KYC Skip | KYC Req |

| CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | If KYC done, skip KYC for LAS | KYC req (even if already done ->as diff lender) |
| Volt: New | If KYC  alrdy done, skip KYC for LAS | If KYC done, skip KYC for LAS |

For applicable cases, trigger the same KYC (via Digilocker) and photo verification flow as used in the OD journey.

Note: KYC skip is subject to an expiry window of 2 year

Step 4: Additional details capture

These details (except Purpose of loan field) can be per-filled for LAS application  based on :

1. Whether the customer also has an ongoing **LAMF** application at the same time.
2. Whether the customer is an **existing or new** user for **Volt /DSP** 

The grids below show when additional details can be pre-filled or not based on these conditions.

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | Details pre-fill exc 'Purpose of Loan' | Details req |
| Volt: New | Details pre-fil exc 'Purpose of Loan' | Details req |

However ‘Purpose of loan’ field shoudn’t be pre-filled and instead needs to be input explicitly by the user/MFD

Step 5: Bank a/c set up & verification

For existing customer (Volt or DSP), the bank account details available are pre-filled in the bank a/c input screen.User can etiher go ahead with the recommended a/c or choose to add a new a/c if desired

In case a new bank a/c is added, then the same is verified via bank a/c verification flow as used in the OD flow

In case, an exisitng bank account is chosen, then bank a/c verification step applicability for LAS varies based on :

1. Whether the customer also has an ongoing **LAMF** application at the same time.
2. Whether the customer is an **existing or new** user for **Volt /DSP** 

The grids below show when a/c verification can be skipped and when it's required based on these conditions.

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | Bank.V Skip if same bank chosen by user | Bank.V req |
| Volt: New | Bank.V Skip if same bank chosen by user | Bank.V req |

| CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | If bank.Verification done & same bank chosen by user, skip | Bank.V req |
| Volt: New | If bank.Verification done & same bank chosen by user, skip | If bank.Verification done & same bank chosen by user, skip |

Step 6: Mandate set up

MFD needs to set up the mandate for the LAS application and the journey will be same as that of OD

Step 7: Email entry & verification

Email id will be pre-filled in case available (see below). In addition, users will first be asked to select their **preferred mode of communication**: **SMS** or **Email**.

- Email ID will be pre-filled  based on
    1. Whether the customer also has an ongoing **LAMF** application at the same time (CONCURRENT 'LAS +LAMF' APPLICATION)
    
    | CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
    | --- | --- | --- |
    |  | DSP: Existing | DSP: New |
    | Volt: Existing | Email pre-filled | Email pre-filled |
    | Volt: New | Email   req | NA |
    1. Whether the customer is an **existing or new** user for **Volt /DSP** 

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | Email pre-filled | Email pre-filled |
| Volt: New | Email   req | Email  Req |
- Email verification will be skipped or not based on :
    1. Whether customer has chosen ‘SMS’ as their primary mode: In this case email verification will be skipped
    2. Whether the customer also has an ongoing **LAMF** application at the same time.
    
    | CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
    | --- | --- | --- |
    |  | DSP: Existing | DSP: New |
    | Volt: Existing | If  already done, skip them for LAS | If already done, skip them for LAS |
    | Volt: New | Email verification req | NA |
    1. Whether the customer is an **existing or new** user for **Volt /DSP** 

| NO CONCURRENT 'LAS +LAMF' APPLICATION |  |  |
| --- | --- | --- |
|  | DSP: Existing | DSP: New |
| Volt: Existing | Email verification skip | Email verification skip |
| Volt: New | Email verification req | Email verification skip |

Note:  

- Email verification step will continue to be before the agreement step ie email entry/verification>>Agreement>>Pledge.
- Email verification skip is only applicable for cases where user continues with the pre-filled email. If the user **chooses to update** the email ID, they must **verify the new email** via **OTP**.

Step 7: KFS /Agreement signing

In LAS, KFS/agreement step comes before pledging step to avoid user having to come back after doing the manual heavy lifting in pledge step. The agreement redirection flow remains same as that of OD. 

PFA the LAS agreement & KFS templates

---

### Step 7: Pledging

Screen A: Review/Enter pledge details 

Screen intent: User to review their pledge amount and provide demat /ac details (ie BO ID)

Post signing the agreement, user lands on the ‘Pledge’ screen where user will be shown the  total pledge amount (ie portfolio to be pledged). MFD is  then asked to enter the client’s demat a/c ID or BO ID (DP id + Client ID) to initiate pledging process.

Note: In V0, users cannot edit the funds post the pledge context screen (ie  PRF generation)

The system extracts the **DP ID** from the entered Demat account ID.

- Demat ID format of CDSL DPs:  DP id +Client ID (16 digits)
    - 1208160012345678
- Demat ID format of NSDL DPs: Prefix ‘IN’+ DP id +Client ID (16 digits w/o prefix)
    - IN300214 12345678
- A backend validation is triggered to confirm the DP ID (list of DP IDs).Upon successful validation, the corresponding **DP Name** is fetched and displayed to the user.

Edge /error cases:

-In case an invalid demat a/c ID is entered, need to throw an inline error message “ Please enter a valid demat a/c id’

Screen B: Pledge process context/education screen

Once the DP is validated, the system checks for the availability of PRF and one of the following outcomes is possible:

**Case 1: HTML PRF Template Available** (REQ NOT A BLOCKER)

ie If User’s DP ID falls into one of the following top  X  DP for which  PRF is configured in the BE as a HTML template :

- ~~SMC~~
- Sharekhan
- ~~Motilal~~
- Samco
- Religare
- ~~Bonanza~~
- Here the education screen will reflect the following steps for pledge process:
    - Step 1: Download /Email your pre-filled PRF form
    - Step 2:Print, physically sign and courier the PRF form to your DP (offline step)
    - User clicks continue to go ahead

Case 2: **Non-Templatized Blank PRF Available**

User’s DP ID falls into one of the following DPs for which only non-templatized blank PRF is available in DSP BE 

- Anand Rathi>> DP ID:  & PRF template:
- Axis Bank
- Groww
- HDFC Securities
- ~~ICICI Bank~~
- IIFL
- ~~NK Securities~~

- Here the education screen will reflect the following steps for pledge process:
    - Step 1: Download /Email your blank PRF form
    - Step 2: Fill the blank PRF with details provided by Volt
    - Step 3: Print the filled form, physically sign and courier the PRF form to your DP (offline step)
    
    User clicks continue to go ahead
    

**Case 3: PRF Template Unavailable in Backend**

ie the PRF template is not available digitally in the backend

Here the education screen will reflect the following steps for pledge process:

- Step 1: Visit the respective **broker’s website to access & download the PRF**
- Step 2: Fill the blank PRF with details provided by Volt
- Step 3: Print the filled form, physically sign and courier the PRF form to your DP (offline step))
- User clicks continue to go ahead

  User clicks continue to go ahead

Screen C: ‘PRF download + courier’ screen

On user. moving ahead from the education screen, ‘pledge request ID’ gets created  and one of the following flow gets triggered :

C**ase 1: HTML PRF Template Available** 

- PRF template gets auto generated and will carry the following pre-filled  details
    - Selected fund details:  ISINs, Units
    - Pledgor and Pledgee information:  DP ID, Client ID, Name
    - Agreement number
- User can either email the generated PDF to their email id or download the same to their device
    - In case user chooses to get it emailed and hits ‘email’ CTA, a pop up appears where they can input their email ID
    - ~~User can either go with the pre-filled email/update email id by entering a new email and verifying the same with an OTP~~
- On user moving ahead from download/email card, the ‘Print, sign or courier’ card auto opens
    - User will be  instructed to sign the received PRF form and send it to the DP address shown in the UI (with a ‘copy’ option)
        - In case DP address is not available in BE, user will be asked to get the DP address by contacting their broker and to physically mail the PRF to the same address.
        - Following are the list of DP address available with DSP

Case 2: **Non- Templatized Blank PRF Available**

- Blank PRF template gets auto generated  on user landing on the screen
- User can either email the generated to their email id or download the same to their device
    - In case user chooses to get it emailed and hits ‘email’ CTA, a pop up appears where they can input their email ID
- On user moving ahead from ‘Download/email PRF’ card, the ‘Fill details’ card auto opens ‘
    - Here user is instructed to manually fill in the blank PRF form by  referring to the details provided by Volt in UI as well as a downloadable PDF. Details contained includes:
        - Selected fund details:  ISINs, Units
        - Pledgor and Pledgee information:  DP ID, Client ID, Name
        - Agreement number
- On user moving ahead from ‘Fill details’ card, the ‘Print, sign or courier’ card auto opens
    - User will be  instructed to sign the  filled PRF form and send it to the DP address shown in the UI (with a copy option)
        - In case DP address is not available in BE, user will be asked to get the DP address by contacting their broker and to physically mail the PRF to the same address.
        - Following are the list of DP address available with DSP

**Case 3: PRF Template Unavailable in Backend**

- On user landing on the screen, the ‘Get access to PRF’ card auto opens
    - User will be instructed to get in touch with their broker to get hold of the PRF (pledge book etc)
- On user moving ahead from ‘Get access to PRF’ card , the ‘Fill details’ card auto opens ‘
    - Here user is instructed to manually fill in the PRF form by  referring to the details provided by Volt in UI as well as a downloadable PDF. Details contained includes:
        - Selected fund details:  ISINs, Units
        - Pledgor and Pledgee information:  DP ID, Client ID, Name
        - Agreement number
- On user moving ahead from ‘Fill details’ card, the ‘Print, sign or courier’ card auto opens
    - User will be  instructed to sign the  filled PRF form and send it to the DP address shown in the UI (with a copy option)
        - In case DP address is not available in BE, user will be asked to get the DP address by contacting their broker and to physically mail the PRF to the same address.
        - Following are the list of DP address available with DSP.Business to review this address on a periodic basis (6 months) to ensure data is current/accurate

Screen D: ‘Line creation in progress’ screen

User moves ahead from the ‘pledge steps’ screen by hitting ‘Continue’  and  land on the line creation pending ‘screen’  while the Volt BE hits the ‘submit opportunity’ API which trigger the following API validations 

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
- **Dedupe Check:**
    - Re-validates de-duplication on the combination of `PAN + Asset type + Product`
- **Agreement Reference IDs check:**
    - Confirms that the 4 utility reference IDs passed in Submit Opportunity match those passed at the time of Loan contract generation ie Photo,Additional data ,KYC, Bank verification
- **Pledge ID Validation (for Submit Opportunity V2 API):**
    - Ensures all pledge reference IDs are in an **approved state**.

If any of the above API validations fail, Volt will  re-attempt the ‘submit opp’ API with correct data. On successful API checks,  line is created at Volt’s end , CLAW workflow initiated in Fenix BE & user is moved to the  ‘Awaiting pledge confirmation’ screen on LMS

Screen E: ‘Awaiting pledge confirmation’ screen

Backend

The CLAW workflow check continues in the Fenix BE, following are the checks done as part of this workflow:

**A. Skipping of AML Check**

- AML check **skipped** at this stage **if already completed** post-mandate setup.
    - If not completed, to re-perform these checks again at this stage:
        - If checks fails(ie match found in trawizz), then application moves to checker flow
        - If checks pass successfully, then workflow continues to the next step
            - AML success if no match found in trackwizz

**B. Document Check**

- **Document Availability Validation:**
    
    Confirms that all mandatory documents are available:
    
    - Aadhaar
    - PAN
    - KYC report (fetched from Digio)
- In case any of these docs are not available, the workflow is blocked and system will try to pull these docs in real time from Digio. Post successful pull, the workflow is unblocked

After the above validations are complete, the following checks are executed to determine whether the flow will follow the STP or Non-STP path:

- Following five sub-checks are executed:
    
    **a1. Sourcing Channel Validation:**
    
    - Verifies if the sourcing channel (e.g.,Volt) is enabled for the STP flow
        - Eg: In initial CUG process, STP is disabled for sourcing channel partners
- a2. KFS **Financial Parameter Thresholds for STP:**
    
    Validates that parameters passed in the KFS are within the below mentioned values:
    

| **Parameter** | **STP Range** |
| --- | --- |
| Mandate Amount checks | STP range:
• Min: Not yet closed 
• Max:1 Cr
Non STP range: 
• If outside of the above range, route to NON STP |
| Tenure | STP range:
• 
Non STP range
• If above conditions are not met, route to non STP flow |
| Interest Rate | • STP range: 9.99%-15%
• Non STP range: 9%-9.99% |
| Processing Fees | STP range:
• -Min 0 (or as per LSP commercials)
• -Max :10,000 or 5% of disbursement TRANCHE amount (excluding GST), whichever is higher;
Non STP range: 
• No NON STP .Anything outside of the above will be rejected |
| Margin Pledge Fees |  |
| Annual Maintenance Fees |  |

**a5. Mandate Check:**

- Following are the validations for the mandate amount/tenure limit /bank :
    - Amount
        - Min: TBC
        - Max: 1Cr
    - Tenure
        - Min: Mandate tenure >= Max( Tranche tenures)+ 3 months;
        - Max: No max value

If any of the above validations fail, the application is routed to Non-STP flow where Ops can either reject or approve the applications.On completion of these checks, workflow will be blocked for ‘pledging status’ confirmation (relayed by CMS via PMR consumption).

On finally receiving pledge status confirmation, line creation will be initiated in Fenix BE involving the following steps:

1. **Client Creation:**
    1. A client ID is generated in Finflux LMS.
2. **Risk Data Mapping:**
    1. CIBIL score and KYC flags (e.g., High Risk) are mapped to the client profile.
3. **Loan creation:**
    1. Loan is created against the client ID.
4. **AML Monitoring:**
    1. Automatically triggered after loan creation.
5. **Bank Account & Mandate Linkage:**
    1. Mandate will be mapped to tranche disbursement a/c for first drawdown
6. **Co-Borrower Step:**
    1. Dummy placeholder; no operations performed.
7. **Charge Application:**
    1. PF (Processing Fee) is applied to the tranche
8. **Agreement Signing Workflow via legality:**
    1. Customer sign is attached to the agreement
    2. NBFC stamps and signs the agreement.
    3. Final signed copy and welcome documents are sent to the customer
9. **Collateral Addition:**
    1. Pledge limit check
    2. Attach the successfully pledged assets to the created loan a/c
10. **Trance limit block**
    1. We block the tranche limit
11. **Tranche Disbursement**
    1. Initiate disbursement
    2. Wait for debit confirmation
    3. Wait for credit confirmation
12. **Tranche creation**
    1. Tranche created in Finflux against the loan ID/client ID after successful disbursement
13. **Polling for tranche creation status from Finflux**

FE

During all this time, user will be shown the following info in frontend:

- Prominently display users need to ensure they are sending the PRF to DP (with address & PRF attached in UI) so that their pledge process is initiated
- Need to provide users with a rough estimate on the Pledge confirmation TAT
- User will also have an option to initiate and queue a withdrawal  request by hitting the ‘Set up Now’ CTA upon which
    - Existing disbursement queuing flow of amount selection and subsequent OTP verification flow will be triggered
        
        Note: Queuing the disbursement removes the need for the user to track pledge status or return to complete the process. Once the pledge is confirmed and the DSP account is created, the disbursement will be auto-triggered.
        
- If user were to click on the ‘back button’ on this screen they will land on the LMS dashboard page

Edge case

- If no confirmation on pledge received within 7 days of sending the PRF to DP (either pledging rejected or PRF not sent by user), then a ‘Pledge incomplete’ screen to appear to  inform user that their “pledge request couldn’t be completed :
    - This screen will carry a generic list of potential failure reasons along with an option to retry sending ‘PRF’. List of failure reasons include:
        - Certain fund units are already pledged and unavailable
        - The PRF wasn’t sent to their DP
        - Certain funds not eligible as per the lender’s policy.
            - in this case, prompt users to confirm fund eligibility by checking the lender-approved ISIN list in the shared ‘ PRF details’ PDF before resending PRF

**3. If All Checks Pass → STP Flow is Initiated**

The application proceeds via the STP route, triggering the following sequential steps:

1. **Client Creation:**
    1. A client ID is generated in Finflux LMS.
2. **Risk Data Mapping:**
    1. CIBIL score and KYC flags (e.g., High Risk) are mapped to the client profile.
3. **Loan creation:**
    1. Loan is created against the client ID.
4. **AML Monitoring:**
    1. Automatically triggered after loan creation.
5. **Bank Account & Mandate Linkage:**
    1. Mandate will be mapped to tranche disbursement a/c for first drawdown
6. **Co-Borrower Step:**
    1. Dummy placeholder; no operations performed.
7. **Charge Application:**
    1. PF (Processing Fee) is applied to the tranche
8. **Agreement Signing Workflow via legality:**
    1. Customer sign is attached to the agreement
    2. NBFC stamps and signs the agreement.
    3. Final signed copy and welcome documents are sent to the customer
9. **Collateral Addition:**
    1. Pledge limit check
    2. Attach the successfully pledged assets to the created loan a/c
10. **Trance limit block**
    1. We block the tranche limit
11. **Tranche Disbursement**
    1. Initiate disbursement
    2. Wait for debit confirmation
    3. Wait for credit confirmation
12. **Tranche creation**
    1. Tranche created in Finflux against the loan ID/client ID after successful disbursement
13. **Polling for tranche creation status from Finflux**

## 

---

# **Design**

---

# **Analytics**

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