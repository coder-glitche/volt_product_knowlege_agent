# Change in audit trail flow for PAN Validation API

: Ameya Aglawe
Created time: October 7, 2024 4:42 PM
Status: Pending Review
Last edited: October 17, 2024 8:05 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

In the applications in which we are not able to fetch PAN details (POV=null), the user’s KYC is not getting verified via BAJAJ KYC_POD. 

---

# **How do we measure success?**

- Reduction in number of application with Aadhar-PAN name mismatch completed successfully
- Reduction in Loan application completion TAT for applications with Aadhar-PAN name mismatch

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

We have to change the current flow for hitting the PAN Validation API. 

- **Current flow**
1. User signs up 
2. Verifies PAN & enters DOB 
3. Fetches funds 
4. Completes the KYC Digilocker step 
5. PAN Validation is hit at the CREDIT APPROVAL step 
6. Loan creation API is hit 

We will be going live with PAN Validation API, in two phases - 

1. Phase 1 : Controlled launch : We will monitor the applications under this launch & accordingly move to complete launch
2. Phase 2 : Complete launch 

**Phase 1 (Through admin action)** 

1. User signs up ***(timestamp stored)***
2. Verifies PAN & enters DOB
3. Fetches funds
4. User comes to KYC step
5. Taps on “Proceed with Digilocker”
6. User faces an issue "Please fetch PAN in digilocker/KYC details are getting verified"
7. User reports Ops
8. ***Ops team uses the admin action to hit the PAN validation API***
9. PAN Validation is hit ***(timestamp stored)***
10. We get PAN Validation response ***(timestamp stored)***
11. User goes to BAJAJ portal and completes the KYC Digilocker verification ***(timestamp stored)***
12. Loan creation API is hit (with the input of timestamps of the required request parameters in the required order)
13. Note : We will also log the request & response payload of the PAN verification API for tracking.

**Phase 2 (Flow added in application flow)** 

1. User signs up ***(timestamp stored)*** 
2. Verifies PAN & enters DOB 
3. Fetches funds 
4. User comes to KYC step 
5. Taps on “Proceed with Digilocker” 
6. PAN Validation is hit at KYC Digilocker step ***(timestamp stored)*** 
    1. If PAN status : E → User moves ahead in the application flow 
    2. If PAN status other than “E” → we block the customer and show the messaging 
        1. Primary message : “Cannot verify PAN”
        2. Secondary message : “Please contact our support team to proceed”
        - UI
            
            ![Screenshot 2024-10-17 at 7.05.16 PM.png](Change%20in%20audit%20trail%20flow%20for%20PAN%20Validation%20API/Screenshot_2024-10-17_at_7.05.16_PM.png)
            
    - De-prioritized item (please ignore)
        1. If DOB, Name : Y → Let customer proceed with the application 
        2. If DOB, Name : N → Open up a modal at the page with 
            1. Primary message : “Cannot verify PAN”
            2. Secondary message : “Please enter correct name/DOB”
    
    c. PAN Validation API Failure 
    
    - UI : Standard API failure modal (Ask user to try again)
        
        
7. We get PAN Validation response ***(timestamp stored)*** 
8. Completes the KYC Digilocker verification ***(timestamp stored)*** 
9. Loan creation API is hit (with the input of timestamps in the required request parameters) 

## Technical Requirements

