# Interest calculator - landing page

: Saksham Srivastava
Created time: April 8, 2024 1:38 PM
Status: In progress
Last edited: October 9, 2024 8:22 PM
Owner: Saksham Srivastava

# **What problem are we solving?**

1. Before applying for Volt LAMF or withdrawals users want an estimate of what is the interest that they will pay.
2. Since alot of user consider Volt LAMF as term loan, they want to get an understanding of how to close the loan in X duration with equal monthly payments. MFDs are asked this query alot as well. 

---

# **How do we measure success?**

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

1. When user visits the landing page, default value should be filled along with it’s calculation. Following is the default value:
    1. Loan amount: ₹1,00,000
    2. Annual interest rate: 10.49%
    3. Repayment duration: 1 year
2. When user switches repayment duration toggle between day, month and year. Switch to these default values:
    1. Days: 180 Days
    2. Month: 6 months
    3. Year: 1 Year
3. Since calculation is on per day basis, when user selects repayment duration in:
    1. Months: Calculate number of days between today and same date X months ahead. Examples: 
        1. Today is 15th April, if a user selects 6 months: Days until 15th October should be selected: 183 Days. 
        2. Today is 31st May, if a user selects 6 months: Since November 31st doesn’t exist use last date of that month (30th November) for calculation: 183 Days.
    2. Years: Calculate number of days between today and same date X years ahead. 
        1. For leap year count 366 days.
        2. Today is 29th Feb 2024, if a user selects 1 year: Since 29th Feb 2025 doesn’t exist use 28th Feb 2025 for calculation. 
