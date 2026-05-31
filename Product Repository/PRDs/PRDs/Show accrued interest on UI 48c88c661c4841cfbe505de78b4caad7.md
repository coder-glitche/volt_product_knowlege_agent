# Show accrued interest on UI

: Vaibhav Arora
Created time: June 3, 2024 8:26 AM
Status: Not started
Last edited: December 26, 2024 5:50 PM
Assignee: Vaibhav Arora

# **What problem are we solving?**

- Users are not able to track their interest before the due date of their interest cycle
    - Users are not able to plan their withdrawals and repayments basis accrued interest on their line (it is an important decision making parameter for them)
    - Ops team estimates this basis the current POS of the user and gives approximate answers
    - Users also like to estimate their monthly interest basis accrued interest and current POS and are currently not able to do it to resolve their queries

![Screenshot 2024-05-30 at 5.13.21 PM.png](Show%20accrued%20interest%20on%20UI/Screenshot_2024-05-30_at_5.13.21_PM.png)

![Screenshot 2024-05-30 at 5.10.06 PM.png](Show%20accrued%20interest%20on%20UI/Screenshot_2024-05-30_at_5.10.06_PM.png)

---

# **How do we measure success?**

Queries across customer support fronts related to accrued interest should reduce

---

# **How are others solving this problem?**

![Untitled](Show%20accrued%20interest%20on%20UI/Untitled.png)

![Untitled](Show%20accrued%20interest%20on%20UI/Untitled%201.png)

---

# **What is the solution?**

Users will be able to track the accrued interest accumulated over the month on the dashboard

## Requirements overview (optional)

Users will be shown the accrued interest on UI and they will be able to expand the callout to check the following details:

- Un-billed interest till today (Foreclosure API)
- Next due date (Get statement API)
- Estimated interest (Current date to end of month date) (interest per day at current POS*(End of month date - Current date +1)
- Other loan details as per design
- Deep link of loan details page

When to show my loan CTA :

- Approved not disbursed and Active state

Deeplink of loan details page

Sample API responses with key value pairs:

- getStatement
    
    INFO NonStaticHttpUtility RRId= RId=5c8d9e77-603d-4409-8f1a-8fa8cde4ab1e, CreditId=8a804bcd8ff6fe53018ff8292a9f0d54, UId= - got a response with status 200, and body {"ClientStatement":[{"LoanAccountName":"MOHITKUMAR  DUDESHWAR PATLE","LoanAccountNo":"183770","LoanContractNo":"V402ALAS00164299","Product":"ALAS","ContractStartDate":"10-Jun-2024","ContractEndDate":"31-May-2027","Tenure":"36 Months","ContractStatus":"Active","Address":"at po paudadauna tah, salekasa Paol Dawana, Gondiya Maharashtra, GONDIYA, 441916","ContractClosureDate":null,"SanctionedLimit":101000.0,"PrincipalOutstanding":40000.0,"AnnualizedInterestRate":"10.49%","InterestPostingFrequency":"Monthly","InterestOutstanding":0.0,"PenalInterest":0.0,"BounceCharges":0.0,"DPCharges":0.0,"ExcessAmount":0.0,"FirstInterestDueDate":"07-Jul-2024","NextIntrestDueDate":"07-Aug-2024","LastRenewalDueDate":null,"InterestSlabDetail":[],"TransactionDetail":[{"ValueDate":"10-Jun-2024","Particulars":"Opening Balance","DebitAmount":0.0,"CreditAmount":0.0},{"ValueDate":"10-Jun-2024","Particulars":"Loan Schedule Approval Posting Of One Time Charges against PROCESSING FEES ALAS 1 For Loan No V402ALAS00164299 For Day 2024-06-10","DebitAmount":1179.0,"CreditAmount":0.0},{"ValueDate":"10-Jun-2024","Particulars":"Loan amount disbursed for loan No:V402ALAS00164299 - By N162243085640413","DebitAmount":40000.0,"CreditAmount":0.0},{"ValueDate":"10-Jun-2024","Particulars":"Charges Posting for LAS - V402ALAS00164299 Loan Account=MOHITKUMAR  DUDESHWAR PATLE - By N162243085640413","DebitAmount":0.0,"CreditAmount":1179.0},{"ValueDate":"07-Jul-2024","Particulars":"Interest for the period 10/06/2024 - 30/06/2024 for loan No:V402ALAS00164299","DebitAmount":241.0,"CreditAmount":0.0},{"ValueDate":"07-Jul-2024","Particulars":"AP Interest Posting For Loan Account - 183770 and LoanNo - V402ALAS00164299","DebitAmount":0.0,"CreditAmount":241.0}],"OtherContractLevelSummary":[{"LoanContractNo":"V402ALAS00164299","SanctionedLimit":101000.0,"LoanAmount":40000.0,"AnnualizedInterestRate":10.49,"LoanMaturityDate":"31-May-2027","InterestOutstanding":0.0,"ChargesOutstanding":0.0}]}],"PDFdata":null,"status":{"Status":"Success","Code":"01","Remarks":""}}
    
- Foreclosure
    
    CreditManagementServicev2/volt-creditmanagementservice/e9689d28e8b04e638b603c00b10149a2
    @message	
    INFO BajajLMSConnector RRId= RId=c1c6ffbe-cb16-4eea-91fa-f3ef896704bd, CreditId=8a804bcd8ff6fe53018ff8292a9f0d54, UId= - got foreclosure statement response for fas-number V402ALAS00164299, response GetForeClosureStatementResponse(data=[ForeClosureData(asOnForeclosureDate=15th July 2024, loanAccountName=MOHITKUMAR  DUDESHWAR PATLE, address=at po paudadauna tah, salekasa Paol Dawana, Gondiya Maharashtra, GONDIYA, 441916, loanAccNo=183770, loanContractNo=V402ALAS00164299, outstandingPrincipal=40000.00, outstandingInterest=0.00, outstandingCharges=0.00, interestAccruedNotDue=160.44, penalInterestReceivable=0.00, penalInterestAccruedNotDue=0.00, tDSReceivable=0.00, totalNotionalChargesAndDematBounce=0.00, prepaymentCharges=0.00, interestOnClosureDate=0.00, penalInterestOnClosureDate=0.00, totalDue=40160.44, advanceInterest=0.00, excessMargin=0.00, totalCredit=0.00, netPayable=40160.44, payableForNext7Days=[PayableForNext7Day(day1ClosureDate=16-Jul-2024, day1ClosureAmount=40171.90, day2ClosureDate=17-Jul-2024, day2ClosureAmount=40183.36, day3ClosureDate=18-Jul-2024, day3ClosureAmount=40194.82, day4ClosureDate=19-Jul-2024, day4ClosureAmount=40206.28, day5ClosureDate=20-Jul-2024, day5ClosureAmount=40217.74, day6ClosureDate=21-Jul-2024, day6ClosureAmount=40229.20, day7ClosureDate=22-Jul-2024, day7ClosureAmount=40240.66)], lenderResponseCode=null)], PDFdata=null)
    

## User stories / User flow

## Requirements

---

# **Design**

https://www.figma.com/design/4gwGZhe8iBeWtzd0GsZQfd/Interest?node-id=2061-1762&t=ba9Ia4XsAzm5mTsZ-4

---

# **Analytics**

Amplitude events

| Journey | Event name |  |
| --- | --- | --- |
| When user click on My loan details button | LOAN_DETAILS_BUTTON_CLICKED |  |
| When user lands on loan deatils page | LOAN_DETAILS_PAGE_VIEWED |  |

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