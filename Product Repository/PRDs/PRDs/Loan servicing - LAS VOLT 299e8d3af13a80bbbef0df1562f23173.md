# Loan servicing - LAS VOLT

: Ranjan kumar Singh
Created time: October 27, 2025 1:06 PM
Status: Not started
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

Stocks collateral management at Volt end:

In scope

1. Remove collateral 
2. Remove collateral status tracking
3. Lien removal communications

Out of scope:

1. Add collateral

---

# **How do we measure success?**

Lien removal success metrics:

1. Accuracy in showing pledged collateral details
2. Accuracy in removable collateral validations
3. Accuracy in life cycle tracking 
4. Accuracy in data points like DP post lien removal is requested
5. TAT from request to completed 
6. Customer complaints (Ticket volume)

---

# **How are others solving this problem?**

---

# **What is the solution?**

## Requirements overview (optional)

## User stories / User flow

## Requirements

# **Account opening:**

Account opening state Management:

In LAMF, customers are allowed to place a disbursal request immediately after the loan is created, based on the Expected DP. The request is queued until the loan reaches Approved Not Disbursed. Since pledging and lodgement together take ~10 minutes on average, there is no negative user impact on disbursal TAT.

However, in LAS, pledging confirmation to lodgement can take 3–4 days. 

Approaches for Disbursal Handling in LAS After Account Opening:

| **Approach** | **Description** | **Pros** | **Cons** |
| --- | --- | --- | --- |
| **1. Block disbursal until lodgement completes** | User cannot place a disbursal request until collateral lodgement is completed. Show “Account Opening in Progress” along with completion TAT status on dashboard. | - Clear expectations, no confusion- Eliminates DP variance-related rejection

- Ops load reduced (no cancellations/adjustments) | - User cannot initiate early disbursal- Perceived delay in access to funds

- May lead to drop-offs for urgent loan needs
- Requires Design and tech effort to handle the status on Home screen specifically for LAS |
| **2. Auto-trigger disbursal request for full limit** | Automatically places disbursal request based on Expected DP, with disclaimer that actual amount may vary depending on market movement. [Similar to INDMoney] | - No drop-off

- No user action needed

- User feels disbursal is progressing in background | - If Actual DP drops, disbursal will be rejected → poor experience

- Higher operational exceptions and Support ticket

- Risk of negative sentiment if promised amount changes

- Requires additional Design/Tech effort  |
| **3. Allow user to place disbursal request for custom amount immediately after account opening** | User can choose any amount up to Expected DP, with disclaimers about DP variance and possible amount change post lodgement along with Expected completion TAT of 3-4 days | - Flexibility to user

- Reduces rejection risk (user may request lower amount)

- User feels in control of disbursal timing | - Actual disbursal may still reduce → confusion/complaints

- User may miss the disclaimer about the DP change and TAT

- Still triggers exception handling if DP drops |

Status:

1. **Pending disbursal approval:** Loan account is created
2. **Pending lodgement:** Credit is Active at lender end and Lodgement is pending
3. **Approved not disbursed:** Account opened → lodgement completed → 1st disbursal pending
4. **Active**
5. **Pending closure**
6. **Closed**

Sub status:

- Frozen

# Principal Repayment

### **Entry points for principal repayment:**

- Repay CTA on Dashboard page: No change

### **Flexi Pay page:**

- No change

### **Confirm & Pay page:**

- No change

# Shortfall

1. Shortfall notification on home screen
2. Shortfall Landing page
3. Shortfall repayment
4. Shortfall education
5. Shortfall reminder comms
6. Shortfall FAQs
    
    
    | **Question** | **Answer** |
    | --- | --- |
    | What is shortfall? | Shortfall happens when credit limit drops below the outstanding amount.Credit limit may drop due to fall in market value of pledged portfolio. |
    | How can I address or meet a shortfall? | Available options to address shortfall:**1. Repay shortfall amount**    You can repay via the Volt Money app using UPI,  net banking, or debit card**2. Pledge additional funds**     Pledge additional to meet shortfall on Volt Money app - **Coming soon**For more help, please reach out to us at {{Customer_contact_number}} or write us at support@voltmoney.in |
    | How to avoid shortfall? | It is advisable to utilize upto 95% of your total credit limit.This will ensure that a shortfall will occur only when your portfolio value decreases by 5%.In case of more than 95% utilisation, we recommend making a partial repayment if your portfolio value decreases due to market fluctuations. |
    | What happens if I fail to meet the shortfall? | If you fail to address the shortfall within 3 days from the date it occurred, Part of your portfolio will be sold off to recover the shortfall amount.For more help, please reach out to us at {{Customer_contact_number}} or write us at support@voltmoney.in |
    
    Open items:
    
    - At what aging sell-off will happen and for how much amount
    - What will happen if user repays the amount on the 4th Day? still portfolio will be sold-off
    - What will be the TAT for initiating the portfolio sell-off to accounting completion
        - User will be in shortfall till the accounting is completed
        - DP will be blocked once sell-off is initiated