- **PAN Validation request**
    - Current flow : We currently use DOB from KYC Digilocker for the DOB required in the request of PAN Validation API
    - New Flow : In the new flow we will use the DOB entered by the user at the initial PAN verification step
        - Request
            
            {
            
            "pan": "BzM1gst09995JhcblaTg==", (**User input)** 
            
            "name": "FKKFopfVWPyMuiRf90zhw==", **(Decentro PAN name)** 
            
            "fathername": "",
            
            "dob": "d4QJCklXN/zT2L8GnKFgwQ==", (**User input)** 
            
            "product": "t~eYRF1P/DWWoAJR2S1mKg=="
            
            }
            
        - Response
            
            {
            
            "statusCode": 200,
            
            "message": "Success",
            
            "data": {
            
            "pan": "AFMPHXXXXR",
            
            "pan_status": "E",
            
            **"name": "Y",**
            
            "fathername": "Y",
            
            **"dob": "Y",**
            
            "seeding_status": "Y"
            
            }
            
            }
            
    - We will only pass cases where "pan_status": "E", all other cases we block the application with the modal “Cannot Verify PAN”.
        - UI
            
            ![Screenshot 2024-10-17 at 5.53.12 PM.png](Change%20in%20audit%20trail%20flow%20for%20PAN%20Validation%20API/Screenshot_2024-10-17_at_5.53.12_PM.png)
            
    - PAN Validation API Failure
        - UI : Standard API failure modal
            
            
