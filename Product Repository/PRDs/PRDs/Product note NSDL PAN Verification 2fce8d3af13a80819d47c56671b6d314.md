# Product note: NSDL PAN Verification

: Devansh Kar
Created time: February 4, 2026 3:50 AM
Status: In progress
Last edited: April 7, 2026 3:21 PM

## **Background and Context**

- 
    - Who is facing the problem (users, internal teams, partners)
    - What is the challenge that they are facing? What is broken today?
    - Why is it important? or What is getting impacted?

As per RBI’s KYC guidelines, if as an RE we are obtaining PAN of the customer the same should be verified from the issuing authority (as per point 10(j) of Chapter III in the RBI KYC [Masterdirections](https://www.rbi.org.in/Scripts/BS_ViewMasDirections.aspx?id=11566)). This means that PAN should be verified via the NSDL PAN verification API. 

![image.png](%5BDSP%5D%20NSDL%20PAN%20Verification%20alignment/image.png)

With the current sources for obtaining PAN that we use in the KYC journey

1. Digilocker PAN
2. If Digilocker PAN is not fetched, we use Signzy enrichment API for verification

Currently we are not integrated with the NSDL PAN verification API for verifying PAN details, which makes us non-compliant. Also, even in cases where we are able to receive PAN document from Digilocker that also needs to be verified from NSDL which is the verification facility of the issuing authority as users can also directly update/ renew PAN with ITDB and records might not be synced with Digio. The interval/ frequency when digilocker updates the new PAN when a user renews it is also uncertain.

---

## **1. Problem scope**

### In scope

- 
    - What specific problems are we solving?
    - Who are we solving it for? Consider both primary and secondary users
- Ensuring all the various sources [Digilocker, LSP, CKYC, etc.] through which DSP is obtaining the PAN related details (PAN number, PAN Name, and PAN DoB) must be verified via NSDL as a part of compliance and KYC.
- Verification with Primary source for KYC being Digilocker.
- Fallback for Consuming Name from Decentro PAN API for Volt flows in order to use it for NSDL PAN Verification in the fallback flows (Volt)
- ~~Downstream changes in th e agreement name and DoB.~~

### Out of scope

- 
    - Call out on items out of scope
    - Rationale for exclusion
- 

---

## **2. Success Criteria**

- 
    
    Top 2-3 **clear outcomes that we are looking to achieve**.
    
    - Key success metrics (Conversion rate / Error rate / TAT)
    - Define post launch good state (Expected behaviour / uptime / SR)
    - Guardrail metrics (Metrics that should not degrade)
- 100% compliance in terms of verifying Proof of identity in KYC
- **≥98%** NSDL PAN verification success based on input parameters passed in the backend
- ≤2% of users who goes through manual input/ Non-STP flow

---

## **3. Solution Scope**

### Solution overview

- 
    
    Explain in 2-3 lines the overview of the solution
    
    - Explain overview of the solution with key product and system changes
    - Explain the rationale on scoping/phasing of the solution
    - Call out scope that has been scoped out and explain the rationale

**Overview of the Solution (Key Product & System Changes)**

- Provide method to LSPs to complete KYC of customers in DSP UI. The complete KYC including  documents pull + NSDL PAN verification +~~selfie match~~ will be orchestrated in DSP UI reducing effort required from LSPs to integrate KYC. This will include Digilocker as method of document download.
- ~~Provide APIs to LSPs to complete *KYC for customers (*NSDL PAN verification + documents pull + selfie match*)*. This will give LSPs the flexibility to build their own UI and experience for completing KYC for customers.~~
- Ensure *regulatory compliance* and with similar *success rates* as now by making the KYC journey simpler and clearer for end users.
- Option for LSP to pass the relevant PAN details in case PAN record is not available in the primary KYC method (Digilocker).
- Fallback UI screen for accepting inputs from user with relevant details for PAN verification
- Non-STP flow for verifying PAN through NSDL PAN verification API before disbursal, in case PAN Verification API faces downtime in the primary flow.
- Handling the verified KYC details used in the DSP agreement.

---

## **4.  High level s***ystem, user or process flow*

**STP flow:**

**LSP flow:**

1. At the KYC step, LSP shall call the KYC init API of DSP. While calling the KYC Init API, the LSP needs to pass the PAN name of the user that it has captured, in the request body of DSP KYC init API. In response of which DSP will generate a unique KYC link for the particular user to complete the KYC journey.
2. LSPs shall be encouraged to primarily pass the name parameter for a seamless KYC journey as well as NSDL PAN Verification but it won’t be a mandatory parameter.
3. The unique KYC link triggered by DSP, that LSP will present to the user for completing KYC shall contain the following steps:
    1. Digilocker KYC
    2. NSDL PAN Verification (Backend API call + fallback to manual user inputs in case of non-matching conditions for necessary fields like PAN number and PAN name)
4. **Step 1: Digilocker step:** After Digilocker step is completed there are 2 scenarios:
    1. PAN document and PAN details are available from Digilocker [Details available: **PAN Number**, **PAN Name**, **PAN DoB**] + Aadhaar document and details [Details available: Aadhaar Name, Aadhaar DoB, Aadhaar Address]
    2. PAN document and PAN details are **NOT** available from Digilocker. Only Aadhaar document and details are available. [Details available: Aadhaar Name, **Aadhaar DoB**, Aadhaar Address]
5. **Step 2: NSDL PAN verification**
    1. After the Digilocker step is completed, NSDL API shall be called in the backend during the DSP KYC journey. The following details need to be passed in the Input request for NSDL PAN Verification in the Backend:
        1. PAN Number
        2. Name
        3. DoB
    
    In [**Step 1](Product%20note%20NSDL%20PAN%20Verification%202fce8d3af13a80819d47c56671b6d314.md),** if: 
    
    1. PAN details are available from Digilocker, then all the details of PAN from Digilocker (PAN number, PAN name, PAN DoB) will be passed in the NSDL API input request for verification.
    2. PAN details are not available from Digilocker, then the PAN details: 
        1. **PAN No**. (Captured by DSP at the time of opportunity creation from LSP)
        2. **PAN** **Name** (Captured by DSP at the time of KYC Init from LSP)
        3. **Aadhaar DoB** fetched from Digilocker
        
        shall be passed in the NSDL API input request for verification.
        
    3. In cases where, the LSPs does not consume/ pass any detail (example: PAN Name in this case), and also the PAN name is not available from Digilocker, a UI screen shall be shown to the user to manually enter the “Name as per PAN” which shall be passed as input in the NSDL PAN Verification API.
    
    b. **Success conditions for PAN verification** - Conditions mentioned below should be satisfied for PAN verification to be successful. If PAN verification is successful, LSP will be sent PAN verification successful webhook. 
    
    1. panStatus: “E” (Existing and Valid)
    2. name: "Y" (Matching)
    3. dateOfBirth: "Y”/ “N” (Non-Matching condition doesn’t reject the verification)
    4. aadhaarSeedingStatus: "Y"/ “R”/ “NA” (Y: Operative, R: Inoperative, NA: Non-individual PAN)
    5. The KYC process going through STP flow (No downtime flow) will be marked as “success” on successful PAN verification via NSDL.
    
    c. **Handling failures:** 
    
    1. If any of the mentioned parameters  that needs a mandatory matching (PAN number, PAN name) received in response from NSDL PAN API response has a “No” match then:
    
    **Step 1 i): On passing PAN details available from Digilocker**
    
    1. If initially the PAN details are passed from Digilocker as input and we get non-matching response (PAN ≠ “E”, AND/ OR Name: “N”), then automatically, a “failure” response will be received by LSPs from DSP at NSDL Step.
    2. Exact failure responses are:
        1. PAN ≠ “E” → “PAN entered is not a valid PAN” And/Or
        2. Name = “N” → Name as per PAN is not valid
        3. PAN ≠ “E” and Name = “N” → PAN number and PAN name entered are not valid
    3. On receiving the “failure” response, DSP will again attempt by passing the PAN details (PAN number, PAN name) received by it from LSP in the NSDL PAN verification API. If NSDL still returns non-matching response for any of the above mentioned parameters, then UI shall be shown in the DSP journey asking for inputs from the user. [PAN: Fixed field, Name as per PAN]. Aadhaar DoB from Digilocker shall be passed to the NSDL API from backend.
    
    **Step 1 ii): When PAN details are not available from Digilocker, and LSP passes PAN details of the user for NSDL input.**
    
    1. Similar to the action mentioned above, on passing the PAN details from LSP, if we receive non-matching response for any of the mentioned parameters, UI shall be shown in the DSP journey asking for inputs from the user. [PAN: Fixed field, Name as per PAN]. Aadhaar DoB from Digilocker shall be passed to the NSDL API from backend.
    2. Customers can trigger PAN verification thrice via user input method. After 7 tries in 20 mins. “Maximum attempts reached for PAN verification” error will be shown to the customer in UI and given as a webhook to LSP as well. The number of retries and the cooldown time should be in a config that can be changed later. The LSP shall block the workflow at this step, and the user needs to redo the entire KYC again as a fresh application with new utility_reference_id.
    3. PAN number should be in the format  **XXXPX1234X.** 4th letter of the PAN should be “P” to indicate that the PAN belongs to an individual. If this requirement is not matched return error `“PAN in opportunity does not belong to an individual”` to LSPs in a webhook.  PAN verification API should not be triggered in this case. This error will result in KYC failure. 
    
    **Step 1 iii)** Possibility that LSP does not consume any detail (PAN, PAN Name, PAN DoB)
    
    1. If LSP does not capture/ verify the relevant PAN details on their end (PAN name), and we don’t have PAN record available from Digilocker, then directly UI should be shown to the user asking for relevant inputs. [PAN: Fixed field, Name as per PAN, DoB as per PAN]
    
    **Global condition** for successful KYC verification completion: Both verifier should be digilocker/ Hyperverge/ any other method used later on for KYC and primary_pan_verifier needs to be **Protean**.
    

