# Interest, shortfall, renewal table on partner dashboard

: Ranjan kumar Singh
Created time: May 3, 2024 8:56 AM
Status: In progress
Last edited: February 19, 2026 7:14 PM
Owner: Lalit Bihani

# **What problem are we solving?**

- MFDs lack visibility regarding their customers' interest details, shortfall occurrences, and loan status.
    - MFDs inquire about the interest status, mandate status and interest calculation.
    - MFDs do not inform their customers about the shortfall, resulting in escalation from the customer's end.
- B2B2C customers depend on advisors to oversee their loan accounts, resulting in reduced attention to direct reminders sent by Volt.

---

# **How do we measure success?**

- Timely repayment of interest, outbound reminder calls should be reduced.
- Outbound calls and inbound queries related to shortfall should be reduced.
- Portfolio sell-off should be reduced.
- loan renewals should be increased before the loan expires.

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview

- Table for current month due interest and charges details with status
    - Filtering: Allow to filter table by mandate status, interest status and lender name
        - Interest = Status Overdue  > Due (Due date) > Collection failed > settled
        - Mandate = Not registered > Registered
        - Lender name = TATA, BAJAJ
    - Search: User should be able to search interest table
    - Education: Interest calculator
    - WA pre-defined message based on interest status and mandate status:
        - Interest status is due and mandate is registered:
            
            `Dear {Customer Name},`
            
            `Total due amount for {due_interest_month} is ₹{due_amount} for your Volt Money credit line account.Please ensure your bank account has enough funds for the automatic payment.`
            
            `For more detail please visit Volt Money app: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
            
            `Warm regards,`
            
            `{Partner name}`
            
        - Interest status is due and mandate is not registered:
            
            `Dear {Customer Name},`
            
            `Total due amount for {due_interest_month} is ₹{due_amount} for your Volt Money credit line account. Please pay due amount on the Volt Money App.`
            
            `App link: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
            
            `Warm regards,`
            
            `{Partner name}`
            
            - Interest status is overdue
                
                `Dear {customername},`
                
                `Payment of ₹{due_amount} for your Volt Money credit line is overdue. To avoid defaulting, pay now using the Volt Money app.`
                
                `App link: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
                
                `If you have already paid, please ignore this message.`
                
                `Warm regards,`
                
                `{Partner name}`
                
    - Pagination [50 records per page]
- Table for shortfall amount with aging
    - Sorting: Sort table by due date (Low to High)
    - Filtering: Aging, Lender name
    - Search: User should be able to search shortfall table
    - Education: What is shortfall?
    - WA pre-defined message:
        - `Dear {customername},`
        
        `Your Volt Money credit line account is currently in shortfall due to a decrease in the market value of your pledged portfolio.`
        
         ``
        
        `Shortfall amount: {shortfall_amount}`
        
        `Due date: {shortfall_due_date}`
        
        `Please make a payment to cover the shortfall amount or pledge additional portfolio via the Volt Money app.`
        
        `App link: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
        
        `If you have already paid, please ignore this message.`
        
        `Warm regards,`
        
        `{Partner name}`
        
    - Pagination [50 records per page]
