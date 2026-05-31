# TATA Dedupe API with updated BRE

: Ameya Aglawe
Created time: September 11, 2024 2:35 PM
Status: Pending Review
Last edited: November 21, 2024 12:42 PM
Owner: Ameya Aglawe

# **What problem are we solving?**

- For users whose lender is assigned as TATA, either via BRE logic or hardcoding, an existing loan account with TATA is only detected after the user has completed the application process.
- This leads to a poor user experience, as the user is required to un-pledge their funds and restart the application process from scratch with a different lender.

---

# **How do we measure success?**

- Number of applications in which a dedupe (after the dedupe API is integrated) is detected at the time BRE is run.
- Atleast 99% of customers whose loan is booked with TATA to not be dedupe rejected.
- Number of applications which get rejected due to presence of an active account with TATA.
- %age of applications which get rejected due to presence of an active account with TATA.
- API success rate of TATA Dedupe to be at least 95%

---

# **How are others solving this problem?**

- Most lenders and LSP do a dedupe check with parameters (PAN, Mobile, etc) at the start of the journey itself
- Most lenders and LSP do a dedupe check with parameters (PAN, Mobile, etc) at the end of the journey before sanction as a fall-back

This ensures that only customers who don’t have a relationship go through till the last stage of the application.

---

# **What is the solution?**

We will hit the TATA dedupe APIs that will return if a customer holds an active LAS/LAMF relationship with TATA. 

1. The customer is checked for the partner from whom the application is being received
2. We check the DB if there are any specific lender assigned to the partner (eg. Jupiter and some MFDs)
3. If the customer has only TATA assigned as the lender OR any lender, the rest of the process follows.
4. At the step of lender assigning through BRE - dedupe check will be done using PAN number of the user for both TATA and BFL
5. Whenever there is a lender change from BAJAJ to TATA through admin panel  
6. Posidex check to be done if the customer is dedupe negative (customer has no relationship with TATA)
7. Dedupe will be the first check in the BRE and basis the outcome, the rest of the BRE logic will be maintained as it is.

**Dedupe flow**

![Screenshot 2024-09-16 at 6.51.27 PM.png](TATA%20Dedupe%20API%20with%20updated%20BRE/Screenshot_2024-09-16_at_6.51.27_PM.png)

**BRE (Dedupe + Other rules)** 

![Screenshot 2024-09-23 at 8.39.35 PM.png](TATA%20Dedupe%20API%20with%20updated%20BRE/Screenshot_2024-09-23_at_8.39.35_PM.png)

Open Points

- What is the CIBIL score that needs to be considered?
- Does Tata do NTC customers?

**For MFDs/B2B/B2C**

1. **Pre BRE stage** 
    1. User comes to the app & fetches funds 
2. **During BRE stage**
    1. Application comes at the set credit limit page and taps on “SET CREDIT LIMIT” CTA - 
        1. BRE will run at this step which will check if the customer has a relationship with TCL on LAS/LAMF product.
        2. Application passes through first 3 rules of BRE (min. eligible limit, Equifax soft pull, dedupe) 
            
            
            | **TATA** | **BAJAJ** | **Lender assignment** | **Blockers & Action post lender assignment** |
            | --- | --- | --- | --- |
            | Not eligible | Not eligible | Lender cannot be assigned |  |
            | Not eligible | Eligible | BAJAJ | KYC_POD issue:  Will be handled operationally |
            | Eligible | Not eligible | TATA | CIBIL, Aadhar/Bank-PAN name mis-match: Will be handled through credit referral |
            | Eligible | Eligible | Will be based on other rules of BRE |  |
3. **Post BRE stage** 
    1. BAJAJ assigned as lender - 
        1. If there is any issue while the user is going through the application (KYC_POD etc.)
            1. Then the Ops team tries to change the lender to TATA through admin action 
            2. Once the Ops person taps on the CTA to change lender 
            3. Then we will again hit the TATA dedupe API 
                
                
                | Dedupe  | State  | Action  | Admin action UI  |
                | --- | --- | --- | --- |
                | TATA | Detected | Do not change the lender to TATA | Dedupe : Loan account already with TATA exists. Cannot change the lender to TATA |
                | TATA | Not detected  | Change the lender to TATA  | Not required  |

## Requirements overview (optional)

### User stories / User flow

Below is the user journey.

