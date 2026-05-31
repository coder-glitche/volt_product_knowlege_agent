# Foreclosure repayment - Handle PenalInterestAccruedNotDue

: Ranjan kumar Singh
Created time: September 23, 2024 11:53 AM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

- In foreclosure request we have not handled the “PenalInterestAccruedNotDue” field in the calculation of net payable amount which is leading to the rejection of foreclosure request.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

- Include the "PenalInterestAccruedNotDue" field in the calculation of the net payable.
- Display the "PenalInterestAccruedNotDue" amount on the UI.
    - The backend (BE) needs to send this field with its value to the frontend (FE), so the FE can display it on the UI and use it to calculate the amount shown to the user.
    - Outstanding interest amount should include the value of “PenalInterestAccruedNotDue”

### Foreclosure data

INFO NonStaticHttpUtility RRId= RId=5e867e3f-2c10-4173-b259-7e6eef585e85, CreditId=8a80138c8ed5fcc1018edacc9df62080, UId= - got a response with status 200, and body {
"RetStatus": "SUCCESS",
"LASGetSummaryData_Response": {
"summary": [
{
"HeadofFamily": "No",
"EmailID": "[Sagar.Chheda@tatacapital.com](mailto:Sagar.Chheda@tatacapital.com)",
"Address": "W/O Sanjay Babel,51,nirmal vihar,hiran magrisector-3,udaipur,Udaipur ShastriCircle,Udaipur,Rajasthan,313001",
"LoanAccount": [
{
"Address_Office": "                                                                                                                                                                                                                                                          3",
"PendingTDS": "0.00",
"PrincipalOutstanding": "33600.00",
"AmountAvailable_ForDisbursement": "157564.82",
"Primary_AccountHolder": "Suman  Babel",
"Product": "LAS",
"ECSApplicable": "No",
"Primary_Borrower": "Suman  Babel",
"AgreementNo": "                    ",
"TotalPortfolioValue": "234326.28",
"CollateralMutualFund": [
{
"LienMarkNo": "1796503172",
"ISIN_Lien": "INF209K01VA3",
"PortfolioValue": "234326.2814",
"AMFI_Code": "119568",
"PlanID": "119568",
"InTransitReleaseQty": "0.0000",
"SchemeName": "Aditya Birla Sun Life Liquid Fund - Growth - Direct Plan",
"Option": "Growth",
"FolioNo": "1037581953",
"LienQuantity": "599.6220"
}
],
"CollateralEquity": [],
"AccountStatus": "Active",
"BankDetailsNonPOA": [],
"PledgeExpiry_Date": null,
"Address_Correspondence": "W/O Sanjay Babel,51,nirmal vihar,hiran magrisector-3,udaipur,Udaipur ShastriCircle,Udaipur,Rajasthan,313001",
"ECSBankAccount": "IDBI",
"Account_Number": "8862",
"OutstandingInterest": "0.00",
"AmountDue": "0.00",
"OutstandingCharges": "0.00",
"AccountExpiry_Date": "3/31/2050 12:00:00 AM",
"LoanAccountName": "Suman  Babel",
"AccountMaturityDate": "3/31/2050 12:00:00 AM",
"ScheduleDetails": [
{
"Purpose_of_Loan": "Personal",
"Grace_Period_Principal": "7",
"LoanType": "Term Loan",
"PenalRateInterest": "25.51",
"PenalInterestAccruedNotDue": "25.28",
"LoanLimit": "187500.00",
"LoanNumber": "11031",
"LoanAmount": "33600.00",
"LoanMaturityDate": "4/14/2025 12:00:00 AM",
"Interest_Outstanding": "0.00",
"PrincipalFrequency": "Monthly",
"OverduePrincipal": "InActive",
"InterestRate": "10.49",
"AmountOverdue_ForCustomer": "954.26",
"SubType": "Short Term",
"PenalRatePrincipal": "0.00",
"ReviewPeriod": "180 Days",
"ChargesPosting": "Daily",
"Interest_Frequency": "Monthly",
"ChargesOutstanding": "0.00",
"InterestType": "Floating",
"OverdueInterest": "Active",
"GracePeriod_Interest": "0",
"PenalInterest": "0.00",
"InterestAccruedNotDue": "954.26",
"AmountDue_ForCustomer": "0.00"
}
],
"TotalOutstanding": "33600.00",
"Coborrowers": [],
"SanctionedLimit": "187500.00",
"DrawingPower": "191164.82",
"ProductCategory": "Loan Against Mutual Funds _Digital",
"AccountOpening_Date": "4/14/2024 12:00:00 AM",
"DPDetailsNonPOA": [],
"PrimaryHolder": "Suman  Babel"
}
],
"ServiceBranch": "DELHI - RAJENDRA PLACE",
"FamilyName": "LAS_DIGITAL",
"CustomerID": "10572",
"DPDetails": [],
"NBFCBankDetails": [
{
"NBFC_BankAccountNo": "00600310031213",
"NBFC_BankName": "HDFC BANK -  NEW COLLECTION A/C",
"NBFC_BranchName": "SANDOZ HOUSE",
"NBFC_IFSC_Code": "HDFC0000240",
"NBFC_DefaultAccount": "Yes"
},
{
"NBFC_BankAccountNo": "00600130014489",
"NBFC_BankName": "HDFC BANK - OLD DISBURSEMENT A/C",
"NBFC_BranchName": "SANDOZ HOUSE",
"NBFC_IFSC_Code": "HDFC0000240",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "12345678910",
"NBFC_BankName": "PRINCIPAL BALANCE OF BANCS AS OF 31-03-2013",
"NBFC_BranchName": "HEAD OFFICE",
"NBFC_IFSC_Code": "11111111111",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "00600310014524",
"NBFC_BankName": "HDFC BANK ",
"NBFC_BranchName": "FORT",
"NBFC_IFSC_Code": "HDFC0000060",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "00600310031203",
"NBFC_BankName": "HDFC BANK - NEW DISBURSEMENT A/C",
"NBFC_BranchName": "SANDOZ HOUSE",
"NBFC_IFSC_Code": "HDFC0000240",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "164051",
"NBFC_BankName": "HDFC BANK - BILL DESK CONTROL ACCOUNT ",
"NBFC_BranchName": "SANDOZ HOUSE",
"NBFC_IFSC_Code": "HDFC0000240",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "115102",
"NBFC_BankName": "ICICI BANK_E-NACH_115102",
"NBFC_BranchName": "MUMBAI",
"NBFC_IFSC_Code": "00000000000",
"NBFC_DefaultAccount": "No"
},
{
"NBFC_BankAccountNo": "00600310031247",
"NBFC_BankName": "HDFC BANK LTD_ENACH",
"NBFC_BranchName": "MUMBAI",
"NBFC_IFSC_Code": "00000000000",
"NBFC_DefaultAccount": "No"
}
],
"Office_Country": "                         ",
"Office_Fax_No": null,
"PhoneNo": "7208111020",
"FaxNo": null,
"mailID": "[sumanbabel252@gmail.com](mailto:sumanbabel252@gmail.com)",
"Office_Telephone": null,
"Office_State": "                         ",
"MobileNo": "7208111020",
"BankDetails": [
{
"BankName": "IDBI",
"POAAccount": "No",
"DefaultAccount": "Yes",
"Branch": "UDAIPUR",
"IFSCCode": "IBKL0000050",
"BeneficiaryName": "Suman Babel",
"AccountType": "Savings",
"BankAccountNumber": "0050104000539913"
}
],
"DefaultMailing": "Home",
"RMName": "Sagar Chheda",
"City": "Udaipur",
"Telephone_Correspondence": null,
"FamilyLoanAccounts": [
{
"LoanAccountNo": "8862",
"LoanAccountName": "Suman  Babel"
}
],
"Office_Address": "                                                                                                                                                                                                                                                          3",
"NameOfCompany": null,
"MobileNumber": "7877458109          ",
"Office_EmailID": null,
"State": "Rajasthan",
"Country": "INDIA",
"Office_Mobile_No": null,
"Office_City": null,
"OccupationType": null
}
],
"PDFdata": null,
"status": {
"Status": "Success",
"Remarks": "",
"Code": "01"
}
},
"sysErrorMessage": "",
"sysErrorCode": ""
}

## User stories / User flow

## Requirements

---

# **Design**

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=11615-13514&t=bq7BBTxum8T4P40v-4](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=11615-13514&t=bq7BBTxum8T4P40v-4)

![Screenshot 2024-09-23 at 12.11.02 PM.png](Foreclosure%20repayment%20-%20Handle%20PenalInterestAccrue/Screenshot_2024-09-23_at_12.11.02_PM.png)

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