- **SFDC Request formats**
    - Current SFDC request format
        
        [
        {
        "FASRecords": {
        "MasterData": [
        {
        "sourcingChannelName": "SALTER TECHNOLOGIES PRIVATE LIMITED-Pratik Bagul"
        }
        ],
        "Account": [
        {
        "Name": "SARMISTHA ROUL",
        "Last_Name__c": "ROUL",
        "First_Name__c": "SARMISTHA",
        "Address_1st_Line__c": "K 86 Badhwar Park Railway",
        "Address_2nd_Line__c": "Officers Quarters Cuffe",
        "Address_3rd_Line__c": "Parade Mumbai Mumbai City Maharashtra",
        "AccCity__c": "Mumbai City",
        "Date_of_Birth__c": "1980-04-05",
        "PANNumber__c": "AOAPR3563F",
        "Mobile__c": "9337598814",
        "Current_Email_Id__c": "[saku86816@gmail.com](mailto:saku86816@gmail.com)",
        "PinCode__c": "400005",
        "Fathers_Husbands_Name__c": "pitambar majhy",
        "Gender__c": "Female",
        "Marital_Status__c": "Single",
        "Qualification__c": "Graduate",
        "Spouse_Name__c": null,
        "Residence_Status__c": "Owned",
        "Permanent_Residence_Address1__c": "K 86 Badhwar Park Railway",
        "Permanent_Residence_Address2__c": "Officers Quarters Cuffe",
        "Permanent_Residence_Address3__c": "Parade Mumbai Mumbai City Maharashtra",
        "Permanent_City__c": "Mumbai City",
        "Permanent_PinCode__c": "400005",
        "Permanent_State__c": "MAHARASHTRA",
        "Residence_TypeAcc__c": "Owned",
        "Permanent_Address_as_above__c": "true",
        "Current_STDCode__c": "91",
        "Residence_Landline_phone__c": "9337598814"
        }
        ],
        "Opportunity": [
        {
        "StageName": "underwriting",
        "Product__c": "FAS",
        "Location__c": "Pune",
        "Branch__c": "PUNE",
        "Branch_Name__c": "a0A90000000eLxU",
        "Sourcing_Channel__c": "a0U0o00002Avb6o",
        "Loan_Type__c": "FAS Mutual Funds",
        "End_Use__c": "Personal Use",
        "Name": "SARMISTHA ROUL",
        "Customer_reference_number__c": null,
        "CloseDate": "2027-10-01",
        "Loan_Amount__c": "200000",
        "Amount_Rs__c": "1769",
        "Processing_Fees__c": null,
        "Tenor__c": "36",
        "Approved_Tenor__c": "36"
        }
        ],
        "Contact": [
        {
        "ApplicantType__c": "Primary",
        "Customer_Type__c": "Individual",
        "Salutation": null,
        "FirstName": "SARMISTHA",
        "LastName": "ROUL",
        "Gender__c": "Female",
        "PAN_Number__c": "AOAPR3563F",
        "Date_of_Birth__c": "1980-04-05",
        "Pin_Code__c": "400005",
        "Mobile__c": "9337598814",
        "Email__c": "[saku86816@gmail.com](mailto:saku86816@gmail.com)",
        "Address_1__c": "K 86 Badhwar Park Railway",
        "Address_2__c": "Officers Quarters Cuffe",
        "Address_3__c": "Parade Mumbai Mumbai City Maharashtra",
        "AppCity__c": "Mumbai City",
        "State__c": "MAHARASHTRA",
        "residence_type__c": "Owned",
        "Permanant_Address_Line_1__c": "K 86 Badhwar Park Railway",
        "Permanant_Address_Line_2__c": "Officers Quarters Cuffe",
        "Permanant_Address_Line_3__c": "Parade Mumbai Mumbai City Maharashtra",
        "Permanent_Pin_Code__c": "400005",
        "Permanant_City__c": "Mumbai City",
        "Permanent_State__c": "MAHARASHTRA",
        "Permanent_Address_same_as_Residence__c": "true",
        "Father_Spouse_Salutation__c": "Mr",
        "Father_Spouse__c": "FATHER",
        "Father_Spouse_First_Name__c": "pitambar",
        "Father_Spouse_Last_Name__c": "majhy",
        "Mother_Salutation__c": "Mrs.",
        "Mother_First_Name__c": "sabita",
        "Mother_Last_Name__c": "majhy",
        "Marital_Status__c": "Single",
        "District__c": "Mumbai City",
        "Occupation_CKYC__c": "Professional",
        "Occupation__c": "Professional",
        "Customer_Device_IP__c": "240.17.224.105",
        "Customer_Device_Type__c": "Laptop",
        "Partner_Website__c": "[www.voltmoney.in](http://www.voltmoney.in/)",
        "Website_IP_Address__c": "3.111.156.109",
        "Customer_Consents_with_date_and_time__c": "2024-10-01 14:51:13",
        "IMA_Reg_no__c": "2024-10-01 12:22:31",
        "Aadhar_Number__c": null,
        "AssistantName": "2024-10-01 14:51:13",
        "PAN_details_are_correct__c": "Yes",
        "PAN_Response__c": "{\"data\":{\"dob\":\"Y\",\"name\":\"Y\",\"pan\":\"AOAPR3563F\",\"pan_status\":\"E\",\"seeding_status\":\"Y\"},\"message\":\"Success\",\"statusCode\":200}",
        "Pan_Check_Status__c": "PanRequestDateTime: 2024-10-01 14:51:13 || PanResponseDateTime: 2024-10-01 14:51:13"
        }
        ],
        "ScripDetails": [
        {
        "Digital_Scrip_Name__c": "UTI Flexi Cap Fund Regular Plan",
        "Digital_Scrip_Type__c": null,
        "Number_of_Shares__c": "592.902",
        "Digital_Scrip_market_price__c": "335.0895",
        "Digital_Scrips_Eligibility__c": "89400",
        "Digital_Scrip_Category__c": null,
        "ISIN__c": "INF789F01513"
        },
        {
        "Digital_Scrip_Name__c": "UTI Mid Cap Fund Regular Plan",
        "Digital_Scrip_Type__c": null,
        "Number_of_Shares__c": "760.673",
        "Digital_Scrip_market_price__c": "323.1493",
        "Digital_Scrips_Eligibility__c": "110600",
        "Digital_Scrip_Category__c": null,
        "ISIN__c": "INF789F01810"
        }
        ],
        "BankDetails": [
        {
        "Depository_Participant_Name__c": "",
        "Depository_Participant_Id__c": "",
        "ClientName__c": "Bajaj",
        "ClientId__c": "123",
        "TrackingId__c": "12345",
        "Account_Type__c": "Savings A/c",
        "Bank_Name__c": "Axis Bank",
        "Bank_Branch__c": "CHURCHGATE",
        "IFSC_Code__c": "UTIB0000695",
        "Bank_Acct_Number__c": "917010038200058",
        "MICR_Code__c": "400211059",
        "Applicant_Name__c": "SARMISTHA ROUL"
        }
        ],
        "Applicant": [
        {
        "CKYC_No__c": null,
        "Proof_of_Identity__c": "OVD-PAN Card",
        "Identity_Document_No__c": "AOAPR3563F",
        "Identity_Document_Expiry_Date__c": "",
        "Proof_of_Residence_Address_Submitted__c": "OVD - Aadhar Card:I",
        "Residence_Address_Doc_No__c": "1710",
        "Residence_Address_Expiry_Date__c": "",
        "Proof_of_Address_Submitted_for_Permanent__c": "OVD - Aadhar Card",
        "Permanent_Address_Doc_No__c": "1710",
        "Permanent_Address_Expiry_Date__c": "",
        "CallStatus__c": "Success - 2024-10-01 14:24:44",
        "CKYC_Data__c": "Digilocker",
        "Note_code__c": "Non-Face to Face",
        "clientIdStamp__c": "140972624142110844",
        "Applicant_Type__c": "Primary"
        }
        ],
        "RepaymentModeDetails": [
        {
        "Open_ECS_Max_Limit__c": "1000000",
        "ECS_Start_Date__c": "2024-10-01",
        "ECS_End_Date__c": "2027-10-01",
        
        "ECS_Amount__c": "1000000",
        "Open_ECS_Facility__c": null
        }
        ],
        "CamDetails": [
        {
        "currencyIsoCode": "INR",
        "CurrencyIsoCode": "INR",
        "Name": "SARMISTHA ROUL",
        "ROI__c": "10.49",
        "Loan_Amount__c": "200000",
        "CY_Tenor__c": "36"
        }
        ],
        "attachments": null
        }
        }
        ]
        
    - Current order of timestamps of parameters in the loan creation API request
        1. "CallStatus__c": "Success - 2024-10-01 14:24:44" (KYC Digilocker) 
        2. "Customer_Consents_with_date_and_time__c": "2024-10-01 14:51:13", (PAN Validation request)
        3. "PanRequestDateTime: 2024-10-01 14:51:13  (PAN Validation request)
        4.  PanResponseDateTime: 2024-10-01 14:51:13"  (PAN Validation response)
    - New order of timestamps of parameters in the loan creation API request
        1. "Customer_Consents_with_date_and_time__c": "2024-10-01 14:21:13", (Customer sign-up timestamp) - **[User sign up time : OTP verification]**
        2. "PanRequestDateTime: 2024-10-01 14:31:13  **[PAN Validation request when user taps on proceed with Digilocker]**
        3.  PanResponseDateTime: 2024-10-01 14:31:13"  **[PAN Validation response]**
        4. "CallStatus__c": "Success - 2024-10-01 14:41:44" **[User completes the KYC Digilocker verification]**

