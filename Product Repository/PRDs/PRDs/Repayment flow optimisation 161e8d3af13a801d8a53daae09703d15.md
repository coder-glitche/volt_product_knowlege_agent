# Repayment flow optimisation

: Ranjan kumar Singh
Created time: December 19, 2024 2:17 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

---

- When users repay amounts through the FlexiPay flow, the repayment is allocated towards charges (when due) and interest repayment (when due) for TCL and DSP customers. However, users are not explicitly informed about how their repayment is distributed across charges, interest, and principal, leading to confusion after payment completion.
    - The interest amount and status are not updated if the repayment is made through the FlexiPay flow.
    - Users are not informed that auto-debit will still be executed if repayment is made between the 1st of the month and the due date. Since the amount is first settled against charges and interest, and then the POS (principal outstanding), users are confused when the POS amount is not updated to reflect the repayment made.
    - Partial settlement of interest and charges are not handled.
- When customers are in shortfall and repay the principal through the FlexiPay flow, we do not inform them to pay the minimum amount required to clear the shortfall.
    - The current shortfall flow involves numerous clicks and pages, making it overwhelming for users who are already aware of the shortfall concept.
    - The operations team is facing challenges in prioritizing repayment accounting when BFL customers are in shortfall.
- The FlexiPay flow does not have the handling virtual account for TCL and DSP

---

# **How do we measure success?**

- CX queries regarding repayment allocation for lenders TCL and DSP should decrease significantly.
- Instances of portfolio sell-offs due to delayed repayment accounting, especially when users are in shortfall, should be minimized.
- Users should be able to repay their due amounts seamlessly, even when the payment gateway is down or if the amount is large.

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

- We want to generalise the FlexiPay flow for all type of repayment.
- Show clear bifurcation of due amount i.e principal, interest and charges
- Nudge user to repayment min amount which are required to meet the shortfall and mark collection as SHORTFALL_REPAYMENT when user are in shortfall and made payment through FlexiPay.
- SYNC interest collection table with EOD to update the due amount
- When user are in shortfall and user repaid principal amount then repayment collection type should be SHORTFALL_REPAYMENT  - This needs to be done only for BFL
- When interest and charges are due, and user does repayment then invoke  lender API like getsummary(TATA) in background to sync the credit and if interest and charges are updated in API then update the interest collection table [Due amount and status].

TCL virtual account requirement:

- Virtual account for interest repayment and principal repayment are same
- LOAN NUMBER = lender_loan_account_number (in our credit table)

![Screenshot 2025-01-03 at 3.53.21 PM.png](Repayment%20flow%20optimisation/Screenshot_2025-01-03_at_3.53.21_PM.png)

DSP virtual account requirement:

- Pending on lender

## User stories / User flow

## Requirements

## TCL and DSP

Case 1: When only principal is due

- Since TCL follows the CIP apportionment logic, repayment done will be accounted based on apportionment logic only.
- User should be able to see Principal outstanding amount when user enters the repayment amount
- User should be able to see the repayment summary, repayment allocation and method  by which they are willing to choose for repayment
    - Repayment method :
        - PG  - Already exist
        - NEFT/RTGS(VA) - Need to implement VA for TCL and DSP
            - We will get Webhook in DSP if repayment done through the VA and we should be able to create collections and repayment status made through the Virtual account.
- In TCL, Virtual account for Principal repayment and interest repayment are same.
    - We have VA of TCL but for DSP its still pending at the lender end [ETA: (TBD)]

Case 2: When interest and principal are due

- In this case, although TCL follows the CIP modal we will given option of Interest + charges and principal options to choose.
- If user choose to repay principal and interest+charges are still due, we need to show allocation of repayment on summary page.

Case 3: When interest and principal are not due

- Repay button should be enable with feedback to user that No amount is due for repayment

Case 4: When charges are due

- Give option to user whether they want to repay charges or principal
- If user choose to repay charges, take user to interest/charges collection flow
- If user choose to repay principal, take user to amount selection page of FlexiPay flow and show repayment allocation on summary page

Case 5: When user are in shortfall

- When user click on repay button, take user to the FelxiPay flow, show nudge user to repay min shortfall amount.

Case 6: When loan is expired

- TBD