- Customer completes the fetch step (after OTP) and sets the credit limit
- At this stage, the lender BRE will run which will include TATA as the lender
- At the BRE stage, TATA dedupe API will be hit along with Bajaj dedupe API
- If the customer isn’t eligible with TATA, they will be routed through Bajaj
- If the customer isn’t eligible with Bajaj, they will be routed through TATA
- If the customer isn’t eligible with either of the lenders, the relevant messaging will be shown

## Requirements

1. Adding TATA dedupe rule in the BRE. 
    - API level handling
        1. In case customer exists & client is active, & ProductName= product_type=LAMF is CLOSED then loan application can be create with TATA. 
        
        | **Existing customer** | **Client Status** | **ProductName** | **Account status** | **Conclusion** |
        | --- | --- | --- | --- | --- |
        | NO | - | - | -  | Can create account with TATA for LAMF (with create client API) |
        | YES | ACTIVE | Any product name | ACTIVE | Cannot create account with TATA for LAMF |
        | YES | ACTIVE | Any product name | CLOSED | Can create account with TATA for LAMF (with update client API) |
    - Note : If existing customer : YES, Client status : Active, Account_Status : CLOSED, and ClientCommonCode=null, then we will generate a client code & pass it in the Update Client Master API (just like how we do it for Create Client API)
