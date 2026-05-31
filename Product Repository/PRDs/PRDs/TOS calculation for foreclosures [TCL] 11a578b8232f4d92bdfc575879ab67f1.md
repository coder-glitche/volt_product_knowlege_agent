# TOS calculation for foreclosures [TCL]

: Ameya Aglawe
Created time: December 3, 2024 4:40 PM
Status: In progress
Last edited: March 24, 2025 7:28 PM

# **What problem are we solving?**

For TCL, we are facing issues at the time of foreclosures due to incorrect foreclosure amount calculation at our end. 

---

# **How do we measure success?**

---

- Total number of foreclosure rejected for TCL will get reduced

# **How are others solving this problem?**

---

# **What is the solution?**

![Screenshot 2024-12-11 at 4.35.21 PM.png](TOS%20calculation%20for%20foreclosures%20%5BTCL%5D/Screenshot_2024-12-11_at_4.35.21_PM.png)

## Requirements overview (optional)

### User stories / User flow

Updated logic to calculate the foreclosure amount - 

- TOS/foreclosure amount = LoanAmount + InterestOutstanding+ ChargesOutstanding + (PenalInterestAccruedNotDue * 1.18) + InterestAccruedNotDue
    - All values will be rounded up
        - In case of PenalInterestAccruedNotDue → round up after multiplying PenalInterestAccruedNotDue with 1.18
