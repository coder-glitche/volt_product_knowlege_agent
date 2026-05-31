# [DSP] KYC v2 (including CKYC)

: Saksham Srivastava
Created time: January 28, 2025 8:07 PM
Status: Ready for Tech
Last edited: August 13, 2025 12:55 PM

# **What problem are we solving?**

Currently for customers to complete KYC on DSP, they only have one KYC mechanism - Digilocker. 

Key pain points of customers on the KYC step - 

1. Frequent Digilocker downtime - 2 major outages/week. Customer conversion on KYC falls to zero during such downtimes, no backup flows for KYC implemented here. 
2. Friction for the customer to complete the KYC journey - 
    1. Customers have to input their complete Aadhaar number, DL PIN, Aadhaar OTP to complete KYC. 
    2. Partners when completing KYC of the customers need them to share Aadhaar OTP and DL PIN to complete KYC of the customer. 

---

# **How do we measure success?**

Current drop-off on the KYC documents fetch step is 23.5%, ie, out of 100 customer landing on the Digilocker page more than 23 customers don’t complete the digilocker journey. 

- Reduce drop-off from the KYC step to  15%.
- > 50% of the customers should be able to complete KYC in less than 10 mins.

---

# **How are others solving this problem?**

Industry standard for the KYC conversion rate is ~75%

- Navi
    1. CKYC is found for 90% of the customers and for 90% out of these customers it passes validations. ~20% customer go through the OKYC flow. 
    2. OKYC flow provider - Digitap. Customer has to enter Captcha, Aadhaar is entered on Digitap UI. 
    3. Overall conversion of 75%(D1 conversion 60%, D7 conversion 75%). Step wise success percentage don’t know current. 
        
        ![mermaid-diagram-2025-01-20-161123.svg](%5BVolt%20LOS%5D%20KYC%20optimisations/mermaid-diagram-2025-01-20-161123.svg)
        
- Cred
    1. Cred has 6-7 lenders each one of them have their own KYC flows. Some have their own stacks which they want LSPs to integrate some allow LSP to do KYC and push documents. 
    2. ~50% of the customers have Digilocker account.
    3. Depending on the lender the KYC conversion is between 50-80%. 
    4. EKYC is limited KYC, lending limit is ₹60k
    5. OKYC flow might go down in near future, Digilocker should be there.
    6. Recent cases of DL outage were because of DL issues and not UIDAI issues. OKYC flow is was working.
    7. Suggests the vanila digilocker flow as after March 2024, opening a DL account does not require you to enter aadhaar which means. DL accounts can be there which don’t have Aadhaar in them. These account are called empty accounts, 1-1.5% cases in Cred. 
    8. In addition to the Navi checks, he mentioned to verify Father’s name as well.
    
    ![IMG_4567.HEIC](%5BVolt%20LOS%5D%20KYC%20optimisations/IMG_4567.heic)
    
- Groww
    1. Connected with the investments product onboarding person, credit team uses their KYC stack only. Mandate credit team have built themselves. 
    2. Only PAN (number) verification through NSDL. Partial verification.
    3. Digilocker - Aadhaar pulled
    4. Complete PAN verification through NSDL - this twice verification costs more but provides better customer experience
    5. In case DL is down, customer flows to manual document upload. These documents are manually verified. 
    6. Very small percentage people go to this flow (same as DL downtime)
    7. Not comfortable with sharing conversion numbers
- Cashe
    - Earlier:
        - CKYC first, then OKYC.
        - Conversion number: Won’t be able to disclose
    - Current:
        - Only digilocker, done upfront in the journey. Both PAN and Aadhaar documents are pulled.
        - PAN verification done through NSDL before DL. If they are unable to pull PAN from DL, they move past.
        - CashE compliance called out CKYC and OKYC non compliant. CKYC - RBI had called CKYC unreliable, OKYC - Non compliant because of scrapping.
        - They do VKYC for cases where the loan amount in more the ₹50k
        - Conversion number: “It’s not bad” 10% down after moving to Digilocker

---

# **What is the solution?**

## Requirements overview (optional)

- Provide an option to LSPs to complete KYC of customers in DSP UI. The complete KYC including NSDL PAN verification + documents pull + selfie match will be orchestrated in DSP UI reducing effort required from LSPs to integrate KYC. This will include Digilocker and CKYC as methods of document download,
- Provide APIs to LSPs to complete *KYC for customers (*NSDL PAN verification + documents pull + selfie match*)*. This will give LSPs the flexibility to build their own UI and experience for completing KYC for customers.
- Ensure *regulatory compliance* and *improve success rates* by making the KYC journey simpler and clearer for end users.

## KYC journey