2. Update client API for the cases in which (TATA dedupe API response is existing customer : “YES”)
    - Request
        1. (We will send the same fields that we send in create client API request along with an additional field CommonClientCode rest of the feilds we can keep as null)
        
        [
            {
                "TransactionID": null,
                "UniqueRecordID": "1000835165",
                "FirstName": "MANISH",
                "MiddleName": "SUDHIR",
                "LastName": "PATIL",
                "BOCodeSecurity": "",
                "FatherOrHusbandName": "SUDHIR",
                "HeadOfFamily": "No",
                "BOCodeMF": "",
                "FamilyID": "1298",
                "FamilyName": "LAS_DIGITAL",
                "GroupID": "1210",
                "GroupName": "LAS_DIGITAL",
                "CommenceOn": "2023-09-09",
                "BOCodeDebt": "",
                "TaxStatusCode": "01",
                "TaxStatus": "Individual",
                "TaxPercent": "0",
                "PoolAccount": "Yes",
                "UCC": "",
                "BOCodeNBFC": "",
                "CategoryCode": "20",
                "Category": "Platinum",
                "CommonClientCode": null,
                "BorrowerIndustryID": "",
        
        "BorrowerIndustryName": "",
                "TaxIdOrPAN": "APLPP8042S",
                "TAN_No": "",
                "GIR_No": "",
                "TaxWaiverInFile": "",
                "CircleOrWardOrDist": "",
                "AadharCardNo": "XXXXXXXX4655",
                "RBIApprovalNo": "",
                "RBIApprovalDate": "",
                "TaxDeductionStatus": "",
                "SEBIRegistrationNo": "",
                "Address1": "K-2601 RUSTAMJEE AZZIANO MUMBAI NASIK ",
                "Address2": "HIGHWAY MAJIWADA THANE NEXT TO RUSTAMJEE ",
                "Address3": "CAMBRIDGE SCHOOL Thane Thane Thane Thane ",
                "City": "Thane",
                "PinCode": "400601",
                "StateID": "27",
                "State": "Maharashtra",
                "CountryID": "5",
                "Country": "India",
                "ResTelNo": "",
                "MobileNo": "9820652320",
                "Fax": "",
                "Email": "[mpatil3084@gmail.com](mailto:mpatil3084@gmail.com)",
                "OffAddress1": "",
                "OffAddress2": "",
                "OffAddress3": "",
        
        "OffCity": "",
                "OffPinCode": "",
                "OffStateID": "",
                "OffState": "",
                "OffCountryID": "",
                "OffCountry": "",
                "OffTelNo": "",
                "OffMobileNo": "",
                "OffFax": "",
                "OffEmail": null,
                "DefaultMailing": "Home",
                "DeciderName": null,
                "DeciderTelNo": null,
                "DeciderFax": null,
                "OperationPersonName": null,
                "OperationPersonTelNo": null,
                "OperationPersonFax": null,
                "Designation": null,
                "OtherAddress1": null,
                "OtherAddress2": null,
                "OtherAddress3": null,
                "OtherCity": null,
                "OtherPinCode": null,
                "LoanRequests": "Investments In Securities",
                "DOB": "30-Oct-1984",
                "GuardianName": null,
                "PlaceOfBirth": null,
        
        "Salutation": null,
                "Gender": "Male",
                "MaritalStatus": "Married",
                "SpouseName": null,
                "WeddingDate": null,
                "SpouseDOB": null,
                "OccupationCode": "7",
                "ProfessionalCode": null,
                "SalariedCode": null,
                "OtherOccupation": null,
                "OccupationType": null,
                "GrossAnnualIncome_InLakhs": null,
                "EstFinancialWealth_InLakhs": null,
                "NameOfEmployer": null,
                "YearsOfEmploymentOrBusiness": null,
                "EducationalQualification": null,
                "PersonalAddress1": null,
                "PersonalAddress2": null,
                "PersonalAddress3": null,
                "Nationality": "Indian Citizen",
                "NationalityIfOther": null,
                "NatureOfBusiness": null,
                "VoterID": null,
                "PassportNo": null,
                "PlaceOfIssue": null,
                "PassportIssueDate": null,
                "PassportExpiryDate": null,
        
        "InterCompany": "No",
                "Jurisdiction": null,
                "DateOfIncoporation": "01-01-1990",
                "DateOfCommencement": null,
                "CorporateNatureOfBusiness": null,
                "LegalConstitutionID": null,
                "LegalConstitution": null,
                "RegisteredOfficeDUNSNumber": null,
                "BorrowerDUNSNumber": null,
                "EstFinancialWealth_InMillion": null,
                "CorporateGrossAnnualIncome_InLakhs": null,
                "FGIInterCompanyCode": "",
                "Email_YesNo": "[mpatil3084@gmail.com](mailto:mpatil3084@gmail.com)",
                "Fax_YesNo": "",
                "Mail_YesNo": null,
                "Hand_YesNo": null,
                "AlertEmail_YesNo": "",
                "AlertFax_YesNo": "",
                "AlertSMS_YesNo": "",
                "EmailOnDeactivationofAccount": null,
                "EmailOnCorporateAction": null,
                "PromotionalMaterial": null,
                "EmailOnCloseOfAccount": null,
                "EmailOnFreezeOfAccount": null,
                "SharePhoneOrEmail": null,
                "Statement": null,
                "ChangeInClientInformation": null,
        
        "InternetID": null,
                "ClientBankDetailsUpdate": [
                    {
                        "Action": null,
                        "BankId": "0",
                        "BankName": "HDFC Bank",
                        "BankBranch": "MUMBAI - POWAI",
                        "MICR": "400240039",
                        "IFSC": "HDFC0000239",
                        "AccountNo": "02391140093584",
                        "FirstHolderName": "Manish Sudhir Patil",
                        "SecondHolderName": null,
                        "ThirdHolderName": null,
                        "AcctOpeningDt": "12-09-2018",
                        "DefaultAccount": "Yes",
                        "Accounttype": "Savings",
                        "BankDtl_CCY": "INR",
                        "PaymentMode": "Account/Fund Transfer",
                        "PaymentCode": "I",
                        "LocationCode": null
                    },
                    {
                        "Action": null,
                        "BankId": "0",
                        "BankName": "STATE BANK OF INDIA",
                        "BankBranch": "MUMBAI - POWAI",
                        "MICR": "110002006",
        
        "IFSC": "SBIN0000745",
                        "AccountNo": "02391140093589",
                        "FirstHolderName": "Manish Sudhir Patil",
                        "SecondHolderName": null,
                        "ThirdHolderName": null,
                        "AcctOpeningDt": "12-09-2018",
                        "DefaultAccount": "No",
                        "Accounttype": "Savings",
                        "BankDtl_CCY": "INR",
                        "PaymentMode": "Account/Fund Transfer",
                        "PaymentCode": "I",
                        "LocationCode": null
                    }
                ],
                "ClientBrokerDetailsUpdate": [
                    {
                        "Action": null,
                        "ExchangeId": "",
                        "ExchangeName": "",
                        "BrokerId": "",
                        "BrokerName": "",
                        "Address": null,
                        "AccountNo": "",
                        "FirstHolderName": "",
                        "AccountOpeningDt": ""
                    }
                ],
        
        "ClientDPDetailsUpdate": [
                    {
                        "Action": null,
                        "Depository": "NSDL",
                        "DPName": "IN303116",
                        "DPMainCode": "268",
                        "DPAccountNo": "13742676",
                        "DpId": "IN303116",
                        "FirstHolderName": "MANISH SUDHIR PATIL",
                        "SecondHolderName": null,
                        "ThirdHolderName": null,
                        "AcctOpeningDt": "12-06-2018",
                        "POAYN": "Yes",
                        "DefaultDp": "No",
                        "AccountType": "1",
                        "AccountTypeName": "Equity",
                        "PrimaryHolderYN": "Yes"
                    }
                ],
                "ClientKeyManagementPersonnelUpdate": [
                    {
                        "Action": null,
                        "Designation": "NA",
                        "Address": "NA",
                        "DUNSNo": null,
                        "NamePrefix": null,
                        "FullName": "NA",
        
        "Relation": "",
                        "RelatedType": "",
                        "Gender": "NA",
                        "PANNo": null,
                        "PassportNo": null,
                        "VoterId": null,
                        "Address2": null,
                        "Address3": null,
                        "City": "",
                        "StateCode": "27",
                        "CountryId": "5",
                        "PinCode": null,
                        "AadharCardNo": null,
                        "Contactno": null
                    }
                ],
                "ClientCreditFacilityUpdate": [
                    {
                        "Action": null,
                        "BankOrInstitutionOrCompanyName": "",
                        "AccountNo": "",
                        "AmountOfLoan": null,
                        "TenureOfLoan": null,
                        "EMIAmount": null
                    }
                ],
                "ClientCreditCardUpdate": [
        
        {
                        "Action": null,
                        "CCBankOrInstitutionOrCompanyName": "",
                        "CreditCardNo": "",
                        "DateOfExpiry": "",
                        "TypeOfCard": ""
                    }
                ],
                "ClientRelatedCompaniesUpdate": [
                    {
                        "Action": null,
                        "RelatedCompanyID": "",
                        "RelatedCompanyName": "",
                        "RelationWithCompany": "",
                        "RelationID": "",
                        "Received": "",
                        "DateOfIntimation": ""
                    }
                ],
                "ClientIntroducerUpdate": [
                    {
                        "ExistingClient": "",
                        "IntroducerName": "",
                        "AddressOfIntroducer1": null,
                        "AddressOfIntroducer2": null,
                        "AddressOfIntroducer3": null,
                        "MappinID": null,
        
        "IntroducerClientCode": null,
                        "NameOfEmployeeInterviewed": null,
                        "DesginationOfEmployeeInterviewed": null
                    }
                ],
                "ClientBranchDetailsUpdate": [
                    {
                        "Action": null,
                        "BranchCode": "386",
                        "BranchName": "DELHI RAJENDRA PLACE",
                        "LocationID": "02",
                        "LocationName": "New Delhi",
                        "RegionName": null,
                        "WefDate": "21-Sep-2023"
                    }
                ],
                "ClientSubBrokerDetailsUpdate": [
                    {
                        "Action": null,
                        "SubBrokerID": null,
                        "SubBrokerName": null,
                        "WefDate": "21-Sep-2023"
                    }
                ],
                "ClientPrimaryRMUpdate": [
                    {
                        "Action": null,
        
        "ManagerCode": "11",
                        "ManagerName": "JALINDAR AVHAD",
                        "ManagerEmailID": "[Jalindar.Avhad@tatacapital.com](mailto:Jalindar.Avhad@tatacapital.com)",
                        "ManagerMobileNo.": "9870003436",
                        "WefDate": "21-Sep-2023"
                    }
                ],
                "ClientSecondaryRMUpdate": [
                    {
                        "Action": null,
                        "ManagerCode": "",
                        "ManagerName": "",
                        "ManagerEmailID": null,
                        "ManagerMobileNo.": null,
                        "WefDate": ""
                    }
                ],
                "ClientGSTDetailsUpdate": [
                    {
                        "Action": null,
                        "StateCode": "22",
                        "State": "Maharashtra",
                        "GSTIN": "",
                        "DefaultLocation": "yes",
                        "IsGSTExempted": "no",
                        "GSTExemptionDesc": null,
                        "IsRelatedParty": "no",
        
        "RelatedPartyDesc": null
                    }
                ],
                "OtherDetails": [
                    {
                        "Employee": null,
                        "Employee Code": null,
                        "Remarks 1": null,
                        "Remarks 2": null
                    }
                ]
            }
        ]
        
    - Response
        
        **Response** 
        
        {
            "ClientMasterUpdateData": [
                {
                    "UniqueRecordID": "1000835165",
                    "RecordStatusCode": "0",
                    "Remarks": "Success"
                }
            ],
            "status": {
                "Status": "Success",
                "Code": "01",
                "Remarks": ""
            }
        
        }
        