- We get all these fields from TCL’s summary API
    - get Summary API response
        
        ```jsx
        {
          "retStatus": "SUCCESS",
          "sysErrorCode": "",
          "sysErrorMessage": "",
          "lasGetSummaryDataResponse": {
            "summary": [
              {
                "customerID": 13262,
                "loanAccount": [
                  {
                    "account_Number": 11538,
                    "loanAccountName": "Vyankatesh Vilas Bhandarkawathekar",
                    "product": "LAS",
                    "primary_Borrower": "Vyankatesh Vilas Bhandarkawathekar",
                    "accountOpening_Date": "5/29/2024 12:00:00 AM",
                    "accountExpiry_Date": "3/31/2050 12:00:00 AM",
                    "sanctionedLimit": 150000.00,
                    "drawingPower": 57091.64,
                    "principalOutstanding": 0.00,
                    "amountDue": 0.00,
                    "totalOutstanding": 0.00,
                    "amountAvailable_ForDisbursement": 57091.64,
                    "outstandingInterest": 0.00,
                    "outstandingCharges": 0.00,
                    "primaryHolder": "Vyankatesh Vilas Bhandarkawathekar",
                    "accountMaturityDate": "3/31/2050 12:00:00 AM",
                    "pledgeExpiry_Date": null,
                    "productCategory": "Loan Against Mutual Funds_Digital",
                    "primary_AccountHolder": "Vyankatesh Vilas Bhandarkawathekar",
                    "coborrowers": [],
                    "eCSApplicable": "No",
                    "address_Correspondence": "S/O Vilas Bhandarkawathekar, Vinayak Apartment Malivasti, S No 84/9A 9B/1 Bil No 1 Wing A Flat No18, Pandharpur, Solapur, Maharashtra",
                    "address_Office": "",
                    "agreementNo": "",
                    "accountStatus": "Active",
                    "pendingTDS": 0.00,
                    "eCSBankAccount": null,
                    "totalPortfolioValue": 206390.77,
                    "bankDetailsNonPOA": [],
                    "dPDetailsNonPOA": [],
                    "scheduleDetails": [
                      {
                        "loanNumber": 13909,
                        "loanType": "Term Loan",
                        "subType": "Short Term",
                        "purpose_of_Loan": "Personal",
                        "loanLimit": 150000.00,
                        "loanAmount": 0.00,
                        "interestRate": 10.49,
                        "loanMaturityDate": "5/29/2025 12:00:00 AM",
                        "interest_Outstanding": 0.00,
                        "chargesOutstanding": 0.00,
                        "reviewPeriod": "180 Days",
                        "interestType": "Floating",
                        "gracePeriod_Interest": 0,
                        "grace_Period_Principal": 7,
                        "overdueInterest": "Active",
                        "overduePrincipal": "InActive",
                        "principalFrequency": "Monthly",
                        "interest_Frequency": "Monthly",
                        "chargesPosting": "Daily",
                        "penalInterest": 0.00,
                        "penalRatePrincipal": 0.00,
                        "penalRateInterest": 25.51,
                        "amountDue_ForCustomer": 0.00,
                        "amountOverdue_ForCustomer": 469.95,
                        "interestAccruedNotDue": 469.95,
                        "penalInterestAccruedNotDue": 0.00
                      }
                    ],
                    "collateralEquity": [],
                    "collateralMutualFund": [
                      {
                        "lienMarkNo": 87925505,
                        "planID": 122640,
                        "schemeName": "Parag Parikh Flexi Cap Fund - Regular Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 122640,
                        "iSIN_Lien": "INF879O01019",
                        "lienQuantity": 415.1850,
                        "portfolioValue": 30200.5569,
                        "folioNo": 12926096,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 271875638,
                        "planID": 102875,
                        "schemeName": "Kotak-Small Cap Fund - Growth",
                        "option": "Growth",
                        "aMFI_Code": 102875,
                        "iSIN_Lien": "INF174K01211",
                        "lienQuantity": 113.1700,
                        "portfolioValue": 27302.2625,
                        "folioNo": 11074856,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 408929895,
                        "planID": 112932,
                        "schemeName": "Mirae Asset Large & Midcap Fund - Regular Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 112932,
                        "iSIN_Lien": "INF769K01101",
                        "lienQuantity": 187.4530,
                        "portfolioValue": 25726.0497,
                        "folioNo": 77760682705,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 1062740918,
                        "planID": 114564,
                        "schemeName": "Axis Midcap Fund - Regular Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 114564,
                        "iSIN_Lien": "INF846K01859",
                        "lienQuantity": 279.2490,
                        "portfolioValue": 28148.2992,
                        "folioNo": 910159898213,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 675880852,
                        "planID": 113177,
                        "schemeName": "Nippon India Small Cap Fund - Growth Plan - Growth Option",
                        "option": "Growth",
                        "aMFI_Code": 113177,
                        "iSIN_Lien": "INF204K01HY3",
                        "lienQuantity": 210.8410,
                        "portfolioValue": 33148.4220,
                        "folioNo": 477269906887,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 166784644,
                        "planID": 135800,
                        "schemeName": "Tata Digital India Fund-Direct Plan-Growth",
                        "option": "Growth",
                        "aMFI_Code": 135800,
                        "iSIN_Lien": "INF277K01Z77",
                        "lienQuantity": 204.8380,
                        "portfolioValue": 9834.2724,
                        "folioNo": 8440690,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 699417891,
                        "planID": 125354,
                        "schemeName": "Axis Small Cap Fund - Direct Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 125354,
                        "iSIN_Lien": "INF846K01K35",
                        "lienQuantity": 113.7420,
                        "portfolioValue": 11982.7197,
                        "folioNo": 910162184681,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 1173857128,
                        "planID": 119835,
                        "schemeName": "SBI Contra Fund - Direct Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 119835,
                        "iSIN_Lien": "INF200K01RA0",
                        "lienQuantity": 16.8350,
                        "portfolioValue": 6510.2629,
                        "folioNo": 32873423,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 1238409652,
                        "planID": 145208,
                        "schemeName": "Tata Small Cap Fund-Regular Plan-Growth",
                        "option": "Growth",
                        "aMFI_Code": 145208,
                        "iSIN_Lien": "INF277K015O2",
                        "lienQuantity": 147.4190,
                        "portfolioValue": 5284.9712,
                        "folioNo": 10339247,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 1826949261,
                        "planID": 120594,
                        "schemeName": "ICICI Prudential Technology Fund - Direct Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 120594,
                        "iSIN_Lien": "INF109K01Z48",
                        "lienQuantity": 24.1750,
                        "portfolioValue": 4556.9875,
                        "folioNo": 24043433,
                        "inTransitReleaseQty": 0.0000
                      },
                      {
                        "lienMarkNo": 116678945,
                        "planID": 122799,
                        "schemeName": "Quant Small Cap Fund - Direct Plan - Growth",
                        "option": "Growth",
                        "aMFI_Code": 122799,
                        "iSIN_Lien": "INF966L01158",
                        "lienQuantity": 35.0050,
                        "portfolioValue": 5487.9750,
                        "folioNo": 6749698975,
                        "inTransitReleaseQty": 0.0000
                      }
                    ],
                    "collateralFixedDeposit": []
                  }
                ]
              }
            ]
          }
        }
        
        ```
        
    - Field mapping
        
        ```jsx
        LoanAmount = "principalOutstanding"
        PenalInterestAccruedNotDue = "penalInterestAccruedNotDue" 
        InterestAccruedNotDue = "interestAccruedNotDue"
        Interest_Outstanding = "outstandingInterest"
        ChargesOutstanding = "outstandingCharges"
        ```
        

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