[https://www.figma.com/board/BnAGa22WS2rTGoXyXo6FKG/DSP-KYC-flow?node-id=620-767&t=1KSg9tP4o6UQPyah-11](https://www.figma.com/board/BnAGa22WS2rTGoXyXo6FKG/DSP-KYC-flow?node-id=620-767&t=1KSg9tP4o6UQPyah-11)

### KYC flow :

- Selfie optional flow
    
    LSPs will have the following options: 
    
    1. Option #1: 
        1. Send oppId (PAN and mobile number mapped to the oppId are the actual required input)
        2. Fenix will respond with a *unique KYC link* that the LSP can present to the user (e.g., via SMS/Email/app).
        3. This link will have UI for NSDL PAN verification, CKYC (search, download and validation), Selfie (Capture, liveliness and Match), Digilocker and deviation handling as well. 
    2. Option #2: 
        1. Sending Full name, DOB along with OppId can skip the NSDL PAN verification step for end customers. 
    3. Option #3: 
        1. Use granular APIs that LSPs can integrate and build their UI on top of it. Here state management and handling will have to be done by the LSP. 

## Integration and BE requirements:

NSDL PAN verification
**Note: 
1.** This is not implemented in the current version as we dont  have the NSDL integration done yet. This will be picked up post NSDL onboarding is done. **** 
2. PAN verification in the current flow will be done via Signzy at the end of successful KYC verification. 

1. Flow #1: 
    1. Customer will see the form to enter Name and DOB. 
    2. Post filling the details, NSDL PAN verification API will be triggered. 
        
        [NSDL PAN Verification API _ HyperVerge.pdf](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/NSDL_PAN_Verification_API___HyperVerge.pdf)
        
    3. Success criteria for PAN verification - all of the below should be satisfied. If PAN verification is successful, LSP will be sent PAN verification successful webhook. 
        1. panStatus: “EXISTING AND VALID”
        2. name: "MATCHING"
        3. dateOfBirth: "MATCHING" or “NOT-MATCHING”
        4. aadhaarSeedingStatus: "Y"
        
        <aside>
        💡
        
        - Name needs to be exactly matching as PAN is the POI for loan application. The name of the applicant in our application should be the exact legal name.
        - DOB does not need to match exactly. We only need to validate if the age of the customer is between 18 and 70 years. This can be checked from the DOB that comes in the CKYC download or from digilocker (as per the current process).
        </aside>
        
    4. PAN number should be in the format  **XXXPX1234X.** 4th letter of the PAN should be “P” to indicate that the PAN belongs to an individual. If this requirement is not matched return error `“PAN in opportunity does not belong to an individual”` to LSPs in a webhook.  PAN verification API should not be triggered in this case. This error will result in KYC failure. 
    5. In case panStatus ≠ EXISTING AND VALID, “PAN entered is not a valid PAN” error will be shown to the customer in UI and given as a webhook to LSP as well. This error will result in KYC failure. 
    6. In case aadhaarSeedingStatus ≠ Y, “PAN is not linked to Aadhaar” error will be shown to the customer in UI and given as a webhook to LSP as well. This error will result in KYC failure. 
    7. Customers can trigger PAN verification thrice. After 3 tries in 15 mins. “Maximum attempts reached for PAN verification” error will be shown to the customer in UI and given as a webhook to LSP as well. The number of retries and the cooldown time should be in a config that can be changed later. 
2. Flow #2: 
    1. DSP will perform NSDL PAN verification check before rendering sending the KYC link. 
    2. Once PAN verification is successful, KYC link will be sent to LSP along with PAN verification successful webhook. Selfie capture UI should be shown to the user, skipping the PAN verification UI. 
    3. In case PAN verification fails as per success criteria mentioned [here.](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)%20189e8d3af13a803aa872e67345979451.md) Error messages mentioned in point d, e, f, and g of flow #1 will be shared with LSP. These errors will result in KYC failure. 
3. Flow #3:
    1. LSP will hit the KYC init API, DSP will internally hit PAN verification API.
    2. If PAN verification is successful, a success callback will be given to LSP. 
    3. In case any error mentioned in point d, e, f, and g of flow #1 occur, corresponding error message will be shared with LSP. These errors will result in KYC failure. 

CKYC search and download OTP trigger

1. Flow #1:
    1. “start” API from the HV CKYC suite will be called with necessary inputs. This API does CKYC search and also triggers CKYC download consent OTP for the user.
    2. API documentation. 
        
        [s&d_req_res (1).pdf](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/sd_req_res_(1).pdf)
        
    3. Sample request:  
        
        ```jsx
        {
           "idNo": <pan>, // Enter user's PAN here 
           "idType": "C", // C corresponds to idType PAN. This can be made constant
           "dob": "dd-mm-yyyy", // Enter user's DOB here
           "mobileNo": "1234567678" // Enter user's mobile number here   
        }
        ```
        
    4. If search and OTP trigger are successful, following response will be given. Success callback should be given to LSPs. Customer will move to the OTP input screen. 
        
        ```jsx
        {"status": "success", "statusCode": "200", "result": "OTP has been sent to the registered mobile number <mobileNo>"}
        ```
        
    5. If user’s records are not present with CKYC, following response will be given. 
        
        ```jsx
        {"status":"failure","statusCode":"404","error":{"code":"ER_CKYC_SEARCH_AND_DOWNLOAD","message":"No record found"}}
        ```
        
    6. If the mobile number that LSP sends doesn’t match with the one in CKYC records, following response will be given.
        
        ```jsx
        { "status": "failure", "statusCode": "400", "error": { "code": "ER_REQ_VALIDATE", "message": "Download failed. Auth Factor does not match that registered in the KYC record" }}
        ```
        
    7. If mobile number for the user is not registered in CKYCRR, following response will be given. 
        
        ```jsx
        { "status": "failure", "statusCode": "400", "error": { "code": "ER_REQ_VALIDATE", "message": "Download failed. Mobile number is not registered in the KYC record. Please download using bulk file methods" }}
        ```
        
    8. For the above error cases following would be the error messaging. User error messages should be in a config that can be configured later without need of FE deployment. 
        
        
        | **Error message from HV** | **Error message sent in LSP webhook** | **Error message shown to user** |
        | --- | --- | --- |
        | No record found | CKYC record doesn’t exist for the user | Direct redirection to Digilocker - No error shown to the user |
        | Download failed. Auth Factor does not match that registered in the KYC record | User mobile number does not match with mobile number is CKYC records | Direct redirection to Digilocker - No error shown to the user |
        | Download failed. Mobile number is not registered in the KYC record. Please download using bulk file methods | Mobile number of the customer is not linked with CKYC records | Direct redirection to Digilocker - No error shown to the user |
    9. In case any of the above errors are encountered, customer will be redirected to Digilocker flow. This will not be a digio link but will be a DSP link. 
2. Flow #2:
    1. Same as flow #1.
3. Flow #3:
    1. Success response will be same as flow #1, LSP should be given success webhook. 
    2. In case of any of the errors mentioned in flow #1 occur, LSP will be required to complete KYC of the customer via digilocker. 

CKYC download OTP verification and resend OTP

