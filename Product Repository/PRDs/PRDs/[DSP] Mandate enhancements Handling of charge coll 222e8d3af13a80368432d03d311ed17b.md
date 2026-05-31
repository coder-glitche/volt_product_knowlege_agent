# [DSP] Mandate enhancements : Handling of charge collection

: Ameya Aglawe
Created time: June 30, 2025 6:23 PM
Status: Pending Review
Last edited: July 25, 2025 3:49 PM

# **What problem are we solving?**

---

Finflux currently does not support configuring a future-dated due date while posting charges. This limitation results in a suboptimal customer experience in the following scenarios:

1. **Charges Posted Between 1st–7th of the Month**
    
    These charges, although intended to be due on the 7th of the *following* month, are treated as due within the *same* month. As a result, collection attempts are initiated prematurely, leading to confusion or dissatisfaction for users expecting the deduction only in the next billing cycle.
    
2. **Charges Posted Between 7th–19th of the Month**
    
    In this window, DSP begins initiating a second mandate from the 20th of the *same* month. Since future-dated charge configuration is unavailable, these charges also get picked up for collection within the same cycle—contrary to the intended behavior of aligning them with the next scheduled mandate.
    

# **How do we measure success?**

---

- No charges are being collected within the same billing cycle via mandate collection

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

- During mandate batch file generation, the system will compute the sum of all charges posted in the current month and subtract it from the total charges due. This will help accurately determine the portion of charges that remain due and need to be included in the current month's mandate presentation.

## User stories / User flow

## Requirements

---

**Fenix handling -** 

- At present, we retrieve interest and charge dues using the Loan Summary API, which also includes charges posted during the current billing cycle.
- Finflux has now shared the getAllChargeDetails API, which provides a detailed list of all outstanding charges for all loan accounts, each tagged with its respective due date.
    - Following is the response
        
        ```jsx
        [
            {
                "account_number": "000000030",
                "charge_id": "LF1",
                "Due Date": "2024-05-29 23:59:59",
                "outstanding_amount": 500.220000
            },
            {
                "account_number": "000000030",
                "charge_id": "PF1",
                "Due Date": "2024-05-29 23:59:59",
                "outstanding_amount": 500.220000
            },
            {
                "account_number": "000000030",
                "charge_id": "PF1",
                "Due Date": "2024-05-29 23:59:59",
                "outstanding_amount": 500.220000
            },
            {
                "account_number": "000000040",
                "charge_id": "PF1",
                "Due Date": "2024-05-30 23:59:59",
                "outstanding_amount": 500.220000
            },
            {
                "account_number": "000000040",
                "charge_id": "PF1",
                "Due Date": "2024-06-24 15:24:22",
                "outstanding_amount": 500.220000
            },
            {
                "account_number": "000000049",
                "charge_id": "CC", 
                "Due Date": "2024-07-19 10:46:04",
                "outstanding_amount": 590.260000
            },
            {
                "account_number": "000000049",
                "charge_id": "CC",
                "Due Date": "2024-07-30 23:59:59",
                "outstanding_amount": 590.260000
            },
            {
                "account_number": "000000049",
                "charge_id": "CC",
                "Due Date": "2024-07-25 17:53:55",
                "outstanding_amount": 590.260000
            },
            {
                "account_number": "000000049",
                "charge_id": "MP",
                "Due Date": "2024-07-24 15:29:09",
                "outstanding_amount": 590.260000
            },
            {
                "account_number": "000000049",
                "charge_id": "MP",
                "Due Date": "2024-07-21 13:53:11",
                "outstanding_amount": 590.260000
            }]
        ```
        
- As part of the mandate file generation job, we will additionally call the getAllChargeDetails API to compute the total charges that became due from the 1st of the current month up to the job execution date.
- This amount will then be subtracted from the total charges fetched via the Loan Summary API, allowing us to isolate and consider only the charges that were posted in the previous billing cycles for each loan account.
- Logic -
    - For mandate presentation on 7th of a month
        - Call summary API to get total interest due, total charges due [consider this as X]
        - Call getAllChargeDetails
            - Sum of all the charges which are posted between 1st and 6th (both included) of the current month [consider this as Y]
        - Set the charges due value for mandate presentation as X - Y
    - For mandate presentation on 20th of a month
        - Call summary API to get total interest due, total charges due [consider this as X]
        - Call getAllChargeDetails
            - Sum of all the charges which are posted between 1st and 19th (both included) of the current month [consider this as Y]
        - Set the charges due value for mandate presentation as X - Y