- Aadhar-PAN mismatch : Less than 70% then pass to credit referral
- KYC Photo verification : 70%
- CIBIL
    - CIBIL < 650
        - Hard reject
    - CIBIL > 650 ; Posidex negative
        - 002,
- PAN-Bank name : Less than 70% then pass to credit referral

BAJAJ : 90%

TATA : 70%, CIBIL < 650 

- Discussion with Nishant
1. Excess Margin during unpledging & Full closure unpledging issue at BAJAJ's end
2. All cases automate (with data) as suggested by tech about 10 tickets per day.
3. Seperate ticket for rejection in case there is a rejection after SLA breach? Or the same mail thread only
    1. Seperate ticket for rejection/approval 
4. Seperate SLA mail thread for credit referral at each step?
5. **Business hour rule?**
    1. TATA Ops business hours? 
        1. Time : (1st and 2nd Saturday leave,) 9-6
        2. Days 
    2. Holidays? - Arpit 
    3. Logic 
        1. Simple handling 
            1. If current time (when credit referral created) is within business hours → Send the credit referral case to TATA & initial the scheduler for SLA breach check right then 
            2. If current time outside business hours → Send the credit referral case to TATA & initial the scheduler for SLA breach check once the business hour starts 
        2. Extra handling 
            1. If current time + 2 hours is within business hours → then send the credit referral case to TATA initiate the scheduler 
            2. If current time is outside business hours → Send the credit referral cases when next business hour starts 
            3. If current time + 2 hours is outside business hours → Send the credit referral case to TATA, but start the scheduler when the next business hour starts 

- Deprioritised handling