3. BRE logic 
    - Logic
        1. Input : Customer entered PAN 
        2. BRE runs 
        3. Check : BAJAJ & TATA dedupe 
        
        | **TATA Dedupe** | **BAJAJ Dedupe** | **Lender assignment** | **Blockers & Action post lender assignment** |
        | --- | --- | --- | --- |
        | Yes  | Yes  | Lender cannot be assigned |  |
        | Yes | No  | BAJAJ | KYC_POD issue:  Will be handled operationally |
        | No  | Yes  | TATA | CIBIL, Aadhar/Bank-PAN name mis-match: Will be handled through credit referral  |
        | No  | No  | Will be based on other rules of BRE |  |
        1.  Other rules check (when there’s no dedupe at both the lender’s end) : As mentioned in the Lender BRE Grid below : 
        
        ![Screenshot 2024-09-23 at 8.39.35 PM.png](TATA%20Dedupe%20API%20with%20updated%20BRE/Screenshot_2024-09-23_at_8.39.35_PM.png)
        
        ---
        
4. Error message to be shown on the UI as per below scenarios.
    - Messaging
        
        
        | **Scenario** | **Tata** | **Bajaj** | **Message** | **Show at**  |
        | --- | --- | --- | --- | --- |
        | Lender allocated basis logic | Eligible | Eligible |  |  |
        | Only TATA is eligible | Eligible | Not Eligible |  |  |
        | Only TATA is eligible | Not Eligible | Eligible |  |  |
        | Not eligible at both TATA & BAJAJ | Not Eligible | Not Eligible | - Loan account cannot be created - You already have active loan account with our lending partners | - Volt App/ Web UI |
        | Ops changing lender from TATA to BAJAJ | Eligible  | Eligible  |  |  |
        | Ops changing lender from BAJAJ to TATA | Eligible  | Eligible  |  |  |
        | Ops changing lender from TATA to BAJAJ | Eligible  | Not eligible  | - Dedupe : Loan account already with BAJAJ exists. Cannot change the lender to BAJAJ.  | - Admin tool  |
        | Ops changing lender from BAJAJ to TATA  | Not eligible  | Eligible  | - Dedupe : Loan account already with TATA exists. Cannot change the lender to TATA.  | - Admin tool  |