- Price Update: 4 PM > Shortfall computation on same days > Aging 7 (6 Days due to same day computation)
- 

# Manage limit

### **Entry points to manage collateral:**

- Manage limit Nav menu

### **Manage limit landing page:**

**Components:**

1. Credit limit card: No change
2. Pledged portfolio:
    1. Mutual funds replaced with Stocks 
    2. Portfolio value: No change
    3. View details CTA: No change

### Pledged Mutual funds page:

**Components:**

1. Page header: Replace Pledged mutual funds with Pledged stocks
2. Portfolio value and available credit limit: No change
3. Pledge More CTA : Disabled 
4. Remove pledge: No change [OnClick → redirect to Remove pledge stepper page]
5. Pledge History: No change [OnClick → Redirect to Pledge history]
6. Pledged mutual funds - List
    1. Replace Pledged mutual funds with Pledged stocks
    2. Replace {{count}} MFs with {{count}} Stocks
    3. Table header 
        1. Replace Mutual funds with Stocks
        2. Table content: 
            1. Scrip name
            2. Value: [Total pledged units *  NAV]
            3. Credit limit: [Value * LTV]
    4. We need to remove filter for stocks

### Remove pledge stepper:

1. Stepper: 
    1. Replace funds with stocks
    2. Track status of your request: Content change
        1. Your request to unpledge will be shared with SDs (NSDL and CDSL). It may take them 2-3 business days to complete unpledging
    3. Change CTA text: Continue to select stocks

### Remove pledge from MFs page

1. Replace all Mutual funds text with Stocks
2. Pledged mutual funds list → Pledged stocks
    1. Stocks List components:
        1. Scrip name
        2. Limit: [Value * LTV]
        3. Funds value: [Total pledged units *  NAV]
        4. Sort table by Funds value (Higher to lower value)
    2. Actions:
        1. OnSelect scrip → Check eligible units available to remove pledge in real time → Notify when Max limit reached
        2. OnEdit scrip
            1. Show total units  → User can enter units to unpledge → Adjust Value based on unit input 
            2. Show funds value  → User can enter Value to unpledge → Adjust units based on Value input
            3. Note: Units to unpledge can’t be in decimal 
    3. Bottom data points:
        1. Selected stocks value and total units
        2. Updated credit limit
    4. Bottom CTA: No change
    
3. Validation: Summation(Units*NAV*LTV)≤ DP - TOS - AI(Accrued Interest)
    1. Allowable quantity  = [Total drawing power ] - [(Total outstanding + Accrue interest)]
        1. Example : Allowable value:  100000(DP) - [(50000 + 100)] = 49,900

### Confirm unpledge page

1. Lending partner: No change
2. Replace All MF/Mutual funds with Stocks
3. Data points:
    1. Selected portfolio[1000 out of 100000] : No change
    2. Selected credit limit : No change
    3. Updated credit limit : No change
4. Actions: 
    1. Edit: No change
    2. Info icons: No change
5. Process to remove the pledge: No change
    
    

### Pledge history page:

![WhatsApp Image 2025-11-03 at 11.00.08 (2).jpeg](Loan%20servicing%20-%20LAS%20VOLT/WhatsApp_Image_2025-11-03_at_11.00.08_(2).jpeg)

1. Listing: No change
2. Status: In progress → Approved → Completed/ Partially released/Failed

### **Remove pledge page (status tracking):**

![WhatsApp Image 2025-11-03 at 11.00.08 (1).jpeg](Loan%20servicing%20-%20LAS%20VOLT/WhatsApp_Image_2025-11-03_at_11.00.08_(1).jpeg)

1. Request details: No change
2. Request status:
    1. Replace RTA with SDs (NSDL and CDSL)
3. Replace MF/Mutual funds with stocks

# Loan details

Changes:

- ~~Pledged mutual funds Value~~ → Pledged stocks value
- Loan Type : ~~Loan against mutual funds~~  → Loan against share

![Screenshot 2025-11-06 at 1.06.14 PM.png](Loan%20servicing%20-%20LAS%20VOLT/Screenshot_2025-11-06_at_1.06.14_PM.png)

# Foreclosure

# Help and support / FAQ

Figma link: https://www.figma.com/design/P6LkjMfxq3UFY2l3JHOIUW/Profile-section?node-id=1437-7582&t=GUo3KdKZB0Qd0qNS-4

Changes:

1. No design level change in Help and support flow
2. Support Topic like Withdrawal, Repayment will be dynamically controlled based on the Product type [LAMF/LAS]
    1. We may not show few options like Renewal for LAS
3. FAQ list page → Config based on the product Type
    1. FAQ content:  
    
    [https://docs.google.com/document/d/1u2aL4cvK3TShMaxYaC0ZE1zeoNmOpmiz2pW-9tHYuho/edit?usp=sharing](https://docs.google.com/document/d/1u2aL4cvK3TShMaxYaC0ZE1zeoNmOpmiz2pW-9tHYuho/edit?usp=sharing)
    

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
    - [ ]  Close data points for collateral listing
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

Verince in DP

Pledging TAT will 2-3 days