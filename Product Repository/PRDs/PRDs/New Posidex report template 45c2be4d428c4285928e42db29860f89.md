# New Posidex report template

: Ayush Kumar
Created time: November 6, 2024 2:22 PM
Status: In progress
Last edited: November 20, 2024 4:54 PM

# **What problem are we solving?**

We are failing to pass required field values to TATA's  Posidex report template, causing Posidex report rejections and user blocks, which needs to be fixed by implementing the new template format with all mandatory fields.

---

# **How do we measure success?**

Reduction in Posidex report rejections (%)

Increase in successful loan application processing rate

---

# **How are others solving this problem?**

---

# **What is the solution?**

Implementing the new template format sent by TATA with all mandatory fields mapped from the Backend.

## User stories / User flow

## Requirements

- I have attached the Posidex report(doc format) with all the variables(key and values) mapped from the BE below:
    
    [https://docs.google.com/document/d/1jC3T6GF8AYaNlfAyfUNYzIQ2C_jug7qoZninJmXsmLM/edit?tab=t.0](https://docs.google.com/document/d/1mDeTYqDohKkSWkJ9UPCRNFR2xABAGiYPiWacsBkz3_c/edit?tab=t.0)
    
- The doc format has to be **converted into the pdf format** and uploaded to the webtop after the **KYC step (CIBIL step)**
- We are **mapping the values to the key** present in the report with the values from from the **CreateDedupeResponse API**
    - Variables to be mapped from the below: (001 & 007)
    
    <firstName>
    <middleName>
    <lastName>
    <dob>
    <permanentAddress1>
    <permanentAddress2>
    <permanentAddress3>
    <permanentCity>
    <permanentPincode>
    <permanentAddressState>
    <permMobileNo>
    <customerlcid>
    <customerProfile>
    <customersource>
    <contractNo>
    <fatherName>
    <panNo>
    <drivingLicense>
    <electionCard>
    <passport>
    <aadhar>
    <ucic>
    <ucicType>
    <matchReason>
    <freeText5>
    <fanNumber>
    <loanNumber>
    <dedupeReferenceId>
    
    ```jsx
    INFO TataConnector RId=857e362c-c095-4648-b6b7-163a749c8890,
    AppId=d2896f53-16b7-4813-ae63-e33768fc920e,
    UId=61977bf3-571c-4b1b-8881-ced33fade058 - got checkDedupe response CreateDedupeResponse(extDedupeResponse=ExtDedupeResponse(opportunityID=,
    "extDedupeResApplicants="[
       "ExtDedupeResApplicant(extDedupeResApplicant=ExtDedupeResApplicantDetails(extDedupeAppDetails=ExtDedupeAppDetails(applicantType=P",
       "extDedupeMatches="[
          "ExtDedupeMatch(extDedupeMatch=ExtDedupeMatchDetails(fatherName=NARAYANSINGH PARMAR",
          "temporaryPhoneNo=",
          "officeState=",
          "matchType=Name",
          "Dob",
          "Pincode",
          "Pancard",
          "Phone_PERMMOBILE",
          "Phone",
          "din=",
          officeAddress1=,
          officeAddress3=,
          officeAddress2=,
          "temporaryState=",
          "freeText1=2024-07-04 00":"00":00,
          "temporaryPincode=",
          freeText2=,
          freeText3=,
          freeText4=,
          "matchReason=Name",
          "Dob",
          "Pincode",
          "Pancard",
          "Phone_PERMMOBILE",
          "Phone",
          "passport=",
          freeText5=1025927427,
          "resiCity=",
          freeText6=NEW,
          freeText7=,
          "commericialMobileNo=",
          extraDate2=,
          extraDate1=,
          "tan=",
          "engineNo=",
          "ckycId=",
          dyanamicIdNumber5=,
          dyanamicIdNumber4=,
          "officeCity=",
          "officePincode=",
          "matchCategory=",
          "motherName=",
          dyanamicIdNumber1=,
          "temporaryMobileNo=",
          "commericialPhoneNo=",
          "temporaryCity=",
          dyanamicIdNumber2=,
          "officePhoneNo=",
          dyanamicNumber3=,
          commericialAddress2=,
          "firstName=Shalu",
          commericialAddress1=,
          resiAddress3=,
          dob=16-06-1994,
          doe=16-06-1994,
          resiAddress2=,
          resiAddress1=,
          permanentPincode=431511,
          "resiPincode=",
          "lastName=Chavan",
          "officeMobileNo=",
          dyanamicIdType5=0,
          "commericialState=",
          "resiMobileNo=",
          "contractSource=MILES VANTAGE",
          "loanSanctionAmount=",
          "overDueCount=",
          contractNo=16788,
          "commericialPincode=",
          "cin=",
          "chasisNo=",
          dyanamicIdType4=0,
          "loanOverDueAmount=",
          dyanamicIdType3=0,
          dyanamicIdType2=0,
          "loanOutstandingAmount=",
          dyanamicIdType1=0,
          commericialAddress3=,
          "electionCard=",
          "aadhar=",
          permanentMobileNo=9359784033,
          temporaryAddress2=,
          "commericialCity=",
          temporaryAddress1=,
          "resiPhoneNo=",
          "contractStatus=",
          "loanDistributedAmount=",
          panNo=AZFPT9905R,
          "permanentPhoneNo=",
          emailId2=,
          "rcNo=",
          emailId1=RANBIRSONA45@GMAIL.COM,
          "permanentState=Maharashtra",
          permanentAddress2=Purna Purna Parbhani,
          permanentAddress3=Maharashtra India 431511,
          permanentAddress1=W/O Vijaysingh Chavan SIDDHARTH NAGAR PURNA Purna,
          customerLcid=16050,
          "drivingLicense=",
          "resiState=",
          "middleName=Vijaysingh",
          "spouseName=",
          "permanentCity=Parbhani",
          "negReason=",
          temporaryAddress3=))
       ],
       "customerProfile=I",
       "ucicType=",
       dedupeReferenceId=98051216,
       "customerSource=VoltMoney",
       applicantReferenceId=4272185703733745422,
       overallResult=001,
       "ucic=)))"
    ],
    "loanNumber=",
    fanNumber=291BZ8641699),
    "retStatus=SUCCESS",
    "sysErrorMessage=null",
    "errorMessage=null",
    "sysErrorCode=null) for lender Tata"
    ```
    
- Notes —> Important points in case of Negative and WIP Dedupe result
    
    In case of **No Match Found. OverallResult = 004**
    
    Map the keys in the Posidex report with the values from the below **CreateDedupeRequest**
    
    <firstName>
    <middleName>
    <lastName>
    <dob>
    <permMobileNo>
    
    ```jsx
    INFO TataConnector RId=9b1f7a29-31d5-482e-bf9f-62f02a447c0c,
    AppId=c31fd0f1-985a-4623-9756-0bd594384396,
    "UId= - got checkDedupe CreateDedupeRequest(password=",
    "extDedupeRequest=ExtDedupeRequest(extDedupeReqLoanDetails=ExtDedupeReqLoanDetails(branchCode=null",
    companyCode=7000,
    webTopNumber=291BZ8655334,
    opportunityID=241150844177,
    "product=LAS",
    "branchName=Mumbai",
    "customerCreation=N",
    "loanNumber=null",
    fanNumber=291BZ8655334,
    "userId=LAS)",
    "extDedupeReqApplicants="[
       ExtDedupeReqApplicant(extDedupeReqApplicant=ExtDedupeReqApplicantv2(fatherName=null,
       officeAdddress1=null,
       customerlcid=c31fd0f1-985a-4623-9756-0bd594384396,
       "customersource=VoltMoney",
       "din=null",
       "commAddressState=null",
       freeText1=null,
       freeText2=null,
       tempAdddress1=null,
       freeText3=null,
       freeText4=null,
       "tempPincode=null",
       "passport=null",
       freeText5=null,
       "officePhone=null",
       "resiCity=Murshidabad",
       freeText6=null,
       freeText7=null,
       freeText8=null,
       extraDate4=null,
       extraDate5=null,
       extraDate2=null,
       extraDate3=null,
       extraDate1=null,
       permMobileNo=8016625324,
       "ucic=null",
       tempAdddress2=null,
       freeText10=null,
       tempAdddress3=null,
       "commCity=null",
       "permanentAddressState=null",
       "tan=null",
       "resiAddressState=West Bengal",
       "ckycId=null",
       "engineNo=null",
       dyanamicIdNumber5=null,
       "resiPhone=null",
       dyanamicIdNumber4=null,
       "officeCity=null",
       commAdddress3=null,
       "officePincode=null",
       commAdddress2=null,
       "commMobileNo=null",
       dyanamicIdNumber1=null,
       "motherName=null",
       freeText9=null,
       applicantReferenceId=1859975472614471635,
       dyanamicIdNumber2=null,
       dyanamicNumber3=null,
       "firstName=Subhadip",
       dob=07-09-1996,
       "permPhone=null",
       commAdddress1=null,
       "doe=null",
       "officeAddressState=null",
       officeAdddress3=null,
       permanentAdddress1=null,
       "permanentPincode=null",
       officeAdddress2=null,
       permanentAdddress2=null,
       permanentAdddress3=null,
       "tempAddressState=null",
       resiPincode=742103,
       "officeMobileNo=null",
       "lastName=Mukherjee",
       "resiMobileNo=null",
       "tempMobileNo=null",
       "contractNo=null",
       "cin=null",
       "chasisNo=null",
       dyanamicIdType2=0,
       dyanamicIdType1=0,
       "customerStage=Prospect",
       "applicantType=P",
       resiAdddress1=null,
       "electionCard=null",
       "aadhar=null",
       resiAdddress2=null,
       resiAdddress3=null,
       "customerProfile=I",
       panNo=DXKPM5313Q,
       "rcNo=null",
       "tempPhone=null",
       "drivingLicense=null",
       "tempCity=null",
       "middleName=null",
       "spouseName=null",
       "permanentCity=null",
       "commPhone=null",
       "commPincode=null))"
    ]")",
    "userName=",
    "refId=1859975472614471635) for lender":"Tata"
    ```
    
    In case of **Negative Dedupe Result. OverallResult = 002** and ****In case of **WIP Result. OverallResult = 006**
    
    We have to produce each of the **ExtDedupeMatch** in the **API response** in different rows in the template.
    
    ```jsx
    {
    	"extDedupeResponse": {
    		"opportunityID": "",
    		"extDedupeResApplicants": [
    			{
    				"extDedupeResApplicant": {
    					"extDedupeAppDetails": {
    						"applicantType": "P",
    						"extDedupeMatches": [
    							{
    								"extDedupeMatch": {
    									"officeState": "",
    									"matchType": "Name,Dob,Pancard,Phone_PERMMOBILE,Phone",
    									"officeAddress1": "",
    									"Product": "",
    									"officeAddress3": "",
    									"officeAddress2": "",
    									"LoanNumber": "APPL12400893",
    									"freeText1": "",
    									"temporaryPincode": "",
    									"freeText2": "",
    									"freeText3": "",
    									"freeText4": "",
    									"matchReason": "Name,Dob,Pancard,Phone_PERMMOBILE,Phone",
    									"freeText5": "",
    									"freeText6": "",
    									"freeText7": "",
    									"extraDate2": "",
    									"extraDate1": "",
    									"engineNo": "",
    									"ckycId": "",
    									"dyanamicIdNumber5": "",
    									"dyanamicIdNumber4": "",
    									"officePincode": "",
    									"matchCategory": "",
    									"dyanamicIdNumber1": "",
    									"temporaryMobileNo": "",
    									"commericialPhoneNo": "",
    									"temporaryCity": "",
    									"dyanamicIdNumber2": "",
    									"resiAddress3": "",
    									"dob": "24-11-1989",
    									"doe": "24-11-1989",
    									"resiAddress2": "",
    									"resiAddress1": "",
    									"permanentPincode": "500037",
    									"lastName": "chaitanaya",
    									"dyanamicIdType5": 0,
    									"contractSource": "FinnOne",
    									"loanSanctionAmount": "",
    									"overDueCount": "",
    									"contractNo": "",
    									"dyanamicIdType4": 0,
    									"loanOverDueAmount": "",
    									"dyanamicIdType3": 0,
    									"dyanamicIdType2": 0,
    									"dyanamicIdType1": 0,
    									"permanentMobileNo": "9640841779",
    									"decisionReason": "",
    									"decisionRemark": "",
    									"commericialCity": "",
    									"resiPhoneNo": "",
    									"contractStatus": "",
    									"decision": "",
    									"panNo": "CCXPK7371M",
    									"emailId2": "",
    									"emailId1": "",
    									"permanentState": "",
    									"NegReasonRemark": "FinnOne_Reject",
    									"permanentAddress2": "HYD",
    									"permanentAddress3": "",
    									"permanentAddress1": "HNO 41 107 1 SANJAYPURI COLONY JAGADGIRIGUTTA BALANAGAR 500037",
    									"OpportunityID": "",
    									"customerLcid": "GLBCUST00012544104",
    									"spouseName": "",
    									"permanentCity": "Hyderabad",
    									"negReason": "FinnOne_Reject",
    									"fatherName": "SATYAVATHI KOMPELLA",
    									"temporaryPhoneNo": "",
    									"din": "",
    									"temporaryState": "",
    									"passport": "",
    									"resiCity": "",
    									"commericialMobileNo": "",
    									"tan": "",
    									"officeCity": "",
    									"motherName": "",
    									"officePhoneNo": "",
    									"FanNumber": "",
    									"dyanamicNumber3": "",
    									"commericialAddress2": "",
    									"firstName": "kompella krishna",
    									"commericialAddress1": "",
    									"decisionStage": "",
    									"resiPincode": "",
    									"officeMobileNo": "",
    									"commericialState": "",
    									"resiMobileNo": "",
    									"commericialPincode": "",
    									"cin": "",
    									"chasisNo": "",
    									"loanOutstandingAmount": "",
    									"commericialAddress3": "",
    									"Branch": "",
    									"electionCard": "",
    									"aadhar": "",
    									"temporaryAddress2": "",
    									"temporaryAddress1": "",
    									"loanDistributedAmount": "",
    									"permanentPhoneNo": "",
    									"rcNo": "",
    									"decisionDate": "",
    									"drivingLicense": "",
    									"resiState": "",
    									"middleName": "",
    									"temporaryAddress3": ""
    								}
    							},
    							{
    								"extDedupeMatch": {
    									"officeState": "",
    									"matchType": "Name,Pancard,Phone_PERMMOBILE,Phone",
    									"officeAddress1": "",
    									"Product": "",
    									"officeAddress3": "",
    									"officeAddress2": "",
    									"LoanNumber": "",
    									"freeText1": "",
    									"temporaryPincode": "",
    									"freeText2": "",
    									"freeText3": "",
    									"freeText4": "",
    									"matchReason": "Name,Pancard,Phone_PERMMOBILE,Phone",
    									"freeText5": "1013735615",
    									"freeText6": "NEW",
    									"freeText7": "NEW",
    									"extraDate2": "",
    									"extraDate1": "",
    									"engineNo": "",
    									"ckycId": "",
    									"dyanamicIdNumber5": "",
    									"dyanamicIdNumber4": "",
    									"officePincode": "",
    									"matchCategory": "",
    									"dyanamicIdNumber1": "",
    									"temporaryMobileNo": "",
    									"commericialPhoneNo": "",
    									"temporaryCity": "",
    									"dyanamicIdNumber2": "",
    									"resiAddress3": "",
    									"dob": "24-01-1989",
    									"doe": "24-01-1989",
    									"resiAddress2": "",
    									"resiAddress1": "",
    									"permanentPincode": "500037",
    									"lastName": "chaitanaya",
    									"dyanamicIdType5": 0,
    									"contractSource": "VMCFAB",
    									"loanSanctionAmount": "",
    									"overDueCount": "",
    									"contractNo": "",
    									"dyanamicIdType4": 0,
    									"loanOverDueAmount": "",
    									"dyanamicIdType3": 0,
    									"dyanamicIdType2": 0,
    									"dyanamicIdType1": 0,
    									"permanentMobileNo": "9640841779",
    									"decisionReason": "",
    									"decisionRemark": "",
    									"commericialCity": "",
    									"resiPhoneNo": "",
    									"contractStatus": "",
    									"decision": "",
    									"panNo": "CCXPK7371M",
    									"emailId2": "",
    									"emailId1": "",
    									"permanentState": "",
    									"NegReasonRemark": "",
    									"permanentAddress2": "GUTTA BALANAGAR 500037",
    									"permanentAddress3": "",
    									"permanentAddress1": "HNO 41 107 1 SANJAYPURI COLONY JAGADGIRI",
    									"OpportunityID": "",
    									"customerLcid": "0066F00001ClVOYQA3",
    									"spouseName": "",
    									"permanentCity": "Hyderabad",
    									"negReason": "",
    									"fatherName": "",
    									"temporaryPhoneNo": "",
    									"din": "",
    									"temporaryState": "",
    									"passport": "",
    									"resiCity": "",
    									"commericialMobileNo": "",
    									"tan": "",
    									"officeCity": "",
    									"motherName": "",
    									"officePhoneNo": "",
    									"FanNumber": "453PZ0332088",
    									"dyanamicNumber3": "",
    									"commericialAddress2": "",
    									"firstName": "PROSPECT-kompella krishna",
    									"commericialAddress1": "",
    									"decisionStage": "",
    									"resiPincode": "",
    									"officeMobileNo": "",
    									"commericialState": "",
    									"resiMobileNo": "",
    									"commericialPincode": "",
    									"cin": "",
    									"chasisNo": "",
    									"loanOutstandingAmount": "",
    									"commericialAddress3": "",
    									"Branch": "",
    									"electionCard": "",
    									"aadhar": "",
    									"temporaryAddress2": "",
    									"temporaryAddress1": "",
    									"loanDistributedAmount": "",
    									"permanentPhoneNo": "",
    									"rcNo": "",
    									"decisionDate": "",
    									"drivingLicense": "",
    									"resiState": "",
    									"middleName": "",
    									"temporaryAddress3": ""
    								}
    							},
    							{
    								"extDedupeMatch": {
    									"officeState": "",
    									"matchType": "Name,Dob,Pincode,Pancard,Phone_PERMMOBILE,Phone",
    									"officeAddress1": "",
    									"Product": "",
    									"officeAddress3": "",
    									"officeAddress2": "",
    									"LoanNumber": "",
    									"freeText1": "",
    									"temporaryPincode": "",
    									"freeText2": "",
    									"freeText3": "",
    									"freeText4": "",
    									"matchReason": "Name,Dob,Pincode,Pancard,Phone_PERMMOBILE,Phone",
    									"freeText5": "1026654020",
    									"freeText6": "NEW",
    									"freeText7": "",
    									"extraDate2": "",
    									"extraDate1": "",
    									"engineNo": "",
    									"ckycId": "",
    									"dyanamicIdNumber5": "",
    									"dyanamicIdNumber4": "",
    									"officePincode": "",
    									"matchCategory": "",
    									"dyanamicIdNumber1": "",
    									"temporaryMobileNo": "",
    									"commericialPhoneNo": "",
    									"temporaryCity": "",
    									"dyanamicIdNumber2": "",
    									"resiAddress3": "",
    									"dob": "24-11-1989",
    									"doe": "24-11-1989",
    									"resiAddress2": "",
    									"resiAddress1": "",
    									"permanentPincode": "500049",
    									"lastName": "Chaitanya",
    									"dyanamicIdType5": 0,
    									"contractSource": "MILES VANTAGE",
    									"loanSanctionAmount": "",
    									"overDueCount": "",
    									"contractNo": "",
    									"dyanamicIdType4": 0,
    									"loanOverDueAmount": "",
    									"dyanamicIdType3": 0,
    									"dyanamicIdType2": 0,
    									"dyanamicIdType1": 0,
    									"permanentMobileNo": "9640841779",
    									"decisionReason": "",
    									"decisionRemark": "",
    									"commericialCity": "",
    									"resiPhoneNo": "",
    									"contractStatus": "",
    									"decision": "",
    									"panNo": "CCXPK7371M",
    									"emailId2": "",
    									"emailId1": "KKC.KOUTILYA@GMAIL.COM",
    									"permanentState": "Telangana",
    									"NegReasonRemark": "",
    									"permanentAddress2": "HafeezpetK.v. RangareddyMANJEERA PIPE LINE ROAD",
    									"permanentAddress3": "TelanganaIndia500049",
    									"permanentAddress1": "S/O MARKANDEYA SARMAFLAT NO 1206, PEARL BLOCKMIYAP",
    									"OpportunityID": "",
    									"customerLcid": "35212",
    									"spouseName": "",
    									"permanentCity": "K.v. Rangareddy",
    									"negReason": "",
    									"fatherName": "MARKANDEYA SARMA KOMPELLA",
    									"temporaryPhoneNo": "",
    									"din": "",
    									"temporaryState": "",
    									"passport": "",
    									"resiCity": "",
    									"commericialMobileNo": "",
    									"tan": "",
    									"officeCity": "",
    									"motherName": "",
    									"officePhoneNo": "",
    									"FanNumber": "",
    									"dyanamicNumber3": "",
    									"commericialAddress2": "",
    									"firstName": "Kompella",
    									"commericialAddress1": "",
    									"decisionStage": "",
    									"resiPincode": "",
    									"officeMobileNo": "",
    									"commericialState": "",
    									"resiMobileNo": "",
    									"commericialPincode": "",
    									"cin": "",
    									"chasisNo": "",
    									"loanOutstandingAmount": "",
    									"commericialAddress3": "",
    									"Branch": "",
    									"electionCard": "",
    									"aadhar": "",
    									"temporaryAddress2": "",
    									"temporaryAddress1": "",
    									"loanDistributedAmount": "",
    									"permanentPhoneNo": "",
    									"rcNo": "",
    									"decisionDate": "",
    									"drivingLicense": "",
    									"resiState": "",
    									"middleName": "Krishna",
    									"temporaryAddress3": ""
    								}
    							}
    						],
    						"customerProfile": "I",
    						"ucicType": "",
    						"dedupeReferenceId": "98049482",
    						"customerSource": "VoltMoney",
    						"applicantReferenceId": "8807716696666506466",
    						"overallResult": "002",
    						"ucic": ""
    					}
    				}
    			}
    		],
    		"loanNumber": "APPL12400893",
    		"fanNumber": "291BZ8654789"
    	},
    	"retStatus": "SUCCESS",
    	"sysErrorMessage": "null",
    	"errorMessage": "null",
    	"sysErrorCode": "null"
    }
    ```
    

- **Map the <customerProfile> with the value and populate value against the Customer Profile from below.**

| Customer Profile | Value |
| --- | --- |
| Individual | I |
| Corporate | C |
- **Map the Result Remark by mapping the below value with <overallResult>**

**Format: Value - Overall Dedupe Result**

![image.png](New%20Posidex%20report%20template/image.png)

| Overall Dedupe Result | Value |
| --- | --- |
| Positive | 001 |
| Negative | 002 |
| No Match Found | 004 |
| WIP | 006 |
| RECENT DISBURSED | 007 |

---

# **Design**

Attaching the sample Posidex reports for:

- Positive

[Positive.pdf](New%20Posidex%20report%20template/Positive.pdf)

- Negative

[Negative.pdf](New%20Posidex%20report%20template/Negative.pdf)

- No match found

[No record found (1).pdf](New%20Posidex%20report%20template/No_record_found_(1).pdf)

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

- [x]  Product
    - [ ]  -
- [x]  Business
    - [ ]  -
- [x]  Design
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