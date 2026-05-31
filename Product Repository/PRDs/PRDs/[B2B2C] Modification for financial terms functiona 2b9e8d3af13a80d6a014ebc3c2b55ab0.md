# [B2B2C] Modification for financial terms  functionality for partners

: Ameya Aglawe
Created time: November 28, 2025 3:44 PM
Status: In progress
Last edited: March 17, 2026 11:55 AM

# **What problem are we solving?**

---

- Business partners (MFDs, Brokers, CAs) frequently request changes on financial terms such as PF, ROI, Margin Pledge charges, and AMC based on customer negotiations and other factors.
- We currently receive ~170 such requests every month. These are manually processed by the sales team through admin actions, consuming bandwidth and increasing the risk of manual errors. These manual errors directly impact partner payout calculations.
- Around 10% of these requests result in increased business impact for Volt (e.g., partners increasing any financial term above the base value), but we are not fully leveraging this because the process is manual and reactive.
- Most partners are not aware that such financial term modifications are possible, leading to missed business opportunities

# **How do we measure success?**

---

- Increase in average number of application per partner
- Increase in average revenue per application per partner
- Financial term modification actions increase by 200%.
- Manual errors related to financial term updates drop to 0.
- Unique MFDs making financial term adjustments increase by 100%.
- Monthly revenue uplift driven by partner negotiations increases by 50%.

# **How are others solving this problem?**

---

- We reviewed flows for various broker dashboard & lending platforms like AngleOne and IDFC PL agent dashboard
    
    ![AngleOne](%5BB2B2C%5D%20Modification%20for%20financial%20terms%20functiona/Screenshot_2025-12-05_at_11.40.01_AM.png)
    
    AngleOne
    
    ![AngleOne](%5BB2B2C%5D%20Modification%20for%20financial%20terms%20functiona/Screenshot_2025-12-05_at_11.40.43_AM.png)
    
    AngleOne
    
    ![IDFC PL ](%5BB2B2C%5D%20Modification%20for%20financial%20terms%20functiona/image.png)
    
    IDFC PL 
    

# **What is the solution?**

---

## Requirements overview

- Provide partners the ability to modify financial terms for their clients directly from the parter dashboard
- Enable PF waive-offs for self-registration journeys for partners (this will be used for driving activations)
- Enable sales team and business team to modify and override terms beyonds the limits available for partners

## Requirements

- Touch points for partners for terms modification
    - For modifying
        - Their partner account settings page *(will be picked up in phase 2)*
        - During customer loan application initiation:
            - While registering a new customer directly
            - Through registering customer in the check eligibility in 15s flow
            - Before sharing the application link with the customer *(will be picked up in phase 2)*
            - From pending applications
                - There will be a “Manage terms” CTA in the pending applications actions
                - Once the users taps on the CTA, the manage terms modal would directly open up
                - User can change PF/ROI and tap on “Confirm Loan Terms”
                - On tapping on the “Confirm Loan Terms” the modal closes and the toast with messaging shows up in the button
                - Please note the “Manage Loan Terms” CTA should only be visible if the application’s agreement step has not started
        - Below are the financial terms and modification limits available to partners:
            
            
            | Financial term | Minimum  | Maximum |
            | --- | --- | --- |
            | PF | Rs 999 | Rs 10,000 |
            | ROI | 9.99% | 14% |
            | Margin pledge | Rs 499 | Rs 10000 |
            | AMC | Rs 999 | Rs 10000 |
    - After modification
        - Partners can view PF, ROI, MP, and AMC for each customer at a customer-specific level
- Admin action
    - Use case
        - To be used when terms needs to be exceeded beyond the limits available for partners through PD
        - The terms can be modified only before the agreement generation for the main application (the pre-agreement step).
        - For only DSP applications
    - 2 separate admin action available to sales and business teams
        - Sales Team
            - Input
                - Application ID
                - Financial term
                    
                    
                    | Financial term | Minimum | Maximum |
                    | --- | --- | --- |
                    | PF | Rs 0 | - |
                    | ROI | 9.99% | 14% |
                    | Commercial split for PF (Volt share) | 0 | 50 |
                    | Commercial split for ROI (Volt share) | 0 | 50 |
                - Value
                - Type
                    - SELF-LINE
                    - NON SELF-LINE
                - Remarks
            - Note -
                - PF & ROI can only be modified before agreement step initiation
                - Commercial split can be modified at any stage - during the application cycle and even after the application is completed
        - Business Team (approval based - TBD with tech team)
            - Input
                - Application ID
                - Remarks
                - Financial term
                    
                    
                    | Financial term | Minimum | Maximum |
                    | --- | --- | --- |
                    | Trail | 0 | 0.65 |
            - Note -
                - The trail can be modified at any stage—during the application cycle and even after the application is completed
- System
    - Flags
        - Partner-level: Controls which partners get access to the financial terms modification feature. [blacklisting of partners for which feature should not be visible]
        - Financial-parameter level: Controls which specific financial parameters (PF, ROI, MP, AMC) a partner is allowed to modify once the feature is enabled
    - Backfilling
        - The entire negotiations sheet should be back filled into the DB
        - Hence the entire payout calculation should now be driven by DB
    - APR calculation for each application
    - Appsmith
        - Adding visibility for the following in appsmith in the application view
            - PF
            - ROI
            - MP
            - AMC
- Data storage
    - Term modifications
        - Modification ID
        - Applied on
            - Platform (Volt/Other)
            - Partner account
            - Customer account
        - Account ID (Platform/Partner/Customer)
        - Modification type
            - Self line
            - Non self line
        - Modification term
            - PF
            - ROI
            - MP
            - AMC
            - Commercial Split
            - Trail
        - Current terms
            
            ```jsx
            {
            
                "PF" : 100, 
                "ROI" : 10.5,
                "MP" : 599, 
                "AMC" : 1500,
                "commercialSplit": 20, 
                "trail" : 0.5
            
            }
            ```
            
        - Updated terms
            
            ```jsx
            {
            
                "PF" : 200, 
                "ROI" : 10.5,
                "MP" : 999, 
                "AMC" : 400,
                "commercialSplit": 30, 
                 "trail" : 0.5
            }
            ```
            
        - Created on
        - Source
            - Admin action
            - System
            - BE (manual update/DB override)
- Payout calculations
    - The entire payout calculations should be driven by the internally stored values of various financial terms in the DB (migrate from the negotiations sheet entirely)

## User stories / User flow

- Will mention once designs are ready

# **Design**

---

- https://www.figma.com/design/zkvrgVzPP83L4LwMKjBF5r/MFD-partner-flow?node-id=6859-1682&t=BEo7aLtjyiW4WdO7-4

# **Analytics**

---

- A dashboard which populates the loan accounts which breach the APR calculation beyond 20%
    - loan account ID
    - APR
    - Processing fees
    - AMC
    - Total interest charged
    - Credit limit
- Number of modification per MFD
- Number of unique MFDs using the modification feature

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

- In case MFD did not do, should be compatible