4. When user enters repayment duration less than 30 days,
    1. User will not see an interest only EMI
    2. User will not see a repayment examples
    3. User will see only total interest, daily interest. 
    [https://www.figma.com/file/FdWIeAxDVF6yweOXvjndsL/Website?type=design&node-id=300-1614&mode=design&t=Uxk8bt9f9BPNRC52-11](https://www.figma.com/file/FdWIeAxDVF6yweOXvjndsL/Website?type=design&node-id=300-1614&mode=design&t=Uxk8bt9f9BPNRC52-11)
5. User should not be able to enter 0 interest rate.
6. User should not be able to enter 0 in Repayment duration.
7. User should not be able enter amount more than 5cr. 
8. User should not be able to enter interest percentage more than 100%.
9. User should not be able to enter repayment duration more than.
    1. Days: 1825 days.
    2. Months: 60 months
    3. Years: 5 years
10. User should see “Interest-only EMI” card. Clicking on “Learn more” will open a bottom sheet in mweb and a popup in desktop web.
11. Users should see two repayment options as cards, clicking on “View full repayment schedule” should open the repayment schedule as a screen on mweb and as a popup overlay in desktop web. 
12. User should be able to horizontally scroll the table. 
13. When user clicks on Download PDF, user should be able to download repayment schedule with Volt logo, and disclaimer. 
14. When user clicks on “Know how Volt is better than a loan” the user should jumpscroll to a section explaining this. Text: Pending
15. Users will have a check eligibility entry point for desktop web. 
16. When user fills phone + PAN  and clicks on “Check eligibility for free” user will be redirected to MFC check eligibility with fetch already initiated. 
17. User should see FAQs below the calculator interface. Content: Pending
18. User should see relevant text material on how LAMF works, how LAMF interest is calculated, etc. SEO text: Pending

## Requirements

1. Interest calculator landing page.
2. Interest calculator entry point in website header.
3. Interest calculator entry point in MFD dashboard. 
4. A config to maintain what are the default input values that will be shown. 
5. Calculation logics to be built. 
6. App should have an entry point for this calculator as well. 
7. Should use style guide for this page as well.
8. Share PDF. 

Calculation logic: /https://docs.google.com/spreadsheets/d/1mPhqqJmpOEVbfBKHtG_tBCYjRpaE69S4YwyRWJVX9Qg/edit?usp=sharing

[Other copies for landing page](Interest%20calculator%20-%20landing%20page/Other%20copies%20for%20landing%20page%2004f8b4c06551465e8967195ad4630c7e.md)

---

# **Design**

- Requirements (old)
    1. Calculator interface 
    Heading: Volt Money’s interest calculator 
        1. User input:
        Amount: Default 1,00,000
        Interest: Default 10.49%
        Tenure: 6M, 9M, 12M. (This can be a slider as well between 1 month to 12 months)
        2. Repayment details:
        Volt Money’s Loan against mutual fund works like an overdraft facility. 
        Interest repayment: 
        Per month interest (Avg): ₹859.83. 
             Per day interest: ₹28.66 (Interest is calculated daily and deducted monthly on a specific date, above calculation shows per month interest only EMI for 30 days)
        Principal Repayment:
        Flexible: Only interest is paid every month, pay principal whenever it suits you. 
        Zero pre-payment charges: No foreclosure or Pre-payment charges on Volt.
        3. Estimate interest:
        Two options will be give Pay principal once, Pay principal monthly.
            1. Pay principal at end: 
            
            | Month | Interest(payed automatically) | Principal (To be payed manually through app) | Total payment from user |
            | --- | --- | --- | --- |
            | April | ₹873 | ₹0 | ₹873 |
            | May | ₹873 | ₹0 | ₹873 |
            | June | ₹873 | ₹0 | ₹873 |
            | July | ₹873 | ₹0 | ₹873 |
            | August | ₹873 | ₹0 | ₹873 |
            | September | ₹873 | ₹1,00,000 | ₹1,00,000 |
            | Total  | ₹6,111 | ₹1,00,000 | ₹1,06,111 |
            
            ii. Pay principal monthly:
            
            Data will be something like this 
            
            ![Screenshot 2024-04-08 at 8.55.35 AM.png](Interest%20calculator%20-%20landing%20page/Screenshot_2024-04-08_at_8.55.35_AM.png)
            
            | Month | Interest(payed automatically) | Principal (To be payed manually through app) | Total payment from user |
            | --- | --- | --- | --- |
            | April | ₹873 | ₹0 | ₹873 |
            | May | ₹873 | ₹0 | ₹873 |
            | June | ₹873 | ₹0 | ₹873 |
            | July | ₹873 | ₹0 | ₹873 |
            | August | ₹873 | ₹0 | ₹873 |
            | September | ₹873 | ₹1,00,000 | ₹1,00,873 |
            | October |  |  |  |
            | November |  |  |  |
            | December |  |  |  |
            | January |  |  |  |
            | Feb |  |  |  |
            | March |  |  |  |
    2. Volt’s loan against mutual funds vs Personal Loan vs Auto loan
        
        
        |  | Volt | Personal loan | Auto loan |
        | --- | --- | --- | --- |
        | Interest rate | 10.49% | ~20% | ~10% |
        | Processing fee | ₹999+GST | 1%-3%  | 1%-3%  |
        | Interest type | Reducing | Fixed | Reducing |
        | Prepayment/Foreclosure charges | ZERO |  |  |
        | Repayment |  |  |  |
        | Tenure |  |  |  |
    3. How Volt Money’s interest calculator works?
    4. Why is Overdraft better than a loan?
- Design link
    
    [https://www.figma.com/file/FdWIeAxDVF6yweOXvjndsL/Website?type=design&node-id=252-1304&mode=design&t=Uxk8bt9f9BPNRC52-11](https://www.figma.com/file/FdWIeAxDVF6yweOXvjndsL/Website?type=design&node-id=252-1304&mode=design&t=Uxk8bt9f9BPNRC52-11)
    

---

# **Analytics**

Amplitude events: To be added. 

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

- Use cases
    
    ## Use cases
    
    Kapil
    
    - Reducing vs Flat interest rate
    - Comparison with different kind of loans
    - Flexibility and benefits of OD
    
    ![WhatsApp Image 2024-04-10 at 3.09.45 PM.jpeg](Interest%20calculator%20-%20landing%20page/WhatsApp_Image_2024-04-10_at_3.09.45_PM.jpeg)
    
    Swara
    
    - Users ask 2-3 days after repayment on what will be the interest due from this point on.
    - MFDs need calculations on what will the effect on interest once repayment is done on a particular date.
    
    Khusboo
    
    - During process, per day calculation and calculation as per withdrawal. Month wise kitna ja rha hai.
    - Sanction limit pe calculation happens, for 3 years is shown.
    - KFS and agreement. Want to understand what is the EMI. This is just for understanding
    - After Repayment what is the interest use case is minimal.
    - After checking the limit show in the journey
    - Below is the calculation that is used to make user understand currently.
    
    ![Screenshot 2024-04-08 at 8.55.35 AM.png](Interest%20calculator%20-%20landing%20page/Screenshot_2024-04-08_at_8.55.35_AM.png)
    
    Sandeep
    
    - Sandeep, thinks while journey the queries will increase: After completing the application user should see. Most users query after the application process is complete.
    - Bajaj case, if withdrawn after 10th interest posting happens in T+2 month. In this case what happens when the user repays full principal during this time?
    
    Amrit
    
    - Before starting the application, mahine ka kitna interest lagega
    - Market comparison: Mirae etc reducing interest and flat interest.
    - Interest per annum but growth as well will always be in surplus.
    - I will pay principal of 5000 per month what will be the
    - For MFDs to convince clients.
    
- User calling
    - User calling for interest calculator
        - Ankit Anand, user: He was thinking “Abhi interest schedule ka clarity milega, Abhi mileage” but he didn’t get that clarity in the journey. Was expecting that after he selects the amount he would be getting 2 details on how much interest will he have to pay. Recommends that we ask the user to enter for how much time the user need the money and give two details:
        1. How much will be the total interest charged?
        2. When will that interest be deducted?
        He also asked for understanding of “Split of principal and interest” that will be deducted. Many users see this as a loan and not OD, so they want a repayment schedule of Principal and Interest. 
        Want us to be completely “Transparent” with the interest schedule. Really likes the information given by groww.
        - Prateek Daftari, user: Browsing loans. Has no relevant question about interest, is an informed user wanted to understand if we could give fixed interest as lenders keep the fixed interest lower and reducing interest is high.
        - Vikas Sachdevnani, user: LLA referee, wants loan for working capital. Has no relevant doubts about interest, said “easy hai”
        - Avinash Sehgal, user: LLA user, completed application. No doubts regarding interest.
        - Dhirendra Kumar Singh, MFD: Users “sometimes” as questions like how interest will be deducted, he uses Credit card analogy where “30 ko bill generate Hota hai and 7th ko pay hota hai”. This also he said after asking specifically about do users actually ask this. 
        Asked if he uses interest rate point to compare between different type of loans, said No. He just uses the point of using Mutual funds for credit line.
        - Subrata Sarkar, MFD: User’s ask monthly “EMI kitna hoga” then MFD says that only interest will be deducted per month. They they ask if they deposit 50k 3 months later and then deposit 30k 5 months later how will the interest change. Also, the user asks they want to repay in 1 year what will be the Principal + interest instalment. All these questions users ask before starting the application.
        - Nagarajan Santhan, MFD: Has 3 clients. No question regarding interest rates. They already knew about LAMF.
1. Monthly schedule (accurate) can only be shown when the lender is finalised. Before that happens we can not show the exact monthly schedule.
2. PF and other charges should be shown in the interest schedule because it might lead to more escalations when charges like PF are cut in the first month. 
3. [https://www.calculate.lk/calculators/od-calculator](https://www.calculate.lk/calculators/od-calculator)
4. [https://upwards.in/personal-loan-overdraft-calculator](https://upwards.in/personal-loan-overdraft-calculator)
- Feedback
    - Design Feedback - 24th April
        - Ankit
            - The design is too complicated, there are too many numbers.
            - Can we reduce numbers by showing a pill to switch between regular principal payment and interest only payment.
            - Show 2 key numbers as result of calculation, highlight them more.
        - Khushboo and Sandeep
            - Looks good and easy to understand.
        - Amrit
            - Can we show that while you payed X interest, your MF also appreciated by 1.3X?: Not sure how can this be integrated in the story of a calculator, this can work in regret calculator.
            - Why are we trying to reduce interest for the user?: This is just to show how much flexibility we are offering
            - Interest rate for MFDs in 9.99%. The callout below interest rate will be confusing.
            - Looks good, will be helpful for MFDs.
        - Rahul
            - Interest rates are more for few partners, clear Volt interest rate callout will create a problem.
            - Download can create problem as the user might comeup and say why is more or less interest deducted. Can this be made into a feature but they can request us for PDF?
            - Data looks clean, clear understanding will be given to the user.
        - Nishant
            - The story in repayment schedule numbers is not clear, club them.
            - Remove Download option.
    - Ankit feedback -
    - Lalit’s review
        
        For less than 30 days the UI will be different. 
        
- Repayment schedule benchmark
    - Cred
        
        ![IMG_9610.png](Interest%20calculator%20-%20landing%20page/IMG_9610.png)
        
        ![IMG_9612.png](Interest%20calculator%20-%20landing%20page/IMG_9612.png)
        
        ![IMG_9611.png](Interest%20calculator%20-%20landing%20page/IMG_9611.png)
        
    - Groww
        
        ![IMG_9613.png](Interest%20calculator%20-%20landing%20page/IMG_9613.png)
        
- SEO text benchmarking: Searched interest calculator and benchmarked the top results
    - Cleartax: Simple questions like What is Simple interest? What is a simple interest calculator? Followed by a short FAQ section.
    - Groww: Similar as above, shows formulas as well.
    - [calculator.net](http://calculator.net): Technical definitions, calculations including graphs and examples.
    - Bajaj Finserv: Similar to cleartax and groww.
    -