1. Flow #1 and #2:
    1. User will land on the OTP input screen and input the OTP shared on his/her registered mobile number. 
    2. The OTP entered by user will be used to call the “validateOtpAndDownload” API. 
        
        [s&d_req_res (1).pdf](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/sd_req_res_(1).pdf)
        
    3. Sample request: 
        
        ```jsx
        {
           "otp": <otp number collected from end user>,
           "mobileNo" : <10-digit mobile no sent in the first request> 
           "retry" : "yes/no" // to be passed as yes if otp needs to be resent       
        }
        ```
        
    4. Success response will include the CKYC download data as well. Sample response is in the API documentation. A success callback should be given to the LSP. 
    5. In case user inputs incorrect OTP, following would be the response
        
        ```jsx
        { "status": "failure", "statusCode": "400", "error": { "code": "ER_REQ_VALIDATE", "message": "Invalid OTP entered. Remaining attempts: <count>" }}
        ```
        
    6. User can try entering the correct OTP thrice. After 3 tries further validation requests will fail. Following is the response in case we try validation post exhausion of 3 attempts. 
        
        ```jsx
        { "status": "failure", "statusCode": "400", "error": { "code": "ER_REQ_VALIDATE", "message": "Download failed as OTP validation was unsuccessful" }}
        ```
        
    7. Resend OTP option will be enabled only post 90 seconds of triggering OTP. The user can try resending OTP 3 times. The same API is used with the following changes.
        1. “otp” param should be blank
        2. “retry” should be “yes”
    8. OTP resend Success response: 
    9. In case OTP resend is tried before 90 seconds:
    10. In case OTP resend exceeds the max 3 attempts of resend OTP: 
    11. All the above success and error events will be shown in UI and will be shared with LSP through webhooks. A similar config to configure user facing error messages should be made for this step as well.  For all the errors that are marked as CKYC terminal errors, the customer will be redirected to the Digilocker flow. 
        
        
        | **Error message from HV** | **Error message sent in LSP webhook** | **Error message shown to user** | CKYC terminal error  |
        | --- | --- | --- | --- |
        | Mobile number doesn't match with the one passed in download request | Mobile number doesn't match with the one passed in download request | Direct redirection to Digilocker - No error shown to the user | Yes |
        | Invalid OTP entered. Remaining attempts: <count> | Invalid OTP entered. Remaining attempts: <count> | Copy in design | No |
        | Download failed as OTP validation was unsuccessful | Max attempts reached for OTP verification | Copy in design | Yes |
        | Resend OTP will be enabled after 90s from first request | Resend OTP will be enabled after 90s from first request | Handling in design | No |
        | Download failed. Number of attempts to resend OTP | Download failed. Number of attempts to resend OTP | Copy in design | Yes |
2. Flow #3
    1. will have to create a wrapper API on top of OTP verification + CKYC validation

Internal validations on CKYC download data