**Volt flow:**

1. At the KYC step, Volt shall call the KYC init API of DSP. While calling the KYC Init API, Volt needs to pass the PAN name of the user that it has captured via Decentro API, in the request body of DSP KYC init API. In response of which DSP will generate a unique KYC link for the particular user to complete the KYC journey.
2. The unique KYC link triggered by DSP, that Volt will present to the user for completing KYC shall contain the following steps:
    1. Digilocker KYC
    2. NSDL PAN Verification (Backend API call + fallback to manual user inputs in case of non-matching conditions for necessary fields like PAN number and PAN name)
3. **Step 1: Digilocker step:** After Digilocker step is completed there are 2 scenarios:
    1. PAN document and PAN details are available from Digilocker [Details available: **PAN Number**, **PAN Name**, **PAN DoB**] + Aadhaar document and details [Details available: Aadhaar Name, Aadhaar DoB, Aadhaar Address]
    2. PAN document and PAN details are **NOT** available from Digilocker. Only Aadhaar document and details are available. [Details available: Aadhaar Name, **Aadhaar DoB**, Aadhaar Address]
4. **Step 2: NSDL PAN verification**
    1. After the Digilocker step is completed, NSDL API shall be called in the backend during the DSP KYC journey. The following details need to be passed in the Input request for NSDL PAN Verification in the Backend:
        1. PAN Number
        2. Name as per PAN
        3. DoB
    
    In [**Step 1](Product%20note%20NSDL%20PAN%20Verification%202fce8d3af13a80819d47c56671b6d314.md),** if: 
    
    1. PAN details are available from Digilocker, then all the details of PAN from Digilocker (PAN number, PAN name, PAN DoB) will be passed in the NSDL API input request for verification.
    2. PAN details are not available from Digilocker, then the PAN details: 
        1. **PAN No**. (Captured by DSP at the time of opportunity creation from Volt)
        2. **PAN** **Name** (Captured by DSP at the time of KYC Init from Volt)
        3. **Aadhaar DoB** fetched from Digilocker
        
        shall be passed in the NSDL API input request for verification.
        
    3. In cases where, the LSPs does not consume/ pass any detail (example: PAN Name in this case), and also the PAN name is not available from Digilocker, a UI screen shall be shown to the user to manually enter the “Name as per PAN” which shall be passed as input in the NSDL PAN Verification API.
    
    b. **Success conditions for PAN verification** - Conditions mentioned below should be satisfied for PAN verification to be successful. If PAN verification is successful, LSP will be sent PAN verification successful webhook. 
    
    1. panStatus: “E” (Existing and Valid)
    2. name: "Y" (Matching)
    3. dateOfBirth: "Y”/ “N” (Non-Matching condition doesn’t reject the verification)
    4. aadhaarSeedingStatus: "Y"/ “R”/ “NA” (Y: Operative, R: Inoperative, NA: Non-individual PAN)
    5. The KYC process going through STP flow (No downtime flow) will be marked as “success” on successful PAN verification via NSDL.
    
    c. **Handling failures:** 
    
    1. If any of the mentioned parameters  that needs a mandatory matching (PAN number, PAN name) received in response from NSDL PAN API response has a “No” match then:
    
    **Step 1 i): On passing PAN details available from Digilocker**
    
    1. If initially the PAN details are passed from Digilocker as input and we get non-matching response (PAN ≠ “E”, AND/ OR Name: “N”), then automatically, a “failure” response will be received by LSPs from DSP at NSDL Step.
    2. Exact failure responses are:
        1. PAN ≠ “E” → “PAN entered is not a valid PAN” And/Or
        2. Name = “N” → Name as per PAN is not valid
        3. PAN ≠ “E” and Name = “N” → PAN number and PAN name entered are not valid
    3. On receiving the “failure” response, DSP will again attempt by passing the PAN details (PAN number, PAN name) received by it from Volt in the NSDL PAN verification API. If NSDL still returns non-matching response for any of the above mentioned parameters, then UI shall be shown in the DSP journey asking for inputs from the user. [PAN: Fixed field, Name as per PAN]. Aadhaar DoB from Digilocker shall be passed to the NSDL API from backend.
    
    **Step 1 ii): When PAN details are not available from Digilocker, and LSP passes PAN details of the user for NSDL input.**
    
    1. Similar to the action mentioned above, on passing the PAN details from LSP, if we receive non-matching response for any of the mentioned parameters, UI shall be shown in the DSP journey asking for inputs from the user. [PAN: Fixed field, Name as per PAN]. Aadhaar DoB from Digilocker shall be passed to the NSDL API from backend.
    2. Customers can trigger PAN verification thrice via user input method. After 7 tries in 20 mins. “Maximum attempts reached for PAN verification” error will be shown to the customer in UI and given as a webhook to LSP as well. The number of retries and the cooldown time should be in a config that can be changed later. The LSP shall block the workflow at this step, and the user needs to redo the entire KYC again as a fresh application with new utility_reference_id.
    3. PAN number should be in the format  **XXXPX1234X.** 4th letter of the PAN should be “P” to indicate that the PAN belongs to an individual. If this requirement is not matched return error `“PAN in opportunity does not belong to an individual”` to LSPs in a webhook.  PAN verification API should not be triggered in this case. This error will result in KYC failure. 
    
    **Step 1 iii)** Possibility that LSP does not consume any detail (PAN, PAN Name, PAN DoB)
    
    1. If LSP does not capture/ verify the relevant PAN details on their end (PAN name), and we don’t have PAN record available from Digilocker, then directly UI should be shown to the user asking for relevant inputs. [PAN: Fixed field, Name as per PAN, DoB as per PAN]
    
    **Global condition** for successful KYC verification completion: Both verifier should be digilocker/ Hyperverge/ any other method used later on for KYC and primary_pan_verifier needs to be **Protean**.
    