5. API Documentations 
    - Dedupe
        
        [TATADedupe.docx](TATA%20Dedupe%20API%20with%20updated%20BRE/TATADedupe.docx)
        
    - Update Client
        
        End point : https://miles-uat-apicast.apps.tclnprdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdates 
        
        Works same as createclient
        

**Update - 21 Nov :** Since entire traffic is shifted to TCL we have done a quick handling for TCL dedupe API wherein we will move all the cases with existingCustomer:Yes & accountStatus=INACTIVE to BFL rather than using TCL’s updateClientMaster API to update user details & open loan account with TCL. Additionally, since DSP is going live by 24 Nov, we will direct cases where there is a dedupe in both BFL & TCL to DSP. Right now if there is a dedupe at both we will assign the lender as BFL. 

---

# **Design**

- https://www.figma.com/design/u5fpymb6jC6ubzT9YUXFgb/Loan-application-flow?node-id=10128-11701&t=SqTLieaZ1exxSzdZ-1

---

# **Analytics**

- Log when the application goes through the dedupe check (timestamp)
- Log when dedupe is detected at TATA’s end “Dedupe detected with TATA for pan :”
- Log all API failure (exception) 

This handling is already done for BAJAJ dedupe API.  

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

Open points 

1. Which loan product can we consider? (LAS, LAMF?) - Open point for Chandrama → In which case will TATA allow the loan account to be created 
2. Can we consider the application if  “Client Active Status” is Closed & Deactive. -Open point for Chandrama 
3. How to stitch both the dedupes together 

### User stories

- Customer starts a new application → Enters phone number → Enters emailID → Fetches portfolio → Taps on “SET CREDIT LIMIT” → BRE runs → Check min. eligible limit & Equifax soft pull → Check BAJAJ & TATA dedupe → Check other rules of BRE → Lender is assigned based on the rules
    - Lender assigned as TATA
        - User moves forward in the application with TATA as lender
        - User encounters an issue due to which Ops tries to change the lender
        - When Ops person taps on change lender option in admin tool
            - There is a dedupe check for BAJAJ
                - Dedupe detected
                    - Yes : Call-out in admin tool that lender cannot be changed because dedupe is detected with BAJAJ
                    - No : Change lender to TATA
    - Lender assigned as BAJAJ
        - User moves forward in the application with BAJAJ as lender
        - User encounters an issue due to which Ops tries to change the lender
        - When Ops person taps on change lender option in admin tool
            - There is a dedupe check for TATA
                - Dedupe detected
                    - Yes : Call-out in admin tool that lender cannot be changed because dedupe is detected with TATA
                    - No : Change lender to BAJAJ