- Principal repayment done on 1st of the month when Interest of amount 133 was due
    
    ![Screenshot 2024-12-21 at 1.19.00 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_1.19.00_PM.png)
    
    ![Screenshot 2024-12-21 at 1.19.25 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_1.19.25_PM.png)
    

- Principal repayment done on 2nd got adjusted with interest but mandate was hit to auto-debit the interest and debited amount got settled with Principal
    
    ![Screenshot 2024-12-21 at 1.32.47 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_1.32.47_PM.png)
    
    ![Screenshot 2024-12-21 at 1.35.02 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_1.35.02_PM.png)
    

## BFL

Case 1: When only principal is due

- User should be able to repay their principal amount only
- User should be able to see Principal outstanding amount when user enters the repayment amount
- User should be able to see the repayment summary and method  by which they are willing to choose for repayment
    - Repayment method : VIA PG and NEFT/RTGS(VA)
- In BFL, Virtual account for Principal repayment and interest repayment are separate - this feature is already live on prod

Case 2: When interest and principal are due

- When user click on repay button given option to user what they want to pay i.e Interest or Principal based on below condition
    - When user will see the interest selection option?
        - Interest is due and mandate is not registered
            - User should be able to see due date and due amount
            - When user choose to repay interest amount, upon selection take user to the interest collection flow
        - Interest is overdue and mandate is registered
            - User should be communicated that interest is overdue and last date of repayment amount to avoid defaulting
            - When user choose to repay interest amount, upon selection take user to the interest collection flow
        - Interest is overdue and mandate is not registered

Case 3: When interest and principal are not due

- Repay button should be enable with feedback to user that No amount is due for repayment

Case 4: When charges are due

- *Charges are collected at time of withdrawal or foreclosure*

Case 5: When user are in shortfall

- If user choose to repay through flexiPay, show min amount payable to meet the shortfall
- Repayment Collection type will be shortfall regardless of the repayment amount if user repays principal through the FlexiPay flow when user are in shortfall

Case 6: When loan is expired

- User has to repay net outstanding due [POS+Interest due + interest accured+ charges due + penal charges - excess]

- Interest repayment done on 3rd of the month got accounted as a advance interest and got adjusted on 7th as interest and hence mandate was not presented.
    
    ![Screenshot 2024-12-21 at 2.44.27 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_2.44.27_PM.png)
    
    ![Screenshot 2024-12-21 at 2.45.19 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_2.45.19_PM.png)
    
- If loan account was opened after 15th of the month and disbursal was made in same month then interest will be due in M+2 month [EX: Account opening date = 21 Dec, withdrawal date = 22 Dec then interest due will be in Feb]
    
    ![Screenshot 2024-12-21 at 2.58.55 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_2.58.55_PM.png)
    
- Interest amount paid on interest due gets accounted and presentation of the mandate do not happen
    
    ![Screenshot 2024-12-21 at 3.57.01 PM.png](Repayment%20flow%20optimisation/Screenshot_2024-12-21_at_3.57.01_PM.png)
    

---

- **Design**
    
    Bajaj :
    
    [https://www.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=1002-12041&t=jY8BOdQBxhk36Yr7-11](https://www.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=1002-12041&t=jY8BOdQBxhk36Yr7-11)
    
    TATA :
    
    [https://www.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=1006-21188&t=jY8BOdQBxhk36Yr7-11](https://www.figma.com/design/axnRcEvkbu75kd0uaWsF9B/Repayment-flow?node-id=1006-21188&t=jY8BOdQBxhk36Yr7-11)
    

---

# **Analytics**

Amplitude events: 

| Journey | Event name | Event property | Expected value |
| --- | --- | --- | --- |
| User lands on amount selection page and select full and partial options | REPAYMENT_AMOUNT_SELECTED_BUTTON_CLICKED | Already exist | Already exist |
| When users land on the repayment summary page - Confirm & pay | CONFIRM_AND_PAY_PAGE_VIEWD | source | principal/interest/shortfall |
| When user select the payment method on the Confirm & Pay page | PAYMENT_MODE_SELECTED | mode | online/bank_transfer |
| Repayment success | REPAYMENT_SUCCESS_PAGE_VIEWED |  |  |

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
    - [ ]  Apportment override
    - [ ]  Effort to implement override is 1 week
    - [ ]  Need to close with Nishant that override is required or not
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

3 Jan 

- Fix interest journey
- Fix copy of interest repayment - Your auto-debit is setup for 7th do you still want to repay
-