| **Check Step**  | Change in handling | **Check**  | **Threshold** | **Actions** |  |
| --- | --- | --- | --- | --- | --- |
| KYC_Documents | Yes  | PAN-Aadhar name match score | 20 ≤match score ≤ 70 | - Straight through process  |  |
|  |  |  | match score <20 | - Through Volt Ops |  |
| KYC_Documents | No  | Photo match score  | match score <70  | - Through Volt Ops  |  |
| CIBIL_Check  | Yes  | CIBIL score  | < 650  | - Application blocked  |  |
|  |  | Posidex code  | Negative (CIBIL > 650)  | - Straight through process  |  |
| Bank Verification  | Yes  | PAN-bank name match score  | 20 ≤match score ≤ 70 | - Straight through process |  |
|  |  |  | match score < 20 | - Through Volt Ops  |  |
- Mail trigger/Zendesk ticketing system
    - Email trigger system
        - Logic
            
            
            | **Handling** | **Scenario**  | **Action**  |
            | --- | --- | --- |
            | STP  | Success | No mail zendesk ticket  |
            |  | Rejection Create zendesk ticket |  |
            |  | SLA breach (> 2 hours) & no callback [with business hour logic] | Create zendesk ticket |
            |  | SLA breached & approved later | Create zendesk ticket/Add top with “Success” in the same mail thread |
            |  | SLA breached & rejected later | Create zendesk ticket/Add top with “Rejected” in the same mail thread |
            | Through Volt Ops  | - | Create zendesk ticket, Ops will check & approve |
            |  | Approved | Create zendesk ticket/Add top with “Success” in the same mail thread |
            |  | Rejected | Create zendesk ticket/Add top with “Rejected” in the same mail thread |
        - Business hour logic
            - Business hours
                - Usual ⇒ Mon-Fri (9AM-6PM) with 2nd, 4th Saturday working
                - Holiday sheet to be shared by Arpit
            
            | **Time**  | **Action**  | SLA  |
            | --- | --- | --- |
            | If time at which credit referral created (T) is  within business hour  | Pass the credit referral to the lender  | T+2 hours  |
            | If time at which credit referral created (T) is outside business hour  | Pass the credit referral to the lender  | Time at which next business hour starts + 2 hours |
    - Email details
        - STP Success
            
            Email/Ticket is not required
            
        - STP SLA breach
            - Email header
                
                Credit referral SLA Breach - {Application ID} - {Customer Name}
                
            - Email template
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar name match percentage :
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    **{Attachments}**
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    **Details -** 
                    
                    Name as per Bank Account :
                    
                    Name as per PAN :
                    
                    PAN-Bank name match percentage : 
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    {Attachments}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    **Details -** 
                    
                    Photo match % : 
                    
                    {Attachments - Customer’s Photo & Aadhar Photo}
                    
                    </aside>
                    
                - For CIBIL/Posidex
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Details:
                    
                    Posidex negative : 
                    
                    CIBIL :
                    
                    **{Attachments}**
                    
                    </aside>
                    
        - STP rejections
            - Email header
                
                Credit referral rejected - {Application ID} - {Customer Name}
                
            - Email template
                - General email template
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Match percentage :
                    
                    Name as per Bank Account :
                    
                    Name as per PAN (%) :
                    
                    Name as per AADHAR (%) :
                    
                    Photo match % :
                    
                    Posidex : negative 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    The credit referral is rejected from the lender’s end.  
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar name match percentage :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Name as per Bank Account :
                    
                    Name as per PAN :
                    
                    PAN-Bank name match percentage : 
                    
                    Please follow up from the lender’s team to take this forward. 
                    
                    {Attachments}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Photo match % : 
                    
                    **{Attachments - Customer’s Photo & Aadhar Photo}**
                    
                    </aside>
                    
                - For CIBIL/Posidex
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    **Details -** 
                    
                    Posidex negative : 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
        - Through Ops : Zendesk ticket
            - Email header
                
                 Credit referral Pending Manual Review - {Application ID} - {Customer Name}
                
            - Email template
                - General email template
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason :
                    
                    Credit referral status : 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID : 
                    
                    Rejection reason :
                    
                    Details:
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Match percentage :
                    
                    Name as per Bank Account :
                    
                    Name as per PAN (%) :
                    
                    Name as per AADHAR (%) :
                    
                    Photo match % :
                    
                    Posidex : negative 
                    
                    CIBIL :
                    
                    {Attachments}
                    
                    </aside>
                    
                - For PAN-Aadhar name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Aadhar match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    PAN-Aadhar match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For PAN-Bank name mismatch
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : PAN-Bank name match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Name as per PAN :
                    
                    Name as per AADHAR :
                    
                    Name as per Bank Account :
                    
                    PAN-Aadhar match percentage : 
                    
                    PAN-Bank match percentage : 
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For Photo verification
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Photo match score < 70%
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Photo match % :
                    
                    {Attachments - Customer’s Photo & Aadhar Photo}
                    
                    </aside>
                    
                - For Posidex negative
                    
                    <aside>
                    💡
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : Posidex negative 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Posidex : negative
                    
                    CIBIL score :
                    
                    {Attachments - including user’s attached documents}
                    
                    </aside>
                    
                - For CIBIL < 650
                    
                    <aside>
                    💡
                    
                    We are rejecting this application. 
                    
                    Customer name :
                    
                    Customer PAN :
                    
                    Application ID :
                    
                    Application type :
                    
                    Credit referral reason : CIBIL Score < 650 
                    
                    Webtop ID :
                    
                    Opportunity ID :
                    
                    Credit referral ID :
                    
                    **Details -** 
                    
                    Posidex : 
                    
                    CIBIL score :
                    
                    {Attachments}
                    
                    </aside>
                    
- Credit referral request/response
    
    **Request :** 
    
    ```jsx
    {
        "LeadId": "226344635",
        "RefId": "2244940402952849110",
        "applSource": "LAS",
        "assignTo": "CM",
        "stage": "4",
        "stagedescription": "OKYC name mismatch",
        "webtopId": "291BZ8640463"
    }
    ```
    
    **Response :** 
    
    ```jsx
    {
        "Assign_Case_Response": {
            "Status": "Success",
            "Message": "Case has been assigned to CM",
            "LeadId": "226344635",
            "RefID": "2244940402952849110"
        },
        "RetStatus": "SUCCESS",
        "sysErrorMessage": "null",
        "sysErrorCode": "null"
    }
    ```
    
    **Callback :** 
    
    ```jsx
    {
      "applSource": "LAS",
      "leadId": "228204425",
      "managerDecision": "Rejected",
      "refId": "5688102400937952287",
      "stage": "3",
      "stageDescription": "Application has been recommended for Credit approval .Dedupe is negative",
      "webtopId": "291BZ8646200"
    }
    ```
    

- Update customer details
    - In our system
    - In TATA system