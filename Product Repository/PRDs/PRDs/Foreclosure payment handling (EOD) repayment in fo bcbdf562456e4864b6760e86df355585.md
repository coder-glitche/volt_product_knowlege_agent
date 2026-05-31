# Foreclosure payment handling (EOD) repayment in foreclosure API (BFL & TCL)

: Ranjan kumar Singh
Created time: July 29, 2024 5:21 PM
Status: Done
Last edited: February 19, 2026 7:14 PM
Owner: Lalit Bihani

# **What problem are we solving?**

BAJAJ:

- When user foreclose the loan on Volt UI after 6 PM, we do not consider interest of same days in Net dues payable.
- This led the foreclosure rejection from the lender end.

TATA:

- We do not ask user to pay accrue penal charges and due to this foreclosure are getting rejected.

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

- This changes are only of BAJAJ customers
- In the foreclosure API, the simulation provides the accrued interest for the next 7 days.
- Users submitting a foreclosure request after 5:59 PM are required to pay according to the “day1ClosureAmount” specified in the foreclosure data.
- We need to add “Interest for {{T+1}}” in Total outstanding interest  Accordion if user are placing foreclosure between 6 PM to 11.59 PM.
    - T = Date on which user are placing foreclosure request
    - T+1 = Next Date from foreclosure request date
- Amount to show in  “Interest for {{T+1}}” = (”day1ClosureAmount" in “payableForNext7Days” Object - "netPayable" in "ForeClosureData" Object)\\\\\\

**Example:**

Lets say user are requesting the foreclose today at 5 PM

Total due as on today = 273.00

Total due on T+1 = 273.18

Then user are required to pay = 273.00

Lets say user are requesting the foreclose today at 7 PM

Total due as on today = 273.00

Total due on T+1 = 273.18

Then user are required to pay  273.18 from 6 PM to 11:59 PM

### Foreclosure data

{

"INFO": "BajajLMSConnector",

"RRId": "",

"RId": "85a80992-990e-49e4-8a3c-f5f45d0adfce",

"CreditId": "8a805bf589cf6d890189dfb3efde033f",

"UId": "",

"message": "got foreclosure statement response",

"fas-number": "V402LAS00110249",

"response": {

"GetForeClosureStatementResponse": {

"data": [

{

"ForeClosureData": {

"asOnForeclosureDate": "4th Nov 2024",

"loanAccountName": "RUCHIT PARESH PATWA",

"address": "B/301-302 MARBLE ARCH, T.P.S. ROAD VEER SAVARKAR, Borivali West, Borivali West, Mumbai, Maharashtra, Mumbai, 400092",

"loanAccNo": "159965",

"loanContractNo": "V402LAS00110249",

"outstandingPrincipal": 0.00,

"outstandingInterest": 273.00,

"outstandingCharges": 0.00,

"interestAccruedNotDue": 0.00,

"penalInterestReceivable": 0.00,

"penalInterestAccruedNotDue": 0.00,

"tDSReceivable": 0.00,

"totalNotionalChargesAndDematBounce": 0.00,

"prepaymentCharges": 0.00,

"interestOnClosureDate": 0.00,

"penalInterestOnClosureDate": 0.00,

"totalDue": 273.00,

"advanceInterest": 0.00,

"excessMargin": 0.00,

"totalCredit": 0.00,

"netPayable": 273.00,

"payableForNext7Days": [

{

"day1ClosureDate": "09-Jul-2024",

"day1ClosureAmount": 273.18

},

{

"day2ClosureDate": "10-Jul-2024",

"day2ClosureAmount": 273.36

},

{

"day3ClosureDate": "11-Jul-2024",

"day3ClosureAmount": 273.54

},

{

"day4ClosureDate": "12-Jul-2024",

"day4ClosureAmount": 273.72

},

{

"day5ClosureDate": "13-Jul-2024",

"day5ClosureAmount": 273.90

},

{

"day6ClosureDate": "14-Jul-2024",

"day6ClosureAmount": 274.08

},

{

"day7ClosureDate": "15-Jul-2024",

"day7ClosureAmount": 274.26

}

]

}

}

],

"PDFdata": null

}

}

}

## User stories / User flow

## Requirements

---

# **Design**

For BAJAJ customer who are placing foreclosure request post 6 PM, we need to show info icon and educate that Net payable includes the next day interest on outstanding amount and any recurring penal interest of the request placed post 6 PM.

[https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=401-28549&t=DQvfLACaQE295vJE-4](https://www.figma.com/design/UjmVWLf9A4C1qs3BATH4wZ/Post-loan-Flow?node-id=401-28549&t=DQvfLACaQE295vJE-4)

![Pay outstanding dues (1).png](Foreclosure%20payment%20handling%20(EOD)%20repayment%20in%20fo/Pay_outstanding_dues_(1).png)

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

- From 12 AM to 6PM, check if current date and asOnForeclosureDate is same if yes collect same day foreclosure amount i.e netPayable value else collect foreclosure amount of current date + 1 days i.e day1ClosureAmount
- Current logic for handling post 6 PM will be same