## Scenarios

- What if we get DOB mismatch error? How will we handle this?
    - The API would still work & we’ll get "dob"/”name”/”seedingStatus”: "N" in the response, we’ll still send such applications to BAJAJ (Confirmed with Pratik Bagul on call, he provided an email confirmation as well)
- Open points
    - PAN Validation request/response time required in milliseconds? - Anirudha confirmed this is not required.
    - Passing of cases with PAN status other than E with BAJAJ to avoid over handling? - Will block the KYC digilocker step itself
    - Modal should close → Add a CTA in “okay, got”
    - Set up a report with cases where panstatus is not “E”

---

# **Design**

---

https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=10128-11701&t=UrxSHNoQloFkFj2K-1

# **Analytics**

---

- We should store the Aadhar (KYC_POD), PAN (decentro), Bank names (Pennydrop) in DB. This will help to analyse the impact of this implementation.
- BAJAJ PAN verification → Save Amplitude event → Log the response of PAN verification API
    - Name & Attributes
    
    | **Journey** | **Events name** | **Events property** | **Sample value** | **Trigger from** |
    | --- | --- | --- | --- | --- |
    | - User completes fetch step, comes to KYC Digilocker page for BAJAJ and taps on “Proceed to Digilocker  | PAN_Validation_SUCCESS | "pan_status": "E” |  | BE  |
    |  | PAN_Validation_FAILED | "pan_status" other than "E” |  | BE |
    |  | PAN_Validation_FAILED | "statusCode": 200 |  | BE  |
- Set up a report with cases where panstatus is not “E” and API failure

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