---

**Non-STP flow:** 

1. When NSDL faces downtime, in the KYC flow, pan_verifier flag shall be turned to Signzy to be used as fallback for PAN verification.
2. The bank name and agreement name used here would be the affirmative PAN name received from Signzy API response as done currently.
3. At “submit opportunity”, there will be another global check if PAN is verified via Protean or not.
4. If the NSDL PAN is not verified then with the existing details (PAN number, PAN name, PAN/ Aadhaar DoB), the NSDL API shall be called again at submit opportunity.
5. If the NSDL still faces downtime, or with the given inputs the NSDL PAN fails to get verified due to some non-matching condition, then a task shall be created for the DSP ops team as PAN Verification deviation flow and the user shall be blocked in the journey here. The LSP shall be given a webhook of “User PAN is not verified via NSDL” here.
6. Ops team shall do the manual NSDL PAN verification by using the NSDL API manually with the required details provided to them [Digilocker Aadhaar and PAN data, LSP name data]. An option will be provided in the CC to do NSDL PAN Verification by ops team by entering the PAN details of the user received from LSP and Digilocker.
7. User shall be communicated, once the PAN is verified by DSP ops team to complete the loan application

---

## **6.  Design**

### https://www.figma.com/design/zim8uwuCQ2Aaj0O1T2OVq6/-New--Loan-application-journey?node-id=9648-25006&t=jCRZ6Xv98XzG92kb-0