- Example -
    - allLoanAccountSummary API response
        
        ```jsx
        {
                "fenixLoanAccountId": "FXLAN97149399",
                "status": "ACTIVE",
                "sanctionAmount": 20000000.00,
                "totalDrawingPower": 193932.43,
                "availableAmountForDisbursement": 1932.43,
                "currentOutstanding": 192000.00,
                "principalOutstandingAmount": 192000.00,
                "excessAmount": 0.00,
                "chargesDue": 200000.00,
                "interestDue": 10000.00,
                "penalChargesDue": 0.00,
                "sourcingChannelCode": "8a81220f90be712c0190be75a3850001"
            },
            {
                "fenixLoanAccountId": "FXLAN89677925",
                "status": "ACTIVE",
                "sanctionAmount": 20000000.00,
                "totalDrawingPower": 635732.09,
                "availableAmountForDisbursement": -4267.91,
                "currentOutstanding": 640000.00,
                "principalOutstandingAmount": 640000.00,
                "excessAmount": 0.00,
                "chargesDue": 0.00,
                "interestDue": 0.00,
                "penalChargesDue": 0.00,
                "sourcingChannelCode": "8a81220f90be712c0190be75a3850001"
            },
        ```
        
    - getAllChargeDetails API
        
        ```jsx
        [
            {
                "account_number": "000000030",
                "fenixLoanAccountId": "FXLAN97149399",
                "charge_id": "LF1",
                "Due Date": "2024-07-02 23:59:59",
                "charge_applied_date": "2024-07-02 23:59:59",
                "outstanding_amount": 400
            },
            {
                "account_number": "000000030",
                "fenixLoanAccountId": "FXLAN97149399",
                "charge_id": "PF1",
                "Due Date": "2024-07-04 23:59:5",
                "charge_applied_date": "2024-07-04 23:59:59",
                "outstanding_amount": 600
            },
            {
                "account_number": "000000030",
                "fenixLoanAccountId": "FXLAN97149399",
                "charge_id": "PF1",
                "Due Date": "2024-06-04 23:59:5",
                "charge_applied_date": "2024-06-04 23:59:59",
                "outstanding_amount": 200
            }
            
        ]
        ```
        
    - Logic of chargeDue calculation
        
        Assuming that the currently month is July and we are generating the mandate presentation file for 7th July mandate presentation 
        
        - According to loan summary API
            - Interest : 20000
            - Charges : 20000
        - According to getAllChargeDetails API
            - Charges which were posted between 1 & 7th
            = 400 + 600
            = 1000
        - Hence total charges to be collected from the customers 
        = 20,000 (getAllLoanSummary API) - 1,000 (getAllChargeDetails) 
        = 19,000
- We will expose a bulk due detail APIs for LSPs to get customers’ due details which they can use to power communications at their end.
    - Request
        
        Request of the API will be the end point of the API 
        
    - Response
        
        ```jsx
           {
                "fenixLoanAccountId": "FXLAN97149399",
                "chargesDue": 200000.00,
                "interestDue": 10000.00,
            },
            {
                "fenixLoanAccountId": "FXLAN89677925",
                "chargesDue": 0.00,
                "interestDue": 0.00,
        
            },
        ```
        
- Handling in dues collection communications
    - Types of comms -
        - Payment reminders
        - Auto-debit notification (1st and 2nd mandate)
        - Auto-debit status (success/failed)
        - Overdue
    - We will power all the comms with the new due details API

**Volt handling -** 

- During EOD sync job
    - Volt syncs the credits table with DSP loan details and summary API, additionally it also sync the interest collection table with the credits table
    - During the sync job when Volt detects an update in the charges due between DSP and Volt then it will additionally sync the interest collection table with the new due details API

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