# [TL] Shortfall handling

: Ameya Aglawe
Created time: August 5, 2025 8:43 AM
Status: Pending Review
Last edited: October 1, 2025 1:26 PM

# **What problem are we solving?**

---

- We want to implement a robust mechanism to handle shortfall scenarios in term loans. Unlike OD products, term loans involve an outstanding principal amount, which increases the likelihood of shortfalls. This makes it essential to build an efficient and well-defined shortfall handling process specifically for term loans

# **How do we measure success?**

---

- 100% accuracy in shortfall amount calculation across all loan accounts
- 100% accuracy in shortfall ageing logic for timely NPA recognition
- 100% delivery rate of shortfall communications to customers and successful web hook triggers for all applicable accounts

# **How are others solving this problem?**

---

**Industry Best Practices:**

1. **FIFO (First In, First Out)** - Most banks use chronological order for tranche settlement
2. **Waterfall Approach** - Sequential settlement from highest to lowest priority dues
3. **Pro-rata Allocation** - Some institutions distribute payments proportionally across all dues
4. **Hybrid Models** - Combination of FIFO and waterfall based on due categories

**Competitive Analysis:**

- **HDFC Bank**: Uses strict FIFO with interest-first allocation
- **ICICI Bank**: Implements waterfall approach with overdue prioritisation
- **Axis Bank**: Employs hybrid model with customer choice options
- **SBI**: Follows RBI guidelines with systematic allocation rules

# **What is the solution?**

## Requirements overview (optional)

- User can cover for shortfall in the following ways -
    - Covering for shortfall amount by pledging more units (will work exactly like the OD product where user have to do a margin pledge)
    - Repaying the shortfall amount

- Implement an automated shortfall handling system that:
    1. **Calculates shortfall amounts** using the formula: `Shortfall Amount = min(DP,SL) - Sum of Principles oustanding (all tranches) + Excess (loan)` 
    2. **Applies systematic apportionment** based on FIFO logic wherein EMI overdues are settled first and then dues are settled following IPC logic 
    3. **Maintains consistent ageing** aligned with existing OD product methodology

## User stories / User flow

## Requirements

---

**Functional Requirements:**

- **Shortfall Calculation Function**
    - Formula: `Shortfall Amount = min(DP,SL) - Sum of Principles outstanding (all tranches) + Excess(loan)`
- **Apportionment Logic**
    - Applies systematic apportionment based on FIFO logic of disbursement wherein EMI overdues are settled first and then dues are settled following IPC logic
    - Across tranches the shortfall repayment would be settled in the following order : Interest Overdue → Principal Overdue → Interest Due → Principal Due → Charges Overdue → Charges Due → Excess
- **Ageing Logic**
    - Follow same methodology as OD product
    - Please find detailed OD shortfall logic [here](https://docs.google.com/spreadsheets/d/1Y_UHnHrbdYzQBZjIfYvO9zXVqszU2uUxPnI9QbHH58Q/edit?usp=sharing).
- **Shortfall repayment**
    - `Shortfall Amount = min(DP,SL) - Sum of Principles outstanding (all tranches) + Excess(loan)`
    - No dues
        - Minimum shortfall repayment amount = Shortfall amount
    - Dues
        - Principal due at loan level < Shortfall amount
            - Minimum shortfall repayment amount = Interest due (at loan level) + shortfall amount
        - Principal due at loan level > Shortfall amount
            - Minimum shortfall repayment amount calculation
                - Stack rank the tranches based on FIFO
                - Find tranche where the aggregate principal due including dues before the tranche is greater than the shortfall amount
                - Minimum shortfall repayment amount = Summation Interest (up till that tranche) + shortfall amount
    - Edge case -
        - In cases where the loan is in shortfall with either “No dues” or "Principal due at loan level < Shortfall amount” then a part of the amount repaid by the customer to cover shortfall will be apportioned against excess, hence we need to ensure that we remove such loan account from the excess clearance job
- **Communications (will be picked up separately)**
    - The comms and the web hooks (for LSPs) will be triggered same as the OD product
        - Shortfall
        - Sell off

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