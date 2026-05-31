# Update user details (for TCL, BFL, DSP)

: Ameya Aglawe
Created time: November 20, 2024 6:54 PM
Status: In progress
Last edited: December 31, 2024 1:18 PM

# **What problem are we solving?**

---

Users have no option to update their phone, email, bank account & mandate details on our app after completing the loan application 

# **How do we measure success?**

---

- Number of details update requests through our app < 20/month
- Man-hours spent & number of tickets created for updating user details goes down by 50%

# **How are others solving this problem?**

---

- Grow

![Screenshot 2024-11-29 at 3.18.01 PM.png](Update%20user%20details%20(for%20TCL,%20BFL,%20DSP)/Screenshot_2024-11-29_at_3.18.01_PM.png)

- Uber (comms)

![Screenshot 2024-12-09 at 12.39.52 PM.png](Update%20user%20details%20(for%20TCL,%20BFL,%20DSP)/Screenshot_2024-12-09_at_12.39.52_PM.png)

- CRED

![Screenshot 2024-11-29 at 3.19.13 PM.png](Update%20user%20details%20(for%20TCL,%20BFL,%20DSP)/Screenshot_2024-11-29_at_3.19.13_PM.png)

# **What is the solution?**

---

- User details need to be updated
    - The user details implementation will be picked up in 2 phases. Following is the phase-wise plan
    
    | Lender | Email  | Phone  | Bank & Mandate |
    | --- | --- | --- | --- |
    | BFL  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
    | TCL  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
    | DSP  | picked-up in v1 | picked-up in v1 | will be picked-up in v2 |
- High level handling of update details
    - BFL
        
        
        | User detail  | Handling |
        | --- | --- |
        | Email  | - collate all the details update requests
        - Mail daily report to BFL [las.crm@bajajfinserv.in](mailto:las.crm@bajajfinserv.in) keeping [shrineel.kakade1@bajajfinserv.in](mailto:shrineel.kakade1@bajajfinserv.in), [yuvraj.simane@bajajfinserv.in](mailto:yuvraj.simane@bajajfinserv.in) in cc 
        - Once updated in BFL & our Ops get an update
        - Our Ops approves the service request through admin action & the details get updated in our DB  |
        | Phone  | - collate all the details update requests
        - Mail daily report to BFL Las CRM
        - Once updated in BFL & our Ops get an update
        - Our Ops approves the service request through admin action & the details get updated in our DB  |
    - TCL
        
        
        | User detail  | Handling |
        | --- | --- |
        | Email  | - use TCL’s updateClientMaster API
        - If we get a success response in the API, we instantly update the email in our system  |
        | Phone  | - use TCL’s updateClientMaster API
        - If we get a success response in the API, we instantly update the email in our system  |
    - DSP
        
        
        | User detail | Handling |
        | --- | --- |
        | Email | - use DSP’s updateEmail API- once we get a success response in the status API, we instantly update the email in our system |
        | Phone | - use DSP’s updateMobile API - once we get a success response in the status API, we instantly update the email in our system |