- Table for loan renewals
    - Search: User should be able to search shortfall table
    - Filter: lender name, status
    - Education: Benefits of loan renewal
    - WA pre-defined message based on loan status:
        - Loan status = Active
            - `Dear {customername},`
            - 
                
                `Your Volt Money credit line account is due for renewal.` 
                
                `To continue enjoying the benefits of credit line, Please renew your credit line account via Volt Money app.`
                
                `App link: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
                
                `Note: If you do not wish to continue your credit line account, please settle any outstanding amount before your account expires.`
                
                `If you have already renewed, please ignore this message.`
                
            
            `Warm regards,`
            
            `{Partner name}`
            
        - Loan status = Expired && outstanding is not ZERO
            - `Dear {customername},`
            - 
                
                `Your Volt Money credit line account has been expired.` 
                
                `To avoid penal charges and portfolio sell-off please settle your outstanding amount via Volt Money app.`
                
                `App link: [https://voltm.app.link/get_volt_money](https://voltm.app.link/get_volt_money)`
                
                `If you have already paid, please ignore this message.`
                
            
            `Warm regards,`
            
            `{Partner name}`
            
    - Pagination [50 records per page]
- Tab and page deep link [All platform (web and android)]

## User stories / User flow

As a user, when I access the completed application page:

- I should be able to view a list of all customers, including those in shortfall, interest details with status and those pending renewal with status.
- By default, the page should display the list of all customers.
- I should have the option to navigate to different tabs to view specific subsets of customers, such as those in shortfall, their interest details, or those pending renewal.
- The total count of customers should be displayed on each tab.
- When total count of customer is ZERO, i.e Completed application count is ZERO than Tab should not be visible. just show empty page with nudge and CTA to add new customer.
- When accessing each tab, if the total count of customers is zero:
    - Display a message indicating that there are no customers in the selected category.
    - Provide educational information about interest, renewal, or shortfall to help me understand the significance of these aspects.
- Upon selecting a tab, the relevant information should be presented in a table format.
- I should be able to search for customers within the selected tab. If no matching customer is found, a "Customer not found" message should be displayed.
- Clicking on a customer's account should allow me to access their details.
- Each row in the table should include a CTA button to send a WhatsApp message or share the app link with the customer.
- When choosing to share on WhatsApp, the predefined message should be tailored to the specific use case. For example, if sharing from the shortfall tab, the message content should reflect the shortfall details.
    - How to insert variable in message?
- When receiving any communication from Volt regarding shortfall, interest, or renewal, clicking on the CTA to check the list of customers should redirect the me  to relevant page and TAB.
- Selected tab state should persist after reloading the page.

## Requirements

Pagination, search filter requirements should work for all table on dashboard : https://docs.google.com/spreadsheets/d/1313xScBTFpgBOursjFyTxGOxaH8NVm9qrWUh9IlFpgA/edit?usp=sharing

- Sub nav bar on completed application nav
    - All customer
    - Interest due
    - Shortfall
    - Loan expiring
- Tab to show category of customers with count
    - Category:
        - All
        - Interest due/overdue
        - Renewal pending
        - Shortfall
- Table Attributes of each category
    - All customer :
        - Filter: Active, closed
        - Pagination [50 records per page]
    - Interest due/overdue:
        - How interest is calculated → Open is modal
        - Sorting by status [Overdue → Due]
        
        | **Attribute name** | **Sample** | **Display on table** | **Display on card(mobile)** | **Display on drawer/bottom sheet** |  |  |
        | --- | --- | --- | --- | --- | --- | --- |
        | Name | Ranjan kumar singh | Y | Y | Y |  |  |
        | Phone | 7980565882 | Y | Y | Y |  |  |
        | Due amount
        - Interest due
        - Charges due | ₹2,000 | Y | N | Y |  |  |
        | Mandate status | **Registered** 
        - Auto-debit on : 2 Aug 2024
        **Not registered**
        - Pay manually | Y | N | Y |  |  |
        | Presentation status | Success, bounced  | Y | N | N |  |  |
        | Due on | 2 Aug 2024 | Y | Y | Y |  |  |
        | Status | Due, Overdue | Y | Y | Y |  |  |
        | Action | View details, View as client, Share with client | Y | Y | Y |  |  |
        | Email | ranjan.singh@voltmoney.in | N | N | Y |  |  |
        | Principal outstanding | ₹190,000 | N | N | Y |  |  |
        | Interest due | ₹1,000 |  |  | Y |  |  |
        | Charges due | ₹1,000 | Y | N | Y |  |  |
        |  |  | Y | N | Y |  |  |
        | Lender name |  | N | N | Y |  |  |
        | Total due | ₹2100 | Y | Y | Y |  |  |
        | Interest rate | 11.49% | N | N | Y |  |  |
        | Download SOA |  |  |  | Y |  |  |
    - Renewal pending:
        - Education: Benefits of renewal, what if i do not renew
        - Sorting: Customer who are nearest to renewal date
        - CTA TEXT based  on expiry date
            - Renewal due in 31- 0 days and outstanding is 0: Renew now
            - Renewal due in 31- 0 days and outstanding is not 0: Renew now
            - Expired and outstanding is 0: Reopen loan
            - Expired and outstanding is not 0: Repay now
        
        | **Attribute name** | **Sample** | Display on table | Display on card | Display on drawer/bottom sheet |
        | --- | --- | --- | --- | --- |
        | Name | Ranjan kumar singh | Y | Y | Y |
        | Phone | 7980565882 | Y | Y | Y |
        | Total credit limit | ₹1,00,000 | Y | Y | Y |
        | Available credit limit | ₹90,000 | Y | N | Y |
        | Total outstanding | ₹10,000 | Y | Y | Y |
        | Renewal due date | 1 Aug 2024 | Y | Y | Y |
        | Clear due by | 7 May 2024 | Y | Y | Y |
        | Status | Renewal pending, Renewal in progress, Expired,  | Y | Y | Y |
        | Action | View details, View as client, Share with client | Y | Y | Y |
        | Email | ranjan.singh@voltmoney.in | N | N | Y |
        | Interest rate | 11.04% | N | N | Y |
        | Created date | 1 Aug 2023 |  |  |  |
        | Download SOA |  |  |  | Y |
        | Download holding statement |  |  |  | Y |
        | Lender name |  |  |  | Y |
    - Shortfall:
        - Make sure the shortfall is displayed on the day of issue
    - What is shortfall ⇒ open in modal
        
        
        | **Attribute name** | **Sample** | Display on table | Display on card | Display on drawer/bottom sheet |
        | --- | --- | --- | --- | --- |
        | Name | Ranjan kumar singh | Y | Y | Y |
        | Phone | 7980565882 | Y | Y | Y |
        | Revised credit limit | ₹80,000 | Y | Y | Y |
        | Principal Outstanding amount | ₹90,000 | Y | N | Y |
        | Shortfall amount | ₹10,000 | Y | Y | Y |
        | Meet shortfall by | 2 Aug 2024 | Y | Y | Y |
        | Action | View details, View as client, Share with client | Y | Y | Y |
        | Email | ranjan.singh@voltmoney.in | N | N | Y |
        | Download holding statement |  | N | N | Y |
        | Lender name |  |  |  | Y |

---

# **Design**

[https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/Partner-flow?node-id=3307-32471&t=AERXllkrC5p0FMw5-4](https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/Partner-flow?node-id=3307-32471&t=AERXllkrC5p0FMw5-4)

---

# **Analytics**

- Amplitude events
    - ALL_CUSTOMER_TAB_CLICKED
    - INTEREST_DUE_TAB_CLICKED
    - SHORTFALL_TAB_CLICKED
    - RENEWAL_DUE_TAB_CLICKED

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

- On interest table, we are showing total due as a sum of Interest due and charges due. For TATA user has to pay interest and charges and but for BAJAJ user only need to pay interest

## Meeting notes