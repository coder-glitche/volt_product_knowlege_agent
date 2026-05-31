# Bank Account Verification for Disbursement in TATA

: Ayush Kumar
Created time: August 12, 2024 3:41 PM
Status: In progress
Last edited: September 6, 2024 7:57 PM
Owner: Ayush Kumar

# **What problem are we solving?**

- For users whose loans are processed with TATA and who have multiple bank accounts stored with the lender, the Volt’s system picks the first bank account for sending disbursement request to the lender.
- Discrepancies occurs between the lender's records and Volt's database regarding a customer's bank account information due to lack of verification process during the account updation using admin tool.

---

# **How do we measure success?**

Success Rate of Disbursement

---

# **How are others solving this problem?**

---

# **What is the solution?**

- We will match the bank account number and IFSC code of a customer's bank account stored in Volt's database with the bank account details stored at TATA's end before disbursal.
- This process ensures synchronisation between the two systems, allowing us to accurately identify the correct bank account for disbursement, even when TATA has multiple bank accounts stored for a user, while Volt only retains one.

Below is the request and response of **getDisbursementInfo API** and **SaveDisbursement API**:

**GetDisbursementInfo API**

**REQUEST:-**

INFO NonStaticHttpUtility RRId= RId=6476af48-8ffd-4e4f-bc3b-dabb5f40bf93, CreditId=8a806612907de1bb01907de459bc0005, UId= - Creating post request for uri [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/GetDisbursementInfo](https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/GetDisbursementInfo) with body [{
"DisbursementAmount": "",
"LoanNo": "16763",
"UserName": "adminiaf"
}]

**RESPONSE:-**

INFO NonStaticHttpUtility RRId= RId=6476af48-8ffd-4e4f-bc3b-dabb5f40bf93, CreditId=8a806612907de1bb01907de459bc0005, UId= - got a response with status 200, and body {
"GetDisbursementInfo_Response": {
"DisbursementDetails": [
{
"ExcessMargin": "0.00",f
"InterestDue": "0.00",
"ThirdPartyBankAccount": [],
"ClientBankAccount": [
{
"ClientBankName": "Axis Bank",
"ClientParyBankIFSC": "UTIB0SAZP01",
"ClientBankAccountNo": "921010054991494"
},
{
"ClientBankName": "CENTRAL BANK OF INDIA",
"ClientParyBankIFSC": "CBIN0280670",
"ClientBankAccountNo": "3309090278"
}
],
"LoanAccount": "14265",
"AvailableAmountForDisbursement": "84434.02",
"LoanNo": "16763",
"ChargesAmountDetails": [],
"ChargesDue": "0.00",
"LoanAmount": "0.00",
"RateOfInterest": "10.49",
"LoanAccountLimit": "74000.00",
"DrawingPower": "84434.02",
"PenalInterest": "0.00",
"LoanContractLimit": "74000.00"
}
],
"status": {
"Status": "Success",
"Remarks": "",
"Code": "01"
}
},
"retStatus": "SUCCESS",
"sysErrorMessage": "",
"sysErrorCode": ""
}

**SaveDisbursement API**

**REQUEST: -**

INFO NonStaticHttpUtility RRId= RId=6476af48-8ffd-4e4f-bc3b-dabb5f40bf93, CreditId=8a806612907de1bb01907de459bc0005, UId= - Creating post request for uri [https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveDisbursement](https://miles-prod-apicast.apps.prdservices.tatacapital.com/rest/v1.0/miles/SaveDisbursement) with body [{
"Amount": "34000",
"AutoApprove": "Y",
"BankAccountNo": "921010054991494",
"ChargesAndAmount": [],
"DeductedCharges": "",
"DeductedInterest": "0.00",
"IFSC": "UTIB0SAZP01",
"LoanNo": "16763",
"NBFCBankAccountNo": "00600310031203",
"NBFCBankName": "HDFC BANK - OLD DISBURSEMENT A/C",
"NBFCIFSC": "HDFC0000240",
"NetAmount": "34000",
"RequestDate": "2024-07-30",
"TransactionType": "Disbursement to Client",
"UniqueRecordID": "162439032908357",
"username": "adminiaf"
}]

**RESPONSE:-**

INFO NonStaticHttpUtility RRId= RId=6476af48-8ffd-4e4f-bc3b-dabb5f40bf93, CreditId=8a806612907de1bb01907de459bc0005, UId= - got a response with status 200, and body {
"retStatus": "SUCCESS",
"sysErrorMessage": "",
"sysErrorCode": "",
"SaveDisbursement_Response": {
"DisbursementData": [
{
"RespRemarks": "Success",
"RecordStatusCode": "0",
"UniqueRecordID": "162439032908357",
"StagingID": "91B95707-40F6-44BD-B3D5-C7EB5E355797"
}
],
"status": {
"Status": "Success",
"Remarks": "",
"Code": "01"
}
}
}

We will match the bank account from the response of **getDisbursementInfo API** and the **bank account stored in Volt’s DB** before sending the disbursement amount along with the bank account in the request of SaveDisbursement API to the lender TATA.

**→ Case 1:** 

- The Bank account stored in our database matches with the bank account received in the response of getDisbursementInfo API
- We send the disbursement in the bank account through a request through SaveDisbursement API

→ **Case 2:**

- The Bank account stored in our database does not matches with the bank account received in the response of getDisbursementInfo API
- We will setDisbursalRemark as “Error while creating disbursal request with lender Bank account details for creditId: {credit_id} does not match with the bank account details from lender. Lender details [{"ClientBankAccountNo":"{Account_number}","ClientBankName":"{Bank_Name} ”

## 

## Requirements in Admin Tool:

**Changes in Admin Tool:**

- After the credit creation, if the customer wants to update the Bank account, then we will follow the general flow:
    - The ops will send the request to the lender and follow up on updates every 1 hr
    - After successful updation of Bank account on the lender’s end, the ops team will use the admin action “Update bank account after credit creation” to update the bank account details in Volt’s database
- The admin tool “Update bank account after credit creation” after successfully updating the bank account should call the getDisbursementInfo API.
- The Bank account details which we receive in response to the getDisbursementInfo API should be matched with the updated bank account present in Volt’s database.
    - Case 1:
    
    If the Bank account matches, there has been successful updation 
    
    - Case 2:
    
    If there is a mismatch in the bank account, then an error message stating “This Bank account is not updated with the lender” should be displayed while using this admin tool and ops will handle it operationally
    

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