- DSP & TCL API Level handling
    - DSP
        - update mobile
            - Request
                
                ```jsx
                curl --location 'https://api.staging.dspfin.com/lms/api/loan/servicing/v1/mobile/update' \
                --header 'Content-Type: application/json' \
                --header 'X-SourcingChannelCode;' \
                --header 'X-Signature;' \
                --header 'X-Timestamp;' \
                --data '{
                    "fenixLoanAccountId": "FXLAN94296139",
                    "newMobileNumber": "8285979766"
                }
                '
                ```
                
            - Response
                
                ```jsx
                {
                  "loanServicingRequestId": "LSRID133645215468",
                  "requestType": "UPDATE_MOBILE_NUMBER",
                  "requestSource": "SYSTEM",
                  "status": "PENDING_CHECKER_APPROVAL",
                  "subStatus": null,
                  "remarks": "request is created to update mobile number and waiting for the checker approval"
                }
                ```
                
        - update mobile status
            - Request
                
                ```jsx
                curl --location 'https://api.staging.dspfin.com/lms/api/loan/servicing/v1/mobile/update/status/LSRID133645215468' \
                --header 'Content-Type: application/json' \
                --header 'X-SourcingChannelCode;' \
                --header 'X-Signature;' \
                --header 'X-Timestamp;'
                ```
                
            - Response
                
                ```jsx
                {
                  "loanServicingRequestId": "LSRID133645215468",
                  "requestType": "UPDATE_MOBILE_NUMBER",
                  "requestSource": "SYSTEM",
                  "status": "PENDING_CHECKER_APPROVAL",
                  "subStatus": null,
                  "remarks": "request is created to update mobile number and waiting for the checker approval"
                }
                ```
                
        - update email
            - Request
                
                ```jsx
                curl --location 'https://api.staging.dspfin.com/lms/api/loan/servicing/v1/email/update' \
                --header 'Content-Type: application/json' \
                --header 'X-SourcingChannelCode;' \
                --header 'X-Signature;' \
                --header 'X-Timestamp;' \
                --data '{
                    "fenixLoanAccountId": "000000756",
                    "newEmailAddress": "pankajrana5gm.ailcom"
                }'
                ```
                
            - Response
                
                ```jsx
                {
                  "loanServicingRequestId": "LSRID133645215468",
                  "requestType": "UPDATE_MOBILE_NUMBER",
                  "requestSource": "SYSTEM",
                  "status": "PENDING_CHECKER_APPROVAL",
                  "subStatus": null,
                  "remarks": "request is created to update mobile number and waiting for the checker approval"
                }
                ```
                
        - update email status
            - Request
                
                ```jsx
                curl --location 'https://api.staging.dspfin.com/lms/api/loan/servicing/v1/email/update/status/LSRID285799569437' \
                --header 'Content-Type: application/json' \
                --header 'X-SourcingChannelCode;' \
                --header 'X-Signature;' \
                --header 'X-Timestamp;'
                ```
                
            - Response
                
                ```jsx
                {
                  "loanServicingRequestId": "LSRID285799569437",
                  "requestType": "UPDATE_EMAIL_ADDRESS",
                  "requestSource": "SYSTEM",
                  "status": "PENDING_CHECKER_APPROVAL",
                  "subStatus": null,
                  "remarks": "request is created to update email address and waiting for the checker approval"
                }
                ```
                
        - Status handling
            
            
            | Status  | Handling  | Status in our DB  | Action  |
            | --- | --- | --- | --- |
            | SUCCESS | Consider success | SUCCESS | Update detail in our DB  |
            | FAILURE | Consider failed  | FAILED | Do not update DB |
            | REJECTED  | Consider rejected  | REJECTED | Do not update DB |
            | CREATED, PENDING_CHECKER_APPROVAL, PENDING_LMS_POSTING, PENDING_LOS_POSTING | Consider pending & continue polling the status API for 5 days. polling frequency | PENDING | Do not update DB & keep polling |
    - TCL
        - We will send the push the OTP verification report in the webtop of the user
        - updateClientMaster API
            - UAT url
                
                [https://miles-uat-apicast.apps.tclnprdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate](https://miles-uat-apicast.apps.tclnprdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate)
                
            - Prod curl
                
                ```jsx
                curl --location 'https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate' \
                --header 'ConversationID: f560b237-4d6b-42a6-ba2c-3a64b347adce' \
                --header 'SourceName: VoltMoney' \
                --header 'Authorization: Basic dm9sdG1vbmV5cHJvZDp2b2x0bW9uZXlwcm9k' \
                --header 'Content-Type: application/json' \
                --data-raw '[{
                 "TransactionID": "",
                 "UniqueRecordID": "351111187155",
                 "FirstName": "Ameya",
                 "MiddleName": "",
                 "LastName": "Aglawe",
                 "BOCodeSecurity": "",
                 "FatherOrHusbandName": "Tushar Aglawe",
                 "HeadOfFamily": "No",
                 "BOCodeMF": "",
                 "FamilyID": "1298",
                 "FamilyName": "LAS_DIGITAL",
                 "GroupID": "1210",
                 "GroupName": "LAS_DIGITAL",
                 "CommenceOn": "2024-11-20",
                 "BOCodeDebt": "",
                 "TaxStatusCode": "01",
                 "TaxStatus": "Individual",
                 "TaxPercent": "0",
                 "PoolAccount": "Yes",
                 "UCC": "",
                 "BOCodeNBFC": "",
                 "CategoryCode": "20",
                 "Category": "Individual",
                 "CommonClientCode": "351111187155",
                 "BorrowerIndustryID": "2",
                 "BorrowerIndustryName": "Non face to face customers",
                 "TaxIdOrPAN": "DTBPA5342C",
                 "TAN_No": "",
                 "GIR_No": "",
                 "TaxWaiverInFile": "",
                 "CircleOrWardOrDist": "",
                 "AadharCardNo": "XXXXXXXX0857",
                 "RBIApprovalNo": "",
                 "RBIApprovalDate": "",
                 "TaxDeductionStatus": "",
                 "SEBIRegistrationNo": "",
                 "Address1": "C/O: Tushar Agalawe7-CBhilaiCivic Centre Bhilai",
                 "Address2": "Civic Centre BhilaiDurgDurgShri Shankara School,",
                 "Address3": "ChhattisgarhIndia490006",
                 "City": "Durg",
                 "PinCode": "490006",
                 "StateID": "7",
                 "State": "Chhattisgarh",
                 "CountryID": "91",
                 "Country": "India",
                 "ResTelNo": "",
                 "MobileNo": "9755101807",
                 "Fax": "",
                 "Email": "ameyaaglawe@gmail.com",
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
                 "OffEmail": "",
                 "DefaultMailing": "Home",
                 "DeciderName": "",
                 "DeciderTelNo": "",
                 "DeciderFax": "",
                 "OperationPersonName": "",
                 "OperationPersonTelNo": "",
                 "OperationPersonFax": "",
                 "Designation": "",
                 "OtherAddress1": "",
                 "OtherAddress2": "",
                 "OtherAddress3": "",
                 "OtherCity": "",
                 "OtherPinCode": "",
                 "LoanRequests": "Investments In Securities",
                 "DOB": "18-Jun-2002",
                 "GuardianName": "",
                 "PlaceOfBirth": "",
                 "Salutation": "",
                 "Gender": "Male",
                 "MaritalStatus": "unMarried",
                 "SpouseName": "",
                 "WeddingDate": "",
                 "SpouseDOB": "",
                 "OccupationCode": "7",
                 "ProfessionalCode": "",
                 "SalariedCode": "",
                 "OtherOccupation": "",
                 "OccupationType": "",
                 "GrossAnnualIncome_InLakhs": "",
                 "EstFinancialWealth_InLakhs": "",
                 "NameOfEmployer": "",
                 "YearsOfEmploymentOrBusiness": "",
                 "EducationalQualification": "",
                 "PersonalAddress1": "",
                 "PersonalAddress2": "",
                 "PersonalAddress3": "",
                 "Nationality": "Indian Citizen",
                 "NationalityIfOther": "",
                 "NatureOfBusiness": "",
                 "VoterID": "",
                 "PassportNo": "",
                 "PlaceOfIssue": "",
                 "PassportIssueDate": "",
                 "PassportExpiryDate": "",
                 "InterCompany": "",
                 "Jurisdiction": "",
                 "DateOfIncoporation": "",
                 "DateOfCommencement": "",
                 "CorporateNatureOfBusiness": "",
                 "LegalConstitutionID": "",
                 "LegalConstitution": "",
                 "RegisteredOfficeDUNSNumber": "",
                 "BorrowerDUNSNumber": "",
                 "EstFinancialWealth_InMillion": "",
                 "CorporateGrossAnnualIncome_InLakhs": "",
                 "FGIInterCompanyCode": "",
                 "Email_YesNo": "",
                 "Fax_YesNo": "",
                 "Mail_YesNo": "",
                 "Hand_YesNo": "",
                 "AlertEmail_YesNo": "",
                 "AlertFax_YesNo": "",
                 "AlertSMS_YesNo": "",
                 "EmailOnDeactivationofAccount": "",
                 "EmailOnCorporateAction": "",
                 "PromotionalMaterial": "",
                 "EmailOnCloseOfAccount": "",
                 "EmailOnFreezeOfAccount": "",
                 "SharePhoneOrEmail": "",
                 "Statement": "",
                 "ChangeInClientInformation": "",
                 "InternetID": "",
                 "ClientBankDetailsUpdate": [
                  {
                   "Action": "",
                   "BankId": "0",
                   "BankName": "State Bank of India",
                   "BankBranch": "RISALI BHILAI",
                   "MICR": "490002020",
                   "IFSC": "SBIN0012328",
                   "AccountNo": "35088812977",
                   "FirstHolderName": "Ameya Aglawe",
                   "SecondHolderName": "",
                   "ThirdHolderName": "",
                   "AcctOpeningDt": "12-09-2018",
                   "DefaultAccount": "Yes",
                   "Accounttype": "Savings",
                   "BankDtl_CCY": "INR",
                   "PaymentMode": "Account/Fund Transfer",
                   "PaymentCode": "I",
                   "LocationCode": ""
                  }
                 ],
                 "ClientBrokerDetailsUpdate": [
                 ],
                 "ClientDPDetailsUpdate": [
                 ],
                 "ClientKeyManagementPersonnelUpdate": [
                 ],
                 "ClientCreditFacilityUpdate": [
                 ],
                 "ClientCreditCardUpdate": [
                 ],
                 "ClientRelatedCompaniesUpdate": [
                 ],
                 "ClientIntroducerUpdate": [
                  {
                   "ExistingClient": "",
                   "IntroducerName": "",
                   "AddressOfIntroducer1": "",
                   "AddressOfIntroducer2": "",
                   "AddressOfIntroducer3": "",
                   "MappinID": "",
                   "IntroducerClientCode": "",
                   "NameOfEmployeeInterviewed": "",
                   "DesginationOfEmployeeInterviewed": ""
                  }
                 ],
                 "ClientBranchDetailsUpdate": [
                  {
                   "Action": "",
                   "BranchCode": "386",
                   "BranchName": "DELHI RAJENDRA PLACE",
                   "LocationID": "02",
                   "LocationName": "New Delhi",
                   "RegionName": "",
                   "WefDate": "20-Nov-2024"
                  }
                 ],
                 "ClientSubBrokerDetailsUpdate": [
                  {
                   "Action": "",
                   "SubBrokerID": "103",
                   "SubBrokerName": "SALTER TECHNOLOGIES PRIVATE LIMITED",
                   "WefDate": "20-Nov-2024"
                  }
                 ],
                 "ClientPrimaryRMUpdate": [
                  {
                   "Action": "",
                   "ManagerCode": "34",
                   "ManagerName": "Sagar Chheda",
                   "ManagerEmailID": "Sagar.Chheda@tatacapital.com",
                   "ManagerMobileNo.": "7208111020",
                   "WefDate": "20-Nov-2024"
                  }
                 ],
                 "ClientSecondaryRMUpdate": [
                 ],
                 "ClientGSTDetailsUpdate": [
                  {
                   "Action": "",
                   "StateCode": "7",
                   "State": "Chhattisgarh",
                   "GSTIN": "",
                   "DefaultLocation": "yes",
                   "IsGSTExempted": "no",
                   "GSTExemptionDesc": "",
                   "IsRelatedParty": "no",
                   "RelatedPartyDesc": ""
                  }
                 ],
                 "OtherDetails": [
                  {
                   "Employee": "",
                   "Employee Code": "",
                   "Remarks 1": "",
                   "Remarks 2": ""
                  }
                 ]
                }]'
                ```
                
            - Request
                
                ```jsx
                curl --location 'https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate' \
                --header 'ConversationID: f560b237-4d6b-42a6-ba2c-3a64b347adce' \
                --header 'SourceName: VoltMoney' \
                --header 'Authorization: Basic dm9sdG1vbmV5cHJvZDp2b2x0bW9uZXlwcm9k' \
                --header 'Content-Type: application/json' \
                --data-raw '[{
                  "TransactionID": "",
                  "UniqueRecordID": "351111187155",
                  "FirstName": "Ameya",
                  "MiddleName": "",
                  "LastName": "Aglawe",
                  "BOCodeSecurity": "",
                  "FatherOrHusbandName": "Tushar Aglawe",
                  "HeadOfFamily": "No",
                  "BOCodeMF": "",
                  "FamilyID": "1298",
                  "FamilyName": "LAS_DIGITAL",
                  "GroupID": "1210",
                  "GroupName": "LAS_DIGITAL",
                  "CommenceOn": "2024-11-20",
                  "BOCodeDebt": "",
                  "TaxStatusCode": "01",
                  "TaxStatus": "Individual",
                  "TaxPercent": "0",
                  "PoolAccount": "Yes",
                  "UCC": "",
                  "BOCodeNBFC": "",
                  "CategoryCode": "1",
                  "Category": "Individual",
                  "CommonClientCode": "351111187155",
                  "BorrowerIndustryID": "2",
                  "BorrowerIndustryName": "Non face to face customers",
                  "TaxIdOrPAN": "DTBPA5342C",
                  "TAN_No": "",
                  "GIR_No": "",
                  "TaxWaiverInFile": "",
                  "CircleOrWardOrDist": "",
                  "AadharCardNo": "XXXXXXXX0857",
                  "RBIApprovalNo": "",
                  "RBIApprovalDate": "",
                  "TaxDeductionStatus": "",
                  "SEBIRegistrationNo": "",
                  "Address1": "C/O: Tushar Agalawe7-CBhilaiCivic Centre Bhilai",
                  "Address2": "Civic Centre BhilaiDurgDurgShri Shankara School,",
                  "Address3": "ChhattisgarhIndia490006",
                  "City": "Durg",
                  "PinCode": "490006",
                  "StateID": "7",
                  "State": "Chhattisgarh",
                  "CountryID": "91",
                  "Country": "India",
                  "ResTelNo": "",
                  "MobileNo": "9755101805",
                  "Fax": "",
                  "Email": "ameyaaglawe@gmail.com",
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
                  "OffEmail": "",
                  "DefaultMailing": "Home",
                  "DeciderName": "",
                  "DeciderTelNo": "",
                  "DeciderFax": "",
                  "OperationPersonName": "",
                  "OperationPersonTelNo": "",
                  "OperationPersonFax": "",
                  "Designation": "",
                  "OtherAddress1": "",
                  "OtherAddress2": "",
                  "OtherAddress3": "",
                  "OtherCity": "",
                  "OtherPinCode": "",
                  "LoanRequests": "Investments In Securities",
                  "DOB": "18-Jun-2002",
                  "GuardianName": "",
                  "PlaceOfBirth": "",
                  "Salutation": "",
                  "Gender": "Male",
                  "MaritalStatus": "unMarried",
                  "SpouseName": "",
                  "WeddingDate": "",
                  "SpouseDOB": "",
                  "OccupationCode": "7",
                  "ProfessionalCode": "",
                  "SalariedCode": "",
                  "OtherOccupation": "",
                  "OccupationType": "",
                  "GrossAnnualIncome_InLakhs": "",
                  "EstFinancialWealth_InLakhs": "",
                  "NameOfEmployer": "",
                  "YearsOfEmploymentOrBusiness": "",
                  "EducationalQualification": "",
                  "PersonalAddress1": "",
                  "PersonalAddress2": "",
                  "PersonalAddress3": "",
                  "Nationality": "Indian Citizen",
                  "NationalityIfOther": "",
                  "NatureOfBusiness": "",
                  "VoterID": "",
                  "PassportNo": "",
                  "PlaceOfIssue": "",
                  "PassportIssueDate": "",
                  "PassportExpiryDate": "",
                  "InterCompany": "",
                  "Jurisdiction": "",
                  "DateOfIncoporation": "",
                  "DateOfCommencement": "",
                  "CorporateNatureOfBusiness": "",
                  "LegalConstitutionID": "",
                  "LegalConstitution": "",
                  "RegisteredOfficeDUNSNumber": "",
                  "BorrowerDUNSNumber": "",
                  "EstFinancialWealth_InMillion": "",
                  "CorporateGrossAnnualIncome_InLakhs": "",
                  "FGIInterCompanyCode": "",
                  "Email_YesNo": "",
                  "Fax_YesNo": "",
                  "Mail_YesNo": "",
                  "Hand_YesNo": "",
                  "AlertEmail_YesNo": "",
                  "AlertFax_YesNo": "",
                  "AlertSMS_YesNo": "",
                  "EmailOnDeactivationofAccount": "",
                  "EmailOnCorporateAction": "",
                  "PromotionalMaterial": "",
                  "EmailOnCloseOfAccount": "",
                  "EmailOnFreezeOfAccount": "",
                  "SharePhoneOrEmail": "",
                  "Statement": "",
                  "ChangeInClientInformation": "",
                  "InternetID": "",
                  "ClientBankDetailsUpdate": [
                    {
                      "Action": "",
                      "BankId": "0",
                      "BankName": "State Bank of India",
                      "BankBranch": "RISALI BHILAI",
                      "MICR": "490002020",
                      "IFSC": "SBIN0012328",
                      "AccountNo": "35088812977",
                      "FirstHolderName": "Ameya Aglawe",
                      "SecondHolderName": "",
                      "ThirdHolderName": "",
                      "AcctOpeningDt": "12-09-2018",
                      "DefaultAccount": "Yes",
                      "Accounttype": "Savings",
                      "BankDtl_CCY": "INR",
                      "PaymentMode": "Account/Fund Transfer",
                      "PaymentCode": "I",
                      "LocationCode": ""
                    }
                  ],
                  "ClientBrokerDetailsUpdate": [
                  ],
                  "ClientDPDetailsUpdate": [
                  ],
                  "ClientKeyManagementPersonnelUpdate": [
                  ],
                  "ClientCreditFacilityUpdate": [
                  ],
                  "ClientCreditCardUpdate": [
                  ],
                  "ClientRelatedCompaniesUpdate": [
                  ],
                  "ClientIntroducerUpdate": [
                    {
                      "ExistingClient": "",
                      "IntroducerName": "",
                      "AddressOfIntroducer1": "",
                      "AddressOfIntroducer2": "",
                      "AddressOfIntroducer3": "",
                      "MappinID": "",
                      "IntroducerClientCode": "",
                      "NameOfEmployeeInterviewed": "",
                      "DesginationOfEmployeeInterviewed": ""
                    }
                  ],
                  "ClientBranchDetailsUpdate": [
                    {
                      "Action": "",
                      "BranchCode": "386",
                      "BranchName": "DELHI RAJENDRA PLACE",
                      "LocationID": "02",
                      "LocationName": "New Delhi",
                      "RegionName": "",
                      "WefDate": "20-Nov-2024"
                    }
                  ],
                  "ClientSubBrokerDetailsUpdate": [
                    {
                      "Action": "",
                      "SubBrokerID": "103",
                      "SubBrokerName": "SALTER TECHNOLOGIES PRIVATE LIMITED",
                      "WefDate": "20-Nov-2024"
                    }
                  ],
                  "ClientPrimaryRMUpdate": [
                    {
                      "Action": "",
                      "ManagerCode": "34",
                      "ManagerName": "Sagar Chheda",
                      "ManagerEmailID": "Sagar.Chheda@tatacapital.com",
                      "ManagerMobileNo.": "7208111020",
                      "WefDate": "20-Nov-2024"
                    }
                  ],
                  "ClientSecondaryRMUpdate": [
                  ],
                  "ClientGSTDetailsUpdate": [
                    {
                      "Action": "",
                      "StateCode": "7",
                      "State": "Chhattisgarh",
                      "GSTIN": "",
                      "DefaultLocation": "yes",
                      "IsGSTExempted": "no",
                      "GSTExemptionDesc": "",
                      "IsRelatedParty": "no",
                      "RelatedPartyDesc": ""
                    }
                  ],
                  "OtherDetails": [
                    {
                      "Employee": "",
                      "Employee Code": "",
                      "Remarks 1": "",
                      "Remarks 2": ""
                    }
                  ]
                }]'
                ```
                
            - Response
                
                ```jsx
                {
                  "retStatus": "SUCCESS",
                  "response": {
                    "ClientMasterUpdateData": [
                      {
                        "RecordStatusCode": "0",
                        "UniqueRecordID": "351111187155",
                        "Remarks": "Success"
                      }
                    ],
                    "status": {
                      "Status": "Success",
                      "Remarks": "",
                      "Code": "01"
                    }
                  },
                  "sysErrorMessage": "",
                  "errorMessage": "",
                  "sysErrorCode": ""
                }
                ```
                
        - Status handling
            
            
            | API response | Handling | Status in our DB  | Action  |
            | --- | --- | --- | --- |
            | "RecordStatusCode": "0" | Consider success | SUCCESS | Update detail in our DB  |
            | Anything other than "RecordStatusCode": "0" | Consider exception  | FAILED | Do not update DB |
        - Once we receive a "RecordStatusCode": "0" from the updateClientMaster API we will push the email ID/mobile verification report to the webtop of the user
            - [email ID report](https://docs.google.com/spreadsheets/d/1KDeQYUSJ31JVpA2TWQmCmLHmSoV7iT05/edit?usp=sharing&ouid=113204369488543186528&rtpof=true&sd=true)
            - [Mobile number report](https://docs.google.com/spreadsheets/d/1sh9XLrHa0dP1m8PROhI2GMjDTnyJD_JH/edit?usp=sharing&ouid=113204369488543186528&rtpof=true&sd=true)
- BFL Process handling
    - There can be 2 approaches here
        - **Approach 1 : More tech effort, less Ops effort [Prioritised]**
            1. User’s request update phone/email through app
            2. We create a service request in our system 
            3. We collate all the service requests and send an EOD sheet to Las CRM, keeping all the stakeholders in cc
            4. BFL team notifies our Ops when details are updated in BFL system
            5. Volt Ops uses a new admin action (Approve/Reject service requests)
                1. Ops enters requestID
                2. Ops approves the service request
        - Approach 2 : Less tech effort, more Ops effort [de-prioritised]
            1. User’s request update phone/email through app
            2. We collate and send a EOD sheet to Las CRM, keeping all the stakeholders in cc
            3. BFL team notifies our Ops when details are updated in BFL system
            4. Our Ops team updates those details using admin action 
    
- Service request status handling
    - Any service request will have the following status
    
    | Status  | Created when  |
    | --- | --- |
    | QUEUED | - When service request received from the user  |
    | REQUESTED | - TCL, DSP : When lender APIs hit for the service request 
    - BFL : When the sheet is sent to Ops  |
    | SUCCESS | - TCL, DSP : When we receive success in API response from the lender 
    - BFL : When Ops approves the service request through admin action  |
    | FAILED | - TCL, DSP : Based on API response 
     |
    | REJECTED | - DSP : Based on API response 
    - BFL : Ops rejects the service request |
- Validations (across DSP, BFL, TCL)
    
    
    | New detail  | Validation  | Handling  |
    | --- | --- | --- |
    | Phone number  | - Check if the phone number is already present in our system for any account  | - If present : Throw an error message in UI 
    - If not present allow user to enter OTP |
    | Email  | - Check if the email is already present in our system for any account | - If present : Throw an error message in UI 
    - If not present allow user to enter OTP |
- BFL Report
    - Header
        - BFL Detail Update - {{date}}
        - Eg : BFL Details Update - 19 Nov 2024
    - Body
        
        <aside>
        💡
        
        Hi Team,
        
        Please find the list of customers who want to update their details as on {{date}}
        
        For any query or feedback, mail us at : {{contactEmail}}
        
        Thank you, 
        Team Volt Money 
        
        </aside>
        
    - SendGrid Body
        
        ```jsx
            <table>
            <tr>
            <td style="font-family: sans-serif; font-size:15px;">
            <p>Hi Team,</p>
            <p>Please find the list of customers who want to update their details as on <b>{{date}}</b>.
        
            <br>
            </td>
            </tr>
            <tr>
                <td align="left" style="font-family: sans-serif; font-size:14px; color:#000000; line-height:1.5;" valign="middle"><table>
                    <tr>
                        <td width="500" style="border-top: solid 1px #e4e4e4;">&nbsp;</td>
                    </tr>
                </table></td>
            </tr>
            <tr>
                
            </tr>
           <tr>
              <td align="left"><table width="100%" class="wFull">
                  <tr>
                  <td align="left" style="font-family: sans-serif; font-size:14px; color: grey; line-height:1.5;" valign="middle"><b>For any query or feedback, mail us at: <a href="mailto:{{contactEmail}}" target="_blank">{{contactEmail}}</a></b></td>
                    
                  
                  </tr>
                  <tr>
            <td>
            <p>Thank you,</p>
            <p>Team Voltmoney</p>.
            </td>
            </tr>
        ```
        
    - SendGrid variables
        - {{date}}
        - {{contactEmail}}
    - Template ID
        - Template ID : d-984f24c337074990b4f189280b456946
    - Report file
        
        
        | request_ID | lender_loan_account_number | customer_pan | customer_name | request_type | current_value | new_value | customer_request_timestamp | Verification mode | Verification IP address | status | comments |
        | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- | --- |
        |  | lender_credit_id  |  |  | email ID update/ mobile number update | including +91 |  |  | Mobile number OTP Verification/email ID OTP verification   | XXXXX.XXX |  |  |
    - We will send the report at 8:00AM everyday and send all the pending cases to BFL (no date-wise filter)
- Admin action (Service request)
    - Admin action name : Approve user service request
    - Flow -
        - Step 1: Volt Ops enters request_ID in the admin action
        - Step 2: Taps on enter
        - Step 3: Service request details opens up
            - Details
                - borrower_account_id
                - lender_loan_account number
                - customer_pan
                - customer_name
                - request_type
                - current_value
                - new_value
        - Step 4 : Taps on the CTA to APPROVE/REJECT
- Staging API
    - TCL
        
        Same curl as prod API & auth of other TCLs UAT APIs
        
    - DSP
        
         [https://documenter.getpostman.com/view/37292788/2sAY52cKZe#95911bd9-b704-4bd3-9c13-95ab8c5a2827](https://documenter.getpostman.com/view/37292788/2sAY52cKZe#95911bd9-b704-4bd3-9c13-95ab8c5a2827)
        
- Prod API
    - TCL
        
        ```jsx
        curl --location 'https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/clientMasterUpdate' \
        --header 'ConversationID: f560b237-4d6b-42a6-ba2c-3a64b347adce' \
        --header 'SourceName: VoltMoney' \
        --header 'Authorization: Basic dm9sdG1vbmV5cHJvZDp2b2x0bW9uZXlwcm9k' \
        --header 'Content-Type: application/json' \
        --data-raw '[{
          "TransactionID": "",
          "UniqueRecordID": "351111187155",
          "FirstName": "Ameya",
          "MiddleName": "",
          "LastName": "Aglawe",
          "BOCodeSecurity": "",
          "FatherOrHusbandName": "Tushar Aglawe",
          "HeadOfFamily": "No",
          "BOCodeMF": "",
          "FamilyID": "1298",
          "FamilyName": "LAS_DIGITAL",
          "GroupID": "1210",
          "GroupName": "LAS_DIGITAL",
          "CommenceOn": "2024-11-20",
          "BOCodeDebt": "",
          "TaxStatusCode": "01",
          "TaxStatus": "Individual",
          "TaxPercent": "0",
          "PoolAccount": "Yes",
          "UCC": "",
          "BOCodeNBFC": "",
          "CategoryCode": "20",
          "Category": "Platinum",
          "CommonClientCode": "351111187155",
          "BorrowerIndustryID": "2",
          "BorrowerIndustryName": "Non face to face customers",
          "TaxIdOrPAN": "DTBPA5342C",
          "TAN_No": "",
          "GIR_No": "",
          "TaxWaiverInFile": "",
          "CircleOrWardOrDist": "",
          "AadharCardNo": "XXXXXXXX0857",
          "RBIApprovalNo": "",
          "RBIApprovalDate": "",
          "TaxDeductionStatus": "",
          "SEBIRegistrationNo": "",
          "Address1": "C/O: Tushar Agalawe7-CBhilaiCivic Centre Bhilai",
          "Address2": "Civic Centre BhilaiDurgDurgShri Shankara School,",
          "Address3": "ChhattisgarhIndia490006",
          "City": "Durg",
          "PinCode": "490006",
          "StateID": "7",
          "State": "Chhattisgarh",
          "CountryID": "91",
          "Country": "India",
          "ResTelNo": "",
          "MobileNo": "9755101805",
          "Fax": "",
          "Email": "ameyaaglawe@gmail.com",
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
          "OffEmail": "",
          "DefaultMailing": "Home",
          "DeciderName": "",
          "DeciderTelNo": "",
          "DeciderFax": "",
          "OperationPersonName": "",
          "OperationPersonTelNo": "",
          "OperationPersonFax": "",
          "Designation": "",
          "OtherAddress1": "",
          "OtherAddress2": "",
          "OtherAddress3": "",
          "OtherCity": "",
          "OtherPinCode": "",
          "LoanRequests": "Investments In Securities",
          "DOB": "18-Jun-2002",
          "GuardianName": "",
          "PlaceOfBirth": "",
          "Salutation": "",
          "Gender": "Male",
          "MaritalStatus": "unMarried",
          "SpouseName": "",
          "WeddingDate": "",
          "SpouseDOB": "",
          "OccupationCode": "7",
          "ProfessionalCode": "",
          "SalariedCode": "",
          "OtherOccupation": "",
          "OccupationType": "",
          "GrossAnnualIncome_InLakhs": "",
          "EstFinancialWealth_InLakhs": "",
          "NameOfEmployer": "",
          "YearsOfEmploymentOrBusiness": "",
          "EducationalQualification": "",
          "PersonalAddress1": "",
          "PersonalAddress2": "",
          "PersonalAddress3": "",
          "Nationality": "Indian Citizen",
          "NationalityIfOther": "",
          "NatureOfBusiness": "",
          "VoterID": "",
          "PassportNo": "",
          "PlaceOfIssue": "",
          "PassportIssueDate": "",
          "PassportExpiryDate": "",
          "InterCompany": "",
          "Jurisdiction": "",
          "DateOfIncoporation": "",
          "DateOfCommencement": "",
          "CorporateNatureOfBusiness": "",
          "LegalConstitutionID": "",
          "LegalConstitution": "",
          "RegisteredOfficeDUNSNumber": "",
          "BorrowerDUNSNumber": "",
          "EstFinancialWealth_InMillion": "",
          "CorporateGrossAnnualIncome_InLakhs": "",
          "FGIInterCompanyCode": "",
          "Email_YesNo": "",
          "Fax_YesNo": "",
          "Mail_YesNo": "",
          "Hand_YesNo": "",
          "AlertEmail_YesNo": "",
          "AlertFax_YesNo": "",
          "AlertSMS_YesNo": "",
          "EmailOnDeactivationofAccount": "",
          "EmailOnCorporateAction": "",
          "PromotionalMaterial": "",
          "EmailOnCloseOfAccount": "",
          "EmailOnFreezeOfAccount": "",
          "SharePhoneOrEmail": "",
          "Statement": "",
          "ChangeInClientInformation": "",
          "InternetID": "",
          "ClientBankDetailsUpdate": [
            {
              "Action": "",
              "BankId": "0",
              "BankName": "State Bank of India",
              "BankBranch": "RISALI BHILAI",
              "MICR": "490002020",
              "IFSC": "SBIN0012328",
              "AccountNo": "35088812977",
              "FirstHolderName": "Ameya Aglawe",
              "SecondHolderName": "",
              "ThirdHolderName": "",
              "AcctOpeningDt": "12-09-2018",
              "DefaultAccount": "Yes",
              "Accounttype": "Savings",
              "BankDtl_CCY": "INR",
              "PaymentMode": "Account/Fund Transfer",
              "PaymentCode": "I",
              "LocationCode": ""
            }
          ],
          "ClientBrokerDetailsUpdate": [
          ],
          "ClientDPDetailsUpdate": [
          ],
          "ClientKeyManagementPersonnelUpdate": [
          ],
          "ClientCreditFacilityUpdate": [
          ],
          "ClientCreditCardUpdate": [
          ],
          "ClientRelatedCompaniesUpdate": [
          ],
          "ClientIntroducerUpdate": [
            {
              "ExistingClient": "",
              "IntroducerName": "",
              "AddressOfIntroducer1": "",
              "AddressOfIntroducer2": "",
              "AddressOfIntroducer3": "",
              "MappinID": "",
              "IntroducerClientCode": "",
              "NameOfEmployeeInterviewed": "",
              "DesginationOfEmployeeInterviewed": ""
            }
          ],
          "ClientBranchDetailsUpdate": [
            {
              "Action": "",
              "BranchCode": "386",
              "BranchName": "DELHI RAJENDRA PLACE",
              "LocationID": "02",
              "LocationName": "New Delhi",
              "RegionName": "",
              "WefDate": "20-Nov-2024"
            }
          ],
          "ClientSubBrokerDetailsUpdate": [
            {
              "Action": "",
              "SubBrokerID": "103",
              "SubBrokerName": "SALTER TECHNOLOGIES PRIVATE LIMITED",
              "WefDate": "20-Nov-2024"
            }
          ],
          "ClientPrimaryRMUpdate": [
            {
              "Action": "",
              "ManagerCode": "34",
              "ManagerName": "Sagar Chheda",
              "ManagerEmailID": "Sagar.Chheda@tatacapital.com",
              "ManagerMobileNo.": "7208111020",
              "WefDate": "20-Nov-2024"
            }
          ],
          "ClientSecondaryRMUpdate": [
          ],
          "ClientGSTDetailsUpdate": [
            {
              "Action": "",
              "StateCode": "7",
              "State": "Chhattisgarh",
              "GSTIN": "",
              "DefaultLocation": "yes",
              "IsGSTExempted": "no",
              "GSTExemptionDesc": "",
              "IsRelatedParty": "no",
              "RelatedPartyDesc": ""
            }
          ],
          "OtherDetails": [
            {
              "Employee": "",
              "Employee Code": "",
              "Remarks 1": "",
              "Remarks 2": ""
            }
          ]
        }]'
        
        Response - 
        
        {
          "retStatus": "SUCCESS",
          "response": {
            "ClientMasterUpdateData": [
              {
                "RecordStatusCode": "0",
                "UniqueRecordID": "351111187155",
                "Remarks": "Success"
              }
            ],
            "status": {
              "Status": "Success",
              "Remarks": "",
              "Code": "01"
            }
          },
          "sysErrorMessage": "",
          "errorMessage": "",
          "sysErrorCode": ""
        }
        ```
        
    - DSP
        - Update Mobile
            
            ```jsx
            curl --location 'http://FenixLMSOrchestrationALB-1608474405.ap-south-1.elb.amazonaws.com/lms/api/loan/servicing/v1/mobile/update' \
            --header 'X-RequestSource: SYSTEM' \
            --header 'X-SourcingChannelCode: 8a81220f90be712c0190be75a3850001' \
            --header 'Content-Type: application/json' \
            --data '{
                "fenixLoanAccountId": "FXLAN79468492",
                "newMobileNumber": "7878787878"
            }
            '
            ```
            
        - Update Email
            
            ```jsx
            curl --location 'http://FenixLMSOrchestrationALB-1608474405.ap-south-1.elb.amazonaws.com/lms/api/loan/servicing/v1/email/update' \
            --header 'X-RequestSource: SYSTEM' \
            --header 'Content-Type: application/json' \
            --data-raw '{
                "fenixLoanAccountId": "FXLAN72383474",
                "newEmailAddress": "trapti.singh.checker@voltmoney.in"
            }'
            ```
            
- CRM requirements
    - When we are updating the email/phone in our DB, then we update the same in LSQ
    
    | Lender  | Trigger | Action  |
    | --- | --- | --- |
    | BFL  | Volt Ops approves the service request | Update in DB & LSQ |
    | TCL  | We get "RecordStatusCode": "0" in API response  | Update in DB & LSQ |
    | DSP  | We get SUCCESS in API response  | Update in DB & LSQ  |
- Notification system for email/phone update
    - Whenever user updates email/phone, a comm will be sent to the user on old email & old phone informing that their phone/email is updated (Whatsapp)
    - Please find the comms PRD [here](https://docs.google.com/document/d/1tnXzQtT-E_IhQZ02-1AoaohV_y1njOzVVdGfASWrSn0/edit?usp=sharing).
    - OTP comms template
        - Email ID
            - Medium used to sent comms
                - Email (sendgrid)
            - Subject
                
                 OTP for email ID update verification
                
            - Body
                
                <aside>
                💡
                
                Dear customer,
                
                Here is your OTP to verify email id with Volt Money:
                
                **222222**
                
                Please refrain from sharing it with anyone. The OTP is valid for 10 minutes.
                
                Regards,
                Team Volt Money 
                
                </aside>
                
            - SendGrid template ID
            - SendGrid template
        - Phone
            - Medium used to sent comms
                - SMS (Vilpower)
            - Body
                
                <aside>
                💡
                
                {#var#} is the OTP to update registered mobile number. It is valid for 15 minutes.
                
                VOLT
                
                </aside>
                
    - Update requested
        - Email ID
            - Medium used to sent comms
                - Email (sendgrid)
            - Subject
                
                 OTP for email ID update verification
                
            - Body
                
                <aside>
                💡
                
                Dear customer,
                
                Here is your OTP to verify email id with Volt Money:
                
                **222222**
                
                Please refrain from sharing it with anyone. The OTP is valid for 10 minutes.
                
                Regards,
                Team Volt Money 
                
                </aside>
                
        - Phone
            
            
    - Update request successful
        - Email ID
            - Medium used to sent comms
                - Email (sendgrid)
                - Whatsapp
            - Subject
                
                Your Volt account email ID was updated 
                
            - Body
                
                <aside>
                💡
                
                Hi Parvesh,
                
                Your email ID is updated to a***********we@gmail.com on our platform. If you didn’t make this change, contact support team at [support@voltmoney.in](mailto:support@voltmoney.in) 
                
                Regards,
                Team Volt Money 
                
                </aside>
                
            - SendGrid template ID
                
                d-1956d88d62d84c69aa0ed17ea4cf19ce
                
            - SendGrid template
                
                ```jsx
                    <tr>
                        <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 30px 20px 20px 20px;" valign="middle">
                            Dear {{customer_name}},
                            <br>
                            <br>
                            Your mobile number is updated to {{mobile_number}}. If you didn’t make this change, please call or whatsapp our support team at 07949106901.
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 20px 20px 20px 20px" valign="middle">Regards,<br>
                            Volt Team
                        </td>
                    </tr>
                    <tr>
                ```
                
        - Phone
            - Medium used to sent comms
                - Email (sendgrid)
                - Whatsapp
            - Subject
                
                Your Volt account mobile number was updated 
                
            - Body
                
                <aside>
                💡
                
                Hi Parvesh,
                
                Your mobile number is updated to **********2106 on our platform. If you didn’t make this change, contact support team at [support@voltmoney.in](mailto:support@voltmoney.in) 
                
                Regards,
                Team Volt Money 
                
                </aside>
                
            - SendGrid template ID
                
                d-82bff1e77ffe42acaa42bc44a3a6620b
                
            - SendGrid template
                
                ```jsx
                Dear {{customername}},
                            <br>
                            <br>
                            Your email ID is updated to {{customer_email}}. If you didn’t make this change, please call or whatsapp our support team at 07949106901.
                        </td>
                    </tr>
                    <tr>
                        <td align="left" style="font-family: sans-serif; font-size:16px; color:#000000; line-height:1.5;padding: 20px 20px 20px 20px" valign="middle">Regards,<br>
                            Volt Team
                        </td>
                ```
                
    - Update request failed
        - Email
        - Phone
- User updates the mobile number & enhances, what happens while fetching?
    - By default, we’ll fetch using the updated phone number
    - User can edit the phone number if they want while fetching
    
    ![Screenshot 2024-12-05 at 7.59.27 PM.png](Update%20user%20details%20(for%20TCL,%20BFL,%20DSP)/Screenshot_2024-12-05_at_7.59.27_PM.png)
    
- Flags
    - Lender wise & detail wise flag to be created
- Logs
    
    
    | Admin tool  | Log  |
    | --- | --- |
    | Update Mobile  | - Update Mobile  admin tool used to update XYXY to XXYY for application_id APAPAP |
    | Update email   | - Update email admin tool used to update XYXY to XXYY for application_id APAPAP |
    | Update service request  | - Update service request admin tool used to update XYXY to XXYY for application_id APAPAP |

**Note** - 

1. Since we don’t store the sessions, hence we won’t be able to log the user out when they update their mobile number.
2. We will not accept any update request from the user if one update request is already in progress. (handled in UI) 
3. **We will only consider update request if the credit status is APPROVED_NOT_DISBURSED, ACTIVE.** 
4. We will store the IP address of each email ID/mobile number update 

## Requirements overview (optional)

### User stories / User flow

1. User taps on the “user profile” icon the home screen on the app. 
2. Goes to the Account details section 
3. Taps on the pencil icon for updating the detail
4. Modal opens up for updating the details 
5. User taps on “Confirm Details” CTA
6. “Enter OTP” modal opens up 
7. User enters OTP & we open up a modal 
    1. For TCL - email & phone 
        1. Success
        2. Failed, Please try again 

Edge cases (UI handling to be done) - 

1. User enters same details while updating - throw an error that it is the same detail 
2. User enters in-correct OTP - throw an error that OTP is wrong 

# **Design**

---

https://www.figma.com/design/P6LkjMfxq3UFY2l3JHOIUW/Profile-section?node-id=578-84&node-type=canvas&t=DneyW5nmbtQSX48o-11

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

**Update details process**

- User raised a request
    - **TCL & BFL**
        - Send daily MIS
        - BFL/TCL Ops updates there status in the sheet
        - Our Ops checks and manually approves/rejects the update detail request manually
            - Approve → Detail updated in the system
            - Reject → Detail not updated in the system
    - **DSP (should DSP have the same MIS type handling as TCL/BFL)**
        - Maker checker
        - Approval/Rejection → DB updated
        - Should we send

- API Endpoint: POST [http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate](http://api-in21.leadsquared.com/v2/LeadManagement.svc/Lead.CreateOrUpdate)
- Request
    
    ```jsx
    {
      "LeadDetails": [
    	  {"Attribute": "EmailAddress", "Value": "[CUSTOMER_UPDATED_EMAILID]"},
        {"Attribute": "Phone", "Value": "[CUSTOMER_UPDATED_PHONE]"},
        {"Attribute": "SearchBy", "Value": "Phone"}
      ]
    }
    ```
    
- Response

- Session storing & expiring
- In app feedback in case of mobile/email update
- **What happens in a new mobile number update is in progress & meanwhile they create a new application with the phone number**
- Take compliance sign-off from TCL, BFL
- **MFD journey - Ranjan**
- Staging API for TCL