1. Common for Flow #1, #2 and #3
    1. Check if Proof of possession of aadhaar document is available or not - Documents are present in the imageDetails object within the verify OTP success response. Documents have codes basis the document type. Mapping of document type and code is [here](https://docs.google.com/spreadsheets/d/1bXLxD6Si3J0PAiXUqJ7lfTjdTLzMg8mWcTyxCIek5Tg/edit?usp=sharing). Need a check that will ensure if CKYC data has necessary ID documents or not. In phase 1, we will consider only “Proof of possession of Aadhaar” (code:04) as a valid ID document. In future, we may consider other documents as valid ID documents. That change should only be a configuration change. If the document is not available, send an error that “Required ID documents not availble in CKYC”. 
    2. Customer age is between 18 and 70 years - Refer to the dob field in CKYC download data to check if the customer’s age is between 18 and 70 years. If not send an error that “Customer age in not within 18-70 years.” **Note:** This is handled via signzy API called at the end of successful CKYC validation. 
    3. In both of the cases the customer will be moved to the Digilocker flow.

Hyperverge CKYC validation API

1. Common for Flow #1, #2 and #3
    1. Sample input for the validation API 
        
        ```jsx
        {
          "first_name": "SAKSHAM SRIVASTAVA",
          "last_name": "SRIVASTAVA",
          "dob": "11-06-1999",
          "address1": "S/O: Ashish Kumar Srivastava,near chhoti",
          "address2": "bazar,H.NO. 24 kanoongopura",
          "address3": "DAKSHINI,Bahraich,Kaiserganj,Bahraich,Bahraich,Utt",
          "city": "Bahraich",
          "district": "Bahraich",
          "state": "UP",
          "country": "IN",
          "pincode": "271801",
          "aadhaar": "XXXXXXXX4049",
          "mask_aadhaar": "yes",
          "imageDetails": [
                                {
                                    "code": "02",
                                    "imageUrl": <s3 URL of the customer image>
                                },
                                {
                                    "code": "04",
                                    "imageType": <s3 URL of the proof of possession of aadhaar document>
                                }           
          ],
          "returnOcrDump": "yes"
        }
        ```
        
    2. first name, last name, dob should be taken from the CKYC download response. 
    3. address details should be taken from the CKYC download response. Only permanent address details should be taken.
    4. Standalone photo of the customer that we get in the CKYC downloaded data should be added in place of the imageUrl with code: 02
    5. Photo of the proof of possession of aadhaar document should be aaded in place of the imageUrl with code: 04
    6. The API checks if the name, dob, address, etc details match with the proof of possession of aadhaar. 
    7. The API also checks if the photo of the customer passed matched the photo in proof of possession of aadhaar. 
    8. No other OVD will be used for CKYC validation for now
    9. The success of the validation will depend on match thresholds of the following parameters:
        1.  **aadhaar faceMatch matchFound should be TRUE** and aadhaar faceMatch score should be above 50
        2.  **aadhaar first name matchFound , aadhaar first name score should be above 80**
        3.  **aadhaar last name matchFound, aadhaar last name score should be above 80**
        4.  **aadhaar address1 matchFound, aadhaar address1 score should be above 80**
        5.  **aadhaar country matchFound, aadhaar country score should be 100**
        6.  **aadhaar pincode matchFound, aadhaar pincode score should be 100**
        7.  **aadhaar dob matchFound, aadhaar dob score should be 100**
        8. ValidPoa has “aadhaar” 
    10. If any of the above criteria is not matched, the user will be given an error that the “CKYC validation failed” and the customer will be moved to Digilocker. 

Selfie capture + liveliness check + selfie match

1. Flow #1:
    1. Post CKYC validation, user will land on the selfie verification UI. 
    2. User will capture selfie, this will be checked for liveliness (through the current Digio API). 
    3. In case liveliness is successful, the same selfie will be matched with the CKYC standalone image of the customer. If the match percentage is above above STP threshold then KYC for the customer will be successful. 
    4. If the selfie match is below STP threshold, the customer should be moved to Digilocker. 
    5. Post digilocker, the selfie will be matched with the Digilocker selfie of the customer, if the match is above STP threshold then KYC is success, if below STP but above rejection threshold then the customer will go into photo deviation, and if the match threshold is below rejection threshold then KYC will be rejected for the customer.
2. Flow #2
    1. Same as flow #1. 
3. Flow #3
    1. For CKYC, LSP will have to use the selfie match APIs to match customer selfie with CKYC standalone image. 
    2. In case selfie match falls below STP threshold with CKYC image, LSP will have to do the Digilocker flow for the customer and then call selfie match API again to match customer selfie and Aadhaar image from Digilocker. 

## DSP FE requirements

https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=3270-2

DSP UI will give theming customisation to LSPs. Following will be the customisation that we will be providing out of the box. 

1. Primary color
2. Secondary color
3. Primary font (will be used for H1s)
4. Secondary font (will be used for everywhere else other than H1s)

## GTM requirements

GTM requirements are collated [here.](https://docs.google.com/spreadsheets/d/1PAnwqh9mXmuL4SNMD5Umx-O38wuBkkvsOuL1YZXP83Q/edit?usp=sharing) 

## Command Center requirements

For loan creation approval task (QC)

1. Applicant details → POI verification
    1. Verification status - Since PAN verification will eventually become mandatory, following should be a sample value “Verified via NSDL at 27-May-2025, 20:50:09”
    2. Document source - TBF
    3. PAN-Aadhaar seeding source - In case, customer KYC is done through CKYC, following should a sample value “CKYC”
2. Proof of address Details → POA verification
    1. Verification status - For KYC through CKYC, following should be a sample value “Verified via CKYC at 27-May-2025, 20:50:09”
    2. Document source - For KYC through CKYC, following should be a sample value “CKYC”
3. Proof of possession of Aadhaar document photo from CKYC should be shown in the Aadhaar section of the document viewer

## Analytics requirements

Data requirement are in [this](https://docs.google.com/spreadsheets/d/19960-G_hYTtnK20_XwexSR0RWwX1cYWvk1fotAo9ufY/edit?usp=sharing) sheet. 

## Leadsquared requirements [WIP]:

In the current flow the events passed for KYC are as below:

With the updated KYC flow, the process includes multiple stages where failures can occur, making it essential to track and communicate each step's status more granularly through the CRM. The CRM must keep the executive informed in real-time so they can proactively assist the customer wherever required.

1. **Flow Initiation**:
    
    The process starts with an internal trigger to the hyper verge. If there's a failure at this stage, it must be pushed to the CRM immediately so the executive can intervene and guide the customer and also flag to the issue internally.
    
2. **KYC OTP Trigger**:
    
    Once KYC is initiated, an OTP is sent to the customer. If the OTP fails to trigger, this must be flagged in the CRM for executive follow-up.
    
3. **Step-wise KYC Monitoring**:
    
    Each subsequent KYC step may result in a failure. These include:
    
    - Mobile number match
    - CKYC search and download check
    - CKYC Validation check
    - Photo/selfie capture and liveness check
    - Selfie with standalone photo match threshold check
    
    At each point:
    
    - If there's a failure, the failure reason must be logged and sent to CRM.
    - If a fallback to **Digilocker reroute** is triggered, both the reroute status and result must be captured.
4. **Selfie Capture & Liveness Check**:
    
    The selfie capture and liveness result should be shared with the CRM. This allows the executive to track if the customer is progressing properly or needs assistance.
    
5. **KYC Success/Failure**:
    
    Once KYC is completed:
    
    - If successful, the completion status should be marked in CRM.
    - If unsuccessful, the failure reason and any deviation from the expected path must be logged and pushed to CRM.
    - In addition to this the deviation flow result must be pushed to the CRM as well.

**List of CRM events to be pushed to LSQ:**

The following are key events and failure points identified across the KYC journey. These will be mapped to Step 9 triggers and surfaced to the CRM for executive visibility:

1. **HyperVerge Trigger Failure** → Triggers **Step 9**
2. **KYC OTP Trigger Failure** → Triggers **Step 9**, marks **Step 9 Initiated**, and proceeds if **CKYC is completed**
3. **CKYC Mobile Number Mismatch** → Triggers **Step 9**, results in **Step 9 Reroute Failure**
4. **CKYC Search & Download Failure** → Triggers **Step 9**, results in **Step 9 Reroute Failure**
5. **CKYC Validation Failure** → Triggers **Step 9**, results in **Step 9 Reroute Failure**
6. **Photo Captured**
7. **Liveness Check Failure** → Deviation triggered → Failure or Success
8. **CKYC Completed** 
9. **Digilocker Initiated** 
10. **CKYC Completed (via fallback)** 

> Final event mappings will be confirmed post Wednesday’s discussion with Rishi.
> 
> 
> **Objective:** Ensure all major failures are captured and shared to CRM for timely executive intervention.
> 

## **Normal KYC Flow (Success Path)**

1. **KYC Flow Initiated**
    
    → *Trigger:* Internal system calls HyperVerge
    
    → **CRM Event:** `KYC Verification Started`
    
2. **OTP Triggered & Verified**
    
    → **CRM Event (if needed):** `OTP Triggered`
    
3. **CKYC Search & Download Successful**
    
    → **CRM Event:** `CKYC Search Success`
    
4. **CKYC Validation Passed**
    
    → **CRM Event:** `CKYC Validation Success`
    
5. **Selfie Capture + Liveness Check Passed**
    
    → **CRM Event:** `Photo Captured` + `Liveness Check Passed`
    
6. **Photo Match Threshold Passed**
    
    → **CRM Event:** `Photo Match Success`
    
7. **KYC Completed Successfully**
    
    → **CRM Event:** `KYC_VERIFICATION_COMPLETE_STEP`
    

## **Fallback Flow (On Any Failure in Normal Path)**

1. **Failure in Any Step (HyperVerge/OTP/CKYC/Photo/Liveness)**
    
    → **CRM Event:** `Step 9 Triggered` with failure reason
    
2. **Digilocker Fallback Flow Initiated**
    
    → **CRM Event:** `Digilocker Initiated`
    
3. **Digilocker-Based CKYC Search & Download**
    
    → **CRM Event:** `CKYC Completed via Fallback`
    
4. **Validation & Photo Steps (If Required Again)**
    
    → Repeat similar events as in the normal flow for selfie/liveness checks, if applicable.
    
5. **KYC Completion (Success/Failure)**
    
    → **CRM Event:**
    
    • If success: `KYC_VERIFICATION_COMPLETE_STEP`
    
    • If fail: `Step 9 Reroute Failure` with reason
    

---

# **Design**

[Design requirements](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/Design%20requirements%201bbe8d3af13a80b398a8e83218d98506.md)

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

- Selfie mandatory flow (outdated)
    
    LSPs will have the following options: 
    
    1. **Flow #1 :** LSP calls the `KYC Init` API *without* providing additional fields (e.g., name, DOB).
        1. LSP will have to send mobile number of the customer along with oppId. 
            
            <aside>
            💡
            
            We will not validate the phone number with the phone number used for creating opportunity. This phone number should be the one linked to CKYC records of  customer.
            
            </aside>
            
        2. DSP responds with a *unique KYC link* that the LSP can present to the user (e.g., via SMS/Email/app).
        3. This link will have UI for NSDL PAN verification, Selfie capture + Liveliness, CKYC (search, download and validation), Digilocker and deviation handling as well. 
    2. **Flow #2 :**LSP calls the `KYC Init` API and provides name and DOB in addition to mobile number and oppId
        1. DSP will perform NSDL PAN verification with the provided data.
        2. If the PAN validation is successful, DSP responds with a unique KYC link. PAN verification UI will be skipped in this case, other steps in KYC will be shown to the user.
        3. If the PAN validation API fails, KYC fails for the customer. 
    3. **Flow #3 :**LSP calls the `KYC Init` API and provides name, DOB, mobile number, and photo of the customer
        1. This will be an API based flow, LSPs have freedom to build their own UI. This will be the route that most Tier 1 LSPs will take. 
        2. LSPs will have to pass a CKYC download consent log with timestamp.
        3. LSPs will have to call another API which provides DSP with the OTP that customer inputs on their UI. This API will also handle the resend OTP flow. 
        4. There will be a “liveliness check done” flag, which if passed `TRUE` will skip liveliness check on DSP side. 
            1. LSPs will have to send Liveliness check log including timestamp, vendor and liveliness score
        5. DSP will perform: NSDL PAN verification → Liveliness check (if flag not passed) → CKYC search and download init → Take CKYC OTP through LSPs → CKYC download → CKYC validation. If CKYC flow fails, DSP will share CKYC failure status along with details necessary for LSPs to invoke Digio digilocker SDK along with a link to complete Digilocker journey.

CERSAI pricing: 

| **Parameter** | **Charge per record (Rs.)** |
| --- | --- |
| First time download of KYC record | 2.25 |
| Subsequent download of KYC record by the same reporting entity | 1.00 |

| **Parameter** | **Incentive per record* (Rs.)** |
| --- | --- |
| Creation of a new KYC record | 0.50 |
| Update of KYC record | 0.25 |
- The charge is exclusive of any applicable relevant tax

[User_Manual_CKYC1.pdf](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/User_Manual_CKYC1.pdf)

Document to document code mapping in CKYC: [https://docs.google.com/spreadsheets/d/1bXLxD6Si3J0PAiXUqJ7lfTjdTLzMg8mWcTyxCIek5Tg/edit?usp=sharing](https://docs.google.com/spreadsheets/d/1bXLxD6Si3J0PAiXUqJ7lfTjdTLzMg8mWcTyxCIek5Tg/edit?usp=sharing)

## Archive

- KYC flow
    
    Flow description: 
    
    1. Customer fetches mutual funds on LSP. [Customer would enter PAN and mobile number]
    2. Customer would select limit that they require
    3. Customer would land and click CTA on the loan offer page
    4. LSP would hit KYC init API. In response LSP will receive a link from DSP. This link will orchestrate the KYC steps: NSDL PAN verification, Selfie (Liveliness and Match), CKYC, and Digilocker. 
        1. LSP would have to specify if they want to trigger CKYC + DL flow for customers.
    5. NSDL PAN verification: DSP would accept customer’s full name and DOB in the KYC init API
        1. If LSP sends Full name and DOB, DSP will initiate NSDL PAN verification in the BE.
            1. If Full name or DOB match fails in NSDL PAN verification, customer will be asked to enter the Full name and DOB as per PAN document. 
            2. In case Aadhaar PAN seeding status is not positive, customer will be shown an error that your PAN is not linked with Aadhaar and we can not do KYC for the customer. 
        2. If LSP does not send Full name and DOB, DSP will show UI where customer will be asked to enter the Full name and DOB as per PAN document. 
            1. Error will be shown in case NSDL returns that that PAN is not verified
            2. Error will be shown  in case NSDL returns customer name or DOB is not matching
        3. Name and DOB in the application will be as per verified from NSDL. 
    6. Selfie liveliness check: Customer clicks selfie, which is checked for liveliness. 
    7. Customer gives consent to fetch CKYC data
    8. CKYC search. Only PAN is required for CKYC search. 
        1. In case CKYC search is unsuccessful, digilocker flow will be triggered for the customer
    9. CKYC download. PAN and DOB is required for CKYC download. 
        1. In case CKYC download is unsuccessful, digilocker flow will be triggered for the customer
    10. Hyperverge’s CKYC validation API is called. The API verifies the user's PII stored in an XML file in the central KYC registry against their officially valid documents (OVDs) downloaded from the same record. It also verifies if the selfie from the record matches the images present in each OVD file.
        1. In case we decide that customer’s CKYC data is not usable for KYC basis response from CKYC validation API, Digilocker flow will be triggered for the customer
    11. Selfie of the customer clicked in step 6 will be matched with CKYC photo of the customer.
        1. If the selfie match is below x%, Digilocker flow will be triggered for the customer 
    12. CKYC is successful for the customer.
    13. Digilocker flow: This will be triggered only in cases CKYC fails
        1. Both Aadhaar and PAN will be pulled from Digilocker
            1. PAN fetched from Digilocker should be matched with NSDL PAN, in case there is a mismatch. Customer will be shown an error that Digilocker PAN doesn’t match the 
            2. In case we are not able fetch PAN from the digilocker, Aadhaar name and DOB will be matched with PAN (from NSDL) name and DOB. 
                1. In case DOB doesn’t match. Customer will be shown an error that KYC can not be completed. 
                2. In case Name doesn’t give a match percentage of X%. Customer will be shown an error that KYC can not be completed. 
        2. Customer’s selfie from step 6 will be matched with Aadhaar photo in Digilocker response.
            1. If the photo match percentage is below x%, customer will be given an error message that the photo is not matching. Customer will be asked to click another picture and and the new photo will be matched with Digilocker photo again. 
    14. Additional details page: Prefill in cases we get Father’s name from digilocker
    15. Verify KYC details page
- Search and download (Decentro)
    
    ### CKYC search
    
    This API searches the CERSAI DB for customer’s records. For searching, we will have to pass one of the following document numbers. 
    
    - **Pan (We will be using PAN for search)**
    - Aadhaar
    - Passport
    - Voter ID
    - Driving License
    - CKYC Number
    
    CKYC search response.  https://jsongrid.com/?data=4dbc3931-7074-4e35-9ce1-9698f74e8dbf
    
    ### CKYC download
    
    If CKYC search is a success, complete CKYC data for the customer is downloaded. To download CKYC data, CKYC number / CKYC reference id along with one of the following as auth factor would be required.
    
    - DOB (We will be using DOB for download)
    - 10-digit Aadhaar linked mobile number of the customer
    - Combination of the 6-digit pin code and the year of birth
    
    CKYC download response.  https://jsongrid.com/?data=27d67894-a727-4d34-8e5a-77846ff58a3e
    
- Old approach
    - Approach 1
        
        Option 1: Complete journey on us. If they pass mode of KYC as 1(for example), we will send a link which will do complete KYC steps for the customer: Following would be the high level flow: 
        
        1. UI for customer to enter Full Name and DOB. This will have the CKYC consent callout as well. 
        2. CKYC search + download + validation will be triggered as soon as NSDL PAN verification is successful in the backend. 
        3. In the FE customer will see a UI to click selfie. Photo liveliness will be checked in the session. 
        4. Customer will then be shown a loading screen, if the CKYC search + download + validation is still in progress. 
        5. Customer will be shown Digilocker flow in case customer’s CKYC download/validation fails. 
        6. Photo match will be done in the BE with CKYC or Digilocker photo. 
        
        Option 2: 
        
        1. CKYC standalone API: This API can be called seperately by the LSP
            1. Input: 
                1. Opportunity ID
                2. DOB
                3. Phone number (optional)
            2. Output: 
                1. CKYC data validated: Yes/No
                2. CKYC ref ID (DSP internal), only in case of success. 
        2. KYC init API
            1. Input: 
                1. 
        
        ### 1. Customer Initiation
        
        - **Mutual Funds Fetch on LSP:**
            - Customer enters **PAN** and **mobile number**.
        - **Loan Limit Selection:**
            - Customer selects the desired loan limit.
        - **CTA Action:**
            - Customer clicks the call-to-action (CTA) on the loan offer page.
        
        ### 2. KYC Initialization
        
        - **KYC Init API Call:**
            - LSP calls the KYC init API.
            - **Response:**
                - LSP receives a link from DSP which orchestrates the following KYC steps:
                    - NSDL PAN Verification
                    - Selfie (for liveliness and matching)
                    - CKYC (search, download, validation)
                    - Digilocker (fallback)
        - **Configuration Flag:**
            - LSP must indicate if the CKYC + Digilocker flow should be triggered for the customer.
        
        ### 3. NSDL PAN Verification
        
        - **Data Submission Options:**
            - **Option 1:** LSP sends Full Name and DOB along with PAN.
                - **Backend Verification:**
                    - DSP uses these details to perform NSDL PAN verification.
                    - **On Mismatch:**
                        - If the Full Name or DOB doesn’t match the PAN record, the customer is prompted to re-enter the details exactly as per the PAN document.
                    - **Aadhaar PAN Seeding:**
                        - If Aadhaar is not linked with PAN, an error is shown: *“Your PAN is not linked with Aadhaar and we cannot do KYC.”*
            - **Option 2:** LSP does not send Full Name and DOB.
                - **UI Prompt:**
                    - DSP shows a UI for the customer to enter the Full Name and DOB.
                    - **Error Handling:**
                        - Errors are shown if NSDL returns an unverified PAN or if the entered details do not match the PAN record.
        - **Outcome:**
            - The verified Name and DOB from NSDL are stored for the application.
        
        ### 4. Selfie Liveliness Check
        
        - **Selfie Capture:**
            - The customer clicks to take a selfie.
        - **Liveliness Verification:**
            - The selfie is checked for liveliness.
        
        ### 5. CKYC Process
        
        - **Consent:**
            - The customer gives consent to fetch CKYC data.
        - **CKYC Search:**
            - **Requirement:** Only PAN is needed.
            - **Failure:**
                - If unsuccessful, the flow moves to the **Digilocker fallback**.
        - **CKYC Download:**
            - **Requirement:** PAN and DOB.
            - **Failure:**
                - If unsuccessful, Download is unsuccessful with DOB then retry download with mobile number.
                - If unsuccessful, the flow moves to the **Digilocker fallback**.
        - **CKYC Validation:**
            - **Hyperverge API:**
                - Validates customer PII from the CKYC XML record against Official Valid Documents (OVDs).
            - **Failure:**
                - If CKYC data is deemed unusable, trigger the **Digilocker flow**.
        - **Selfie Matching:**
            - The selfie taken earlier is matched with the CKYC photo.
            - **Threshold Check:**
                - If the match is below a defined percentage (x%), the flow falls back to **Digilocker**.
        - **Success:**
            - If all CKYC steps are successful, proceed with KYC as successful.
        
        ### 6. Digilocker Fallback Flow (Triggered When CKYC Fails)
        
        - **Data Retrieval:**
            - **Fetch:** Both Aadhaar and PAN are pulled from Digilocker.
            - **PAN Matching:**
                - The PAN from Digilocker must match the NSDL PAN.
                - **Mismatch:**
                    - An error is shown: *“Digilocker PAN doesn’t match.”*
            - **Alternate Check (if PAN not fetched):**
                - Compare Aadhaar name and DOB with NSDL PAN name and DOB.
                - **Mismatch:**
                    - If DOB does not match or if the name match is below the required percentage, display an error: *“KYC cannot be completed.”*
        - **Selfie Matching:**
            - The customer’s selfie is matched against the Aadhaar photo from Digilocker.
            - **Threshold Check:**
                - If the match percentage is below x%, an error is shown, prompting the customer to retake the selfie.
        - **Success:**
            - Upon a successful match, the Digilocker KYC is considered successful.
        
        ### 7. Subsequent Steps
        
        - **Additional Details Page:**
            - Pre-fill information (e.g., Father’s name if available from Digilocker).
        - **KYC Details Verification Page:**
            - Final review and verification of the KYC details before proceeding further.
            - Consents from customer: Customer is an Indian resident, and Customer’s current address and
                
                ![mermaid-diagram-2025-02-13-154156.svg](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/mermaid-diagram-2025-02-13-154156.svg)
                
- Upload/download benchmarking
    
    ### CKYC search/download and upload options alignment
    
    | Search | Upload | Pros | Cons |
    | --- | --- | --- | --- |
    | HYpverUpload - HV (API based) |  | - Single vendor for all CKYC utilities
    - Can setup workflows  | - Dev effort in modifying integration |
    | Search and Download - HV (Self hosted solution)
    Upload - Decentro (Self hosted solution) |  |  | - One time setup fee for Decentro will be
    - Dev effort in modifying Decentro integration |
- Old requirements
    1. KYC flow starts: 
        1. LSPs will call the KYC flow 2.0 APIs with customer name, DOB, and mobile number along with oppId.
    2. NSDL PAN verification: 
        1. DSP will use customer name, DOB, and PAN (PAN will be taken from the PAN used for opp creation) to verify PAN from NSDL.
        2. API documentation :
        3. NSDL PAN verification will be considered successful only when ALL of the below conditions are satisfied: 
            1. panStatus: “EXISTING AND VALID”
            2. name: "MATCHING"
            3. dateOfBirth: "MATCHING"
            4. aadhaarSeedingStatus: "Y"
            
            In all other cases, PAN verification would be considered failed. DSP will share the corresponding error message with LSP. 
            
            [NSDL error messaging](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/NSDL%20error%20messaging%201f1e8d3af13a8055821fe32411fbc417.md)
            
        4. Sample success response: 
            
            ```jsx
            {
              "status": "success",
              "statusCode": 200,
              "metaData": {
                "requestId": "<Request_Identifier>"
              },
              "result": {
                "pan": "<User's_PAN_Identifier>",
                "panStatus": "EXISTING AND VALID",
                "name": "MATCHING",
                "dateOfBirth": "MATCHING",
                "aadhaarSeedingStatus": "Y"
              }
            }
            ```
            
        5. Name and DOB should be stored against the oppId. 
        6. PAN verification log should be created and stored. The format of the log should be. 
            1. PAN verification status: Existing and valid
            2. PAN verification source: NSDL
            3. PAN verification timestamp: <timestamp of verification>
        7. If this NSDL PAN verification fails, it will be considered as customer KYC failure. 
    3. CKYC search and download OTP trigger
        1. Trigger the CKYC seach and download init API with the necessary required inputs. 
        2. Sample request: 
            
            ```jsx
            {
               "idNo": <pan>, // Enter user's PAN here 
               "idType": "C", // C corresponds to idType PAN. This can be made constant
               "dob": "dd-mm-yyyy", // Enter user's DOB here
               "mobileNo": "1234567678" // Enter user's mobile number here   
            }
            ```
            
        3. Sample response (success):
            
            ```jsx
            {
            "status": "success",
              "statusCode": "200",
              "result": "OTP has been sent to the registered mobile number <mobileNo
            >"
            }
            ```
            
        4. Error handling
            
            [CKYC S&D error handling](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/CKYC%20S&D%20error%20handling%201f2e8d3af13a806387d5e8f15a7cf5ef.md)
            
        5. If user encounters a CKYC terminal status(defined in the error documentation), user will be moved to Digilocker flow. 
    4. CKYC download OTP verify
        1. This API will be used to verify the OTP entered by the customer and download CKYC data. 
        2. Sample request: 
            
            ```jsx
            {
               "otp": <otp number collected from end user>,
               "mobileNo" : <10-digit mobile no sent in the first request>        
            }
            ```
            
        3. Sample response: 
            
            ```jsx
            {
                "status": "success",
                "statusCode": "200",
                "result": {
                    "constituitonType": "Individual",
                    "accountType": "normal",
                    "ckycNo": "",
                    "preFix": "Ms",
                    "firstName": "",
                    "middleName": "",
                    "lastName": "",
                    "fullName": "",
                    "fatherOrSpouse": "father",
                    "fatherPrefix": "",
                    "fatherFname": "",
                    "fatherMname": "",
                    "fatherLname": "",
                    "fatherFullName": "",
                    "motherPrefix": "Mrs",
                    "motherFname": "",
                    "motherMname": "",
                    "motherLname": "",
                    "motherFullName": "",
                    "gender": "F",
                    "dob": "",
                    "age": "",
                    "address1": "",
                    "address2": "",
                    "address3": "",
                    "city": "Kamrup",
                    "district": "",
                    "state": "AS",
                    "country": "IN",
                    "pincode": "",
                    "permAndCorresAddSame": "Y",
                    "corresAddress1": "",
                    "corresAddress2": "",
                    "corresAddress3": "",
                    "corresCity": "",
                    "corresDist": "",
                    "corresState": "AS",
                    "corresCountry": "IN",
                    "corresPin": "",
                    "resiStdCode": "91",
                    "resiTelNo": "",
                    "mobileCode": "91",
                    "mobileNumber": "",
                    "email": "",
                    "decDate": "18122021",
                    "decPlace": "Bengaluru",
                    "kycDate": "********",
                    "updatedDate": "",
                    "idList": "",
                    "DocSub": "04",
                    "kycName": "********",
                    "kycDesignation": "********",
                    "kycBranch": "********",
                    "kycEmpCode": "********",
                    "numIdentity": "1",
                    "numRelated": "0",
                    "numImages": "4",
                    "aadhaar": "",
                    "pan": "",
                    "voterId": "",
                    "passport": "",
                    "drivingLicense": "",
                    "nregaJobCard": "",
                    "nationalPopulationReg": "",
                    "imageDetails": [
                        {
                            "code": "04",
                            "type": "pdf",
                            "imageUrl": "Image_URL"
                        },
                        {
                            "code": "02",
                            "type": "jpg",
                            "imageUrl": "Image_URL"
                        },
                        {
                            "code": "03",
                            "type": "jpg",
                            "imageUrl": "Image_URL"
                        },
                        {
                            "code": "09",
                            "type": "jpg",
                            "imageUrl": "Image_URL"
                        }
                    ]
                }
            }
            ```
            
        4. In case customer wants to resend the OTP. 
        5. Documents are present in the imageDetails object within the verify OTP success response. Documents have codes basis the document type. Mapping of document type and code is [here](https://docs.google.com/spreadsheets/d/1bXLxD6Si3J0PAiXUqJ7lfTjdTLzMg8mWcTyxCIek5Tg/edit?usp=sharing). Need a check that will ensure if CKYC data has necessary ID documents or not. In phase 1, we will consider only “Proof of possession of Aadhaar” (code:04) as a valid ID document. In future, we may consider other documents as valid ID documents. That change should only be a configuration change. 
            
            [CKYC OTP verify error cases](%5BDSP%5D%20KYC%20v2%20(including%20CKYC)/CKYC%20OTP%20verify%20error%20cases%201f2e8d3af13a80adba07caf2cbf6dc7f.md)
            
    5. Trigger Hyperverge CKYC validation API
        1. CKYC validation API 
    6. Liveliness check + selfie capture: 
        1. LSPs will call the selfie capture API, they will send opptunity ID along with captured image of the customer in base64 format. 
        2. DSP will perform liveliness check on the photo sent by LSP, and corresponsing error codes/messages will be share with the LSP. 
        3. In case liveliness check is passed, selfie of the image will be stored for further validation. 
        
        <aside>
        💡
        
        - Current photo validation API runs after the KYC documents download. For CKYC flow, this will be run before KYC documents download.
        - Current photo validation API matches the photo with Aadhaar image. For CKYC flow, this validation will be done later in the flow.
        </aside>
        
    7. KYC flow start: 
        1. LSPs will call the KYC flow 2.0 APIs with customer name, DOB, and mobile number along with opportunityID. 
        
        <aside>
        💡
        
        </aside>
        
    
    ### Option 1 Flow
    
    1. **KYC Init (Minimal Data)**
        - LSP calls the `KYC Init` API *without* providing additional fields (e.g., name, DOB).
        - DSP responds with a *unique KYC link* that the LSP can present to the user (e.g., via SMS/Email/app).
    2. **User Clicks Link & Completes KYC**
        1. Customer is guided (in DSP’s hosted flow) to performs the following:
            - **NSDL PAN verification** (user enters Name and DOB).
            - **Selfie capture** (Liveliness will be checked in-sync, this selfie will be matched with CKYC data later)
            - **CKYC S&D** (use PAN+DOB as the primary authentication factor. PAN+Mobile number will be used as backup authentication flow in case S&D API fails with PAN+DOB).
            - **CKYC Validation** (we will run the data that we got in CKYC S&D through HV validation API). Following are the cases of validation.
            - **Digilocker** (in cases where customer can not be taken through the CKYC journey)
            - **KYC Deviation handling** (for Digilocker fallback, if the customer face is below match threshold or when PAN could not be retrieved and matched with Aadhaar with absolute certainty [This still needs to be aligned] )
    3. **Validations**
        1. In NSDL PAN verification, if either Name or DOB is not matched. Customer should be shown inline error in UI on which parameter is not matching. Both should match before moving the user ahead. 
        2. Selfie capture, when customer submits that captured selfie. We will run the same through Digio liveliness API, in case validation fails. Customer will be shown the error upfront. Only a liveliness verified selfie should be allowed to proceed. 
        3. If CKYC S&D fails via PAN+DOB and PAN+Mobile combination both, customer should be moved to the Digilocker flow.
        4. In CKYC S&D, currently it is mandatory for the customer to have proof of possession of Aadhaar document (document code: 4). If the customer doesn’t have this document the customer should be moved to the Digilocker flow. NOTE: Keep this handling very modular in code, in future we would want to add other acceptable document codes here. 
        5. In CKYC Validation, we will run the HV validation API with the image, Proof of possession of Aadhaar document and permanent address fetched from CKYC data. 
            1. In case we receive address related errors: []
    4. **Results**
        - On success, the DSP returns *KYC Success* to the LSP.
        - If the user’s details fail checks, the DSP returns a *KYC Failure*
    
    ### Option 2 Flow
    
    1. **KYC Init (Name & DOB Provided)**
        - LSP calls the `KYC Init` API and provides the customer’s *full name* and *DOB*.
        - DSP triggers *NSDL PAN verification* in its backend using the input data.
    2. **PAN Verification**
        - If *NSDL verification succeeds*, DSP returns a *selfie link* (and possibly next steps to the LSP).
        - If verification *fails*, an *error* is thrown (“PAN validation failed”).
    3. **Selfie Capture & Document Upload**
        1. User is prompted to take a selfie and upload identity/address proofs.
        2. DSP backend checks:
            - **CKYC search** with the *PAN/DOB* combination.
            - **OCR & Face Match** with the submitted documents vs. selfie.
            - **Name & DOB** consistency.
            - **Address Validation** if relevant.
            - **Deviation Handling** if partial mismatch.
    4. **Results**
        - Success → *KYC Success* returned to LSP.
        - Failure → *KYC Failure* or further *manual review* steps if needed.
    
    ### Option 3 Flow
    
    1. **KYC Init (Name, DOB, Photo, CKYC Consent)**
        - LSP calls `KYC Init` API with:
            - Customer’s full name, DOB
            - A photo (captured by LSP)
            - A flag indicating *CKYC consent*
    2. **DSP Backend Checks**
        1. **NSDL PAN Verification** (based on name/DOB or provided PAN).
        2. **Liveliness Check** on the submitted photo.
        - If either fails, return an *error* to LSP (KYC can’t proceed).
    3. **CKYC Process (If All Above Passes)**
        - DSP automatically attempts CKYC (search & fetch).
        - If CKYC data is present and valid → *KYC Success* is returned to the LSP.
        - If CKYC fails or is not available:
            - **Digilocker Link** is provided to the LSP.
            - The user pulls Aadhaar or other identity documents via Digilocker.
    4. **Digilocker Photo Match**
        - DSP compares the photo from LSP input (Step 1) with the *Digilocker photo*.
        - If they match: *KYC Success.*
        - If they don’t match or there is any other mismatch above thresholds → *KYC Failure* or *Manual Review.*
    
    Following will be the high level flow. 
    
    NSDL PAN verification:
    
    1. Integrate with the Hyperverge NSDL PAN verification API to do PAN verification of the customer. 
    2. If LSPs don’t share the re
- Data validation benchmarking
    
    ### CKYC Data validation
    
    - Research
        
        There are following ways to validate CKYC data - 
        
        1. Using Hyperverge CKYC data validation API: This validates quality of the CKYC data. 
            1. Pros
                1. No need to build the CKYC validation logic on our side
                2. Incorporates multiple cross checks of the data and OVD OCR as well
            2. Cons
                1. Rule of validation can NOT be changed, it gives a final Approve, Review and Reject rating. 
        2. Matching data points in house: Here we will match the data that we get from NSDL PAN verification and CKYC to validate quality of CKYC data
            1. Name - Use a name matching algorithm and finalise a threshold for match success. Check hyperverge for Name match algorithms. 
            2. DOB - Exact match
            3. PAN - Exact match
        
        <aside>
        💡
        
        - Cred uses the Hyperverge API to validate CKYC data.
        - Navi uses the second approach. It uses Levenshtein method at 40% for name match.
        </aside>
        
    
    We would be using Hyperverge’s CKYC validation API