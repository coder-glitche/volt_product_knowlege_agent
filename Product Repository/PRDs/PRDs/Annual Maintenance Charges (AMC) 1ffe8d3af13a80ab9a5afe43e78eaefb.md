# Annual Maintenance Charges (AMC)

: Ranjan kumar Singh
Created time: May 26, 2025 6:25 PM
Status: In progress
Last edited: February 19, 2026 7:12 PM
Owner: Lalit Bihani

# **What problem are we solving?**

**DSP offers a credit line facility to users for a tenure of 3 years.** Maintaining this credit line involves ongoing costs including customer servicing, technology infrastructure, portfolio monitoring, and operational overheads.

To ensure the long-term sustainability of the offering and continue delivering high-quality service, **we propose introducing an Annual Maintenance Charge (AMC)**. This will serve as a recurring revenue stream to offset the costs associated with account maintenance and user support throughout the lifecycle of the credit line.

---

# **How are others solving this problem?**

—INTERNAL—

---

# **What is the solution?**

We will be applying AMC on the user’s loan account. AMC will be applied at the end of every year(should be calculated based on account opening date). The same will be added in the product construct.

AMC is Non-contingent charge: will be charged unconditionally whether there is 100%  utilization also. 

## Requirements overview (optional)

## User stories / User flow

## Requirements

Following are requirements:

- **KFS and Agreement:**
    - AMC charges to be included in the KFS and the loan agreement.
    - AMC charges will the part of APR calculation.
        - Note: AMC for first year is included in processing fees
        - In KFS Annual maintenance charges field are their but Value is mentioned as NIL
        - Need to add frequency in Agreement (Annual rec.)
        - APR Calculation logic:
            
            APR =[{(Processing fees incl. GST + AMC + Total interest charged)/Credit limit}/Tenure in days]*365*100
            
            AMC = [AMC Amount incl. GST * (Loan tenure in Year - 1)]
            
    - AMC will apply for only new customer from the date of AMC go-live
    - **Changes in Computation of APR section of Agreement**
        
        
        | Parameter |  |
        | --- | --- |
        | **Fee/ Charges payable (including GST) (SI no. 8 of
        the KFS - Part 1)** | Processing fee + Insurance charges  + Valuation fees  + Any other  + [AMC amount * Tenure in year -1] |
        | Payable to DSP Finance Pvt. Ltd. (SI no. 8A of the KFS - Part 1 | Processing fee + Insurance charges  + Valuation fees  + Any other  + [AMC amount * Tenure in year -1] |
    - **Repayment Schedule**
        - We need to include the AMC amount in the repayment schedule in instalment amt
        - Calculate the 12 Month and 24 month from the month of account creation and add AMC charges in instalment amt
            - If account opening date is 07-Jul-2025 then first AMC will apply on Month end of the Jul and AMC amount (999) will be added under the repayment date of 07 Aug-2026 and similarly second AMC amount will be collected on 07- Aug-2027
- **AMC on Loan application UI:**
    - LSP to show the AMC charges on loan application journey (loan offer page)
- **Who will calculate and send AMC charges**
    - DSP to update the **generate loan contract** API and **KFS v2** - (Include annualMaintenanceFee as key in feeDetails)
    - LSPs to send the AMC charges in generate loan contract API and (KFS v2 API - only for PhonePe)
        
        **Update Payload Structure:**
        
        ```json
        
        {
          "feeDetails": {
            "processingFee": 1299.00,
            "annualMaintenanceFee": 999.00,
            "enhanceLimitFee": 499,
            "renewalFee": 1899.00,
            "marginPledgeFee": 599.00
          }
        }
        ```
        
    - Min max value of the AMC to be configured at sourcing channel level in AWS app config
    - If LSP’s do not pass the AMC charges, default AMC Amount will be applied (MIN value)
- **What will be the AMC Amount?**
    - AMC can be a absolute amount or percentage, added to the user’s loan account and should be configurable.
        - *Logic of percentage based charges calculation logic is pending on business*
    - AMC charges type (percentage or absolute) and the corresponding values (what percentage or what value) should be configurable at a sourcing channel level and customer level(product construct)
    - GST of 18% will be applied on top of the charge amount applied to the user’s loan account
- **How and when to Apply AMC?**
    - AMC for first year is already included in processing fee
    - AMC for second year will be applied in month end of 13th month with the billing cycle
    - AMC for third year will be applied in month end of 25th month with the billing cycle
        - **Example and visualisation of AMC application:**
            
            <aside>
            💡
            
            ### AMC Application Timeline
            
            ## **Scenario Details**
            
            - **Customer Name**: Atul Singh
            - **Loan Account Opening Date**: January 15, 2025
            - **AMC Amount**: ₹999 + GST (18%) = ₹1,178.82
            - **Loan Tenure**: 3 years
            - **Total AMC for 3 year loan tenure:** ₹1,178.82 * (Tenure in year - 1) = 2357.64
            
            ---
            
            ## **Year-by-Year AMC Application**
            
            ### **Year 1 (2025) - No Separate AMC Charge**
            
            - **Period**: January 15, 2025 to January 14, 2026
            - **AMC Status**: **Already included in processing fees**
            - **Action Required**: None
            - **Customer Impact**: No additional charges
            
            **Customer Communication on UI & agreement:**
            
            > "Your first-year maintenance charges are included in the processing fees. No separate AMC will be applied during your first year."
            > 
            
            ---
            
            ### **Year 2 (2026) - First AMC Application**
            
            ### **Calculation Logic:**
            
            - Account opened: January 15, 2025
            - 13th month: January 2026
            - Application timing: **End of January 2026**
            
            ### **Timeline:**
            
            - **AMC Application Date**: January 31, 2026
            - **Due Date for Payment**: February 1, 2026 (7 days grace period)
            - **Auto-debit Attempt**: February 7, 2026
            
            ---
            
            ### **Year 3 (2027) - Second AMC Application**
            
            ### **Calculation Logic:**
            
            - Account opened: January 15, 2025
            - 25th month: January 2027
            - Application timing: **End of January 2027**
            
            ### **Timeline:**
            
            - **AMC Application Date**: January 31, 2027
            - **Due Date for Payment**: February 1, 2027
            - **Auto-debit Attempt**: February 7, 2027
            
            ---
            
            ---
            
            ## **Collection Scenarios**
            
            ### **Scenario 1: Successful Auto-debit**
            
            ```
            January 31, 2026: AMC ₹1,178.82 applied
            February 7, 2026: Auto-debit successful
            Result: AMC collected
            ```
            
            ### **Scenario 2: Failed Auto-debit**
            
            ```
            January 31, 2026: AMC ₹1,178.82 applied
            February 7, 2026: Auto-debit failed (insufficient funds)
            Result: AMC remains in outstanding balance
            Collection: Will be adjusted against next repayment or mandate attemp
            ```
            
            ### **Scenario 3: Customer in Default (DPD)**
            
            ```
            January 31, 2026: AMC ₹1,178.82 applied
            February 15, 2026: Customer in default, no repayments
            Result: Securities worth ₹1,178.82 will be sold to recover AMC
            ```
            
            ---
            
            ## **APR Impact Example**
            
            - APR Calculation:
                
                APR =[{(Processing fees incl. GST + AMC + Total interest charged)/Credit limit}/Tenure in days]*365*100
                
                AMC = [AMC Amount incl. GST * (Loan tenure in Year - 1)]
                
            
            ### **For a ₹5 Lakh Loan at 12% Interest**
            
            ```
            Base Interest Rate: 12.00%
            Processing Fee Impact: +0.35%
            AMC Impact (₹999 + GST × 2 years): +0.40%
            Total APR: 12.75%
            
            Annual Cost Breakdown:
            - Interest: ₹60,000
            - AMC (Years 2&3): ₹1,178.82 each
            - Total Additional Cost: ₹2,357.64 over 3 years
            
            ```
            
            </aside>
            
    - AMC charges refund logic: When AMC is charged and if customer want to close his account within (X) days then we need to refund (X)% of AMC
        - No waiver of AMC once applied. Waivers shall be processed on an ad-hoc basis based on customer escalation.
    - In case the operations team wants to apply charges (If system failed to apply charges or on demand), they should apply it manually via add charge maker on the command centre
    - Their will be no Charge approval (maker checker) for AMC charges
    - Application of AMC will be CRON based, Finflux or Fenix to run a CRON every month end and identify the user account who are eligible for applying the AMC charges
        - Action items: Need to discuss the requirement with Finflux to check the feasibility
- **How to collect AMC?**
    - AMC will be collected via ~~next withdrawal~~, repayments or mandate made to the user’s loan account according to the predefined apportionment strategy:
    
    Interest overdue → Charges overdue → Interest due → Charges due → Principal → Excess
    - In case of  bounce, bounce charges will applied.

- **APR Calculation:**
    
    
    APR =[{(Processing fees incl. GST + AMC + Total interest charged)/Credit limit}/Tenure in days]*365*100
    
    AMC = [AMC Amount incl. GST * (Loan tenure in Year - 1)]
    
- **Reporting requirement**:
    - AMC will be reported, as a part of the total outstanding charges, like all other outstanding charges
- **Accounting:**
    - same as PF
- **Communication to users:**
    - Currently in agreement AMC is mentioned as ZERO, we need to inform existing user about the change in charges.
    - Inform user when AMC is applied with Auto-debit date
        
        **When AMC is applied:**
        
        Dear [Name], Annual Maintenance Charges of ₹299 have been applied to your loan account. This will be auto-debited on [Due Date]. No action needed.
        

---

# **Design**

NA

---

# **Analytics**

- Revenue contribution
- Number of users for whom AMC was applied
- AMC refunded/reversed

---

# **Timeline/Release Planning**

- PRD kickoff 27 May 2025

---

# **Go to market**

- PRD Sign-off from stake holder
- Communication to users
- Communication to LSP
- Training about the AMC charges to sales and ops team

## Marketing

## Ops & Sales training

- TBD

## Frequently asked questions (FAQs)

---

# **Action items / checklist**

[](data:image/png;base64,iVBORw0KGgoAAAANSUhEUgAAAEgAAABICAYAAABV7bNHAAAA1ElEQVR4Ae3bMQ4BURSFYY2xBuwQ7BIkTGxFRj9Oo9RdkXn5TvL3L19u+2ZmZmZmZhVbpH26pFcaJ9IrndMudb/CWadHGiden1bll9MIzqd79SUd0thY20qga4NA50qgoUGgoRJo/NL/V/N+QIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIECBAgQIAAAQIEyFeEZyXQpUGgUyXQrkGgTSVQl/qGcG5pnkq3Sn0jOMv0k3Vpm05pmNjfsGPalFyOmZmZmdkbSS9cKbtzhxMAAAAASUVORK5CYII=)

- [ ]  Product
    - Discuss requirement with Finflux for implementation of AMC
    - Set up of charge on Finflux UAT and Production
    - Test charge application on UAT on Finflux
    - DSP operations SOP update for charge
- [ ]  Business
    - [ ]  Do we need to inform LSPs when AMC is applied on user loan account? Close with Keyur
    - [ ]  Keyur and Nakesh to co-ordinate with LSPs for the implementation of AMC
    - [ ]  Nishant to share waive-off an refund logic
    - [ ]  Nishant to confirm the requirement of accounting for AMC
    - [ ]  Min max value of the AMC to be configured at sourcing channel level in AWS app config
    - [ ]  Keyur to share the requirement and provide sign-off on implementation of AMC with LSPs like INDMoney, Groww, phonePe, ETMONEY, YENMO etc
- [ ]  Design
    - [ ]  AMC on Volt Loan offer page

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

**AMC amount:** 

- Flat or % of [min of DP and SL] floor of min 500
    - LSP to send AMC

When to apply:

- First year AMC is included in PF
- Apply AMC from second year onwards : 13th month

- New user or existing users?
    - Existing + new

Collection: 

- Disbursal + Mandate or sell -off

APR calculation:

- Will be part of APR

Comms: 

- Inform cx about the charges change

Open point

- % calculation
- AMC refund logic

```
Dear Rahul,

Your Annual Maintenance Charge of ₹1,178.82 (₹999 + GST) will be
applied to your loan account ending xxxx on January 31, 2026.

This amount will be auto-debited from your registered bank account
ending xxxx on February 15, 2026.

This charge covers:
• Account maintenance and servicing
• Technology infrastructure costs
• Customer support services
• Portfolio monitoring

No action required from your side.

Questions? Call 1800-xxx-xxxx or visit our app.

Best regards,
DSP Team

```