**Create client API** 

**Request** 

[
{
"AadharCardNo": "XXXXXXXX3977",
"Address1": "S/O Jai Prakash Lalmohalla jametul banat nagar n p jiyanpurJiyanpur",
"Address2": "JiyanpurBurhanpurAzamgarh",
"Address3": "Uttar PradeshIndia276140",
"BorrowerIndustryID": "2",
"BorrowerIndustryName": "Non face to face customers",
"Category": "Platinum",
"CategoryCode": "20",
"City": "Azamgarh",
"ClientBankDetails": [
{
"AccountNo": "50100533913884",
"AccountType": "Savings",
"AcctOpeningDate": "12-09-2018",
"BankBranch": "AZAMGARH",
"BankCurrency": "INR",
"BankName": "HDFC Bank",
"DefaultAccount": "Yes",
"FirstHolderName": "Manish Srivastava",
"IFSC": "HDFC0001884",
"MICR": "276240002",
"PaymentCode": "I",
"PaymentMode": "Account/Fund Transfer"
}
],
"ClientBranchDetails": [
{
"BranchCode": "386",
"BranchName": "DELHI RAJENDRA PLACE",
"LocationID": "02",
"LocationName": "New Delhi",
"RegionName": "",
"WefDate": "26-Sep-2024"
}
],
"ClientBrokerDetails": [],
"ClientCreditCard": [],
"ClientCreditFacility": [],
"ClientDPDetails": [],
"ClientGSTDetails": [
{
"DefaultLocation": "Yes",
"GSTIN": "",
"IsGSTExempted": "No",
"IsRelatedParty": "No",
"State": "Uttar Pradesh",
"StateCode": "42"
}
],
"ClientIntroducer": [],
"ClientKeyManagementPersonnel": [],
"ClientPrimaryRM": [
{
"ManagerCode": "34",
"ManagerEmailID": "[Sagar.Chheda@tatacapital.com](mailto:Sagar.Chheda@tatacapital.com)",
"ManagerMobileNo": "7208111020",
"ManagerName": "Sagar Chheda",
"WefDate": "26-Sep-2024"
}
],
"ClientRelatedCompanies": [],
"ClientSecondaryRM": [],
"ClientSubBrokerDetails": [
{
"SubBrokerID": "103",
"SubBrokerName": "SALTER TECHNOLOGIES PRIVATE LIMITED",
"WefDate": "26-Sep-2024"
}
],
"CommenceOn": "2024-09-26",
"CommonClientCode": "393618848812",
"Country": "India",
"CountryID": "91",
"DOB": "13-Apr-1976",
"DefaultMailing": "Home",
"Email": "[manishlal768@gmail.com](mailto:manishlal768@gmail.com)",
"FamilyID": "1298",
"FamilyName": "LAS_DIGITAL",
"FatherOrHusbandName": "JAIPRAKASH LAL",
"FirstName": "Manish",
"Gender": "Male",
"GroupID": "1210",
"GroupName": "LAS_DIGITAL",
"HeadOfFamily": "No",
"LastName": "Srivastava",
"LoanRequests": "Investments In Securities",
"MaritalStatus": "Unmarried",
"MiddleName": "Lal",
"MobileNo": "9936738179",
"Nationality": "Indian Citizen",
"OccupationCode": "7",
"OtherDetails": [],
"PinCode": "276140",
"PoolAccount": "Yes",
"State": "Uttar Pradesh",
"StateID": "42",
"TaxIdOrPAN": "CZUPS3657L",
"TaxPercent": "0",
"TaxStatus": "Individual",
"TaxStatusCode": "01",
"UniqueRecordID": "393618848812"
}
]

**Response** 

{
"retStatus": "SUCCESS",
"sysErrorMessage": "",
"sysErrorCode": "",
"create_Client": {
"CreateClient": {
"clientMasterData": [
{
"recordStatusCode": 0,
"uniqueRecordID": 393618848812,
"remarks": "Success",
"customerID": 33702
}
],
"createClientStatus": null
}
}
}

Comments 

1. Customer POV
2. BAJAJ 
3. TATA
4. Partner 
5. Volt