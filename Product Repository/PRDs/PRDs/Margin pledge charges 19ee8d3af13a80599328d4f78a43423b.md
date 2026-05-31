# Margin pledge charges

: Vaibhav Arora
Created time: February 18, 2025 5:49 AM
Status: Pending Review
Last edited: June 19, 2025 4:24 PM

# **What problem are we solving?**

Currently, DSP Finance offers a maximum sanction limit of ₹2,00,00,000, allowing users to pledge collaterals post-account opening up to this limit (calculated as NAV × LTV × Units) to access credit.

However, this leads to cost implications such as lien marking charges, ongoing tech maintenance, and operational overheads, which are not being recovered from users today. To address this and improve monetisation, we plan to introduce pledge invocation charges, applicable when users pledge additional securities to increase their credit limit.

---

- Increased IRR (Internal rate of return) and corresponding NIM (net interest margin) from users at an average loan account level

---

# **How are others solving this problem?**

TCL and BFL have a concept of sanctioned limit, whenever sanctioned limit of the loan account is updated, enhancement charges are applied to the loan account (LSP - Volt) places the charge

---

# **What is the solution?**

We will be applying margin pledge charges (Additional pledge charges) on the user’s loan account. Margin pledge charges will be applied. The same will be added in the product construct.

## Requirements overview (optional)

## User stories / User flow

## Requirements

Following are requirements:

- **Amount**:
    - Additional pledge charges can be a fixed amount, or a percentage of the pledge amount (additional credit) added to the user’s loan account and should be configurable.
    - Additional pledge charges will only be applied from the second lodgement onwards on the loan account, Business team may choose to allow one free lodgement for every month (For now the same can be handled via reversals)
    - Additional pledge charges charges type (percentage or absolute) and the corresponding values (what percentage or what value) should be configurable at a sourcing channel level (product construct)
    - GST of 18% will be applied on top of the charge amount applied to the user’s loan account
- **Application**:
    - Additional pledge charges should not be applied if the user is doing an additional pledge for covering shortfall, that is if the account is in “Regulatory shortfall” and the user does an additional pledge, no charges will be applied to the user’s loan account
    - Additional pledge charges will be applied on user initiated requests, that is for manual lodgements requests raised by the operations team, there will be no additional pledge charge application charge applied on the user’s loan account
    
    (Command centre should support application of the corresponding charge to the user’s loan account)
    - In case the operations team wants to apply charges for a particular lodgement, they should apply it manually via add charge maker on the command centre
    - Charge application will be done post lodgement (to accurately track status and amount of lodgement before applying the charge). As soon as the lodgement request is processed (STP lodgement / Manual) the approval task for the corresponding charge will get created for the loan account
    - Charge approval for additional pledge charges:
        
        <aside>
        ⭐
        
        **Name:**
        
        Charges posting approval
        
        **Request details section:**
        
        Approval status - Task approval status
        
        Request ID - Charge transaction ID
        
        Charge type
        
        Amount
        
        GST
        Request reference ID: {{Add collateral request}}
        
        Sub status
        
        Maker name
        
        Maker remarks
        
        Maker created on
        
        Task description
        
        </aside>
        
- **Collection**:
    - Additional pledge charges will be collected via repayments made to the user’s loan account according to the predefined apportionment strategy:
    
    Interest overdue → Charges overdue → Interest due → Charges due → Principal → Excess
    - Additional pledge charges will not be collected from the following withdrawal
- **Reporting**:
    - Additional pledge charges will be reported, as a part of the total outstanding charges, like all other outstanding charges
- Communication:
    - Currently communications are not built for charge application (leaving this out of scope for the current requirement, communication for charges will be picked up as a separate requirement) - Communications to both the LSP (Volt/Groww/Indmoney) and the end customer via webhooks/email/sms.

---

# **Design**

NA

---

# **Analytics**

- Number of additional pledges post loan account creation
- Number of additional pledge charges posted to loan account
- Number of additional pledge charges application skipped due to the following reason:
    - Lodgement via command centre
    - Account in shortfall

---

# **Timeline/Release Planning**

- PRD kickoff 18 Feb 2025
- Development start: 18 Feb 2025
- Development completion: 20 Feb 2025
- Release to production (for Volt LSP): 21 Feb 2025

---

# **Go to market**

- Margin pledge charges

## Marketing

## Ops & Sales training

- Training scheduled for 20 Feb 2025

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - Set up of charge on Finflux UAT and Production
    - Test charge application on UAT on Finflux
    - DSP operations SOP update for charge
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